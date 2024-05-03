# views.py
import win32con
from django.shortcuts import render
from .models import Product, Sale
import win32print
import win32ui
from django.http import HttpResponse
from django.template.loader import render_to_string
import os
from django.conf import settings

def euToLeke(price):
    lekep = float(price * settings.EURO)
    return lekep

def euToUSD(price):
    price = euToLeke(price)
    usdp = price * settings.DOLLAR / 10000
    return usdp


def cashier_view(request):
    products = Product.objects.all()
    return render(request, 'kasa.html', {'products': products, 'euro':settings.EURO, 'dollar':settings.DOLLAR})

from django.shortcuts import redirect
import datetime
import json
from django.http import JsonResponse

import requests

def perditesim(request):
    try:
        with open(r'db4.sqlite3', 'rb') as file:
            files = {'file': file}
            response = requests.post('https://mbaci.pythonanywhere.com/upload/', files=files, timeout=10)

        # Check the response status code
        if response.status_code == 201:
            print("POST request was successful.")
            print("Response:", response.json())
        else:
            print("POST request failed with status code:", response.status_code)
    except:
        pass

    return redirect(request.META.get('HTTP_REFERER'))

def register_sale(request):
    if request.method == 'POST':
        sale_items_json = request.POST.get('sale_items')
        sale_items_data = json.loads(sale_items_json)
        receipt_code = generate_receipt_code()
        for item in sale_items_data:
            product_id = item['prodID']
            price = item['price']
            # Create Sale object for each sale item
            sale = Sale.objects.create(product_id=product_id, price=price, receipt_code=receipt_code)
        # upload_script_path = os.path.join(os.path.dirname(__file__), r'C:\Users\User\store_manager\manager\uploadDB.py')
        # exec(open(upload_script_path).read())
        # print(upload_script_path)
        perditesim(request)

        return JsonResponse({'success': True, 'last_sale':sale_items_data})
    else:
        return JsonResponse({'success': False})


import uuid

def generate_receipt_code():
    prefix = 'SA'  # Prefix for the receipt code
    unique_id = uuid.uuid4().hex[:6]  # Generate a random 6-character unique ID
    return f'{prefix}-{unique_id}'



def print_receipt(request, products):
    # Render the receipt template with the product data
    receipt_data = {
        'products': products,
    }
    receipt_html = render_to_string('receipt.html', receipt_data)

    # Create a printer device context
    printer_name = win32print.GetDefaultPrinter()
    printer_handle = win32print.OpenPrinter(printer_name)
    printer_dc = win32ui.CreateDC()
    printer_dc.CreatePrinterDC(printer_name)

    # Start a print job
    job_info = ("Receipt", None, {"DesiredAccess": win32print.PRINTER_ACCESS_USE})
    printer_handle = win32print.OpenPrinter(printer_name, job_info)
    win32print.StartDocPrinter(printer_handle, 1, ("Receipt", None, "RAW"))
    win32print.StartPagePrinter(printer_handle)

    # Print the receipt content
    printer_dc.StartDoc(receipt_html)
    printer_dc.StartPage()

    # Set the printer font and print the HTML content
    printer_dc.SetMapMode(win32con.MM_TEXT)
    printer_dc.DrawText(receipt_html, (100, 100), win32con.DT_LEFT)

    # End the print job
    printer_dc.EndPage()
    printer_dc.EndDoc()
    win32print.EndPagePrinter(printer_handle)
    win32print.ClosePrinter(printer_handle)

    # Return a response to indicate successful printing
    return HttpResponse("Receipt printed successfully")