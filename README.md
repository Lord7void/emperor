# Emperor of Cyber Darkness

**Emperor of Cyber Darkness** هو نظام سيبراني متقدم يعمل في بيئة Termux، مصمم لمحاكاة واجهات الذكاء الاصطناعي والهجمات الإلكترونية بطريقة خيالية وجذابة.

## مميزات النظام:

- واجهة ASCII مذهلة باستخدام `pyfiglet` و `rich`.
- أدوات متعددة (وهمية حالياً، قابلة للتوسعة مستقبلاً):
  - Neural Port Scanner
  - Cyber Payload Forge
  - AI IP Tracker
  - Quantum Keylogger Simulator
  - Drone Mapper
  - Photon Tunnel (Ngrok)
  - GPS Interceptor
  - MetaMind Payload
- دعم لتحديث جميع الأدوات بضغطة زر.
- نظام دخول بكلمة سر لحماية الوصول.
- متوافق مع Termux 100%.

---

## التثبيت على Termux:

```bash
pkg install git -y
git clone https://github.com/CyberDarkEmperor/emperor.git
cd emperor
chmod +x install.sh
./install.sh
