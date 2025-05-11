#!/data/data/com.termux/files/usr/bin/bash

clear
echo -e "\e[1;35m[+] Installing Emperor of Cyber Darkness...\e[0m"

# تحديث الحزم
pkg update -y && pkg upgrade -y

# تثبيت المتطلبات
pkg install -y python git figlet toilet
pip install rich pyfiglet

# إنشاء أمر تشغيل مباشر
chmod +x emperor.py
mkdir -p $PREFIX/bin
echo -e "#!/bin/bash\ncd $(pwd) && python emperor.py" > $PREFIX/bin/emperor
chmod +x $PREFIX/bin/emperor

echo -e "\e[1;32m[+] Installation Complete!"
echo -e "[*] You can now run the system by typing: \e[1;36memperor\e[0m"
