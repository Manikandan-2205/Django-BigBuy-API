# Generated by Django 5.1.5 on 2025-02-14 07:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Brand",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("brandname", models.CharField(max_length=50)),
                ("createdby", models.IntegerField()),
                ("createdtime", models.DateTimeField(auto_now_add=True)),
                ("updatedby", models.IntegerField(blank=True, null=True)),
                ("updatedtime", models.DateTimeField(auto_now=True, null=True)),
                ("isdeleted", models.CharField(default="N", max_length=1)),
                ("isactive", models.CharField(default="N", max_length=1)),
            ],
            options={
                "db_table": "TB_BB_PRODUCT_BRAND",
            },
        ),
        migrations.CreateModel(
            name="Department",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("department", models.CharField(max_length=50, unique=True)),
                ("isdeleted", models.CharField(default="N", max_length=1)),
                ("isactive", models.CharField(default="N", max_length=1)),
            ],
            options={
                "db_table": "TB_BB_DEPARTMENT",
            },
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("orderid", models.CharField(max_length=10, unique=True)),
                ("orderqty", models.IntegerField()),
                ("createdby", models.IntegerField()),
                ("createdtime", models.DateTimeField(auto_now_add=True)),
                ("updatedby", models.IntegerField(blank=True, null=True)),
                ("updatedtime", models.DateTimeField(auto_now=True, null=True)),
                ("isdeleted", models.CharField(default="N", max_length=1)),
            ],
            options={
                "db_table": "TB_BB_ORDERR",
            },
        ),
        migrations.CreateModel(
            name="ProductCategory",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("productcategory", models.CharField(max_length=50)),
                ("createdby", models.IntegerField()),
                ("createdtime", models.DateTimeField(auto_now_add=True)),
                ("updatedby", models.IntegerField(blank=True, null=True)),
                ("updatedtime", models.DateTimeField(auto_now=True, null=True)),
                ("isdeleted", models.CharField(default="N", max_length=1)),
                ("isactive", models.CharField(default="N", max_length=1)),
            ],
            options={
                "db_table": "TB_BB_PRODUCT_CATEORY",
            },
        ),
        migrations.CreateModel(
            name="Role",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("rolename", models.CharField(max_length=50, unique=True)),
                ("isdeleted", models.CharField(default="N", max_length=1)),
                ("isactive", models.CharField(default="N", max_length=1)),
            ],
            options={
                "db_table": "TB_BB_ROLE",
            },
        ),
        migrations.CreateModel(
            name="OrderTransaction",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("rating", models.IntegerField(default=0)),
                ("remark", models.CharField(blank=True, max_length=1000, null=True)),
                ("createdby", models.IntegerField()),
                ("createdtime", models.DateTimeField(auto_now_add=True)),
                ("updatedby", models.IntegerField(blank=True, null=True)),
                ("updatedtime", models.DateTimeField(auto_now=True, null=True)),
                ("isdeleted", models.CharField(default="N", max_length=1)),
                ("iscanceled", models.CharField(default="N", max_length=1)),
                ("isreturn", models.CharField(default="N", max_length=1)),
                (
                    "orderid",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="BigBuyAPI.order",
                    ),
                ),
            ],
            options={
                "db_table": "TB_BB_ORDERR_TRANS",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("productname", models.CharField(max_length=50)),
                ("createdby", models.IntegerField()),
                ("createdtime", models.DateTimeField(auto_now_add=True)),
                ("updatedby", models.IntegerField(blank=True, null=True)),
                ("updatedtime", models.DateTimeField(auto_now=True, null=True)),
                ("isdeleted", models.CharField(default="N", max_length=1)),
                ("isactive", models.CharField(default="N", max_length=1)),
                (
                    "brand",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="BigBuyAPI.brand",
                    ),
                ),
                (
                    "productcategory",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="BigBuyAPI.productcategory",
                    ),
                ),
            ],
            options={
                "db_table": "TB_BB_PRODUCT",
            },
        ),
        migrations.AddField(
            model_name="order",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="BigBuyAPI.product"
            ),
        ),
        migrations.CreateModel(
            name="ProductDetails",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("model", models.CharField(max_length=50)),
                ("color", models.CharField(max_length=50)),
                ("imageurl", models.CharField(max_length=300)),
                ("yearofmanufacturing", models.IntegerField()),
                ("rate", models.DecimalField(decimal_places=3, max_digits=7)),
                ("createdby", models.IntegerField()),
                ("createdtime", models.DateTimeField(auto_now_add=True)),
                ("updatedby", models.IntegerField(blank=True, null=True)),
                ("updatedtime", models.DateTimeField(auto_now=True, null=True)),
                ("isdeleted", models.CharField(default="N", max_length=1)),
                ("isactive", models.CharField(default="N", max_length=1)),
                (
                    "productname",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="BigBuyAPI.product",
                    ),
                ),
            ],
            options={
                "db_table": "TB_BB_PRODUCT_DETAILS",
            },
        ),
        migrations.CreateModel(
            name="ProductStack",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("qty", models.IntegerField()),
                ("createdby", models.IntegerField()),
                ("createdtime", models.DateTimeField(auto_now_add=True)),
                ("updatedby", models.IntegerField(blank=True, null=True)),
                ("updatedtime", models.DateTimeField(auto_now=True, null=True)),
                ("isdeleted", models.CharField(default="N", max_length=1)),
                ("isactive", models.CharField(default="N", max_length=1)),
                (
                    "productname",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="BigBuyAPI.product",
                    ),
                ),
            ],
            options={
                "db_table": "TB_BB_PRODUCT_STACK",
            },
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("username", models.CharField(max_length=50, unique=True)),
                ("displayname", models.CharField(max_length=50)),
                ("emailid", models.CharField(max_length=100)),
                ("age", models.IntegerField()),
                ("mobileno", models.CharField(max_length=15)),
                ("password", models.CharField(max_length=200)),
                (
                    "profilename",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("createdby", models.IntegerField()),
                ("createdtime", models.DateTimeField(auto_now_add=True)),
                ("updatedby", models.IntegerField(blank=True, null=True)),
                ("updatedtime", models.DateTimeField(auto_now=True, null=True)),
                ("isdeleted", models.CharField(default="N", max_length=1)),
                ("isactive", models.CharField(default="N", max_length=1)),
                (
                    "role",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="BigBuyAPI.role",
                    ),
                ),
            ],
            options={
                "db_table": "TB_BB_USER",
            },
        ),
        migrations.CreateModel(
            name="UserAddress",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("usertype", models.IntegerField()),
                ("addressline1", models.CharField(max_length=100)),
                ("city", models.CharField(max_length=50)),
                ("state", models.CharField(max_length=50)),
                ("country", models.CharField(max_length=50)),
                ("createdby", models.IntegerField()),
                ("createdtime", models.DateTimeField(auto_now_add=True)),
                ("updatedby", models.IntegerField(blank=True, null=True)),
                ("updatedtime", models.DateTimeField(auto_now=True, null=True)),
                ("isdeleted", models.CharField(default="N", max_length=1)),
                ("isactive", models.CharField(default="N", max_length=1)),
                (
                    "userid",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="BigBuyAPI.user"
                    ),
                ),
            ],
            options={
                "db_table": "TB_BB_USER_ADDRESS",
            },
        ),
        migrations.CreateModel(
            name="Employee",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("employeeid", models.IntegerField()),
                ("username", models.CharField(max_length=50)),
                ("displayname", models.CharField(max_length=50)),
                ("emailid", models.CharField(max_length=100)),
                ("age", models.IntegerField()),
                ("mobileno", models.CharField(max_length=15)),
                ("password", models.CharField(max_length=200)),
                (
                    "profilename",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("createdby", models.IntegerField()),
                ("createdtime", models.DateTimeField(auto_now_add=True)),
                ("updatedby", models.IntegerField(blank=True, null=True)),
                ("updatedtime", models.DateTimeField(auto_now=True, null=True)),
                ("isdeleted", models.CharField(default="N", max_length=1)),
                ("isactive", models.CharField(default="N", max_length=1)),
                (
                    "department",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="BigBuyAPI.department",
                    ),
                ),
                (
                    "role",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="BigBuyAPI.role"
                    ),
                ),
            ],
            options={
                "db_table": "TB_BB_EMPLOYEE",
                "constraints": [
                    models.CheckConstraint(
                        condition=models.Q(("age__gte", 18)), name="age_gte_18"
                    )
                ],
            },
        ),
    ]
