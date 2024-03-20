from django.contrib import admin
from dashboard.models import pegawai
# Register your models here.

@admin.register(pegawai)
class pegawaiAdmin(admin.ModelAdmin):
    list_display = ['nama', 'alamat', 'jenis_kelamin', 'golongan']