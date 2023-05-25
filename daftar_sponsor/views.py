from django.shortcuts import render

# Create your views here.

def indexDaftarSponsor(request):
    if request.method == 'POST':
        # Handle form submission
        nama_sponsor = request.POST.get('nama-sponsor')
        tanggal_mulai = request.POST.get('start-date')
        tanggal_selesai = request.POST.get('finish-date')
        
        # Do something with the data (e.g. save to database)
        # ...
        
        # Render a success message
        return render(request, 'daftar_sponsor.html')
    
    # Render the form template
    return render(request, 'daftar_sponsor.html')