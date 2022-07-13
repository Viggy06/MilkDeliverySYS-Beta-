# request, redirect
from django.shortcuts import render, redirect

# AUTH
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# For Excel
import pandas as pd
import openpyxl

# models and forms
from .models import FixedForAll, Delivery_Boy_Model, OrderHistory, Dboyride
from .forms import FixedForAllForm, Dboy_form

#django
from django.views.decorators.csrf import csrf_exempt

#DATE
import datetime
from dateutil.relativedelta import relativedelta

# Create your views here.
def home(request):
    if request.user.is_authenticated :
        user = request.user
        if user.is_staff :
            d = FixedForAll.objects.filter(Group = None)  # unassigned data to group will be showed
            fm = []
            for i in d: fm.append(FixedForAllForm(instance=i))
            return render(request, 'impexp.html', {'d': fm})

        else :
            dboy = Delivery_Boy_Model.objects.filter(Dusername=user)  # username
            for i in dboy:
                datac = i.order.split(',')
            res = []
            for i in datac:
                if (i != ""):
                    res.append(i)
            d = []
            for j in res:
                r = FixedForAll.objects.filter(CustomerID=j.strip())
                # print(r)
                for i in r:
                    d.append(i)
            return render(request, 'deliveryboylogin.html', {'user': dboy, 'data': d, 'duser': user})

    elif request.method == 'POST':
        u = request.POST['username']
        p = request.POST['password']
        user = authenticate(username=u, password=p)

        if user is None:
            return render(request, 'login.html', {'error': 'Username or password did not match'})
        elif user.is_staff :
            login(request, user)
            d = FixedForAll.objects.filter(Group=None)  # unassigned data to group will be showed
            fm = []
            for i in d: fm.append(FixedForAllForm(instance=i))
            return render(request, 'impexp.html', {'d': fm})

        else:
            login(request, user)
            dboy = Delivery_Boy_Model.objects.filter(Dusername=user)
            for i in dboy:
                check = i.order
            # print(check)
            if check == None:
                return render(request, 'deliveryboylogin.html', {'user': dboy})
            else:
                for i in dboy:
                    datac = i.order.split(',')
                res = []
                for i in datac:
                    if (i != ""):
                        res.append(i)
                # print(res)
                d = []
                for j in res:
                    r = FixedForAll.objects.filter(CustomerID=j.strip())
                    # print(r)
                    for i in r:
                        # print(i)
                        d.append(i)
        return render(request, 'deliveryboylogin.html', {'user': dboy, 'data': d, 'duser': user})
    return render(request, 'login.html')

#test1
def logoutUser(request):
    logout(request)
    return redirect('/')

@login_required
def cao(request): #CLEAR ALL ASSIGN ORDERS of DBOYS BUTTON
    if request.method == 'POST':
        Delivery_Boy_Model.objects.all().update(order = None, group = None)
        FixedForAll.objects.all().update(status = '',dboy = None)
    return redirect('/')

@login_required
def upload(request):
    if request.method == 'POST':
        f = request.FILES.getlist('myfile')
        for i in range(len(f)):
            d = openpyxl.load_workbook(f[i])
            for s in d.sheetnames:
                dt = pd.read_excel(f[i], engine="openpyxl", sheet_name=s).dropna(
                    how='all')
                ll = []

                for j in dt.columns:
                    if dt[j].any(): ll.append(dt[j].values)  #
                ll = zip(*ll)

                if str(f[i]).split('.')[0] == 'Gosrushti':
                    for j in ll:
                        print(j[0])
                        FixedForAll.objects.update_or_create(pk=j[0], defaults={'Customer_Name': j[1],
                                                                                'Address': str(
                                                                                    j[2]) + " " + str(j[3]),
                                                                                'Plan': str(j[-1]),
                                                                                'Phone_No': 'None',
                                                                                'Total_milk': 'None',
                                                                                'bottles' : 0,
                                                                                'status': '',
                                                                                'Company_name':
                                                                                    str(f[i]).split('.')[0].replace(" ", "")
                                                                                })
                elif str(f[i]).split('.')[0] == 'Vedaaz':
                    for j in ll:
                        bt = int(j[5])
                        if float(j[5]) % 1 > 0 : bt += 1
                        FixedForAll.objects.update_or_create(pk=j[0], defaults={'Customer_Name': j[1],
                                                                                'Address': str(j[2]),
                                                                                'Phone_No': str(j[3]),
                                                                                'Plan': str(j[4]),
                                                                                'Total_milk': str(j[5]),
                                                                                'bottles': bt,
                                                                                'status': '',
                                                                                'Company_name':
                                                                                    str(f[i]).split('.')[
                                                                                        0].replace(" ", "")
                                                                                })
                elif str(f[i]).split('.')[0] == 'Dear Cow':
                    for j in ll:
                        FixedForAll.objects.update_or_create(pk=j[7], defaults={'Customer_Name': j[3],
                                                                                'Address': str(
                                                                                    j[4]) + " " + str(j[5]),
                                                                                'Phone_No': "None",
                                                                                'Plan': "None",
                                                                                'Total_milk': str(j[6]),
                                                                                'bottles' : 0,
                                                                                'status': '',
                                                                                'Company_name':
                                                                                    str(f[i]).split('.')[
                                                                                        0].replace(" ", "")
                                                                                })
                elif str(f[i]).split('.')[0] == 'Amurut':
                    for j in ll:
                        FixedForAll.objects.update_or_create(pk=j[0], defaults={'Customer_Name': j[1],
                                                                                'Total_milk': str(j[2]),
                                                                                'bottles' : 0,
                                                                                'Address': str(j[3]),
                                                                                'Phone_No': str(j[4]),
                                                                                'Plan': "None",
                                                                                'status': '',
                                                                                'Company_name':
                                                                                    str(f[i]).split('.')[
                                                                                        0].replace(" ", "")
                                                                                })
                elif str(f[i]).split('.')[0] == 'Happycow':
                    for j in ll:
                        FixedForAll.objects.update_or_create(pk=j[0], defaults={'Customer_Name': j[1],
                                                                                'Address': str(
                                                                                    j[2]) + " " + str(
                                                                                    j[3]) + " " + str(j[4]),
                                                                                'Phone_No': "None",
                                                                                'Plan': 'None',
                                                                                'Total_milk': str(j[5]),
                                                                                'bottles' : 0,
                                                                                'status': '',
                                                                                'Company_name':
                                                                                    str(f[i]).split('.')[
                                                                                        0].replace(" ", "")
                                                                                })
                elif str(f[i]).split('.')[0] == 'Mygir':
                    for j in ll:
                        FixedForAll.objects.update_or_create(pk=j[0], defaults={'Customer_Name': "None",
                                                                                'Address': str(j[1]),
                                                                                'Phone_No': "None",
                                                                                'Plan': "None",
                                                                                'Total_milk': str(j[2]),
                                                                                'bottles' : 0,
                                                                                'status': '',
                                                                                'Company_name':
                                                                                    str(f[i]).split('.')[0]
                                                                                })
                elif str(f[i]).split('.')[0] == 'White life farm':
                    for j in ll:
                        bt = int(j[4])
                        if float(j[4]) % 1 > 0 : bt += 1
                        # try:
                        #     st = FixedForAll.objects.get(pk=j[0])
                        #     bt = st.bottles
                        #     bt += int(j[4])
                        #     if float(j[4]) % 1 > 0: bt += 1
                        # except:
                        #     bt = int(j[4])
                        #     if float(j[4]) % 1 > 0: bt += 1
                        # print(bt)
                        FixedForAll.objects.update_or_create(pk=j[0], defaults={'Customer_Name': j[1],
                                                                                'Address': str(
                                                                                    j[2]) + " " + str(j[3]),
                                                                                'Phone_No': "None",
                                                                                'Plan': 'None',
                                                                                'Total_milk': str(j[4]),
                                                                                'bottles': bt,
                                                                                'status': '',
                                                                                'Company_name':
                                                                                    str(f[i]).split('.')[
                                                                                        0].replace(" ", "")
                                                                                })
                elif str(f[i]).split('.')[0] == 'Other Clients':
                    for j in ll:
                        FixedForAll.objects.update_or_create(pk=j[0], defaults={'Customer_Name': j[1],
                                                                                'Phone_No': str(j[2]),
                                                                                'Address': str(j[3]),
                                                                                'Plan': str(j[5]),
                                                                                'Total_milk': str(j[6]),
                                                                                'bottles' : 0,
                                                                                'status': '',
                                                                                'Company_name':
                                                                                    str(f[i]).split('.')[
                                                                                        0].replace(" ", "")
                                                                                })
        return redirect("/")
    return render(request, 'upload.html')


@login_required
def impexp(request):  # data wont get saved until group is assigned
    d = FixedForAll.objects.filter(Group=None)  # unassigned data to group will be showed
    fm = []
    for i in d: fm.append(FixedForAllForm(instance=i))
    return render(request, 'impexp.html', {'d': fm})


@login_required
def sb(request):
    cid = request.POST.getlist('CustomerID')
    cnm = request.POST.getlist('Customer_Name')
    cad = request.POST.getlist('Address')
    cpn = request.POST.getlist('Phone_No')
    cpl = request.POST.getlist('Plan')
    ctm = request.POST.getlist('Total_milk')
    ccn = request.POST.getlist('Company_name')
    cbt = request.POST.getlist('bottles')
    cgp = request.POST.getlist('Group')

    for i in range(len(cid)):
        gp = None
        if cgp[i] : gp = cgp[i]
        fm = FixedForAll(
            CustomerID = cid[i],
            Customer_Name = cnm[i],
            Address = cad[i],
            Phone_No = cpn[i],
            Plan = cpl[i],
            Total_milk = ctm[i],
            Company_name = ccn[i],
            bottles = cbt[i],
            Group = gp
        )
        fm.save()
    return redirect('/')


@login_required
def assign_orders(request):
    ops = FixedForAll.objects.values_list('Group').distinct()
    boys = Delivery_Boy_Model.objects.values_list('Dusername')
    if request.method == 'POST':
        gp = request.POST['dropdown']
        if gp == '---Groups---' or gp == 'None' :
            return render(request, "assign_orders.html", {'ops' : ops, 'error':"Select group first"})
        else:
            op = FixedForAll.objects.filter(Group=gp)
            ops = FixedForAll.objects.values_list('Group').distinct()
            ini_ord = ''
            for i in op: ini_ord += i.CustomerID+','
            return render(request, "assign_orders.html", {'ops': ops, 'op':op, 'boys' : boys,'ini_ord':ini_ord, 'gp':gp})
    return render(request, "assign_orders.html", {'ops' : ops})


# @login_required
# def ods(request): #group order in dmodel remaining
#     gp = request.POST["s_group"]
#     od = request.POST['sort_order'].split(',')
#     dby = request.POST['boysdropdown']
#     ch = request.POST['Checked_value'].split(',')
#     dod = []
#     for i in range(len(ch)):
#         if ch[i] == '1':
#             FixedForAll.objects.filter(CustomerID=od[i]).update(dboy=dby)
#             dod.append(od[i])
#     dod = ",".join(dod)
#     Delivery_Boy_Model.objects.filter(DName=dby).update(order = dod, group = gp)
#     # return redirect('/')
#     return redirect('/assign_orders/')


@login_required
def ods(request): #group order in dmodel remaining
    gp = request.POST["s_group"]
    od = request.POST['sort_order'].split(',')
    dby = request.POST['boysdropdown']
    ch = request.POST['Checked_value'].split(',')
    dod = []
    for i in range(len(ch)):
        if ch[i] == '1':
            FixedForAll.objects.filter(CustomerID=od[i]).update(dboy=dby)
            dod.append(od[i])
    dod = ",".join(dod)
    # Delivery_Boy_Model.objects.filter(DName=dby).update(order = dod, group = gp)
# -----------
    a = ''
    g = ''
    for i in Delivery_Boy_Model.objects.filter(DName=dby):
        if i.order == None or i.group == None:
            i.order = ''
            i.group = ''
        a = i.order
        sm = a+dod+","
        g = i.group
        gg = g+gp+","
        Delivery_Boy_Model.objects.filter(DName=dby).update(order = sm, group = gg)
    return redirect('/assign_orders/')

@login_required
def DeleteAssignedOrders(request): #clear assigned order of single dboy
    if request.method == 'POST':
        res = request.POST['bt']
        Delivery_Boy_Model.objects.filter(Dusername = res).update(order = None , group = None)
        FixedForAll.objects.filter(dboy = res).update(dboy = None)
    return redirect('/exisitingdboy/')

@login_required
def dboy(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        number = request.POST['number']
        username = request.POST['username']
        address = request.POST['address']
        password1 = request.POST['password1']
        # password2 = request.POST['password2']
        age = request.POST['age']
        gen = request.POST['gender']
        if request.POST['password1'] == request.POST['password2']:
            try:
                print(username,address)
                user = User.objects.create_user(
                username=username, password=password1,email=email, first_name=fname, last_name=lname)
                user.save()
                fm = Delivery_Boy_Model(DName=fname,DLast_Name=lname,Demail=email,Dage=age,DPhone_Number=number,Dusername=username,DLocation=address,Dpassword=password1,Dgender=gen)
                fm.save()
            except:
                return render(request, "dboy.html", {'error': 'Username already taken'})
        else:
            return render(request, "dboy.html",{'error': 'Passwords did not match'})
    return render(request, "dboy.html")


@login_required
def exisitingdboy(request):
    db = Delivery_Boy_Model.objects.all()
    if request.method == 'POST':
        res = request.POST['dboy']
        db = Delivery_Boy_Model.objects.filter(Dusername = res)
        return render(request, 'exisitingdboy.html', {'db':db})
    else:
        return render(request, 'exisitingdboy.html', {'db':db})
    
@login_required
def getpost(request):
    if request.method == 'POST':
        # print(request.POST)
        one_year_from_now = datetime.datetime.now() + relativedelta()
        Ddate = one_year_from_now.strftime("%d/%m/%Y")
        a = request.POST["dstatus"]
        a = a.split("*")
        k = a[0]
        comment = request.POST['comment']
        print(a)
        st = FixedForAll.objects.get(pk=k)

        if a[-1] == 'Delivered':
            if a[6] == 'Vedaaz' or a[6] == 'Whitelifefarm':
                bt = request.POST['bottles'] 
                if st.remaining_bottles == None: #first time and rmb is empty and delivered
                    st.remaining_bottles = 0
                    st.remaining_bottles +=st.bottles
                    st.status = "disabled"
                    st.save()
                else:
                    st.remaining_bottles +=st.bottles #second time when rmb not empty and delivered
                    st.remaining_bottles -= int(bt)
                    st.status = "disabled"
                    st.save()       
                data = OrderHistory(CustomerID = a[0],Customer_Name = a[1],Address = a[2],Phone_No = a[3],Plan = a[4],Total_milk = a[5],
                Company_name = a[6], DeliveryBoy = a[-2], status = a[-1],ogroup = a[-3], Ddate = Ddate,bottles=st.bottles, remaining_bottles=st.remaining_bottles,cust_comment=comment)
                data.save()
            else: #other companys
                st.status = "disabled"
                st.save()
                data = OrderHistory(CustomerID = a[0],Customer_Name = a[1],Address = a[2],Phone_No = a[3],Plan = a[4],Total_milk = a[5],
                Company_name = a[6], DeliveryBoy = a[-2], status = a[-1],ogroup = a[-3], Ddate = Ddate,cust_comment=comment)
                data.save()

        elif a[-1] == 'Not-Delivered':
            if a[6] == 'Vedaaz' or a[6] == 'Whitelifefarm':
                bt = request.POST['bottles']
                if st.remaining_bottles == None: #first time and rmb is empty and not delivered
                    st.remaining_bottles = 0
                    st.status = "disabled"
                    st.save()
                else:
                    #second time when rmb not empty and not d
                    st.remaining_bottles -= int(bt)
                    st.status = "disabled"
                    st.save()       
                data = OrderHistory(CustomerID = a[0],Customer_Name = a[1],Address = a[2],Phone_No = a[3],Plan = a[4],Total_milk = a[5],
                Company_name = a[6], DeliveryBoy = a[-2], status = a[-1],ogroup = a[-3], Ddate = Ddate,bottles=st.bottles, remaining_bottles=st.remaining_bottles,cust_comment=comment)
                data.save()
            else:
                # print('2nd else')
                st.status = "disabled"
                st.save()
                data = OrderHistory(CustomerID = a[0],Customer_Name = a[1],Address = a[2],Phone_No = a[3],Plan = a[4],Total_milk = a[5],
                Company_name = a[6], DeliveryBoy = a[-2], status = a[-1],ogroup = a[-3], Ddate = Ddate,cust_comment=comment)
                data.save()
    return redirect('/')

@login_required
def dboyride(request):
     #DBOY RIDE
    if request.method == "POST":
        startride = request.POST['startride']
        endride = request.POST['endride']
        user = request.POST['user']
        one_year_from_now = datetime.datetime.now() + relativedelta()
        Ddate = one_year_from_now.strftime("%d/%m/%Y")
        tride = float(startride) - float(endride)
        r = Dboyride.objects.create(Dusername = user, Ddate = Ddate, startride = float(startride), endride = float(endride) ,totalride =  str(tride).replace("-",""))
        r.save()
    return redirect('/')

@login_required
def orderhistory(request):#ONLY PAGE
    duser = Delivery_Boy_Model.objects.values_list('Dusername')
    gp = FixedForAll.objects.values_list('Group').distinct()
    cpy = FixedForAll.objects.values_list('Company_name').distinct()
    cpylist = []
    for i in cpy:
       cpylist.append(i[0].replace(" ",""))
    return render(request, 'orderhistory.html', {'duser':duser, 'group' : gp, 'company': cpylist})

@login_required
def orderhistoryf1(request):#DATE
    duser = Delivery_Boy_Model.objects.values_list('Dusername')
    gp = FixedForAll.objects.values_list('Group').distinct()
    cpy = FixedForAll.objects.values_list('Company_name').distinct()
    cpylist = []
    for i in cpy:
       cpylist.append(i[0].replace(" ",""))

    startdate = request.POST['startdate']
    enddate = request.POST['enddate']
    try:
        std = startdate.split('-')
        ans = std[::-1]
        startdate = ans[0] + "/" + ans[1] + "/" + ans[2]
    # print(startdate)
        endt = enddate.split('-')
        ans = endt[::-1]
        enddate = ans[0] + "/" + ans[1] + "/" + ans[2]
    except:
        pass

    # res = ''
    res = OrderHistory.objects.raw('select * from OrderHistory where Ddate between %s and %s',[startdate, enddate])
    return render(request, 'orderhistory.html', {'duser':duser, 'group' : gp, 'company': cpylist, 'res' : res})

@login_required
def orderhistoryf2(request): #FOR DBOY
    duser = Delivery_Boy_Model.objects.values_list('Dusername')
    gp = FixedForAll.objects.values_list('Group').distinct()
    cpy = FixedForAll.objects.values_list('Company_name').distinct()
    cpylist = []
    for i in cpy:
       cpylist.append(i[0].replace(" ",""))

    startdate = request.POST['startdate']
    enddate = request.POST['enddate']
    dboy = request.POST['dboy']

    try:
        std = startdate.split('-')
        ans = std[::-1]
        startdate = ans[0] + "/" + ans[1] + "/" + ans[2]
    # print(startdate)

        endt = enddate.split('-')
        ans = endt[::-1]
        enddate = ans[0] + "/" + ans[1] + "/" + ans[2]
    except:
        pass
    # print(enddate)

    res = OrderHistory.objects.raw('select * from OrderHistory where Ddate between %s and %s and DeliveryBoy = %s',[startdate, enddate, dboy])
    dboykms = Dboyride.objects.raw('select * from Dboyride where Ddate between %s and %s and Dusername = %s',[startdate, enddate, dboy])
    return render(request, 'orderhistory.html', {'duser':duser, 'group' : gp, 'company': cpylist, 'res' : res, 'dboykms':dboykms})

@login_required
def orderhistoryf3(request):
    duser = Delivery_Boy_Model.objects.values_list('Dusername')
    gp = FixedForAll.objects.values_list('Group').distinct()
    cpy = FixedForAll.objects.values_list('Company_name').distinct()
    cpylist = []
    for i in cpy:
       cpylist.append(i[0].replace(" ",""))
    
    startdate = request.POST['startdate']
    enddate = request.POST['enddate']

    try:
        std = startdate.split('-')
        ans = std[::-1]
        startdate = ans[0] + "/" + ans[1] + "/" + ans[2]
    # print(startdate)
        endt = enddate.split('-')
        ans = endt[::-1]
        enddate = ans[0] + "/" + ans[1] + "/" + ans[2]
    except:
        pass

    group = request.POST['Group']  #group
    res = OrderHistory.objects.raw('select * from OrderHistory where Ddate between %s and %s and  ogroup = %s',[startdate, enddate, group])
    return render(request, 'orderhistory.html', {'duser':duser, 'group' : gp, 'company': cpylist, 'res' : res})

@login_required
def orderhistoryf4(request):
    duser = Delivery_Boy_Model.objects.values_list('Dusername')
    gp = FixedForAll.objects.values_list('Group').distinct()
    cpy = FixedForAll.objects.values_list('Company_name').distinct()
    cpylist = []
    for i in cpy:
       cpylist.append(i[0].replace(" ",""))
    # print(cpylist)
    startdate = request.POST['startdate']
    enddate = request.POST['enddate']
    try:
        std = startdate.split('-')
        ans = std[::-1]
        startdate = ans[0] + "/" + ans[1] + "/" + ans[2]
    # print(startdate)
        endt = enddate.split('-')
        ans = endt[::-1]
        enddate = ans[0] + "/" + ans[1] + "/" + ans[2]
    except:
        pass

    company = request.POST['Company'] #company
    res = OrderHistory.objects.raw('select * from OrderHistory where Ddate between %s and %s and Company_name = %s',[startdate, enddate, company])
    return render(request, 'orderhistory.html', {'duser':duser, 'group' : gp, 'company': cpylist, 'res' : res})


