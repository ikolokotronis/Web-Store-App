function e(n){return(e="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(e){return typeof e}:function(e){return e&&"function"==typeof Symbol&&e.constructor===Symbol&&e!==Symbol.prototype?"symbol":typeof e})(n)}if("undefined"==typeof gemius_cmpclient&&(gemius_cmpclient={gemius_vendor_id:328,cmp_frame:null,cmp_callbacks:{},add_event:function(e,n,i){e.addEventListener?e.addEventListener(n,i,!1):e.attachEvent&&e.attachEvent("on"+n,i)},find_cmp_frame:function(e){for(var n=window;!gemius_cmpclient.cmp_frame;){try{if(n.frames[e])return gemius_cmpclient.cmp_frame=n,!0}catch(e){}if(n===window.top)break;n=n.parent}return!1},add_cmp_event:function(e){gemius_cmpclient.add_event(window,"message",(function(n){try{var i="string"==typeof n.data?JSON.parse(n.data):n.data;if(i[e]){var c=i[e];gemius_cmpclient.cmp_callbacks[c.callId](c.returnValue,c.success)}}catch(e){}}))},find_cmp_v1:function(){return!(!gemius_cmpclient.__cmp&&("function"==typeof window.__cmp?(gemius_cmpclient.__cmp=function(){window.__cmp.apply(this,arguments)},0):!gemius_cmpclient.find_cmp_frame("__cmpLocator")||(gemius_cmpclient.add_cmp_event("__cmpReturn"),gemius_cmpclient.__cmp=function(e,n,i){var c=Math.random()+"",t={__cmpCall:{command:e,parameter:n,callId:c}};gemius_cmpclient.cmp_callbacks[c]=i,gemius_cmpclient.cmp_frame.postMessage(t,"*")},0)))},find_cmp_v2:function(){return!(!gemius_cmpclient.__tcfapi&&("function"==typeof window.__tcfapi?(gemius_cmpclient.__tcfapi=function(){window.__tcfapi.apply(this,arguments)},0):!gemius_cmpclient.find_cmp_frame("__tcfapiLocator")||(gemius_cmpclient.add_cmp_event("__tcfapiReturn"),gemius_cmpclient.__tcfapi=function(e,n,i,c){var t=Math.random()+"",o={__tcfapiCall:{command:e,parameter:c,version:n,callId:t}};gemius_cmpclient.cmp_callbacks[t]=i,gemius_cmpclient.cmp_frame.postMessage(o,"*")},0)))},find_cmp:function(){return!!gemius_cmpclient.find_cmp_v2()||gemius_cmpclient.find_cmp_v1()},has_consent_v1:function(e,n){try{if(!e.vendorConsents[gemius_cmpclient.gemius_vendor_id])return!1;for(var i=0;i<n.length;i++)if(!e.purposeConsents[n[i]])return!1}catch(e){return!1}return!0},cmp_callback_v1:function(e,n){var i=!1;return function(c,t){i||(i=!0,e(t&&gemius_cmpclient.has_consent_v1(c,n)))}},has_consent_v2:function(e,n){try{if("boolean"==typeof e.gdprApplies&&!e.gdprApplies)return!0;if(!e.vendor.consents[gemius_cmpclient.gemius_vendor_id])return!1;for(var i=0;i<n.length;i++)if(1!=n[i]||!0!==e.purposeOneTreatment){var c=1;try{c=e.publisher.restrictions[n[i]][gemius_cmpclient.gemius_vendor_id]}catch(e){}if(!e.purpose.consents[n[i]]||0==c)return!1}}catch(e){return!1}return!0},cmp_callback_v2:function(e,n){var i=!1;return function(c,t){!t||"tcloaded"!==c.eventStatus&&"useractioncomplete"!==c.eventStatus||gemius_cmpclient.__tcfapi("removeEventListener",2,(function(t){i||(i=!0,e(t&&gemius_cmpclient.has_consent_v2(c,n)))}),c.listenerId)}},get_consent:function(e,n){"function"==typeof gemius_cmpclient.__tcfapi?gemius_cmpclient.__tcfapi("addEventListener",2,gemius_cmpclient.cmp_callback_v2(e,n[2])):"function"==typeof gemius_cmpclient.__cmp?gemius_cmpclient.__cmp("getVendorConsents",[gemius_cmpclient.gemius_vendor_id],gemius_cmpclient.cmp_callback_v1(e,n[1])):e(!1)}}),"undefined"==typeof gemius_hcconn){gemius_hcconn={version:322,lsdata:"",fpdata:"",gdprdisabled:0,gdprdata:[],gdprversion:null,cmp_found:0,gdpr_found:0,event_identifier:null,current_receiver:null,waiting_for_fpdata:1,waiting_for_lsdata:1,params_ready_called:0,fpdata_ready_called:0,fpdata_callbacks:[],gsconf_added:0,waiting_on_prerender:1,waiting_for_consent:1,require_consent_info:0,has_consent:null,closing:0,visapi_s:"",visapi_h:"",visapi_c:"",loadinit:0,fto:null,addto:null,sto:null,cmpto:null,ltime:0,lsgetframe:null,sonar_data:null,sonar_auto_init:0,timerevents:[],requests:[],images:[],state:0,flashv:"",src:document.currentScript&&document.currentScript.src?document.currentScript.src:null,ssl:"string"==typeof gemius_proto?"https"==gemius_proto.substr(0,5)?1:0:"string"==typeof pp_gemius_proto?"https"==pp_gemius_proto.substr(0,5)?1:0:document.location&&document.location.protocol&&"https:"==document.location.protocol?1:0,hc:"string"==typeof gemius_hitcollector?gemius_hitcollector:"string"==typeof pp_gemius_hitcollector?pp_gemius_hitcollector:"gapl.hit.gemius.pl",dnt:"undefined"!=typeof gemius_dnt&&gemius_dnt||"undefined"!=typeof pp_gemius_dnt&&pp_gemius_dnt?1:0,use_cmp:"undefined"!=typeof gemius_use_cmp&&gemius_use_cmp||"undefined"!=typeof pp_gemius_use_cmp&&pp_gemius_use_cmp?1:0,cmp_purposes_overrides:"undefined"!=typeof gemius_cmp_purposes?gemius_cmp_purposes:"undefined"!=typeof pp_gemius_cmp_purposes?pp_gemius_cmp_purposes:null,cmp_timeout:"number"==typeof gemius_cmp_timeout?gemius_cmp_timeout:"number"==typeof pp_gemius_cmp_timeout?pp_gemius_cmp_timeout:1e4,dmp_purpose:"boolean"==typeof gemius_dmp_purpose?gemius_dmp_purpose:"boolean"==typeof pp_gemius_dmp_purpose&&pp_gemius_dmp_purpose,gdpr_applies:"undefined"!=typeof gemius_gdpr_applies?gemius_gdpr_applies:"undefined"!=typeof pp_gemius_gdpr_applies?pp_gemius_gdpr_applies:null,gdpr_consent:"undefined"!=typeof gemius_gdpr_consent?gemius_gdpr_consent:"undefined"!=typeof pp_gemius_gdpr_consent?pp_gemius_gdpr_consent:null,explicit_consent:"boolean"==typeof gemius_consent?gemius_consent:"boolean"==typeof pp_gemius_consent?pp_gemius_consent:null,use_gsync:"boolean"==typeof gemius_disable_gsync?!gemius_disable_gsync:"boolean"!=typeof pp_gemius_disable_gsync||!pp_gemius_disable_gsync,add_event:function(e,n,i){e.addEventListener?e.addEventListener(n,i,!1):e.attachEvent&&e.attachEvent("on"+n,i)},remove_script:function(e,n){var i=document.getElementById(e);if(i){if(n)try{"undefined"!=typeof gemius_notify?gemius_notify(n):"undefined"!=typeof pp_gemius_notify&&pp_gemius_notify(n)}catch(e){}try{i.parentNode.removeChild(i)}catch(e){}}},append_script:function(e,n,i){var c="gemius_hcconn_"+(new Date).getTime()+"_"+Math.floor(1e8*Math.random());try{var t=document.createElement("script"),o=document.getElementsByTagName("script")[0];null!=n&&(gemius_hcconn.add_event(t,"load",n),gemius_hcconn.add_event(t,"error",n),gemius_hcconn.add_event(t,"readystatechange",(function(){t.readyState&&"loaded"!==t.readyState&&"complete"!==t.readyState||n()}))),gemius_hcconn.add_event(t,"load",(function(){gemius_hcconn.remove_script(c,i?e:null)})),gemius_hcconn.add_event(t,"error",(function(){gemius_hcconn.remove_script(c,null)})),gemius_hcconn.add_event(t,"readystatechange",(function(){t.readyState&&"loaded"!==t.readyState&&"complete"!==t.readyState||gemius_hcconn.remove_script(c,i?e:null)})),t.setAttribute("id",c),t.setAttribute("defer","defer"),t.setAttribute("async","async"),t.setAttribute("type","text/javascript"),t.setAttribute("src",e),o?o.parentNode.insertBefore(t,o):document.body&&document.body.appendChild(t)}catch(e){}},xdot_loaded:function(){"undefined"==typeof gemius_open&&(gemius_hcconn.state=0)},sendhits:function(e){var n;if(0==gemius_hcconn.waiting_for_fpdata&&0==gemius_hcconn.waiting_for_lsdata&&0==gemius_hcconn.waiting_on_prerender&&(0==gemius_hcconn.require_consent_info||0==gemius_hcconn.waiting_for_consent)){for(n=0;n<gemius_hcconn.requests.length;n++){var i=gemius_hcconn.requests[n],c=(gemius_hcconn.hssl?"https://":"http://")+gemius_hcconn.hc+"/_",t=(new Date).getTime(),o=""==gemius_hcconn.visapi_h?3:document[gemius_hcconn.visapi_h]?2:1,s="&ltime="+gemius_hcconn.ltime+"&lsdata="+gemius_hcconn.lsdata+"&fpdata="+gemius_hcconn.getrawfpdata()+"&vis="+o;if(0==gemius_hcconn.ssl&&null!==e&&(s+="&lsadd="+e),!0!==gemius_hcconn.has_consent?s+="&nc=1":!0===gemius_hcconn.explicit_consent&&(s+="&nc=0"),gemius_hcconn.closing)if(c+=t+n+"/redot.gif?l="+i.vers+i.req+s,"function"==typeof navigator.sendBeacon)navigator.sendBeacon(c);else{var _=gemius_hcconn.images.length;gemius_hcconn.images[_]=new Image,gemius_hcconn.images[_].src=c}else gemius_hcconn.state>0||0==i.allowaddscript||"undefined"!=typeof gemius_open?(c+=t+n+"/redot.js?l="+i.vers+i.req+s,gemius_hcconn.append_script(c,null,1)):(c+=t+n+"/rexdot.js?l="+i.vers+i.req+s,gemius_hcconn.state=1,gemius_hcconn.append_script(c,gemius_hcconn.xdot_loaded,1))}gemius_hcconn.requests=[]}},latehits:function(){if(0==gemius_hcconn.waiting_for_fpdata&&0==gemius_hcconn.waiting_for_lsdata&&0==gemius_hcconn.waiting_on_prerender)if(0==gemius_hcconn.closing&&0==gemius_hcconn.ssl&&""!=gemius_hcconn.lsdata&&"-"!=gemius_hcconn.lsdata[0]&&gemius_hcconn.lsgetframe){if(null==gemius_hcconn.addto)try{gemius_hcconn.lsgetframe.contentWindow.postMessage("_xx_gemius_get_add_xx_","*"),gemius_hcconn.addto=setTimeout(gemius_hcconn.lsaddto,250)}catch(e){gemius_hcconn.sendhits(null)}}else gemius_hcconn.sendhits(null)},lsaddto:function(){null!=gemius_hcconn.addto&&(gemius_hcconn.addto=null,gemius_hcconn.sendhits(null))},add_fpdata_callback:function(e){if(0==gemius_hcconn.fpdata_ready_called)gemius_hcconn.fpdata_callbacks[gemius_hcconn.fpdata_callbacks.length]=e;else try{e(gemius_hcconn.getrawfpdata())}catch(e){}},paramsready:function(){if(1!=gemius_hcconn.waiting_for_consent){if(0==gemius_hcconn.fpdata_ready_called&&0==gemius_hcconn.waiting_for_fpdata){gemius_hcconn.fpdata_ready_called=1;for(var e=0;e<gemius_hcconn.fpdata_callbacks.length;e++)try{gemius_hcconn.fpdata_callbacks[e](gemius_hcconn.getrawfpdata())}catch(e){}}if(0==gemius_hcconn.params_ready_called&&0==gemius_hcconn.waiting_for_fpdata&&0==gemius_hcconn.waiting_for_lsdata){var n={lsdata:gemius_hcconn.lsdata,fpdata:gemius_hcconn.getrawfpdata()};gemius_hcconn.params_ready_called=1;try{"undefined"!=typeof gemius_params_ready?gemius_params_ready(n):"undefined"!=typeof pp_gemius_params_ready&&pp_gemius_params_ready(n)}catch(e){}}}},visibilitychanged:function(){"prerender"!=document[gemius_hcconn.visapi_s]&&gemius_hcconn.waiting_on_prerender&&(gemius_hcconn.waiting_on_prerender=0,setTimeout(gemius_hcconn.latehits,100))},unloadhit:function(e,n){var i=(gemius_hcconn.hssl?"https://":"http://")+gemius_hcconn.hc+"/_",c=(new Date).getTime(),t="&vis="+(""==gemius_hcconn.visapi_h?3:document[gemius_hcconn.visapi_h]?2:1);if(t+="&fpdata="+(0==gemius_hcconn.waiting_for_fpdata&&gemius_hcconn.has_consent?gemius_hcconn.getrawfpdata():"-UNLOAD"),t+="&lsdata="+(0==gemius_hcconn.waiting_for_lsdata&&gemius_hcconn.has_consent?gemius_hcconn.lsdata+"&ltime="+gemius_hcconn.ltime:"-UNLOAD"),!0!==gemius_hcconn.has_consent?t+="&nc=1":!0===gemius_hcconn.explicit_consent&&(t+="&nc=0"),gemius_hcconn.closing)if(i+=c+n+"/redot.gif?l="+e.vers+t+e.req,"function"==typeof navigator.sendBeacon)navigator.sendBeacon(i);else{var o=gemius_hcconn.images.length;gemius_hcconn.images[o]=new Image,gemius_hcconn.images[o].src=i}else i+=c+n+"/redot.js?l="+e.vers+e.req+t,gemius_hcconn.append_script(i,null,1)},unload:function(e){try{var n,i=0,c=!gemius_hcconn.closing&&e;if(gemius_hcconn.closing=gemius_hcconn.closing>0||e?1:0,0==gemius_hcconn.waiting_on_prerender&&(0==gemius_hcconn.require_consent_info||0==gemius_hcconn.waiting_for_consent)){for(i=gemius_hcconn.requests.length,n=0;n<gemius_hcconn.requests.length;n++)gemius_hcconn.unloadhit(gemius_hcconn.requests[n],n+10);gemius_hcconn.requests=[]}if(c&&"function"!=typeof navigator.sendBeacon&&i>0)for(var t=(new Date).getTime();t+200>(new Date).getTime(););}catch(e){}},mousedown:function(){1==gemius_hcconn.cmp_found&&0!=gemius_hcconn.waiting_for_consent||gemius_hcconn.unload(!1)},getcookie:function(e){var n="-TURNEDOFF";try{for(var i,c=document.cookie.split(";"),t=0;t<c.length;t++)if((i=c[t].split("="))[0].replace(/^\s+|\s+$/g,"")==e){n=i[1].replace(/^\s+|\s+$/g,"");break}}catch(e){}return n},getrawfpdata:function(){return gemius_hcconn.fpdata.split("|")[0]},getfpcookie:function(){gemius_hcconn.fpdata=gemius_hcconn.getcookie("__gfp_64b")},getdntcookie:function(){0==gemius_hcconn.dnt&&(gemius_hcconn.dnt=parseInt(gemius_hcconn.getcookie("__gfp_dnt"))?1:0)},setfpcookie:function(){var e=(new Date).getTime()+34128e6;if(""!=gemius_hcconn.fpdata)try{document.cookie="__gfp_64b="+gemius_hcconn.fpdata+"; path=/"+(gemius_hcconn.fpcdomain?"; domain="+gemius_hcconn.fpcdomain:"")+"; expires="+new Date(e).toGMTString()}catch(e){}},fpdata_loaded:function(){null!=gemius_hcconn.sto&&(clearTimeout(gemius_hcconn.sto),gemius_hcconn.sto=null),gemius_hcconn.setfpcookie(),gemius_hcconn.getfpcookie(),gemius_hcconn.waiting_for_fpdata=0,gemius_hcconn.paramsready(),gemius_hcconn.latehits()},addframe:function(e,n,i,c){if(document.body){gemius_hcconn.current_receiver=c;var t="http"+(e?"s":"")+"://ls.hit.gemius.pl/ls"+n+".html"+i;null!=c&&(gemius_hcconn.loadinit=(new Date).getTime(),null==gemius_hcconn.fto&&(gemius_hcconn.fto=setTimeout(gemius_hcconn.frameto,1e4)));var o="gemius_hcconn_"+(new Date).getTime()+"_"+Math.floor(1e8*Math.random()),s=document.createElement("iframe");s.setAttribute("id",o),s.setAttribute("name","ls"+n+"frame"),s.setAttribute("width",0),s.setAttribute("height",0),s.setAttribute("scrolling","no"),s.setAttribute("sandbox","allow-scripts allow-same-origin"),s.style.display="none",s.style.visibility="hidden",document.body.appendChild(s),s.setAttribute("src",t),"get"==n&&0==e&&(gemius_hcconn.lsgetframe=s)}else setTimeout((function(){gemius_hcconn.addframe(e,n,i,c)}),100)},frameto:function(){null!=gemius_hcconn.fto&&(gemius_hcconn.fto=null,""==gemius_hcconn.lsdata&&(gemius_hcconn.ltime=1e4,gemius_hcconn.lsdata="-TIMEDOUT",gemius_hcconn.waiting_for_lsdata=0,gemius_hcconn.paramsready(),gemius_hcconn.latehits()))},scriptto:function(){null!=gemius_hcconn.sto&&(gemius_hcconn.sto=null,""!=gemius_hcconn.fpdata&&"-"!=gemius_hcconn.fpdata[0]&&(gemius_hcconn.setfpcookie(),gemius_hcconn.getfpcookie()),""==gemius_hcconn.fpdata&&(gemius_hcconn.fpdata="-TIMEDOUT"),gemius_hcconn.waiting_for_fpdata=0,gemius_hcconn.paramsready(),gemius_hcconn.latehits())},last_datareceiver:function(e){gemius_hcconn.current_receiver=null,gemius_hcconn.lsdata=e,gemius_hcconn.waiting_for_lsdata=0,gemius_hcconn.paramsready(),gemius_hcconn.latehits()},second_datareceiver:function(e){"-"==e.charAt(0)||""==e?gemius_hcconn.addframe(1,"set","",gemius_hcconn.last_datareceiver):gemius_hcconn.last_datareceiver(e)},first_datareceiver:function(e){var n=e.match(/^([A-Z0-9a-z\.\_\/]*).*\|([0-9]+)$/),i=(new Date).getTime();"-"==e.charAt(0)||""==e||!n||n[2]<i?gemius_hcconn.addframe(1,"get","",gemius_hcconn.second_datareceiver):(n&&(e=n[1]),gemius_hcconn.last_datareceiver(e))},msgreceiver:function(e){if("string"==typeof e.data&&"_xx_gemius_xx_/"==e.data.substr(0,15)&&(null!=gemius_hcconn.fto&&(clearTimeout(gemius_hcconn.fto),gemius_hcconn.fto=null,gemius_hcconn.ltime=(new Date).getTime()-gemius_hcconn.loadinit),null!=gemius_hcconn.current_receiver&&gemius_hcconn.current_receiver(e.data.substr(15))),"string"==typeof e.data&&"_xx_gemius_add_xx_/"==e.data.substr(0,19)){null!=gemius_hcconn.addto&&(clearTimeout(gemius_hcconn.addto),gemius_hcconn.addto=null);var n=e.data.substr(19);gemius_hcconn.sendhits("-GETERR"==n?null:n)}if(window.top===window.self&&"string"==typeof e.data&&"_xx_gemius_getfpdata_xx_"==e.data.substring(0,24)&&e.origin&&/(http|https)*(:)*\/\/.+\.hit\.gemius\.pl.*/.test(e.origin)){var i=new String(document.location.href);gemius_hcconn.add_fpdata_callback((function(n){gemius_hcconn.has_consent&&e.source.postMessage("_xx_gemius_putfpdata_xx_/"+n+"/"+encodeURIComponent(i),e.origin)}))}},getflashv:function(){var e="-";if("undefined"!=typeof Error){var n;try{e=navigator.plugins["Shockwave Flash"].description}catch(e){}if("undefined"!=typeof ActiveXObject){try{n=new ActiveXObject("ShockwaveFlash.ShockwaveFlash.7")}catch(i){try{n=new ActiveXObject("ShockwaveFlash.ShockwaveFlash.6"),e="X",n.AllowScriptAccess="always"}catch(n){"X"==e&&(e="WIN 6,0,20,0")}try{n=new ActiveXObject("ShockwaveFlash.ShockwaveFlash")}catch(e){}}"-"!=e&&"X"!=e||!n||(e=n.GetVariable("$version"))}}return e},gdpr_params:function(e){var n="";return null!=gemius_hcconn.gdpr_applies&&(n+="&gdpr="+(gemius_hcconn.gdpr_applies?"1":"0")),null!=gemius_hcconn.gdpr_consent&&(n+="&gdpr_consent="+("string"==typeof gemius_hcconn.gdpr_consent?gemius_hcconn.gdpr_consent:"")),e&&""!=n&&(n="?"+n.substring(1)),n},cmp_purposes:function(){var e={1:[1,5],2:[1,7,8,9,10]};try{!function(e,n,i){var c={1:[1],2:[3,5],3:[2,4,7],4:[6,8],5:[7,8,9]},t={1:[1,2,3,5],2:[1,2,3,4,5,7,8,9,10]};if(void 0!==n&&null!=n)if(n.constructor===Array){e[1]=n,e[2]=[10];for(var o=0;o<e[1].length;o++)v2_purposes=c[e[1][o]],"undefined"!=typeof v2_purposes&&(e[2]=e[2].concat(v2_purposes))}else for(version in n)e[version]=n[version];if(i)for(version in t)e[version]=e[version].concat(t[version])}(e,gemius_hcconn.cmp_purposes_overrides,gemius_hcconn.dmp_purpose)}catch(e){}return e},parameters:function(){var e,n,i=document,c=window,t=new String(i.location.href),o=0;if(e=i.referrer?new String(i.referrer):"","undefined"!=typeof Error)try{o=i==top.document?1:2,"string"==typeof top.document.referrer&&(e=top.document.referrer)}catch(e){o=3}try{""==e&&"undefined"!=typeof ia_document&&ia_document.referrer&&(e="https://"+new String(ia_document.referrer))}catch(e){}var s="&fr="+o+"&tz="+(new Date).getTimezoneOffset();if("undefined"!=typeof encodeURIComponent&&(s+="&fv="+encodeURIComponent(gemius_hcconn.flashv)+"&href="+encodeURIComponent(t.substring(0,499))+"&ref="+encodeURIComponent(e.substring(0,499))),screen){var _=screen;_.width&&(_.deviceXDPI&&_.deviceYDPI?s+="&screen="+Math.floor(_.width*_.deviceXDPI/96)+"x"+Math.floor(_.height*_.deviceYDPI/96):s+="&screen="+_.width+"x"+_.height),c.devicePixelRatio&&(s+="r"+Math.round(1e3*c.devicePixelRatio)),_.colorDepth&&(s+="&col="+_.colorDepth)}return"number"==typeof c.innerWidth?s+="&window="+c.innerWidth+"x"+c.innerHeight:((n=i.documentElement)&&(n.clientWidth||n.clientHeight)||(n=i.body)&&(n.clientWidth||n.clientHeight))&&(s+="&window="+n.clientWidth+"x"+n.clientHeight),gemius_hcconn.cmp_found&&(s+="&cmpf=1"),gemius_hcconn.gdpr_found&&(s+="&gdprf=1"),s},array_to_string:function(e,n){var i,c;if("string"==typeof e)return e;if(c="",void 0!==e.length)for(i=n;i<e.length;i++)i>n&&(c+="|"),c+=new String(e[i]).replace(/\|/g,"_");return c},internal_hit:function(e,n,i,c,t,o,s,_){var a="";null==gemius_hcconn.event_identifier&&i&&(gemius_hcconn.event_identifier=i),a+="&id="+i,void 0!==t&&(a+="&et="+t),void 0!==o&&(a+="&hsrc="+o),s&&"view"==t&&i&&"function"==typeof i.indexOf&&i.indexOf("&sargencoding=")<0&&(gemius_hcconn.sonar_auto_init=0,a+="&initsonar=1"),void 0!==_&&"undefined"!=typeof encodeURIComponent&&(a+="&extra="+encodeURIComponent(_.substring(0,1999))),a+="&eventid="+c+gemius_hcconn.parameters(),gemius_hcconn.requests[gemius_hcconn.requests.length]={req:a,allowaddscript:e,vers:n},gemius_hcconn.latehits()},timer:function(){var e;for(e=0;e<gemius_hcconn.timerevents.length;e++)gemius_hcconn.internal_hit(0,103,gemius_hcconn.timerevents[e],0,"sonar")},gtimer_add:function(e){gemius_hcconn.internal_hit(0,103,e,0,"sonar"),gemius_hcconn.timerevents[gemius_hcconn.timerevents.length]=e},sonar_add:function(e,n,i,c){if(null==gemius_hcconn.sonar_data){var t={};t.id=e,t.evid=n,t.freq=i,t.extra=c,t.to=null,t.linterval=(new Date).getTime(),t.sdur=0,e&&n&&i>0&&(t.to=setInterval(gemius_hcconn.sonar,1e3)),gemius_hcconn.sonar_data=t}},sonar:function(){var e,n,i;if(null!=gemius_hcconn.sonar_data)for(i=gemius_hcconn.visapi_s?document[gemius_hcconn.visapi_s]:"",e=gemius_hcconn.sonar_data,n=((new Date).getTime()-e.linterval)/1e3,e.linterval=(new Date).getTime();n>0;)e.sdur<86400&&n<=4&&"visible"==i&&Math.random()<n/e.freq&&gemius_hcconn.internal_hit(0,109,e.id,e.evid,"smpsonar",0,0,"_ASF="+e.freq+(e.extra?"|"+e.extra:"")),e.sdur+=Math.min(n,e.freq),n-=e.freq},gdprdata_loaded:function(){try{if(gemius_hcconn.gdprdisabled)return void gemius_hcconn.consent_loaded(!0);var e=gemius_hcconn.cmp_purposes()[gemius_hcconn.gdprversion];if(void 0===e)return void gemius_hcconn.consent_loaded(!1);for(var n=0;n<e.length;++n)if(!gemius_hcconn.gdprdata[e[n]-1])return void gemius_hcconn.consent_loaded(!1)}catch(e){return void gemius_hcconn.consent_loaded(!1)}gemius_hcconn.consent_loaded(!0)},consent_loaded:function(e){1==gemius_hcconn.waiting_for_consent&&(null!=gemius_hcconn.cmpto&&(clearTimeout(gemius_hcconn.cmpto),gemius_hcconn.cmpto=null),gemius_hcconn.waiting_for_consent=0,gemius_hcconn.has_consent=!!e,gemius_hcconn.has_consent?(gemius_hcconn.waiting_for_fpdata&&gemius_hcconn.load_fpdata(),gemius_hcconn.waiting_for_lsdata&&gemius_hcconn.load_lsdata(),gemius_hcconn.load_gsconf()):(gemius_hcconn.fpdata="-NOCONSENT",gemius_hcconn.lsdata="-NOCONSENT",gemius_hcconn.waiting_for_fpdata=0,gemius_hcconn.waiting_for_lsdata=0,gemius_hcconn.paramsready()),gemius_hcconn.latehits())},consentto:function(){1==gemius_hcconn.waiting_for_consent&&(gemius_hcconn.cmpto=null,gemius_hcconn.waiting_for_consent=0,gemius_hcconn.has_consent=!1,gemius_hcconn.fpdata="-CMPTIMEDOUT",gemius_hcconn.lsdata="-CMPTIMEDOUT",gemius_hcconn.waiting_for_fpdata=0,gemius_hcconn.waiting_for_lsdata=0,gemius_hcconn.paramsready(),gemius_hcconn.latehits())},ghit:function(e,n,i,c,t,o){i.length>0&&gemius_hcconn.internal_hit(e,n,i[0],c,"view",t,o,gemius_hcconn.array_to_string(i,1))},gevent:function(e,n,i,c,t,o){var s=0,_="view";if(i.length>1){var a=new String(i[0]).match("^_([a-zA-Z0-9]+)_$");a&&(_=a[1],s=1)}i.length>s&&(i[s]||null==gemius_hcconn.event_identifier||(i[s]=gemius_hcconn.event_identifier),i[s]&&gemius_hcconn.internal_hit(e,n,i[s],c,_,t,o,gemius_hcconn.array_to_string(i,s+1)))},addscripthit:function(){gemius_hcconn.ghit(1,106,arguments,0,2,gemius_hcconn.sonar_auto_init)},plainhit:function(){gemius_hcconn.ghit(0,107,arguments,0,2,gemius_hcconn.sonar_auto_init)},addscriptevent:function(){gemius_hcconn.gevent(1,106,arguments,0,3,gemius_hcconn.sonar_auto_init)},plainevent:function(){gemius_hcconn.gevent(0,107,arguments,0,3,gemius_hcconn.sonar_auto_init)},pendingdata:function(e,n){var i;if(void 0!==window[e]){for(i=0;i<window[e].length;i++)n.apply(this,window[e][i]);window[e]=[]}},sendpendingdata:function(){gemius_hcconn.pendingdata("pp_gemius_hit_pdata",gemius_hcconn.addscripthit),gemius_hcconn.pendingdata("gemius_hit_pdata",gemius_hcconn.plainhit),gemius_hcconn.pendingdata("pp_gemius_event_pdata",gemius_hcconn.addscriptevent),gemius_hcconn.pendingdata("gemius_event_pdata",gemius_hcconn.plainevent),gemius_hcconn.pendingdata("gemius_shits",gemius_hcconn.addscripthit),gemius_hcconn.pendingdata("gemius_phits",gemius_hcconn.plainhit),gemius_hcconn.pendingdata("gemius_sevents",gemius_hcconn.addscriptevent),gemius_hcconn.pendingdata("gemius_pevents",gemius_hcconn.plainevent)},findvisapi:function(){var e,n=["moz","webkit","ms","o"];if(void 0!==document.hidden)gemius_hcconn.visapi_h="hidden",gemius_hcconn.visapi_s="visibilityState",gemius_hcconn.visapi_c="visibilitychange";else for(e in n)void 0!==document[n[e]+"Hidden"]&&(gemius_hcconn.visapi_h=n[e]+"Hidden",gemius_hcconn.visapi_s=n[e]+"VisibilityState",gemius_hcconn.visapi_c=n[e]+"visibilitychange")},load_fpdata:function(){if(0==gemius_hcconn.waiting_for_consent){var e=new String(document.location.hostname);if("hit.gemius.pl"==e||".hit.gemius.pl"==e.substr(-"hit.gemius.pl".length-1))gemius_hcconn.fpdata="",gemius_hcconn.fpcdomain="",gemius_hcconn.fpdata_loaded();else{var n=(gemius_hcconn.hssl?"https://":"http://")+gemius_hcconn.hc+"/fpdata.js?href="+e;gemius_hcconn.sto=setTimeout(gemius_hcconn.scriptto,1e4),gemius_hcconn.append_script(n,gemius_hcconn.fpdata_loaded,0)}}},load_lsdata:function(){0==gemius_hcconn.waiting_for_consent&&(gemius_hcconn.ssl?gemius_hcconn.addframe(1,"get","",gemius_hcconn.second_datareceiver):gemius_hcconn.addframe(0,"get","",gemius_hcconn.first_datareceiver))},getchromever:function(){if(window.chrome&&"string"==typeof navigator.userAgent){var e=navigator.userAgent.match(/(Chrom(e|ium)|CriOS)\/([0-9]+)\./);return null==e?-1:parseInt(e[3])}return-1},getanticache:function(){var e=new Date,n=new Date(e.getFullYear(),e.getMonth(),e.getDate(),4).getTime()/36e5;return(0!=e.getDay()||e.getHours()>=4)&&(n+=24*(7-e.getDay())),n},gsconf_loaded:function(){if("object"==("undefined"==typeof gemius_gsconf?"undefined":e(gemius_gsconf))&&null!=gemius_gsconf&&gemius_gsconf.publishers&&"string"==typeof gemius_hcconn.src){var n=new URL(gemius_hcconn.src);n=n.origin+n.pathname.substr(0,n.pathname.lastIndexOf("/")),n+="/mgemius.js?gsver="+gemius_hcconn.version+"&v="+gemius_hcconn.getanticache(),gemius_hcconn.append_script(n,null,0)}},load_gsconf:function(){if(gemius_hcconn.use_gsync&&0==gemius_hcconn.gsconf_added){gemius_hcconn.gsconf_added=1;var e=new String(document.location.hostname),n=(gemius_hcconn.hssl?"https://":"http://")+gemius_hcconn.hc+"/gsconf.js?gst=parent&href="+e+"&gsver="+gemius_hcconn.version+"&v="+gemius_hcconn.getanticache();gemius_hcconn.append_script(n,gemius_hcconn.gsconf_loaded,0)}},init:function(){setInterval(gemius_hcconn.timer,6e4),gemius_hcconn.add_event(window,"message",gemius_hcconn.msgreceiver),gemius_hcconn.getdntcookie(),gemius_hcconn.hssl=gemius_hcconn.ssl||gemius_hcconn.getchromever()>=67?1:0,gemius_hcconn.flashv=gemius_hcconn.getflashv(),0==gemius_hcconn.dnt&&!1!==gemius_hcconn.explicit_consent?(gemius_hcconn.getfpcookie(),gemius_hcconn.waiting_for_fpdata=gemius_hcconn.fpdata.length>0&&"-"==gemius_hcconn.fpdata[0]||""==gemius_hcconn.fpdata?1:0):(gemius_hcconn.waiting_for_fpdata=0,gemius_hcconn.fpdata="-DNT");try{0==gemius_hcconn.dnt&&!1!==gemius_hcconn.explicit_consent?(gemius_hcconn.waiting_for_lsdata=void 0!==window.postMessage&&"undefined"!=typeof localStorage&&null!=localStorage?1:0,0==gemius_hcconn.waiting_for_lsdata&&(gemius_hcconn.lsdata="-NOTSUP")):(gemius_hcconn.waiting_for_lsdata=0,gemius_hcconn.lsdata="-DNT")}catch(e){gemius_hcconn.waiting_for_lsdata=0,gemius_hcconn.lsdata="-TURNEDOFF"}if(0==gemius_hcconn.dnt&&!1!==gemius_hcconn.explicit_consent)if(null===gemius_hcconn.explicit_consent&&gemius_hcconn.use_cmp&&gemius_cmpclient.find_cmp())gemius_hcconn.cmp_found=1,gemius_hcconn.cmp_timeout==1/0?gemius_hcconn.require_consent_info=1:gemius_hcconn.cmpto=setTimeout(gemius_hcconn.consentto,gemius_hcconn.cmp_timeout),gemius_cmpclient.get_consent(gemius_hcconn.consent_loaded,gemius_hcconn.cmp_purposes());else if(null===gemius_hcconn.explicit_consent&&""!=gemius_hcconn.gdpr_params()){gemius_hcconn.gdpr_found=1,gemius_hcconn.cmpto=setTimeout(gemius_hcconn.consentto,1e4);var e=(gemius_hcconn.hssl?"https://":"http://")+gemius_hcconn.hc+"/gdprdata.js"+gemius_hcconn.gdpr_params(!0);gemius_hcconn.append_script(e,gemius_hcconn.gdprdata_loaded,0)}else gemius_hcconn.waiting_for_consent=0,gemius_hcconn.has_consent=!0,gemius_hcconn.waiting_for_fpdata&&gemius_hcconn.load_fpdata(),gemius_hcconn.waiting_for_lsdata&&gemius_hcconn.load_lsdata(),gemius_hcconn.load_gsconf();else gemius_hcconn.waiting_for_consent=0,gemius_hcconn.has_consent=!1,gemius_hcconn.waiting_for_fpdata=0,gemius_hcconn.fpdata="-DNT";gemius_hcconn.waiting_on_prerender=0,gemius_hcconn.paramsready(),gemius_hcconn.findvisapi(),""!=gemius_hcconn.visapi_s&&("prerender"==document[gemius_hcconn.visapi_s]&&(gemius_hcconn.waiting_on_prerender=1),gemius_hcconn.add_event(document,gemius_hcconn.visapi_c,gemius_hcconn.visibilitychanged)),gemius_hcconn.latehits(),gemius_hcconn.add_event(window,"unload",(function(){gemius_hcconn.unload(!0)})),gemius_hcconn.add_event(window,"beforeunload",(function(){gemius_hcconn.unload(!0)})),gemius_hcconn.add_event(document,"mousedown",(function(){gemius_hcconn.mousedown()}))}},gemius_hcconn.init(),gemius_hit=gemius_hcconn.plainhit,gemius_event=gemius_hcconn.plainevent,pp_gemius_hit=gemius_hcconn.addscripthit,pp_gemius_event=gemius_hcconn.addscriptevent,"undefined"==typeof gemius_identifier&&"undefined"==typeof pp_gemius_identifier&&(gemius_hcconn.sonar_auto_init="boolean"==typeof gemius_sonar_auto_init_disabled?gemius_sonar_auto_init_disabled?0:1:"boolean"==typeof pp_gemius_sonar_auto_init_disabled&&pp_gemius_sonar_auto_init_disabled?0:1);try{"undefined"!=typeof gemius_loaded?gemius_loaded():"undefined"!=typeof pp_gemius_loaded&&pp_gemius_loaded()}catch(e){}"undefined"!=typeof gemius_identifier?gemius_hcconn.event_identifier=gemius_identifier:"undefined"!=typeof pp_gemius_identifier&&(gemius_hcconn.event_identifier=pp_gemius_identifier),gemius_hcconn.sendpendingdata()}!function(){if("undefined"==typeof pp_gemius_identifier||pp_gemius_identifier.match(/^USED_/))"undefined"==typeof gemius_identifier||gemius_identifier.match(/^USED_/)||(n=101-(e="undefined"!=typeof pp_gemius_mode?0:1),void 0!==window.pp_gemius_cnt&&(gemius_identifier="ERR_"+gemius_identifier.replace(/id=/g,"id=ERR_"),n=102),window.pp_gemius_cnt=1,"undefined"!=typeof gemius_extraparameters?gemius_hcconn.gevent(e,n,[gemius_identifier].concat(gemius_extraparameters),0,1,1):gemius_hcconn.ghit(e,n,[gemius_identifier],0,1,1),null==gemius_hcconn.event_identifier&&(gemius_hcconn.event_identifier=gemius_identifier),gemius_identifier="USED_"+gemius_identifier.replace(/id=/g,"id=USED_"));else{var e,n=101-(e="undefined"!=typeof pp_gemius_mode?0:1);void 0!==window.pp_gemius_cnt&&(pp_gemius_identifier="ERR_"+pp_gemius_identifier.replace(/id=/g,"id=ERR_"),n=102),window.pp_gemius_cnt=1,"undefined"!=typeof pp_gemius_extraparameters?gemius_hcconn.gevent(e,n,[pp_gemius_identifier].concat(pp_gemius_extraparameters),0,1,1):gemius_hcconn.ghit(e,n,[pp_gemius_identifier],0,1,1),null==gemius_hcconn.event_identifier&&(gemius_hcconn.event_identifier=pp_gemius_identifier),102!=n&&"undefined"!=typeof pp_gemius_time_identifier&&gemius_hcconn.gtimer_add(pp_gemius_time_identifier),pp_gemius_identifier="USED_"+pp_gemius_identifier.replace(/id=/g,"id=USED_")}gemius_hcconn.sendpendingdata()}();