from django.db import models

class Employees(models.Model):
    EmployeeId = models.IntegerField(db_column='EmployeeId', primary_key=True)  
    LastName = models.TextField(db_column='LastName')   
    FirstName = models.TextField(db_column='FirstName')   
    Title = models.TextField(db_column='Title', blank=True, null=True)   
    ReportsTo = models.IntegerField(db_column='ReportsTo', blank=True, null=True)  
    BirthDate = models.DateTimeField(db_column='BirthDate', blank=True, null=True)  
    HireDate = models.DateTimeField(db_column='HireDate', blank=True, null=True)  
    Address = models.TextField(db_column='Address', blank=True, null=True)   
    City = models.TextField(db_column='City', blank=True, null=True)   
    State = models.TextField(db_column='State', blank=True, null=True)   
    Country = models.TextField(db_column='Country', blank=True, null=True)   
    PostalCode = models.TextField(db_column='PostalCode', blank=True, null=True)   
    Phone = models.TextField(db_column='Phone', blank=True, null=True)   
    Fax = models.TextField(db_column='Fax', blank=True, null=True)   
    Email = models.TextField(db_column='Email', blank=True, null=True)   

    class Meta:
        managed = False
        db_table = 'employees'

class Customers(models.Model):
    CustomerId = models.IntegerField(db_column='CustomerId', primary_key=True)  
    FirstName = models.TextField(db_column='FirstName')   
    LastName = models.TextField(db_column='LastName')   
    Company = models.TextField(db_column='Company', blank=True, null=True)   
    Address = models.TextField(db_column='Address', blank=True, null=True)   
    City = models.TextField(db_column='City', blank=True, null=True)   
    State = models.TextField(db_column='State', blank=True, null=True)   
    Country = models.TextField(db_column='Country', blank=True, null=True)   
    Postalcode = models.TextField(db_column='PostalCode', blank=True, null=True)   
    Phone = models.TextField(db_column='Phone', blank=True, null=True)   
    Fax = models.TextField(db_column='Fax', blank=True, null=True)   
    Email = models.TextField(db_column='Email')   
    SupportRepId = models.ForeignKey(Employees, db_column='SupportRepId', on_delete=models.CASCADE)  

    class Meta:
        managed = False
        db_table = 'customers'


class Genres(models.Model):
    GenreId = models.IntegerField(db_column='GenreId', primary_key=True)  
    Name = models.CharField(db_column='Name', blank=True, null=True, max_length=120)   

    class Meta:
        managed = False
        db_table = 'genres'


class Artists(models.Model):
    ArtistId = models.IntegerField(db_column='ArtistId', primary_key=True)  
    Name = models.CharField(db_column='Name', blank=True, null=True, max_length=120)   

    class Meta:
        managed = False
        db_table = 'Artists'

class Albums(models.Model):
    AlbumId = models.IntegerField(db_column='AlbumId', primary_key=True)  
    Title = models.CharField(db_column='Title', max_length=160)   
    ArtistId = models.ForeignKey(Artists, on_delete=models.CASCADE, db_column="ArtistId")  

    class Meta:
        managed = False
        db_table = 'Albums'


class Invoices(models.Model):
    InvoiceId = models.IntegerField(db_column='InvoiceId', primary_key=True)  
    CustomerId = models.ForeignKey(Customers, db_column='CustomerId', on_delete=models.CASCADE)  
    InvoiceDate = models.DateTimeField(db_column='InvoiceDate')  
    BillingAddress = models.TextField(db_column='BillingAddress', blank=True, null=True)   
    BillingCity = models.TextField(db_column='BillingCity', blank=True, null=True)   
    BillingState = models.TextField(db_column='BillingState', blank=True, null=True)   
    BillingCountry = models.TextField(db_column='BillingCountry', blank=True, null=True)   
    BillingPostalCode = models.TextField(db_column='BillingPostalCode', blank=True, null=True)   
    Total = models.TextField(db_column='Total')   

    class Meta:
        managed = False
        db_table = 'invoices'




class MediaTypes(models.Model):
    MediaTypeId = models.IntegerField(db_column='MediaTypeId', primary_key=True)  
    Name = models.CharField(db_column='Name', blank=True, null=True, max_length=120)   

    class Meta:
        managed = False
        db_table = 'media_types'


class Playlists(models.Model):
    PlaylistId = models.IntegerField(db_column='PlaylistId', primary_key=True)  
    Name = models.CharField(db_column='Name', blank=True, null=True, max_length=120)   

    class Meta:
        managed = False
        db_table = 'playlists'


class SqliteStat1(models.Model):
    tbl = models.TextField(blank=True, null=True)  # 
    idx = models.TextField(blank=True, null=True)  # 
    stat = models.TextField(blank=True, null=True)  # 

    class Meta:
        managed = False
        db_table = 'sqlite_stat1'


class Tracks(models.Model):
    TrackId = models.IntegerField(db_column='TrackId', primary_key=True)  
    Name = models.CharField(db_column='Name', max_length=200)   
    AlbumId = models.ForeignKey(Albums, on_delete=models.CASCADE, db_column="AlbumId")  
    MediaTypeId = models.ForeignKey(MediaTypes, on_delete=models.CASCADE, db_column="MediaTypeId")  
    GenreId = models.ForeignKey(Genres, on_delete=models.CASCADE, db_column="GenreId")  
    Composer = models.CharField(db_column='Composer', blank=True, null=True, max_length=220)   
    Milliseconds = models.IntegerField(db_column='Milliseconds')  
    Bytes = models.IntegerField(db_column='Bytes')  
    UnitPrice = models.FloatField(db_column='UnitPrice')   

    class Meta:
        managed = False
        db_table = 'tracks'

class PlaylistTrack(models.Model):
    PlaylistId = models.ForeignKey(Playlists, on_delete=models.CASCADE, db_column="PlaylistId")  
    TrackId = models.ForeignKey(Tracks, on_delete=models.CASCADE, db_column="TrackId")  

    class Meta:
        managed = False
        db_table = 'playlist_track'

class InvoiceItems(models.Model):
    InvoiceLineId = models.IntegerField(db_column='InvoiceLineId', primary_key=True)  
    InvoiceId = models.ForeignKey(Invoices, on_delete=models.CASCADE, db_column="InvoiceId")  
    TrackId = models.ForeignKey(Tracks, on_delete=models.CASCADE, db_column="TrackId")  
    UnitPrice = models.FloatField(db_column='UnitPrice')   
    Quantity = models.IntegerField(db_column='Quantity')  

    class Meta:
        managed = False
        db_table = 'invoice_items'