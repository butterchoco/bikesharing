# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Acara(models.Model):
    id_acara = models.CharField(primary_key=True, max_length=10)
    judul = models.CharField(max_length=100)
    deskripsi = models.TextField(blank=True, null=True)
    tgl_mulai = models.DateField()
    tgl_akhir = models.DateField()
    is_free = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'ACARA'


class AcaraStasiun(models.Model):
    id_stasiun = models.ForeignKey('Stasiun', models.DO_NOTHING, db_column='id_stasiun', primary_key=True)
    id_acara = models.ForeignKey(Acara, models.DO_NOTHING, db_column='id_acara')

    class Meta:
        managed = False
        db_table = 'ACARA_STASIUN'
        unique_together = (('id_stasiun', 'id_acara'),)


class Anggota(models.Model):
    no_kartu = models.CharField(primary_key=True, max_length=10)
    saldo = models.FloatField(blank=True, null=True)
    points = models.IntegerField(blank=True, null=True)
    ktp = models.ForeignKey('Person', models.DO_NOTHING, db_column='ktp')

    class Meta:
        managed = False
        db_table = 'ANGGOTA'


class Laporan(models.Model):
    id_laporan = models.CharField(primary_key=True, max_length=10)
    no_kartu_anggota = models.ForeignKey('Peminjaman', models.DO_NOTHING, db_column='no_kartu_anggota')
    datetime_pinjam = models.DateTimeField()
    nomor_sepeda = models.CharField(max_length=10)
    id_stasiun = models.CharField(max_length=10)
    status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'LAPORAN'
        unique_together = (('id_laporan', 'no_kartu_anggota', 'datetime_pinjam', 'nomor_sepeda', 'id_stasiun'),)


class Peminjaman(models.Model):
    no_kartu_anggota = models.ForeignKey(Anggota, models.DO_NOTHING, db_column='no_kartu_anggota', primary_key=True)
    datetime_pinjam = models.DateTimeField()
    nomor_sepeda = models.ForeignKey('Sepeda', models.DO_NOTHING, db_column='nomor_sepeda')
    id_stasiun = models.ForeignKey('Stasiun', models.DO_NOTHING, db_column='id_stasiun')
    datetime_kembali = models.DateTimeField(blank=True, null=True)
    biaya = models.FloatField(blank=True, null=True)
    denda = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PEMINJAMAN'
        unique_together = (('no_kartu_anggota', 'datetime_pinjam', 'nomor_sepeda', 'id_stasiun'),)


class Penugasan(models.Model):
    ktp = models.ForeignKey('Petugas', models.DO_NOTHING, db_column='ktp', primary_key=True)
    start_datetime = models.DateTimeField()
    id_stasiun = models.ForeignKey('Stasiun', models.DO_NOTHING, db_column='id_stasiun')
    end_datetime = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'PENUGASAN'
        unique_together = (('ktp', 'start_datetime', 'id_stasiun'),)


class Person(models.Model):
    ktp = models.CharField(primary_key=True, max_length=20)
    email = models.CharField(unique=True, max_length=50)
    nama = models.CharField(max_length=50)
    alamat = models.TextField(blank=True, null=True)
    tgl_lahir = models.DateField()
    no_telp = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'PERSON'


class Petugas(models.Model):
    ktp = models.ForeignKey(Person, models.DO_NOTHING, db_column='ktp', primary_key=True)
    gaji = models.FloatField()

    class Meta:
        managed = False
        db_table = 'PETUGAS'


class Sepeda(models.Model):
    nomor = models.CharField(primary_key=True, max_length=10)
    merk = models.CharField(max_length=10)
    jenis = models.CharField(max_length=50)
    status = models.BooleanField()
    id_stasiun = models.ForeignKey('Stasiun', models.DO_NOTHING, db_column='id_stasiun')
    no_kartu_penyumbang = models.ForeignKey(Anggota, models.DO_NOTHING, db_column='no_kartu_penyumbang', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'SEPEDA'


class Stasiun(models.Model):
    id_stasiun = models.CharField(primary_key=True, max_length=10)
    alamat = models.TextField()
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    nama = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'STASIUN'


class Transaksi(models.Model):
    no_kartu_anggota = models.ForeignKey(Anggota, models.DO_NOTHING, db_column='no_kartu_anggota', primary_key=True)
    date_time = models.DateTimeField()
    jenis = models.CharField(max_length=20)
    nominal = models.FloatField()

    class Meta:
        managed = False
        db_table = 'TRANSAKSI'
        unique_together = (('no_kartu_anggota', 'date_time'),)


class TransaksiKhususPeminjaman(models.Model):
    no_kartu_anggota = models.ForeignKey(Transaksi, models.DO_NOTHING, db_column='no_kartu_anggota', primary_key=True)
    date_time = models.DateTimeField()
    no_kartu_peminjam = models.ForeignKey(Peminjaman, models.DO_NOTHING, db_column='no_kartu_peminjam', blank=True, null=True)
    datetime_pinjam = models.DateTimeField(blank=True, null=True)
    no_sepeda = models.CharField(max_length=10, blank=True, null=True)
    id_stasiun = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TRANSAKSI_KHUSUS_PEMINJAMAN'
        unique_together = (('no_kartu_anggota', 'date_time'),)


class Voucher(models.Model):
    id_voucher = models.CharField(primary_key=True, max_length=10)
    nama = models.CharField(max_length=255)
    kategori = models.CharField(max_length=255)
    nilai_poin = models.FloatField()
    deskripsi = models.TextField(blank=True, null=True)
    no_kartu_anggota = models.ForeignKey(Anggota, models.DO_NOTHING, db_column='no_kartu_anggota', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'VOUCHER'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
