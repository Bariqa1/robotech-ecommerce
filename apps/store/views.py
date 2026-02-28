from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Product, ContactMessage, CartItem
import qrcode
import base64
from io import BytesIO
from django.contrib.auth.forms import UserCreationForm
from .forms import UserUpdateForm, ProfileUpdateForm
from .models import Profile

# ==========================================
# المهمة 12 و 13: نموذج (Contact Us)
# ==========================================
def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message_content = request.POST.get('message')
        
        ContactMessage.objects.create(
            name=name, email=email, subject=subject, message=message_content
        )
        
        messages.success(request, 'تم استلام رسالتك وجاري معالجة الطلب بنجاح!')
        return redirect('contact_us') 
        
    return render(request, 'store/contact.html')

# ==========================================
# المهمة 14: صفحة الملف الشخصي (Profile)
# ==========================================
@login_required
def profile(request):
    # التأكد من وجود بروفايل للمستخدم
    profile_obj, created = Profile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'تم تحديث بياناتك بنجاح!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'store/profile.html', context)
# ==========================================
# المهمة 15 (الجزء الأول): صفحة الدفع (Checkout)
# ==========================================
@login_required(login_url='/login/')
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    
    total_price = sum(item.get_total_price() for item in cart_items)
    
    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'store/checkout.html', context)

# ==========================================
# المهمة 15 (الجزء الثاني): إنشاء الفاتورة مع الـ QR Code
# ==========================================
@login_required(login_url='/login/')
def generate_invoice(request):
    if request.method == 'POST':
        cart_items = CartItem.objects.filter(user=request.user)
        total_price = sum(item.get_total_price() for item in cart_items)
        company_name = "RoboTech - روبروتيك"
        
        qr_data = f"اسم الشركة: {company_name}\nالعميل: {request.user.username}\nالإجمالي: {total_price} ريال"
        
        qr = qrcode.make(qr_data)
        buffer = BytesIO()
        qr.save(buffer, format="PNG")
        
        qr_image_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
        
        context = {
            'company_name': company_name,
            'customer_name': request.user.username,
            'items': cart_items,          
            'total': total_price,     
            'qr_code': qr_image_base64,    
            'order_id': "12345",          
        }
        
        
        return render(request, 'store/invoice.html', context)
    
    return redirect('checkout')

# ==========================================
# عرض الصفحة الرئيسية (المنتجات)
# ==========================================
def home(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})

# ==========================================
# دالة إضافة المنتج للسلة
# ==========================================
@login_required(login_url='/login/')
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
        
    messages.success(request, f'تم إضافة {product.name} للسلة بنجاح!')
    return redirect('home')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'تم إنشاء الحساب بنجاح! يمكنك الآن تسجيل الدخول.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def add_review(request, product_id):
    if request.method == 'POST':
        product = Product.objects.get(id=product_id)
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        Review.objects.create(product=product, user=request.user, rating=rating, comment=comment)
        messages.success(request, 'شكراً لتقييمك!')
    return redirect('home')