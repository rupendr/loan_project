# Generated by Django 3.2.6 on 2021-08-14 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=20)),
                ('father_name', models.CharField(max_length=20)),
                ('customer_profile', models.CharField(max_length=12)),
                ('loan_account_no', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customer data',
            },
        ),
        migrations.CreateModel(
            name='LoanAmountData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agreement_date', models.CharField(max_length=12, verbose_name='AGREEMENT DATE ')),
                ('lrn', models.CharField(max_length=12, verbose_name='LRN')),
                ('tenor', models.CharField(max_length=12, verbose_name='TENOR')),
                ('adv_emi', models.CharField(max_length=12, verbose_name='ADV EMI')),
                ('mob', models.CharField(max_length=12, verbose_name='MOB')),
                ('CustLoan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CustLoan', to='loan.customer')),
            ],
            options={
                'verbose_name': 'Loan amount data',
                'verbose_name_plural': 'Loan amount data',
            },
        ),
        migrations.CreateModel(
            name='CustomerOfficeAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('office_pincode', models.CharField(max_length=12, verbose_name='ZIP / Postal code')),
                ('office_landmark', models.CharField(max_length=1024, verbose_name='landmark')),
                ('office_address1', models.CharField(max_length=1024, verbose_name='Address line 1')),
                ('office_address2', models.CharField(max_length=1024, verbose_name='Address line 2')),
                ('office_address3', models.CharField(max_length=1024, verbose_name='Address line 3')),
                ('CustOffice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CustOffice', to='loan.customer')),
            ],
            options={
                'verbose_name': 'Cust office Address',
                'verbose_name_plural': 'Cust office Address',
            },
        ),
        migrations.CreateModel(
            name='CustomerHomeAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pincode', models.CharField(max_length=12, verbose_name='ZIP / Postal code')),
                ('landmark', models.CharField(max_length=1024, verbose_name='landmark')),
                ('address1', models.CharField(max_length=1024, verbose_name='Address line 1')),
                ('address2', models.CharField(max_length=1024, verbose_name='Address line 2')),
                ('address3', models.CharField(max_length=1024, verbose_name='Address line 3')),
                ('CustHome', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CustHome', to='loan.customer')),
            ],
            options={
                'verbose_name': 'Cust Home Address',
                'verbose_name_plural': 'Cust Home Address',
            },
        ),
        migrations.CreateModel(
            name='BranchData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zone_name', models.CharField(max_length=12, verbose_name='Zone Name')),
                ('region_name', models.CharField(max_length=12, verbose_name='Region Name')),
                ('area_name', models.CharField(max_length=12, verbose_name='Area Name')),
                ('branch_name', models.CharField(max_length=12, verbose_name='Branch Name')),
                ('branch_code', models.CharField(max_length=12, verbose_name='Branch Code')),
                ('CustBranch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CustBranch', to='loan.customer')),
            ],
            options={
                'verbose_name': 'Branch data',
                'verbose_name_plural': 'Branch data',
            },
        ),
    ]
