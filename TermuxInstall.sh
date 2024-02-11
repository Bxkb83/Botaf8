# @FnarkBey - < https://t.me/FnarkBey >
# Copyright (C) 2022
# Tüm hakları saklıdır.
#
# Bu dosya, < https://github.com/Bxkb83-github/PyFileLock > parçasıdır.
# Lütfen GNU Affero Genel Kamu Lisansını okuyun;
# < https://github.com/Bxkb83/Botaf8/blob/main/LICENSE/ >
# ================================================================

DOGE="🔐 PyFileLock kütüphanesi kuruluyor..."
INFOX="📣 Telegram: @FnarkBey"
INFOX+="\n "
INFOX+="\n💬 Destek Grubu: @Zirve_Sohbett"
INFOX+="\n "
INFOX+="\n💫 İŞLEM DEVAM EDERKEN UYGULAMADAN AYRILMAYIN!"
PACKAGEX="\n⏳ PAKETLERİ GÜNCELLİYORUM..."
PYTHOX="\n⌛ PYTHON KURUYORUM..."
REQUIREX="\n⌛ GEREKSİNİMLERİ KURUYORUM..."
SPACEX="\n "
clear
echo -e $DOGE
echo -e $SPACEX
echo -e $SPACEX
echo -e $PACKAGEX
echo -e $SPACEX
pkg update -y
clear
echo -e $DOGE
echo -e $SPACEX
echo -e $INFOX
echo -e $SPACEX
echo -e $PYTHOX
echo -e $SPACEX
pkg install python -y
pip install --upgrade pip
clear
echo -e $DOGE
echo -e $SPACEX
echo -e $INFOX
echo -e $SPACEX
echo -e $REQUIREX
echo -e $SPACEX
pip install wheel
pip install -U WichRider
python3 -m WichRider
