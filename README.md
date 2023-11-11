# linkit_7688_duo_sht30
 由於MediaTek(聯發科) 已經將此專案關閉了，所以目前網路上找到的Arduino package 都已失效，找了好久發現MediaTek有把最後的package放在github上
 不過是python2.7時代，所以要想辦法把python降回2.7然後重新打包成zip檔，之後重新編寫json檔案for Arduino 使用
 所以我把打包好的zip跟json放在這邊給大家使用，只要放到自己的web 底下就可以

 Since MediaTek has already closed Linkit7688(Duo) project, the Arduino packages found online are no longer valid. After searching for a while, I found that MediaTek had put the last package on GitHub. However, it used Python tool chain, so we needs to downgrade Python to 2.7 and then rebuild the project. Subsequently, one would need to rewrite the JSON file for Arduino IDE. So, I've upload zip and JSON file here for everyone to use. You can simply place it on your web server.


## How to Use
1.modify url in "package_mtk_linkit_smart_7688_index.json" file
from http://localhost to Your Website URL 

2. Open  Arduino Preferences--> Boards Manager URLs
   add your website url such as "http://localhost/package_mtk_linkit_smart_7688_index.json"


##gauge.html
1.modift FASTAPI_IP to your fastapi ip address
2.change gauge.js url
