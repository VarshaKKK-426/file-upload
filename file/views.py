from django.shortcuts import render
from .models import Company
from .resources import CompanyResource
from django.contrib import messages
from tablib import Dataset
from django.http import HttpResponse

import os
import csv


# Create your views here.
def simple_upload(request):
    if request.method == 'POST':
        new_company = request.FILES['myfile']
        target_currency = request.POST['target_currency']
        exchange_rate = request.POST['exchange_rate']

        if not new_company.name.endswith('csv'):
            messages.info(request,'wrong format')
            return render(request,'upload.html')
        
        if new_company.multiple_chunks():
            messages.info(request,"Uploaded file is too big (%.2f MB)." % (new_company.size/(1000*1000),))
            return render(request,'upload.html')

        file_data = new_company.read().decode("utf-8")
        lines = file_data.split("\n")[1:]
        
        new_converted_data = []

        for line in lines:
            if len(line) < 4:
                break
            fields = line.split(",")
            data_dict = {}
            data_dict["name"] = fields[0]
            data_dict["currency"] = fields[1]
            data_dict["amount"] = fields[2]
            data_dict["transaction_date"] = fields[3]
            data_dict["converted_currency"] = target_currency
            data_dict["converted_amount"] = float(fields[2])*float(exchange_rate)
            new_converted_data.append(data_dict)
        
            
            

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="Data.csv"'
        writer = csv.writer(response)
        writer.writerow(["Name", "Currency", "Amount", "Transaction Date", "Converted Currency", "Converted Amount"])
        for i in new_converted_data:
            writer.writerow([i['name'],i['currency'],i['amount'],i['transaction_date'],i['converted_currency'],i['converted_amount']])
        return response       

       

    return render(request,'upload.html')
             

       



