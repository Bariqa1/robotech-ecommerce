from django.db import models
from django.contrib.auth.models import User

# --- 1. جداول المنتجات (RoboTech) ---
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم القسم")
    
    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="القسم")
    name = models.CharField(max_length=150, verbose_name="اسم القطعة (الروبوت/الحساس)")
    description = models.TextField(verbose_name="المواصفات التقنية")
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="السعر")
    image = models.ImageField(upload_to='products/', blank=True, null=True, verbose_name="صورة القطعة")
    
    def __str__(self):
        return self.name

# --- 2. جدول اتصل بنا (المهمة 12) ---
class ContactMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name="الاسم")
    email = models.EmailField(verbose_name="البريد الإلكتروني")
    subject = models.CharField(max_length=200, verbose_name="موضوع الرسالة")
    message = models.TextField(verbose_name="محتوى الرسالة")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="وقت الإرسال")

    def __str__(self):
        return f"رسالة من {self.name} - {self.subject}"

# --- 3. جدول سلة المشتريات (Checkout) ---
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="المستخدم")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="القطعة")
    quantity = models.PositiveIntegerField(default=1, verbose_name="الكمية")
    
    # دالة تحسب إجمالي سعر القطعة بناء على الكمية
    def get_total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
    
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)]) # من 1 لـ 5
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.user.username