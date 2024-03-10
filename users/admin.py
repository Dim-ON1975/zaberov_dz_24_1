from django.contrib import admin
from users.models import User, Payment


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'is_superuser',
        'email_verify',)
    list_filter = ('email', 'email_verify', 'is_staff', 'is_active', 'is_superuser',)
    search_fields = ('first_name', 'last_name', 'email',)


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('payer', 'course_pay', 'lesson_pay', 'date_pay', 'amount_pay', 'method_pay',)
    list_filter = ('payer', 'course_pay', 'lesson_pay', 'date_pay', 'amount_pay', 'method_pay',)
    search_fields = ('payer', 'course_pay', 'lesson_pay',)
