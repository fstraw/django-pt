# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Air',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('specialist', models.CharField(default=b'', max_length=50, choices=[(b'Employee 1', b'Employee 1'), (b'Employee 2', b'Employee 2'), (b'Employee 3', b'Employee 3'), (b'Employee 4', b'Employee 4'), (b'Employee 5', b'Employee 5')])),
                ('gdot_specialist', models.CharField(default=b'', max_length=50)),
                ('title', models.CharField(default=b'', max_length=50)),
                ('documenttype', models.CharField(default=b'', max_length=15)),
                ('draftsubmittal', models.DateField(null=True, blank=True)),
                ('draftapproval', models.DateField(null=True, blank=True)),
                ('duedate', models.DateField(null=True, blank=True)),
                ('comments', models.CharField(default=b'', max_length=1000, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Aquatics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('specialist', models.CharField(default=b'', max_length=50, choices=[(b'Employee 1', b'Employee 1'), (b'Employee 2', b'Employee 2'), (b'Employee 3', b'Employee 3'), (b'Employee 4', b'Employee 4'), (b'Employee 5', b'Employee 5')])),
                ('gdot_specialist', models.CharField(default=b'', max_length=50)),
                ('title', models.CharField(default=b'', max_length=50)),
                ('documenttype', models.CharField(default=b'', max_length=15)),
                ('draftsubmittal', models.DateField(null=True, blank=True)),
                ('draftapproval', models.DateField(null=True, blank=True)),
                ('duedate', models.DateField(null=True, blank=True)),
                ('comments', models.CharField(default=b'', max_length=1000, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Archaeology',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('specialist', models.CharField(default=b'', max_length=50, choices=[(b'Employee 1', b'Employee 1'), (b'Employee 2', b'Employee 2'), (b'Employee 3', b'Employee 3'), (b'Employee 4', b'Employee 4'), (b'Employee 5', b'Employee 5')])),
                ('gdot_specialist', models.CharField(default=b'', max_length=50)),
                ('title', models.CharField(default=b'', max_length=50)),
                ('documenttype', models.CharField(default=b'', max_length=15)),
                ('draftsubmittal', models.DateField(null=True, blank=True)),
                ('draftapproval', models.DateField(null=True, blank=True)),
                ('duedate', models.DateField(null=True, blank=True)),
                ('comments', models.CharField(default=b'', max_length=1000, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ecology',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('specialist', models.CharField(default=b'', max_length=50, choices=[(b'Employee 1', b'Employee 1'), (b'Employee 2', b'Employee 2'), (b'Employee 3', b'Employee 3'), (b'Employee 4', b'Employee 4'), (b'Employee 5', b'Employee 5')])),
                ('gdot_specialist', models.CharField(default=b'', max_length=50)),
                ('title', models.CharField(default=b'', max_length=50)),
                ('documenttype', models.CharField(default=b'', max_length=15)),
                ('draftsubmittal', models.DateField(null=True, blank=True)),
                ('draftapproval', models.DateField(null=True, blank=True)),
                ('duedate', models.DateField(null=True, blank=True)),
                ('comments', models.CharField(default=b'', max_length=1000, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('specialist', models.CharField(default=b'', max_length=50, choices=[(b'Employee 1', b'Employee 1'), (b'Employee 2', b'Employee 2'), (b'Employee 3', b'Employee 3'), (b'Employee 4', b'Employee 4'), (b'Employee 5', b'Employee 5')])),
                ('gdot_specialist', models.CharField(default=b'', max_length=50)),
                ('title', models.CharField(default=b'', max_length=50)),
                ('documenttype', models.CharField(default=b'', max_length=15)),
                ('draftsubmittal', models.DateField(null=True, blank=True)),
                ('draftapproval', models.DateField(null=True, blank=True)),
                ('duedate', models.DateField(null=True, blank=True)),
                ('comments', models.CharField(default=b'', max_length=1000, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Nepa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('specialist', models.CharField(default=b'', max_length=50, choices=[(b'Planner 1', b'Planner 1'), (b'Planner 2', b'Planner 2'), (b'Planner 3', b'Planner 3'), (b'Planner 4', b'Planner 4'), (b'Planner 5', b'Planner 5')])),
                ('stateplanner', models.CharField(default=b'', max_length=50)),
                ('documenttype', models.CharField(default=b'', max_length=15, choices=[(b'DocType 1', b'DocType 1'), (b'DocType 2', b'DocType 2'), (b'DocType 3', b'DocType 3'), (b'DocType 4', b'DocType 4'), (b'DocType 5', b'DocType 5')])),
                ('earlycoordination', models.DateField(null=True, blank=True)),
                ('statedraft', models.DateField(null=True, blank=True)),
                ('stateapproval', models.DateField(null=True, blank=True)),
                ('fhwadraft', models.DateField(null=True, blank=True)),
                ('fhwaapproval', models.DateField(null=True, blank=True)),
                ('statedraftdue', models.DateField(null=True, blank=True)),
                ('fhwadraftdue', models.DateField(null=True, blank=True)),
                ('comments', models.CharField(default=b'', max_length=1000, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Noise',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('specialist', models.CharField(default=b'', max_length=50, choices=[(b'Employee 1', b'Employee 1'), (b'Employee 2', b'Employee 2'), (b'Employee 3', b'Employee 3'), (b'Employee 4', b'Employee 4'), (b'Employee 5', b'Employee 5')])),
                ('gdot_specialist', models.CharField(default=b'', max_length=50)),
                ('title', models.CharField(default=b'', max_length=50)),
                ('documenttype', models.CharField(default=b'', max_length=15)),
                ('draftsubmittal', models.DateField(null=True, blank=True)),
                ('draftapproval', models.DateField(null=True, blank=True)),
                ('duedate', models.DateField(null=True, blank=True)),
                ('comments', models.CharField(default=b'', max_length=1000, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PINumbers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pi_number', models.CharField(max_length=7, unique=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'PI Numbers',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('jobnumber', models.CharField(default=b'', unique=True, max_length=15)),
                ('projectname', models.CharField(default=b'', max_length=100)),
                ('projectmanager', models.CharField(default=b'', max_length=25, choices=[(b'Manager 1', b'Manager 1'), (b'Manager 2', b'Manager 2'), (b'Manager 3', b'Manager 3'), (b'Manager 4', b'Manager 4'), (b'Manager 5', b'Manager 5')])),
                ('projectdescription', models.CharField(default=b'', max_length=1000, blank=True)),
                ('client', models.CharField(default=b'', max_length=30, blank=True)),
                ('county', models.CharField(default=b'', max_length=15, choices=[(b'Appling', b'Appling'), (b'Atkinson', b'Atkinson'), (b'Bacon', b'Bacon'), (b'Baker', b'Baker'), (b'Baldwin', b'Baldwin'), (b'Banks', b'Banks'), (b'Barrow', b'Barrow'), (b'Bartow', b'Bartow'), (b'Ben Hill', b'Ben Hill'), (b'Berrien', b'Berrien'), (b'Bibb', b'Bibb'), (b'Bleckley', b'Bleckley'), (b'Brantley', b'Brantley'), (b'Brooks', b'Brooks'), (b'Bryan', b'Bryan'), (b'Bulloch', b'Bulloch'), (b'Burke', b'Burke'), (b'Butts', b'Butts'), (b'Calhoun', b'Calhoun'), (b'Camden', b'Camden'), (b'Candler', b'Candler'), (b'Carroll', b'Carroll'), (b'Catoosa', b'Catoosa'), (b'Charlton', b'Charlton'), (b'Chatham', b'Chatham'), (b'Chattahoochee', b'Chattahoochee'), (b'Chattooga', b'Chattooga'), (b'Cherokee', b'Cherokee'), (b'Clarke', b'Clarke'), (b'Clay', b'Clay'), (b'Clayton', b'Clayton'), (b'Clinch', b'Clinch'), (b'Cobb', b'Cobb'), (b'Coffee', b'Coffee'), (b'Colquitt', b'Colquitt'), (b'Columbia', b'Columbia'), (b'Cook', b'Cook'), (b'Coweta', b'Coweta'), (b'Crawford', b'Crawford'), (b'Crisp', b'Crisp'), (b'Dade', b'Dade'), (b'Dawson', b'Dawson'), (b'DeKalb', b'DeKalb'), (b'Decatur', b'Decatur'), (b'Dodge', b'Dodge'), (b'Dooly', b'Dooly'), (b'Dougherty', b'Dougherty'), (b'Douglas', b'Douglas'), (b'Early', b'Early'), (b'Echols', b'Echols'), (b'Effingham', b'Effingham'), (b'Elbert', b'Elbert'), (b'Emanuel', b'Emanuel'), (b'Evans', b'Evans'), (b'Fannin', b'Fannin'), (b'Fayette', b'Fayette'), (b'Floyd', b'Floyd'), (b'Forsyth', b'Forsyth'), (b'Franklin', b'Franklin'), (b'Fulton', b'Fulton'), (b'Gilmer', b'Gilmer'), (b'Glascock', b'Glascock'), (b'Glynn', b'Glynn'), (b'Gordon', b'Gordon'), (b'Grady', b'Grady'), (b'Greene', b'Greene'), (b'Gwinnett', b'Gwinnett'), (b'Habersham', b'Habersham'), (b'Hall', b'Hall'), (b'Hancock', b'Hancock'), (b'Haralson', b'Haralson'), (b'Harris', b'Harris'), (b'Hart', b'Hart'), (b'Heard', b'Heard'), (b'Henry', b'Henry'), (b'Houston', b'Houston'), (b'Irwin', b'Irwin'), (b'Jackson', b'Jackson'), (b'Jasper', b'Jasper'), (b'Jeff Davis', b'Jeff Davis'), (b'Jefferson', b'Jefferson'), (b'Jenkins', b'Jenkins'), (b'Johnson', b'Johnson'), (b'Jones', b'Jones'), (b'Lamar', b'Lamar'), (b'Lanier', b'Lanier'), (b'Laurens', b'Laurens'), (b'Lee', b'Lee'), (b'Liberty', b'Liberty'), (b'Lincoln', b'Lincoln'), (b'Long', b'Long'), (b'Lowndes', b'Lowndes'), (b'Lumpkin', b'Lumpkin'), (b'Macon', b'Macon'), (b'Madison', b'Madison'), (b'Marion', b'Marion'), (b'McDuffie', b'McDuffie'), (b'McIntosh', b'McIntosh'), (b'Meriwether', b'Meriwether'), (b'Miller', b'Miller'), (b'Mitchell', b'Mitchell'), (b'Monroe', b'Monroe'), (b'Montgomery', b'Montgomery'), (b'Morgan', b'Morgan'), (b'Murray', b'Murray'), (b'Muscogee', b'Muscogee'), (b'Newton', b'Newton'), (b'Oconee', b'Oconee'), (b'Oglethorpe', b'Oglethorpe'), (b'Paulding', b'Paulding'), (b'Peach', b'Peach'), (b'Pickens', b'Pickens'), (b'Pierce', b'Pierce'), (b'Pike', b'Pike'), (b'Polk', b'Polk'), (b'Pulaski', b'Pulaski'), (b'Putnam', b'Putnam'), (b'Quitman', b'Quitman'), (b'Rabun', b'Rabun'), (b'Randolph', b'Randolph'), (b'Richmond', b'Richmond'), (b'Rockdale', b'Rockdale'), (b'Schley', b'Schley'), (b'Screven', b'Screven'), (b'Seminole', b'Seminole'), (b'Spalding', b'Spalding'), (b'Stephens', b'Stephens'), (b'Stewart', b'Stewart'), (b'Sumter', b'Sumter'), (b'Talbot', b'Talbot'), (b'Taliaferro', b'Taliaferro'), (b'Tattnall', b'Tattnall'), (b'Taylor', b'Taylor'), (b'Telfair', b'Telfair'), (b'Terrell', b'Terrell'), (b'Thomas', b'Thomas'), (b'Tift', b'Tift'), (b'Toombs', b'Toombs'), (b'Towns', b'Towns'), (b'Treutlen', b'Treutlen'), (b'Troup', b'Troup'), (b'Turner', b'Turner'), (b'Twiggs', b'Twiggs'), (b'Union', b'Union'), (b'Upson', b'Upson'), (b'Walker', b'Walker'), (b'Walton', b'Walton'), (b'Ware', b'Ware'), (b'Warren', b'Warren'), (b'Washington', b'Washington'), (b'Wayne', b'Wayne'), (b'Webster', b'Webster'), (b'Wheeler', b'Wheeler'), (b'White', b'White'), (b'Whitfield', b'Whitfield'), (b'Wilcox', b'Wilcox'), (b'Wilkes', b'Wilkes'), (b'Wilkinson', b'Wilkinson'), (b'Worth', b'Worth')])),
                ('env_cert_row', models.DateField(null=True, blank=True)),
                ('env_cert_let', models.DateField(null=True, blank=True)),
                ('row_auth', models.DateField(null=True, blank=True)),
                ('let_cert', models.DateField(null=True, blank=True)),
                ('pfpr', models.DateField(null=True, blank=True)),
                ('ffpr', models.DateField(null=True, blank=True)),
                ('comments', models.CharField(default=b'', max_length=2000, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectNumbers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('project_number', models.CharField(max_length=20, unique=True, null=True)),
                ('projects', models.ManyToManyField(related_name='projectnumbers', to='pt.Project')),
            ],
            options={
                'verbose_name_plural': 'Project Numbers',
            },
        ),
        migrations.AddField(
            model_name='pinumbers',
            name='projects',
            field=models.ManyToManyField(related_name='pis', to='pt.Project'),
        ),
        migrations.AddField(
            model_name='noise',
            name='project',
            field=models.ForeignKey(default=b'', to='pt.Project'),
        ),
        migrations.AddField(
            model_name='nepa',
            name='project',
            field=models.ForeignKey(default=b'', to='pt.Project'),
        ),
        migrations.AddField(
            model_name='history',
            name='project',
            field=models.ForeignKey(default=b'', to='pt.Project'),
        ),
        migrations.AddField(
            model_name='ecology',
            name='project',
            field=models.ForeignKey(default=b'', to='pt.Project'),
        ),
        migrations.AddField(
            model_name='archaeology',
            name='project',
            field=models.ForeignKey(default=b'', to='pt.Project'),
        ),
        migrations.AddField(
            model_name='aquatics',
            name='project',
            field=models.ForeignKey(default=b'', to='pt.Project'),
        ),
        migrations.AddField(
            model_name='air',
            name='project',
            field=models.ForeignKey(default=b'', to='pt.Project'),
        ),
    ]
