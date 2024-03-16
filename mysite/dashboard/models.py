from django.db import models

# Create your models here.
class pegawai(models.Model):    
    nama = models.CharField(max_length=225)
    alamat  = models.CharField(max_length=225)
    JENIS_KELAMIN = (
        ('laki-laki', 'laki-laki'),
        ('perempuan', 'perempuan')
    )
    jenis_kelamin = models.CharField(max_length=225, choices=JENIS_KELAMIN)

    GOLONGAN_PEGAWAI = (
             ('pembina - I/A', 'pembina - I/A'),
             ('pembina - II/A', 'pembina - II/A'),
             ('pembina - III/A', 'pembina - III/A'),
             ('pembina - II/B', 'pembina - II/B'),
             ('pembina - I/A', 'pembina - I/A'),
             ('pembina - II/A', 'pembina - I/IA'),
             ('pembina - II/B', 'pembina - II/B'),
             ('pembina - III/C', 'pembina - III/C'),
    )    
    golongan = models.CharField(max_length=225, choices=GOLONGAN_PEGAWAI)
    
    def _str_(self):
        return self.nama
 