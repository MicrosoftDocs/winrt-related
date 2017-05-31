---
author: msatranjr
description: This topic lists the Win32 and COM APIs that are part of the Universal Windows Platform (UWP) and that are implemented by some Windows 10 devices.
title: Extension APIs for Windows 10 devices (grouped by module)
ms.author: misatran
ms.topic: article
ms.prod: windows
ms.technology: uwp
keywords: windows 10, uwp, win32, COM
ms.date: 04/05/2017
ms.assetid: e8d54f37-9969-4f33-8b1b-fcb3d659c507
---

# Extension APIs for Windows 10 devices
This topic lists the Win32 and COM APIs that are part of the Universal Windows Platform (UWP) and that are implemented by some Windows 10 devices, so your calls to these APIs must be guarded with conditions that first confirm the presence of the API on the device your app is running on. The union of [APIs present on all Windows 10 devices](win32-apis.md) and the APIs listed in this topic make up the entire Win32 and COM surface area of UWP.

This topic lists the APIs grouped by module (where the module is either an [API set](https://msdn.microsoft.com/en-us/library/windows/apps/mt683763.aspx#api_sets) or a dll). For delay load, use the module name.

## <span id="_ext-ms-win-ole32-bindctx-l1-1-0"></span><span id="_EXT-MS-WIN-OLE32-BINDCTX-L1-1-0"></span>APIs from the API Set ext-ms-win-ole32-bindctx-l1-1-0


| API                                    | Requirements                                                                                                                         |
|----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| [**CoGetObject**](https://msdn.microsoft.com/en-us/library/windows/apps/ms678805.aspx)     | Introduced into ext-ms-win-ole32-bindctx-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**CreateBindCtx**](https://msdn.microsoft.com/en-us/library/windows/apps/ms678542.aspx) | Introduced into ext-ms-win-ole32-bindctx-l1-1-0 in Windows 10.0.10240.0. Moved to api-ms-win-ole32-ie-l1-1-0 in Windows 10.0.14393.0 |

 

## <span id="_ext-ms-win-ole32-ie-ext-l1-1-0"></span><span id="_EXT-MS-WIN-OLE32-IE-EXT-L1-1-0"></span>APIs from the API Set ext-ms-win-ole32-ie-ext-l1-1-0


| API                                                      | Requirements                                                           |
|----------------------------------------------------------|------------------------------------------------------------------------|
| [**CreateGenericComposite**](https://msdn.microsoft.com/en-us/library/windows/apps/ms687265.aspx) | Introduced into ext-ms-win-ole32-ie-ext-l1-1-0 in Windows 10.0.10240.0 |
| [**GetClassFile**](https://msdn.microsoft.com/en-us/library/windows/apps/ms693715.aspx)                     | Introduced into ext-ms-win-ole32-ie-ext-l1-1-0 in Windows 10.0.10240.0 |
| [**MonikerRelativePathTo**](https://msdn.microsoft.com/en-us/library/windows/apps/ms682532.aspx)   | Introduced into ext-ms-win-ole32-ie-ext-l1-1-0 in Windows 10.0.10240.0 |
| [**MkParseDisplayName**](https://msdn.microsoft.com/en-us/library/windows/apps/ms691253.aspx)         | Introduced into ext-ms-win-ole32-ie-ext-l1-1-0 in Windows 10.0.14393.0 |

 

## <span id="_ext-ms-win-com-ole32-l1-1-0"></span><span id="_EXT-MS-WIN-COM-OLE32-L1-1-0"></span>APIs from the API Set ext-ms-win-com-ole32-l1-1-0


| API                                                  | Requirements                                                        |
|------------------------------------------------------|---------------------------------------------------------------------|
| [**CreateItemMoniker**](https://msdn.microsoft.com/en-us/library/windows/apps/ms680140.aspx)       | Introduced into ext-ms-win-com-ole32-l1-1-0 in Windows 10.0.10240.0 |
| [**CreatePointerMoniker**](https://msdn.microsoft.com/en-us/library/windows/apps/ms693427.aspx) | Introduced into ext-ms-win-com-ole32-l1-1-0 in Windows 10.0.10240.0 |

 

## <span id="_ext-ms-win-els-elscore-l1-1-0"></span><span id="_EXT-MS-WIN-ELS-ELSCORE-L1-1-0"></span>APIs from the API Set ext-ms-win-els-elscore-l1-1-0


| API                                                       | Requirements                                                          |
|-----------------------------------------------------------|-----------------------------------------------------------------------|
| [**MappingFreePropertyBag**](https://msdn.microsoft.com/en-us/library/windows/apps/dd319058.aspx) | Introduced into ext-ms-win-els-elscore-l1-1-0 in Windows 10.0.10240.0 |
| [**MappingFreeServices**](https://msdn.microsoft.com/en-us/library/windows/apps/dd319059.aspx)       | Introduced into ext-ms-win-els-elscore-l1-1-0 in Windows 10.0.10240.0 |
| [**MappingGetServices**](https://msdn.microsoft.com/en-us/library/windows/apps/dd319060.aspx)         | Introduced into ext-ms-win-els-elscore-l1-1-0 in Windows 10.0.10240.0 |
| [**MappingRecognizeText**](https://msdn.microsoft.com/en-us/library/windows/apps/dd319063.aspx)     | Introduced into ext-ms-win-els-elscore-l1-1-0 in Windows 10.0.10240.0 |

 

## <span id="_ext-ms-win-com-ole32-l1-1-1"></span><span id="_EXT-MS-WIN-COM-OLE32-L1-1-1"></span>APIs from the API Set ext-ms-win-com-ole32-l1-1-1


| API                                              | Requirements                                                        |
|--------------------------------------------------|---------------------------------------------------------------------|
| [**MkParseDisplayName**](https://msdn.microsoft.com/en-us/library/windows/apps/ms691253.aspx) | Introduced into ext-ms-win-com-ole32-l1-1-1 in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-core-slapi-l1-1-0"></span><span id="_API-MS-WIN-CORE-SLAPI-L1-1-0"></span>APIs from the API Set api-ms-win-core-slapi-l1-1-0


| API                                                                   | Requirements                                                         |
|-----------------------------------------------------------------------|----------------------------------------------------------------------|
| [**SLQueryLicenseValueFromApp**](https://msdn.microsoft.com/en-us/library/windows/apps/mt403327.aspx) | Introduced into api-ms-win-core-slapi-l1-1-0 in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-crt-convert-l1-1-0"></span><span id="_API-MS-WIN-CRT-CONVERT-L1-1-0"></span>APIs from the API Set api-ms-win-crt-convert-l1-1-0


| API                                                                 | Requirements                                                                                                                       |
|---------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| [**\_\_toascii**](https://www.bing.com/search?q=__toascii)          | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_atodbl**](https://www.bing.com/search?q=_atodbl)               | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_atodbl\_l**](https://www.bing.com/search?q=_atodbl_l)          | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_atof\_l**](https://www.bing.com/search?q=_atof_l)              | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_atoflt**](https://www.bing.com/search?q=_atoflt)               | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_atoflt\_l**](https://www.bing.com/search?q=_atoflt_l)          | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_atoi\_l**](https://www.bing.com/search?q=_atoi_l)              | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_atoi64**](https://www.bing.com/search?q=_atoi64)               | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0. Moved to api-ms-win-core-crt-l1-1-0 in Windows 10.0.10586.0 |
| [**\_atoi64\_l**](https://www.bing.com/search?q=_atoi64_l)          | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_atol\_l**](https://www.bing.com/search?q=_atol_l)              | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_atoldbl**](https://www.bing.com/search?q=_atoldbl)             | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_atoldbl\_l**](https://www.bing.com/search?q=_atoldbl_l)        | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_atoll\_l**](https://www.bing.com/search?q=_atoll_l)            | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_ecvt**](https://www.bing.com/search?q=_ecvt)                   | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_ecvt\_s**](https://www.bing.com/search?q=_ecvt_s)              | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_fcvt**](https://www.bing.com/search?q=_fcvt)                   | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_fcvt\_s**](https://www.bing.com/search?q=_fcvt_s)              | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_gcvt**](https://www.bing.com/search?q=_gcvt)                   | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_gcvt\_s**](https://www.bing.com/search?q=_gcvt_s)              | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_i64toa**](https://www.bing.com/search?q=_i64toa)               | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_i64toa\_s**](https://www.bing.com/search?q=_i64toa_s)          | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_i64tow**](https://www.bing.com/search?q=_i64tow)               | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_itoa**](https://www.bing.com/search?q=_itoa)                   | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_itoa\_s**](https://www.bing.com/search?q=_itoa_s)              | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_itow**](https://www.bing.com/search?q=_itow)                   | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_ltoa**](https://www.bing.com/search?q=_ltoa)                   | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_ltoa\_s**](https://www.bing.com/search?q=_ltoa_s)              | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_ltow**](https://www.bing.com/search?q=_ltow)                   | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_strtod\_l**](https://www.bing.com/search?q=_strtod_l)          | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_strtof\_l**](https://www.bing.com/search?q=_strtof_l)          | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_strtoi64**](https://www.bing.com/search?q=_strtoi64)           | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_strtoi64\_l**](https://www.bing.com/search?q=_strtoi64_l)      | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_strtoimax\_l**](https://www.bing.com/search?q=_strtoimax_l)    | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_strtol\_l**](https://www.bing.com/search?q=_strtol_l)          | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_strtold\_l**](https://www.bing.com/search?q=_strtold_l)        | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_strtoll\_l**](https://www.bing.com/search?q=_strtoll_l)        | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_strtoui64**](https://www.bing.com/search?q=_strtoui64)         | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_strtoui64\_l**](https://www.bing.com/search?q=_strtoui64_l)    | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_strtoul\_l**](https://www.bing.com/search?q=_strtoul_l)        | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_strtoull\_l**](https://www.bing.com/search?q=_strtoull_l)      | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_strtoumax\_l**](https://www.bing.com/search?q=_strtoumax_l)    | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_ui64toa**](https://www.bing.com/search?q=_ui64toa)             | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_ui64toa\_s**](https://www.bing.com/search?q=_ui64toa_s)        | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_ui64tow**](https://www.bing.com/search?q=_ui64tow)             | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_ui64tow\_s**](https://www.bing.com/search?q=_ui64tow_s)        | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_ultoa**](https://www.bing.com/search?q=_ultoa)                 | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_ultoa\_s**](https://www.bing.com/search?q=_ultoa_s)            | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_ultow**](https://www.bing.com/search?q=_ultow)                 | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0. Moved to api-ms-win-core-crt-l1-1-0 in Windows 10.0.14393.0 |
| [**\_ultow\_s**](https://www.bing.com/search?q=_ultow_s)            | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0. Moved to api-ms-win-core-crt-l1-1-0 in Windows 10.0.10586.0 |
| [**\_wcstod\_l**](https://www.bing.com/search?q=_wcstod_l)          | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wcstof\_l**](https://www.bing.com/search?q=_wcstof_l)          | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wcstoi64**](https://www.bing.com/search?q=_wcstoi64)           | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0. Moved to api-ms-win-core-crt-l1-1-0 in Windows 10.0.10586.0 |
| [**\_wcstoi64\_l**](https://www.bing.com/search?q=_wcstoi64_l)      | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wcstoimax\_l**](https://www.bing.com/search?q=_wcstoimax_l)    | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wcstol\_l**](https://www.bing.com/search?q=_wcstol_l)          | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wcstold\_l**](https://www.bing.com/search?q=_wcstold_l)        | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wcstoll\_l**](https://www.bing.com/search?q=_wcstoll_l)        | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wcstombs\_l**](https://www.bing.com/search?q=_wcstombs_l)      | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wcstombs\_s\_l**](https://www.bing.com/search?q=_wcstombs_s_l) | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wcstoui64**](https://www.bing.com/search?q=_wcstoui64)         | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0. Moved to api-ms-win-core-crt-l1-1-0 in Windows 10.0.10586.0 |
| [**\_wcstoui64\_l**](https://www.bing.com/search?q=_wcstoui64_l)    | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wcstoul\_l**](https://www.bing.com/search?q=_wcstoul_l)        | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wcstoull\_l**](https://www.bing.com/search?q=_wcstoull_l)      | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wcstoumax\_l**](https://www.bing.com/search?q=_wcstoumax_l)    | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wctomb\_l**](https://www.bing.com/search?q=_wctomb_l)          | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wctomb\_s\_l**](https://www.bing.com/search?q=_wctomb_s_l)     | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wtof**](https://www.bing.com/search?q=_wtof)                   | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wtof\_l**](https://www.bing.com/search?q=_wtof_l)              | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wtoi\_l**](https://www.bing.com/search?q=_wtoi_l)              | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wtoi64\_l**](https://www.bing.com/search?q=_wtoi64_l)          | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wtol\_l**](https://www.bing.com/search?q=_wtol_l)              | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wtoll**](https://www.bing.com/search?q=_wtoll)                 | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wtoll\_l**](https://www.bing.com/search?q=_wtoll_l)            | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**atof**](https://www.bing.com/search?q=atof)                      | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**atoll**](https://www.bing.com/search?q=atoll)                    | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**btowc**](https://www.bing.com/search?q=btowc)                    | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**c16rtomb**](https://www.bing.com/search?q=c16rtomb)              | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**c32rtomb**](https://www.bing.com/search?q=c32rtomb)              | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**mbrtoc16**](https://www.bing.com/search?q=mbrtoc16)              | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**mbrtoc32**](https://www.bing.com/search?q=mbrtoc32)              | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**mbrtowc**](https://www.bing.com/search?q=mbrtowc)                | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**mbsrtowcs**](https://www.bing.com/search?q=mbsrtowcs)            | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**mbsrtowcs\_s**](https://www.bing.com/search?q=mbsrtowcs_s)       | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**mbstowcs**](https://www.bing.com/search?q=mbstowcs)              | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**mbstowcs\_s**](https://www.bing.com/search?q=mbstowcs_s)         | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**mbtowc**](https://www.bing.com/search?q=mbtowc)                  | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**strtod**](https://www.bing.com/search?q=strtod)                  | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**strtof**](https://www.bing.com/search?q=strtof)                  | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**strtoimax**](https://www.bing.com/search?q=strtoimax)            | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**strtold**](https://www.bing.com/search?q=strtold)                | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**strtoll**](https://www.bing.com/search?q=strtoll)                | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**strtoull**](https://www.bing.com/search?q=strtoull)              | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**strtoumax**](https://www.bing.com/search?q=strtoumax)            | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**wcrtomb**](https://www.bing.com/search?q=wcrtomb)                | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**wcrtomb\_s**](https://www.bing.com/search?q=wcrtomb_s)           | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**wcsrtombs**](https://www.bing.com/search?q=wcsrtombs)            | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**wcsrtombs\_s**](https://www.bing.com/search?q=wcsrtombs_s)       | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**wcstod**](https://www.bing.com/search?q=wcstod)                  | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**wcstof**](https://www.bing.com/search?q=wcstof)                  | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**wcstoimax**](https://www.bing.com/search?q=wcstoimax)            | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**wcstold**](https://www.bing.com/search?q=wcstold)                | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**wcstoll**](https://www.bing.com/search?q=wcstoll)                | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**wcstombs**](https://www.bing.com/search?q=wcstombs)              | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**wcstombs\_s**](https://www.bing.com/search?q=wcstombs_s)         | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**wcstoull**](https://www.bing.com/search?q=wcstoull)              | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**wcstoumax**](https://www.bing.com/search?q=wcstoumax)            | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**wctob**](https://www.bing.com/search?q=wctob)                    | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**wctomb**](https://www.bing.com/search?q=wctomb)                  | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**wctomb\_s**](https://www.bing.com/search?q=wctomb_s)             | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**wctrans**](https://www.bing.com/search?q=wctrans)                | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_i64tow\_s**](https://www.bing.com/search?q=_i64tow_s)          | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10586.0. Moved to api-ms-win-core-crt-l1-1-0 in Windows 10.0.14393.0 |
| [**\_itow\_s**](https://www.bing.com/search?q=_itow_s)              | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10586.0. Moved to api-ms-win-core-crt-l1-1-0 in Windows 10.0.14393.0 |
| [**\_wtoi**](https://www.bing.com/search?q=_wtoi)                   | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10586.0. Moved to api-ms-win-core-crt-l1-1-0 in Windows 10.0.14393.0 |
| [**\_wtoi64**](https://www.bing.com/search?q=_wtoi64)               | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10586.0                                                              |
| [**atol**](https://www.bing.com/search?q=atol)                      | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10586.0. Moved to api-ms-win-core-crt-l1-1-0 in Windows 10.0.14393.0 |
| [**strtol**](https://www.bing.com/search?q=strtol)                  | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10586.0                                                              |
| [**wcstoul**](https://www.bing.com/search?q=wcstoul)                | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10586.0                                                              |
| [**\_wtol**](https://www.bing.com/search?q=_wtol)                   | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.14393.0                                                              |
| [**strtoul**](https://www.bing.com/search?q=strtoul)                | Introduced into api-ms-win-crt-convert-l1-1-0 in Windows 10.0.14393.0                                                              |

 

## <span id="_api-ms-win-core-crt-l1-1-0"></span><span id="_API-MS-WIN-CORE-CRT-L1-1-0"></span>APIs from the API Set api-ms-win-core-crt-l1-1-0


| API                                                                | Requirements                                                                                                                          |
|--------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| [**\_i64tow\_s**](https://www.bing.com/search?q=_i64tow_s)         | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.10240.0. Moved to api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10586.0    |
| [**\_itow\_s**](https://www.bing.com/search?q=_itow_s)             | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.10240.0. Moved to api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10586.0    |
| [**\_ltow\_s**](https://www.bing.com/search?q=_ltow_s)             | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.10240.0                                                                    |
| [**\_wtoi**](https://www.bing.com/search?q=_wtoi)                  | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.10240.0. Moved to api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10586.0    |
| [**\_wtoi64**](https://www.bing.com/search?q=_wtoi64)              | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.10240.0. Moved to api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10586.0    |
| [**\_wtol**](https://www.bing.com/search?q=_wtol)                  | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.10240.0. Moved to api-ms-win-crt-convert-l1-1-0 in Windows 10.0.14393.0    |
| [**atoi**](https://www.bing.com/search?q=atoi)                     | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.10240.0                                                                    |
| [**atol**](https://www.bing.com/search?q=atol)                     | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.10240.0. Moved to api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10586.0    |
| [**strtol**](https://www.bing.com/search?q=strtol)                 | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.10240.0. Moved to api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10586.0    |
| [**strtoul**](https://www.bing.com/search?q=strtoul)               | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.10240.0. Moved to api-ms-win-crt-convert-l1-1-0 in Windows 10.0.14393.0    |
| [**wcstol**](https://www.bing.com/search?q=wcstol)                 | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.10240.0                                                                    |
| [**wcstoul**](https://www.bing.com/search?q=wcstoul)               | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.10240.0. Moved to api-ms-win-crt-convert-l1-1-0 in Windows 10.0.10586.0    |
| [**\_splitpath\_s**](https://www.bing.com/search?q=_splitpath_s)   | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.10240.0. Moved to api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.10586.0 |
| [**\_strlwr\_s**](https://www.bing.com/search?q=_strlwr_s)         | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.10240.0. Moved to api-ms-win-crt-string-l1-1-0 in Windows 10.0.10586.0     |
| [**\_strupr\_s**](https://www.bing.com/search?q=_strupr_s)         | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.10240.0. Moved to api-ms-win-crt-string-l1-1-0 in Windows 10.0.14393.0     |
| [**\_wcslwr\_s**](https://www.bing.com/search?q=_wcslwr_s)         | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.10240.0                                                                    |
| [**\_wcsnicmp**](https://www.bing.com/search?q=_wcsnicmp)          | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.10240.0. Moved to api-ms-win-crt-string-l1-1-0 in Windows 10.0.10586.0     |
| [**\_wcsupr\_s**](https://www.bing.com/search?q=_wcsupr_s)         | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.10240.0. Moved to api-ms-win-crt-string-l1-1-0 in Windows 10.0.10586.0     |
| [**isdigit**](https://www.bing.com/search?q=isdigit)               | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.10240.0. Moved to api-ms-win-crt-string-l1-1-0 in Windows 10.0.10586.0     |
| [**isgraph**](https://www.bing.com/search?q=isgraph)               | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.10240.0. Moved to api-ms-win-crt-string-l1-1-0 in Windows 10.0.14393.0     |
| [**islower**](https://www.bing.com/search?q=islower)               | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.10240.0. Moved to api-ms-win-crt-string-l1-1-0 in Windows 10.0.14393.0     |
| [**isprint**](https://www.bing.com/search?q=isprint)               | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.10240.0. Moved to api-ms-win-crt-string-l1-1-0 in Windows 10.0.10586.0     |
| [**iswalnum**](https://www.bing.com/search?q=iswalnum)             | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.10240.0. Moved to api-ms-win-crt-string-l1-1-0 in Windows 10.0.10586.0     |
| [**iswascii**](https://www.bing.com/search?q=iswascii)             | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.10240.0                                                                    |
| [**iswctype**](https://www.bing.com/search?q=iswctype)             | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.10240.0. Moved to api-ms-win-crt-string-l1-1-0 in Windows 10.0.10586.0     |
| [**iswprint**](https://www.bing.com/search?q=iswprint)             | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.10240.0. Moved to api-ms-win-crt-string-l1-1-0 in Windows 10.0.10586.0     |
| [**memcpy\_s**](https://www.bing.com/search?q=memcpy_s)            | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.10240.0. Moved to api-ms-win-crt-string-l1-1-0 in Windows 10.0.10586.0     |
| [**memset**](https://www.bing.com/search?q=memset)                 | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.10240.0                                                                    |
| [**strcmp**](https://msdn.microsoft.com/en-us/library/windows/apps/bb759938.aspx)                                         | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.10240.0                                                                    |
| [**strcpy\_s**](https://www.bing.com/search?q=strcpy_s)            | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.10240.0. Moved to api-ms-win-crt-string-l1-1-0 in Windows 10.0.14393.0     |
| [**strncpy\_s**](https://www.bing.com/search?q=strncpy_s)          | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.10240.0. Moved to api-ms-win-crt-string-l1-1-0 in Windows 10.0.10586.0     |
| [**strpbrk**](https://msdn.microsoft.com/en-us/library/windows/apps/bb760010.aspx)                                       | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.10240.0. Moved to api-ms-win-crt-string-l1-1-0 in Windows 10.0.10586.0     |
| [**tolower**](https://www.bing.com/search?q=tolower)               | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.10240.0. Moved to api-ms-win-crt-string-l1-1-0 in Windows 10.0.14393.0     |
| [**towlower**](https://www.bing.com/search?q=towlower)             | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.10240.0. Moved to api-ms-win-crt-string-l1-1-0 in Windows 10.0.10586.0     |
| [**towupper**](https://www.bing.com/search?q=towupper)             | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.10240.0. Moved to api-ms-win-crt-string-l1-1-0 in Windows 10.0.10586.0     |
| [**wcscat\_s**](https://www.bing.com/search?q=wcscat_s)            | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.10240.0                                                                    |
| [**wcscmp**](https://www.bing.com/search?q=wcscmp)                 | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.10240.0. Moved to api-ms-win-crt-string-l1-1-0 in Windows 10.0.10586.0     |
| [**wcslen**](https://www.bing.com/search?q=wcslen)                 | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.10240.0. Moved to api-ms-win-crt-string-l1-1-0 in Windows 10.0.10586.0     |
| [**wcsncat\_s**](https://www.bing.com/search?q=wcsncat_s)          | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.10240.0                                                                    |
| [**wcsncmp**](https://www.bing.com/search?q=wcsncmp)               | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.10240.0. Moved to api-ms-win-crt-string-l1-1-0 in Windows 10.0.10586.0     |
| [**wcsncpy\_s**](https://www.bing.com/search?q=wcsncpy_s)          | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.10240.0. Moved to api-ms-win-crt-string-l1-1-0 in Windows 10.0.10586.0     |
| [**wcsnlen**](https://www.bing.com/search?q=wcsnlen)               | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.10240.0                                                                    |
| [**wcspbrk**](https://www.bing.com/search?q=wcspbrk)               | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.10240.0. Moved to api-ms-win-crt-string-l1-1-0 in Windows 10.0.14393.0     |
| [**qsort\_s**](https://www.bing.com/search?q=qsort_s)              | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.10240.0. Moved to api-ms-win-crt-utility-l1-1-0 in Windows 10.0.10586.0    |
| [**\_atoi64**](https://www.bing.com/search?q=_atoi64)              | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.10586.0. Moved to api-ms-win-crt-convert-l1-1-0 in Windows 10.0.14393.0    |
| [**\_ultow\_s**](https://www.bing.com/search?q=_ultow_s)           | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.10586.0                                                                    |
| [**\_wcstoi64**](https://www.bing.com/search?q=_wcstoi64)          | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.10586.0. Moved to api-ms-win-crt-convert-l1-1-0 in Windows 10.0.14393.0    |
| [**\_wcstoui64**](https://www.bing.com/search?q=_wcstoui64)        | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.10586.0                                                                    |
| [**\_wsplitpath\_s**](https://www.bing.com/search?q=_wsplitpath_s) | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.10586.0. Moved to api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.14393.0 |
| [**\_\_isascii**](https://www.bing.com/search?q=__isascii)         | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.10586.0. Moved to api-ms-win-crt-string-l1-1-0 in Windows 10.0.14393.0     |
| [**\_stricmp**](https://www.bing.com/search?q=_stricmp)            | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.10586.0. Moved to api-ms-win-crt-string-l1-1-0 in Windows 10.0.14393.0     |
| [**\_strnicmp**](https://www.bing.com/search?q=_strnicmp)          | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.10586.0                                                                    |
| [**isalnum**](https://www.bing.com/search?q=isalnum)               | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.10586.0                                                                    |
| [**isspace**](https://www.bing.com/search?q=isspace)               | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.10586.0. Moved to api-ms-win-crt-string-l1-1-0 in Windows 10.0.14393.0     |
| [**isupper**](https://www.bing.com/search?q=isupper)               | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.10586.0. Moved to api-ms-win-crt-string-l1-1-0 in Windows 10.0.14393.0     |
| [**iswdigit**](https://www.bing.com/search?q=iswdigit)             | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.10586.0. Moved to api-ms-win-crt-string-l1-1-0 in Windows 10.0.14393.0     |
| [**iswspace**](https://www.bing.com/search?q=iswspace)             | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.10586.0. Moved to api-ms-win-crt-string-l1-1-0 in Windows 10.0.14393.0     |
| [**strncat\_s**](https://www.bing.com/search?q=strncat_s)          | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.10586.0. Moved to api-ms-win-crt-string-l1-1-0 in Windows 10.0.14393.0     |
| [**strtok\_s**](https://www.bing.com/search?q=strtok_s)            | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.10586.0. Moved to api-ms-win-crt-string-l1-1-0 in Windows 10.0.14393.0     |
| [**wcscpy\_s**](https://www.bing.com/search?q=wcscpy_s)            | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.10586.0                                                                    |
| [**wcscspn**](https://www.bing.com/search?q=wcscspn)               | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.10586.0                                                                    |
| [**\_ultow**](https://www.bing.com/search?q=_ultow)                | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.14393.0                                                                    |
| [**\_errno**](https://www.bing.com/search?q=_errno)                | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.14393.0                                                                    |
| [**\_wcsicmp**](https://www.bing.com/search?q=_wcsicmp)            | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.14393.0                                                                    |
| [**toupper**](https://www.bing.com/search?q=toupper)               | Introduced into api-ms-win-core-crt-l1-1-0 in Windows 10.0.14393.0                                                                    |

 

## <span id="_api-ms-win-crt-environment-l1-1-0"></span><span id="_API-MS-WIN-CRT-ENVIRONMENT-L1-1-0"></span>APIs from the API Set api-ms-win-crt-environment-l1-1-0


| API                                                                  | Requirements                                                              |
|----------------------------------------------------------------------|---------------------------------------------------------------------------|
| [**\_\_p\_\_environ**](https://www.bing.com/search?q=__p__environ)   | Introduced into api-ms-win-crt-environment-l1-1-0 in Windows 10.0.10240.0 |
| [**\_\_p\_\_wenviron**](https://www.bing.com/search?q=__p__wenviron) | Introduced into api-ms-win-crt-environment-l1-1-0 in Windows 10.0.10240.0 |
| [**\_wgetcwd**](https://www.bing.com/search?q=_wgetcwd)              | Introduced into api-ms-win-crt-environment-l1-1-0 in Windows 10.0.10240.0 |
| [**\_wgetdcwd**](https://www.bing.com/search?q=_wgetdcwd)            | Introduced into api-ms-win-crt-environment-l1-1-0 in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-crt-filesystem-l1-1-0"></span><span id="_API-MS-WIN-CRT-FILESYSTEM-L1-1-0"></span>APIs from the API Set api-ms-win-crt-filesystem-l1-1-0


| API                                                                     | Requirements                                                                                                                          |
|-------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| [**\_access**](https://www.bing.com/search?q=_access)                   | Introduced into api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_access\_s**](https://www.bing.com/search?q=_access_s)              | Introduced into api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_chdir**](https://www.bing.com/search?q=_chdir)                     | Introduced into api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_chmod**](https://www.bing.com/search?q=_chmod)                     | Introduced into api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_findclose**](https://www.bing.com/search?q=_findclose)             | Introduced into api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_findfirst32**](https://www.bing.com/search?q=_findfirst32)         | Introduced into api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_findfirst32i64**](https://www.bing.com/search?q=_findfirst32i64)   | Introduced into api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_findfirst64**](https://www.bing.com/search?q=_findfirst64)         | Introduced into api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_findfirst64i32**](https://www.bing.com/search?q=_findfirst64i32)   | Introduced into api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_findnext32**](https://www.bing.com/search?q=_findnext32)           | Introduced into api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_findnext32i64**](https://www.bing.com/search?q=_findnext32i64)     | Introduced into api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_findnext64**](https://www.bing.com/search?q=_findnext64)           | Introduced into api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_findnext64i32**](https://www.bing.com/search?q=_findnext64i32)     | Introduced into api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_fstat32**](https://www.bing.com/search?q=_fstat32)                 | Introduced into api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_fstat32i64**](https://www.bing.com/search?q=_fstat32i64)           | Introduced into api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_fstat64**](https://www.bing.com/search?q=_fstat64)                 | Introduced into api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_fstat64i32**](https://www.bing.com/search?q=_fstat64i32)           | Introduced into api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_fullpath**](https://www.bing.com/search?q=_fullpath)               | Introduced into api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_lock\_file**](https://www.bing.com/search?q=_lock_file)            | Introduced into api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_makepath**](https://www.bing.com/search?q=_makepath)               | Introduced into api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_makepath\_s**](https://www.bing.com/search?q=_makepath_s)          | Introduced into api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_mkdir**](https://www.bing.com/search?q=_mkdir)                     | Introduced into api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_rmdir**](https://www.bing.com/search?q=_rmdir)                     | Introduced into api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_splitpath**](https://www.bing.com/search?q=_splitpath)             | Introduced into api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_stat32**](https://www.bing.com/search?q=_stat32)                   | Introduced into api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_stat32i64**](https://www.bing.com/search?q=_stat32i64)             | Introduced into api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_stat64**](https://www.bing.com/search?q=_stat64)                   | Introduced into api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_stat64i32**](https://www.bing.com/search?q=_stat64i32)             | Introduced into api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_umask**](https://www.bing.com/search?q=_umask)                     | Introduced into api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_umask\_s**](https://www.bing.com/search?q=_umask_s)                | Introduced into api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_unlink**](https://www.bing.com/search?q=_unlink)                   | Introduced into api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_unlock\_file**](https://www.bing.com/search?q=_unlock_file)        | Introduced into api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_waccess**](https://www.bing.com/search?q=_waccess)                 | Introduced into api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_waccess\_s**](https://www.bing.com/search?q=_waccess_s)            | Introduced into api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wchdir**](https://www.bing.com/search?q=_wchdir)                   | Introduced into api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wchmod**](https://www.bing.com/search?q=_wchmod)                   | Introduced into api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wfindfirst32**](https://www.bing.com/search?q=_wfindfirst32)       | Introduced into api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wfindfirst32i64**](https://www.bing.com/search?q=_wfindfirst32i64) | Introduced into api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wfindfirst64**](https://www.bing.com/search?q=_wfindfirst64)       | Introduced into api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wfindfirst64i32**](https://www.bing.com/search?q=_wfindfirst64i32) | Introduced into api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wfindnext32**](https://www.bing.com/search?q=_wfindnext32)         | Introduced into api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wfindnext32i64**](https://www.bing.com/search?q=_wfindnext32i64)   | Introduced into api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wfindnext64**](https://www.bing.com/search?q=_wfindnext64)         | Introduced into api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wfindnext64i32**](https://www.bing.com/search?q=_wfindnext64i32)   | Introduced into api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wfullpath**](https://www.bing.com/search?q=_wfullpath)             | Introduced into api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wmakepath**](https://www.bing.com/search?q=_wmakepath)             | Introduced into api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wmakepath\_s**](https://www.bing.com/search?q=_wmakepath_s)        | Introduced into api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wmkdir**](https://www.bing.com/search?q=_wmkdir)                   | Introduced into api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wremove**](https://www.bing.com/search?q=_wremove)                 | Introduced into api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wrename**](https://www.bing.com/search?q=_wrename)                 | Introduced into api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wrmdir**](https://www.bing.com/search?q=_wrmdir)                   | Introduced into api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wsplitpath**](https://www.bing.com/search?q=_wsplitpath)           | Introduced into api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wsplitpath\_s**](https://www.bing.com/search?q=_wsplitpath_s)      | Introduced into api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.10240.0. Moved to api-ms-win-core-crt-l1-1-0 in Windows 10.0.10586.0 |
| [**\_wstat32**](https://www.bing.com/search?q=_wstat32)                 | Introduced into api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wstat32i64**](https://www.bing.com/search?q=_wstat32i64)           | Introduced into api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wstat64**](https://www.bing.com/search?q=_wstat64)                 | Introduced into api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wstat64i32**](https://www.bing.com/search?q=_wstat64i32)           | Introduced into api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wunlink**](https://www.bing.com/search?q=_wunlink)                 | Introduced into api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**remove**](https://www.bing.com/search?q=remove)                      | Introduced into api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**rename**](https://www.bing.com/search?q=rename)                      | Introduced into api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_splitpath\_s**](https://www.bing.com/search?q=_splitpath_s)        | Introduced into api-ms-win-crt-filesystem-l1-1-0 in Windows 10.0.10586.0                                                              |

 

## <span id="_api-ms-win-crt-stdio-l1-1-0"></span><span id="_API-MS-WIN-CRT-STDIO-L1-1-0"></span>APIs from the API Set api-ms-win-crt-stdio-l1-1-0


| API                                                                                               | Requirements                                                        |
|---------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| [**\_getcwd**](https://www.bing.com/search?q=_getcwd)                                             | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_getdcwd**](https://www.bing.com/search?q=_getdcwd)                                           | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_\_acrt\_iob\_func**](https://www.bing.com/search?q=__acrt_iob_func)                          | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_\_p\_\_commode**](https://www.bing.com/search?q=__p__commode)                                | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_\_p\_\_fmode**](https://www.bing.com/search?q=__p__fmode)                                    | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_\_stdio\_common\_vfprintf**](https://www.bing.com/search?q=__stdio_common_vfprintf)          | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_\_stdio\_common\_vfprintf\_p**](https://www.bing.com/search?q=__stdio_common_vfprintf_p)     | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_\_stdio\_common\_vfprintf\_s**](https://www.bing.com/search?q=__stdio_common_vfprintf_s)     | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_\_stdio\_common\_vfscanf**](https://www.bing.com/search?q=__stdio_common_vfscanf)            | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_\_stdio\_common\_vfwprintf**](https://www.bing.com/search?q=__stdio_common_vfwprintf)        | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_\_stdio\_common\_vfwprintf\_p**](https://www.bing.com/search?q=__stdio_common_vfwprintf_p)   | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_\_stdio\_common\_vfwprintf\_s**](https://www.bing.com/search?q=__stdio_common_vfwprintf_s)   | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_\_stdio\_common\_vfwscanf**](https://www.bing.com/search?q=__stdio_common_vfwscanf)          | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_\_stdio\_common\_vsnprintf\_s**](https://www.bing.com/search?q=__stdio_common_vsnprintf_s)   | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_\_stdio\_common\_vsnwprintf\_s**](https://www.bing.com/search?q=__stdio_common_vsnwprintf_s) | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_\_stdio\_common\_vsprintf**](https://www.bing.com/search?q=__stdio_common_vsprintf)          | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_\_stdio\_common\_vsprintf\_p**](https://www.bing.com/search?q=__stdio_common_vsprintf_p)     | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_\_stdio\_common\_vsprintf\_s**](https://www.bing.com/search?q=__stdio_common_vsprintf_s)     | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_\_stdio\_common\_vsscanf**](https://www.bing.com/search?q=__stdio_common_vsscanf)            | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_\_stdio\_common\_vswprintf**](https://www.bing.com/search?q=__stdio_common_vswprintf)        | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_\_stdio\_common\_vswprintf\_p**](https://www.bing.com/search?q=__stdio_common_vswprintf_p)   | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_\_stdio\_common\_vswprintf\_s**](https://www.bing.com/search?q=__stdio_common_vswprintf_s)   | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_\_stdio\_common\_vswscanf**](https://www.bing.com/search?q=__stdio_common_vswscanf)          | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_chsize**](https://www.bing.com/search?q=_chsize)                                             | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_chsize\_s**](https://www.bing.com/search?q=_chsize_s)                                        | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_close**](https://www.bing.com/search?q=_close)                                               | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_commit**](https://www.bing.com/search?q=_commit)                                             | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_creat**](https://www.bing.com/search?q=_creat)                                               | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_dup**](https://www.bing.com/search?q=_dup)                                                   | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_dup2**](https://www.bing.com/search?q=_dup2)                                                 | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_eof**](https://www.bing.com/search?q=_eof)                                                   | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_fclose\_nolock**](https://www.bing.com/search?q=_fclose_nolock)                              | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_fcloseall**](https://www.bing.com/search?q=_fcloseall)                                       | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_fflush\_nolock**](https://www.bing.com/search?q=_fflush_nolock)                              | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_fgetc\_nolock**](https://www.bing.com/search?q=_fgetc_nolock)                                | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_fgetchar**](https://www.bing.com/search?q=_fgetchar)                                         | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_fgetwc\_nolock**](https://www.bing.com/search?q=_fgetwc_nolock)                              | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_fgetwchar**](https://www.bing.com/search?q=_fgetwchar)                                       | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_filelength**](https://www.bing.com/search?q=_filelength)                                     | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_filelengthi64**](https://www.bing.com/search?q=_filelengthi64)                               | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_fileno**](https://www.bing.com/search?q=_fileno)                                             | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_flushall**](https://www.bing.com/search?q=_flushall)                                         | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_fputc\_nolock**](https://www.bing.com/search?q=_fputc_nolock)                                | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_fputchar**](https://www.bing.com/search?q=_fputchar)                                         | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_fputwc\_nolock**](https://www.bing.com/search?q=_fputwc_nolock)                              | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_fputwchar**](https://www.bing.com/search?q=_fputwchar)                                       | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_fread\_nolock**](https://www.bing.com/search?q=_fread_nolock)                                | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_fread\_nolock\_s**](https://www.bing.com/search?q=_fread_nolock_s)                           | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_fseek\_nolock**](https://www.bing.com/search?q=_fseek_nolock)                                | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_fseeki64**](https://www.bing.com/search?q=_fseeki64)                                         | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_fseeki64\_nolock**](https://www.bing.com/search?q=_fseeki64_nolock)                          | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_fsopen**](https://www.bing.com/search?q=_fsopen)                                             | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_ftell\_nolock**](https://www.bing.com/search?q=_ftell_nolock)                                | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_ftelli64**](https://www.bing.com/search?q=_ftelli64)                                         | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_ftelli64\_nolock**](https://www.bing.com/search?q=_ftelli64_nolock)                          | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_fwrite\_nolock**](https://www.bing.com/search?q=_fwrite_nolock)                              | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_get\_fmode**](https://www.bing.com/search?q=_get_fmode)                                      | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_get\_osfhandle**](https://www.bing.com/search?q=_get_osfhandle)                              | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_get\_printf\_count\_output**](https://www.bing.com/search?q=_get_printf_count_output)        | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_get\_stream\_buffer\_pointers**](https://www.bing.com/search?q=_get_stream_buffer_pointers)  | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_getc\_nolock**](https://www.bing.com/search?q=_getc_nolock)                                  | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_getmaxstdio**](https://www.bing.com/search?q=_getmaxstdio)                                   | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_getw**](https://www.bing.com/search?q=_getw)                                                 | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_getwc\_nolock**](https://www.bing.com/search?q=_getwc_nolock)                                | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_getws**](https://www.bing.com/search?q=_getws)                                               | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_getws\_s**](https://www.bing.com/search?q=_getws_s)                                          | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_isatty**](https://www.bing.com/search?q=_isatty)                                             | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_locking**](https://www.bing.com/search?q=_locking)                                           | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_lseek**](https://www.bing.com/search?q=_lseek)                                               | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_lseeki64**](https://www.bing.com/search?q=_lseeki64)                                         | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_mktemp**](https://www.bing.com/search?q=_mktemp)                                             | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_mktemp\_s**](https://www.bing.com/search?q=_mktemp_s)                                        | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_open**](https://www.bing.com/search?q=_open)                                                 | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_open\_osfhandle**](https://www.bing.com/search?q=_open_osfhandle)                            | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_putc\_nolock**](https://www.bing.com/search?q=_putc_nolock)                                  | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_putw**](https://www.bing.com/search?q=_putw)                                                 | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_putwc\_nolock**](https://www.bing.com/search?q=_putwc_nolock)                                | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_putws**](https://www.bing.com/search?q=_putws)                                               | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_read**](https://www.bing.com/search?q=_read)                                                 | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_rmtmp**](https://www.bing.com/search?q=_rmtmp)                                               | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_set\_fmode**](https://www.bing.com/search?q=_set_fmode)                                      | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_set\_printf\_count\_output**](https://www.bing.com/search?q=_set_printf_count_output)        | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_setmaxstdio**](https://www.bing.com/search?q=_setmaxstdio)                                   | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_setmode**](https://www.bing.com/search?q=_setmode)                                           | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_sopen**](https://www.bing.com/search?q=_sopen)                                               | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_sopen\_dispatch**](https://www.bing.com/search?q=_sopen_dispatch)                            | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_sopen\_s**](https://www.bing.com/search?q=_sopen_s)                                          | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_tell**](https://www.bing.com/search?q=_tell)                                                 | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_telli64**](https://www.bing.com/search?q=_telli64)                                           | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_tempnam**](https://www.bing.com/search?q=_tempnam)                                           | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_ungetc\_nolock**](https://www.bing.com/search?q=_ungetc_nolock)                              | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_ungetwc\_nolock**](https://www.bing.com/search?q=_ungetwc_nolock)                            | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_wcreat**](https://www.bing.com/search?q=_wcreat)                                             | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_wfdopen**](https://www.bing.com/search?q=_wfdopen)                                           | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_wfopen**](https://www.bing.com/search?q=_wfopen)                                             | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_wfopen\_s**](https://www.bing.com/search?q=_wfopen_s)                                        | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_wfreopen**](https://www.bing.com/search?q=_wfreopen)                                         | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_wfreopen\_s**](https://www.bing.com/search?q=_wfreopen_s)                                    | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_wfsopen**](https://www.bing.com/search?q=_wfsopen)                                           | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_wmktemp**](https://www.bing.com/search?q=_wmktemp)                                           | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_wmktemp\_s**](https://www.bing.com/search?q=_wmktemp_s)                                      | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_wopen**](https://www.bing.com/search?q=_wopen)                                               | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_write**](https://www.bing.com/search?q=_write)                                               | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_wsopen**](https://www.bing.com/search?q=_wsopen)                                             | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_wsopen\_dispatch**](https://www.bing.com/search?q=_wsopen_dispatch)                          | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_wsopen\_s**](https://www.bing.com/search?q=_wsopen_s)                                        | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_wtempnam**](https://www.bing.com/search?q=_wtempnam)                                         | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_wtmpnam**](https://www.bing.com/search?q=_wtmpnam)                                           | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**\_wtmpnam\_s**](https://www.bing.com/search?q=_wtmpnam_s)                                      | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**clearerr**](https://www.bing.com/search?q=clearerr)                                            | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**clearerr\_s**](https://www.bing.com/search?q=clearerr_s)                                       | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**fclose**](https://www.bing.com/search?q=fclose)                                                | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**feof**](https://www.bing.com/search?q=feof)                                                    | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**ferror**](https://www.bing.com/search?q=ferror)                                                | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**fflush**](https://www.bing.com/search?q=fflush)                                                | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**fgetc**](https://www.bing.com/search?q=fgetc)                                                  | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**fgetpos**](https://www.bing.com/search?q=fgetpos)                                              | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**fgets**](https://www.bing.com/search?q=fgets)                                                  | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**fgetwc**](https://www.bing.com/search?q=fgetwc)                                                | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**fgetws**](https://www.bing.com/search?q=fgetws)                                                | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**fopen**](https://www.bing.com/search?q=fopen)                                                  | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**fopen\_s**](https://www.bing.com/search?q=fopen_s)                                             | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**fputc**](https://www.bing.com/search?q=fputc)                                                  | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**fputs**](https://www.bing.com/search?q=fputs)                                                  | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**fputwc**](https://www.bing.com/search?q=fputwc)                                                | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**fputws**](https://www.bing.com/search?q=fputws)                                                | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**fread**](https://www.bing.com/search?q=fread)                                                  | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**fread\_s**](https://www.bing.com/search?q=fread_s)                                             | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**freopen**](https://www.bing.com/search?q=freopen)                                              | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**freopen\_s**](https://www.bing.com/search?q=freopen_s)                                         | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**fseek**](https://www.bing.com/search?q=fseek)                                                  | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**fsetpos**](https://www.bing.com/search?q=fsetpos)                                              | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**ftell**](https://www.bing.com/search?q=ftell)                                                  | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**fwrite**](https://www.bing.com/search?q=fwrite)                                                | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**getc**](https://www.bing.com/search?q=getc)                                                    | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**getchar**](https://www.bing.com/search?q=getchar)                                              | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**gets\_s**](https://www.bing.com/search?q=gets_s)                                               | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**getwc**](https://www.bing.com/search?q=getwc)                                                  | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**getwchar**](https://www.bing.com/search?q=getwchar)                                            | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**putc**](https://www.bing.com/search?q=putc)                                                    | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**putchar**](https://www.bing.com/search?q=putchar)                                              | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**puts**](https://www.bing.com/search?q=puts)                                                    | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**putwc**](https://www.bing.com/search?q=putwc)                                                  | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**putwchar**](https://www.bing.com/search?q=putwchar)                                            | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**rewind**](https://www.bing.com/search?q=rewind)                                                | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**setbuf**](https://www.bing.com/search?q=setbuf)                                                | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**setvbuf**](https://www.bing.com/search?q=setvbuf)                                              | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**tmpfile**](https://www.bing.com/search?q=tmpfile)                                              | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**tmpfile\_s**](https://www.bing.com/search?q=tmpfile_s)                                         | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**tmpnam**](https://www.bing.com/search?q=tmpnam)                                                | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**tmpnam\_s**](https://www.bing.com/search?q=tmpnam_s)                                           | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**ungetc**](https://www.bing.com/search?q=ungetc)                                                | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |
| [**ungetwc**](https://www.bing.com/search?q=ungetwc)                                              | Introduced into api-ms-win-crt-stdio-l1-1-0 in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-crt-heap-l1-1-0"></span><span id="_API-MS-WIN-CRT-HEAP-L1-1-0"></span>APIs from the API Set api-ms-win-crt-heap-l1-1-0


| API                                                                                       | Requirements                                                       |
|-------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| [**\_aligned\_free**](https://www.bing.com/search?q=_aligned_free)                        | Introduced into api-ms-win-crt-heap-l1-1-0 in Windows 10.0.10240.0 |
| [**\_aligned\_malloc**](https://www.bing.com/search?q=_aligned_malloc)                    | Introduced into api-ms-win-crt-heap-l1-1-0 in Windows 10.0.10240.0 |
| [**\_aligned\_msize**](https://www.bing.com/search?q=_aligned_msize)                      | Introduced into api-ms-win-crt-heap-l1-1-0 in Windows 10.0.10240.0 |
| [**\_aligned\_offset\_malloc**](https://www.bing.com/search?q=_aligned_offset_malloc)     | Introduced into api-ms-win-crt-heap-l1-1-0 in Windows 10.0.10240.0 |
| [**\_aligned\_offset\_realloc**](https://www.bing.com/search?q=_aligned_offset_realloc)   | Introduced into api-ms-win-crt-heap-l1-1-0 in Windows 10.0.10240.0 |
| [**\_aligned\_offset\_recalloc**](https://www.bing.com/search?q=_aligned_offset_recalloc) | Introduced into api-ms-win-crt-heap-l1-1-0 in Windows 10.0.10240.0 |
| [**\_aligned\_realloc**](https://www.bing.com/search?q=_aligned_realloc)                  | Introduced into api-ms-win-crt-heap-l1-1-0 in Windows 10.0.10240.0 |
| [**\_aligned\_recalloc**](https://www.bing.com/search?q=_aligned_recalloc)                | Introduced into api-ms-win-crt-heap-l1-1-0 in Windows 10.0.10240.0 |
| [**\_callnewh**](https://www.bing.com/search?q=_callnewh)                                 | Introduced into api-ms-win-crt-heap-l1-1-0 in Windows 10.0.10240.0 |
| [**\_calloc\_base**](https://www.bing.com/search?q=_calloc_base)                          | Introduced into api-ms-win-crt-heap-l1-1-0 in Windows 10.0.10240.0 |
| [**\_expand**](https://www.bing.com/search?q=_expand)                                     | Introduced into api-ms-win-crt-heap-l1-1-0 in Windows 10.0.10240.0 |
| [**\_free\_base**](https://www.bing.com/search?q=_free_base)                              | Introduced into api-ms-win-crt-heap-l1-1-0 in Windows 10.0.10240.0 |
| [**\_get\_heap\_handle**](https://www.bing.com/search?q=_get_heap_handle)                 | Introduced into api-ms-win-crt-heap-l1-1-0 in Windows 10.0.10240.0 |
| [**\_heapmin**](https://www.bing.com/search?q=_heapmin)                                   | Introduced into api-ms-win-crt-heap-l1-1-0 in Windows 10.0.10240.0 |
| [**\_malloc\_base**](https://www.bing.com/search?q=_malloc_base)                          | Introduced into api-ms-win-crt-heap-l1-1-0 in Windows 10.0.10240.0 |
| [**\_msize**](https://www.bing.com/search?q=_msize)                                       | Introduced into api-ms-win-crt-heap-l1-1-0 in Windows 10.0.10240.0 |
| [**\_query\_new\_handler**](https://www.bing.com/search?q=_query_new_handler)             | Introduced into api-ms-win-crt-heap-l1-1-0 in Windows 10.0.10240.0 |
| [**\_query\_new\_mode**](https://www.bing.com/search?q=_query_new_mode)                   | Introduced into api-ms-win-crt-heap-l1-1-0 in Windows 10.0.10240.0 |
| [**\_realloc\_base**](https://www.bing.com/search?q=_realloc_base)                        | Introduced into api-ms-win-crt-heap-l1-1-0 in Windows 10.0.10240.0 |
| [**\_recalloc**](https://www.bing.com/search?q=_recalloc)                                 | Introduced into api-ms-win-crt-heap-l1-1-0 in Windows 10.0.10240.0 |
| [**\_set\_new\_mode**](https://www.bing.com/search?q=_set_new_mode)                       | Introduced into api-ms-win-crt-heap-l1-1-0 in Windows 10.0.10240.0 |
| [**calloc**](https://www.bing.com/search?q=calloc)                                        | Introduced into api-ms-win-crt-heap-l1-1-0 in Windows 10.0.10240.0 |
| [**free**](https://www.bing.com/search?q=free)                                            | Introduced into api-ms-win-crt-heap-l1-1-0 in Windows 10.0.10240.0 |
| [**malloc**](https://www.bing.com/search?q=malloc)                                        | Introduced into api-ms-win-crt-heap-l1-1-0 in Windows 10.0.10240.0 |
| [**realloc**](https://www.bing.com/search?q=realloc)                                      | Introduced into api-ms-win-crt-heap-l1-1-0 in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-crt-locale-l1-1-0"></span><span id="_API-MS-WIN-CRT-LOCALE-L1-1-0"></span>APIs from the API Set api-ms-win-crt-locale-l1-1-0


| API                                                                                      | Requirements                                                         |
|------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| [**\_\_\_lc\_codepage\_func**](https://www.bing.com/search?q=___lc_codepage_func)        | Introduced into api-ms-win-crt-locale-l1-1-0 in Windows 10.0.10240.0 |
| [**\_\_\_lc\_collate\_cp\_func**](https://www.bing.com/search?q=___lc_collate_cp_func)   | Introduced into api-ms-win-crt-locale-l1-1-0 in Windows 10.0.10240.0 |
| [**\_\_\_lc\_locale\_name\_func**](https://www.bing.com/search?q=___lc_locale_name_func) | Introduced into api-ms-win-crt-locale-l1-1-0 in Windows 10.0.10240.0 |
| [**\_\_\_mb\_cur\_max\_func**](https://www.bing.com/search?q=___mb_cur_max_func)         | Introduced into api-ms-win-crt-locale-l1-1-0 in Windows 10.0.10240.0 |
| [**\_\_\_mb\_cur\_max\_l\_func**](https://www.bing.com/search?q=___mb_cur_max_l_func)    | Introduced into api-ms-win-crt-locale-l1-1-0 in Windows 10.0.10240.0 |
| [**\_\_pctype\_func**](https://www.bing.com/search?q=__pctype_func)                      | Introduced into api-ms-win-crt-locale-l1-1-0 in Windows 10.0.10240.0 |
| [**\_\_pwctype\_func**](https://www.bing.com/search?q=__pwctype_func)                    | Introduced into api-ms-win-crt-locale-l1-1-0 in Windows 10.0.10240.0 |
| [**\_configthreadlocale**](https://www.bing.com/search?q=_configthreadlocale)            | Introduced into api-ms-win-crt-locale-l1-1-0 in Windows 10.0.10240.0 |
| [**\_create\_locale**](https://www.bing.com/search?q=_create_locale)                     | Introduced into api-ms-win-crt-locale-l1-1-0 in Windows 10.0.10240.0 |
| [**\_free\_locale**](https://www.bing.com/search?q=_free_locale)                         | Introduced into api-ms-win-crt-locale-l1-1-0 in Windows 10.0.10240.0 |
| [**\_get\_current\_locale**](https://www.bing.com/search?q=_get_current_locale)          | Introduced into api-ms-win-crt-locale-l1-1-0 in Windows 10.0.10240.0 |
| [**\_getmbcp**](https://www.bing.com/search?q=_getmbcp)                                  | Introduced into api-ms-win-crt-locale-l1-1-0 in Windows 10.0.10240.0 |
| [**\_lock\_locales**](https://www.bing.com/search?q=_lock_locales)                       | Introduced into api-ms-win-crt-locale-l1-1-0 in Windows 10.0.10240.0 |
| [**\_setmbcp**](https://www.bing.com/search?q=_setmbcp)                                  | Introduced into api-ms-win-crt-locale-l1-1-0 in Windows 10.0.10240.0 |
| [**\_unlock\_locales**](https://www.bing.com/search?q=_unlock_locales)                   | Introduced into api-ms-win-crt-locale-l1-1-0 in Windows 10.0.10240.0 |
| [**\_wcreate\_locale**](https://www.bing.com/search?q=_wcreate_locale)                   | Introduced into api-ms-win-crt-locale-l1-1-0 in Windows 10.0.10240.0 |
| [**\_wsetlocale**](https://www.bing.com/search?q=_wsetlocale)                            | Introduced into api-ms-win-crt-locale-l1-1-0 in Windows 10.0.10240.0 |
| [**localeconv**](https://www.bing.com/search?q=localeconv)                               | Introduced into api-ms-win-crt-locale-l1-1-0 in Windows 10.0.10240.0 |
| [**setlocale**](https://www.bing.com/search?q=setlocale)                                 | Introduced into api-ms-win-crt-locale-l1-1-0 in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-crt-math-l1-1-0"></span><span id="_API-MS-WIN-CRT-MATH-L1-1-0"></span>APIs from the API Set api-ms-win-crt-math-l1-1-0


| API                                                                       | Requirements                                                       |
|---------------------------------------------------------------------------|--------------------------------------------------------------------|
| [**\_\_setusermatherr**](https://www.bing.com/search?q=__setusermatherr)  | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_cabs**](https://www.bing.com/search?q=_cabs)                         | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_Cbuild**](https://www.bing.com/search?q=_Cbuild)                     | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_chgsign**](https://www.bing.com/search?q=_chgsign)                   | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_chgsignf**](https://www.bing.com/search?q=_chgsignf)                 | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_Cmulcc**](https://www.bing.com/search?q=_Cmulcc)                     | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_Cmulcr**](https://www.bing.com/search?q=_Cmulcr)                     | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_copysign**](https://www.bing.com/search?q=_copysign)                 | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_copysignf**](https://www.bing.com/search?q=_copysignf)               | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_d\_int**](https://www.bing.com/search?q=_d_int)                      | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_dclass**](https://www.bing.com/search?q=_dclass)                     | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_dexp**](https://www.bing.com/search?q=_dexp)                         | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_dlog**](https://www.bing.com/search?q=_dlog)                         | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_dnorm**](https://www.bing.com/search?q=_dnorm)                       | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_dpcomp**](https://www.bing.com/search?q=_dpcomp)                     | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_dpoly**](https://www.bing.com/search?q=_dpoly)                       | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_dscale**](https://www.bing.com/search?q=_dscale)                     | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_dsign**](https://www.bing.com/search?q=_dsign)                       | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_dsin**](https://www.bing.com/search?q=_dsin)                         | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_dtest**](https://www.bing.com/search?q=_dtest)                       | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_dunscale**](https://www.bing.com/search?q=_dunscale)                 | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_FCbuild**](https://www.bing.com/search?q=_FCbuild)                   | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_FCmulcc**](https://www.bing.com/search?q=_FCmulcc)                   | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_FCmulcr**](https://www.bing.com/search?q=_FCmulcr)                   | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_fd\_int**](https://www.bing.com/search?q=_fd_int)                    | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_fdclass**](https://www.bing.com/search?q=_fdclass)                   | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_fdexp**](https://www.bing.com/search?q=_fdexp)                       | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_fdlog**](https://www.bing.com/search?q=_fdlog)                       | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_fdnorm**](https://www.bing.com/search?q=_fdnorm)                     | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_fdopen**](https://www.bing.com/search?q=_fdopen)                     | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_fdpcomp**](https://www.bing.com/search?q=_fdpcomp)                   | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_fdpoly**](https://www.bing.com/search?q=_fdpoly)                     | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_fdscale**](https://www.bing.com/search?q=_fdscale)                   | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_fdsign**](https://www.bing.com/search?q=_fdsign)                     | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_fdsin**](https://www.bing.com/search?q=_fdsin)                       | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_fdtest**](https://www.bing.com/search?q=_fdtest)                     | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_fdunscale**](https://www.bing.com/search?q=_fdunscale)               | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_finite**](https://www.bing.com/search?q=_finite)                     | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_finitef**](https://www.bing.com/search?q=_finitef)                   | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_fpclass**](https://www.bing.com/search?q=_fpclass)                   | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_fpclassf**](https://www.bing.com/search?q=_fpclassf)                 | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_get\_FMA3\_enable**](https://www.bing.com/search?q=_get_FMA3_enable) | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_hypot**](https://www.bing.com/search?q=_hypot)                       | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_hypotf**](https://www.bing.com/search?q=_hypotf)                     | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_isnan**](https://www.bing.com/search?q=_isnan)                       | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_isnanf**](https://www.bing.com/search?q=_isnanf)                     | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_j0**](https://www.bing.com/search?q=_j0)                             | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_j1**](https://www.bing.com/search?q=_j1)                             | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_jn**](https://www.bing.com/search?q=_jn)                             | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_LCbuild**](https://www.bing.com/search?q=_LCbuild)                   | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_LCmulcc**](https://www.bing.com/search?q=_LCmulcc)                   | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_LCmulcr**](https://www.bing.com/search?q=_LCmulcr)                   | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_ld\_int**](https://www.bing.com/search?q=_ld_int)                    | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_ldclass**](https://www.bing.com/search?q=_ldclass)                   | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_ldexp**](https://www.bing.com/search?q=_ldexp)                       | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_ldlog**](https://www.bing.com/search?q=_ldlog)                       | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_ldpcomp**](https://www.bing.com/search?q=_ldpcomp)                   | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_ldpoly**](https://www.bing.com/search?q=_ldpoly)                     | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_ldscale**](https://www.bing.com/search?q=_ldscale)                   | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_ldsign**](https://www.bing.com/search?q=_ldsign)                     | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_ldsin**](https://www.bing.com/search?q=_ldsin)                       | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_ldtest**](https://www.bing.com/search?q=_ldtest)                     | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_ldunscale**](https://www.bing.com/search?q=_ldunscale)               | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_logb**](https://www.bing.com/search?q=_logb)                         | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_logbf**](https://www.bing.com/search?q=_logbf)                       | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_nextafter**](https://www.bing.com/search?q=_nextafter)               | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_nextafterf**](https://www.bing.com/search?q=_nextafterf)             | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_scalb**](https://www.bing.com/search?q=_scalb)                       | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_scalbf**](https://www.bing.com/search?q=_scalbf)                     | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_set\_FMA3\_enable**](https://www.bing.com/search?q=_set_FMA3_enable) | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_y0**](https://www.bing.com/search?q=_y0)                             | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_y1**](https://www.bing.com/search?q=_y1)                             | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**\_yn**](https://www.bing.com/search?q=_yn)                             | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**acos**](https://www.bing.com/search?q=acos)                            | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**acosf**](https://www.bing.com/search?q=acosf)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**acosh**](https://www.bing.com/search?q=acosh)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**acoshf**](https://www.bing.com/search?q=acoshf)                        | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**acoshl**](https://www.bing.com/search?q=acoshl)                        | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**asin**](https://www.bing.com/search?q=asin)                            | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**asinf**](https://www.bing.com/search?q=asinf)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**asinh**](https://www.bing.com/search?q=asinh)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**asinhf**](https://www.bing.com/search?q=asinhf)                        | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**asinhl**](https://www.bing.com/search?q=asinhl)                        | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**atan**](https://www.bing.com/search?q=atan)                            | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**atan2**](https://www.bing.com/search?q=atan2)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**atan2f**](https://www.bing.com/search?q=atan2f)                        | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**atanf**](https://www.bing.com/search?q=atanf)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**atanh**](https://www.bing.com/search?q=atanh)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**atanhf**](https://www.bing.com/search?q=atanhf)                        | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**atanhl**](https://www.bing.com/search?q=atanhl)                        | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**cabs**](https://www.bing.com/search?q=cabs)                            | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**cabsf**](https://www.bing.com/search?q=cabsf)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**cabsl**](https://www.bing.com/search?q=cabsl)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**cacos**](https://www.bing.com/search?q=cacos)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**cacosf**](https://www.bing.com/search?q=cacosf)                        | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**cacosh**](https://www.bing.com/search?q=cacosh)                        | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**cacoshf**](https://www.bing.com/search?q=cacoshf)                      | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**cacoshl**](https://www.bing.com/search?q=cacoshl)                      | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**cacosl**](https://www.bing.com/search?q=cacosl)                        | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**carg**](https://www.bing.com/search?q=carg)                            | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**cargf**](https://www.bing.com/search?q=cargf)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**cargl**](https://www.bing.com/search?q=cargl)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**casin**](https://www.bing.com/search?q=casin)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**casinf**](https://www.bing.com/search?q=casinf)                        | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**casinh**](https://www.bing.com/search?q=casinh)                        | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**casinhf**](https://www.bing.com/search?q=casinhf)                      | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**casinhl**](https://www.bing.com/search?q=casinhl)                      | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**casinl**](https://www.bing.com/search?q=casinl)                        | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**catan**](https://www.bing.com/search?q=catan)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**catanf**](https://www.bing.com/search?q=catanf)                        | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**catanh**](https://www.bing.com/search?q=catanh)                        | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**catanhf**](https://www.bing.com/search?q=catanhf)                      | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**catanhl**](https://www.bing.com/search?q=catanhl)                      | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**catanl**](https://www.bing.com/search?q=catanl)                        | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**cbrt**](https://www.bing.com/search?q=cbrt)                            | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**cbrtf**](https://www.bing.com/search?q=cbrtf)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**cbrtl**](https://www.bing.com/search?q=cbrtl)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**ccos**](https://www.bing.com/search?q=ccos)                            | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**ccosf**](https://www.bing.com/search?q=ccosf)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**ccosh**](https://www.bing.com/search?q=ccosh)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**ccoshf**](https://www.bing.com/search?q=ccoshf)                        | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**ccoshl**](https://www.bing.com/search?q=ccoshl)                        | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**ccosl**](https://www.bing.com/search?q=ccosl)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**ceil**](https://www.bing.com/search?q=ceil)                            | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**ceilf**](https://www.bing.com/search?q=ceilf)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**cexp**](https://www.bing.com/search?q=cexp)                            | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**cexpf**](https://www.bing.com/search?q=cexpf)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**cexpl**](https://www.bing.com/search?q=cexpl)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**cimag**](https://www.bing.com/search?q=cimag)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**cimagf**](https://www.bing.com/search?q=cimagf)                        | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**cimagl**](https://www.bing.com/search?q=cimagl)                        | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**clog**](https://www.bing.com/search?q=clog)                            | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**clog10**](https://www.bing.com/search?q=clog10)                        | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**clog10f**](https://www.bing.com/search?q=clog10f)                      | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**clog10l**](https://www.bing.com/search?q=clog10l)                      | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**clogf**](https://www.bing.com/search?q=clogf)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**clogl**](https://www.bing.com/search?q=clogl)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**conj**](https://www.bing.com/search?q=conj)                            | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**conjf**](https://www.bing.com/search?q=conjf)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**conjl**](https://www.bing.com/search?q=conjl)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**copysign**](https://www.bing.com/search?q=copysign)                    | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**copysignf**](https://www.bing.com/search?q=copysignf)                  | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**copysignl**](https://www.bing.com/search?q=copysignl)                  | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**cos**](https://www.bing.com/search?q=cos)                              | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**cosf**](https://www.bing.com/search?q=cosf)                            | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**cosh**](https://www.bing.com/search?q=cosh)                            | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**coshf**](https://www.bing.com/search?q=coshf)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**cpow**](https://www.bing.com/search?q=cpow)                            | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**cpowf**](https://www.bing.com/search?q=cpowf)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**cpowl**](https://www.bing.com/search?q=cpowl)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**cproj**](https://www.bing.com/search?q=cproj)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**cprojf**](https://www.bing.com/search?q=cprojf)                        | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**cprojl**](https://www.bing.com/search?q=cprojl)                        | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**creal**](https://www.bing.com/search?q=creal)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**crealf**](https://www.bing.com/search?q=crealf)                        | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**creall**](https://www.bing.com/search?q=creall)                        | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**csin**](https://www.bing.com/search?q=csin)                            | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**csinf**](https://www.bing.com/search?q=csinf)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**csinh**](https://www.bing.com/search?q=csinh)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**csinhf**](https://www.bing.com/search?q=csinhf)                        | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**csinhl**](https://www.bing.com/search?q=csinhl)                        | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**csinl**](https://www.bing.com/search?q=csinl)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**csqrt**](https://www.bing.com/search?q=csqrt)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**csqrtf**](https://www.bing.com/search?q=csqrtf)                        | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**csqrtl**](https://www.bing.com/search?q=csqrtl)                        | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**ctan**](https://www.bing.com/search?q=ctan)                            | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**ctanf**](https://www.bing.com/search?q=ctanf)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**ctanh**](https://www.bing.com/search?q=ctanh)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**ctanhf**](https://www.bing.com/search?q=ctanhf)                        | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**ctanhl**](https://www.bing.com/search?q=ctanhl)                        | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**ctanl**](https://www.bing.com/search?q=ctanl)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**erf**](https://www.bing.com/search?q=erf)                              | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**erfc**](https://www.bing.com/search?q=erfc)                            | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**erfcf**](https://www.bing.com/search?q=erfcf)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**erfcl**](https://www.bing.com/search?q=erfcl)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**erff**](https://www.bing.com/search?q=erff)                            | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**erfl**](https://www.bing.com/search?q=erfl)                            | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**exp**](https://www.bing.com/search?q=exp)                              | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**exp2**](https://www.bing.com/search?q=exp2)                            | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**exp2f**](https://www.bing.com/search?q=exp2f)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**exp2l**](https://www.bing.com/search?q=exp2l)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**expf**](https://www.bing.com/search?q=expf)                            | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**expm1**](https://www.bing.com/search?q=expm1)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**expm1f**](https://www.bing.com/search?q=expm1f)                        | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**expm1l**](https://www.bing.com/search?q=expm1l)                        | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**fabs**](https://www.bing.com/search?q=fabs)                            | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**fdim**](https://www.bing.com/search?q=fdim)                            | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**fdimf**](https://www.bing.com/search?q=fdimf)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**fdiml**](https://www.bing.com/search?q=fdiml)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**floor**](https://www.bing.com/search?q=floor)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**floorf**](https://www.bing.com/search?q=floorf)                        | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**fma**](https://www.bing.com/search?q=fma)                              | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**fmaf**](https://www.bing.com/search?q=fmaf)                            | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**fmal**](https://www.bing.com/search?q=fmal)                            | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**fmax**](https://www.bing.com/search?q=fmax)                            | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**fmaxf**](https://www.bing.com/search?q=fmaxf)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**fmaxl**](https://www.bing.com/search?q=fmaxl)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**fmin**](https://www.bing.com/search?q=fmin)                            | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**fminf**](https://www.bing.com/search?q=fminf)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**fminl**](https://www.bing.com/search?q=fminl)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**fmod**](https://www.bing.com/search?q=fmod)                            | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**fmodf**](https://www.bing.com/search?q=fmodf)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**frexp**](https://www.bing.com/search?q=frexp)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**hypot**](https://www.bing.com/search?q=hypot)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**ilogb**](https://www.bing.com/search?q=ilogb)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**ilogbf**](https://www.bing.com/search?q=ilogbf)                        | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**ilogbl**](https://www.bing.com/search?q=ilogbl)                        | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**ldexp**](https://www.bing.com/search?q=ldexp)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**lgamma**](https://www.bing.com/search?q=lgamma)                        | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**lgammaf**](https://www.bing.com/search?q=lgammaf)                      | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**lgammal**](https://www.bing.com/search?q=lgammal)                      | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**llrint**](https://www.bing.com/search?q=llrint)                        | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**llrintf**](https://www.bing.com/search?q=llrintf)                      | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**llrintl**](https://www.bing.com/search?q=llrintl)                      | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**llround**](https://www.bing.com/search?q=llround)                      | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**llroundf**](https://www.bing.com/search?q=llroundf)                    | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**llroundl**](https://www.bing.com/search?q=llroundl)                    | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**log**](https://www.bing.com/search?q=log)                              | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**log10**](https://www.bing.com/search?q=log10)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**log10f**](https://www.bing.com/search?q=log10f)                        | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**log1p**](https://www.bing.com/search?q=log1p)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**log1pf**](https://www.bing.com/search?q=log1pf)                        | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**log1pl**](https://www.bing.com/search?q=log1pl)                        | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**log2**](https://www.bing.com/search?q=log2)                            | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**log2f**](https://www.bing.com/search?q=log2f)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**log2l**](https://www.bing.com/search?q=log2l)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**logb**](https://www.bing.com/search?q=logb)                            | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**logbf**](https://www.bing.com/search?q=logbf)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**logbl**](https://www.bing.com/search?q=logbl)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**logf**](https://www.bing.com/search?q=logf)                            | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**lrint**](https://www.bing.com/search?q=lrint)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**lrintf**](https://www.bing.com/search?q=lrintf)                        | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**lrintl**](https://www.bing.com/search?q=lrintl)                        | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**lround**](https://www.bing.com/search?q=lround)                        | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**lroundf**](https://www.bing.com/search?q=lroundf)                      | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**lroundl**](https://www.bing.com/search?q=lroundl)                      | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**modf**](https://www.bing.com/search?q=modf)                            | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**modff**](https://www.bing.com/search?q=modff)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**nan**](https://www.bing.com/search?q=nan)                              | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**nanf**](https://www.bing.com/search?q=nanf)                            | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**nanl**](https://www.bing.com/search?q=nanl)                            | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**nearbyint**](https://www.bing.com/search?q=nearbyint)                  | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**nearbyintf**](https://www.bing.com/search?q=nearbyintf)                | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**nearbyintl**](https://www.bing.com/search?q=nearbyintl)                | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**nextafter**](https://www.bing.com/search?q=nextafter)                  | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**nextafterf**](https://www.bing.com/search?q=nextafterf)                | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**nextafterl**](https://www.bing.com/search?q=nextafterl)                | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**nexttoward**](https://www.bing.com/search?q=nexttoward)                | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**nexttowardf**](https://www.bing.com/search?q=nexttowardf)              | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**nexttowardl**](https://www.bing.com/search?q=nexttowardl)              | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**norm**](https://www.bing.com/search?q=norm)                            | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**normf**](https://www.bing.com/search?q=normf)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**norml**](https://www.bing.com/search?q=norml)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**pow**](https://www.bing.com/search?q=pow)                              | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**powf**](https://www.bing.com/search?q=powf)                            | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**remainder**](https://www.bing.com/search?q=remainder)                  | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**remainderf**](https://www.bing.com/search?q=remainderf)                | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**remainderl**](https://www.bing.com/search?q=remainderl)                | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**remquo**](https://www.bing.com/search?q=remquo)                        | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**remquof**](https://www.bing.com/search?q=remquof)                      | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**remquol**](https://www.bing.com/search?q=remquol)                      | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**rint**](https://www.bing.com/search?q=rint)                            | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**rintf**](https://www.bing.com/search?q=rintf)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**rintl**](https://www.bing.com/search?q=rintl)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**round**](https://www.bing.com/search?q=round)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**roundf**](https://www.bing.com/search?q=roundf)                        | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**roundl**](https://www.bing.com/search?q=roundl)                        | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**scalbln**](https://www.bing.com/search?q=scalbln)                      | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**scalblnf**](https://www.bing.com/search?q=scalblnf)                    | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**scalblnl**](https://www.bing.com/search?q=scalblnl)                    | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**scalbn**](https://www.bing.com/search?q=scalbn)                        | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**scalbnf**](https://www.bing.com/search?q=scalbnf)                      | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**scalbnl**](https://www.bing.com/search?q=scalbnl)                      | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**sin**](https://www.bing.com/search?q=sin)                              | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**sinf**](https://www.bing.com/search?q=sinf)                            | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**sinh**](https://www.bing.com/search?q=sinh)                            | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**sinhf**](https://www.bing.com/search?q=sinhf)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**sqrt**](https://www.bing.com/search?q=sqrt)                            | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**sqrtf**](https://www.bing.com/search?q=sqrtf)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**tan**](https://www.bing.com/search?q=tan)                              | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**tanf**](https://www.bing.com/search?q=tanf)                            | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**tanh**](https://www.bing.com/search?q=tanh)                            | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**tanhf**](https://www.bing.com/search?q=tanhf)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**tgamma**](https://www.bing.com/search?q=tgamma)                        | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**tgammaf**](https://www.bing.com/search?q=tgammaf)                      | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**tgammal**](https://www.bing.com/search?q=tgammal)                      | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**trunc**](https://www.bing.com/search?q=trunc)                          | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**truncf**](https://www.bing.com/search?q=truncf)                        | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |
| [**truncl**](https://www.bing.com/search?q=truncl)                        | Introduced into api-ms-win-crt-math-l1-1-0 in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-crt-multibyte-l1-1-0"></span><span id="_API-MS-WIN-CRT-MULTIBYTE-L1-1-0"></span>APIs from the API Set api-ms-win-crt-multibyte-l1-1-0


| API                                                                    | Requirements                                                            |
|------------------------------------------------------------------------|-------------------------------------------------------------------------|
| [**\_\_p\_\_mbcasemap**](https://www.bing.com/search?q=__p__mbcasemap) | Introduced into api-ms-win-crt-multibyte-l1-1-0 in Windows 10.0.10240.0 |
| [**\_\_p\_\_mbctype**](https://www.bing.com/search?q=__p__mbctype)     | Introduced into api-ms-win-crt-multibyte-l1-1-0 in Windows 10.0.10240.0 |
| [**\_ismbbalnum**](https://www.bing.com/search?q=_ismbbalnum)          | Introduced into api-ms-win-crt-multibyte-l1-1-0 in Windows 10.0.10240.0 |
| [**\_ismbbalnum\_l**](https://www.bing.com/search?q=_ismbbalnum_l)     | Introduced into api-ms-win-crt-multibyte-l1-1-0 in Windows 10.0.10240.0 |
| [**\_ismbbalpha**](https://www.bing.com/search?q=_ismbbalpha)          | Introduced into api-ms-win-crt-multibyte-l1-1-0 in Windows 10.0.10240.0 |
| [**\_ismbbalpha\_l**](https://www.bing.com/search?q=_ismbbalpha_l)     | Introduced into api-ms-win-crt-multibyte-l1-1-0 in Windows 10.0.10240.0 |
| [**\_ismbbblank**](https://www.bing.com/search?q=_ismbbblank)          | Introduced into api-ms-win-crt-multibyte-l1-1-0 in Windows 10.0.10240.0 |
| [**\_ismbbblank\_l**](https://www.bing.com/search?q=_ismbbblank_l)     | Introduced into api-ms-win-crt-multibyte-l1-1-0 in Windows 10.0.10240.0 |
| [**\_ismbbgraph**](https://www.bing.com/search?q=_ismbbgraph)          | Introduced into api-ms-win-crt-multibyte-l1-1-0 in Windows 10.0.10240.0 |
| [**\_ismbbgraph\_l**](https://www.bing.com/search?q=_ismbbgraph_l)     | Introduced into api-ms-win-crt-multibyte-l1-1-0 in Windows 10.0.10240.0 |
| [**\_ismbbkalnum**](https://www.bing.com/search?q=_ismbbkalnum)        | Introduced into api-ms-win-crt-multibyte-l1-1-0 in Windows 10.0.10240.0 |
| [**\_ismbbkalnum\_l**](https://www.bing.com/search?q=_ismbbkalnum_l)   | Introduced into api-ms-win-crt-multibyte-l1-1-0 in Windows 10.0.10240.0 |
| [**\_ismbbkana**](https://www.bing.com/search?q=_ismbbkana)            | Introduced into api-ms-win-crt-multibyte-l1-1-0 in Windows 10.0.10240.0 |
| [**\_ismbbkana\_l**](https://www.bing.com/search?q=_ismbbkana_l)       | Introduced into api-ms-win-crt-multibyte-l1-1-0 in Windows 10.0.10240.0 |
| [**\_ismbbkprint**](https://www.bing.com/search?q=_ismbbkprint)        | Introduced into api-ms-win-crt-multibyte-l1-1-0 in Windows 10.0.10240.0 |
| [**\_ismbbkprint\_l**](https://www.bing.com/search?q=_ismbbkprint_l)   | Introduced into api-ms-win-crt-multibyte-l1-1-0 in Windows 10.0.10240.0 |
| [**\_ismbbkpunct**](https://www.bing.com/search?q=_ismbbkpunct)        | Introduced into api-ms-win-crt-multibyte-l1-1-0 in Windows 10.0.10240.0 |
| [**\_ismbbkpunct\_l**](https://www.bing.com/search?q=_ismbbkpunct_l)   | Introduced into api-ms-win-crt-multibyte-l1-1-0 in Windows 10.0.10240.0 |
| [**\_ismbblead**](https://www.bing.com/search?q=_ismbblead)            | Introduced into api-ms-win-crt-multibyte-l1-1-0 in Windows 10.0.10240.0 |
| [**\_ismbblead\_l**](https://www.bing.com/search?q=_ismbblead_l)       | Introduced into api-ms-win-crt-multibyte-l1-1-0 in Windows 10.0.10240.0 |
| [**\_ismbbprint**](https://www.bing.com/search?q=_ismbbprint)          | Introduced into api-ms-win-crt-multibyte-l1-1-0 in Windows 10.0.10240.0 |
| [**\_ismbbprint\_l**](https://www.bing.com/search?q=_ismbbprint_l)     | Introduced into api-ms-win-crt-multibyte-l1-1-0 in Windows 10.0.10240.0 |
| [**\_ismbbpunct**](https://www.bing.com/search?q=_ismbbpunct)          | Introduced into api-ms-win-crt-multibyte-l1-1-0 in Windows 10.0.10240.0 |
| [**\_ismbbpunct\_l**](https://www.bing.com/search?q=_ismbbpunct_l)     | Introduced into api-ms-win-crt-multibyte-l1-1-0 in Windows 10.0.10240.0 |
| [**\_ismbbtrail**](https://www.bing.com/search?q=_ismbbtrail)          | Introduced into api-ms-win-crt-multibyte-l1-1-0 in Windows 10.0.10240.0 |
| [**\_ismbbtrail\_l**](https://www.bing.com/search?q=_ismbbtrail_l)     | Introduced into api-ms-win-crt-multibyte-l1-1-0 in Windows 10.0.10240.0 |
| [**\_ismbslead**](https://www.bing.com/search?q=_ismbslead)            | Introduced into api-ms-win-crt-multibyte-l1-1-0 in Windows 10.0.10240.0 |
| [**\_ismbslead\_l**](https://www.bing.com/search?q=_ismbslead_l)       | Introduced into api-ms-win-crt-multibyte-l1-1-0 in Windows 10.0.10240.0 |
| [**\_ismbstrail**](https://www.bing.com/search?q=_ismbstrail)          | Introduced into api-ms-win-crt-multibyte-l1-1-0 in Windows 10.0.10240.0 |
| [**\_ismbstrail\_l**](https://www.bing.com/search?q=_ismbstrail_l)     | Introduced into api-ms-win-crt-multibyte-l1-1-0 in Windows 10.0.10240.0 |
| [**\_mbcasemap**](https://www.bing.com/search?q=_mbcasemap)            | Introduced into api-ms-win-crt-multibyte-l1-1-0 in Windows 10.0.10240.0 |
| [**\_mblen\_l**](https://www.bing.com/search?q=_mblen_l)               | Introduced into api-ms-win-crt-multibyte-l1-1-0 in Windows 10.0.10240.0 |
| [**\_mbsdup**](https://www.bing.com/search?q=_mbsdup)                  | Introduced into api-ms-win-crt-multibyte-l1-1-0 in Windows 10.0.10240.0 |
| [**\_mbstowcs\_l**](https://www.bing.com/search?q=_mbstowcs_l)         | Introduced into api-ms-win-crt-multibyte-l1-1-0 in Windows 10.0.10240.0 |
| [**\_mbstowcs\_s\_l**](https://www.bing.com/search?q=_mbstowcs_s_l)    | Introduced into api-ms-win-crt-multibyte-l1-1-0 in Windows 10.0.10240.0 |
| [**\_mbstrlen**](https://www.bing.com/search?q=_mbstrlen)              | Introduced into api-ms-win-crt-multibyte-l1-1-0 in Windows 10.0.10240.0 |
| [**\_mbstrlen\_l**](https://www.bing.com/search?q=_mbstrlen_l)         | Introduced into api-ms-win-crt-multibyte-l1-1-0 in Windows 10.0.10240.0 |
| [**\_mbstrnlen**](https://www.bing.com/search?q=_mbstrnlen)            | Introduced into api-ms-win-crt-multibyte-l1-1-0 in Windows 10.0.10240.0 |
| [**\_mbstrnlen\_l**](https://www.bing.com/search?q=_mbstrnlen_l)       | Introduced into api-ms-win-crt-multibyte-l1-1-0 in Windows 10.0.10240.0 |
| [**\_mbtowc\_l**](https://www.bing.com/search?q=_mbtowc_l)             | Introduced into api-ms-win-crt-multibyte-l1-1-0 in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-crt-runtime-l1-1-0"></span><span id="_API-MS-WIN-CRT-RUNTIME-L1-1-0"></span>APIs from the API Set api-ms-win-crt-runtime-l1-1-0


| API                                                                                                                                | Requirements                                                                                                                       |
|------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| [**\_\_doserrno**](https://www.bing.com/search?q=__doserrno)                                                                       | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_\_fpe\_flt\_rounds**](https://www.bing.com/search?q=__fpe_flt_rounds)                                                         | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_\_fpecode**](https://www.bing.com/search?q=__fpecode)                                                                         | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_\_p\_\_\_argc**](https://www.bing.com/search?q=__p___argc)                                                                    | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_\_p\_\_\_argv**](https://www.bing.com/search?q=__p___argv)                                                                    | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_\_p\_\_\_wargv**](https://www.bing.com/search?q=__p___wargv)                                                                  | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_\_p\_\_acmdln**](https://www.bing.com/search?q=__p__acmdln)                                                                   | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_\_p\_\_pgmptr**](https://www.bing.com/search?q=__p__pgmptr)                                                                   | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_\_p\_\_wcmdln**](https://www.bing.com/search?q=__p__wcmdln)                                                                   | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_\_p\_\_wpgmptr**](https://www.bing.com/search?q=__p__wpgmptr)                                                                 | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_\_pxcptinfoptrs**](https://www.bing.com/search?q=__pxcptinfoptrs)                                                             | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_\_sys\_errlist**](https://www.bing.com/search?q=__sys_errlist)                                                                | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_\_sys\_nerr**](https://www.bing.com/search?q=__sys_nerr)                                                                      | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_\_threadhandle**](https://www.bing.com/search?q=__threadhandle)                                                               | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_\_threadid**](https://www.bing.com/search?q=__threadid)                                                                       | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_\_wcserror**](https://www.bing.com/search?q=__wcserror)                                                                       | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_\_wcserror\_s**](https://www.bing.com/search?q=__wcserror_s)                                                                  | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_beginthread**](https://www.bing.com/search?q=_beginthread)                                                                    | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_beginthreadex**](https://www.bing.com/search?q=_beginthreadex)                                                                | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_c\_exit**](https://www.bing.com/search?q=_c_exit)                                                                             | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0. Moved to api-ms-win-core-crt-l2-1-0 in Windows 10.0.14393.0 |
| [**\_clearfp**](https://www.bing.com/search?q=_clearfp)                                                                            | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_configure\_narrow\_argv**](https://www.bing.com/search?q=_configure_narrow_argv)                                              | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_configure\_wide\_argv**](https://www.bing.com/search?q=_configure_wide_argv)                                                  | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_control87**](https://www.bing.com/search?q=_control87)                                                                        | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_controlfp**](https://www.bing.com/search?q=_controlfp)                                                                        | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_controlfp\_s**](https://www.bing.com/search?q=_controlfp_s)                                                                   | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_crt\_at\_quick\_exit**](https://www.bing.com/search?q=_crt_at_quick_exit)                                                     | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_crt\_atexit**](https://www.bing.com/search?q=_crt_atexit)                                                                     | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_endthread**](https://www.bing.com/search?q=_endthread)                                                                        | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_endthreadex**](https://www.bing.com/search?q=_endthreadex)                                                                    | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_errno**](https://www.bing.com/search?q=_errno)                                                                                | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0. Moved to api-ms-win-core-crt-l1-1-0 in Windows 10.0.14393.0 |
| [**\_execute\_onexit\_table**](https://www.bing.com/search?q=_execute_onexit_table)                                                | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_Exit**](https://www.bing.com/search?q=_Exit)                                                                                  | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_exit**](https://www.bing.com/search?q=_exit)                                                                                  | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_fpieee\_flt**](https://www.bing.com/search?q=_fpieee_flt)                                                                     | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_fpreset**](https://www.bing.com/search?q=_fpreset)                                                                            | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_get\_doserrno**](https://www.bing.com/search?q=_get_doserrno)                                                                 | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_get\_errno**](https://www.bing.com/search?q=_get_errno)                                                                       | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_get\_initial\_narrow\_environment**](https://www.bing.com/search?q=_get_initial_narrow_environment)                           | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_get\_initial\_wide\_environment**](https://www.bing.com/search?q=_get_initial_wide_environment)                               | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_get\_invalid\_parameter\_handler**](https://www.bing.com/search?q=_get_invalid_parameter_handler)                             | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_get\_narrow\_winmain\_command\_line**](https://www.bing.com/search?q=_get_narrow_winmain_command_line)                        | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_get\_pgmptr**](https://www.bing.com/search?q=_get_pgmptr)                                                                     | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_get\_terminate**](https://www.bing.com/search?q=_get_terminate)                                                               | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_get\_thread\_local\_invalid\_parameter\_handler**](https://www.bing.com/search?q=_get_thread_local_invalid_parameter_handler) | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_get\_wide\_winmain\_command\_line**](https://www.bing.com/search?q=_get_wide_winmain_command_line)                            | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_get\_wpgmptr**](https://www.bing.com/search?q=_get_wpgmptr)                                                                   | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_getpid**](https://www.bing.com/search?q=_getpid)                                                                              | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_initialize\_narrow\_environment**](https://www.bing.com/search?q=_initialize_narrow_environment)                              | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_initialize\_onexit\_table**](https://www.bing.com/search?q=_initialize_onexit_table)                                          | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_initialize\_wide\_environment**](https://www.bing.com/search?q=_initialize_wide_environment)                                  | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_initterm**](https://www.bing.com/search?q=_initterm)                                                                          | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0. Moved to api-ms-win-core-crt-l2-1-0 in Windows 10.0.10586.0 |
| [**\_query\_app\_type**](https://www.bing.com/search?q=_query_app_type)                                                            | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_register\_onexit\_function**](https://www.bing.com/search?q=_register_onexit_function)                                        | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_register\_thread\_local\_exe\_atexit\_callback**](https://www.bing.com/search?q=_register_thread_local_exe_atexit_callback)   | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_seh\_filter\_dll**](https://www.bing.com/search?q=_seh_filter_dll)                                                            | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_seh\_filter\_exe**](https://www.bing.com/search?q=_seh_filter_exe)                                                            | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_set\_abort\_behavior**](https://www.bing.com/search?q=_set_abort_behavior)                                                    | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_set\_app\_type**](https://www.bing.com/search?q=_set_app_type)                                                                | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_set\_controlfp**](https://www.bing.com/search?q=_set_controlfp)                                                               | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_set\_doserrno**](https://www.bing.com/search?q=_set_doserrno)                                                                 | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_set\_errno**](https://www.bing.com/search?q=_set_errno)                                                                       | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_set\_error\_mode**](https://www.bing.com/search?q=_set_error_mode)                                                            | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_set\_invalid\_parameter\_handler**](https://www.bing.com/search?q=_set_invalid_parameter_handler)                             | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_set\_new\_handler**](https://www.bing.com/search?q=_set_new_handler)                                                          | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_set\_thread\_local\_invalid\_parameter\_handler**](https://www.bing.com/search?q=_set_thread_local_invalid_parameter_handler) | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_sleep**](https://www.bing.com/search?q=_sleep)                                                                                | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_statusfp**](https://www.bing.com/search?q=_statusfp)                                                                          | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_strerror**](https://www.bing.com/search?q=_strerror)                                                                          | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_strerror\_s**](https://www.bing.com/search?q=_strerror_s)                                                                     | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wassert**](https://www.bing.com/search?q=_wassert)                                                                            | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wcserror**](https://www.bing.com/search?q=_wcserror)                                                                          | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wcserror\_s**](https://www.bing.com/search?q=_wcserror_s)                                                                     | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wperror**](https://www.bing.com/search?q=_wperror)                                                                            | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**abort**](https://msdn.microsoft.com/en-us/library/windows/apps/ff728669.aspx)                                                                                                    | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**exit**](https://www.bing.com/search?q=exit)                                                                                     | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**feclearexcept**](https://www.bing.com/search?q=feclearexcept)                                                                   | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**fegetenv**](https://www.bing.com/search?q=fegetenv)                                                                             | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**fegetexceptflag**](https://www.bing.com/search?q=fegetexceptflag)                                                               | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**fegetround**](https://www.bing.com/search?q=fegetround)                                                                         | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**feholdexcept**](https://www.bing.com/search?q=feholdexcept)                                                                     | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**fesetenv**](https://www.bing.com/search?q=fesetenv)                                                                             | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**fesetexceptflag**](https://www.bing.com/search?q=fesetexceptflag)                                                               | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**fesetround**](https://www.bing.com/search?q=fesetround)                                                                         | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**fetestexcept**](https://www.bing.com/search?q=fetestexcept)                                                                     | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**perror**](https://www.bing.com/search?q=perror)                                                                                 | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**quick\_exit**](https://www.bing.com/search?q=quick_exit)                                                                        | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**raise**](https://www.bing.com/search?q=raise)                                                                                   | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**set\_terminate**](https://www.bing.com/search?q=set_terminate)                                                                  | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**signal**](https://www.bing.com/search?q=signal)                                                                                 | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**strerror**](https://www.bing.com/search?q=strerror)                                                                             | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**strerror\_s**](https://www.bing.com/search?q=strerror_s)                                                                        | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**terminate**](https://www.bing.com/search?q=terminate)                                                                           | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_cexit**](https://www.bing.com/search?q=_cexit)                                                                                | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10586.0                                                              |
| [**\_initterm\_e**](https://www.bing.com/search?q=_initterm_e)                                                                     | Introduced into api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.14393.0                                                              |

 

## <span id="_api-ms-win-core-crt-l2-1-0"></span><span id="_API-MS-WIN-CORE-CRT-L2-1-0"></span>APIs from the API Set api-ms-win-core-crt-l2-1-0


| API                                                            | Requirements                                                                                                                       |
|----------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| [**\_cexit**](https://www.bing.com/search?q=_cexit)            | Introduced into api-ms-win-core-crt-l2-1-0 in Windows 10.0.10240.0. Moved to api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.10586.0 |
| [**\_initterm\_e**](https://www.bing.com/search?q=_initterm_e) | Introduced into api-ms-win-core-crt-l2-1-0 in Windows 10.0.10240.0. Moved to api-ms-win-crt-runtime-l1-1-0 in Windows 10.0.14393.0 |
| [**\_time64**](https://www.bing.com/search?q=_time64)          | Introduced into api-ms-win-core-crt-l2-1-0 in Windows 10.0.10240.0. Moved to api-ms-win-crt-time-l1-1-0 in Windows 10.0.10586.0    |
| [**\_initterm**](https://www.bing.com/search?q=_initterm)      | Introduced into api-ms-win-core-crt-l2-1-0 in Windows 10.0.10586.0                                                                 |
| [**\_c\_exit**](https://www.bing.com/search?q=_c_exit)         | Introduced into api-ms-win-core-crt-l2-1-0 in Windows 10.0.14393.0                                                                 |

 

## <span id="_api-ms-win-crt-string-l1-1-0"></span><span id="_API-MS-WIN-CRT-STRING-L1-1-0"></span>APIs from the API Set api-ms-win-crt-string-l1-1-0


| API                                                                | Requirements                                                                                                                      |
|--------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| [**\_\_isascii**](https://www.bing.com/search?q=__isascii)         | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0. Moved to api-ms-win-core-crt-l1-1-0 in Windows 10.0.10586.0 |
| [**\_\_iscsym**](https://www.bing.com/search?q=__iscsym)           | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_\_iscsymf**](https://www.bing.com/search?q=__iscsymf)         | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_\_iswcsym**](https://www.bing.com/search?q=__iswcsym)         | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_\_iswcsymf**](https://www.bing.com/search?q=__iswcsymf)       | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_\_strncnt**](https://www.bing.com/search?q=__strncnt)         | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_\_wcsncnt**](https://www.bing.com/search?q=__wcsncnt)         | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_isalnum\_l**](https://www.bing.com/search?q=_isalnum_l)       | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_isalpha\_l**](https://www.bing.com/search?q=_isalpha_l)       | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_isblank\_l**](https://www.bing.com/search?q=_isblank_l)       | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_iscntrl\_l**](https://www.bing.com/search?q=_iscntrl_l)       | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_isctype**](https://www.bing.com/search?q=_isctype)            | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_isctype\_l**](https://www.bing.com/search?q=_isctype_l)       | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_isdigit\_l**](https://www.bing.com/search?q=_isdigit_l)       | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_isgraph\_l**](https://www.bing.com/search?q=_isgraph_l)       | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_isleadbyte\_l**](https://www.bing.com/search?q=_isleadbyte_l) | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_islower\_l**](https://www.bing.com/search?q=_islower_l)       | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_isprint\_l**](https://www.bing.com/search?q=_isprint_l)       | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_ispunct\_l**](https://www.bing.com/search?q=_ispunct_l)       | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_isspace\_l**](https://www.bing.com/search?q=_isspace_l)       | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_isupper\_l**](https://www.bing.com/search?q=_isupper_l)       | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_iswalnum\_l**](https://www.bing.com/search?q=_iswalnum_l)     | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_iswalpha\_l**](https://www.bing.com/search?q=_iswalpha_l)     | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_iswblank\_l**](https://www.bing.com/search?q=_iswblank_l)     | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_iswcntrl\_l**](https://www.bing.com/search?q=_iswcntrl_l)     | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_iswcsym\_l**](https://www.bing.com/search?q=_iswcsym_l)       | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_iswcsymf\_l**](https://www.bing.com/search?q=_iswcsymf_l)     | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_iswctype\_l**](https://www.bing.com/search?q=_iswctype_l)     | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_iswdigit\_l**](https://www.bing.com/search?q=_iswdigit_l)     | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_iswgraph\_l**](https://www.bing.com/search?q=_iswgraph_l)     | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_iswlower\_l**](https://www.bing.com/search?q=_iswlower_l)     | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_iswprint\_l**](https://www.bing.com/search?q=_iswprint_l)     | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_iswpunct\_l**](https://www.bing.com/search?q=_iswpunct_l)     | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_iswspace\_l**](https://www.bing.com/search?q=_iswspace_l)     | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_iswupper\_l**](https://www.bing.com/search?q=_iswupper_l)     | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_iswxdigit\_l**](https://www.bing.com/search?q=_iswxdigit_l)   | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_isxdigit\_l**](https://www.bing.com/search?q=_isxdigit_l)     | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_memccpy**](https://www.bing.com/search?q=_memccpy)            | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_memicmp**](https://www.bing.com/search?q=_memicmp)            | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_memicmp\_l**](https://www.bing.com/search?q=_memicmp_l)       | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_strcoll\_l**](https://www.bing.com/search?q=_strcoll_l)       | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_strdup**](https://www.bing.com/search?q=_strdup)              | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_stricmp**](https://www.bing.com/search?q=_stricmp)            | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0. Moved to api-ms-win-core-crt-l1-1-0 in Windows 10.0.10586.0 |
| [**\_stricmp\_l**](https://www.bing.com/search?q=_stricmp_l)       | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_stricoll**](https://www.bing.com/search?q=_stricoll)          | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_stricoll\_l**](https://www.bing.com/search?q=_stricoll_l)     | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_strlwr**](https://www.bing.com/search?q=_strlwr)              | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_strlwr\_l**](https://www.bing.com/search?q=_strlwr_l)         | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_strlwr\_s\_l**](https://www.bing.com/search?q=_strlwr_s_l)    | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_strncoll**](https://www.bing.com/search?q=_strncoll)          | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_strncoll\_l**](https://www.bing.com/search?q=_strncoll_l)     | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_strnicmp**](https://www.bing.com/search?q=_strnicmp)          | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0. Moved to api-ms-win-core-crt-l1-1-0 in Windows 10.0.10586.0 |
| [**\_strnicmp\_l**](https://www.bing.com/search?q=_strnicmp_l)     | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_strnicoll**](https://www.bing.com/search?q=_strnicoll)        | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_strnicoll\_l**](https://www.bing.com/search?q=_strnicoll_l)   | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_strnset**](https://www.bing.com/search?q=_strnset)            | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_strnset\_s**](https://www.bing.com/search?q=_strnset_s)       | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_strrev**](https://www.bing.com/search?q=_strrev)              | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_strset**](https://www.bing.com/search?q=_strset)              | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_strset\_s**](https://www.bing.com/search?q=_strset_s)         | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_strupr**](https://www.bing.com/search?q=_strupr)              | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_strupr\_l**](https://www.bing.com/search?q=_strupr_l)         | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_strupr\_s\_l**](https://www.bing.com/search?q=_strupr_s_l)    | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_strxfrm\_l**](https://www.bing.com/search?q=_strxfrm_l)       | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_tolower**](https://www.bing.com/search?q=_tolower)            | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_tolower\_l**](https://www.bing.com/search?q=_tolower_l)       | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_toupper**](https://www.bing.com/search?q=_toupper)            | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_toupper\_l**](https://www.bing.com/search?q=_toupper_l)       | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_towlower\_l**](https://www.bing.com/search?q=_towlower_l)     | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_towupper\_l**](https://www.bing.com/search?q=_towupper_l)     | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wcscoll\_l**](https://www.bing.com/search?q=_wcscoll_l)       | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wcsdup**](https://www.bing.com/search?q=_wcsdup)              | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wcsicmp**](https://www.bing.com/search?q=_wcsicmp)            | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0. Moved to api-ms-win-core-crt-l1-1-0 in Windows 10.0.14393.0 |
| [**\_wcsicmp\_l**](https://www.bing.com/search?q=_wcsicmp_l)       | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wcsicoll**](https://www.bing.com/search?q=_wcsicoll)          | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wcsicoll\_l**](https://www.bing.com/search?q=_wcsicoll_l)     | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wcslwr**](https://www.bing.com/search?q=_wcslwr)              | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wcslwr\_l**](https://www.bing.com/search?q=_wcslwr_l)         | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wcslwr\_s\_l**](https://www.bing.com/search?q=_wcslwr_s_l)    | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wcsncoll**](https://www.bing.com/search?q=_wcsncoll)          | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wcsncoll\_l**](https://www.bing.com/search?q=_wcsncoll_l)     | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wcsnicmp\_l**](https://www.bing.com/search?q=_wcsnicmp_l)     | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wcsnicoll**](https://www.bing.com/search?q=_wcsnicoll)        | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wcsnicoll\_l**](https://www.bing.com/search?q=_wcsnicoll_l)   | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wcsnset**](https://www.bing.com/search?q=_wcsnset)            | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wcsnset\_s**](https://www.bing.com/search?q=_wcsnset_s)       | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wcsrev**](https://www.bing.com/search?q=_wcsrev)              | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wcsset**](https://www.bing.com/search?q=_wcsset)              | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wcsset\_s**](https://www.bing.com/search?q=_wcsset_s)         | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wcsupr**](https://www.bing.com/search?q=_wcsupr)              | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wcsupr\_l**](https://www.bing.com/search?q=_wcsupr_l)         | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wcsupr\_s\_l**](https://www.bing.com/search?q=_wcsupr_s_l)    | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wcsxfrm\_l**](https://www.bing.com/search?q=_wcsxfrm_l)       | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**isalnum**](https://www.bing.com/search?q=isalnum)               | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0. Moved to api-ms-win-core-crt-l1-1-0 in Windows 10.0.10586.0 |
| [**isalpha**](https://www.bing.com/search?q=isalpha)               | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**isblank**](https://www.bing.com/search?q=isblank)               | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**iscntrl**](https://www.bing.com/search?q=iscntrl)               | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**isleadbyte**](https://www.bing.com/search?q=isleadbyte)         | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**ispunct**](https://www.bing.com/search?q=ispunct)               | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**isspace**](https://www.bing.com/search?q=isspace)               | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0. Moved to api-ms-win-core-crt-l1-1-0 in Windows 10.0.10586.0 |
| [**isupper**](https://www.bing.com/search?q=isupper)               | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0. Moved to api-ms-win-core-crt-l1-1-0 in Windows 10.0.10586.0 |
| [**iswalpha**](https://www.bing.com/search?q=iswalpha)             | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**iswblank**](https://www.bing.com/search?q=iswblank)             | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**iswcntrl**](https://www.bing.com/search?q=iswcntrl)             | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**iswdigit**](https://www.bing.com/search?q=iswdigit)             | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0. Moved to api-ms-win-core-crt-l1-1-0 in Windows 10.0.10586.0 |
| [**iswgraph**](https://www.bing.com/search?q=iswgraph)             | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**iswlower**](https://www.bing.com/search?q=iswlower)             | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**iswpunct**](https://www.bing.com/search?q=iswpunct)             | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**iswspace**](https://www.bing.com/search?q=iswspace)             | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0. Moved to api-ms-win-core-crt-l1-1-0 in Windows 10.0.10586.0 |
| [**iswupper**](https://www.bing.com/search?q=iswupper)             | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**iswxdigit**](https://www.bing.com/search?q=iswxdigit)           | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**isxdigit**](https://www.bing.com/search?q=isxdigit)             | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**mblen**](https://www.bing.com/search?q=mblen)                   | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**mbrlen**](https://www.bing.com/search?q=mbrlen)                 | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**strcat**](https://msdn.microsoft.com/en-us/library/windows/apps/bb759925.aspx)                                         | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**strcat\_s**](https://www.bing.com/search?q=strcat_s)            | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**strcoll**](https://www.bing.com/search?q=strcoll)               | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**strcpy**](https://msdn.microsoft.com/en-us/library/windows/apps/bb759960.aspx)                                         | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**strcspn**](https://msdn.microsoft.com/en-us/library/windows/apps/bb759964.aspx)                                       | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**strlen**](https://www.bing.com/search?q=strlen)                 | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**strncat**](https://msdn.microsoft.com/en-us/library/windows/apps/bb759987.aspx)                                       | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**strncat\_s**](https://www.bing.com/search?q=strncat_s)          | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0. Moved to api-ms-win-core-crt-l1-1-0 in Windows 10.0.10586.0 |
| [**strncmp**](https://www.bing.com/search?q=strncmp)               | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**strncpy**](https://www.bing.com/search?q=strncpy)               | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**strnlen**](https://www.bing.com/search?q=strnlen)               | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**strspn**](https://msdn.microsoft.com/en-us/library/windows/apps/bb773435.aspx)                                         | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**strtok**](https://www.bing.com/search?q=strtok)                 | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**strtok\_s**](https://www.bing.com/search?q=strtok_s)            | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0. Moved to api-ms-win-core-crt-l1-1-0 in Windows 10.0.10586.0 |
| [**strxfrm**](https://www.bing.com/search?q=strxfrm)               | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**toupper**](https://www.bing.com/search?q=toupper)               | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0. Moved to api-ms-win-core-crt-l1-1-0 in Windows 10.0.14393.0 |
| [**towctrans**](https://www.bing.com/search?q=towctrans)           | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**wcscat**](https://www.bing.com/search?q=wcscat)                 | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**wcscoll**](https://www.bing.com/search?q=wcscoll)               | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**wcscpy**](https://www.bing.com/search?q=wcscpy)                 | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**wcscpy\_s**](https://www.bing.com/search?q=wcscpy_s)            | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0. Moved to api-ms-win-core-crt-l1-1-0 in Windows 10.0.10586.0 |
| [**wcscspn**](https://www.bing.com/search?q=wcscspn)               | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0. Moved to api-ms-win-core-crt-l1-1-0 in Windows 10.0.10586.0 |
| [**wcsncat**](https://www.bing.com/search?q=wcsncat)               | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**wcsncpy**](https://www.bing.com/search?q=wcsncpy)               | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**wcsspn**](https://www.bing.com/search?q=wcsspn)                 | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**wcstok**](https://www.bing.com/search?q=wcstok)                 | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**wcstok\_s**](https://www.bing.com/search?q=wcstok_s)            | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**wcsxfrm**](https://www.bing.com/search?q=wcsxfrm)               | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**wctype**](https://www.bing.com/search?q=wctype)                 | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**wmemcpy\_s**](https://www.bing.com/search?q=wmemcpy_s)          | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**wmemmove\_s**](https://www.bing.com/search?q=wmemmove_s)        | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_strlwr\_s**](https://www.bing.com/search?q=_strlwr_s)         | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10586.0                                                              |
| [**\_wcsnicmp**](https://www.bing.com/search?q=_wcsnicmp)          | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10586.0                                                              |
| [**\_wcsupr\_s**](https://www.bing.com/search?q=_wcsupr_s)         | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10586.0. Moved to api-ms-win-core-crt-l1-1-0 in Windows 10.0.14393.0 |
| [**isdigit**](https://www.bing.com/search?q=isdigit)               | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10586.0                                                              |
| [**isprint**](https://www.bing.com/search?q=isprint)               | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10586.0                                                              |
| [**iswalnum**](https://www.bing.com/search?q=iswalnum)             | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10586.0                                                              |
| [**iswctype**](https://www.bing.com/search?q=iswctype)             | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10586.0. Moved to api-ms-win-core-crt-l1-1-0 in Windows 10.0.14393.0 |
| [**iswprint**](https://www.bing.com/search?q=iswprint)             | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10586.0                                                              |
| [**memcpy\_s**](https://www.bing.com/search?q=memcpy_s)            | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10586.0. Moved to api-ms-win-core-crt-l1-1-0 in Windows 10.0.14393.0 |
| [**strncpy\_s**](https://www.bing.com/search?q=strncpy_s)          | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10586.0                                                              |
| [**strpbrk**](https://msdn.microsoft.com/en-us/library/windows/apps/bb760010.aspx)                                       | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10586.0                                                              |
| [**towlower**](https://www.bing.com/search?q=towlower)             | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10586.0                                                              |
| [**towupper**](https://www.bing.com/search?q=towupper)             | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10586.0. Moved to api-ms-win-core-crt-l1-1-0 in Windows 10.0.14393.0 |
| [**wcscmp**](https://www.bing.com/search?q=wcscmp)                 | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10586.0                                                              |
| [**wcslen**](https://www.bing.com/search?q=wcslen)                 | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10586.0                                                              |
| [**wcsncmp**](https://www.bing.com/search?q=wcsncmp)               | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10586.0. Moved to api-ms-win-core-crt-l1-1-0 in Windows 10.0.14393.0 |
| [**wcsncpy\_s**](https://www.bing.com/search?q=wcsncpy_s)          | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.10586.0. Moved to api-ms-win-core-crt-l1-1-0 in Windows 10.0.14393.0 |
| [**\_strupr\_s**](https://www.bing.com/search?q=_strupr_s)         | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.14393.0                                                              |
| [**isgraph**](https://www.bing.com/search?q=isgraph)               | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.14393.0                                                              |
| [**islower**](https://www.bing.com/search?q=islower)               | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.14393.0                                                              |
| [**strcpy\_s**](https://www.bing.com/search?q=strcpy_s)            | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.14393.0                                                              |
| [**tolower**](https://www.bing.com/search?q=tolower)               | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.14393.0                                                              |
| [**wcspbrk**](https://www.bing.com/search?q=wcspbrk)               | Introduced into api-ms-win-crt-string-l1-1-0 in Windows 10.0.14393.0                                                              |

 

## <span id="_api-ms-win-crt-time-l1-1-0"></span><span id="_API-MS-WIN-CRT-TIME-L1-1-0"></span>APIs from the API Set api-ms-win-crt-time-l1-1-0


| API                                                                    | Requirements                                                                                                                    |
|------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| [**\_\_daylight**](https://www.bing.com/search?q=__daylight)           | Introduced into api-ms-win-crt-time-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_\_dstbias**](https://www.bing.com/search?q=__dstbias)             | Introduced into api-ms-win-crt-time-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_\_timezone**](https://www.bing.com/search?q=__timezone)           | Introduced into api-ms-win-crt-time-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_\_tzname**](https://www.bing.com/search?q=__tzname)               | Introduced into api-ms-win-crt-time-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_ctime32**](https://www.bing.com/search?q=_ctime32)                | Introduced into api-ms-win-crt-time-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_ctime32\_s**](https://www.bing.com/search?q=_ctime32_s)           | Introduced into api-ms-win-crt-time-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_ctime64**](https://www.bing.com/search?q=_ctime64)                | Introduced into api-ms-win-crt-time-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_ctime64\_s**](https://www.bing.com/search?q=_ctime64_s)           | Introduced into api-ms-win-crt-time-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_difftime32**](https://www.bing.com/search?q=_difftime32)          | Introduced into api-ms-win-crt-time-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_difftime64**](https://www.bing.com/search?q=_difftime64)          | Introduced into api-ms-win-crt-time-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_ftime32**](https://www.bing.com/search?q=_ftime32)                | Introduced into api-ms-win-crt-time-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_ftime32\_s**](https://www.bing.com/search?q=_ftime32_s)           | Introduced into api-ms-win-crt-time-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_ftime64**](https://www.bing.com/search?q=_ftime64)                | Introduced into api-ms-win-crt-time-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_ftime64\_s**](https://www.bing.com/search?q=_ftime64_s)           | Introduced into api-ms-win-crt-time-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_futime32**](https://www.bing.com/search?q=_futime32)              | Introduced into api-ms-win-crt-time-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_futime64**](https://www.bing.com/search?q=_futime64)              | Introduced into api-ms-win-crt-time-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_get\_daylight**](https://www.bing.com/search?q=_get_daylight)     | Introduced into api-ms-win-crt-time-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_get\_dstbias**](https://www.bing.com/search?q=_get_dstbias)       | Introduced into api-ms-win-crt-time-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_get\_timezone**](https://www.bing.com/search?q=_get_timezone)     | Introduced into api-ms-win-crt-time-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_get\_tzname**](https://www.bing.com/search?q=_get_tzname)         | Introduced into api-ms-win-crt-time-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_gmtime32**](https://www.bing.com/search?q=_gmtime32)              | Introduced into api-ms-win-crt-time-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_gmtime32\_s**](https://www.bing.com/search?q=_gmtime32_s)         | Introduced into api-ms-win-crt-time-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_gmtime64**](https://www.bing.com/search?q=_gmtime64)              | Introduced into api-ms-win-crt-time-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_gmtime64\_s**](https://www.bing.com/search?q=_gmtime64_s)         | Introduced into api-ms-win-crt-time-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_localtime32**](https://www.bing.com/search?q=_localtime32)        | Introduced into api-ms-win-crt-time-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_localtime32\_s**](https://www.bing.com/search?q=_localtime32_s)   | Introduced into api-ms-win-crt-time-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_localtime64**](https://www.bing.com/search?q=_localtime64)        | Introduced into api-ms-win-crt-time-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_localtime64\_s**](https://www.bing.com/search?q=_localtime64_s)   | Introduced into api-ms-win-crt-time-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_mkgmtime32**](https://www.bing.com/search?q=_mkgmtime32)          | Introduced into api-ms-win-crt-time-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_mkgmtime64**](https://www.bing.com/search?q=_mkgmtime64)          | Introduced into api-ms-win-crt-time-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_mktime32**](https://www.bing.com/search?q=_mktime32)              | Introduced into api-ms-win-crt-time-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_mktime64**](https://www.bing.com/search?q=_mktime64)              | Introduced into api-ms-win-crt-time-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_strdate**](https://www.bing.com/search?q=_strdate)                | Introduced into api-ms-win-crt-time-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_strdate\_s**](https://www.bing.com/search?q=_strdate_s)           | Introduced into api-ms-win-crt-time-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_strftime\_l**](https://www.bing.com/search?q=_strftime_l)         | Introduced into api-ms-win-crt-time-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_strtime**](https://www.bing.com/search?q=_strtime)                | Introduced into api-ms-win-crt-time-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_strtime\_s**](https://www.bing.com/search?q=_strtime_s)           | Introduced into api-ms-win-crt-time-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_time32**](https://www.bing.com/search?q=_time32)                  | Introduced into api-ms-win-crt-time-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_timespec32\_get**](https://www.bing.com/search?q=_timespec32_get) | Introduced into api-ms-win-crt-time-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_timespec64\_get**](https://www.bing.com/search?q=_timespec64_get) | Introduced into api-ms-win-crt-time-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_tzset**](https://www.bing.com/search?q=_tzset)                    | Introduced into api-ms-win-crt-time-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_utime32**](https://www.bing.com/search?q=_utime32)                | Introduced into api-ms-win-crt-time-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_utime64**](https://www.bing.com/search?q=_utime64)                | Introduced into api-ms-win-crt-time-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wasctime**](https://www.bing.com/search?q=_wasctime)              | Introduced into api-ms-win-crt-time-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wasctime\_s**](https://www.bing.com/search?q=_wasctime_s)         | Introduced into api-ms-win-crt-time-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wcsftime\_l**](https://www.bing.com/search?q=_wcsftime_l)         | Introduced into api-ms-win-crt-time-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wctime32**](https://www.bing.com/search?q=_wctime32)              | Introduced into api-ms-win-crt-time-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wctime32\_s**](https://www.bing.com/search?q=_wctime32_s)         | Introduced into api-ms-win-crt-time-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wctime64**](https://www.bing.com/search?q=_wctime64)              | Introduced into api-ms-win-crt-time-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wctime64\_s**](https://www.bing.com/search?q=_wctime64_s)         | Introduced into api-ms-win-crt-time-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wstrdate**](https://www.bing.com/search?q=_wstrdate)              | Introduced into api-ms-win-crt-time-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wstrdate\_s**](https://www.bing.com/search?q=_wstrdate_s)         | Introduced into api-ms-win-crt-time-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wstrtime**](https://www.bing.com/search?q=_wstrtime)              | Introduced into api-ms-win-crt-time-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wstrtime\_s**](https://www.bing.com/search?q=_wstrtime_s)         | Introduced into api-ms-win-crt-time-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wutime32**](https://www.bing.com/search?q=_wutime32)              | Introduced into api-ms-win-crt-time-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_wutime64**](https://www.bing.com/search?q=_wutime64)              | Introduced into api-ms-win-crt-time-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**asctime**](https://www.bing.com/search?q=asctime)                   | Introduced into api-ms-win-crt-time-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**asctime\_s**](https://www.bing.com/search?q=asctime_s)              | Introduced into api-ms-win-crt-time-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**clock**](https://www.bing.com/search?q=clock)                       | Introduced into api-ms-win-crt-time-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**strftime**](https://www.bing.com/search?q=strftime)                 | Introduced into api-ms-win-crt-time-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**wcsftime**](https://www.bing.com/search?q=wcsftime)                 | Introduced into api-ms-win-crt-time-l1-1-0 in Windows 10.0.10240.0                                                              |
| [**\_time64**](https://www.bing.com/search?q=_time64)                  | Introduced into api-ms-win-crt-time-l1-1-0 in Windows 10.0.10586.0. Moved to api-ms-win-core-crt-l2-1-0 in Windows 10.0.14393.0 |

 

## <span id="_api-ms-win-crt-utility-l1-1-0"></span><span id="_API-MS-WIN-CRT-UTILITY-L1-1-0"></span>APIs from the API Set api-ms-win-crt-utility-l1-1-0


| API                                                                      | Requirements                                                          |
|--------------------------------------------------------------------------|-----------------------------------------------------------------------|
| [**\_abs64**](https://www.bing.com/search?q=_abs64)                      | Introduced into api-ms-win-crt-utility-l1-1-0 in Windows 10.0.10240.0 |
| [**\_byteswap\_uint64**](https://www.bing.com/search?q=_byteswap_uint64) | Introduced into api-ms-win-crt-utility-l1-1-0 in Windows 10.0.10240.0 |
| [**\_byteswap\_ulong**](https://www.bing.com/search?q=_byteswap_ulong)   | Introduced into api-ms-win-crt-utility-l1-1-0 in Windows 10.0.10240.0 |
| [**\_byteswap\_ushort**](https://www.bing.com/search?q=_byteswap_ushort) | Introduced into api-ms-win-crt-utility-l1-1-0 in Windows 10.0.10240.0 |
| [**\_lfind**](https://www.bing.com/search?q=_lfind)                      | Introduced into api-ms-win-crt-utility-l1-1-0 in Windows 10.0.10240.0 |
| [**\_lfind\_s**](https://www.bing.com/search?q=_lfind_s)                 | Introduced into api-ms-win-crt-utility-l1-1-0 in Windows 10.0.10240.0 |
| [**\_lrotl**](https://www.bing.com/search?q=_lrotl)                      | Introduced into api-ms-win-crt-utility-l1-1-0 in Windows 10.0.10240.0 |
| [**\_lrotr**](https://www.bing.com/search?q=_lrotr)                      | Introduced into api-ms-win-crt-utility-l1-1-0 in Windows 10.0.10240.0 |
| [**\_lsearch**](https://www.bing.com/search?q=_lsearch)                  | Introduced into api-ms-win-crt-utility-l1-1-0 in Windows 10.0.10240.0 |
| [**\_lsearch\_s**](https://www.bing.com/search?q=_lsearch_s)             | Introduced into api-ms-win-crt-utility-l1-1-0 in Windows 10.0.10240.0 |
| [**\_rotl**](https://www.bing.com/search?q=_rotl)                        | Introduced into api-ms-win-crt-utility-l1-1-0 in Windows 10.0.10240.0 |
| [**\_rotl64**](https://www.bing.com/search?q=_rotl64)                    | Introduced into api-ms-win-crt-utility-l1-1-0 in Windows 10.0.10240.0 |
| [**\_rotr**](https://www.bing.com/search?q=_rotr)                        | Introduced into api-ms-win-crt-utility-l1-1-0 in Windows 10.0.10240.0 |
| [**\_rotr64**](https://www.bing.com/search?q=_rotr64)                    | Introduced into api-ms-win-crt-utility-l1-1-0 in Windows 10.0.10240.0 |
| [**\_swab**](https://www.bing.com/search?q=_swab)                        | Introduced into api-ms-win-crt-utility-l1-1-0 in Windows 10.0.10240.0 |
| [**abs**](https://www.bing.com/search?q=abs)                             | Introduced into api-ms-win-crt-utility-l1-1-0 in Windows 10.0.10240.0 |
| [**bsearch**](https://www.bing.com/search?q=bsearch)                     | Introduced into api-ms-win-crt-utility-l1-1-0 in Windows 10.0.10240.0 |
| [**bsearch\_s**](https://www.bing.com/search?q=bsearch_s)                | Introduced into api-ms-win-crt-utility-l1-1-0 in Windows 10.0.10240.0 |
| [**div**](https://www.bing.com/search?q=div)                             | Introduced into api-ms-win-crt-utility-l1-1-0 in Windows 10.0.10240.0 |
| [**imaxabs**](https://www.bing.com/search?q=imaxabs)                     | Introduced into api-ms-win-crt-utility-l1-1-0 in Windows 10.0.10240.0 |
| [**imaxdiv**](https://www.bing.com/search?q=imaxdiv)                     | Introduced into api-ms-win-crt-utility-l1-1-0 in Windows 10.0.10240.0 |
| [**labs**](https://www.bing.com/search?q=labs)                           | Introduced into api-ms-win-crt-utility-l1-1-0 in Windows 10.0.10240.0 |
| [**ldiv**](https://www.bing.com/search?q=ldiv)                           | Introduced into api-ms-win-crt-utility-l1-1-0 in Windows 10.0.10240.0 |
| [**llabs**](https://www.bing.com/search?q=llabs)                         | Introduced into api-ms-win-crt-utility-l1-1-0 in Windows 10.0.10240.0 |
| [**lldiv**](https://www.bing.com/search?q=lldiv)                         | Introduced into api-ms-win-crt-utility-l1-1-0 in Windows 10.0.10240.0 |
| [**qsort**](https://www.bing.com/search?q=qsort)                         | Introduced into api-ms-win-crt-utility-l1-1-0 in Windows 10.0.10240.0 |
| [**rand**](https://www.bing.com/search?q=rand)                           | Introduced into api-ms-win-crt-utility-l1-1-0 in Windows 10.0.10240.0 |
| [**rand\_s**](https://www.bing.com/search?q=rand_s)                      | Introduced into api-ms-win-crt-utility-l1-1-0 in Windows 10.0.10240.0 |
| [**srand**](https://www.bing.com/search?q=srand)                         | Introduced into api-ms-win-crt-utility-l1-1-0 in Windows 10.0.10240.0 |
| [**qsort\_s**](https://www.bing.com/search?q=qsort_s)                    | Introduced into api-ms-win-crt-utility-l1-1-0 in Windows 10.0.10586.0 |

 

## <span id="_api-ms-win-gaming-tcui-l1-1-1"></span><span id="_API-MS-WIN-GAMING-TCUI-L1-1-1"></span>APIs from the API Set api-ms-win-gaming-tcui-l1-1-1


| API                                                                                            | Requirements                                                          |
|------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| [**CheckGamingPrivilegeSilently**](https://www.bing.com/search?q=CheckGamingPrivilegeSilently) | Introduced into api-ms-win-gaming-tcui-l1-1-1 in Windows 10.0.10586.0 |
| [**CheckGamingPrivilegeWithUI**](https://www.bing.com/search?q=CheckGamingPrivilegeWithUI)     | Introduced into api-ms-win-gaming-tcui-l1-1-1 in Windows 10.0.10586.0 |

 

## <span id="_ext-ms-win-security-srp-l1-1-0"></span><span id="_EXT-MS-WIN-SECURITY-SRP-L1-1-0"></span>APIs from the API Set ext-ms-win-security-srp-l1-1-0


| API                                                                                                | Requirements                                                           |
|----------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| [**SrpDoesPolicyAllowAppExecution**](https://www.bing.com/search?q=SrpDoesPolicyAllowAppExecution) | Introduced into ext-ms-win-security-srp-l1-1-0 in Windows 10.0.10586.0 |

 

## <span id="_api-ms-win-ole32-ie-l1-1-0"></span><span id="_API-MS-WIN-OLE32-IE-L1-1-0"></span>APIs from the API Set api-ms-win-ole32-ie-l1-1-0


| API                                    | Requirements                                                       |
|----------------------------------------|--------------------------------------------------------------------|
| [**CreateBindCtx**](https://msdn.microsoft.com/en-us/library/windows/apps/ms678542.aspx) | Introduced into api-ms-win-ole32-ie-l1-1-0 in Windows 10.0.14393.0 |

 

## <span id="_ext-ms-win-com-ole32-l1-1-4"></span><span id="_EXT-MS-WIN-COM-OLE32-L1-1-4"></span>APIs from the API Set ext-ms-win-com-ole32-l1-1-4


| API                                            | Requirements                                                        |
|------------------------------------------------|---------------------------------------------------------------------|
| [**CreateFileMoniker**](https://msdn.microsoft.com/en-us/library/ms693465.aspx) | Introduced into ext-ms-win-com-ole32-l1-1-4 in Windows 10.0.14393.0 |

 

## <span id="_ext-ms-win-ntuser-window-l1-1-0"></span><span id="_EXT-MS-WIN-NTUSER-WINDOW-L1-1-0"></span>APIs from the API Set ext-ms-win-ntuser-window-l1-1-0


| API                                   | Requirements                                                            |
|---------------------------------------|-------------------------------------------------------------------------|
| [**SoundSentry**](https://msdn.microsoft.com/en-us/library/aa969269.aspx) | Introduced into ext-ms-win-ntuser-window-l1-1-0 in Windows 10.0.14393.0 |

 

## <span id="_ext-ms-win-ntuser-keyboard-l1-2-0"></span><span id="_EXT-MS-WIN-NTUSER-KEYBOARD-L1-2-0"></span>APIs from the API Set ext-ms-win-ntuser-keyboard-l1-2-0


| API                                            | Requirements                                                              |
|------------------------------------------------|---------------------------------------------------------------------------|
| [**GetKeyNameTextW**](https://msdn.microsoft.com/en-us/library/ms646300.aspx) | Introduced into ext-ms-win-ntuser-keyboard-l1-2-0 in Windows 10.0.14393.0 |

 

## <span id="_ext-ms-win-ntuser-keyboard-l1-3-0"></span><span id="_EXT-MS-WIN-NTUSER-KEYBOARD-L1-3-0"></span>APIs from the API Set ext-ms-win-ntuser-keyboard-l1-3-0


| API                                          | Requirements                                                              |
|----------------------------------------------|---------------------------------------------------------------------------|
| [**MapVirtualKeyA**](https://msdn.microsoft.com/en-us/library/ms646306.aspx) | Introduced into ext-ms-win-ntuser-keyboard-l1-3-0 in Windows 10.0.14393.0 |

 

## <span id="_ext-ms-win-ntuser-keyboard-l1-1-0"></span><span id="_EXT-MS-WIN-NTUSER-KEYBOARD-L1-1-0"></span>APIs from the API Set ext-ms-win-ntuser-keyboard-l1-1-0


| API                                              | Requirements                                                              |
|--------------------------------------------------|---------------------------------------------------------------------------|
| [**MapVirtualKeyW**](https://msdn.microsoft.com/en-us/library/ms646306.aspx)     | Introduced into ext-ms-win-ntuser-keyboard-l1-1-0 in Windows 10.0.14393.0 |
| [**MapVirtualKeyExW**](https://msdn.microsoft.com/en-us/library/ms646307.aspx) | Introduced into ext-ms-win-ntuser-keyboard-l1-1-0 in Windows 10.0.14393.0 |

 

## <span id="_PHONEAUDIOSES.DLL"></span>APIs from the dll PhoneAudioSes.dll


| API                                                                                    | Requirements                                              |
|----------------------------------------------------------------------------------------|-----------------------------------------------------------|
| [**ActivateAudioInterface**](https://www.bing.com/search?q=ActivateAudioInterface)     | Introduced into PhoneAudioSes.dll in Windows 10.0.10240.0 |
| [**GetDefaultAudioCaptureId**](https://www.bing.com/search?q=GetDefaultAudioCaptureId) | Introduced into PhoneAudioSes.dll in Windows 10.0.14393.0 |
| [**GetDefaultAudioRenderId**](https://www.bing.com/search?q=GetDefaultAudioRenderId)   | Introduced into PhoneAudioSes.dll in Windows 10.0.14393.0 |

 

## <span id="_MSAJAPI.DLL"></span>APIs from the dll MSAJApi.dll


| API                                                                                                    | Requirements                                        |
|--------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| [**alljoyn\_aboutdata\_createfromxml**](https://www.bing.com/search?q=alljoyn_aboutdata_createfromxml) | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_routerinit**](https://www.bing.com/search?q=alljoyn_routerinit)                            | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_routershutdown**](https://www.bing.com/search?q=alljoyn_routershutdown)                    | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |

 

## <span id="_BCRYPT.DLL"></span>APIs from the dll Bcrypt.dll


| API                                                                                            | Requirements                                       |
|------------------------------------------------------------------------------------------------|----------------------------------------------------|
| [**BCryptCreateMultiHash**](https://www.bing.com/search?q=BCryptCreateMultiHash)               | Introduced into Bcrypt.dll in Windows 10.0.10240.0 |
| [**BCryptProcessMultiOperations**](https://www.bing.com/search?q=BCryptProcessMultiOperations) | Introduced into Bcrypt.dll in Windows 10.0.10240.0 |

 

## <span id="_OLE32.DLL"></span>APIs from the dll ole32.dll


| API                                                        | Requirements                                                                                                    |
|------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| [**BindMoniker**](https://msdn.microsoft.com/en-us/library/windows/apps/ms683759.aspx)                         | Introduced into ole32.dll in Windows 10.0.10240.0                                                               |
| [**CreateAntiMoniker**](https://msdn.microsoft.com/en-us/library/windows/apps/ms679750.aspx)             | Introduced into ole32.dll in Windows 10.0.10240.0                                                               |
| [**CreateClassMoniker**](https://msdn.microsoft.com/en-us/library/windows/apps/ms688698.aspx)           | Introduced into ole32.dll in Windows 10.0.10240.0                                                               |
| [**CreateFileMoniker**](https://msdn.microsoft.com/en-us/library/windows/apps/ms693465.aspx)             | Introduced into ole32.dll in Windows 10.0.10240.0. Moved to ext-ms-win-com-ole32-l1-1-4 in Windows 10.0.14393.0 |
| [**CreateObjrefMoniker**](https://msdn.microsoft.com/en-us/library/windows/apps/ms678493.aspx)         | Introduced into ole32.dll in Windows 10.0.10240.0                                                               |
| [**IsEqualGUID**](https://msdn.microsoft.com/en-us/library/windows/apps/ms680575.aspx)                         | Introduced into ole32.dll in Windows 10.0.10240.0                                                               |
| [**MonikerCommonPrefixWith**](https://msdn.microsoft.com/en-us/library/windows/apps/ms686583.aspx) | Introduced into ole32.dll in Windows 10.0.10240.0                                                               |

 

## <span id="_DMPROCESSXMLFILTERED.DLL"></span>APIs from the dll dmprocessxmlfiltered.dll


| API                                                                                        | Requirements                                                     |
|--------------------------------------------------------------------------------------------|------------------------------------------------------------------|
| [**DMProcessConfigXMLFiltered**](https://www.bing.com/search?q=DMProcessConfigXMLFiltered) | Introduced into dmprocessxmlfiltered.dll in Windows 10.0.10240.0 |

 

## <span id="_IPHLPAPI.DLL"></span>APIs from the dll iphlpapi.dll


| API                                                            | Requirements                                         |
|----------------------------------------------------------------|------------------------------------------------------|
| [**GetAdaptersAddresses**](https://msdn.microsoft.com/en-us/library/windows/apps/aa365915.aspx)         | Introduced into iphlpapi.dll in Windows 10.0.10240.0 |
| [**FreeMibTable**](https://msdn.microsoft.com/en-us/library/windows/apps/aa814408.aspx)                         | Introduced into iphlpapi.dll in Windows 10.0.10586.0 |
| [**GetBestRoute2**](https://msdn.microsoft.com/en-us/library/windows/apps/aa814411.aspx)                       | Introduced into iphlpapi.dll in Windows 10.0.10586.0 |
| [**GetUnicastIpAddressTable**](https://msdn.microsoft.com/en-us/library/windows/apps/aa814428.aspx) | Introduced into iphlpapi.dll in Windows 10.0.10586.0 |

 

## <span id="_PHONEAUDIOSES.LIB"></span>APIs from the dll PhoneAudioSes.lib


| API                                                                                    | Requirements                                              |
|----------------------------------------------------------------------------------------|-----------------------------------------------------------|
| [**GetDefaultAudioCaptureId**](https://www.bing.com/search?q=GetDefaultAudioCaptureId) | Introduced into PhoneAudioSes.lib in Windows 10.0.10240.0 |
| [**GetDefaultAudioRenderId**](https://www.bing.com/search?q=GetDefaultAudioRenderId)   | Introduced into PhoneAudioSes.lib in Windows 10.0.10240.0 |

 

## <span id="_WPGLOBUTIL.DLL"></span>APIs from the dll wpglobutil.dll


| API                                                                  | Requirements                                           |
|----------------------------------------------------------------------|--------------------------------------------------------|
| [**GetTimeZoneList**](https://www.bing.com/search?q=GetTimeZoneList) | Introduced into wpglobutil.dll in Windows 10.0.10240.0 |

 

## <span id="_KERNEL32.DLL"></span>APIs from the dll kernel32.dll


| API                                                                                                      | Requirements                                         |
|----------------------------------------------------------------------------------------------------------|------------------------------------------------------|
| [**InterlockedCompareExchange**](https://msdn.microsoft.com/en-us/library/windows/apps/ff471479.aspx) | Introduced into kernel32.dll in Windows 10.0.10240.0 |
| [**InterlockedCompareExchange64**](https://msdn.microsoft.com/en-us/library/windows/apps/ms683562.aspx)                                    | Introduced into kernel32.dll in Windows 10.0.10240.0 |
| [**InterlockedDecrement**](https://msdn.microsoft.com/en-us/library/windows/apps/ms683580.aspx)                                                    | Introduced into kernel32.dll in Windows 10.0.10240.0 |
| [**InterlockedExchange**](https://msdn.microsoft.com/en-us/library/windows/apps/ff471481.aspx)               | Introduced into kernel32.dll in Windows 10.0.10240.0 |
| [**InterlockedExchangeAdd**](https://msdn.microsoft.com/en-us/library/windows/apps/ms683597.aspx)                                                | Introduced into kernel32.dll in Windows 10.0.10240.0 |
| [**InterlockedIncrement**](https://msdn.microsoft.com/en-us/library/windows/apps/ms683614.aspx)                                                    | Introduced into kernel32.dll in Windows 10.0.10240.0 |

 

## <span id="_KERNELBASE.DLL"></span>APIs from the dll kernelbase.dll


| API                                                    | Requirements                                           |
|--------------------------------------------------------|--------------------------------------------------------|
| [**GetProcessMemoryInfo**](https://msdn.microsoft.com/en-us/library/windows/apps/ms683219.aspx) | Introduced into kernelbase.dll in Windows 10.0.10240.0 |

 

## <span id="_RPCRT4.DLL"></span>APIs from the dll rpcrt4.dll


| API                                                | Requirements                                       |
|----------------------------------------------------|----------------------------------------------------|
| [**NdrAsyncClientCall2**](https://msdn.microsoft.com/en-us/library/windows/apps/mt297483.aspx) | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrClientCall4**](https://msdn.microsoft.com/en-us/library/windows/apps/mt297484.aspx)           | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |

 

## <span id="_windows.data.pdf.dll"></span><span id="_WINDOWS.DATA.PDF.DLL"></span>APIs from the dll windows.data.pdf.dll


| API                                          | Requirements                                                 |
|----------------------------------------------|--------------------------------------------------------------|
| [**PdfRenderParams**](https://msdn.microsoft.com/en-us/library/windows/apps/mt604123.aspx) | Introduced into windows.data.pdf.dll in Windows 10.0.10240.0 |

 

## <span id="_SRPAPI.DLL"></span>APIs from the dll srpapi.dll


| API                                                                                                | Requirements                                       |
|----------------------------------------------------------------------------------------------------|----------------------------------------------------|
| [**SrpDoesPolicyAllowAppExecution**](https://www.bing.com/search?q=SrpDoesPolicyAllowAppExecution) | Introduced into srpapi.dll in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-crt-math-l1-1-0.dll"></span><span id="_API-MS-WIN-CRT-MATH-L1-1-0.DLL"></span>APIs from the dll api-ms-win-crt-math-l1-1-0.dll


| API                                                                       | Requirements                                                           |
|---------------------------------------------------------------------------|------------------------------------------------------------------------|
| [**\_set\_SSE2\_enable**](https://www.bing.com/search?q=_set_SSE2_enable) | Introduced into api-ms-win-crt-math-l1-1-0.dll in Windows 10.0.10240.0 |
| [**fabsf**](https://www.bing.com/search?q=fabsf)                          | Introduced into api-ms-win-crt-math-l1-1-0.dll in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-crt-runtime-l1-1-0.dll"></span><span id="_API-MS-WIN-CRT-RUNTIME-L1-1-0.DLL"></span>APIs from the dll api-ms-win-crt-runtime-l1-1-0.dll


| API                                                                 | Requirements                                                              |
|---------------------------------------------------------------------|---------------------------------------------------------------------------|
| [**\_\_control87\_2**](https://www.bing.com/search?q=__control87_2) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in Windows 10.0.10240.0 |
| [**\_statusfp2**](https://www.bing.com/search?q=_statusfp2)         | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in Windows 10.0.10240.0 |

 

## <span id="_WINSQLITE3.DLL"></span>APIs from the dll winsqlite3.dll


| API                                                                                                     | Requirements                                           |
|---------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
| [**sqlite3\_aggregate\_context**](https://www.bing.com/search?q=sqlite3_aggregate_context)              | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_aggregate\_count**](https://www.bing.com/search?q=sqlite3_aggregate_count)                  | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_auto\_extension**](https://www.bing.com/search?q=sqlite3_auto_extension)                    | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_backup\_finish**](https://www.bing.com/search?q=sqlite3_backup_finish)                      | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_backup\_init**](https://www.bing.com/search?q=sqlite3_backup_init)                          | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_backup\_pagecount**](https://www.bing.com/search?q=sqlite3_backup_pagecount)                | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_backup\_remaining**](https://www.bing.com/search?q=sqlite3_backup_remaining)                | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_backup\_step**](https://www.bing.com/search?q=sqlite3_backup_step)                          | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_bind\_blob**](https://www.bing.com/search?q=sqlite3_bind_blob)                              | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_bind\_blob64**](https://www.bing.com/search?q=sqlite3_bind_blob64)                          | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_bind\_double**](https://www.bing.com/search?q=sqlite3_bind_double)                          | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_bind\_int**](https://www.bing.com/search?q=sqlite3_bind_int)                                | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_bind\_int64**](https://www.bing.com/search?q=sqlite3_bind_int64)                            | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_bind\_null**](https://www.bing.com/search?q=sqlite3_bind_null)                              | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_bind\_parameter\_count**](https://www.bing.com/search?q=sqlite3_bind_parameter_count)       | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_bind\_parameter\_index**](https://www.bing.com/search?q=sqlite3_bind_parameter_index)       | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_bind\_parameter\_name**](https://www.bing.com/search?q=sqlite3_bind_parameter_name)         | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_bind\_text**](https://www.bing.com/search?q=sqlite3_bind_text)                              | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_bind\_text16**](https://www.bing.com/search?q=sqlite3_bind_text16)                          | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_bind\_text64**](https://www.bing.com/search?q=sqlite3_bind_text64)                          | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_bind\_value**](https://www.bing.com/search?q=sqlite3_bind_value)                            | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_bind\_zeroblob**](https://www.bing.com/search?q=sqlite3_bind_zeroblob)                      | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_blob\_bytes**](https://www.bing.com/search?q=sqlite3_blob_bytes)                            | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_blob\_close**](https://www.bing.com/search?q=sqlite3_blob_close)                            | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_blob\_open**](https://www.bing.com/search?q=sqlite3_blob_open)                              | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_blob\_read**](https://www.bing.com/search?q=sqlite3_blob_read)                              | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_blob\_reopen**](https://www.bing.com/search?q=sqlite3_blob_reopen)                          | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_blob\_write**](https://www.bing.com/search?q=sqlite3_blob_write)                            | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_busy\_handler**](https://www.bing.com/search?q=sqlite3_busy_handler)                        | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_busy\_timeout**](https://www.bing.com/search?q=sqlite3_busy_timeout)                        | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_cancel\_auto\_extension**](https://www.bing.com/search?q=sqlite3_cancel_auto_extension)     | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_changes**](https://www.bing.com/search?q=sqlite3_changes)                                   | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_clear\_bindings**](https://www.bing.com/search?q=sqlite3_clear_bindings)                    | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_close**](https://www.bing.com/search?q=sqlite3_close)                                       | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_close\_v2**](https://www.bing.com/search?q=sqlite3_close_v2)                                | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_collation\_needed**](https://www.bing.com/search?q=sqlite3_collation_needed)                | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_collation\_needed16**](https://www.bing.com/search?q=sqlite3_collation_needed16)            | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_column\_blob**](https://www.bing.com/search?q=sqlite3_column_blob)                          | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_column\_bytes**](https://www.bing.com/search?q=sqlite3_column_bytes)                        | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_column\_bytes16**](https://www.bing.com/search?q=sqlite3_column_bytes16)                    | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_column\_count**](https://www.bing.com/search?q=sqlite3_column_count)                        | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_column\_database\_name**](https://www.bing.com/search?q=sqlite3_column_database_name)       | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_column\_database\_name16**](https://www.bing.com/search?q=sqlite3_column_database_name16)   | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_column\_decltype**](https://www.bing.com/search?q=sqlite3_column_decltype)                  | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_column\_decltype16**](https://www.bing.com/search?q=sqlite3_column_decltype16)              | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_column\_double**](https://www.bing.com/search?q=sqlite3_column_double)                      | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_column\_int**](https://www.bing.com/search?q=sqlite3_column_int)                            | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_column\_int64**](https://www.bing.com/search?q=sqlite3_column_int64)                        | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_column\_name**](https://www.bing.com/search?q=sqlite3_column_name)                          | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_column\_name16**](https://www.bing.com/search?q=sqlite3_column_name16)                      | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_column\_origin\_name**](https://www.bing.com/search?q=sqlite3_column_origin_name)           | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_column\_origin\_name16**](https://www.bing.com/search?q=sqlite3_column_origin_name16)       | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_column\_table\_name**](https://www.bing.com/search?q=sqlite3_column_table_name)             | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_column\_table\_name16**](https://www.bing.com/search?q=sqlite3_column_table_name16)         | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_column\_text**](https://www.bing.com/search?q=sqlite3_column_text)                          | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_column\_text16**](https://www.bing.com/search?q=sqlite3_column_text16)                      | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_column\_type**](https://www.bing.com/search?q=sqlite3_column_type)                          | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_column\_value**](https://www.bing.com/search?q=sqlite3_column_value)                        | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_commit\_hook**](https://www.bing.com/search?q=sqlite3_commit_hook)                          | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_compileoption\_get**](https://www.bing.com/search?q=sqlite3_compileoption_get)              | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_compileoption\_used**](https://www.bing.com/search?q=sqlite3_compileoption_used)            | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_complete**](https://www.bing.com/search?q=sqlite3_complete)                                 | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_complete16**](https://www.bing.com/search?q=sqlite3_complete16)                             | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_config**](https://www.bing.com/search?q=sqlite3_config)                                     | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_context\_db\_handle**](https://www.bing.com/search?q=sqlite3_context_db_handle)             | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_create\_collation**](https://www.bing.com/search?q=sqlite3_create_collation)                | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_create\_collation16**](https://www.bing.com/search?q=sqlite3_create_collation16)            | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_create\_collation\_v2**](https://www.bing.com/search?q=sqlite3_create_collation_v2)         | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_create\_function**](https://www.bing.com/search?q=sqlite3_create_function)                  | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_create\_function16**](https://www.bing.com/search?q=sqlite3_create_function16)              | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_create\_function\_v2**](https://www.bing.com/search?q=sqlite3_create_function_v2)           | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_create\_module**](https://www.bing.com/search?q=sqlite3_create_module)                      | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_create\_module\_v2**](https://www.bing.com/search?q=sqlite3_create_module_v2)               | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_data\_count**](https://www.bing.com/search?q=sqlite3_data_count)                            | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_data\_directory**](https://www.bing.com/search?q=sqlite3_data_directory)                    | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_db\_config**](https://www.bing.com/search?q=sqlite3_db_config)                              | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_db\_filename**](https://www.bing.com/search?q=sqlite3_db_filename)                          | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_db\_handle**](https://www.bing.com/search?q=sqlite3_db_handle)                              | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_db\_mutex**](https://www.bing.com/search?q=sqlite3_db_mutex)                                | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_db\_readonly**](https://www.bing.com/search?q=sqlite3_db_readonly)                          | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_db\_release\_memory**](https://www.bing.com/search?q=sqlite3_db_release_memory)             | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_db\_status**](https://www.bing.com/search?q=sqlite3_db_status)                              | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_declare\_vtab**](https://www.bing.com/search?q=sqlite3_declare_vtab)                        | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_enable\_load\_extension**](https://www.bing.com/search?q=sqlite3_enable_load_extension)     | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_enable\_shared\_cache**](https://www.bing.com/search?q=sqlite3_enable_shared_cache)         | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_errcode**](https://www.bing.com/search?q=sqlite3_errcode)                                   | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_errmsg**](https://www.bing.com/search?q=sqlite3_errmsg)                                     | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_errmsg16**](https://www.bing.com/search?q=sqlite3_errmsg16)                                 | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_errstr**](https://www.bing.com/search?q=sqlite3_errstr)                                     | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_exec**](https://www.bing.com/search?q=sqlite3_exec)                                         | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_expired**](https://www.bing.com/search?q=sqlite3_expired)                                   | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_extended\_errcode**](https://www.bing.com/search?q=sqlite3_extended_errcode)                | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_extended\_result\_codes**](https://www.bing.com/search?q=sqlite3_extended_result_codes)     | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_file\_control**](https://www.bing.com/search?q=sqlite3_file_control)                        | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_finalize**](https://www.bing.com/search?q=sqlite3_finalize)                                 | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_free**](https://www.bing.com/search?q=sqlite3_free)                                         | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_free\_table**](https://www.bing.com/search?q=sqlite3_free_table)                            | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_get\_autocommit**](https://www.bing.com/search?q=sqlite3_get_autocommit)                    | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_get\_auxdata**](https://www.bing.com/search?q=sqlite3_get_auxdata)                          | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_get\_table**](https://www.bing.com/search?q=sqlite3_get_table)                              | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_global\_recover**](https://www.bing.com/search?q=sqlite3_global_recover)                    | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_initialize**](https://www.bing.com/search?q=sqlite3_initialize)                             | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_interrupt**](https://www.bing.com/search?q=sqlite3_interrupt)                               | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_last\_insert\_rowid**](https://www.bing.com/search?q=sqlite3_last_insert_rowid)             | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_libversion**](https://www.bing.com/search?q=sqlite3_libversion)                             | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_libversion\_number**](https://www.bing.com/search?q=sqlite3_libversion_number)              | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_limit**](https://www.bing.com/search?q=sqlite3_limit)                                       | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_load\_extension**](https://www.bing.com/search?q=sqlite3_load_extension)                    | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_log**](https://www.bing.com/search?q=sqlite3_log)                                           | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_malloc**](https://www.bing.com/search?q=sqlite3_malloc)                                     | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_malloc64**](https://www.bing.com/search?q=sqlite3_malloc64)                                 | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_memory\_alarm**](https://www.bing.com/search?q=sqlite3_memory_alarm)                        | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_memory\_highwater**](https://www.bing.com/search?q=sqlite3_memory_highwater)                | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_memory\_used**](https://www.bing.com/search?q=sqlite3_memory_used)                          | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_mprintf**](https://www.bing.com/search?q=sqlite3_mprintf)                                   | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_msize**](https://www.bing.com/search?q=sqlite3_msize)                                       | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_mutex\_alloc**](https://www.bing.com/search?q=sqlite3_mutex_alloc)                          | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_mutex\_enter**](https://www.bing.com/search?q=sqlite3_mutex_enter)                          | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_mutex\_free**](https://www.bing.com/search?q=sqlite3_mutex_free)                            | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_mutex\_leave**](https://www.bing.com/search?q=sqlite3_mutex_leave)                          | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_mutex\_try**](https://www.bing.com/search?q=sqlite3_mutex_try)                              | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_next\_stmt**](https://www.bing.com/search?q=sqlite3_next_stmt)                              | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_open**](https://www.bing.com/search?q=sqlite3_open)                                         | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_open16**](https://www.bing.com/search?q=sqlite3_open16)                                     | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_open\_v2**](https://www.bing.com/search?q=sqlite3_open_v2)                                  | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_os\_end**](https://www.bing.com/search?q=sqlite3_os_end)                                    | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_os\_init**](https://www.bing.com/search?q=sqlite3_os_init)                                  | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_overload\_function**](https://www.bing.com/search?q=sqlite3_overload_function)              | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_prepare**](https://www.bing.com/search?q=sqlite3_prepare)                                   | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_prepare16**](https://www.bing.com/search?q=sqlite3_prepare16)                               | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_prepare16\_v2**](https://www.bing.com/search?q=sqlite3_prepare16_v2)                        | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_prepare\_v2**](https://www.bing.com/search?q=sqlite3_prepare_v2)                            | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_profile**](https://www.bing.com/search?q=sqlite3_profile)                                   | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_progress\_handler**](https://www.bing.com/search?q=sqlite3_progress_handler)                | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_randomness**](https://www.bing.com/search?q=sqlite3_randomness)                             | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_realloc**](https://www.bing.com/search?q=sqlite3_realloc)                                   | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_realloc64**](https://www.bing.com/search?q=sqlite3_realloc64)                               | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_release\_memory**](https://www.bing.com/search?q=sqlite3_release_memory)                    | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_reset**](https://www.bing.com/search?q=sqlite3_reset)                                       | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_reset\_auto\_extension**](https://www.bing.com/search?q=sqlite3_reset_auto_extension)       | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_result\_blob**](https://www.bing.com/search?q=sqlite3_result_blob)                          | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_result\_blob64**](https://www.bing.com/search?q=sqlite3_result_blob64)                      | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_result\_double**](https://www.bing.com/search?q=sqlite3_result_double)                      | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_result\_error**](https://www.bing.com/search?q=sqlite3_result_error)                        | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_result\_error16**](https://www.bing.com/search?q=sqlite3_result_error16)                    | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_result\_error\_code**](https://www.bing.com/search?q=sqlite3_result_error_code)             | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_result\_error\_nomem**](https://www.bing.com/search?q=sqlite3_result_error_nomem)           | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_result\_error\_toobig**](https://www.bing.com/search?q=sqlite3_result_error_toobig)         | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_result\_int**](https://www.bing.com/search?q=sqlite3_result_int)                            | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_result\_int64**](https://www.bing.com/search?q=sqlite3_result_int64)                        | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_result\_null**](https://www.bing.com/search?q=sqlite3_result_null)                          | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_result\_text**](https://www.bing.com/search?q=sqlite3_result_text)                          | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_result\_text16**](https://www.bing.com/search?q=sqlite3_result_text16)                      | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_result\_text16be**](https://www.bing.com/search?q=sqlite3_result_text16be)                  | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_result\_text16le**](https://www.bing.com/search?q=sqlite3_result_text16le)                  | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_result\_text64**](https://www.bing.com/search?q=sqlite3_result_text64)                      | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_result\_value**](https://www.bing.com/search?q=sqlite3_result_value)                        | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_result\_zeroblob**](https://www.bing.com/search?q=sqlite3_result_zeroblob)                  | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_rollback\_hook**](https://www.bing.com/search?q=sqlite3_rollback_hook)                      | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_rtree\_geometry\_callback**](https://www.bing.com/search?q=sqlite3_rtree_geometry_callback) | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_rtree\_query\_callback**](https://www.bing.com/search?q=sqlite3_rtree_query_callback)       | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_set\_authorizer**](https://www.bing.com/search?q=sqlite3_set_authorizer)                    | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_set\_auxdata**](https://www.bing.com/search?q=sqlite3_set_auxdata)                          | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_shutdown**](https://www.bing.com/search?q=sqlite3_shutdown)                                 | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_sleep**](https://www.bing.com/search?q=sqlite3_sleep)                                       | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_snprintf**](https://www.bing.com/search?q=sqlite3_snprintf)                                 | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_soft\_heap\_limit**](https://www.bing.com/search?q=sqlite3_soft_heap_limit)                 | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_soft\_heap\_limit64**](https://www.bing.com/search?q=sqlite3_soft_heap_limit64)             | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_sourceid**](https://www.bing.com/search?q=sqlite3_sourceid)                                 | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_sql**](https://www.bing.com/search?q=sqlite3_sql)                                           | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_status**](https://www.bing.com/search?q=sqlite3_status)                                     | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_step**](https://www.bing.com/search?q=sqlite3_step)                                         | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_stmt\_busy**](https://www.bing.com/search?q=sqlite3_stmt_busy)                              | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_stmt\_readonly**](https://www.bing.com/search?q=sqlite3_stmt_readonly)                      | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_stmt\_status**](https://www.bing.com/search?q=sqlite3_stmt_status)                          | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_strglob**](https://www.bing.com/search?q=sqlite3_strglob)                                   | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_stricmp**](https://www.bing.com/search?q=sqlite3_stricmp)                                   | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_strnicmp**](https://www.bing.com/search?q=sqlite3_strnicmp)                                 | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_table\_column\_metadata**](https://www.bing.com/search?q=sqlite3_table_column_metadata)     | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_temp\_directory**](https://www.bing.com/search?q=sqlite3_temp_directory)                    | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_test\_control**](https://www.bing.com/search?q=sqlite3_test_control)                        | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_thread\_cleanup**](https://www.bing.com/search?q=sqlite3_thread_cleanup)                    | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_threadsafe**](https://www.bing.com/search?q=sqlite3_threadsafe)                             | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_total\_changes**](https://www.bing.com/search?q=sqlite3_total_changes)                      | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_trace**](https://www.bing.com/search?q=sqlite3_trace)                                       | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_transfer\_bindings**](https://www.bing.com/search?q=sqlite3_transfer_bindings)              | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_update\_hook**](https://www.bing.com/search?q=sqlite3_update_hook)                          | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_uri\_boolean**](https://www.bing.com/search?q=sqlite3_uri_boolean)                          | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_uri\_int64**](https://www.bing.com/search?q=sqlite3_uri_int64)                              | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_uri\_parameter**](https://www.bing.com/search?q=sqlite3_uri_parameter)                      | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_user\_data**](https://www.bing.com/search?q=sqlite3_user_data)                              | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_value\_blob**](https://www.bing.com/search?q=sqlite3_value_blob)                            | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_value\_bytes**](https://www.bing.com/search?q=sqlite3_value_bytes)                          | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_value\_bytes16**](https://www.bing.com/search?q=sqlite3_value_bytes16)                      | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_value\_double**](https://www.bing.com/search?q=sqlite3_value_double)                        | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_value\_int**](https://www.bing.com/search?q=sqlite3_value_int)                              | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_value\_int64**](https://www.bing.com/search?q=sqlite3_value_int64)                          | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_value\_numeric\_type**](https://www.bing.com/search?q=sqlite3_value_numeric_type)           | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_value\_text**](https://www.bing.com/search?q=sqlite3_value_text)                            | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_value\_text16**](https://www.bing.com/search?q=sqlite3_value_text16)                        | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_value\_text16be**](https://www.bing.com/search?q=sqlite3_value_text16be)                    | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_value\_text16le**](https://www.bing.com/search?q=sqlite3_value_text16le)                    | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_value\_type**](https://www.bing.com/search?q=sqlite3_value_type)                            | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_version**](https://www.bing.com/search?q=sqlite3_version)                                   | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_vfs\_find**](https://www.bing.com/search?q=sqlite3_vfs_find)                                | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_vfs\_register**](https://www.bing.com/search?q=sqlite3_vfs_register)                        | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_vfs\_unregister**](https://www.bing.com/search?q=sqlite3_vfs_unregister)                    | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_vmprintf**](https://www.bing.com/search?q=sqlite3_vmprintf)                                 | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_vsnprintf**](https://www.bing.com/search?q=sqlite3_vsnprintf)                               | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_vtab\_config**](https://www.bing.com/search?q=sqlite3_vtab_config)                          | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_vtab\_on\_conflict**](https://www.bing.com/search?q=sqlite3_vtab_on_conflict)               | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_wal\_autocheckpoint**](https://www.bing.com/search?q=sqlite3_wal_autocheckpoint)            | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_wal\_checkpoint**](https://www.bing.com/search?q=sqlite3_wal_checkpoint)                    | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_wal\_checkpoint\_v2**](https://www.bing.com/search?q=sqlite3_wal_checkpoint_v2)             | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_wal\_hook**](https://www.bing.com/search?q=sqlite3_wal_hook)                                | Introduced into winsqlite3.dll in Windows 10.0.10586.0 |
| [**sqlite3\_bind\_zeroblob64**](https://www.bing.com/search?q=sqlite3_bind_zeroblob64)                  | Introduced into winsqlite3.dll in Windows 10.0.14393.0 |
| [**sqlite3\_db\_cacheflush**](https://www.bing.com/search?q=sqlite3_db_cacheflush)                      | Introduced into winsqlite3.dll in Windows 10.0.14393.0 |
| [**sqlite3\_result\_subtype**](https://www.bing.com/search?q=sqlite3_result_subtype)                    | Introduced into winsqlite3.dll in Windows 10.0.14393.0 |
| [**sqlite3\_result\_zeroblob64**](https://www.bing.com/search?q=sqlite3_result_zeroblob64)              | Introduced into winsqlite3.dll in Windows 10.0.14393.0 |
| [**sqlite3\_status64**](https://www.bing.com/search?q=sqlite3_status64)                                 | Introduced into winsqlite3.dll in Windows 10.0.14393.0 |
| [**sqlite3\_strlike**](https://www.bing.com/search?q=sqlite3_strlike)                                   | Introduced into winsqlite3.dll in Windows 10.0.14393.0 |
| [**sqlite3\_system\_errno**](https://www.bing.com/search?q=sqlite3_system_errno)                        | Introduced into winsqlite3.dll in Windows 10.0.14393.0 |
| [**sqlite3\_value\_dup**](https://www.bing.com/search?q=sqlite3_value_dup)                              | Introduced into winsqlite3.dll in Windows 10.0.14393.0 |
| [**sqlite3\_value\_free**](https://www.bing.com/search?q=sqlite3_value_free)                            | Introduced into winsqlite3.dll in Windows 10.0.14393.0 |
| [**sqlite3\_value\_subtype**](https://www.bing.com/search?q=sqlite3_value_subtype)                      | Introduced into winsqlite3.dll in Windows 10.0.14393.0 |

 

## <span id="_USER32.DLL"></span>APIs from the dll user32.dll


| API                                              | Requirements                                       |
|--------------------------------------------------|----------------------------------------------------|
| [**GetKeyNameTextA**](https://msdn.microsoft.com/en-us/library/windows/apps/ms646300.aspx)   | Introduced into user32.dll in Windows 10.0.14393.0 |
| [**MapVirtualKeyExA**](https://msdn.microsoft.com/en-us/library/windows/apps/ms646307.aspx) | Introduced into user32.dll in Windows 10.0.14393.0 |

 

## <span id="_com_interfaces"></span><span id="_COM_INTERFACES"></span>COM interfaces


| API                                                                                                                                      | Requirements                       |
|------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------|
| [**\_IRDPSessionEvents**](https://msdn.microsoft.com/en-us/library/windows/apps/aa373879.aspx)                                                                                        | Introduced in Windows 10.0.10240.0 |
| [**\_IWorkspaceBrokerAxEvents**](https://www.bing.com/search?q=_IWorkspaceBrokerAxEvents)                                                | Introduced in Windows 10.0.10240.0 |
| [**IAccessibleEx**](https://msdn.microsoft.com/en-us/library/windows/apps/ee671234.aspx)                                                                                        | Introduced in Windows 10.0.10240.0 |
| [**IAccessibleHostingElementProviders**](https://msdn.microsoft.com/en-us/library/windows/apps/hh448733.aspx)                                                     | Introduced in Windows 10.0.10240.0 |
| [**IActivateAudioInterfaceAsyncOperation**](https://msdn.microsoft.com/en-us/library/windows/apps/jj128300.aspx)                                             | Introduced in Windows 10.0.10240.0 |
| [**IActivateAudioInterfaceCompletionHandler**](https://msdn.microsoft.com/en-us/library/windows/apps/jj128302.aspx)                                       | Introduced in Windows 10.0.10240.0 |
| [**IActivationFactory**](https://msdn.microsoft.com/en-us/library/windows/apps/br205779.aspx)                                                                                       | Introduced in Windows 10.0.10240.0 |
| [**IAdvancedMediaCapture**](https://msdn.microsoft.com/en-us/library/windows/apps/hh802709.aspx)                                                                                    | Introduced in Windows 10.0.10240.0 |
| [**IAdvancedMediaCaptureInitializationSettings**](https://msdn.microsoft.com/en-us/library/windows/apps/hh802710.aspx)                                        | Introduced in Windows 10.0.10240.0 |
| [**IAdvancedMediaCaptureSettings**](https://msdn.microsoft.com/en-us/library/windows/apps/hh802712.aspx)                                                                    | Introduced in Windows 10.0.10240.0 |
| [**IAgileObject**](https://msdn.microsoft.com/en-us/library/windows/apps/hh802476.aspx)                                                                                                     | Introduced in Windows 10.0.10240.0 |
| [**IAgileObject**](https://msdn.microsoft.com/en-us/library/windows/apps/hh802476.aspx)                                                                                                     | Introduced in Windows 10.0.10240.0 |
| [**IAgileReference**](https://msdn.microsoft.com/en-us/library/windows/apps/dn269837.aspx)                                                                                             | Introduced in Windows 10.0.10240.0 |
| [**IAgileReference**](https://msdn.microsoft.com/en-us/library/windows/apps/dn269837.aspx)                                                                                             | Introduced in Windows 10.0.10240.0 |
| [**IAnnotationProvider**](https://msdn.microsoft.com/en-us/library/windows/apps/hh448757.aspx)                                                                            | Introduced in Windows 10.0.10240.0 |
| [**IAoWAppActivatedRuntime**](https://www.bing.com/search?q=IAoWAppActivatedRuntime)                                                     | Introduced in Windows 10.0.10240.0 |
| [**IAoWBackgroundTaskRuntime**](https://www.bing.com/search?q=IAoWBackgroundTaskRuntime)                                                 | Introduced in Windows 10.0.10240.0 |
| [**IApartmentShutdown**](https://msdn.microsoft.com/en-us/library/windows/apps/jj219263.aspx)                                                                                       | Introduced in Windows 10.0.10240.0 |
| [**IAsyncInfo**](https://msdn.microsoft.com/en-us/library/windows/apps/br205795.aspx)                                                                                                       | Introduced in Windows 10.0.10240.0 |
| [**IAudioCaptureClient**](https://msdn.microsoft.com/en-us/library/windows/apps/dd370858.aspx)                                                                                 | Introduced in Windows 10.0.10240.0 |
| [**IAudioClient**](https://msdn.microsoft.com/en-us/library/windows/apps/dd370865.aspx)                                                                                               | Introduced in Windows 10.0.10240.0 |
| [**IAudioClient2**](https://msdn.microsoft.com/en-us/library/windows/apps/hh404179.aspx)                                                                                             | Introduced in Windows 10.0.10240.0 |
| [**IAudioClient3**](https://msdn.microsoft.com/en-us/library/windows/apps/dn911487.aspx)                                                                                             | Introduced in Windows 10.0.10240.0 |
| [**IAudioClock**](https://msdn.microsoft.com/en-us/library/windows/apps/dd370881.aspx)                                                                                                 | Introduced in Windows 10.0.10240.0 |
| [**IAudioEndpointVolume**](https://msdn.microsoft.com/en-us/library/windows/apps/dd370892.aspx)                                                                               | Introduced in Windows 10.0.10240.0 |
| [**IAudioEndpointVolumeCallback**](https://msdn.microsoft.com/en-us/library/windows/apps/dd370894.aspx)                                                               | Introduced in Windows 10.0.10240.0 |
| [**IAudioFrameNative**](https://msdn.microsoft.com/en-us/library/windows/apps/mt431700.aspx)                                                                                         | Introduced in Windows 10.0.10240.0 |
| [**IAudioFrameNativeFactory**](https://msdn.microsoft.com/en-us/library/windows/apps/mt431701.aspx)                                                                           | Introduced in Windows 10.0.10240.0 |
| [**IAudioMeterInformation**](https://msdn.microsoft.com/en-us/library/windows/apps/dd368227.aspx)                                                                           | Introduced in Windows 10.0.10240.0 |
| [**IAudioRenderClient**](https://msdn.microsoft.com/en-us/library/windows/apps/dd368242.aspx)                                                                                   | Introduced in Windows 10.0.10240.0 |
| [**IAudioSessionControl**](https://msdn.microsoft.com/en-us/library/windows/apps/dd368246.aspx)                                                                               | Introduced in Windows 10.0.10240.0 |
| [**IAudioSessionEvents**](https://msdn.microsoft.com/en-us/library/windows/apps/dd368289.aspx)                                                                                 | Introduced in Windows 10.0.10240.0 |
| [**IAudioStreamVolume**](https://msdn.microsoft.com/en-us/library/windows/apps/dd370977.aspx)                                                                                   | Introduced in Windows 10.0.10240.0 |
| [**IAudioVideoCaptureDeviceNative**](https://www.bing.com/search?q=IAudioVideoCaptureDeviceNative)                                       | Introduced in Windows 10.0.10240.0 |
| [**IBindCtx**](https://msdn.microsoft.com/en-us/library/windows/apps/ms693755.aspx)                                                                                                             | Introduced in Windows 10.0.10240.0 |
| [**ICameraCaptureDeviceNative**](https://www.bing.com/search?q=ICameraCaptureDeviceNative)                                               | Introduced in Windows 10.0.10240.0 |
| [**ICameraCaptureFrameNative**](https://www.bing.com/search?q=ICameraCaptureFrameNative)                                                 | Introduced in Windows 10.0.10240.0 |
| [**ICameraCapturePreviewSink**](https://www.bing.com/search?q=ICameraCapturePreviewSink)                                                 | Introduced in Windows 10.0.10240.0 |
| [**ICameraUIControl**](https://www.bing.com/search?q=ICameraUIControl)                                                                   | Introduced in Windows 10.0.10240.0 |
| [**ICameraUIControlEventCallback**](https://www.bing.com/search?q=ICameraUIControlEventCallback)                                         | Introduced in Windows 10.0.10240.0 |
| [**IClassFactory**](https://msdn.microsoft.com/en-us/library/windows/apps/ms694364.aspx)                                                                                                   | Introduced in Windows 10.0.10240.0 |
| [**IClassFactory**](https://msdn.microsoft.com/en-us/library/windows/apps/ms694364.aspx)                                                                                                   | Introduced in Windows 10.0.10240.0 |
| [**IClientSecurity**](https://msdn.microsoft.com/en-us/library/windows/apps/ms683964.aspx)                                                                                               | Introduced in Windows 10.0.10240.0 |
| [**IClientSecurity**](https://msdn.microsoft.com/en-us/library/windows/apps/ms683964.aspx)                                                                                               | Introduced in Windows 10.0.10240.0 |
| [**ICodecAPI**](https://msdn.microsoft.com/en-us/library/windows/apps/dd311953.aspx)                                                                                                         | Introduced in Windows 10.0.10240.0 |
| [**IConnectionPoint**](https://msdn.microsoft.com/en-us/library/windows/apps/ms694318.aspx)                                                                                             | Introduced in Windows 10.0.10240.0 |
| [**IConnectionPointContainer**](https://msdn.microsoft.com/en-us/library/windows/apps/ms683857.aspx)                                                                           | Introduced in Windows 10.0.10240.0 |
| [**IContextCallback**](https://msdn.microsoft.com/en-us/library/windows/apps/ms682253.aspx)                                                                                             | Introduced in Windows 10.0.10240.0 |
| [**ICreateDeviceAccessAsync**](https://msdn.microsoft.com/en-us/library/windows/apps/hh404248.aspx)                                                                    | Introduced in Windows 10.0.10240.0 |
| [**ICustomNavigationProvider**](https://www.bing.com/search?q=ICustomNavigationProvider)                                                 | Introduced in Windows 10.0.10240.0 |
| [**ID2D1AnalysisTransform**](https://msdn.microsoft.com/en-us/library/windows/apps/hh404347.aspx)                                                                            | Introduced in Windows 10.0.10240.0 |
| [**ID2D1Bitmap**](https://msdn.microsoft.com/en-us/library/windows/apps/dd371109.aspx)                                                                                                  | Introduced in Windows 10.0.10240.0 |
| [**ID2D1Bitmap1**](https://msdn.microsoft.com/en-us/library/windows/apps/hh404349.aspx)                                                                                                | Introduced in Windows 10.0.10240.0 |
| [**ID2D1BitmapBrush**](https://msdn.microsoft.com/en-us/library/windows/apps/dd371122.aspx)                                                                                        | Introduced in Windows 10.0.10240.0 |
| [**ID2D1BitmapRenderTarget**](https://msdn.microsoft.com/en-us/library/windows/apps/dd371146.aspx)                                                                          | Introduced in Windows 10.0.10240.0 |
| [**ID2D1BlendTransform**](https://msdn.microsoft.com/en-us/library/windows/apps/hh404361.aspx)                                                                                  | Introduced in Windows 10.0.10240.0 |
| [**ID2D1BorderTransform**](https://msdn.microsoft.com/en-us/library/windows/apps/hh404367.aspx)                                                                                | Introduced in Windows 10.0.10240.0 |
| [**ID2D1BoundsAdjustmentTransform**](https://msdn.microsoft.com/en-us/library/windows/apps/hh847963.aspx)                                                             | Introduced in Windows 10.0.10240.0 |
| [**ID2D1Brush**](https://msdn.microsoft.com/en-us/library/windows/apps/dd371173.aspx)                                                                                                    | Introduced in Windows 10.0.10240.0 |
| [**ID2D1ColorContext**](https://msdn.microsoft.com/en-us/library/windows/apps/hh404388.aspx)                                                                                      | Introduced in Windows 10.0.10240.0 |
| [**ID2D1CommandList**](https://msdn.microsoft.com/en-us/library/windows/apps/hh404392.aspx)                                                                                        | Introduced in Windows 10.0.10240.0 |
| [**ID2D1CommandSink**](https://msdn.microsoft.com/en-us/library/windows/apps/hh404394.aspx)                                                                                        | Introduced in Windows 10.0.10240.0 |
| [**ID2D1CommandSink1**](https://msdn.microsoft.com/en-us/library/windows/apps/dn280436.aspx)                                                                                      | Introduced in Windows 10.0.10240.0 |
| [**ID2D1CommandSink2**](https://msdn.microsoft.com/en-us/library/windows/apps/dn890781.aspx)                                                                                      | Introduced in Windows 10.0.10240.0 |
| [**ID2D1ComputeInfo**](https://msdn.microsoft.com/en-us/library/windows/apps/hh847966.aspx)                                                                                        | Introduced in Windows 10.0.10240.0 |
| [**ID2D1ComputeTransform**](https://msdn.microsoft.com/en-us/library/windows/apps/hh404434.aspx)                                                                              | Introduced in Windows 10.0.10240.0 |
| [**ID2D1ConcreteTransform**](https://msdn.microsoft.com/en-us/library/windows/apps/hh404452.aspx)                                                                            | Introduced in Windows 10.0.10240.0 |
| [**ID2D1DCRenderTarget**](https://msdn.microsoft.com/en-us/library/windows/apps/dd371213.aspx)                                                                                  | Introduced in Windows 10.0.10240.0 |
| [**ID2D1Device**](https://msdn.microsoft.com/en-us/library/windows/apps/hh404478.aspx)                                                                                                  | Introduced in Windows 10.0.10240.0 |
| [**ID2D1Device1**](https://msdn.microsoft.com/en-us/library/windows/apps/dn280458.aspx)                                                                                                | Introduced in Windows 10.0.10240.0 |
| [**ID2D1Device2**](https://msdn.microsoft.com/en-us/library/windows/apps/dn890786.aspx)                                                                                                | Introduced in Windows 10.0.10240.0 |
| [**ID2D1DeviceContext**](https://msdn.microsoft.com/en-us/library/windows/apps/hh404479.aspx)                                                                                    | Introduced in Windows 10.0.10240.0 |
| [**ID2D1DeviceContext1**](https://msdn.microsoft.com/en-us/library/windows/apps/dn280461.aspx)                                                                                  | Introduced in Windows 10.0.10240.0 |
| [**ID2D1DeviceContext2**](https://msdn.microsoft.com/en-us/library/windows/apps/dn890789.aspx)                                                                                  | Introduced in Windows 10.0.10240.0 |
| [**ID2D1DrawInfo**](https://msdn.microsoft.com/en-us/library/windows/apps/hh847986.aspx)                                                                                              | Introduced in Windows 10.0.10240.0 |
| [**ID2D1DrawingStateBlock**](https://msdn.microsoft.com/en-us/library/windows/apps/dd371218.aspx)                                                                            | Introduced in Windows 10.0.10240.0 |
| [**ID2D1DrawingStateBlock1**](https://msdn.microsoft.com/en-us/library/windows/apps/hh871452.aspx)                                                                          | Introduced in Windows 10.0.10240.0 |
| [**ID2D1DrawTransform**](https://msdn.microsoft.com/en-us/library/windows/apps/hh847992.aspx)                                                                                    | Introduced in Windows 10.0.10240.0 |
| [**ID2D1Effect**](https://msdn.microsoft.com/en-us/library/windows/apps/hh404566.aspx)                                                                                                  | Introduced in Windows 10.0.10240.0 |
| [**ID2D1EffectContext**](https://msdn.microsoft.com/en-us/library/windows/apps/hh404459.aspx)                                                                                  | Introduced in Windows 10.0.10240.0 |
| [**ID2D1EffectContext1**](https://msdn.microsoft.com/en-us/library/windows/apps/dn949338.aspx)                                                                                  | Introduced in Windows 10.0.10240.0 |
| [**ID2D1EffectImpl**](https://msdn.microsoft.com/en-us/library/windows/apps/hh404568.aspx)                                                                                          | Introduced in Windows 10.0.10240.0 |
| [**ID2D1EllipseGeometry**](https://msdn.microsoft.com/en-us/library/windows/apps/dd371239.aspx)                                                                                | Introduced in Windows 10.0.10240.0 |
| [**ID2D1Factory**](https://msdn.microsoft.com/en-us/library/windows/apps/dd371246.aspx)                                                                                                | Introduced in Windows 10.0.10240.0 |
| [**ID2D1Factory1**](https://msdn.microsoft.com/en-us/library/windows/apps/hh404596.aspx)                                                                                              | Introduced in Windows 10.0.10240.0 |
| [**ID2D1Factory2**](https://msdn.microsoft.com/en-us/library/windows/apps/dn280481.aspx)                                                                                              | Introduced in Windows 10.0.10240.0 |
| [**ID2D1Factory3**](https://msdn.microsoft.com/en-us/library/windows/apps/dn900394.aspx)                                                                                              | Introduced in Windows 10.0.10240.0 |
| [**ID2D1GdiMetafile**](https://msdn.microsoft.com/en-us/library/windows/apps/hh871460.aspx)                                                                                        | Introduced in Windows 10.0.10240.0 |
| [**ID2D1GdiMetafile1**](https://msdn.microsoft.com/en-us/library/windows/apps/dn900400.aspx)                                                                                      | Introduced in Windows 10.0.10240.0 |
| [**ID2D1GdiMetafileSink**](https://msdn.microsoft.com/en-us/library/windows/apps/hh871461.aspx)                                                                                | Introduced in Windows 10.0.10240.0 |
| [**ID2D1GdiMetafileSink1**](https://msdn.microsoft.com/en-us/library/windows/apps/dn900403.aspx)                                                                              | Introduced in Windows 10.0.10240.0 |
| [**ID2D1Geometry**](https://msdn.microsoft.com/en-us/library/windows/apps/dd316578.aspx)                                                                                              | Introduced in Windows 10.0.10240.0 |
| [**ID2D1GeometryGroup**](https://msdn.microsoft.com/en-us/library/windows/apps/dd316581.aspx)                                                                                    | Introduced in Windows 10.0.10240.0 |
| [**ID2D1GeometryRealization**](https://msdn.microsoft.com/en-us/library/windows/apps/dn280515.aspx)                                                                        | Introduced in Windows 10.0.10240.0 |
| [**ID2D1GeometrySink**](https://msdn.microsoft.com/en-us/library/windows/apps/dd316592.aspx)                                                                                      | Introduced in Windows 10.0.10240.0 |
| [**ID2D1GradientMesh**](https://msdn.microsoft.com/en-us/library/windows/apps/dn900410.aspx)                                                                                      | Introduced in Windows 10.0.10240.0 |
| [**ID2D1GradientStopCollection**](https://msdn.microsoft.com/en-us/library/windows/apps/dd316783.aspx)                                                                  | Introduced in Windows 10.0.10240.0 |
| [**ID2D1GradientStopCollection1**](https://msdn.microsoft.com/en-us/library/windows/apps/hh446792.aspx)                                                                | Introduced in Windows 10.0.10240.0 |
| [**ID2D1HwndRenderTarget**](https://msdn.microsoft.com/en-us/library/windows/apps/dd371461.aspx)                                                                              | Introduced in Windows 10.0.10240.0 |
| [**ID2D1Image**](https://msdn.microsoft.com/en-us/library/windows/apps/hh446803.aspx)                                                                                                    | Introduced in Windows 10.0.10240.0 |
| [**ID2D1ImageBrush**](https://msdn.microsoft.com/en-us/library/windows/apps/hh446804.aspx)                                                                                          | Introduced in Windows 10.0.10240.0 |
| [**ID2D1ImageSource**](https://msdn.microsoft.com/en-us/library/windows/apps/dn900413.aspx)                                                                                        | Introduced in Windows 10.0.10240.0 |
| [**ID2D1ImageSourceFromWic**](https://msdn.microsoft.com/en-us/library/windows/apps/dn900414.aspx)                                                                          | Introduced in Windows 10.0.10240.0 |
| [**ID2D1Ink**](https://msdn.microsoft.com/en-us/library/windows/apps/dn900426.aspx)                                                                                                        | Introduced in Windows 10.0.10240.0 |
| [**ID2D1InkStyle**](https://msdn.microsoft.com/en-us/library/windows/apps/dn900427.aspx)                                                                                              | Introduced in Windows 10.0.10240.0 |
| [**ID2D1Layer**](https://msdn.microsoft.com/en-us/library/windows/apps/dd371483.aspx)                                                                                                    | Introduced in Windows 10.0.10240.0 |
| [**ID2D1LinearGradientBrush**](https://msdn.microsoft.com/en-us/library/windows/apps/dd371488.aspx)                                                                        | Introduced in Windows 10.0.10240.0 |
| [**ID2D1LookupTable3D**](https://msdn.microsoft.com/en-us/library/windows/apps/dn900453.aspx)                                                                                    | Introduced in Windows 10.0.10240.0 |
| [**ID2D1Mesh**](https://msdn.microsoft.com/en-us/library/windows/apps/dd371508.aspx)                                                                                                      | Introduced in Windows 10.0.10240.0 |
| [**ID2D1Multithread**](https://msdn.microsoft.com/en-us/library/windows/apps/hh997713.aspx)                                                                                        | Introduced in Windows 10.0.10240.0 |
| [**ID2D1OffsetTransform**](https://msdn.microsoft.com/en-us/library/windows/apps/hh446820.aspx)                                                                                | Introduced in Windows 10.0.10240.0 |
| [**ID2D1PathGeometry**](https://msdn.microsoft.com/en-us/library/windows/apps/dd371512.aspx)                                                                                      | Introduced in Windows 10.0.10240.0 |
| [**ID2D1PathGeometry1**](https://msdn.microsoft.com/en-us/library/windows/apps/hh446826.aspx)                                                                                    | Introduced in Windows 10.0.10240.0 |
| [**ID2D1PrintControl**](https://msdn.microsoft.com/en-us/library/windows/apps/hh847997.aspx)                                                                                      | Introduced in Windows 10.0.10240.0 |
| [**ID2D1Properties**](https://msdn.microsoft.com/en-us/library/windows/apps/hh446854.aspx)                                                                                          | Introduced in Windows 10.0.10240.0 |
| [**ID2D1RadialGradientBrush**](https://msdn.microsoft.com/en-us/library/windows/apps/dd371529.aspx)                                                                        | Introduced in Windows 10.0.10240.0 |
| [**ID2D1RectangleGeometry**](https://msdn.microsoft.com/en-us/library/windows/apps/dd371561.aspx)                                                                            | Introduced in Windows 10.0.10240.0 |
| [**ID2D1RenderInfo**](https://msdn.microsoft.com/en-us/library/windows/apps/hh446890.aspx)                                                                                          | Introduced in Windows 10.0.10240.0 |
| [**ID2D1RenderTarget**](https://msdn.microsoft.com/en-us/library/windows/apps/dd371766.aspx)                                                                                      | Introduced in Windows 10.0.10240.0 |
| [**ID2D1Resource**](https://msdn.microsoft.com/en-us/library/windows/apps/dd316908.aspx)                                                                                              | Introduced in Windows 10.0.10240.0 |
| [**ID2D1ResourceTexture**](https://msdn.microsoft.com/en-us/library/windows/apps/hh446904.aspx)                                                                                | Introduced in Windows 10.0.10240.0 |
| [**ID2D1RoundedRectangleGeometry**](https://msdn.microsoft.com/en-us/library/windows/apps/dd316914.aspx)                                                              | Introduced in Windows 10.0.10240.0 |
| [**ID2D1SimplifiedGeometrySink**](https://msdn.microsoft.com/en-us/library/windows/apps/dd316919.aspx)                                                                  | Introduced in Windows 10.0.10240.0 |
| [**ID2D1SolidColorBrush**](https://msdn.microsoft.com/en-us/library/windows/apps/dd372207.aspx)                                                                                | Introduced in Windows 10.0.10240.0 |
| [**ID2D1SourceTransform**](https://msdn.microsoft.com/en-us/library/windows/apps/hh446908.aspx)                                                                                | Introduced in Windows 10.0.10240.0 |
| [**ID2D1StrokeStyle**](https://msdn.microsoft.com/en-us/library/windows/apps/dd372217.aspx)                                                                                        | Introduced in Windows 10.0.10240.0 |
| [**ID2D1StrokeStyle1**](https://msdn.microsoft.com/en-us/library/windows/apps/hh446914.aspx)                                                                                      | Introduced in Windows 10.0.10240.0 |
| [**ID2D1TessellationSink**](https://msdn.microsoft.com/en-us/library/windows/apps/dd372245.aspx)                                                                              | Introduced in Windows 10.0.10240.0 |
| [**ID2D1Transform**](https://msdn.microsoft.com/en-us/library/windows/apps/hh446919.aspx)                                                                                            | Introduced in Windows 10.0.10240.0 |
| [**ID2D1TransformedGeometry**](https://msdn.microsoft.com/en-us/library/windows/apps/dd372252.aspx)                                                                        | Introduced in Windows 10.0.10240.0 |
| [**ID2D1TransformedImageSource**](https://msdn.microsoft.com/en-us/library/windows/apps/dn952305.aspx)                                                                  | Introduced in Windows 10.0.10240.0 |
| [**ID2D1TransformGraph**](https://msdn.microsoft.com/en-us/library/windows/apps/hh446920.aspx)                                                                                  | Introduced in Windows 10.0.10240.0 |
| [**ID2D1TransformNode**](https://msdn.microsoft.com/en-us/library/windows/apps/hh446939.aspx)                                                                                    | Introduced in Windows 10.0.10240.0 |
| [**ID2D1VertexBuffer**](https://msdn.microsoft.com/en-us/library/windows/apps/hh446949.aspx)                                                                                      | Introduced in Windows 10.0.10240.0 |
| [**ID3D10Blob**](https://msdn.microsoft.com/en-us/library/windows/apps/bb173507.aspx)                                                                                                  | Introduced in Windows 10.0.10240.0 |
| [**ID3D10Multithread**](https://msdn.microsoft.com/en-us/library/windows/apps/bb173816.aspx)                                                                                    | Introduced in Windows 10.0.10240.0 |
| [**ID3D11Asynchronous**](https://msdn.microsoft.com/en-us/library/windows/apps/ff476347.aspx)                                                                                  | Introduced in Windows 10.0.10240.0 |
| [**ID3D11AuthenticatedChannel**](https://msdn.microsoft.com/en-us/library/windows/apps/hh447690.aspx)                                                                          | Introduced in Windows 10.0.10240.0 |
| [**ID3D11BlendState**](https://msdn.microsoft.com/en-us/library/windows/apps/ff476349.aspx)                                                                                      | Introduced in Windows 10.0.10240.0 |
| [**ID3D11BlendState1**](https://msdn.microsoft.com/en-us/library/windows/apps/hh404571.aspx)                                                                                    | Introduced in Windows 10.0.10240.0 |
| [**ID3D11Buffer**](https://msdn.microsoft.com/en-us/library/windows/apps/ff476351.aspx)                                                                                              | Introduced in Windows 10.0.10240.0 |
| [**ID3D11ClassInstance**](https://msdn.microsoft.com/en-us/library/windows/apps/ff476353.aspx)                                                                                | Introduced in Windows 10.0.10240.0 |
| [**ID3D11ClassLinkage**](https://msdn.microsoft.com/en-us/library/windows/apps/ff476358.aspx)                                                                                  | Introduced in Windows 10.0.10240.0 |
| [**ID3D11CommandList**](https://msdn.microsoft.com/en-us/library/windows/apps/ff476361.aspx)                                                                                    | Introduced in Windows 10.0.10240.0 |
| [**ID3D11ComputeShader**](https://msdn.microsoft.com/en-us/library/windows/apps/ff476363.aspx)                                                                                | Introduced in Windows 10.0.10240.0 |
| [**ID3D11Counter**](https://msdn.microsoft.com/en-us/library/windows/apps/ff476364.aspx)                                                                                            | Introduced in Windows 10.0.10240.0 |
| [**ID3D11CryptoSession**](https://msdn.microsoft.com/en-us/library/windows/apps/hh447691.aspx)                                                                                        | Introduced in Windows 10.0.10240.0 |
| [**ID3D11Debug**](https://msdn.microsoft.com/en-us/library/windows/apps/ff476366.aspx)                                                                                                | Introduced in Windows 10.0.10240.0 |
| [**ID3D11DepthStencilState**](https://msdn.microsoft.com/en-us/library/windows/apps/ff476375.aspx)                                                                        | Introduced in Windows 10.0.10240.0 |
| [**ID3D11DepthStencilView**](https://msdn.microsoft.com/en-us/library/windows/apps/ff476377.aspx)                                                                          | Introduced in Windows 10.0.10240.0 |
| [**ID3D11Device**](https://msdn.microsoft.com/en-us/library/windows/apps/ff476379.aspx)                                                                                              | Introduced in Windows 10.0.10240.0 |
| [**ID3D11Device1**](https://msdn.microsoft.com/en-us/library/windows/apps/hh404575.aspx)                                                                                            | Introduced in Windows 10.0.10240.0 |
| [**ID3D11Device2**](https://msdn.microsoft.com/en-us/library/windows/apps/dn280493.aspx)                                                                                            | Introduced in Windows 10.0.10240.0 |
| [**ID3D11DeviceChild**](https://msdn.microsoft.com/en-us/library/windows/apps/ff476380.aspx)                                                                                    | Introduced in Windows 10.0.10240.0 |
| [**ID3D11DeviceContext**](https://msdn.microsoft.com/en-us/library/windows/apps/ff476385.aspx)                                                                                | Introduced in Windows 10.0.10240.0 |
| [**ID3D11DeviceContext1**](https://msdn.microsoft.com/en-us/library/windows/apps/hh404598.aspx)                                                                              | Introduced in Windows 10.0.10240.0 |
| [**ID3D11DeviceContext2**](https://msdn.microsoft.com/en-us/library/windows/apps/dn280498.aspx)                                                                              | Introduced in Windows 10.0.10240.0 |
| [**ID3D11DeviceContext3**](https://msdn.microsoft.com/en-us/library/windows/apps/dn912875.aspx)                                                                              | Introduced in Windows 10.0.10240.0 |
| [**ID3D11Device3**](https://msdn.microsoft.com/en-us/library/windows/apps/dn899218.aspx)                                                                                            | Introduced in Windows 10.0.10240.0 |
| [**ID3D11Texture2D1**](https://msdn.microsoft.com/en-us/library/windows/apps/dn899244.aspx)                                                                                      | Introduced in Windows 10.0.10240.0 |
| [**ID3D11Texture3D1**](https://msdn.microsoft.com/en-us/library/windows/apps/dn899246.aspx)                                                                                      | Introduced in Windows 10.0.10240.0 |
| [**ID3D11DomainShader**](https://msdn.microsoft.com/en-us/library/windows/apps/ff476535.aspx)                                                                                  | Introduced in Windows 10.0.10240.0 |
| [**ID3D11FunctionLinkingGraph**](https://msdn.microsoft.com/en-us/library/windows/apps/dn280535.aspx)                                                                  | Introduced in Windows 10.0.10240.0 |
| [**ID3D11GeometryShader**](https://msdn.microsoft.com/en-us/library/windows/apps/ff476536.aspx)                                                                              | Introduced in Windows 10.0.10240.0 |
| [**ID3D11HullShader**](https://msdn.microsoft.com/en-us/library/windows/apps/ff476537.aspx)                                                                                      | Introduced in Windows 10.0.10240.0 |
| [**ID3D11InfoQueue**](https://msdn.microsoft.com/en-us/library/windows/apps/ff476538.aspx)                                                                                        | Introduced in Windows 10.0.10240.0 |
| [**ID3D11InputLayout**](https://msdn.microsoft.com/en-us/library/windows/apps/ff476575.aspx)                                                                                    | Introduced in Windows 10.0.10240.0 |
| [**ID3D11LibraryReflection**](https://msdn.microsoft.com/en-us/library/windows/apps/dn280554.aspx)                                                                        | Introduced in Windows 10.0.10240.0 |
| [**ID3D11Linker**](https://msdn.microsoft.com/en-us/library/windows/apps/dn280558.aspx)                                                                                              | Introduced in Windows 10.0.10240.0 |
| [**ID3D11LinkingNode**](https://msdn.microsoft.com/en-us/library/windows/apps/dn280562.aspx)                                                                                    | Introduced in Windows 10.0.10240.0 |
| [**ID3D11Module**](https://msdn.microsoft.com/en-us/library/windows/apps/dn280563.aspx)                                                                                              | Introduced in Windows 10.0.10240.0 |
| [**ID3D11ModuleInstance**](https://msdn.microsoft.com/en-us/library/windows/apps/dn280564.aspx)                                                                              | Introduced in Windows 10.0.10240.0 |
| [**ID3D11On12Device**](https://www.bing.com/search?q=ID3D11On12Device)                                                                   | Introduced in Windows 10.0.10240.0 |
| [**ID3D11PixelShader**](https://msdn.microsoft.com/en-us/library/windows/apps/ff476576.aspx)                                                                                    | Introduced in Windows 10.0.10240.0 |
| [**ID3D11Predicate**](https://msdn.microsoft.com/en-us/library/windows/apps/ff476577.aspx)                                                                                        | Introduced in Windows 10.0.10240.0 |
| [**ID3D11Query**](https://msdn.microsoft.com/en-us/library/windows/apps/ff476578.aspx)                                                                                                | Introduced in Windows 10.0.10240.0 |
| [**ID3D11Query1**](https://msdn.microsoft.com/en-us/library/windows/apps/dn899236.aspx)                                                                                              | Introduced in Windows 10.0.10240.0 |
| [**ID3D11RasterizerState**](https://msdn.microsoft.com/en-us/library/windows/apps/ff476580.aspx)                                                                            | Introduced in Windows 10.0.10240.0 |
| [**ID3D11RasterizerState1**](https://msdn.microsoft.com/en-us/library/windows/apps/hh446828.aspx)                                                                          | Introduced in Windows 10.0.10240.0 |
| [**ID3D11RasterizerState2**](https://msdn.microsoft.com/en-us/library/windows/apps/dn899238.aspx)                                                                          | Introduced in Windows 10.0.10240.0 |
| [**ID3D11RefDefaultTrackingOptions**](https://msdn.microsoft.com/en-us/library/windows/apps/hh446832.aspx)                                                        | Introduced in Windows 10.0.10240.0 |
| [**ID3D11RefTrackingOptions**](https://msdn.microsoft.com/en-us/library/windows/apps/hh446836.aspx)                                                                      | Introduced in Windows 10.0.10240.0 |
| [**ID3D11RenderTargetView**](https://msdn.microsoft.com/en-us/library/windows/apps/ff476582.aspx)                                                                          | Introduced in Windows 10.0.10240.0 |
| [**ID3D11RenderTargetView1**](https://msdn.microsoft.com/en-us/library/windows/apps/dn899240.aspx)                                                                        | Introduced in Windows 10.0.10240.0 |
| [**ID3D11Resource**](https://msdn.microsoft.com/en-us/library/windows/apps/ff476584.aspx)                                                                                          | Introduced in Windows 10.0.10240.0 |
| [**ID3D11SamplerState**](https://msdn.microsoft.com/en-us/library/windows/apps/ff476588.aspx)                                                                                  | Introduced in Windows 10.0.10240.0 |
| [**ID3D11ShaderReflection**](https://msdn.microsoft.com/en-us/library/windows/apps/ff476590.aspx)                                                                          | Introduced in Windows 10.0.10240.0 |
| [**ID3D11ShaderReflectionConstantBuffer**](https://msdn.microsoft.com/en-us/library/windows/apps/ff476591.aspx)                                              | Introduced in Windows 10.0.10240.0 |
| [**ID3D11ShaderReflectionType**](https://msdn.microsoft.com/en-us/library/windows/apps/ff476595.aspx)                                                                  | Introduced in Windows 10.0.10240.0 |
| [**ID3D11ShaderReflectionVariable**](https://msdn.microsoft.com/en-us/library/windows/apps/ff476607.aspx)                                                          | Introduced in Windows 10.0.10240.0 |
| [**ID3D11ShaderResourceView**](https://msdn.microsoft.com/en-us/library/windows/apps/ff476628.aspx)                                                                      | Introduced in Windows 10.0.10240.0 |
| [**ID3D11ShaderResourceView1**](https://msdn.microsoft.com/en-us/library/windows/apps/dn899242.aspx)                                                                    | Introduced in Windows 10.0.10240.0 |
| [**ID3D11ShaderTrace**](https://msdn.microsoft.com/en-us/library/windows/apps/hh446840.aspx)                                                                                    | Introduced in Windows 10.0.10240.0 |
| [**ID3D11ShaderTraceFactory**](https://msdn.microsoft.com/en-us/library/windows/apps/hh446842.aspx)                                                                      | Introduced in Windows 10.0.10240.0 |
| [**ID3D11Texture1D**](https://msdn.microsoft.com/en-us/library/windows/apps/ff476633.aspx)                                                                                        | Introduced in Windows 10.0.10240.0 |
| [**ID3D11Texture2D**](https://msdn.microsoft.com/en-us/library/windows/apps/ff476635.aspx)                                                                                        | Introduced in Windows 10.0.10240.0 |
| [**ID3D11Texture3D**](https://msdn.microsoft.com/en-us/library/windows/apps/ff476637.aspx)                                                                                        | Introduced in Windows 10.0.10240.0 |
| [**ID3D11TracingDevice**](https://msdn.microsoft.com/en-us/library/windows/apps/hh446868.aspx)                                                                                | Introduced in Windows 10.0.10240.0 |
| [**ID3D11UnorderedAccessView**](https://msdn.microsoft.com/en-us/library/windows/apps/ff476639.aspx)                                                                    | Introduced in Windows 10.0.10240.0 |
| [**ID3D11UnorderedAccessView1**](https://msdn.microsoft.com/en-us/library/windows/apps/dn899248.aspx)                                                                  | Introduced in Windows 10.0.10240.0 |
| [**ID3D11VertexShader**](https://msdn.microsoft.com/en-us/library/windows/apps/ff476641.aspx)                                                                                  | Introduced in Windows 10.0.10240.0 |
| [**ID3D11VideoContext**](https://msdn.microsoft.com/en-us/library/windows/apps/hh447703.aspx)                                                                                          | Introduced in Windows 10.0.10240.0 |
| [**ID3D11VideoContext1**](https://msdn.microsoft.com/en-us/library/windows/apps/dn894126.aspx)                                                                                        | Introduced in Windows 10.0.10240.0 |
| [**ID3D11VideoDecoder**](https://msdn.microsoft.com/en-us/library/windows/apps/hh447766.aspx)                                                                                          | Introduced in Windows 10.0.10240.0 |
| [**ID3D11VideoDecoderOutputView**](https://msdn.microsoft.com/en-us/library/windows/apps/hh447767.aspx)                                                                      | Introduced in Windows 10.0.10240.0 |
| [**ID3D11VideoDevice**](https://msdn.microsoft.com/en-us/library/windows/apps/hh447781.aspx)                                                                                            | Introduced in Windows 10.0.10240.0 |
| [**ID3D11VideoDevice1**](https://msdn.microsoft.com/en-us/library/windows/apps/dn894141.aspx)                                                                                          | Introduced in Windows 10.0.10240.0 |
| [**ID3D11VideoProcessor**](https://msdn.microsoft.com/en-us/library/windows/apps/hh447799.aspx)                                                                                      | Introduced in Windows 10.0.10240.0 |
| [**ID3D11VideoProcessorEnumerator**](https://msdn.microsoft.com/en-us/library/windows/apps/hh447800.aspx)                                                                  | Introduced in Windows 10.0.10240.0 |
| [**ID3D11VideoProcessorEnumerator1**](https://msdn.microsoft.com/en-us/library/windows/apps/dn894146.aspx)                                                                | Introduced in Windows 10.0.10240.0 |
| [**ID3D11VideoProcessorInputView**](https://msdn.microsoft.com/en-us/library/windows/apps/hh447807.aspx)                                                                    | Introduced in Windows 10.0.10240.0 |
| [**ID3D11VideoProcessorOutputView**](https://msdn.microsoft.com/en-us/library/windows/apps/hh447809.aspx)                                                                  | Introduced in Windows 10.0.10240.0 |
| [**ID3D11View**](https://msdn.microsoft.com/en-us/library/windows/apps/ff476642.aspx)                                                                                                  | Introduced in Windows 10.0.10240.0 |
| [**ID3D12CommandAllocator**](https://www.bing.com/search?q=ID3D12CommandAllocator)                                                       | Introduced in Windows 10.0.10240.0 |
| [**ID3D12CommandList**](https://www.bing.com/search?q=ID3D12CommandList)                                                                 | Introduced in Windows 10.0.10240.0 |
| [**ID3D12CommandQueue**](https://www.bing.com/search?q=ID3D12CommandQueue)                                                               | Introduced in Windows 10.0.10240.0 |
| [**ID3D12CommandSignature**](https://www.bing.com/search?q=ID3D12CommandSignature)                                                       | Introduced in Windows 10.0.10240.0 |
| [**ID3D12Debug**](https://www.bing.com/search?q=ID3D12Debug)                                                                             | Introduced in Windows 10.0.10240.0 |
| [**ID3D12DebugCommandList**](https://www.bing.com/search?q=ID3D12DebugCommandList)                                                       | Introduced in Windows 10.0.10240.0 |
| [**ID3D12DebugCommandQueue**](https://www.bing.com/search?q=ID3D12DebugCommandQueue)                                                     | Introduced in Windows 10.0.10240.0 |
| [**ID3D12DebugDevice**](https://www.bing.com/search?q=ID3D12DebugDevice)                                                                 | Introduced in Windows 10.0.10240.0 |
| [**ID3D12DescriptorHeap**](https://www.bing.com/search?q=ID3D12DescriptorHeap)                                                           | Introduced in Windows 10.0.10240.0 |
| [**ID3D12Device**](https://www.bing.com/search?q=ID3D12Device)                                                                           | Introduced in Windows 10.0.10240.0 |
| [**ID3D12DeviceChild**](https://www.bing.com/search?q=ID3D12DeviceChild)                                                                 | Introduced in Windows 10.0.10240.0 |
| [**ID3D12Fence**](https://www.bing.com/search?q=ID3D12Fence)                                                                             | Introduced in Windows 10.0.10240.0 |
| [**ID3D12GraphicsCommandList**](https://www.bing.com/search?q=ID3D12GraphicsCommandList)                                                 | Introduced in Windows 10.0.10240.0 |
| [**ID3D12Heap**](https://www.bing.com/search?q=ID3D12Heap)                                                                               | Introduced in Windows 10.0.10240.0 |
| [**ID3D12InfoQueue**](https://www.bing.com/search?q=ID3D12InfoQueue)                                                                     | Introduced in Windows 10.0.10240.0 |
| [**ID3D12LibraryReflection**](https://www.bing.com/search?q=ID3D12LibraryReflection)                                                     | Introduced in Windows 10.0.10240.0 |
| [**ID3D12Object**](https://www.bing.com/search?q=ID3D12Object)                                                                           | Introduced in Windows 10.0.10240.0 |
| [**ID3D12Pageable**](https://www.bing.com/search?q=ID3D12Pageable)                                                                       | Introduced in Windows 10.0.10240.0 |
| [**ID3D12PipelineState**](https://www.bing.com/search?q=ID3D12PipelineState)                                                             | Introduced in Windows 10.0.10240.0 |
| [**ID3D12QueryHeap**](https://www.bing.com/search?q=ID3D12QueryHeap)                                                                     | Introduced in Windows 10.0.10240.0 |
| [**ID3D12Resource**](https://www.bing.com/search?q=ID3D12Resource)                                                                       | Introduced in Windows 10.0.10240.0 |
| [**ID3D12RootSignature**](https://www.bing.com/search?q=ID3D12RootSignature)                                                             | Introduced in Windows 10.0.10240.0 |
| [**ID3D12RootSignatureDeserializer**](https://www.bing.com/search?q=ID3D12RootSignatureDeserializer)                                     | Introduced in Windows 10.0.10240.0 |
| [**ID3D12ShaderReflection**](https://www.bing.com/search?q=ID3D12ShaderReflection)                                                       | Introduced in Windows 10.0.10240.0 |
| [**ID3DDeviceContextState**](https://msdn.microsoft.com/en-us/library/windows/apps/hh446878.aspx)                                                                          | Introduced in Windows 10.0.10240.0 |
| [**ID3DUserDefinedAnnotation**](https://msdn.microsoft.com/en-us/library/windows/apps/hh446881.aspx)                                                                    | Introduced in Windows 10.0.10240.0 |
| [**IDeviceIoControl**](https://msdn.microsoft.com/en-us/library/windows/apps/hh404258.aspx)                                                                                    | Introduced in Windows 10.0.10240.0 |
| [**IDeviceRequestCompletionCallback**](https://msdn.microsoft.com/en-us/library/windows/apps/hh404262.aspx)                                                    | Introduced in Windows 10.0.10240.0 |
| [**IDirect3DDxgiInterfaceAccess**](https://www.bing.com/search?q=IDirect3DDxgiInterfaceAccess)                                           | Introduced in Windows 10.0.10240.0 |
| [**IDirectWriterLock**](https://msdn.microsoft.com/en-us/library/windows/apps/aa379158.aspx)                                                                                           | Introduced in Windows 10.0.10240.0 |
| [**IDispatch**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221608.aspx)                                                                                                       | Introduced in Windows 10.0.10240.0 |
| [**IDockProvider**](https://msdn.microsoft.com/en-us/library/windows/apps/ee671239.aspx)                                                                                        | Introduced in Windows 10.0.10240.0 |
| [**IDragProvider**](https://msdn.microsoft.com/en-us/library/windows/apps/hh707338.aspx)                                                                                        | Introduced in Windows 10.0.10240.0 |
| [**IDropTargetProvider**](https://msdn.microsoft.com/en-us/library/windows/apps/hh707345.aspx)                                                                            | Introduced in Windows 10.0.10240.0 |
| [**IDvdControl2**](https://msdn.microsoft.com/en-us/library/windows/apps/dd389895.aspx)                                                                                                   | Introduced in Windows 10.0.10240.0 |
| [**IDvdInfo2**](https://msdn.microsoft.com/en-us/library/windows/apps/dd376432.aspx)                                                                                                         | Introduced in Windows 10.0.10240.0 |
| [**IDWriteBitmapRenderTarget**](https://msdn.microsoft.com/en-us/library/windows/apps/dd368165.aspx)                                                                   | Introduced in Windows 10.0.10240.0 |
| [**IDWriteBitmapRenderTarget1**](https://msdn.microsoft.com/en-us/library/windows/apps/hh780398.aspx)                                                                 | Introduced in Windows 10.0.10240.0 |
| [**IDWriteColorGlyphRunEnumerator**](https://msdn.microsoft.com/en-us/library/windows/apps/dn280445.aspx)                                                         | Introduced in Windows 10.0.10240.0 |
| [**IDWriteFactory**](https://msdn.microsoft.com/en-us/library/windows/apps/dd368183.aspx)                                                                                         | Introduced in Windows 10.0.10240.0 |
| [**IDWriteFactory1**](https://msdn.microsoft.com/en-us/library/windows/apps/hh780401.aspx)                                                                                       | Introduced in Windows 10.0.10240.0 |
| [**IDWriteFactory2**](https://msdn.microsoft.com/en-us/library/windows/apps/dn280448.aspx)                                                                                       | Introduced in Windows 10.0.10240.0 |
| [**IDWriteFactory3**](https://msdn.microsoft.com/en-us/library/windows/apps/dn890753.aspx)                                                                                       | Introduced in Windows 10.0.10240.0 |
| [**IDWriteFont**](https://msdn.microsoft.com/en-us/library/windows/apps/dd368213.aspx)                                                                                               | Introduced in Windows 10.0.10240.0 |
| [**IDWriteFont1**](https://msdn.microsoft.com/en-us/library/windows/apps/hh780404.aspx)                                                                                             | Introduced in Windows 10.0.10240.0 |
| [**IDWriteFont2**](https://msdn.microsoft.com/en-us/library/windows/apps/dn280452.aspx)                                                                                             | Introduced in Windows 10.0.10240.0 |
| [**IDWriteFont3**](https://msdn.microsoft.com/en-us/library/windows/apps/dn890766.aspx)                                                                                             | Introduced in Windows 10.0.10240.0 |
| [**IDWriteFontCollection**](https://msdn.microsoft.com/en-us/library/windows/apps/dd368214.aspx)                                                                           | Introduced in Windows 10.0.10240.0 |
| [**IDWriteFontCollection1**](https://msdn.microsoft.com/en-us/library/windows/apps/dn933224.aspx)                                                                         | Introduced in Windows 10.0.10240.0 |
| [**IDWriteFontCollectionLoader**](https://msdn.microsoft.com/en-us/library/windows/apps/dd368215.aspx)                                                               | Introduced in Windows 10.0.10240.0 |
| [**IDWriteFontDownloadListener**](https://msdn.microsoft.com/en-us/library/windows/apps/dn890775.aspx)                                                               | Introduced in Windows 10.0.10240.0 |
| [**IDWriteFontDownloadQueue**](https://msdn.microsoft.com/en-us/library/windows/apps/dn890778.aspx)                                                                     | Introduced in Windows 10.0.10240.0 |
| [**IDWriteFontFace**](https://msdn.microsoft.com/en-us/library/windows/apps/dd370983.aspx)                                                                                       | Introduced in Windows 10.0.10240.0 |
| [**IDWriteFontFace1**](https://msdn.microsoft.com/en-us/library/windows/apps/hh780409.aspx)                                                                                     | Introduced in Windows 10.0.10240.0 |
| [**IDWriteFontFace2**](https://msdn.microsoft.com/en-us/library/windows/apps/dn280454.aspx)                                                                                     | Introduced in Windows 10.0.10240.0 |
| [**IDWriteFontFace3**](https://msdn.microsoft.com/en-us/library/windows/apps/dn894561.aspx)                                                                                     | Introduced in Windows 10.0.10240.0 |
| [**IDWriteFontFaceReference**](https://msdn.microsoft.com/en-us/library/windows/apps/dn894576.aspx)                                                                     | Introduced in Windows 10.0.10240.0 |
| [**IDWriteFontFallback**](https://msdn.microsoft.com/en-us/library/windows/apps/dn280474.aspx)                                                                               | Introduced in Windows 10.0.10240.0 |
| [**IDWriteFontFallbackBuilder**](https://msdn.microsoft.com/en-us/library/windows/apps/dn280476.aspx)                                                                 | Introduced in Windows 10.0.10240.0 |
| [**IDWriteFontFamily**](https://msdn.microsoft.com/en-us/library/windows/apps/dd371042.aspx)                                                                                   | Introduced in Windows 10.0.10240.0 |
| [**IDWriteFontFamily1**](https://msdn.microsoft.com/en-us/library/windows/apps/dn894590.aspx)                                                                                 | Introduced in Windows 10.0.10240.0 |
| [**IDWriteFontFile**](https://msdn.microsoft.com/en-us/library/windows/apps/dd371060.aspx)                                                                                       | Introduced in Windows 10.0.10240.0 |
| [**IDWriteFontFileEnumerator**](https://msdn.microsoft.com/en-us/library/windows/apps/dd371063.aspx)                                                                   | Introduced in Windows 10.0.10240.0 |
| [**IDWriteFontFileLoader**](https://msdn.microsoft.com/en-us/library/windows/apps/dd371075.aspx)                                                                           | Introduced in Windows 10.0.10240.0 |
| [**IDWriteFontFileStream**](https://msdn.microsoft.com/en-us/library/windows/apps/dd371081.aspx)                                                                           | Introduced in Windows 10.0.10240.0 |
| [**IDWriteFontList**](https://msdn.microsoft.com/en-us/library/windows/apps/dd371120.aspx)                                                                                       | Introduced in Windows 10.0.10240.0 |
| [**IDWriteFontList1**](https://msdn.microsoft.com/en-us/library/windows/apps/dn894594.aspx)                                                                                     | Introduced in Windows 10.0.10240.0 |
| [**IDWriteFontSet**](https://msdn.microsoft.com/en-us/library/windows/apps/dn933235.aspx)                                                                                         | Introduced in Windows 10.0.10240.0 |
| [**IDWriteFontSetBuilder**](https://msdn.microsoft.com/en-us/library/windows/apps/dn933236.aspx)                                                                           | Introduced in Windows 10.0.10240.0 |
| [**IDWriteGdiInterop**](https://msdn.microsoft.com/en-us/library/windows/apps/dd371172.aspx)                                                                                   | Introduced in Windows 10.0.10240.0 |
| [**IDWriteGdiInterop1**](https://msdn.microsoft.com/en-us/library/windows/apps/dn958415.aspx)                                                                                 | Introduced in Windows 10.0.10240.0 |
| [**IDWriteGlyphRunAnalysis**](https://msdn.microsoft.com/en-us/library/windows/apps/dd371188.aspx)                                                                       | Introduced in Windows 10.0.10240.0 |
| [**IDWriteInlineObject**](https://msdn.microsoft.com/en-us/library/windows/apps/dd371221.aspx)                                                                               | Introduced in Windows 10.0.10240.0 |
| [**IDWriteLocalFontFileLoader**](https://msdn.microsoft.com/en-us/library/windows/apps/dd371238.aspx)                                                                 | Introduced in Windows 10.0.10240.0 |
| [**IDWriteLocalizedStrings**](https://msdn.microsoft.com/en-us/library/windows/apps/dd371250.aspx)                                                                       | Introduced in Windows 10.0.10240.0 |
| [**IDWriteNumberSubstitution**](https://msdn.microsoft.com/en-us/library/windows/apps/dd371271.aspx)                                                                   | Introduced in Windows 10.0.10240.0 |
| [**IDWritePixelSnapping**](https://msdn.microsoft.com/en-us/library/windows/apps/dd371274.aspx)                                                                             | Introduced in Windows 10.0.10240.0 |
| [**IDWriteRenderingParams**](https://msdn.microsoft.com/en-us/library/windows/apps/dd371285.aspx)                                                                         | Introduced in Windows 10.0.10240.0 |
| [**IDWriteRenderingParams1**](https://msdn.microsoft.com/en-us/library/windows/apps/hh780422.aspx)                                                                       | Introduced in Windows 10.0.10240.0 |
| [**IDWriteRenderingParams2**](https://msdn.microsoft.com/en-us/library/windows/apps/dn900387.aspx)                                                                       | Introduced in Windows 10.0.10240.0 |
| [**IDWriteRenderingParams3**](https://msdn.microsoft.com/en-us/library/windows/apps/dn900389.aspx)                                                                       | Introduced in Windows 10.0.10240.0 |
| [**IDWriteStringList**](https://msdn.microsoft.com/en-us/library/windows/apps/dn958421.aspx)                                                                                   | Introduced in Windows 10.0.10240.0 |
| [**IDWriteTextAnalysisSink**](https://msdn.microsoft.com/en-us/library/windows/apps/dd371303.aspx)                                                                       | Introduced in Windows 10.0.10240.0 |
| [**IDWriteTextAnalysisSink1**](https://msdn.microsoft.com/en-us/library/windows/apps/hh780424.aspx)                                                                     | Introduced in Windows 10.0.10240.0 |
| [**IDWriteTextAnalysisSource**](https://msdn.microsoft.com/en-us/library/windows/apps/dd371318.aspx)                                                                   | Introduced in Windows 10.0.10240.0 |
| [**IDWriteTextAnalysisSource1**](https://msdn.microsoft.com/en-us/library/windows/apps/hh780426.aspx)                                                                 | Introduced in Windows 10.0.10240.0 |
| [**IDWriteTextAnalyzer**](https://msdn.microsoft.com/en-us/library/windows/apps/dd316607.aspx)                                                                               | Introduced in Windows 10.0.10240.0 |
| [**IDWriteTextAnalyzer1**](https://msdn.microsoft.com/en-us/library/windows/apps/hh780428.aspx)                                                                             | Introduced in Windows 10.0.10240.0 |
| [**IDWriteTextAnalyzer2**](https://msdn.microsoft.com/en-us/library/windows/apps/dn280483.aspx)                                                                             | Introduced in Windows 10.0.10240.0 |
| [**IDWriteTextFormat**](https://msdn.microsoft.com/en-us/library/windows/apps/dd316628.aspx)                                                                                   | Introduced in Windows 10.0.10240.0 |
| [**IDWriteTextFormat1**](https://msdn.microsoft.com/en-us/library/windows/apps/dn280485.aspx)                                                                                 | Introduced in Windows 10.0.10240.0 |
| [**IDWriteTextFormat2**](https://msdn.microsoft.com/en-us/library/windows/apps/mt574121.aspx)                                                                                 | Introduced in Windows 10.0.10240.0 |
| [**IDWriteTextLayout**](https://msdn.microsoft.com/en-us/library/windows/apps/dd316718.aspx)                                                                                   | Introduced in Windows 10.0.10240.0 |
| [**IDWriteTextLayout1**](https://msdn.microsoft.com/en-us/library/windows/apps/hh780438.aspx)                                                                                 | Introduced in Windows 10.0.10240.0 |
| [**IDWriteTextLayout2**](https://msdn.microsoft.com/en-us/library/windows/apps/dn280491.aspx)                                                                                 | Introduced in Windows 10.0.10240.0 |
| [**IDWriteTextLayout3**](https://msdn.microsoft.com/en-us/library/windows/apps/dn900405.aspx)                                                                                 | Introduced in Windows 10.0.10240.0 |
| [**IDWriteTextRenderer**](https://msdn.microsoft.com/en-us/library/windows/apps/dd371523.aspx)                                                                               | Introduced in Windows 10.0.10240.0 |
| [**IDWriteTextRenderer1**](https://msdn.microsoft.com/en-us/library/windows/apps/dn280513.aspx)                                                                             | Introduced in Windows 10.0.10240.0 |
| [**IDWriteTypography**](https://msdn.microsoft.com/en-us/library/windows/apps/dd371541.aspx)                                                                                   | Introduced in Windows 10.0.10240.0 |
| [**IDXGIAdapter**](https://msdn.microsoft.com/en-us/library/windows/apps/bb174523.aspx)                                                                                            | Introduced in Windows 10.0.10240.0 |
| [**IDXGIAdapter1**](https://msdn.microsoft.com/en-us/library/windows/apps/ff471329.aspx)                                                                                          | Introduced in Windows 10.0.10240.0 |
| [**IDXGIAdapter2**](https://msdn.microsoft.com/en-us/library/windows/apps/hh404537.aspx)                                                                                          | Introduced in Windows 10.0.10240.0 |
| [**IDXGIAdapter3**](https://msdn.microsoft.com/en-us/library/windows/apps/dn933221.aspx)                                                                                          | Introduced in Windows 10.0.10240.0 |
| [**IDXGIDebug**](https://msdn.microsoft.com/en-us/library/windows/apps/hh780351.aspx)                                                                                                | Introduced in Windows 10.0.10240.0 |
| [**IDXGIDebug1**](https://msdn.microsoft.com/en-us/library/windows/apps/dn457938.aspx)                                                                                              | Introduced in Windows 10.0.10240.0 |
| [**IDXGIDevice**](https://msdn.microsoft.com/en-us/library/windows/apps/bb174527.aspx)                                                                                              | Introduced in Windows 10.0.10240.0 |
| [**IDXGIDevice1**](https://msdn.microsoft.com/en-us/library/windows/apps/ff471331.aspx)                                                                                            | Introduced in Windows 10.0.10240.0 |
| [**IDXGIDevice2**](https://msdn.microsoft.com/en-us/library/windows/apps/hh404543.aspx)                                                                                            | Introduced in Windows 10.0.10240.0 |
| [**IDXGIDevice3**](https://msdn.microsoft.com/en-us/library/windows/apps/dn280345.aspx)                                                                                            | Introduced in Windows 10.0.10240.0 |
| [**IDXGIDeviceSubObject**](https://msdn.microsoft.com/en-us/library/windows/apps/bb174528.aspx)                                                                            | Introduced in Windows 10.0.10240.0 |
| [**IDXGIFactory**](https://msdn.microsoft.com/en-us/library/windows/apps/bb174535.aspx)                                                                                            | Introduced in Windows 10.0.10240.0 |
| [**IDXGIFactory1**](https://msdn.microsoft.com/en-us/library/windows/apps/ff471335.aspx)                                                                                          | Introduced in Windows 10.0.10240.0 |
| [**IDXGIFactory2**](https://msdn.microsoft.com/en-us/library/windows/apps/hh404556.aspx)                                                                                          | Introduced in Windows 10.0.10240.0 |
| [**IDXGIFactory3**](https://msdn.microsoft.com/en-us/library/windows/apps/dn457942.aspx)                                                                                          | Introduced in Windows 10.0.10240.0 |
| [**IDXGIFactory4**](https://msdn.microsoft.com/en-us/library/windows/apps/mt427785.aspx)                                                                                          | Introduced in Windows 10.0.10240.0 |
| [**IDXGIInfoQueue**](https://msdn.microsoft.com/en-us/library/windows/apps/hh780355.aspx)                                                                                        | Introduced in Windows 10.0.10240.0 |
| [**IDXGIKeyedMutex**](https://msdn.microsoft.com/en-us/library/windows/apps/ff471338.aspx)                                                                                      | Introduced in Windows 10.0.10240.0 |
| [**IDXGIObject**](https://msdn.microsoft.com/en-us/library/windows/apps/bb174541.aspx)                                                                                              | Introduced in Windows 10.0.10240.0 |
| [**IDXGIOutput**](https://msdn.microsoft.com/en-us/library/windows/apps/bb174546.aspx)                                                                                              | Introduced in Windows 10.0.10240.0 |
| [**IDXGIOutput1**](https://msdn.microsoft.com/en-us/library/windows/apps/hh404597.aspx)                                                                                            | Introduced in Windows 10.0.10240.0 |
| [**IDXGIOutput2**](https://msdn.microsoft.com/en-us/library/windows/apps/dn280410.aspx)                                                                                            | Introduced in Windows 10.0.10240.0 |
| [**IDXGIOutput3**](https://msdn.microsoft.com/en-us/library/windows/apps/dn903669.aspx)                                                                                            | Introduced in Windows 10.0.10240.0 |
| [**IDXGIOutput4**](https://msdn.microsoft.com/en-us/library/windows/apps/dn903671.aspx)                                                                                            | Introduced in Windows 10.0.10240.0 |
| [**IDXGIResource**](https://msdn.microsoft.com/en-us/library/windows/apps/bb174560.aspx)                                                                                          | Introduced in Windows 10.0.10240.0 |
| [**IDXGIResource1**](https://msdn.microsoft.com/en-us/library/windows/apps/hh404625.aspx)                                                                                        | Introduced in Windows 10.0.10240.0 |
| [**IDXGISurface**](https://msdn.microsoft.com/en-us/library/windows/apps/bb174565.aspx)                                                                                            | Introduced in Windows 10.0.10240.0 |
| [**IDXGISurface1**](https://msdn.microsoft.com/en-us/library/windows/apps/ff471343.aspx)                                                                                          | Introduced in Windows 10.0.10240.0 |
| [**IDXGISurface2**](https://msdn.microsoft.com/en-us/library/windows/apps/hh404628.aspx)                                                                                          | Introduced in Windows 10.0.10240.0 |
| [**IDXGISwapChain**](https://msdn.microsoft.com/en-us/library/windows/apps/bb174569.aspx)                                                                                        | Introduced in Windows 10.0.10240.0 |
| [**IDXGISwapChain1**](https://msdn.microsoft.com/en-us/library/windows/apps/hh404631.aspx)                                                                                      | Introduced in Windows 10.0.10240.0 |
| [**IDXGISwapChain2**](https://msdn.microsoft.com/en-us/library/windows/apps/dn280420.aspx)                                                                                      | Introduced in Windows 10.0.10240.0 |
| [**IDXGISwapChain3**](https://msdn.microsoft.com/en-us/library/windows/apps/dn903673.aspx)                                                                                      | Introduced in Windows 10.0.10240.0 |
| [**IEditionUpgradeHelper**](https://www.bing.com/search?q=IEditionUpgradeHelper)                                                         | Introduced in Windows 10.0.10240.0 |
| [**IEnumCodePage**](https://www.bing.com/search?q=IEnumCodePage)                                                                         | Introduced in Windows 10.0.10240.0 |
| [**IEnumConnectionPoints**](https://msdn.microsoft.com/en-us/library/windows/apps/ms688265.aspx)                                                                                   | Introduced in Windows 10.0.10240.0 |
| [**IEnumConnections**](https://msdn.microsoft.com/en-us/library/windows/apps/ms682237.aspx)                                                                                             | Introduced in Windows 10.0.10240.0 |
| [**IEnumGUID**](https://msdn.microsoft.com/en-us/library/windows/apps/ms682393.aspx)                                                                                                           | Introduced in Windows 10.0.10240.0 |
| [**IEnumITfCompositionView**](https://msdn.microsoft.com/en-us/library/windows/apps/ms538115.aspx)                                                                               | Introduced in Windows 10.0.10240.0 |
| [**IEnumMoniker**](https://msdn.microsoft.com/en-us/library/windows/apps/ms692852.aspx)                                                                                                     | Introduced in Windows 10.0.10240.0 |
| [**IEnumPortableDeviceObjectIDs**](https://msdn.microsoft.com/en-us/library/windows/apps/dd319350.aspx)                                                                  | Introduced in Windows 10.0.10240.0 |
| [**IEnumRfc1766**](https://www.bing.com/search?q=IEnumRfc1766)                                                                           | Introduced in Windows 10.0.10240.0 |
| [**IEnumScript**](https://www.bing.com/search?q=IEnumScript)                                                                             | Introduced in Windows 10.0.10240.0 |
| [**IEnumSpellingError**](https://msdn.microsoft.com/en-us/library/windows/apps/hh869751.aspx)                                                                                        | Introduced in Windows 10.0.10240.0 |
| [**IEnumSTATDATA**](https://msdn.microsoft.com/en-us/library/windows/apps/ms688589.aspx)                                                                                                   | Introduced in Windows 10.0.10240.0 |
| [**IEnumSTATPROPSETSTG**](https://msdn.microsoft.com/en-us/library/windows/apps/aa379184.aspx)                                                                                       | Introduced in Windows 10.0.10240.0 |
| [**IEnumSTATPROPSETSTG**](https://msdn.microsoft.com/en-us/library/windows/apps/aa379184.aspx)                                                                                       | Introduced in Windows 10.0.10240.0 |
| [**IEnumSTATPROPSTG**](https://msdn.microsoft.com/en-us/library/windows/apps/aa379210.aspx)                                                                                             | Introduced in Windows 10.0.10240.0 |
| [**IEnumSTATPROPSTG**](https://msdn.microsoft.com/en-us/library/windows/apps/aa379210.aspx)                                                                                             | Introduced in Windows 10.0.10240.0 |
| [**IEnumSTATSTG**](https://msdn.microsoft.com/en-us/library/windows/apps/aa379217.aspx)                                                                                                     | Introduced in Windows 10.0.10240.0 |
| [**IEnumString**](https://msdn.microsoft.com/en-us/library/windows/apps/ms687257.aspx)                                                                                                       | Introduced in Windows 10.0.10240.0 |
| [**IEnumString**](https://msdn.microsoft.com/en-us/library/windows/apps/ms687257.aspx)                                                                                                       | Introduced in Windows 10.0.10240.0 |
| [**IEnumTfCandidates**](https://msdn.microsoft.com/en-us/library/windows/apps/ms538125.aspx)                                                                                           | Introduced in Windows 10.0.10240.0 |
| [**IEnumTfContexts**](https://msdn.microsoft.com/en-us/library/windows/apps/ms538135.aspx)                                                                                               | Introduced in Windows 10.0.10240.0 |
| [**IEnumTfContextViews**](https://msdn.microsoft.com/en-us/library/windows/apps/ms538144.aspx)                                                                                       | Introduced in Windows 10.0.10240.0 |
| [**IEnumTfDisplayAttributeInfo**](https://msdn.microsoft.com/en-us/library/windows/apps/ms538154.aspx)                                                                       | Introduced in Windows 10.0.10240.0 |
| [**IEnumTfDocumentMgrs**](https://msdn.microsoft.com/en-us/library/windows/apps/ms538164.aspx)                                                                                       | Introduced in Windows 10.0.10240.0 |
| [**IEnumTfFunctionProviders**](https://msdn.microsoft.com/en-us/library/windows/apps/ms538172.aspx)                                                                             | Introduced in Windows 10.0.10240.0 |
| [**IEnumTfInputProcessorProfiles**](https://msdn.microsoft.com/en-us/library/windows/apps/aa380591.aspx)                                                                   | Introduced in Windows 10.0.10240.0 |
| [**IEnumTfProperties**](https://msdn.microsoft.com/en-us/library/windows/apps/ms538218.aspx)                                                                                           | Introduced in Windows 10.0.10240.0 |
| [**IEnumTfPropertyValue**](https://msdn.microsoft.com/en-us/library/windows/apps/ms538230.aspx)                                                                                     | Introduced in Windows 10.0.10240.0 |
| [**IEnumTfRanges**](https://msdn.microsoft.com/en-us/library/windows/apps/ms538241.aspx)                                                                                                   | Introduced in Windows 10.0.10240.0 |
| [**IEnumTfUIElements**](https://msdn.microsoft.com/en-us/library/windows/apps/aa380866.aspx)                                                                                           | Introduced in Windows 10.0.10240.0 |
| [**IEnumUnknown**](https://msdn.microsoft.com/en-us/library/windows/apps/ms683764.aspx)                                                                                                     | Introduced in Windows 10.0.10240.0 |
| [**IEnumUnknown**](https://msdn.microsoft.com/en-us/library/windows/apps/ms683764.aspx)                                                                                                     | Introduced in Windows 10.0.10240.0 |
| [**IEnumVARIANT**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221053.aspx)                                                                                                 | Introduced in Windows 10.0.10240.0 |
| [**IExpandCollapseProvider**](https://msdn.microsoft.com/en-us/library/windows/apps/ee671242.aspx)                                                                    | Introduced in Windows 10.0.10240.0 |
| [**IFillLockBytes**](https://msdn.microsoft.com/en-us/library/windows/apps/aa379224.aspx)                                                                                                 | Introduced in Windows 10.0.10240.0 |
| [**IFindReferenceTargetsCallback**](https://msdn.microsoft.com/en-us/library/windows/apps/jj542493.aspx)                                                                 | Introduced in Windows 10.0.10240.0 |
| [**IGlobalInterfaceTable**](https://msdn.microsoft.com/en-us/library/windows/apps/ms678517.aspx)                                                                                   | Introduced in Windows 10.0.10240.0 |
| [**IGlobalInterfaceTable**](https://msdn.microsoft.com/en-us/library/windows/apps/ms678517.aspx)                                                                                   | Introduced in Windows 10.0.10240.0 |
| [**IGlobalOptions**](https://msdn.microsoft.com/en-us/library/windows/apps/aa344211.aspx)                                                                                                 | Introduced in Windows 10.0.10240.0 |
| [**IGlobalOptions**](https://msdn.microsoft.com/en-us/library/windows/apps/aa344211.aspx)                                                                                                 | Introduced in Windows 10.0.10240.0 |
| [**IGridItemProvider**](https://msdn.microsoft.com/en-us/library/windows/apps/ee671246.aspx)                                                                                | Introduced in Windows 10.0.10240.0 |
| [**IGridProvider**](https://msdn.microsoft.com/en-us/library/windows/apps/ee671252.aspx)                                                                                        | Introduced in Windows 10.0.10240.0 |
| [**IInkD2DRenderer**](https://www.bing.com/search?q=IInkD2DRenderer)                                                                     | Introduced in Windows 10.0.10240.0 |
| [**IInspectable**](https://msdn.microsoft.com/en-us/library/windows/apps/br205821.aspx)                                                                                                   | Introduced in Windows 10.0.10240.0 |
| [**IInvokeProvider**](https://msdn.microsoft.com/en-us/library/windows/apps/ee671256.aspx)                                                                                    | Introduced in Windows 10.0.10240.0 |
| [**IItemContainerProvider**](https://msdn.microsoft.com/en-us/library/windows/apps/ee671258.aspx)                                                                      | Introduced in Windows 10.0.10240.0 |
| [**ILanguageExceptionErrorInfo**](https://msdn.microsoft.com/en-us/library/windows/apps/dn302120.aspx)                                                                     | Introduced in Windows 10.0.10240.0 |
| [**ILayoutStorage**](https://msdn.microsoft.com/en-us/library/windows/apps/aa379232.aspx)                                                                                                 | Introduced in Windows 10.0.10240.0 |
| [**ILegacyIAccessibleProvider**](https://msdn.microsoft.com/en-us/library/windows/apps/ee671260.aspx)                                                              | Introduced in Windows 10.0.10240.0 |
| [**ILockBytes**](https://msdn.microsoft.com/en-us/library/windows/apps/aa379238.aspx)                                                                                                         | Introduced in Windows 10.0.10240.0 |
| [**IMarshal**](https://msdn.microsoft.com/en-us/library/windows/apps/ms688712.aspx)                                                                                                             | Introduced in Windows 10.0.10240.0 |
| [**IMarshal**](https://msdn.microsoft.com/en-us/library/windows/apps/ms688712.aspx)                                                                                                             | Introduced in Windows 10.0.10240.0 |
| [**IMbnConnection**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430368.aspx)                                                                                                 | Introduced in Windows 10.0.10240.0 |
| [**IMbnConnectionEvents**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430375.aspx)                                                                                     | Introduced in Windows 10.0.10240.0 |
| [**IMbnConnectionManager**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430380.aspx)                                                                                   | Introduced in Windows 10.0.10240.0 |
| [**IMbnConnectionManagerEvents**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430381.aspx)                                                                       | Introduced in Windows 10.0.10240.0 |
| [**IMbnDeviceService**](https://msdn.microsoft.com/en-us/library/windows/apps/hh780509.aspx)                                                                                           | Introduced in Windows 10.0.10240.0 |
| [**IMbnDeviceServicesContext**](https://msdn.microsoft.com/en-us/library/windows/apps/hh780510.aspx)                                                                           | Introduced in Windows 10.0.10240.0 |
| [**IMbnDeviceServicesEvents**](https://msdn.microsoft.com/en-us/library/windows/apps/hh780515.aspx)                                                                             | Introduced in Windows 10.0.10240.0 |
| [**IMbnDeviceServicesManager**](https://msdn.microsoft.com/en-us/library/windows/apps/hh780527.aspx)                                                                           | Introduced in Windows 10.0.10240.0 |
| [**IMbnInterface**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430406.aspx)                                                                                                   | Introduced in Windows 10.0.10240.0 |
| [**IMbnInterfaceEvents**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430407.aspx)                                                                                       | Introduced in Windows 10.0.10240.0 |
| [**IMbnInterfaceManager**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430416.aspx)                                                                                     | Introduced in Windows 10.0.10240.0 |
| [**IMbnInterfaceManagerEvents**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430417.aspx)                                                                         | Introduced in Windows 10.0.10240.0 |
| [**IMbnPin**](https://msdn.microsoft.com/en-us/library/windows/apps/dd323109.aspx)                                                                                                               | Introduced in Windows 10.0.10240.0 |
| [**IMbnPinEvents**](https://msdn.microsoft.com/en-us/library/windows/apps/dd323110.aspx)                                                                                                   | Introduced in Windows 10.0.10240.0 |
| [**IMbnPinManager**](https://msdn.microsoft.com/en-us/library/windows/apps/dd323117.aspx)                                                                                                 | Introduced in Windows 10.0.10240.0 |
| [**IMbnPinManagerEvents**](https://msdn.microsoft.com/en-us/library/windows/apps/dd323118.aspx)                                                                                     | Introduced in Windows 10.0.10240.0 |
| [**IMbnRegistration**](https://msdn.microsoft.com/en-us/library/windows/apps/dd323142.aspx)                                                                                             | Introduced in Windows 10.0.10240.0 |
| [**IMbnRegistrationEvents**](https://msdn.microsoft.com/en-us/library/windows/apps/dd323143.aspx)                                                                                 | Introduced in Windows 10.0.10240.0 |
| [**IMetaDataAssemblyImport**](https://msdn.microsoft.com/en-us/library/windows/apps/hh870550.aspx)                                                                             | Introduced in Windows 10.0.10240.0 |
| [**IMetaDataDispenser**](https://msdn.microsoft.com/en-us/library/windows/apps/hh870566.aspx)                                                                                       | Introduced in Windows 10.0.10240.0 |
| [**IMetaDataDispenserEx**](https://msdn.microsoft.com/en-us/library/windows/apps/hh870567.aspx)                                                                                   | Introduced in Windows 10.0.10240.0 |
| [**IMetaDataImport**](https://msdn.microsoft.com/en-us/library/windows/apps/hh870577.aspx)                                                                                             | Introduced in Windows 10.0.10240.0 |
| [**IMetaDataImport2**](https://msdn.microsoft.com/en-us/library/windows/apps/hh870578.aspx)                                                                                           | Introduced in Windows 10.0.10240.0 |
| [**IMetaDataTables**](https://msdn.microsoft.com/en-us/library/windows/apps/hh870643.aspx)                                                                                             | Introduced in Windows 10.0.10240.0 |
| [**IMetaDataTables2**](https://msdn.microsoft.com/en-us/library/windows/apps/hh870644.aspx)                                                                                           | Introduced in Windows 10.0.10240.0 |
| [**IMF2DBuffer**](https://msdn.microsoft.com/en-us/library/windows/apps/ms699894.aspx)                                                                                                        | Introduced in Windows 10.0.10240.0 |
| [**IMF2DBuffer2**](https://msdn.microsoft.com/en-us/library/windows/apps/hh447827.aspx)                                                                                                      | Introduced in Windows 10.0.10240.0 |
| [**IMFActivate**](https://msdn.microsoft.com/en-us/library/windows/apps/ms703039.aspx)                                                                                                        | Introduced in Windows 10.0.10240.0 |
| [**IMFAsyncCallback**](https://msdn.microsoft.com/en-us/library/windows/apps/ms699856.aspx)                                                                                              | Introduced in Windows 10.0.10240.0 |
| [**IMFAsyncResult**](https://msdn.microsoft.com/en-us/library/windows/apps/ms700196.aspx)                                                                                                  | Introduced in Windows 10.0.10240.0 |
| [**IMFAttributes**](https://msdn.microsoft.com/en-us/library/windows/apps/ms704598.aspx)                                                                                                    | Introduced in Windows 10.0.10240.0 |
| [**IMFByteStream**](https://msdn.microsoft.com/en-us/library/windows/apps/ms698720.aspx)                                                                                                    | Introduced in Windows 10.0.10240.0 |
| [**IMFByteStreamBuffering**](https://msdn.microsoft.com/en-us/library/windows/apps/aa372548.aspx)                                                                                  | Introduced in Windows 10.0.10240.0 |
| [**IMFByteStreamCacheControl**](https://msdn.microsoft.com/en-us/library/windows/apps/dd368785.aspx)                                                                            | Introduced in Windows 10.0.10240.0 |
| [**IMFByteStreamCacheControl2**](https://msdn.microsoft.com/en-us/library/windows/apps/hh447830.aspx)                                                                          | Introduced in Windows 10.0.10240.0 |
| [**IMFByteStreamTimeSeek**](https://msdn.microsoft.com/en-us/library/windows/apps/hh447836.aspx)                                                                                    | Introduced in Windows 10.0.10240.0 |
| [**IMFClock**](https://msdn.microsoft.com/en-us/library/windows/apps/ms696248.aspx)                                                                                                              | Introduced in Windows 10.0.10240.0 |
| [**IMFClockStateSink**](https://msdn.microsoft.com/en-us/library/windows/apps/ms701593.aspx)                                                                                            | Introduced in Windows 10.0.10240.0 |
| [**IMFCollection**](https://msdn.microsoft.com/en-us/library/windows/apps/ms705661.aspx)                                                                                                    | Introduced in Windows 10.0.10240.0 |
| [**IMFContentDecryptorContext**](https://msdn.microsoft.com/en-us/library/windows/apps/mt219182.aspx)                                                                          | Introduced in Windows 10.0.10240.0 |
| [**IMFContentProtectionDevice**](https://msdn.microsoft.com/en-us/library/windows/apps/mt219184.aspx)                                                                          | Introduced in Windows 10.0.10240.0 |
| [**IMFDXGIBuffer**](https://msdn.microsoft.com/en-us/library/windows/apps/hh447901.aspx)                                                                                                    | Introduced in Windows 10.0.10240.0 |
| [**IMFDXGIDeviceManager**](https://msdn.microsoft.com/en-us/library/windows/apps/hh447906.aspx)                                                                                      | Introduced in Windows 10.0.10240.0 |
| [**IMFDXGIDeviceManagerSource**](https://msdn.microsoft.com/en-us/library/windows/apps/dn280687.aspx)                                                                          | Introduced in Windows 10.0.10240.0 |
| [**IMFGetService**](https://msdn.microsoft.com/en-us/library/windows/apps/ms694261.aspx)                                                                                                    | Introduced in Windows 10.0.10240.0 |
| [**IMFInputTrustAuthority**](https://msdn.microsoft.com/en-us/library/windows/apps/ms697500.aspx)                                                                                  | Introduced in Windows 10.0.10240.0 |
| [**IMFMediaBuffer**](https://msdn.microsoft.com/en-us/library/windows/apps/ms696261.aspx)                                                                                                  | Introduced in Windows 10.0.10240.0 |
| [**IMFMediaEngine**](https://msdn.microsoft.com/en-us/library/windows/apps/hh447918.aspx)                                                                                                  | Introduced in Windows 10.0.10240.0 |
| [**IMFMediaEngineClassFactory**](https://msdn.microsoft.com/en-us/library/windows/apps/hh447919.aspx)                                                                          | Introduced in Windows 10.0.10240.0 |
| [**IMFMediaEngineEx**](https://msdn.microsoft.com/en-us/library/windows/apps/hh447923.aspx)                                                                                              | Introduced in Windows 10.0.10240.0 |
| [**IMFMediaEngineExtension**](https://msdn.microsoft.com/en-us/library/windows/apps/hh447924.aspx)                                                                                | Introduced in Windows 10.0.10240.0 |
| [**IMFMediaEngineNotify**](https://msdn.microsoft.com/en-us/library/windows/apps/hh447962.aspx)                                                                                      | Introduced in Windows 10.0.10240.0 |
| [**IMFMediaEngineProtectedContent**](https://msdn.microsoft.com/en-us/library/windows/apps/hh447964.aspx)                                                                  | Introduced in Windows 10.0.10240.0 |
| [**IMFMediaEngineSrcElements**](https://msdn.microsoft.com/en-us/library/windows/apps/hh447971.aspx)                                                                            | Introduced in Windows 10.0.10240.0 |
| [**IMFMediaError**](https://msdn.microsoft.com/en-us/library/windows/apps/hh448022.aspx)                                                                                                    | Introduced in Windows 10.0.10240.0 |
| [**IMFMediaEvent**](https://msdn.microsoft.com/en-us/library/windows/apps/ms702249.aspx)                                                                                                    | Introduced in Windows 10.0.10240.0 |
| [**IMFMediaEventGenerator**](https://msdn.microsoft.com/en-us/library/windows/apps/ms701755.aspx)                                                                                  | Introduced in Windows 10.0.10240.0 |
| [**IMFMediaEventQueue**](https://msdn.microsoft.com/en-us/library/windows/apps/ms704617.aspx)                                                                                          | Introduced in Windows 10.0.10240.0 |
| [**IMFMediaSink**](https://msdn.microsoft.com/en-us/library/windows/apps/ms694262.aspx)                                                                                                      | Introduced in Windows 10.0.10240.0 |
| [**IMFMediaSinkPreroll**](https://msdn.microsoft.com/en-us/library/windows/apps/ms699832.aspx)                                                                                        | Introduced in Windows 10.0.10240.0 |
| [**IMFMediaSource**](https://msdn.microsoft.com/en-us/library/windows/apps/ms700189.aspx)                                                                                                  | Introduced in Windows 10.0.10240.0 |
| [**IMFMediaSourceEx**](https://msdn.microsoft.com/en-us/library/windows/apps/hh448029.aspx)                                                                                              | Introduced in Windows 10.0.10240.0 |
| [**IMFMediaStream**](https://msdn.microsoft.com/en-us/library/windows/apps/ms697561.aspx)                                                                                                  | Introduced in Windows 10.0.10240.0 |
| [**IMFMediaStreamSourceSampleRequest**](https://msdn.microsoft.com/en-us/library/windows/apps/dn280741.aspx)                                                            | Introduced in Windows 10.0.10240.0 |
| [**IMFMediaTimeRange**](https://msdn.microsoft.com/en-us/library/windows/apps/hh448033.aspx)                                                                                            | Introduced in Windows 10.0.10240.0 |
| [**IMFMediaType**](https://msdn.microsoft.com/en-us/library/windows/apps/ms704850.aspx)                                                                                                      | Introduced in Windows 10.0.10240.0 |
| [**IMFMediaTypeHandler**](https://msdn.microsoft.com/en-us/library/windows/apps/ms697311.aspx)                                                                                        | Introduced in Windows 10.0.10240.0 |
| [**IMFMetadata**](https://msdn.microsoft.com/en-us/library/windows/apps/ms696970.aspx)                                                                                                        | Introduced in Windows 10.0.10240.0 |
| [**IMFMetadataProvider**](https://msdn.microsoft.com/en-us/library/windows/apps/ms705606.aspx)                                                                                        | Introduced in Windows 10.0.10240.0 |
| [**IMFOutputPolicy**](https://msdn.microsoft.com/en-us/library/windows/apps/ms698985.aspx)                                                                                                | Introduced in Windows 10.0.10240.0 |
| [**IMFOutputSchema**](https://msdn.microsoft.com/en-us/library/windows/apps/ms703800.aspx)                                                                                                | Introduced in Windows 10.0.10240.0 |
| [**IMFOutputTrustAuthority**](https://msdn.microsoft.com/en-us/library/windows/apps/ms695254.aspx)                                                                                | Introduced in Windows 10.0.10240.0 |
| [**IMFPMPClientApp**](https://msdn.microsoft.com/en-us/library/windows/apps/jj128316.aspx)                                                                                                | Introduced in Windows 10.0.10240.0 |
| [**IMFPMPHostApp**](https://msdn.microsoft.com/en-us/library/windows/apps/jj128318.aspx)                                                                                                    | Introduced in Windows 10.0.10240.0 |
| [**IMFPresentationClock**](https://msdn.microsoft.com/en-us/library/windows/apps/ms701581.aspx)                                                                                      | Introduced in Windows 10.0.10240.0 |
| [**IMFPresentationDescriptor**](https://msdn.microsoft.com/en-us/library/windows/apps/ms703990.aspx)                                                                            | Introduced in Windows 10.0.10240.0 |
| [**IMFPresentationTimeSource**](https://msdn.microsoft.com/en-us/library/windows/apps/ms704711.aspx)                                                                            | Introduced in Windows 10.0.10240.0 |
| [**IMFProtectedEnvironmentAccess**](https://msdn.microsoft.com/en-us/library/windows/apps/hh448045.aspx)                                                                    | Introduced in Windows 10.0.10240.0 |
| [**IMFQualityAdvise**](https://msdn.microsoft.com/en-us/library/windows/apps/ms695241.aspx)                                                                                              | Introduced in Windows 10.0.10240.0 |
| [**IMFQualityAdvise2**](https://msdn.microsoft.com/en-us/library/windows/apps/dd743249.aspx)                                                                                            | Introduced in Windows 10.0.10240.0 |
| [**IMFQualityAdviseLimits**](https://msdn.microsoft.com/en-us/library/windows/apps/dd374511.aspx)                                                                                  | Introduced in Windows 10.0.10240.0 |
| [**IMFRateControl**](https://msdn.microsoft.com/en-us/library/windows/apps/ms697193.aspx)                                                                                                  | Introduced in Windows 10.0.10240.0 |
| [**IMFRateSupport**](https://msdn.microsoft.com/en-us/library/windows/apps/ms701858.aspx)                                                                                                  | Introduced in Windows 10.0.10240.0 |
| [**IMFReadWriteClassFactory**](https://msdn.microsoft.com/en-us/library/windows/apps/dd374514.aspx)                                                                              | Introduced in Windows 10.0.10240.0 |
| [**IMFRealTimeClientEx**](https://msdn.microsoft.com/en-us/library/windows/apps/hh448047.aspx)                                                                                        | Introduced in Windows 10.0.10240.0 |
| [**IMFSample**](https://msdn.microsoft.com/en-us/library/windows/apps/ms702192.aspx)                                                                                                            | Introduced in Windows 10.0.10240.0 |
| [**IMFSampleOutputStream**](https://msdn.microsoft.com/en-us/library/windows/apps/hh448051.aspx)                                                                                    | Introduced in Windows 10.0.10240.0 |
| [**IMFSampleProtection**](https://msdn.microsoft.com/en-us/library/windows/apps/ms703018.aspx)                                                                                        | Introduced in Windows 10.0.10240.0 |
| [**IMFSchemeHandler**](https://msdn.microsoft.com/en-us/library/windows/apps/ms701638.aspx)                                                                                              | Introduced in Windows 10.0.10240.0 |
| [**IMFSeekInfo**](https://msdn.microsoft.com/en-us/library/windows/apps/hh448054.aspx)                                                                                                        | Introduced in Windows 10.0.10240.0 |
| [**IMFShutdown**](https://msdn.microsoft.com/en-us/library/windows/apps/ms703054.aspx)                                                                                                        | Introduced in Windows 10.0.10240.0 |
| [**IMFSignedLibrary**](https://msdn.microsoft.com/en-us/library/windows/apps/hh448058.aspx)                                                                                              | Introduced in Windows 10.0.10240.0 |
| [**IMFSinkWriter**](https://msdn.microsoft.com/en-us/library/windows/apps/dd374642.aspx)                                                                                                    | Introduced in Windows 10.0.10240.0 |
| [**IMFSinkWriterCallback**](https://msdn.microsoft.com/en-us/library/windows/apps/dd374643.aspx)                                                                                    | Introduced in Windows 10.0.10240.0 |
| [**IMFSinkWriterCallback2**](https://msdn.microsoft.com/en-us/library/windows/apps/dn949415.aspx)                                                                                  | Introduced in Windows 10.0.10240.0 |
| [**IMFSinkWriterEx**](https://msdn.microsoft.com/en-us/library/windows/apps/hh448060.aspx)                                                                                                | Introduced in Windows 10.0.10240.0 |
| [**IMFSinkWriterEncoderConfig**](https://msdn.microsoft.com/en-us/library/windows/apps/dn302046.aspx)                                                                          | Introduced in Windows 10.0.10240.0 |
| [**IMFSourceReader**](https://msdn.microsoft.com/en-us/library/windows/apps/dd374655.aspx)                                                                                                | Introduced in Windows 10.0.10240.0 |
| [**IMFSourceReaderCallback**](https://msdn.microsoft.com/en-us/library/windows/apps/dd374656.aspx)                                                                                | Introduced in Windows 10.0.10240.0 |
| [**IMFSourceReaderCallback2**](https://msdn.microsoft.com/en-us/library/windows/apps/dn949418.aspx)                                                                              | Introduced in Windows 10.0.10240.0 |
| [**IMFSourceReaderEx**](https://msdn.microsoft.com/en-us/library/windows/apps/hh448062.aspx)                                                                                            | Introduced in Windows 10.0.10240.0 |
| [**IMFSourceResolver**](https://msdn.microsoft.com/en-us/library/windows/apps/ms694009.aspx)                                                                                            | Introduced in Windows 10.0.10240.0 |
| [**IMFStreamDescriptor**](https://msdn.microsoft.com/en-us/library/windows/apps/ms701622.aspx)                                                                                        | Introduced in Windows 10.0.10240.0 |
| [**IMFStreamingSinkConfig**](https://msdn.microsoft.com/en-us/library/windows/apps/dd374676.aspx)                                                                                  | Introduced in Windows 10.0.10240.0 |
| [**IMFStreamSink**](https://msdn.microsoft.com/en-us/library/windows/apps/ms705657.aspx)                                                                                                    | Introduced in Windows 10.0.10240.0 |
| [**IMFSystemId**](https://msdn.microsoft.com/en-us/library/windows/apps/hh448067.aspx)                                                                                                        | Introduced in Windows 10.0.10240.0 |
| [**IMFTrackedSample**](https://msdn.microsoft.com/en-us/library/windows/apps/ms697026.aspx)                                                                                              | Introduced in Windows 10.0.10240.0 |
| [**IMFTransform**](https://msdn.microsoft.com/en-us/library/windows/apps/ms696260.aspx)                                                                                                      | Introduced in Windows 10.0.10240.0 |
| [**IMFTrustedInput**](https://msdn.microsoft.com/en-us/library/windows/apps/ms697279.aspx)                                                                                                | Introduced in Windows 10.0.10240.0 |
| [**IMFTrustedOutput**](https://msdn.microsoft.com/en-us/library/windows/apps/ms694305.aspx)                                                                                              | Introduced in Windows 10.0.10240.0 |
| [**IMFVideoSampleAllocator**](https://msdn.microsoft.com/en-us/library/windows/apps/aa473823.aspx)                                                                                | Introduced in Windows 10.0.10240.0 |
| [**IMFVideoSampleAllocatorCallback**](https://msdn.microsoft.com/en-us/library/windows/apps/dd374900.aspx)                                                                | Introduced in Windows 10.0.10240.0 |
| [**IMFVideoSampleAllocatorEx**](https://msdn.microsoft.com/en-us/library/windows/apps/hh448076.aspx)                                                                            | Introduced in Windows 10.0.10240.0 |
| [**IMFVideoSampleAllocatorNotify**](https://msdn.microsoft.com/en-us/library/windows/apps/dd374906.aspx)                                                                    | Introduced in Windows 10.0.10240.0 |
| [**IMFVideoSampleAllocatorNotifyEx**](https://msdn.microsoft.com/en-us/library/windows/apps/mt627756.aspx)                                                                | Introduced in Windows 10.0.10240.0 |
| [**IMFVideoProcessorControl**](https://msdn.microsoft.com/en-us/library/windows/apps/hh448069.aspx)                                                                              | Introduced in Windows 10.0.10240.0 |
| [**IMFVideoProcessorControl2**](https://msdn.microsoft.com/en-us/library/windows/apps/dn800741.aspx)                                                                            | Introduced in Windows 10.0.10240.0 |
| [**IMLangConvertCharset**](https://www.bing.com/search?q=IMLangConvertCharset)                                                           | Introduced in Windows 10.0.10240.0 |
| [**IMultiLanguage**](https://www.bing.com/search?q=IMultiLanguage)                                                                       | Introduced in Windows 10.0.10240.0 |
| [**IMultiLanguage2**](https://www.bing.com/search?q=IMultiLanguage2)                                                                     | Introduced in Windows 10.0.10240.0 |
| [**IMultipleViewProvider**](https://msdn.microsoft.com/en-us/library/windows/apps/ee671296.aspx)                                                                        | Introduced in Windows 10.0.10240.0 |
| [**IMultiQI**](https://msdn.microsoft.com/en-us/library/windows/apps/ms683863.aspx)                                                                                                             | Introduced in Windows 10.0.10240.0 |
| [**IMultiQI**](https://msdn.microsoft.com/en-us/library/windows/apps/ms683863.aspx)                                                                                                             | Introduced in Windows 10.0.10240.0 |
| [**INoMarshal**](https://msdn.microsoft.com/en-us/library/windows/apps/hh802477.aspx)                                                                                                         | Introduced in Windows 10.0.10240.0 |
| [**INoMarshal**](https://msdn.microsoft.com/en-us/library/windows/apps/hh802477.aspx)                                                                                                         | Introduced in Windows 10.0.10240.0 |
| [**IObjectModelProvider**](https://msdn.microsoft.com/en-us/library/windows/apps/hh448776.aspx)                                                                          | Introduced in Windows 10.0.10240.0 |
| [**IOpcCertificateEnumerator**](https://msdn.microsoft.com/en-us/library/windows/apps/dd368258.aspx)                                                                           | Introduced in Windows 10.0.10240.0 |
| [**IOpcCertificateSet**](https://msdn.microsoft.com/en-us/library/windows/apps/dd368269.aspx)                                                                                         | Introduced in Windows 10.0.10240.0 |
| [**IOpcDigitalSignature**](https://msdn.microsoft.com/en-us/library/windows/apps/dd368278.aspx)                                                                                     | Introduced in Windows 10.0.10240.0 |
| [**IOpcDigitalSignatureEnumerator**](https://msdn.microsoft.com/en-us/library/windows/apps/dd368280.aspx)                                                                 | Introduced in Windows 10.0.10240.0 |
| [**IOpcDigitalSignatureManager**](https://msdn.microsoft.com/en-us/library/windows/apps/dd368288.aspx)                                                                       | Introduced in Windows 10.0.10240.0 |
| [**IOpcFactory**](https://msdn.microsoft.com/en-us/library/windows/apps/dd370991.aspx)                                                                                                       | Introduced in Windows 10.0.10240.0 |
| [**IOpcPackage**](https://msdn.microsoft.com/en-us/library/windows/apps/dd371025.aspx)                                                                                                       | Introduced in Windows 10.0.10240.0 |
| [**IOpcPart**](https://msdn.microsoft.com/en-us/library/windows/apps/dd371038.aspx)                                                                                                             | Introduced in Windows 10.0.10240.0 |
| [**IOpcPartEnumerator**](https://msdn.microsoft.com/en-us/library/windows/apps/dd371043.aspx)                                                                                         | Introduced in Windows 10.0.10240.0 |
| [**IOpcPartSet**](https://msdn.microsoft.com/en-us/library/windows/apps/dd371062.aspx)                                                                                                       | Introduced in Windows 10.0.10240.0 |
| [**IOpcPartUri**](https://msdn.microsoft.com/en-us/library/windows/apps/dd371083.aspx)                                                                                                       | Introduced in Windows 10.0.10240.0 |
| [**IOpcRelationship**](https://msdn.microsoft.com/en-us/library/windows/apps/dd371131.aspx)                                                                                             | Introduced in Windows 10.0.10240.0 |
| [**IOpcRelationshipEnumerator**](https://msdn.microsoft.com/en-us/library/windows/apps/dd371135.aspx)                                                                         | Introduced in Windows 10.0.10240.0 |
| [**IOpcRelationshipSelector**](https://msdn.microsoft.com/en-us/library/windows/apps/dd371151.aspx)                                                                             | Introduced in Windows 10.0.10240.0 |
| [**IOpcRelationshipSelectorEnumerator**](https://msdn.microsoft.com/en-us/library/windows/apps/dd371154.aspx)                                                         | Introduced in Windows 10.0.10240.0 |
| [**IOpcRelationshipSelectorSet**](https://msdn.microsoft.com/en-us/library/windows/apps/dd371169.aspx)                                                                       | Introduced in Windows 10.0.10240.0 |
| [**IOpcRelationshipSet**](https://msdn.microsoft.com/en-us/library/windows/apps/dd371217.aspx)                                                                                       | Introduced in Windows 10.0.10240.0 |
| [**IOpcSignatureCustomObject**](https://msdn.microsoft.com/en-us/library/windows/apps/dd316546.aspx)                                                                           | Introduced in Windows 10.0.10240.0 |
| [**IOpcSignatureCustomObjectEnumerator**](https://msdn.microsoft.com/en-us/library/windows/apps/dd316548.aspx)                                                       | Introduced in Windows 10.0.10240.0 |
| [**IOpcSignatureCustomObjectSet**](https://msdn.microsoft.com/en-us/library/windows/apps/dd316560.aspx)                                                                     | Introduced in Windows 10.0.10240.0 |
| [**IOpcSignaturePartReference**](https://msdn.microsoft.com/en-us/library/windows/apps/dd316570.aspx)                                                                         | Introduced in Windows 10.0.10240.0 |
| [**IOpcSignaturePartReferenceEnumerator**](https://msdn.microsoft.com/en-us/library/windows/apps/dd316571.aspx)                                                     | Introduced in Windows 10.0.10240.0 |
| [**IOpcSignaturePartReferenceSet**](https://msdn.microsoft.com/en-us/library/windows/apps/dd316585.aspx)                                                                   | Introduced in Windows 10.0.10240.0 |
| [**IOpcSignatureReference**](https://msdn.microsoft.com/en-us/library/windows/apps/dd316612.aspx)                                                                                 | Introduced in Windows 10.0.10240.0 |
| [**IOpcSignatureReferenceEnumerator**](https://msdn.microsoft.com/en-us/library/windows/apps/dd316615.aspx)                                                             | Introduced in Windows 10.0.10240.0 |
| [**IOpcSignatureReferenceSet**](https://msdn.microsoft.com/en-us/library/windows/apps/dd316629.aspx)                                                                           | Introduced in Windows 10.0.10240.0 |
| [**IOpcSignatureRelationshipReference**](https://msdn.microsoft.com/en-us/library/windows/apps/dd316670.aspx)                                                         | Introduced in Windows 10.0.10240.0 |
| [**IOpcSignatureRelationshipReferenceEnumerator**](https://msdn.microsoft.com/en-us/library/windows/apps/dd316673.aspx)                                     | Introduced in Windows 10.0.10240.0 |
| [**IOpcSignatureRelationshipReferenceSet**](https://msdn.microsoft.com/en-us/library/windows/apps/dd316689.aspx)                                                   | Introduced in Windows 10.0.10240.0 |
| [**IOpcSigningOptions**](https://msdn.microsoft.com/en-us/library/windows/apps/dd316719.aspx)                                                                                         | Introduced in Windows 10.0.10240.0 |
| [**IOpcUri**](https://msdn.microsoft.com/en-us/library/windows/apps/dd316778.aspx)                                                                                                               | Introduced in Windows 10.0.10240.0 |
| [**IOptionDescription**](https://msdn.microsoft.com/en-us/library/windows/apps/hh869762.aspx)                                                                                        | Introduced in Windows 10.0.10240.0 |
| [**IPdfRendererNative**](https://msdn.microsoft.com/en-us/library/windows/apps/dn302125.aspx)                                                                                       | Introduced in Windows 10.0.10240.0 |
| [**IPMApplicationInfo**](https://www.bing.com/search?q=IPMApplicationInfo)                                                               | Introduced in Windows 10.0.10240.0 |
| [**IPMApplicationInfoEnumerator**](https://www.bing.com/search?q=IPMApplicationInfoEnumerator)                                           | Introduced in Windows 10.0.10240.0 |
| [**IPMBackgroundServiceAgentInfo**](https://www.bing.com/search?q=IPMBackgroundServiceAgentInfo)                                         | Introduced in Windows 10.0.10240.0 |
| [**IPMBackgroundServiceAgentInfoEnumerator**](https://www.bing.com/search?q=IPMBackgroundServiceAgentInfoEnumerator)                     | Introduced in Windows 10.0.10240.0 |
| [**IPMBackgroundWorkerInfo**](https://www.bing.com/search?q=IPMBackgroundWorkerInfo)                                                     | Introduced in Windows 10.0.10240.0 |
| [**IPMBackgroundWorkerInfoEnumerator**](https://www.bing.com/search?q=IPMBackgroundWorkerInfoEnumerator)                                 | Introduced in Windows 10.0.10240.0 |
| [**IPMEnumerationManager**](https://www.bing.com/search?q=IPMEnumerationManager)                                                         | Introduced in Windows 10.0.10240.0 |
| [**IPMExtensionCachedFileUpdaterInfo**](https://www.bing.com/search?q=IPMExtensionCachedFileUpdaterInfo)                                 | Introduced in Windows 10.0.10240.0 |
| [**IPMExtensionContractInfo**](https://www.bing.com/search?q=IPMExtensionContractInfo)                                                   | Introduced in Windows 10.0.10240.0 |
| [**IPMExtensionFileExtensionInfo**](https://www.bing.com/search?q=IPMExtensionFileExtensionInfo)                                         | Introduced in Windows 10.0.10240.0 |
| [**IPMExtensionFileOpenPickerInfo**](https://www.bing.com/search?q=IPMExtensionFileOpenPickerInfo)                                       | Introduced in Windows 10.0.10240.0 |
| [**IPMExtensionFileSavePickerInfo**](https://www.bing.com/search?q=IPMExtensionFileSavePickerInfo)                                       | Introduced in Windows 10.0.10240.0 |
| [**IPMExtensionInfo**](https://www.bing.com/search?q=IPMExtensionInfo)                                                                   | Introduced in Windows 10.0.10240.0 |
| [**IPMExtensionInfoEnumerator**](https://www.bing.com/search?q=IPMExtensionInfoEnumerator)                                               | Introduced in Windows 10.0.10240.0 |
| [**IPMExtensionProtocolInfo**](https://www.bing.com/search?q=IPMExtensionProtocolInfo)                                                   | Introduced in Windows 10.0.10240.0 |
| [**IPMExtensionShareTargetInfo**](https://www.bing.com/search?q=IPMExtensionShareTargetInfo)                                             | Introduced in Windows 10.0.10240.0 |
| [**IPMLiveTileJobInfo**](https://www.bing.com/search?q=IPMLiveTileJobInfo)                                                               | Introduced in Windows 10.0.10240.0 |
| [**IPMLiveTileJobInfoEnumerator**](https://www.bing.com/search?q=IPMLiveTileJobInfoEnumerator)                                           | Introduced in Windows 10.0.10240.0 |
| [**IPMTaskInfo**](https://www.bing.com/search?q=IPMTaskInfo)                                                                             | Introduced in Windows 10.0.10240.0 |
| [**IPMTaskInfoEnumerator**](https://www.bing.com/search?q=IPMTaskInfoEnumerator)                                                         | Introduced in Windows 10.0.10240.0 |
| [**IPMTileInfo**](https://www.bing.com/search?q=IPMTileInfo)                                                                             | Introduced in Windows 10.0.10240.0 |
| [**IPMTileInfoEnumerator**](https://www.bing.com/search?q=IPMTileInfoEnumerator)                                                         | Introduced in Windows 10.0.10240.0 |
| [**IPMTilePropertyEnumerator**](https://www.bing.com/search?q=IPMTilePropertyEnumerator)                                                 | Introduced in Windows 10.0.10240.0 |
| [**IPMTilePropertyInfo**](https://www.bing.com/search?q=IPMTilePropertyInfo)                                                             | Introduced in Windows 10.0.10240.0 |
| [**IPortableDevice**](https://msdn.microsoft.com/en-us/library/windows/apps/dd319361.aspx)                                                                                            | Introduced in Windows 10.0.10240.0 |
| [**IPortableDeviceCapabilities**](https://msdn.microsoft.com/en-us/library/windows/apps/dd319362.aspx)                                                                    | Introduced in Windows 10.0.10240.0 |
| [**IPortableDeviceContent**](https://msdn.microsoft.com/en-us/library/windows/apps/dd388529.aspx)                                                                              | Introduced in Windows 10.0.10240.0 |
| [**IPortableDeviceContent2**](https://msdn.microsoft.com/en-us/library/windows/apps/dd388530.aspx)                                                                            | Introduced in Windows 10.0.10240.0 |
| [**IPortableDeviceDataStream**](https://msdn.microsoft.com/en-us/library/windows/apps/dd388542.aspx)                                                                        | Introduced in Windows 10.0.10240.0 |
| [**IPortableDeviceDispatchFactory**](https://msdn.microsoft.com/en-us/library/windows/apps/dd389218.aspx)                                                   | Introduced in Windows 10.0.10240.0 |
| [**IPortableDeviceEventCallback**](https://msdn.microsoft.com/en-us/library/windows/apps/dd388545.aspx)                                                                  | Introduced in Windows 10.0.10240.0 |
| [**IPortableDeviceKeyCollection**](https://msdn.microsoft.com/en-us/library/windows/apps/dd388547.aspx)                                                                  | Introduced in Windows 10.0.10240.0 |
| [**IPortableDeviceManager**](https://msdn.microsoft.com/en-us/library/windows/apps/dd388688.aspx)                                                                              | Introduced in Windows 10.0.10240.0 |
| [**IPortableDeviceProperties**](https://msdn.microsoft.com/en-us/library/windows/apps/dd388696.aspx)                                                                        | Introduced in Windows 10.0.10240.0 |
| [**IPortableDevicePropertiesBulk**](https://msdn.microsoft.com/en-us/library/windows/apps/dd388697.aspx)                                                                | Introduced in Windows 10.0.10240.0 |
| [**IPortableDevicePropertiesBulkCallback**](https://msdn.microsoft.com/en-us/library/windows/apps/dd388698.aspx)                                                | Introduced in Windows 10.0.10240.0 |
| [**IPortableDevicePropVariantCollection**](https://msdn.microsoft.com/en-us/library/windows/apps/dd388719.aspx)                                                  | Introduced in Windows 10.0.10240.0 |
| [**IPortableDeviceResources**](https://msdn.microsoft.com/en-us/library/windows/apps/dd388733.aspx)                                                                          | Introduced in Windows 10.0.10240.0 |
| [**IPortableDeviceService**](https://msdn.microsoft.com/en-us/library/windows/apps/dd388753.aspx)                                                                              | Introduced in Windows 10.0.10240.0 |
| [**IPortableDeviceServiceActivation**](https://www.bing.com/search?q=IPortableDeviceServiceActivation)                                   | Introduced in Windows 10.0.10240.0 |
| [**IPortableDeviceServiceCapabilities**](https://msdn.microsoft.com/en-us/library/windows/apps/dd388755.aspx)                                                      | Introduced in Windows 10.0.10240.0 |
| [**IPortableDeviceServiceManager**](https://msdn.microsoft.com/en-us/library/windows/apps/dd319402.aspx)                                                                | Introduced in Windows 10.0.10240.0 |
| [**IPortableDeviceServiceMethodCallback**](https://msdn.microsoft.com/en-us/library/windows/apps/dd319411.aspx)                                                  | Introduced in Windows 10.0.10240.0 |
| [**IPortableDeviceServiceMethods**](https://msdn.microsoft.com/en-us/library/windows/apps/dd319418.aspx)                                                                | Introduced in Windows 10.0.10240.0 |
| [**IPortableDeviceServiceOpenCallback**](https://www.bing.com/search?q=IPortableDeviceServiceOpenCallback)                               | Introduced in Windows 10.0.10240.0 |
| [**IPortableDeviceUnitsStream**](https://msdn.microsoft.com/en-us/library/windows/apps/hh707376.aspx)                                                                      | Introduced in Windows 10.0.10240.0 |
| [**IPortableDeviceValues**](https://msdn.microsoft.com/en-us/library/windows/apps/dd319461.aspx)                                                                                | Introduced in Windows 10.0.10240.0 |
| [**IPortableDeviceValuesCollection**](https://msdn.microsoft.com/en-us/library/windows/apps/dd319463.aspx)                                                            | Introduced in Windows 10.0.10240.0 |
| [**IPrintDocumentPackageTarget**](https://msdn.microsoft.com/en-us/library/windows/apps/hh448393.aspx)                                                                       | Introduced in Windows 10.0.10240.0 |
| [**IPrintDocumentPageSource**](https://www.bing.com/search?q=IPrintDocumentPageSource)                                                   | Introduced in Windows 10.0.10240.0 |
| [**IPrinterBidiSetRequestCallback**](https://www.bing.com/search?q=IPrinterBidiSetRequestCallback)                                       | Introduced in Windows 10.0.10240.0 |
| [**IPrinterExtensionAsyncOperation**](https://www.bing.com/search?q=IPrinterExtensionAsyncOperation)                                     | Introduced in Windows 10.0.10240.0 |
| [**IPrinterExtensionContext**](https://www.bing.com/search?q=IPrinterExtensionContext)                                                   | Introduced in Windows 10.0.10240.0 |
| [**IPrinterPropertyBag**](https://www.bing.com/search?q=IPrinterPropertyBag)                                                             | Introduced in Windows 10.0.10240.0 |
| [**IPrinterQueue**](https://www.bing.com/search?q=IPrinterQueue)                                                                         | Introduced in Windows 10.0.10240.0 |
| [**IPrinterQueue2**](https://www.bing.com/search?q=IPrinterQueue2)                                                                       | Introduced in Windows 10.0.10240.0 |
| [**IPrinterQueueEvent**](https://www.bing.com/search?q=IPrinterQueueEvent)                                                               | Introduced in Windows 10.0.10240.0 |
| [**IPrinterQueueView**](https://www.bing.com/search?q=IPrinterQueueView)                                                                 | Introduced in Windows 10.0.10240.0 |
| [**IPrinterQueueViewEvent**](https://www.bing.com/search?q=IPrinterQueueViewEvent)                                                       | Introduced in Windows 10.0.10240.0 |
| [**IPrintJob**](https://www.bing.com/search?q=IPrintJob)                                                                                 | Introduced in Windows 10.0.10240.0 |
| [**IPrintJobCollection**](https://www.bing.com/search?q=IPrintJobCollection)                                                             | Introduced in Windows 10.0.10240.0 |
| [**IPrintPreviewDxgiPackageTarget**](https://www.bing.com/search?q=IPrintPreviewDxgiPackageTarget)                                       | Introduced in Windows 10.0.10240.0 |
| [**IPrintPreviewPageCollection**](https://www.bing.com/search?q=IPrintPreviewPageCollection)                                             | Introduced in Windows 10.0.10240.0 |
| [**IPrintSchemaAsyncOperation**](https://www.bing.com/search?q=IPrintSchemaAsyncOperation)                                               | Introduced in Windows 10.0.10240.0 |
| [**IPrintSchemaAsyncOperationEvent**](https://www.bing.com/search?q=IPrintSchemaAsyncOperationEvent)                                     | Introduced in Windows 10.0.10240.0 |
| [**IPrintSchemaCapabilities**](https://www.bing.com/search?q=IPrintSchemaCapabilities)                                                   | Introduced in Windows 10.0.10240.0 |
| [**IPrintSchemaCapabilities2**](https://www.bing.com/search?q=IPrintSchemaCapabilities2)                                                 | Introduced in Windows 10.0.10240.0 |
| [**IPrintSchemaDisplayableElement**](https://www.bing.com/search?q=IPrintSchemaDisplayableElement)                                       | Introduced in Windows 10.0.10240.0 |
| [**IPrintSchemaElement**](https://www.bing.com/search?q=IPrintSchemaElement)                                                             | Introduced in Windows 10.0.10240.0 |
| [**IPrintSchemaFeature**](https://www.bing.com/search?q=IPrintSchemaFeature)                                                             | Introduced in Windows 10.0.10240.0 |
| [**IPrintSchemaNUpOption**](https://www.bing.com/search?q=IPrintSchemaNUpOption)                                                         | Introduced in Windows 10.0.10240.0 |
| [**IPrintSchemaOption**](https://www.bing.com/search?q=IPrintSchemaOption)                                                               | Introduced in Windows 10.0.10240.0 |
| [**IPrintSchemaOptionCollection**](https://www.bing.com/search?q=IPrintSchemaOptionCollection)                                           | Introduced in Windows 10.0.10240.0 |
| [**IPrintSchemaPageImageableSize**](https://www.bing.com/search?q=IPrintSchemaPageImageableSize)                                         | Introduced in Windows 10.0.10240.0 |
| [**IPrintSchemaPageMediaSizeOption**](https://www.bing.com/search?q=IPrintSchemaPageMediaSizeOption)                                     | Introduced in Windows 10.0.10240.0 |
| [**IPrintSchemaParameterDefinition**](https://www.bing.com/search?q=IPrintSchemaParameterDefinition)                                     | Introduced in Windows 10.0.10240.0 |
| [**IPrintSchemaParameterInitializer**](https://www.bing.com/search?q=IPrintSchemaParameterInitializer)                                   | Introduced in Windows 10.0.10240.0 |
| [**IPrintSchemaTicket**](https://www.bing.com/search?q=IPrintSchemaTicket)                                                               | Introduced in Windows 10.0.10240.0 |
| [**IPrintSchemaTicket2**](https://www.bing.com/search?q=IPrintSchemaTicket2)                                                             | Introduced in Windows 10.0.10240.0 |
| [**IPropertyBag2**](https://www.bing.com/search?q=IPropertyBag2)                                                                         | Introduced in Windows 10.0.10240.0 |
| [**IPropertySetStorage**](https://msdn.microsoft.com/en-us/library/windows/apps/aa379840.aspx)                                                                                       | Introduced in Windows 10.0.10240.0 |
| [**IPropertySetStorage**](https://msdn.microsoft.com/en-us/library/windows/apps/aa379840.aspx)                                                                                       | Introduced in Windows 10.0.10240.0 |
| [**IPropertyStorage**](https://msdn.microsoft.com/en-us/library/windows/apps/aa379968.aspx)                                                                                             | Introduced in Windows 10.0.10240.0 |
| [**IPropertyStorage**](https://msdn.microsoft.com/en-us/library/windows/apps/aa379968.aspx)                                                                                             | Introduced in Windows 10.0.10240.0 |
| [**IPropertyStore**](https://msdn.microsoft.com/en-us/library/windows/apps/bb761474.aspx)                                                                                          | Introduced in Windows 10.0.10240.0 |
| [**IProxyProviderWinEventHandler**](https://msdn.microsoft.com/en-us/library/windows/apps/ee671303.aspx)                                                        | Introduced in Windows 10.0.10240.0 |
| [**IProxyProviderWinEventSink**](https://msdn.microsoft.com/en-us/library/windows/apps/ee671305.aspx)                                                              | Introduced in Windows 10.0.10240.0 |
| [**IPSFactoryBuffer**](https://msdn.microsoft.com/en-us/library/windows/apps/ms695281.aspx)                                                                                             | Introduced in Windows 10.0.10240.0 |
| [**IPSFactoryBuffer**](https://msdn.microsoft.com/en-us/library/windows/apps/ms695281.aspx)                                                                                             | Introduced in Windows 10.0.10240.0 |
| [**IQuickActivate**](https://msdn.microsoft.com/en-us/library/windows/apps/ms690146.aspx)                                                                                                 | Introduced in Windows 10.0.10240.0 |
| [**IRangeValueProvider**](https://msdn.microsoft.com/en-us/library/windows/apps/ee671309.aspx)                                                                            | Introduced in Windows 10.0.10240.0 |
| [**IRawElementProviderAdviseEvents**](https://msdn.microsoft.com/en-us/library/windows/apps/ee671317.aspx)                                                    | Introduced in Windows 10.0.10240.0 |
| [**IRawElementProviderFragment**](https://msdn.microsoft.com/en-us/library/windows/apps/ee671320.aspx)                                                            | Introduced in Windows 10.0.10240.0 |
| [**IRawElementProviderFragmentRoot**](https://msdn.microsoft.com/en-us/library/windows/apps/ee671321.aspx)                                                    | Introduced in Windows 10.0.10240.0 |
| [**IRawElementProviderHostingAccessibles**](https://msdn.microsoft.com/en-us/library/windows/apps/hh448785.aspx)                                        | Introduced in Windows 10.0.10240.0 |
| [**IRawElementProviderHwndOverride**](https://msdn.microsoft.com/en-us/library/windows/apps/ee671330.aspx)                                                    | Introduced in Windows 10.0.10240.0 |
| [**IRawElementProviderSimple**](https://msdn.microsoft.com/en-us/library/windows/apps/ee671332.aspx)                                                                | Introduced in Windows 10.0.10240.0 |
| [**IRawElementProviderSimple2**](https://msdn.microsoft.com/en-us/library/windows/apps/dn302133.aspx)                                                              | Introduced in Windows 10.0.10240.0 |
| [**IRawElementProviderWindowlessSite**](https://msdn.microsoft.com/en-us/library/windows/apps/hh448787.aspx)                                                | Introduced in Windows 10.0.10240.0 |
| [**IRDPSRAPIApplication**](https://msdn.microsoft.com/en-us/library/windows/apps/aa373266.aspx)                                                                                     | Introduced in Windows 10.0.10240.0 |
| [**IRDPSRAPIApplicationFilter**](https://msdn.microsoft.com/en-us/library/windows/apps/aa373267.aspx)                                                                         | Introduced in Windows 10.0.10240.0 |
| [**IRDPSRAPIApplicationList**](https://msdn.microsoft.com/en-us/library/windows/apps/aa373271.aspx)                                                                             | Introduced in Windows 10.0.10240.0 |
| [**IRDPSRAPIAttendee**](https://msdn.microsoft.com/en-us/library/windows/apps/aa373279.aspx)                                                                                           | Introduced in Windows 10.0.10240.0 |
| [**IRDPSRAPIAttendeeDisconnectInfo**](https://msdn.microsoft.com/en-us/library/windows/apps/aa373280.aspx)                                                               | Introduced in Windows 10.0.10240.0 |
| [**IRDPSRAPIAttendeeManager**](https://msdn.microsoft.com/en-us/library/windows/apps/aa373284.aspx)                                                                             | Introduced in Windows 10.0.10240.0 |
| [**IRDPSRAPIAudioStream**](https://www.bing.com/search?q=IRDPSRAPIAudioStream)                                                           | Introduced in Windows 10.0.10240.0 |
| [**IRDPSRAPIDebug**](https://www.bing.com/search?q=IRDPSRAPIDebug)                                                                       | Introduced in Windows 10.0.10240.0 |
| [**IRDPSRAPIFrameBuffer**](https://msdn.microsoft.com/en-us/library/windows/apps/dn894394.aspx)                                                                                     | Introduced in Windows 10.0.10240.0 |
| [**IRDPSRAPIInvitation**](https://msdn.microsoft.com/en-us/library/windows/apps/aa373294.aspx)                                                                                       | Introduced in Windows 10.0.10240.0 |
| [**IRDPSRAPIInvitationManager**](https://msdn.microsoft.com/en-us/library/windows/apps/aa373295.aspx)                                                                         | Introduced in Windows 10.0.10240.0 |
| [**IRDPSRAPIPerfCounterLogger**](https://www.bing.com/search?q=IRDPSRAPIPerfCounterLogger)                                               | Introduced in Windows 10.0.10240.0 |
| [**IRDPSRAPIPerfCounterLoggingManager**](https://www.bing.com/search?q=IRDPSRAPIPerfCounterLoggingManager)                               | Introduced in Windows 10.0.10240.0 |
| [**IRDPSRAPISessionProperties**](https://msdn.microsoft.com/en-us/library/windows/apps/aa373305.aspx)                                                                         | Introduced in Windows 10.0.10240.0 |
| [**IRDPSRAPISharingSession**](https://msdn.microsoft.com/en-us/library/windows/apps/aa373307.aspx)                                                                               | Introduced in Windows 10.0.10240.0 |
| [**IRDPSRAPISharingSession2**](https://msdn.microsoft.com/en-us/library/windows/apps/dn894401.aspx)                                                                             | Introduced in Windows 10.0.10240.0 |
| [**IRDPSRAPITcpConnectionInfo**](https://msdn.microsoft.com/en-us/library/windows/apps/aa373321.aspx)                                                                         | Introduced in Windows 10.0.10240.0 |
| [**IRDPSRAPITransportStream**](https://msdn.microsoft.com/en-us/library/windows/apps/ee620975.aspx)                                                                             | Introduced in Windows 10.0.10240.0 |
| [**IRDPSRAPITransportStreamBuffer**](https://msdn.microsoft.com/en-us/library/windows/apps/ee620976.aspx)                                                                 | Introduced in Windows 10.0.10240.0 |
| [**IRDPSRAPITransportStreamEvents**](https://msdn.microsoft.com/en-us/library/windows/apps/ee620984.aspx)                                                                 | Introduced in Windows 10.0.10240.0 |
| [**IRDPSRAPIViewer**](https://msdn.microsoft.com/en-us/library/windows/apps/aa373327.aspx)                                                                                               | Introduced in Windows 10.0.10240.0 |
| [**IRDPSRAPIVirtualChannel**](https://msdn.microsoft.com/en-us/library/windows/apps/aa373361.aspx)                                                                               | Introduced in Windows 10.0.10240.0 |
| [**IRDPSRAPIVirtualChannelManager**](https://msdn.microsoft.com/en-us/library/windows/apps/aa373362.aspx)                                                                 | Introduced in Windows 10.0.10240.0 |
| [**IRDPSRAPIWindow**](https://msdn.microsoft.com/en-us/library/windows/apps/aa373371.aspx)                                                                                               | Introduced in Windows 10.0.10240.0 |
| [**IRDPSRAPIWindowList**](https://msdn.microsoft.com/en-us/library/windows/apps/aa373372.aspx)                                                                                       | Introduced in Windows 10.0.10240.0 |
| [**IRDPViewerInputSink**](https://www.bing.com/search?q=IRDPViewerInputSink)                                                             | Introduced in Windows 10.0.10240.0 |
| [**IRDPViewerRenderingSurface**](https://msdn.microsoft.com/en-us/library/windows/apps/hh802746.aspx)                                                                         | Introduced in Windows 10.0.10240.0 |
| [**IReferenceTracker**](https://msdn.microsoft.com/en-us/library/windows/apps/jj542495.aspx)                                                                                         | Introduced in Windows 10.0.10240.0 |
| [**IReferenceTrackerHost**](https://msdn.microsoft.com/en-us/library/windows/apps/jj542496.aspx)                                                                                 | Introduced in Windows 10.0.10240.0 |
| [**IReferenceTrackerManager**](https://msdn.microsoft.com/en-us/library/windows/apps/jj542503.aspx)                                                                           | Introduced in Windows 10.0.10240.0 |
| [**IReferenceTrackerTarget**](https://msdn.microsoft.com/en-us/library/windows/apps/jj542508.aspx)                                                                             | Introduced in Windows 10.0.10240.0 |
| [**IRemoteDesktopClient**](https://msdn.microsoft.com/en-us/library/windows/apps/hh448564.aspx)                                                                                | Introduced in Windows 10.0.10240.0 |
| [**IRemoteDesktopClientActions**](https://msdn.microsoft.com/en-us/library/windows/apps/hh448581.aspx)                                                                  | Introduced in Windows 10.0.10240.0 |
| [**IRemoteDesktopClientEvents**](https://msdn.microsoft.com/en-us/library/windows/apps/hh448568.aspx)                                                                    | Introduced in Windows 10.0.10240.0 |
| [**IRemoteDesktopClientSettings**](https://msdn.microsoft.com/en-us/library/windows/apps/hh448590.aspx)                                                                | Introduced in Windows 10.0.10240.0 |
| [**IRestrictedErrorInfo**](https://msdn.microsoft.com/en-us/library/windows/apps/br224587.aspx)                                                                                   | Introduced in Windows 10.0.10240.0 |
| [**IRootStorage**](https://msdn.microsoft.com/en-us/library/windows/apps/aa379987.aspx)                                                                                                     | Introduced in Windows 10.0.10240.0 |
| [**IRpcChannelBuffer**](https://msdn.microsoft.com/en-us/library/windows/apps/ms679738.aspx)                                                                                           | Introduced in Windows 10.0.10240.0 |
| [**IRpcChannelBuffer**](https://msdn.microsoft.com/en-us/library/windows/apps/ms679738.aspx)                                                                                           | Introduced in Windows 10.0.10240.0 |
| [**IRpcStubBuffer**](https://msdn.microsoft.com/en-us/library/windows/apps/ms678504.aspx)                                                                                                 | Introduced in Windows 10.0.10240.0 |
| [**IRpcStubBuffer**](https://msdn.microsoft.com/en-us/library/windows/apps/ms678504.aspx)                                                                                                 | Introduced in Windows 10.0.10240.0 |
| [**IScrollItemProvider**](https://msdn.microsoft.com/en-us/library/windows/apps/ee671338.aspx)                                                                            | Introduced in Windows 10.0.10240.0 |
| [**IScrollProvider**](https://msdn.microsoft.com/en-us/library/windows/apps/ee671340.aspx)                                                                                    | Introduced in Windows 10.0.10240.0 |
| [**ISelectionItemProvider**](https://msdn.microsoft.com/en-us/library/windows/apps/ee671349.aspx)                                                                      | Introduced in Windows 10.0.10240.0 |
| [**ISelectionProvider**](https://msdn.microsoft.com/en-us/library/windows/apps/ee671355.aspx)                                                                              | Introduced in Windows 10.0.10240.0 |
| [**ISequentialStream**](https://msdn.microsoft.com/en-us/library/windows/apps/aa380010.aspx)                                                                                           | Introduced in Windows 10.0.10240.0 |
| [**ISequentialStream**](https://msdn.microsoft.com/en-us/library/windows/apps/aa380010.aspx)                                                                                           | Introduced in Windows 10.0.10240.0 |
| [**ISignalableNotifier**](https://www.bing.com/search?q=ISignalableNotifier)                                                             | Introduced in Windows 10.0.10240.0 |
| [**ISimpleAudioVolume**](https://msdn.microsoft.com/en-us/library/windows/apps/dd316531.aspx)                                                                                   | Introduced in Windows 10.0.10240.0 |
| [**ISoftwareBitmapNative**](https://msdn.microsoft.com/en-us/library/windows/apps/dn878036.aspx)                                                                                 | Introduced in Windows 10.0.10240.0 |
| [**ISoftwareBitmapNativeFactory**](https://msdn.microsoft.com/en-us/library/windows/apps/dn878037.aspx)                                                                   | Introduced in Windows 10.0.10240.0 |
| [**ISpellChecker**](https://msdn.microsoft.com/en-us/library/windows/apps/hh869767.aspx)                                                                                                  | Introduced in Windows 10.0.10240.0 |
| [**ISpellChecker2**](https://msdn.microsoft.com/en-us/library/windows/apps/mt422900.aspx)                                                                                                | Introduced in Windows 10.0.10240.0 |
| [**ISpellCheckerChangedEventHandler**](https://msdn.microsoft.com/en-us/library/windows/apps/hh869768.aspx)                                                            | Introduced in Windows 10.0.10240.0 |
| [**ISpellCheckerFactory**](https://msdn.microsoft.com/en-us/library/windows/apps/hh869770.aspx)                                                                                    | Introduced in Windows 10.0.10240.0 |
| [**ISpellingError**](https://msdn.microsoft.com/en-us/library/windows/apps/hh869805.aspx)                                                                                                | Introduced in Windows 10.0.10240.0 |
| [**ISpreadsheetItemProvider**](https://msdn.microsoft.com/en-us/library/windows/apps/hh448790.aspx)                                                                  | Introduced in Windows 10.0.10240.0 |
| [**ISpreadsheetProvider**](https://msdn.microsoft.com/en-us/library/windows/apps/hh448796.aspx)                                                                          | Introduced in Windows 10.0.10240.0 |
| [**IStorage**](https://msdn.microsoft.com/en-us/library/windows/apps/aa380015.aspx)                                                                                                             | Introduced in Windows 10.0.10240.0 |
| [**IStream**](https://msdn.microsoft.com/en-us/library/windows/apps/aa380034.aspx)                                                                                                               | Introduced in Windows 10.0.10240.0 |
| [**IStream**](https://msdn.microsoft.com/en-us/library/windows/apps/aa380034.aspx)                                                                                                               | Introduced in Windows 10.0.10240.0 |
| [**IStylesProvider**](https://msdn.microsoft.com/en-us/library/windows/apps/hh448800.aspx)                                                                                    | Introduced in Windows 10.0.10240.0 |
| [**ISurfaceImageSourceManagerNative**](https://msdn.microsoft.com/en-us/library/windows/apps/dn448959.aspx)                                                           | Introduced in Windows 10.0.10240.0 |
| [**ISurfaceImageSourceNative**](https://msdn.microsoft.com/en-us/library/windows/apps/hh848322.aspx)                                                                         | Introduced in Windows 10.0.10240.0 |
| [**ISurfaceImageSourceNativeWithD2D**](https://msdn.microsoft.com/en-us/library/windows/apps/dn302137.aspx)                                                           | Introduced in Windows 10.0.10240.0 |
| [**ISurrogate**](https://msdn.microsoft.com/en-us/library/windows/apps/ms695062.aspx)                                                                                                         | Introduced in Windows 10.0.10240.0 |
| [**ISurrogate**](https://msdn.microsoft.com/en-us/library/windows/apps/ms695062.aspx)                                                                                                         | Introduced in Windows 10.0.10240.0 |
| [**ISwapChainBackgroundPanelNative**](https://msdn.microsoft.com/en-us/library/windows/apps/hh848326.aspx)                                                             | Introduced in Windows 10.0.10240.0 |
| [**ISwapChainPanelNative**](https://msdn.microsoft.com/en-us/library/windows/apps/dn302143.aspx)                                                                                 | Introduced in Windows 10.0.10240.0 |
| [**ISwapChainPanelNative2**](https://msdn.microsoft.com/en-us/library/windows/apps/dn858172.aspx)                                                                               | Introduced in Windows 10.0.10240.0 |
| [**ISynchronizedInputProvider**](https://msdn.microsoft.com/en-us/library/windows/apps/ee671359.aspx)                                                              | Introduced in Windows 10.0.10240.0 |
| [**ITableItemProvider**](https://msdn.microsoft.com/en-us/library/windows/apps/ee671362.aspx)                                                                              | Introduced in Windows 10.0.10240.0 |
| [**ITableProvider**](https://msdn.microsoft.com/en-us/library/windows/apps/ee671365.aspx)                                                                                      | Introduced in Windows 10.0.10240.0 |
| [**ITextChildProvider**](https://msdn.microsoft.com/en-us/library/windows/apps/hh437317.aspx)                                                                             | Introduced in Windows 10.0.10240.0 |
| [**ITextEditProvider**](https://msdn.microsoft.com/en-us/library/windows/apps/dn302166.aspx)                                                                                | Introduced in Windows 10.0.10240.0 |
| [**ITextProvider**](https://msdn.microsoft.com/en-us/library/windows/apps/ee671370.aspx)                                                                                        | Introduced in Windows 10.0.10240.0 |
| [**ITextProvider2**](https://msdn.microsoft.com/en-us/library/windows/apps/hh448818.aspx)                                                                                      | Introduced in Windows 10.0.10240.0 |
| [**ITextRangeProvider**](https://msdn.microsoft.com/en-us/library/windows/apps/ee671377.aspx)                                                                              | Introduced in Windows 10.0.10240.0 |
| [**ITextRangeProvider2**](https://msdn.microsoft.com/en-us/library/windows/apps/dn302169.aspx)                                                                            | Introduced in Windows 10.0.10240.0 |
| [**ITextStoreACP2**](https://msdn.microsoft.com/en-us/library/windows/apps/jj670566.aspx)                                                                                                 | Introduced in Windows 10.0.10240.0 |
| [**ITextStoreACPServices**](https://msdn.microsoft.com/en-us/library/windows/apps/ms538387.aspx)                                                                                   | Introduced in Windows 10.0.10240.0 |
| [**ITextStoreACPSink**](https://msdn.microsoft.com/en-us/library/windows/apps/ms538395.aspx)                                                                                           | Introduced in Windows 10.0.10240.0 |
| [**ITextStoreAnchor**](https://msdn.microsoft.com/en-us/library/windows/apps/ms538453.aspx)                                                                                             | Introduced in Windows 10.0.10240.0 |
| [**ITextStoreAnchorSink**](https://msdn.microsoft.com/en-us/library/windows/apps/ms538454.aspx)                                                                                     | Introduced in Windows 10.0.10240.0 |
| [**ITfCandidateList**](https://msdn.microsoft.com/en-us/library/windows/apps/ms538492.aspx)                                                                                             | Introduced in Windows 10.0.10240.0 |
| [**ITfCandidateListUIElement**](https://msdn.microsoft.com/en-us/library/windows/apps/aa380892.aspx)                                                                           | Introduced in Windows 10.0.10240.0 |
| [**ITfCandidateListUIElementBehavior**](https://msdn.microsoft.com/en-us/library/windows/apps/aa381004.aspx)                                                           | Introduced in Windows 10.0.10240.0 |
| [**ITfCandidateString**](https://msdn.microsoft.com/en-us/library/windows/apps/ms538497.aspx)                                                                                         | Introduced in Windows 10.0.10240.0 |
| [**ITfCategoryMgr**](https://msdn.microsoft.com/en-us/library/windows/apps/ms538500.aspx)                                                                                                 | Introduced in Windows 10.0.10240.0 |
| [**ITfCompartment**](https://msdn.microsoft.com/en-us/library/windows/apps/ms538621.aspx)                                                                                                 | Introduced in Windows 10.0.10240.0 |
| [**ITfCompartmentEventSink**](https://msdn.microsoft.com/en-us/library/windows/apps/ms538625.aspx)                                                                               | Introduced in Windows 10.0.10240.0 |
| [**ITfCompartmentMgr**](https://msdn.microsoft.com/en-us/library/windows/apps/ms538631.aspx)                                                                                           | Introduced in Windows 10.0.10240.0 |
| [**ITfComposition**](https://msdn.microsoft.com/en-us/library/windows/apps/ms538653.aspx)                                                                                                 | Introduced in Windows 10.0.10240.0 |
| [**ITfCompositionSink**](https://msdn.microsoft.com/en-us/library/windows/apps/ms538654.aspx)                                                                                         | Introduced in Windows 10.0.10240.0 |
| [**ITfCompositionView**](https://msdn.microsoft.com/en-us/library/windows/apps/ms538660.aspx)                                                                                         | Introduced in Windows 10.0.10240.0 |
| [**ITfConfigureSystemKeystrokeFeed**](https://msdn.microsoft.com/en-us/library/windows/apps/ms538692.aspx)                                                               | Introduced in Windows 10.0.10240.0 |
| [**ITfContext**](https://msdn.microsoft.com/en-us/library/windows/apps/ms538703.aspx)                                                                                                         | Introduced in Windows 10.0.10240.0 |
| [**ITfContextComposition**](https://msdn.microsoft.com/en-us/library/windows/apps/ms538705.aspx)                                                                                   | Introduced in Windows 10.0.10240.0 |
| [**ITfContextOwnerCompositionServices**](https://msdn.microsoft.com/en-us/library/windows/apps/ms538734.aspx)                                                         | Introduced in Windows 10.0.10240.0 |
| [**ITfContextOwnerCompositionSink**](https://msdn.microsoft.com/en-us/library/windows/apps/ms538740.aspx)                                                                 | Introduced in Windows 10.0.10240.0 |
| [**ITfContextOwnerServices**](https://msdn.microsoft.com/en-us/library/windows/apps/ms538750.aspx)                                                                               | Introduced in Windows 10.0.10240.0 |
| [**ITfContextView**](https://msdn.microsoft.com/en-us/library/windows/apps/ms538779.aspx)                                                                                                 | Introduced in Windows 10.0.10240.0 |
| [**ITfDisplayAttributeInfo**](https://msdn.microsoft.com/en-us/library/windows/apps/ms538802.aspx)                                                                               | Introduced in Windows 10.0.10240.0 |
| [**ITfDisplayAttributeMgr**](https://msdn.microsoft.com/en-us/library/windows/apps/ms538808.aspx)                                                                                 | Introduced in Windows 10.0.10240.0 |
| [**ITfDisplayAttributeNotifySink**](https://msdn.microsoft.com/en-us/library/windows/apps/ms538869.aspx)                                                                   | Introduced in Windows 10.0.10240.0 |
| [**ITfDisplayAttributeProvider**](https://msdn.microsoft.com/en-us/library/windows/apps/ms538873.aspx)                                                                       | Introduced in Windows 10.0.10240.0 |
| [**ITfDocumentMgr**](https://msdn.microsoft.com/en-us/library/windows/apps/ms538878.aspx)                                                                                                 | Introduced in Windows 10.0.10240.0 |
| [**ITfEditRecord**](https://msdn.microsoft.com/en-us/library/windows/apps/ms538901.aspx)                                                                                                   | Introduced in Windows 10.0.10240.0 |
| [**ITfEditSession**](https://msdn.microsoft.com/en-us/library/windows/apps/ms538906.aspx)                                                                                                 | Introduced in Windows 10.0.10240.0 |
| [**ITfFnGetSAPIObject**](https://msdn.microsoft.com/en-us/library/windows/apps/ms538932.aspx)                                                                                         | Introduced in Windows 10.0.10240.0 |
| [**ITfFnReconversion**](https://msdn.microsoft.com/en-us/library/windows/apps/ms538970.aspx)                                                                                           | Introduced in Windows 10.0.10240.0 |
| [**ITfFunction**](https://msdn.microsoft.com/en-us/library/windows/apps/ms538978.aspx)                                                                                                       | Introduced in Windows 10.0.10240.0 |
| [**ITfFunctionProvider**](https://msdn.microsoft.com/en-us/library/windows/apps/ms538979.aspx)                                                                                       | Introduced in Windows 10.0.10240.0 |
| [**ITfInputProcessorProfileActivationSink**](https://msdn.microsoft.com/en-us/library/windows/apps/aa381928.aspx)                                                 | Introduced in Windows 10.0.10240.0 |
| [**ITfInputProcessorProfileMgr**](https://msdn.microsoft.com/en-us/library/windows/apps/aa381941.aspx)                                                                       | Introduced in Windows 10.0.10240.0 |
| [**ITfInputScope**](https://msdn.microsoft.com/en-us/library/windows/apps/ms628582.aspx)                                                                                                   | Introduced in Windows 10.0.10240.0 |
| [**ITfInputScope2**](https://msdn.microsoft.com/en-us/library/windows/apps/aa382054.aspx)                                                                                                 | Introduced in Windows 10.0.10240.0 |
| [**ITfKeyEventSink**](https://msdn.microsoft.com/en-us/library/windows/apps/ms628601.aspx)                                                                                               | Introduced in Windows 10.0.10240.0 |
| [**ITfKeystrokeMgr**](https://msdn.microsoft.com/en-us/library/windows/apps/ms628676.aspx)                                                                                               | Introduced in Windows 10.0.10240.0 |
| [**ITfKeyTraceEventSink**](https://msdn.microsoft.com/en-us/library/windows/apps/ms628691.aspx)                                                                                     | Introduced in Windows 10.0.10240.0 |
| [**ITfLanguageProfileNotifySink**](https://msdn.microsoft.com/en-us/library/windows/apps/ms628769.aspx)                                                                     | Introduced in Windows 10.0.10240.0 |
| [**ITfPersistentPropertyLoaderACP**](https://msdn.microsoft.com/en-us/library/windows/apps/ms628877.aspx)                                                                 | Introduced in Windows 10.0.10240.0 |
| [**ITfPreservedKeyNotifySink**](https://msdn.microsoft.com/en-us/library/windows/apps/ms628879.aspx)                                                                           | Introduced in Windows 10.0.10240.0 |
| [**ITfProperty**](https://msdn.microsoft.com/en-us/library/windows/apps/ms628891.aspx)                                                                                                       | Introduced in Windows 10.0.10240.0 |
| [**ITfPropertyStore**](https://msdn.microsoft.com/en-us/library/windows/apps/ms628892.aspx)                                                                                             | Introduced in Windows 10.0.10240.0 |
| [**ITfRange**](https://msdn.microsoft.com/en-us/library/windows/apps/ms628908.aspx)                                                                                                             | Introduced in Windows 10.0.10240.0 |
| [**ITfRangeACP**](https://msdn.microsoft.com/en-us/library/windows/apps/ms628909.aspx)                                                                                                       | Introduced in Windows 10.0.10240.0 |
| [**ITfRangeBackup**](https://msdn.microsoft.com/en-us/library/windows/apps/ms628912.aspx)                                                                                                 | Introduced in Windows 10.0.10240.0 |
| [**ITfReadingInformationUIElement**](https://msdn.microsoft.com/en-us/library/windows/apps/aa382576.aspx)                                                                 | Introduced in Windows 10.0.10240.0 |
| [**ITfReadOnlyProperty**](https://msdn.microsoft.com/en-us/library/windows/apps/ms628936.aspx)                                                                                       | Introduced in Windows 10.0.10240.0 |
| [**ITfSource**](https://msdn.microsoft.com/en-us/library/windows/apps/ms628941.aspx)                                                                                                           | Introduced in Windows 10.0.10240.0 |
| [**ITfSourceSingle**](https://msdn.microsoft.com/en-us/library/windows/apps/ms628942.aspx)                                                                                               | Introduced in Windows 10.0.10240.0 |
| [**ITfTextEditSink**](https://msdn.microsoft.com/en-us/library/windows/apps/ms628962.aspx)                                                                                               | Introduced in Windows 10.0.10240.0 |
| [**ITfThreadMgr2**](https://msdn.microsoft.com/en-us/library/windows/apps/hh920960.aspx)                                                                                                   | Introduced in Windows 10.0.10240.0 |
| [**ITfUIElement**](https://msdn.microsoft.com/en-us/library/windows/apps/aa383175.aspx)                                                                                                     | Introduced in Windows 10.0.10240.0 |
| [**ITfUIElementMgr**](https://msdn.microsoft.com/en-us/library/windows/apps/aa383178.aspx)                                                                                               | Introduced in Windows 10.0.10240.0 |
| [**ITfUIElementSink**](https://msdn.microsoft.com/en-us/library/windows/apps/aa383201.aspx)                                                                                             | Introduced in Windows 10.0.10240.0 |
| [**IThumbnailStreamCache**](https://msdn.microsoft.com/en-us/library/windows/apps/mt438734.aspx)                                                                                 | Introduced in Windows 10.0.10240.0 |
| [**IToggleProvider**](https://msdn.microsoft.com/en-us/library/windows/apps/ee671396.aspx)                                                                                    | Introduced in Windows 10.0.10240.0 |
| [**ITransformProvider**](https://msdn.microsoft.com/en-us/library/windows/apps/ee671399.aspx)                                                                              | Introduced in Windows 10.0.10240.0 |
| [**ITransformProvider2**](https://msdn.microsoft.com/en-us/library/windows/apps/hh448824.aspx)                                                                            | Introduced in Windows 10.0.10240.0 |
| [**IUIAnimationInterpolator**](https://msdn.microsoft.com/en-us/library/windows/apps/dd371665.aspx)                                                                     | Introduced in Windows 10.0.10240.0 |
| [**IUIAnimationInterpolator2**](https://msdn.microsoft.com/en-us/library/windows/apps/hh437121.aspx)                                                                   | Introduced in Windows 10.0.10240.0 |
| [**IUIAnimationLoopIterationChangeHandler2**](https://msdn.microsoft.com/en-us/library/windows/apps/hh437133.aspx)                                       | Introduced in Windows 10.0.10240.0 |
| [**IUIAnimationManager**](https://msdn.microsoft.com/en-us/library/windows/apps/dd371687.aspx)                                                                               | Introduced in Windows 10.0.10240.0 |
| [**IUIAnimationManager2**](https://msdn.microsoft.com/en-us/library/windows/apps/hh437135.aspx)                                                                             | Introduced in Windows 10.0.10240.0 |
| [**IUIAnimationManagerEventHandler**](https://msdn.microsoft.com/en-us/library/windows/apps/dd371690.aspx)                                                       | Introduced in Windows 10.0.10240.0 |
| [**IUIAnimationManagerEventHandler2**](https://msdn.microsoft.com/en-us/library/windows/apps/hh437172.aspx)                                                     | Introduced in Windows 10.0.10240.0 |
| [**IUIAnimationPrimitiveInterpolation**](https://msdn.microsoft.com/en-us/library/windows/apps/hh437174.aspx)                                                 | Introduced in Windows 10.0.10240.0 |
| [**IUIAnimationPriorityComparison**](https://msdn.microsoft.com/en-us/library/windows/apps/dd371757.aspx)                                                         | Introduced in Windows 10.0.10240.0 |
| [**IUIAnimationPriorityComparison2**](https://msdn.microsoft.com/en-us/library/windows/apps/hh437176.aspx)                                                       | Introduced in Windows 10.0.10240.0 |
| [**IUIAnimationStoryboard**](https://msdn.microsoft.com/en-us/library/windows/apps/dd371761.aspx)                                                                         | Introduced in Windows 10.0.10240.0 |
| [**IUIAnimationStoryboard2**](https://msdn.microsoft.com/en-us/library/windows/apps/hh437178.aspx)                                                                       | Introduced in Windows 10.0.10240.0 |
| [**IUIAnimationStoryboardEventHandler**](https://msdn.microsoft.com/en-us/library/windows/apps/dd371764.aspx)                                                 | Introduced in Windows 10.0.10240.0 |
| [**IUIAnimationStoryboardEventHandler2**](https://msdn.microsoft.com/en-us/library/windows/apps/hh448599.aspx)                                               | Introduced in Windows 10.0.10240.0 |
| [**IUIAnimationTimer**](https://msdn.microsoft.com/en-us/library/windows/apps/dd371831.aspx)                                                                                   | Introduced in Windows 10.0.10240.0 |
| [**IUIAnimationTimerClientEventHandler**](https://msdn.microsoft.com/en-us/library/windows/apps/dd371834.aspx)                                               | Introduced in Windows 10.0.10240.0 |
| [**IUIAnimationTimerEventHandler**](https://msdn.microsoft.com/en-us/library/windows/apps/dd371841.aspx)                                                           | Introduced in Windows 10.0.10240.0 |
| [**IUIAnimationTimerUpdateHandler**](https://msdn.microsoft.com/en-us/library/windows/apps/dd371853.aspx)                                                         | Introduced in Windows 10.0.10240.0 |
| [**IUIAnimationTransition**](https://msdn.microsoft.com/en-us/library/windows/apps/dd371887.aspx)                                                                         | Introduced in Windows 10.0.10240.0 |
| [**IUIAnimationTransition2**](https://msdn.microsoft.com/en-us/library/windows/apps/hh448602.aspx)                                                                       | Introduced in Windows 10.0.10240.0 |
| [**IUIAnimationTransitionFactory**](https://msdn.microsoft.com/en-us/library/windows/apps/dd371891.aspx)                                                           | Introduced in Windows 10.0.10240.0 |
| [**IUIAnimationTransitionFactory2**](https://msdn.microsoft.com/en-us/library/windows/apps/hh448610.aspx)                                                         | Introduced in Windows 10.0.10240.0 |
| [**IUIAnimationTransitionLibrary**](https://msdn.microsoft.com/en-us/library/windows/apps/dd371897.aspx)                                                           | Introduced in Windows 10.0.10240.0 |
| [**IUIAnimationTransitionLibrary2**](https://msdn.microsoft.com/en-us/library/windows/apps/hh448612.aspx)                                                         | Introduced in Windows 10.0.10240.0 |
| [**IUIAnimationVariable**](https://msdn.microsoft.com/en-us/library/windows/apps/dd316797.aspx)                                                                             | Introduced in Windows 10.0.10240.0 |
| [**IUIAnimationVariable2**](https://msdn.microsoft.com/en-us/library/windows/apps/hh448632.aspx)                                                                           | Introduced in Windows 10.0.10240.0 |
| [**IUIAnimationVariableChangeHandler**](https://msdn.microsoft.com/en-us/library/windows/apps/dd316806.aspx)                                                   | Introduced in Windows 10.0.10240.0 |
| [**IUIAnimationVariableChangeHandler2**](https://msdn.microsoft.com/en-us/library/windows/apps/hh448659.aspx)                                                 | Introduced in Windows 10.0.10240.0 |
| [**IUIAnimationVariableCurveChangeHandler2**](https://msdn.microsoft.com/en-us/library/windows/apps/hh448661.aspx)                                       | Introduced in Windows 10.0.10240.0 |
| [**IUIAnimationVariableIntegerChangeHandler**](https://msdn.microsoft.com/en-us/library/windows/apps/dd316819.aspx)                                     | Introduced in Windows 10.0.10240.0 |
| [**IUIAnimationVariableIntegerChangeHandler2**](https://msdn.microsoft.com/en-us/library/windows/apps/hh448663.aspx)                                   | Introduced in Windows 10.0.10240.0 |
| [**IUIAutomationPatternHandler**](https://msdn.microsoft.com/en-us/library/windows/apps/ee696113.aspx)                                                            | Introduced in Windows 10.0.10240.0 |
| [**IUIAutomationPatternInstance**](https://msdn.microsoft.com/en-us/library/windows/apps/ee696116.aspx)                                                          | Introduced in Windows 10.0.10240.0 |
| [**IUIAutomationRegistrar**](https://msdn.microsoft.com/en-us/library/windows/apps/ee696161.aspx)                                                                      | Introduced in Windows 10.0.10240.0 |
| [**IUnknown**](https://msdn.microsoft.com/en-us/library/windows/apps/ms680509.aspx)                                                                                                             | Introduced in Windows 10.0.10240.0 |
| [**IUnknown**](https://msdn.microsoft.com/en-us/library/windows/apps/ms680509.aspx)                                                                                                             | Introduced in Windows 10.0.10240.0 |
| [**IValueProvider**](https://msdn.microsoft.com/en-us/library/windows/apps/ee671565.aspx)                                                                                      | Introduced in Windows 10.0.10240.0 |
| [**IVideoFrameNative**](https://msdn.microsoft.com/en-us/library/windows/apps/mt431704.aspx)                                                                                         | Introduced in Windows 10.0.10240.0 |
| [**IVideoFrameNativeFactory**](https://msdn.microsoft.com/en-us/library/windows/apps/mt431705.aspx)                                                                           | Introduced in Windows 10.0.10240.0 |
| [**IVirtualizedItemProvider**](https://msdn.microsoft.com/en-us/library/windows/apps/ee671569.aspx)                                                                  | Introduced in Windows 10.0.10240.0 |
| [**IVirtualSurfaceImageSourceNative**](https://msdn.microsoft.com/en-us/library/windows/apps/hh848328.aspx)                                                           | Introduced in Windows 10.0.10240.0 |
| [**IVirtualSurfaceUpdatesCallbackNative**](https://msdn.microsoft.com/en-us/library/windows/apps/hh848336.aspx)                                                   | Introduced in Windows 10.0.10240.0 |
| [**IWeakReference**](https://msdn.microsoft.com/en-us/library/windows/apps/br224608.aspx)                                                                                               | Introduced in Windows 10.0.10240.0 |
| [**IWeakReferenceSource**](https://msdn.microsoft.com/en-us/library/windows/apps/br224609.aspx)                                                                                   | Introduced in Windows 10.0.10240.0 |
| [**IWICBitmap**](https://msdn.microsoft.com/en-us/library/windows/apps/ee719675.aspx)                                                                                              | Introduced in Windows 10.0.10240.0 |
| [**IWICBitmapClipper**](https://msdn.microsoft.com/en-us/library/windows/apps/ee719676.aspx)                                                                                | Introduced in Windows 10.0.10240.0 |
| [**IWICBitmapCodecInfo**](https://msdn.microsoft.com/en-us/library/windows/apps/ee719679.aspx)                                                                            | Introduced in Windows 10.0.10240.0 |
| [**IWICBitmapCodecProgressNotification**](https://msdn.microsoft.com/en-us/library/windows/apps/ee690084.aspx)                                            | Introduced in Windows 10.0.10240.0 |
| [**IWICBitmapDecoder**](https://msdn.microsoft.com/en-us/library/windows/apps/ee690086.aspx)                                                                                | Introduced in Windows 10.0.10240.0 |
| [**IWICBitmapDecoderInfo**](https://msdn.microsoft.com/en-us/library/windows/apps/ee690087.aspx)                                                                        | Introduced in Windows 10.0.10240.0 |
| [**IWICBitmapEncoder**](https://msdn.microsoft.com/en-us/library/windows/apps/ee690110.aspx)                                                                                | Introduced in Windows 10.0.10240.0 |
| [**IWICBitmapEncoderInfo**](https://msdn.microsoft.com/en-us/library/windows/apps/ee690112.aspx)                                                                        | Introduced in Windows 10.0.10240.0 |
| [**IWICBitmapFlipRotator**](https://msdn.microsoft.com/en-us/library/windows/apps/ee690131.aspx)                                                                        | Introduced in Windows 10.0.10240.0 |
| [**IWICBitmapFrameDecode**](https://msdn.microsoft.com/en-us/library/windows/apps/ee690134.aspx)                                                                        | Introduced in Windows 10.0.10240.0 |
| [**IWICBitmapFrameEncode**](https://msdn.microsoft.com/en-us/library/windows/apps/ee690141.aspx)                                                                        | Introduced in Windows 10.0.10240.0 |
| [**IWICBitmapLock**](https://msdn.microsoft.com/en-us/library/windows/apps/ee690161.aspx)                                                                                      | Introduced in Windows 10.0.10240.0 |
| [**IWICBitmapScaler**](https://msdn.microsoft.com/en-us/library/windows/apps/ee690168.aspx)                                                                                  | Introduced in Windows 10.0.10240.0 |
| [**IWICBitmapSource**](https://msdn.microsoft.com/en-us/library/windows/apps/ee690171.aspx)                                                                                  | Introduced in Windows 10.0.10240.0 |
| [**IWICBitmapSourceTransform**](https://msdn.microsoft.com/en-us/library/windows/apps/ee690172.aspx)                                                                | Introduced in Windows 10.0.10240.0 |
| [**IWICColorContext**](https://msdn.microsoft.com/en-us/library/windows/apps/ee690193.aspx)                                                                                  | Introduced in Windows 10.0.10240.0 |
| [**IWICColorTransform**](https://msdn.microsoft.com/en-us/library/windows/apps/ee690201.aspx)                                                                              | Introduced in Windows 10.0.10240.0 |
| [**IWICComponentFactory**](https://msdn.microsoft.com/en-us/library/windows/apps/ee690203.aspx)                                                                          | Introduced in Windows 10.0.10240.0 |
| [**IWICComponentInfo**](https://msdn.microsoft.com/en-us/library/windows/apps/ee690213.aspx)                                                                                | Introduced in Windows 10.0.10240.0 |
| [**IWICDevelopRaw**](https://msdn.microsoft.com/en-us/library/windows/apps/ee690228.aspx)                                                                                      | Introduced in Windows 10.0.10240.0 |
| [**IWICDevelopRawNotificationCallback**](https://msdn.microsoft.com/en-us/library/windows/apps/ee690229.aspx)                                              | Introduced in Windows 10.0.10240.0 |
| [**IWICEnumMetadataItem**](https://msdn.microsoft.com/en-us/library/windows/apps/ee690264.aspx)                                                                          | Introduced in Windows 10.0.10240.0 |
| [**IWICFastMetadataEncoder**](https://msdn.microsoft.com/en-us/library/windows/apps/ee690269.aspx)                                                                    | Introduced in Windows 10.0.10240.0 |
| [**IWICFormatConverter**](https://msdn.microsoft.com/en-us/library/windows/apps/ee690274.aspx)                                                                            | Introduced in Windows 10.0.10240.0 |
| [**IWICFormatConverterInfo**](https://msdn.microsoft.com/en-us/library/windows/apps/ee690275.aspx)                                                                    | Introduced in Windows 10.0.10240.0 |
| [**IWICImageEncoder**](https://msdn.microsoft.com/en-us/library/windows/apps/hh880844.aspx)                                                                                             | Introduced in Windows 10.0.10240.0 |
| [**IWICImagingFactory**](https://msdn.microsoft.com/en-us/library/windows/apps/ee690281.aspx)                                                                              | Introduced in Windows 10.0.10240.0 |
| [**IWICImagingFactory2**](https://msdn.microsoft.com/en-us/library/windows/apps/hh880848.aspx)                                                                                       | Introduced in Windows 10.0.10240.0 |
| [**IWICMetadataBlockReader**](https://msdn.microsoft.com/en-us/library/windows/apps/ee690327.aspx)                                                                    | Introduced in Windows 10.0.10240.0 |
| [**IWICMetadataBlockWriter**](https://msdn.microsoft.com/en-us/library/windows/apps/ee690335.aspx)                                                                    | Introduced in Windows 10.0.10240.0 |
| [**IWICMetadataHandlerInfo**](https://msdn.microsoft.com/en-us/library/windows/apps/ee719700.aspx)                                                                    | Introduced in Windows 10.0.10240.0 |
| [**IWICMetadataQueryReader**](https://msdn.microsoft.com/en-us/library/windows/apps/ee719708.aspx)                                                                    | Introduced in Windows 10.0.10240.0 |
| [**IWICMetadataQueryWriter**](https://msdn.microsoft.com/en-us/library/windows/apps/ee719717.aspx)                                                                    | Introduced in Windows 10.0.10240.0 |
| [**IWICMetadataReader**](https://msdn.microsoft.com/en-us/library/windows/apps/ee719722.aspx)                                                                              | Introduced in Windows 10.0.10240.0 |
| [**IWICMetadataReaderInfo**](https://msdn.microsoft.com/en-us/library/windows/apps/ee719723.aspx)                                                                      | Introduced in Windows 10.0.10240.0 |
| [**IWICMetadataWriter**](https://msdn.microsoft.com/en-us/library/windows/apps/ee719733.aspx)                                                                              | Introduced in Windows 10.0.10240.0 |
| [**IWICMetadataWriterInfo**](https://msdn.microsoft.com/en-us/library/windows/apps/ee719734.aspx)                                                                      | Introduced in Windows 10.0.10240.0 |
| [**IWICPalette**](https://msdn.microsoft.com/en-us/library/windows/apps/ee719741.aspx)                                                                                            | Introduced in Windows 10.0.10240.0 |
| [**IWICPersistStream**](https://msdn.microsoft.com/en-us/library/windows/apps/ee719760.aspx)                                                                                | Introduced in Windows 10.0.10240.0 |
| [**IWICPixelFormatInfo**](https://msdn.microsoft.com/en-us/library/windows/apps/ee719763.aspx)                                                                            | Introduced in Windows 10.0.10240.0 |
| [**IWICPixelFormatInfo2**](https://msdn.microsoft.com/en-us/library/windows/apps/ee719764.aspx)                                                                          | Introduced in Windows 10.0.10240.0 |
| [**IWICProgressCallback**](https://msdn.microsoft.com/en-us/library/windows/apps/ee719775.aspx)                                                                          | Introduced in Windows 10.0.10240.0 |
| [**IWICProgressiveLevelControl**](https://msdn.microsoft.com/en-us/library/windows/apps/ee719778.aspx)                                                            | Introduced in Windows 10.0.10240.0 |
| [**IWICStream**](https://msdn.microsoft.com/en-us/library/windows/apps/ee719782.aspx)                                                                                              | Introduced in Windows 10.0.10240.0 |
| [**IWICStreamProvider**](https://msdn.microsoft.com/en-us/library/windows/apps/ee719783.aspx)                                                                              | Introduced in Windows 10.0.10240.0 |
| [**IWICDdsDecoder**](https://msdn.microsoft.com/en-us/library/windows/apps/dn302079.aspx)                                                                                                 | Introduced in Windows 10.0.10240.0 |
| [**IWICDdsEncoder**](https://msdn.microsoft.com/en-us/library/windows/apps/dn302082.aspx)                                                                                                 | Introduced in Windows 10.0.10240.0 |
| [**IWICDdsFrameDecode**](https://msdn.microsoft.com/en-us/library/windows/apps/dn302086.aspx)                                                                                         | Introduced in Windows 10.0.10240.0 |
| [**IWICPlanarBitmapFrameEncode**](https://msdn.microsoft.com/en-us/library/windows/apps/dn302090.aspx)                                                                       | Introduced in Windows 10.0.10240.0 |
| [**IWICPlanarBitmapSourceTransform**](https://msdn.microsoft.com/en-us/library/windows/apps/dn302093.aspx)                                                               | Introduced in Windows 10.0.10240.0 |
| [**IWICPlanarFormatConverter**](https://msdn.microsoft.com/en-us/library/windows/apps/dn302096.aspx)                                                                           | Introduced in Windows 10.0.10240.0 |
| [**IWICJpegFrameDecode**](https://msdn.microsoft.com/en-us/library/windows/apps/dn903834.aspx)                                                                                       | Introduced in Windows 10.0.10240.0 |
| [**IWICJpegFrameEncode**](https://msdn.microsoft.com/en-us/library/windows/apps/dn903864.aspx)                                                                                       | Introduced in Windows 10.0.10240.0 |
| [**IWindowProvider**](https://msdn.microsoft.com/en-us/library/windows/apps/ee671571.aspx)                                                                                    | Introduced in Windows 10.0.10240.0 |
| [**IWindowsDevicesAllJoynBusAttachmentFactoryInterop**](https://www.bing.com/search?q=IWindowsDevicesAllJoynBusAttachmentFactoryInterop) | Introduced in Windows 10.0.10240.0 |
| [**IWindowsDevicesAllJoynBusAttachmentInterop**](https://www.bing.com/search?q=IWindowsDevicesAllJoynBusAttachmentInterop)               | Introduced in Windows 10.0.10240.0 |
| [**IWorkspaceBrokerAx**](https://www.bing.com/search?q=IWorkspaceBrokerAx)                                                               | Introduced in Windows 10.0.10240.0 |
| [**IWorkspaceBrokerAx2**](https://www.bing.com/search?q=IWorkspaceBrokerAx2)                                                             | Introduced in Windows 10.0.10240.0 |
| [**IXAPO**](https://msdn.microsoft.com/en-us/library/windows/apps/microsoft.directx_sdk.ixapo.ixapo.aspx)                                                                                                               | Introduced in Windows 10.0.10240.0 |
| [**IXAPOHrtfParameters**](https://msdn.microsoft.com/en-us/library/windows/apps/mt186608.aspx)                                                                                   | Introduced in Windows 10.0.10240.0 |
| [**IXAPOParameters**](https://msdn.microsoft.com/en-us/library/windows/apps/microsoft.directx_sdk.ixapoparameters.ixapoparameters.aspx)                                                                                           | Introduced in Windows 10.0.10240.0 |
| [**IXAudio2**](https://msdn.microsoft.com/en-us/library/windows/apps/microsoft.directx_sdk.ixaudio2.ixaudio2.aspx)                                                                                                         | Introduced in Windows 10.0.10240.0 |
| [**IXAudio2EngineCallback**](https://msdn.microsoft.com/en-us/library/windows/apps/microsoft.directx_sdk.ixaudio2enginecallback.ixaudio2enginecallback.aspx)                                                                             | Introduced in Windows 10.0.10240.0 |
| [**IXAudio2MasteringVoice**](https://msdn.microsoft.com/en-us/library/windows/apps/microsoft.directx_sdk.ixaudio2masteringvoice.ixaudio2masteringvoice.aspx)                                                                             | Introduced in Windows 10.0.10240.0 |
| [**IXAudio2SourceVoice**](https://msdn.microsoft.com/en-us/library/windows/apps/microsoft.directx_sdk.ixaudio2sourcevoice.ixaudio2sourcevoice.aspx)                                                                                   | Introduced in Windows 10.0.10240.0 |
| [**IXAudio2SubmixVoice**](https://msdn.microsoft.com/en-us/library/windows/apps/microsoft.directx_sdk.ixaudio2submixvoice.ixaudio2submixvoice.aspx)                                                                                   | Introduced in Windows 10.0.10240.0 |
| [**IXAudio2Voice**](https://msdn.microsoft.com/en-us/library/windows/apps/microsoft.directx_sdk.ixaudio2voice.ixaudio2voice.aspx)                                                                                               | Introduced in Windows 10.0.10240.0 |
| [**IXAudio2VoiceCallback**](https://msdn.microsoft.com/en-us/library/windows/apps/microsoft.directx_sdk.ixaudio2voicecallback.ixaudio2voicecallback.aspx)                                                                               | Introduced in Windows 10.0.10240.0 |
| [**IXMLHTTPRequest2**](https://msdn.microsoft.com/en-us/library/windows/apps/hh831151.aspx)                                                                                           | Introduced in Windows 10.0.10240.0 |
| [**IXMLHTTPRequest2Callback**](https://msdn.microsoft.com/en-us/library/windows/apps/hh831152.aspx)                                                                           | Introduced in Windows 10.0.10240.0 |
| [**IXMLHTTPRequest3**](https://msdn.microsoft.com/en-us/library/windows/apps/dn376398.aspx)                                                                                           | Introduced in Windows 10.0.10240.0 |
| [**IXMLHTTPRequest3Callback**](https://msdn.microsoft.com/en-us/library/windows/apps/dn376399.aspx)                                                                           | Introduced in Windows 10.0.10240.0 |
| [**IXmlReader**](https://www.bing.com/search?q=IXmlReader)                                                                               | Introduced in Windows 10.0.10240.0 |
| [**IXmlReaderInput**](https://www.bing.com/search?q=IXmlReaderInput)                                                                     | Introduced in Windows 10.0.10240.0 |
| [**IXmlResolver**](https://www.bing.com/search?q=IXmlResolver)                                                                           | Introduced in Windows 10.0.10240.0 |
| [**IXmlWriter**](https://www.bing.com/search?q=IXmlWriter)                                                                               | Introduced in Windows 10.0.10240.0 |
| [**IXmlWriterLite**](https://www.bing.com/search?q=IXmlWriterLite)                                                                       | Introduced in Windows 10.0.10240.0 |
| [**IXmlWriterOutput**](https://www.bing.com/search?q=IXmlWriterOutput)                                                                   | Introduced in Windows 10.0.10240.0 |
| [**IXpsDocumentPackageTarget**](https://msdn.microsoft.com/en-us/library/windows/apps/hh994456.aspx)                                                                           | Introduced in Windows 10.0.10240.0 |
| [**IXpsDocumentPackageTarget3D**](https://msdn.microsoft.com/en-us/library/windows/apps/dn280684.aspx)                                                                       | Introduced in Windows 10.0.10240.0 |
| [**IXpsOMBrush**](https://msdn.microsoft.com/en-us/library/windows/apps/dd317026.aspx)                                                                                                       | Introduced in Windows 10.0.10240.0 |
| [**IXpsOMCanvas**](https://msdn.microsoft.com/en-us/library/windows/apps/dd317033.aspx)                                                                                                     | Introduced in Windows 10.0.10240.0 |
| [**IXpsOMColorProfileResource**](https://msdn.microsoft.com/en-us/library/windows/apps/dd372020.aspx)                                                                         | Introduced in Windows 10.0.10240.0 |
| [**IXpsOMColorProfileResourceCollection**](https://msdn.microsoft.com/en-us/library/windows/apps/dd372023.aspx)                                                     | Introduced in Windows 10.0.10240.0 |
| [**IXpsOMCoreProperties**](https://msdn.microsoft.com/en-us/library/windows/apps/dd372040.aspx)                                                                                     | Introduced in Windows 10.0.10240.0 |
| [**IXpsOMDashCollection**](https://msdn.microsoft.com/en-us/library/windows/apps/dd372105.aspx)                                                                                     | Introduced in Windows 10.0.10240.0 |
| [**IXpsOMDictionary**](https://msdn.microsoft.com/en-us/library/windows/apps/dd372128.aspx)                                                                                             | Introduced in Windows 10.0.10240.0 |
| [**IXpsOMDocument**](https://msdn.microsoft.com/en-us/library/windows/apps/dd372155.aspx)                                                                                                 | Introduced in Windows 10.0.10240.0 |
| [**IXpsOMDocumentCollection**](https://msdn.microsoft.com/en-us/library/windows/apps/dd372157.aspx)                                                                             | Introduced in Windows 10.0.10240.0 |
| [**IXpsOMDocumentSequence**](https://msdn.microsoft.com/en-us/library/windows/apps/dd372363.aspx)                                                                                 | Introduced in Windows 10.0.10240.0 |
| [**IXpsOMDocumentStructureResource**](https://msdn.microsoft.com/en-us/library/windows/apps/dd372377.aspx)                                                               | Introduced in Windows 10.0.10240.0 |
| [**IXpsOMFontResource**](https://msdn.microsoft.com/en-us/library/windows/apps/dd372415.aspx)                                                                                         | Introduced in Windows 10.0.10240.0 |
| [**IXpsOMFontResourceCollection**](https://msdn.microsoft.com/en-us/library/windows/apps/dd372419.aspx)                                                                     | Introduced in Windows 10.0.10240.0 |
| [**IXpsOMGeometry**](https://msdn.microsoft.com/en-us/library/windows/apps/dd372455.aspx)                                                                                                 | Introduced in Windows 10.0.10240.0 |
| [**IXpsOMGeometryFigure**](https://msdn.microsoft.com/en-us/library/windows/apps/dd372457.aspx)                                                                                     | Introduced in Windows 10.0.10240.0 |
| [**IXpsOMGeometryFigureCollection**](https://msdn.microsoft.com/en-us/library/windows/apps/dd372461.aspx)                                                                 | Introduced in Windows 10.0.10240.0 |
| [**IXpsOMGlyphs**](https://msdn.microsoft.com/en-us/library/windows/apps/dd317087.aspx)                                                                                                     | Introduced in Windows 10.0.10240.0 |
| [**IXpsOMGlyphsEditor**](https://msdn.microsoft.com/en-us/library/windows/apps/dd317088.aspx)                                                                                         | Introduced in Windows 10.0.10240.0 |
| [**IXpsOMGradientBrush**](https://msdn.microsoft.com/en-us/library/windows/apps/dd317230.aspx)                                                                                       | Introduced in Windows 10.0.10240.0 |
| [**IXpsOMGradientStop**](https://msdn.microsoft.com/en-us/library/windows/apps/dd317250.aspx)                                                                                         | Introduced in Windows 10.0.10240.0 |
| [**IXpsOMGradientStopCollection**](https://msdn.microsoft.com/en-us/library/windows/apps/dd317252.aspx)                                                                     | Introduced in Windows 10.0.10240.0 |
| [**IXpsOMImageBrush**](https://msdn.microsoft.com/en-us/library/windows/apps/dd317277.aspx)                                                                                             | Introduced in Windows 10.0.10240.0 |
| [**IXpsOMImageResource**](https://msdn.microsoft.com/en-us/library/windows/apps/dd317289.aspx)                                                                                       | Introduced in Windows 10.0.10240.0 |
| [**IXpsOMImageResourceCollection**](https://msdn.microsoft.com/en-us/library/windows/apps/dd317291.aspx)                                                                   | Introduced in Windows 10.0.10240.0 |
| [**IXpsOMLinearGradientBrush**](https://msdn.microsoft.com/en-us/library/windows/apps/dd317306.aspx)                                                                           | Introduced in Windows 10.0.10240.0 |
| [**IXpsOMMatrixTransform**](https://msdn.microsoft.com/en-us/library/windows/apps/dd372495.aspx)                                                                                   | Introduced in Windows 10.0.10240.0 |
| [**IXpsOMNameCollection**](https://msdn.microsoft.com/en-us/library/windows/apps/dd372502.aspx)                                                                                     | Introduced in Windows 10.0.10240.0 |
| [**IXpsOMObjectFactory**](https://msdn.microsoft.com/en-us/library/windows/apps/dd372509.aspx)                                                                                       | Introduced in Windows 10.0.10240.0 |
| [**IXpsOMObjectFactory1**](https://msdn.microsoft.com/en-us/library/windows/apps/hh448399.aspx)                                                                                     | Introduced in Windows 10.0.10240.0 |
| [**IXpsOMPackage**](https://msdn.microsoft.com/en-us/library/windows/apps/dd372618.aspx)                                                                                                   | Introduced in Windows 10.0.10240.0 |
| [**IXpsOMPackage1**](https://msdn.microsoft.com/en-us/library/windows/apps/hh448410.aspx)                                                                                                 | Introduced in Windows 10.0.10240.0 |
| [**IXpsOMPackageTarget**](https://msdn.microsoft.com/en-us/library/windows/apps/ff970304.aspx)                                                                                       | Introduced in Windows 10.0.10240.0 |
| [**IXpsOMPackageWriter**](https://msdn.microsoft.com/en-us/library/windows/apps/dd372619.aspx)                                                                                       | Introduced in Windows 10.0.10240.0 |
| [**IXpsOMPackageWriter3D**](https://msdn.microsoft.com/en-us/library/windows/apps/dn280743.aspx)                                                                                   | Introduced in Windows 10.0.10240.0 |
| [**IXpsOMPage**](https://msdn.microsoft.com/en-us/library/windows/apps/dd372635.aspx)                                                                                                         | Introduced in Windows 10.0.10240.0 |
| [**IXpsOMPage1**](https://msdn.microsoft.com/en-us/library/windows/apps/hh448414.aspx)                                                                                                       | Introduced in Windows 10.0.10240.0 |
| [**IXpsOMPageReference**](https://msdn.microsoft.com/en-us/library/windows/apps/dd372636.aspx)                                                                                       | Introduced in Windows 10.0.10240.0 |
| [**IXpsOMPageReferenceCollection**](https://msdn.microsoft.com/en-us/library/windows/apps/dd372637.aspx)                                                                   | Introduced in Windows 10.0.10240.0 |
| [**IXpsOMPart**](https://msdn.microsoft.com/en-us/library/windows/apps/dd372684.aspx)                                                                                                         | Introduced in Windows 10.0.10240.0 |
| [**IXpsOMPartResources**](https://msdn.microsoft.com/en-us/library/windows/apps/dd372685.aspx)                                                                                       | Introduced in Windows 10.0.10240.0 |
| [**IXpsOMPartUriCollection**](https://msdn.microsoft.com/en-us/library/windows/apps/dd372690.aspx)                                                                               | Introduced in Windows 10.0.10240.0 |
| [**IXpsOMPath**](https://msdn.microsoft.com/en-us/library/windows/apps/dd372699.aspx)                                                                                                         | Introduced in Windows 10.0.10240.0 |
| [**IXpsOMPrintTicketResource**](https://msdn.microsoft.com/en-us/library/windows/apps/dd372740.aspx)                                                                           | Introduced in Windows 10.0.10240.0 |
| [**IXpsOMRadialGradientBrush**](https://msdn.microsoft.com/en-us/library/windows/apps/dd372743.aspx)                                                                           | Introduced in Windows 10.0.10240.0 |
| [**IXpsOMRemoteDictionaryResource**](https://msdn.microsoft.com/en-us/library/windows/apps/dd372751.aspx)                                                                 | Introduced in Windows 10.0.10240.0 |
| [**IXpsOMRemoteDictionaryResource1**](https://msdn.microsoft.com/en-us/library/windows/apps/jj159899.aspx)                                                               | Introduced in Windows 10.0.10240.0 |
| [**IXpsOMRemoteDictionaryResourceCollection**](https://msdn.microsoft.com/en-us/library/windows/apps/dd372752.aspx)                                             | Introduced in Windows 10.0.10240.0 |
| [**IXpsOMResource**](https://msdn.microsoft.com/en-us/library/windows/apps/dd372762.aspx)                                                                                                 | Introduced in Windows 10.0.10240.0 |
| [**IXpsOMShareable**](https://msdn.microsoft.com/en-us/library/windows/apps/dd372763.aspx)                                                                                               | Introduced in Windows 10.0.10240.0 |
| [**IXpsOMSignatureBlockResource**](https://msdn.microsoft.com/en-us/library/windows/apps/dd372766.aspx)                                                                     | Introduced in Windows 10.0.10240.0 |
| [**IXpsOMSignatureBlockResourceCollection**](https://msdn.microsoft.com/en-us/library/windows/apps/dd372767.aspx)                                                 | Introduced in Windows 10.0.10240.0 |
| [**IXpsOMSolidColorBrush**](https://msdn.microsoft.com/en-us/library/windows/apps/dd372779.aspx)                                                                                   | Introduced in Windows 10.0.10240.0 |
| [**IXpsOMStoryFragmentsResource**](https://msdn.microsoft.com/en-us/library/windows/apps/dd372783.aspx)                                                                     | Introduced in Windows 10.0.10240.0 |
| [**IXpsOMTileBrush**](https://msdn.microsoft.com/en-us/library/windows/apps/dd372789.aspx)                                                                                               | Introduced in Windows 10.0.10240.0 |
| [**IXpsOMVisual**](https://msdn.microsoft.com/en-us/library/windows/apps/dd372801.aspx)                                                                                                     | Introduced in Windows 10.0.10240.0 |
| [**IXpsOMVisualBrush**](https://msdn.microsoft.com/en-us/library/windows/apps/dd372802.aspx)                                                                                           | Introduced in Windows 10.0.10240.0 |
| [**IXpsOMVisualCollection**](https://msdn.microsoft.com/en-us/library/windows/apps/dd372809.aspx)                                                                                 | Introduced in Windows 10.0.10240.0 |
| [**IBtRadioController**](https://www.bing.com/search?q=IBtRadioController)                                                               | Introduced in Windows 10.0.10586.0 |
| [**IBtCommandCallback**](https://www.bing.com/search?q=IBtCommandCallback)                                                               | Introduced in Windows 10.0.10586.0 |
| [**IBtConnectionObserver**](https://www.bing.com/search?q=IBtConnectionObserver)                                                         | Introduced in Windows 10.0.10586.0 |
| [**IBtConnectionObserverCallback**](https://www.bing.com/search?q=IBtConnectionObserverCallback)                                         | Introduced in Windows 10.0.10586.0 |
| [**IBtConnectionObserverCallback2**](https://www.bing.com/search?q=IBtConnectionObserverCallback2)                                       | Introduced in Windows 10.0.10586.0 |
| [**IBtPairingRequest**](https://www.bing.com/search?q=IBtPairingRequest)                                                                 | Introduced in Windows 10.0.10586.0 |
| [**IBtPairingRequestCallback**](https://www.bing.com/search?q=IBtPairingRequestCallback)                                                 | Introduced in Windows 10.0.10586.0 |
| [**IBtIncomingPairingCallback**](https://www.bing.com/search?q=IBtIncomingPairingCallback)                                               | Introduced in Windows 10.0.10586.0 |
| [**ID3D11Device4**](https://msdn.microsoft.com/en-us/library/windows/apps/mt589889.aspx)                                                                                            | Introduced in Windows 10.0.10586.0 |
| [**IAppxBlockMapBlock**](https://msdn.microsoft.com/en-us/library/windows/apps/hh446630.aspx)                                                                                     | Introduced in Windows 10.0.14393.0 |
| [**IAppxBlockMapBlocksEnumerator**](https://msdn.microsoft.com/en-us/library/windows/apps/hh446631.aspx)                                                               | Introduced in Windows 10.0.14393.0 |
| [**IAppxBlockMapFile**]https://msdn.microsoft.com/en-us/library/windows/apps/hh446637.aspx)                                                                                       | Introduced in Windows 10.0.14393.0 |
| [**IAppxBlockMapFilesEnumerator**](https://msdn.microsoft.com/en-us/library/windows/apps/hh446638.aspx)                                                                 | Introduced in Windows 10.0.14393.0 |
| [**IAppxBlockMapReader**](https://msdn.microsoft.com/en-us/library/windows/apps/hh446651.aspx)                                                                                   | Introduced in Windows 10.0.14393.0 |
| [**IAppxBundleFactory**](https://msdn.microsoft.com/en-us/library/windows/apps/dn280277.aspx)                                                                                     | Introduced in Windows 10.0.14393.0 |
| [**IAppxBundleWriter**](https://msdn.microsoft.com/en-us/library/windows/apps/dn280302.aspx)                                                                                       | Introduced in Windows 10.0.14393.0 |
| [**IAppxBundleReader**](https://msdn.microsoft.com/en-us/library/windows/apps/dn280296.aspx)                                                                                       | Introduced in Windows 10.0.14393.0 |
| [**IAppxBundleManifestReader**](https://msdn.microsoft.com/en-us/library/windows/apps/dn280292.aspx)                                                                       | Introduced in Windows 10.0.14393.0 |
| [**IAppxBundleManifestPackageInfoEnumerator**](https://msdn.microsoft.com/en-us/library/windows/apps/dn280282.aspx)                                         | Introduced in Windows 10.0.14393.0 |
| [**IAppxBundleManifestPackageInfo**](https://msdn.microsoft.com/en-us/library/windows/apps/dn280281.aspx)                                                             | Introduced in Windows 10.0.14393.0 |
| [**IAppxFactory**](https://msdn.microsoft.com/en-us/library/windows/apps/hh446671.aspx)                                                                                                 | Introduced in Windows 10.0.14393.0 |
| [**IAppxFile**](https://msdn.microsoft.com/en-us/library/windows/apps/hh446683.aspx)                                                                                                       | Introduced in Windows 10.0.14393.0 |
| [**IAppxFilesEnumerator**](https://msdn.microsoft.com/en-us/library/windows/apps/hh446685.aspx)                                                                                 | Introduced in Windows 10.0.14393.0 |
| [**IAppxManifestApplication**](https://msdn.microsoft.com/en-us/library/windows/apps/hh446697.aspx)                                                                         | Introduced in Windows 10.0.14393.0 |
| [**IAppxManifestApplicationsEnumerator**](https://msdn.microsoft.com/en-us/library/windows/apps/hh446698.aspx)                                                   | Introduced in Windows 10.0.14393.0 |
| [**IAppxManifestQualifiedResource**](https://msdn.microsoft.com/en-us/library/windows/apps/dn280305.aspx)                                                             | Introduced in Windows 10.0.14393.0 |
| [**IAppxManifestQualifiedResourcesEnumerator**](https://msdn.microsoft.com/en-us/library/windows/apps/dn280306.aspx)                                       | Introduced in Windows 10.0.14393.0 |
| [**IAppxPackageReader**](https://msdn.microsoft.com/en-us/library/windows/apps/hh446756.aspx)                                                                                     | Introduced in Windows 10.0.14393.0 |
| [**IAppxPackageWriter**](https://msdn.microsoft.com/en-us/library/windows/apps/hh446762.aspx)                                                                                     | Introduced in Windows 10.0.14393.0 |
| [**IAppxManifestDeviceCapabilitiesEnumerator**](https://msdn.microsoft.com/en-us/library/windows/apps/hh446704.aspx)                                       | Introduced in Windows 10.0.14393.0 |
| [**IAppxManifestPackageId**](https://msdn.microsoft.com/en-us/library/windows/apps/hh446717.aspx)                                                                             | Introduced in Windows 10.0.14393.0 |
| [**IAppxManifestPackageDependency**](https://msdn.microsoft.com/en-us/library/windows/apps/hh446713.aspx)                                                             | Introduced in Windows 10.0.14393.0 |
| [**IAppxManifestPackageDependenciesEnumerator**](https://msdn.microsoft.com/en-us/library/windows/apps/hh446708.aspx)                                     | Introduced in Windows 10.0.14393.0 |
| [**IAppxManifestProperties**](https://msdn.microsoft.com/en-us/library/windows/apps/hh446731.aspx)                                                                           | Introduced in Windows 10.0.14393.0 |
| [**IAppxManifestReader**](https://msdn.microsoft.com/en-us/library/windows/apps/hh446737.aspx)                                                                                   | Introduced in Windows 10.0.14393.0 |
| [**IAppxManifestReader2**](https://msdn.microsoft.com/en-us/library/windows/apps/dn280312.aspx)                                                                                 | Introduced in Windows 10.0.14393.0 |
| [**IAppxManifestReader3**](https://www.bing.com/search?q=IAppxManifestReader3)                                                           | Introduced in Windows 10.0.14393.0 |
| [**IAppxManifestCapabilitiesEnumerator**](https://www.bing.com/search?q=IAppxManifestCapabilitiesEnumerator)                             | Introduced in Windows 10.0.14393.0 |
| [**IAppxManifestTargetDeviceFamiliesEnumerator**](https://www.bing.com/search?q=IAppxManifestTargetDeviceFamiliesEnumerator)             | Introduced in Windows 10.0.14393.0 |
| [**IAppxManifestTargetDeviceFamily**](https://www.bing.com/search?q=IAppxManifestTargetDeviceFamily)                                     | Introduced in Windows 10.0.14393.0 |
| [**IAppxManifestPackageDependency2**](https://www.bing.com/search?q=IAppxManifestPackageDependency2)                                     | Introduced in Windows 10.0.14393.0 |
| [**IAppxManifestResourcesEnumerator**](https://msdn.microsoft.com/en-us/library/windows/apps/hh446752.aspx)                                                         | Introduced in Windows 10.0.14393.0 |
| [**IAppxManifestReader4**](https://www.bing.com/search?q=IAppxManifestReader4)                                                           | Introduced in Windows 10.0.14393.0 |
| [**IAppxManifestOptionalPackageInfo**](https://www.bing.com/search?q=IAppxManifestOptionalPackageInfo)                                   | Introduced in Windows 10.0.14393.0 |
| [**IXblIdpAuthManager**](https://www.bing.com/search?q=IXblIdpAuthManager)                                                               | Introduced in Windows 10.0.14393.0 |
| [**IXblIdpAuthTokenResult**](https://www.bing.com/search?q=IXblIdpAuthTokenResult)                                                       | Introduced in Windows 10.0.14393.0 |

 

## <span id="_com_coclasses"></span><span id="_COM_COCLASSES"></span>COM coclasses


| API                                                                                                                       | Requirements                       |
|---------------------------------------------------------------------------------------------------------------------------|------------------------------------|
| [**AudioReverb**](https://www.bing.com/search?q=AudioReverb)                                                              | Introduced in Windows 10.0.10240.0 |
| [**AudioVolumeMeter**](https://www.bing.com/search?q=AudioVolumeMeter)                                                    | Introduced in Windows 10.0.10240.0 |
| [**AoWAppActivatedRuntime**](https://www.bing.com/search?q=AoWAppActivatedRuntime)                                        | Introduced in Windows 10.0.10240.0 |
| [**AoWBackgroundTaskRuntime**](https://www.bing.com/search?q=AoWBackgroundTaskRuntime)                                    | Introduced in Windows 10.0.10240.0 |
| [**CameraUIControl**](https://www.bing.com/search?q=CameraUIControl)                                                      | Introduced in Windows 10.0.10240.0 |
| [**CLSID\_AudioFrameNativeFactory**](https://www.bing.com/search?q=CLSID_AudioFrameNativeFactory)                         | Introduced in Windows 10.0.10240.0 |
| [**CLSID\_CMultiLanguage**](https://www.bing.com/search?q=CLSID_CMultiLanguage)                                           | Introduced in Windows 10.0.10240.0 |
| [**CLSID\_CUIAutomationRegistrar**](https://www.bing.com/search?q=CLSID_CUIAutomationRegistrar)                           | Introduced in Windows 10.0.10240.0 |
| [**CLSID\_DeviceIoControl**](https://www.bing.com/search?q=CLSID_DeviceIoControl)                                         | Introduced in Windows 10.0.10240.0 |
| [**CLSID\_DShowSourceResolver**](https://www.bing.com/search?q=CLSID_DShowSourceResolver)                                 | Introduced in Windows 10.0.10240.0 |
| [**CLSID\_FreeThreadedXMLHTTP60**](https://www.bing.com/search?q=CLSID_FreeThreadedXMLHTTP60)                             | Introduced in Windows 10.0.10240.0 |
| [**CLSID\_GlobalOptions**](https://www.bing.com/search?q=CLSID_GlobalOptions)                                             | Introduced in Windows 10.0.10240.0 |
| [**CLSID\_InProcFreeMarshaler**](https://www.bing.com/search?q=CLSID_InProcFreeMarshaler)                                 | Introduced in Windows 10.0.10240.0 |
| [**CLSID\_MbnConnectionManager**](https://www.bing.com/search?q=CLSID_MbnConnectionManager)                               | Introduced in Windows 10.0.10240.0 |
| [**CLSID\_MbnDeviceServicesManager**](https://www.bing.com/search?q=CLSID_MbnDeviceServicesManager)                       | Introduced in Windows 10.0.10240.0 |
| [**CLSID\_MbnInterfaceManager**](https://www.bing.com/search?q=CLSID_MbnInterfaceManager)                                 | Introduced in Windows 10.0.10240.0 |
| [**CLSID\_MFMediaEngineClassFactory**](https://www.bing.com/search?q=CLSID_MFMediaEngineClassFactory)                     | Introduced in Windows 10.0.10240.0 |
| [**CLSID\_MFReadWriteClassFactory**](https://www.bing.com/search?q=CLSID_MFReadWriteClassFactory)                         | Introduced in Windows 10.0.10240.0 |
| [**CLSID\_MPEG2ByteStreamPlugin**](https://www.bing.com/search?q=CLSID_MPEG2ByteStreamPlugin)                             | Introduced in Windows 10.0.10240.0 |
| [**CLSID\_NetSchemePlugin**](https://www.bing.com/search?q=CLSID_NetSchemePlugin)                                         | Introduced in Windows 10.0.10240.0 |
| [**CLSID\_OpcFactory**](https://www.bing.com/search?q=CLSID_OpcFactory)                                                   | Introduced in Windows 10.0.10240.0 |
| [**CLSID\_PortableDevice**](https://www.bing.com/search?q=CLSID_PortableDevice)                                           | Introduced in Windows 10.0.10240.0 |
| [**CLSID\_PortableDeviceDispatchFactory**](https://www.bing.com/search?q=CLSID_PortableDeviceDispatchFactory)             | Introduced in Windows 10.0.10240.0 |
| [**CLSID\_PortableDeviceFTM**](https://www.bing.com/search?q=CLSID_PortableDeviceFTM)                                     | Introduced in Windows 10.0.10240.0 |
| [**CLSID\_PortableDeviceKeyCollection**](https://www.bing.com/search?q=CLSID_PortableDeviceKeyCollection)                 | Introduced in Windows 10.0.10240.0 |
| [**CLSID\_PortableDeviceManager**](https://www.bing.com/search?q=CLSID_PortableDeviceManager)                             | Introduced in Windows 10.0.10240.0 |
| [**CLSID\_PortableDevicePropVariantCollection**](https://www.bing.com/search?q=CLSID_PortableDevicePropVariantCollection) | Introduced in Windows 10.0.10240.0 |
| [**CLSID\_PortableDeviceService**](https://www.bing.com/search?q=CLSID_PortableDeviceService)                             | Introduced in Windows 10.0.10240.0 |
| [**CLSID\_PortableDeviceServiceFTM**](https://www.bing.com/search?q=CLSID_PortableDeviceServiceFTM)                       | Introduced in Windows 10.0.10240.0 |
| [**CLSID\_PortableDeviceValues**](https://www.bing.com/search?q=CLSID_PortableDeviceValues)                               | Introduced in Windows 10.0.10240.0 |
| [**CLSID\_PortableDeviceValuesCollection**](https://www.bing.com/search?q=CLSID_PortableDeviceValuesCollection)           | Introduced in Windows 10.0.10240.0 |
| [**CLSID\_RemoteDesktopClient**](https://www.bing.com/search?q=CLSID_RemoteDesktopClient)                                 | Introduced in Windows 10.0.10240.0 |
| [**CLSID\_SoftwareBitmapNativeFactory**](https://www.bing.com/search?q=CLSID_SoftwareBitmapNativeFactory)                 | Introduced in Windows 10.0.10240.0 |
| [**CLSID\_StdGlobalInterfaceTable**](https://www.bing.com/search?q=CLSID_StdGlobalInterfaceTable)                         | Introduced in Windows 10.0.10240.0 |
| [**CLSID\_TF\_CategoryMgr**](https://www.bing.com/search?q=CLSID_TF_CategoryMgr)                                          | Introduced in Windows 10.0.10240.0 |
| [**CLSID\_TF\_DisplayAttributeMgr**](https://www.bing.com/search?q=CLSID_TF_DisplayAttributeMgr)                          | Introduced in Windows 10.0.10240.0 |
| [**CLSID\_TF\_InputProcessorProfiles**](https://www.bing.com/search?q=CLSID_TF_InputProcessorProfiles)                    | Introduced in Windows 10.0.10240.0 |
| [**CLSID\_TF\_ThreadMgr**](https://www.bing.com/search?q=CLSID_TF_ThreadMgr)                                              | Introduced in Windows 10.0.10240.0 |
| [**CLSID\_ThumbnailStreamCache**](https://www.bing.com/search?q=CLSID_ThumbnailStreamCache)                               | Introduced in Windows 10.0.10240.0 |
| [**CLSID\_UIAnimationManager**](https://www.bing.com/search?q=CLSID_UIAnimationManager)                                   | Introduced in Windows 10.0.10240.0 |
| [**CLSID\_UIAnimationManager2**](https://www.bing.com/search?q=CLSID_UIAnimationManager2)                                 | Introduced in Windows 10.0.10240.0 |
| [**CLSID\_UIAnimationTimer**](https://www.bing.com/search?q=CLSID_UIAnimationTimer)                                       | Introduced in Windows 10.0.10240.0 |
| [**CLSID\_UIAnimationTransitionFactory**](https://www.bing.com/search?q=CLSID_UIAnimationTransitionFactory)               | Introduced in Windows 10.0.10240.0 |
| [**CLSID\_UIAnimationTransitionFactory2**](https://www.bing.com/search?q=CLSID_UIAnimationTransitionFactory2)             | Introduced in Windows 10.0.10240.0 |
| [**CLSID\_UIAnimationTransitionLibrary**](https://www.bing.com/search?q=CLSID_UIAnimationTransitionLibrary)               | Introduced in Windows 10.0.10240.0 |
| [**CLSID\_UIAnimationTransitionLibrary2**](https://www.bing.com/search?q=CLSID_UIAnimationTransitionLibrary2)             | Introduced in Windows 10.0.10240.0 |
| [**CLSID\_VideoFrameNativeFactory**](https://www.bing.com/search?q=CLSID_VideoFrameNativeFactory)                         | Introduced in Windows 10.0.10240.0 |
| [**CLSID\_WICImagingFactory**](https://www.bing.com/search?q=CLSID_WICImagingFactory)                                     | Introduced in Windows 10.0.10240.0 |
| [**CLSID\_WICImagingFactory1**](https://www.bing.com/search?q=CLSID_WICImagingFactory1)                                   | Introduced in Windows 10.0.10240.0 |
| [**CLSID\_WICImagingFactory2**](https://www.bing.com/search?q=CLSID_WICImagingFactory2)                                   | Introduced in Windows 10.0.10240.0 |
| [**CLSID\_XpsOMObjectFactory**](https://www.bing.com/search?q=CLSID_XpsOMObjectFactory)                                   | Introduced in Windows 10.0.10240.0 |
| [**FXEcho**](https://www.bing.com/search?q=FXEcho)                                                                        | Introduced in Windows 10.0.10240.0 |
| [**FXEQ**](https://www.bing.com/search?q=FXEQ)                                                                            | Introduced in Windows 10.0.10240.0 |
| [**FXMasteringLimiter**](https://www.bing.com/search?q=FXMasteringLimiter)                                                | Introduced in Windows 10.0.10240.0 |
| [**FXReverb**](https://www.bing.com/search?q=FXReverb)                                                                    | Introduced in Windows 10.0.10240.0 |
| [**RDPSession**](https://www.bing.com/search?q=RDPSession)                                                                | Introduced in Windows 10.0.10240.0 |
| [**RDPSRAPIApplication**](https://www.bing.com/search?q=RDPSRAPIApplication)                                              | Introduced in Windows 10.0.10240.0 |
| [**RDPSRAPIApplicationFilter**](https://www.bing.com/search?q=RDPSRAPIApplicationFilter)                                  | Introduced in Windows 10.0.10240.0 |
| [**RDPSRAPIApplicationList**](https://www.bing.com/search?q=RDPSRAPIApplicationList)                                      | Introduced in Windows 10.0.10240.0 |
| [**RDPSRAPIAttendee**](https://www.bing.com/search?q=RDPSRAPIAttendee)                                                    | Introduced in Windows 10.0.10240.0 |
| [**RDPSRAPIAttendeeDisconnectInfo**](https://www.bing.com/search?q=RDPSRAPIAttendeeDisconnectInfo)                        | Introduced in Windows 10.0.10240.0 |
| [**RDPSRAPIAttendeeManager**](https://www.bing.com/search?q=RDPSRAPIAttendeeManager)                                      | Introduced in Windows 10.0.10240.0 |
| [**RDPSRAPIInvitation**](https://www.bing.com/search?q=RDPSRAPIInvitation)                                                | Introduced in Windows 10.0.10240.0 |
| [**RDPSRAPIInvitationManager**](https://www.bing.com/search?q=RDPSRAPIInvitationManager)                                  | Introduced in Windows 10.0.10240.0 |
| [**RDPSRAPISessionProperties**](https://www.bing.com/search?q=RDPSRAPISessionProperties)                                  | Introduced in Windows 10.0.10240.0 |
| [**RDPSRAPITcpConnectionInfo**](https://www.bing.com/search?q=RDPSRAPITcpConnectionInfo)                                  | Introduced in Windows 10.0.10240.0 |
| [**RDPSRAPIWindow**](https://www.bing.com/search?q=RDPSRAPIWindow)                                                        | Introduced in Windows 10.0.10240.0 |
| [**RDPSRAPIWindowList**](https://www.bing.com/search?q=RDPSRAPIWindowList)                                                | Introduced in Windows 10.0.10240.0 |
| [**RDPViewer**](https://www.bing.com/search?q=RDPViewer)                                                                  | Introduced in Windows 10.0.10240.0 |
| [**SignalableNotifier**](https://www.bing.com/search?q=SignalableNotifier)                                                | Introduced in Windows 10.0.10240.0 |
| [**SpellCheckerFactory**](https://www.bing.com/search?q=SpellCheckerFactory)                                              | Introduced in Windows 10.0.10240.0 |
| [**WorkspaceBrokerAx**](https://www.bing.com/search?q=WorkspaceBrokerAx)                                                  | Introduced in Windows 10.0.10240.0 |
| [**AppxFactory**](https://www.bing.com/search?q=AppxFactory)                                                              | Introduced in Windows 10.0.14393.0 |
| [**CLSID\_AudioResamplerMediaObject**](https://www.bing.com/search?q=CLSID_AudioResamplerMediaObject)                     | Introduced in Windows 10.0.14393.0 |
| [**CLSID\_MSAACDecMFT**](https://www.bing.com/search?q=CLSID_MSAACDecMFT)                                                 | Introduced in Windows 10.0.14393.0 |
| [**CLSID\_MSDDPlusDecMFT**](https://www.bing.com/search?q=CLSID_MSDDPlusDecMFT)                                           | Introduced in Windows 10.0.14393.0 |
| [**CLSID\_MSH264DecoderMFT**](https://www.bing.com/search?q=CLSID_MSH264DecoderMFT)                                       | Introduced in Windows 10.0.14393.0 |
| [**CLSID\_MSH264EncoderMFT**](https://www.bing.com/search?q=CLSID_MSH264EncoderMFT)                                       | Introduced in Windows 10.0.14393.0 |
| [**CLSID\_MSH265DecoderMFT**](https://www.bing.com/search?q=CLSID_MSH265DecoderMFT)                                       | Introduced in Windows 10.0.14393.0 |
| [**CLSID\_MSMPEGAudDecMFT**](https://www.bing.com/search?q=CLSID_MSMPEGAudDecMFT)                                         | Introduced in Windows 10.0.14393.0 |
| [**CLSID\_MSMPEGDecoderMFT**](https://www.bing.com/search?q=CLSID_MSMPEGDecoderMFT)                                       | Introduced in Windows 10.0.14393.0 |
| [**CLSID\_MSVPxDecoder**](https://www.bing.com/search?q=CLSID_MSVPxDecoder)                                               | Introduced in Windows 10.0.14393.0 |
| [**CLSID\_MP3DecMediaObject**](https://www.bing.com/search?q=CLSID_MP3DecMediaObject)                                     | Introduced in Windows 10.0.14393.0 |
| [**CLSID\_PublicShellFeedbackBroker**](https://www.bing.com/search?q=CLSID_PublicShellFeedbackBroker)                     | Introduced in Windows 10.0.14393.0 |
| [**CLSID\_VideoProcessorMFT**](https://www.bing.com/search?q=CLSID_VideoProcessorMFT)                                     | Introduced in Windows 10.0.14393.0 |
| [**CLSID\_WMADecMediaObject**](https://www.bing.com/search?q=CLSID_WMADecMediaObject)                                     | Introduced in Windows 10.0.14393.0 |
| [**CLSID\_WMVDecoderMFT**](https://www.bing.com/search?q=CLSID_WMVDecoderMFT)                                             | Introduced in Windows 10.0.14393.0 |
| [**XblIdpAuthManager**](https://www.bing.com/search?q=XblIdpAuthManager)                                                  | Introduced in Windows 10.0.14393.0 |

 

 

 



