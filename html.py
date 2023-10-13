def html_func(user, ise, kee):
    html = f'''
        <!DOCTYPE html>
    <html xmlns="http://www.w3.org/1999/xhtml">
    
    <head>
        <meta charset="utf-8">
        <!-- utf-8 works for most cases -->
        <meta name="viewport" content="width=device-width">
        <!-- Forcing initial-scale shouldn't be necessary -->
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <!-- Use the latest (edge) version of IE rendering engine -->
        <meta name="x-apple-disable-message-reformatting">
        <!-- Disable auto-scale in iOS 10 Mail entirely -->
        <title></title>
        <!-- Web Font / @font-face : BEGIN -->
        <!--[if mso]>
           
    </head>
    
    <body width="100%" bgcolor="#F2F2F2" style="margin: 0; mso-line-height-rule: exactly;">
        <center style="width: 100%; background: #F2F2F2;">
            <!-- Visually Hidden Preheader Text : BEGIN -->
            <div style="display:none;font-size:1px;line-height:1px;max-height:0px;max-width:0px;opacity:0;overflow:hidden;mso-hide:all;font-family: sans-serif;"> Добро пожаловать в Сабетту! </div>
            <!-- Visually Hidden Preheader Text : END -->
            <div style="max-width: 680px; margin: auto;" class="email-container">
                <table role="presentation" cellspacing="0" cellpadding="0" border="0" align="center" width="100%" style="max-width: 680px;">
                    <tr>
                        <td style="padding: 20px 0; text-align: center"> 
                    </tr>
                </table>
    
                <table role="presentation" cellspacing="0" cellpadding="0" border="0" align="center" width="100%" style="max-width: 680px;">
    
                    <tr>
                        <td bgcolor="#ffffff"> 
    
                    </tr>
    
                    <tr>
                        <td bgcolor="#ffffff">
                            <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
                                <tr>
                                    <td style="padding: 20px 40px; font-family: sans-serif; font-size: 15px; line-height: 20px; color: #555555; text-align: center;">
                                        <h1 style="margin: 10px">Добро пожаловать в Сабетту! </h1>
                                       <p>Доступ к сервисам ниже поможет на старте работы.</p>
                                    </td>
                                </tr>
                            </table>
                        </td>
                                    <tr>
                                        <!-- dir=ltr is where the magic happens. This can be changed to dir=rtl to swap the alignment on wide while maintaining stack order on narrow. -->
                                        <td dir="ltr" bgcolor="#ffffff" align="center" height="100%" valign="top" width="100%" style="padding: 0px 0;">
    
                                            <table role="presentation" border="0" cellpadding="0" cellspacing="0" align="center" width="100%" style="max-width:600px;">
                                                <tr>
                                                    <td align="center" valign="top" style="font-size:0; padding: 0px 0;">
                                                        <div style="display:inline-block; margin: 0 -2px; max-width:66.66%; min-width:320px; vertical-align:top;" class="stack-column">
                                                            <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
                                                                <tr>
                                                                    <td dir="ltr" style="font-family: sans-serif; font-size: 15px; line-height: 23px; color: #555555; padding: 10px 20px 10px 20px; text-align: left;" class="action-items">
                                                                        <h1 style="display:block;font-size:23px;font-style:normal;font-weight:bold;line-height:28px;letter-spacing:normal;margin: 0px 70px 10px;color:rgb(46,46,46);padding-bottom:0px;text-align:left" class="center-on-narrow">Мастер-Пароль</h1>
    
                                                                        <p style="display: block;font-family: Helvetica, Arial, sans-serif;font-size: 17px;font-weight: lighter;line-height: 24px;letter-spacing: normal;margin: 0px 70px 10px;color: #616161;">Используйте корпоративную почту с личных устройств.</p>
                                                                        <p style="display: block;font-family: Helvetica, Arial, sans-serif;font-size: 17px;font-weight: lighter;line-height: 24px;letter-spacing: normal;margin: 0px 70px 10px;color: #616161;"><b>Логин:</b> msk\\{user}<br>
                                                                        <b>Пароль: </b>{kee}</p>
                                                                    </td>
                                                                </tr>
                                                            </table>
                                                        </div>
                                                    </td>
                                                </tr>
                                            </table>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td dir="ltr" bgcolor="#ffffff" align="center" height="100%" valign="top" width="100%" style="padding: 0px 0;">
                                            <table role="presentation" border="0" cellpadding="0" cellspacing="0" align="center" width="100%" style="max-width:600px;">
                                                <tr>
                                                    <td align="center" valign="top" style="font-size:0; padding: 0px 0;">
                                                        <div style="display:inline-block; margin: 0 -2px; max-width:66.66%; min-width:320px; vertical-align:top;" class="stack-column">
                                                            <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
                                                                <tr>
                                                                    <td dir="ltr" style="font-family: sans-serif; font-size: 15px; line-height: 20px; color: #555555; padding: 10px 20px 10px 20px; text-align: left;" class="action-items">
                                                                        <h1 style="display:block;font-size:24px;font-style:normal;font-weight:bold;line-height:28px;letter-spacing:normal;margin: 0px 70px 10px;color:rgb(46,46,46);padding-bottom:0px;text-align:left" class="center-on-narrow">Пароль Wi-Fi</h1>
    
                                                                        <p style="display: block;font-family: Helvetica, Arial, sans-serif;font-size: 17px;font-weight: lighter;line-height: 24px;letter-spacing: normal;margin: 0px 70px 10px;color: #616161;">Используйте беспроводную сеть YLNG_USERS.</p>
                                                                        <p style="display: block;font-family: Helvetica, Arial, sans-serif;font-size: 17px;font-weight: lighter;line-height: 24px;letter-spacing: normal;margin: 0px 70px 10px;color: #616161;"><b>Логин:</b> {user}<br>
                                                                        <b>Пароль:</b> {ise}</p>
                                                                    </td>
                                                                </tr>
                                                            </table>
                                                        </div>
                                                    </td>
                                                </tr>
                                            </table>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td dir="ltr" bgcolor="#ffffff" align="center" height="100%" valign="top" width="100%" style="padding: 0px 0;">
                                            <table role="presentation" border="0" cellpadding="0" cellspacing="0" align="center" width="100%" style="max-width:600px;">
                                                <tr>
                                                    <td align="center" valign="top" style="font-size:0; padding: 0px 0;">
                                                        <div style="display:inline-block; margin: 0 -2px; max-width:66.66%; min-width:320px; vertical-align:top;" class="stack-column">
                                                            <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
                                                                <tr>
                                                                    <td dir="ltr" style="font-family: sans-serif; font-size: 15px; line-height: 20px; color: #555555; padding: 10px 20px 10px 20px; text-align: left;" class="action-items">
                                                                        <h1 style="display:block;font-size:24px;font-style:normal;font-weight:bold;line-height:28px;letter-spacing:normal;margin: 0px 70px 10px;color:rgb(46,46,46);padding-bottom:0px;text-align:left" class="center-on-narrow">Горячая линия 42-222</h1>
                                                                        <p style="display: block;font-family: Helvetica, Arial, sans-serif;font-size: 17px;font-weight: lighter;line-height: 24px;letter-spacing: normal;margin: 0px 70px 10px;color: #616161;">Не получилось самостоятельно настроить личные устройства? Не переживайте. Специалисты технической поддержки проконсультируют Вас.</p>
                                                                    </td>
                                                                </tr>
                                                            </table>
                                                        </div>
                                                    </td>
                                                </tr>
                                            </table>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td bgcolor="#ffffff">
                                            <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
                                                <tr>
                                                    <td align="center" style="padding: 40px; font-family: sans-serif; font-size: 15px; line-height: 20px; color: #555555;">
                                                        <h2 style="margin: 10px">Спасибо<h2>
                                                        <h4> Более подробные инструкции &mdash; <a href="Q:\Public\IT\Инструкции" style="color:#2E93CE; text-decoration:none">Q:\Public\IT\Инструкции</a> </h4>
                                                                                                            </td>
                                            </table>
                                        </td>
                                        </tr>
                            </table>
                            <table align="center" border="0" cellpadding="0" cellspacing="0" role="presentation" style="max-width: 680px;" width="100%">
                                <tr>
                                    <td style="background-color:#F2F2F2; padding: 40px 10px;width: 100%;font-size: 12px; font-family: sans-serif; line-height:18px; text-align: center; color: #888888;">
                                        <br> <span class="mobile-link--footer">Ямал СПГ</span>
                                        <br> <span class="mobile-link--footer">Сабетта</span>
    
    
                                </tr>
                            </table>
                </td>
                </tr>
                </table>
                <![endif]-->
            </div>
        </center>
    </body>
    
    </html>
    '''
    return html