from django.db import models

class Employees(models.Model):
    EmployeeId = models.IntegerField(db_column='EmployeeId', primary_key=True)  # Field name made lowercase.
    LastName = models.TextField(db_column='LastName')  # Field name made lowercase. This field type is a guess.
    FirstName = models.TextField(db_column='FirstName')  # Field name made lowercase. This field type is a guess.
    Title = models.TextField(db_column='Title', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ReportsTo = models.IntegerField(db_column='ReportsTo', blank=True, null=True)  # Field name made lowercase.
    BirthDate = models.DateTimeField(db_column='BirthDate', blank=True, null=True)  # Field name made lowercase.
    HireDate = models.DateTimeField(db_column='HireDate', blank=True, null=True)  # Field name made lowercase.
    Address = models.TextField(db_column='Address', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    City = models.TextField(db_column='City', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    State = models.TextField(db_column='State', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    Country = models.TextField(db_column='Country', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    PostalCode = models.TextField(db_column='PostalCode', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    Phone = models.TextField(db_column='Phone', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    Fax = models.TextField(db_column='Fax', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    Email = models.TextField(db_column='Email', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'employees'

class Customers(models.Model):
    CustomerId = models.IntegerField(db_column='CustomerId', primary_key=True)  # Field name made lowercase.
    FirstName = models.TextField(db_column='FirstName')  # Field name made lowercase. This field type is a guess.
    LastName = models.TextField(db_column='LastName')  # Field name made lowercase. This field type is a guess.
    Company = models.TextField(db_column='Company', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    Address = models.TextField(db_column='Address', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    City = models.TextField(db_column='City', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    State = models.TextField(db_column='State', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    Country = models.TextField(db_column='Country', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    Postalcode = models.TextField(db_column='PostalCode', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    Phone = models.TextField(db_column='Phone', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    Fax = models.TextField(db_column='Fax', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    Email = models.TextField(db_column='Email')  # Field name made lowercase. This field type is a guess.
    SupportRepId = models.ForeignKey(Employees, db_column='SupportRepId', on_delete=models.CASCADE)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customers'


class Genres(models.Model):
    GenreId = models.IntegerField(db_column='GenreId', primary_key=True)  # Field name made lowercase.
    Name = models.CharField(db_column='Name', blank=True, null=True, max_length=120)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'genres'


class Artists(models.Model):
    ArtistId = models.IntegerField(db_column='ArtistId', primary_key=True)  # Field name made lowercase.
    Name = models.CharField(db_column='Name', blank=True, null=True, max_length=120)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Artists'

class Albums(models.Model):
    AlbumId = models.IntegerField(db_column='AlbumId', primary_key=True)  # Field name made lowercase.
    Title = models.CharField(db_column='Title', max_length=160)  # Field name made lowercase. This field type is a guess.
    ArtistId = models.ForeignKey(Artists, on_delete=models.CASCADE, db_column="ArtistId")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Albums'


class Invoices(models.Model):
    InvoiceId = models.IntegerField(db_column='InvoiceId', primary_key=True)  # Field name made lowercase.
    CustomerId = models.ForeignKey(Customers, db_column='CustomerId', on_delete=models.CASCADE)  # Field name made lowercase.
    InvoiceDate = models.DateTimeField(db_column='InvoiceDate')  # Field name made lowercase.
    BillingAddress = models.TextField(db_column='BillingAddress', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    BillingCity = models.TextField(db_column='BillingCity', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    BillingState = models.TextField(db_column='BillingState', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    BillingCountry = models.TextField(db_column='BillingCountry', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    BillingPostalCode = models.TextField(db_column='BillingPostalCode', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    Total = models.TextField(db_column='Total')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'invoices'




class MediaTypes(models.Model):
    MediaTypeId = models.IntegerField(db_column='MediaTypeId', primary_key=True)  # Field name made lowercase.
    Name = models.CharField(db_column='Name', blank=True, null=True, max_length=120)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'media_types'


class Playlists(models.Model):
    PlaylistId = models.IntegerField(db_column='PlaylistId', primary_key=True)  # Field name made lowercase.
    Name = models.CharField(db_column='Name', blank=True, null=True, max_length=120)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'playlists'


class SqliteStat1(models.Model):
    tbl = models.TextField(blank=True, null=True)  # This field type is a guess.
    idx = models.TextField(blank=True, null=True)  # This field type is a guess.
    stat = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'sqlite_stat1'


class Tracks(models.Model):
    TrackId = models.IntegerField(db_column='TrackId', primary_key=True)  # Field name made lowercase.
    Name = models.CharField(db_column='Name', max_length=200)  # Field name made lowercase. This field type is a guess.
    AlbumId = models.ForeignKey(Albums, on_delete=models.CASCADE, db_column="AlbumId")  # Field name made lowercase.
    MediaTypeId = models.ForeignKey(MediaTypes, on_delete=models.CASCADE, db_column="MediaTypeId")  # Field name made lowercase.
    GenreId = models.ForeignKey(Genres, on_delete=models.CASCADE, db_column="GenreId")  # Field name made lowercase.
    Composer = models.CharField(db_column='Composer', blank=True, null=True, max_length=220)  # Field name made lowercase. This field type is a guess.
    Milliseconds = models.IntegerField(db_column='Milliseconds')  # Field name made lowercase.
    Bytes = models.IntegerField(db_column='Bytes')  # Field name made lowercase.
    UnitPrice = models.FloatField(db_column='UnitPrice')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'tracks'

class PlaylistTrack(models.Model):
    PlaylistId = models.ForeignKey(Playlists, on_delete=models.CASCADE, db_column="PlaylistId")  # Field name made lowercase.
    TrackId = models.ForeignKey(Tracks, on_delete=models.CASCADE, db_column="TrackId")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'playlist_track'

class InvoiceItems(models.Model):
    InvoiceLineId = models.IntegerField(db_column='InvoiceLineId', primary_key=True)  # Field name made lowercase.
    InvoiceId = models.ForeignKey(Invoices, on_delete=models.CASCADE, db_column="InvoiceId")  # Field name made lowercase.
    TrackId = models.ForeignKey(Tracks, on_delete=models.CASCADE, db_column="TrackId")  # Field name made lowercase.
    UnitPrice = models.FloatField(db_column='UnitPrice')  # Field name made lowercase. This field type is a guess.
    Quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'invoice_items'