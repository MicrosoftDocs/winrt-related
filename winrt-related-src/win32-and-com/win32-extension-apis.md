---
author: msatranjr
description: This topic lists the Win32 and COM APIs that are part of the Universal Windows Platform (UWP) and that are implemented by some Windows 10 devices.
title: Extension APIs for Windows 10 devices (grouped by module)
ms.author: misatran
ms.topic: article
ms.prod: windows
ms.technology: uwp
keywords: windows 10, uwp, win32, COM
ms.date: 07/25/2017
ms.assetid: e8d54f37-9969-4f33-8b1b-fcb3d659c507
---

# Extension APIs for Windows 10 devices
This topic lists the Win32 and COM APIs that are part of the Universal Windows Platform (UWP) and that are implemented by some Windows 10 devices, so your calls to these APIs must be guarded with conditions that first confirm the presence of the API on the device your app is running on. The union of [APIs present on all Windows 10 devices](win32-apis.md) and the APIs listed in this topic make up the entire Win32 and COM surface area of UWP.

This topic lists the APIs grouped by module (where the module is either an [API set](https://msdn.microsoft.com/en-us/library/windows/apps/mt683763.aspx#api_sets) or a dll). For delay load, use the module name.

## APIs from PhoneAudioSes.dll

| API | Requirements |
| -----| --------------|
| ActivateAudioInterface | Introduced into PhoneAudioSes.dll in 10.0.10240. |


## APIs from MSAJApi.dll

| API | Requirements |
| -----| --------------|
| [alljoyn_aboutdata_createfromxml](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Removed in 10.0.14393. |
| [alljoyn_routerinit](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Removed in 10.0.14393. |
| [alljoyn_routershutdown](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Removed in 10.0.14393. |


## APIs from Bcrypt.dll

| API | Requirements |
| -----| --------------|
| BCryptCreateMultiHash | Introduced into Bcrypt.dll in 10.0.10240. Removed in 10.0.10586. |
| BCryptProcessMultiOperations | Introduced into Bcrypt.dll in 10.0.10240. Removed in 10.0.10586. |


## APIs from ole32.dll

| API | Requirements |
| -----| --------------|
| [BindMoniker](https://msdn.microsoft.com/en-us/library/windows/desktop/ms683759.aspx) | Introduced into ole32.dll in 10.0.10240. |
| [CoGetObject](https://msdn.microsoft.com/en-us/library/windows/desktop/ms678805.aspx) | Introduced into ole32.dll in 10.0.10240. |
| [CreateAntiMoniker](https://msdn.microsoft.com/en-us/library/windows/desktop/ms679750.aspx) | Introduced into ole32.dll in 10.0.10240. |
| [CreateBindCtx](https://msdn.microsoft.com/en-us/library/windows/desktop/ms678542.aspx) | Introduced into ole32.dll in 10.0.10240. |
| [CreateClassMoniker](https://msdn.microsoft.com/en-us/library/windows/desktop/ms688698.aspx) | Introduced into ole32.dll in 10.0.10240. |
| [CreateFileMoniker](https://msdn.microsoft.com/en-us/library/windows/desktop/ms693465.aspx) | Introduced into ole32.dll in 10.0.10240. |
| [CreateGenericComposite](https://msdn.microsoft.com/en-us/library/windows/desktop/ms687265.aspx) | Introduced into ole32.dll in 10.0.10240. |
| [CreateItemMoniker](https://msdn.microsoft.com/en-us/library/windows/desktop/ms680140.aspx) | Introduced into ole32.dll in 10.0.10240. |
| [CreateObjrefMoniker](https://msdn.microsoft.com/en-us/library/windows/desktop/ms678493.aspx) | Introduced into ole32.dll in 10.0.10240. |
| [CreatePointerMoniker](https://msdn.microsoft.com/en-us/library/windows/desktop/ms693427.aspx) | Introduced into ole32.dll in 10.0.10240. |
| [GetClassFile](https://msdn.microsoft.com/en-us/library/windows/desktop/ms693715.aspx) | Introduced into ole32.dll in 10.0.10240. |
| [IsEqualGUID](https://msdn.microsoft.com/en-us/library/windows/desktop/ms680575.aspx) | Introduced into ole32.dll in 10.0.10240. |
| [MkParseDisplayName](https://msdn.microsoft.com/en-us/library/windows/desktop/ms691253.aspx) | Introduced into ole32.dll in 10.0.10240. |
| [MonikerCommonPrefixWith](https://msdn.microsoft.com/en-us/library/windows/desktop/ms686583.aspx) | Introduced into ole32.dll in 10.0.10240. |
| [MonikerRelativePathTo](https://msdn.microsoft.com/en-us/library/windows/desktop/ms682532.aspx) | Introduced into ole32.dll in 10.0.10240. |


## APIs from dmprocessxmlfiltered.dll

| API | Requirements |
| -----| --------------|
| [DMProcessConfigXMLFiltered](https://msdn.microsoft.com/en-us/library/Mt591928.aspx) | Introduced into dmprocessxmlfiltered.dll in 10.0.10240. |


## APIs from iphlpapi.dll

| API | Requirements |
| -----| --------------|
| [GetAdaptersAddresses](https://msdn.microsoft.com/en-us/library/windows/desktop/aa365915.aspx) | Introduced into iphlpapi.dll in 10.0.10240. Removed in 10.0.14393. |
| [FreeMibTable](https://msdn.microsoft.com/en-us/library/windows/desktop/aa814408.aspx) | Introduced into iphlpapi.dll in 10.0.10586. Removed in 10.0.14393. |
| [GetBestRoute2](https://msdn.microsoft.com/en-us/library/windows/desktop/aa814411.aspx) | Introduced into iphlpapi.dll in 10.0.10586. Removed in 10.0.14393. |
| [GetUnicastIpAddressTable](https://msdn.microsoft.com/en-us/library/windows/desktop/aa814428.aspx) | Introduced into iphlpapi.dll in 10.0.10586. Removed in 10.0.14393. |


## APIs from PhoneAudioSes.lib

| API | Requirements |
| -----| --------------|
| GetDefaultAudioCaptureId | Introduced into PhoneAudioSes.lib in 10.0.10240. Moved into PhoneAudioSes.dll in 10.0.14393. |
| GetDefaultAudioRenderId | Introduced into PhoneAudioSes.lib in 10.0.10240. Moved into PhoneAudioSes.dll in 10.0.14393. |


## APIs from wpglobutil.dll

| API | Requirements |
| -----| --------------|
| GetTimeZoneList | Introduced into wpglobutil.dll in 10.0.10240. |


## APIs from kernel32.dll

| API | Requirements |
| -----| --------------|
| [InterlockedCompareExchange](https://msdn.microsoft.com/en-us/library/windows/desktop/ff471409.aspx) | Introduced into kernel32.dll in 10.0.10240. |
| [InterlockedCompareExchange64](https://msdn.microsoft.com/en-us/library/windows/desktop/ms683562.aspx) | Introduced into kernel32.dll in 10.0.10240. |
| [InterlockedDecrement](https://msdn.microsoft.com/en-us/library/windows/desktop/ms683580.aspx) | Introduced into kernel32.dll in 10.0.10240. |
| [InterlockedExchange](https://msdn.microsoft.com/en-us/library/windows/desktop/ff471411.aspx) | Introduced into kernel32.dll in 10.0.10240. |
| [InterlockedExchangeAdd](https://msdn.microsoft.com/en-us/library/windows/desktop/ms683597.aspx) | Introduced into kernel32.dll in 10.0.10240. |
| [InterlockedIncrement](https://msdn.microsoft.com/en-us/library/windows/desktop/ms683614.aspx) | Introduced into kernel32.dll in 10.0.10240. |


## APIs from kernelbase.dll

| API | Requirements |
| -----| --------------|
| [GetProcessMemoryInfo](https://msdn.microsoft.com/en-us/library/windows/desktop/ms683219.aspx) | Introduced into kernelbase.dll in 10.0.10240. Removed in 10.0.14393. |


## APIs from elscore.dll

| API | Requirements |
| -----| --------------|
| [MappingFreePropertyBag](https://msdn.microsoft.com/en-us/library/windows/desktop/dd319058.aspx) | Introduced into elscore.dll in 10.0.10240. |
| [MappingFreeServices](https://msdn.microsoft.com/en-us/library/windows/desktop/dd319059.aspx) | Introduced into elscore.dll in 10.0.10240. |
| [MappingGetServices](https://msdn.microsoft.com/en-us/library/windows/desktop/dd319060.aspx) | Introduced into elscore.dll in 10.0.10240. |
| [MappingRecognizeText](https://msdn.microsoft.com/en-us/library/windows/desktop/dd319063.aspx) | Introduced into elscore.dll in 10.0.10240. |


## APIs from rpcrt4.dll

| API | Requirements |
| -----| --------------|
| [NdrAsyncClientCall2](https://msdn.microsoft.com/en-us/library/windows/desktop/mt297483.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrClientCall4](https://msdn.microsoft.com/en-us/library/windows/desktop/mt297484.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |


## APIs from windows.data.pdf.dll

| API | Requirements |
| -----| --------------|
| [PdfRenderParams](https://msdn.microsoft.com/en-us/library/windows/desktop/mt604123.aspx) | Introduced into windows.data.pdf.dll in 10.0.10240. Removed in 10.0.14393. |


## APIs from api-ms-win-core-slapi-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [SLQueryLicenseValueFromApp](https://msdn.microsoft.com/en-us/library/windows/desktop/mt403327.aspx) | Introduced into api-ms-win-core-slapi-l1-1-0.dll in 10.0.10240. Removed in 10.0.14393. |
| SLQueryLicenseValueFromApp2 | Introduced into api-ms-win-core-slapi-l1-1-0.dll in 10.0.10240. Removed in 10.0.14393. |


## APIs from srpapi.dll

| API | Requirements |
| -----| --------------|
| SrpDoesPolicyAllowAppExecution | Introduced into srpapi.dll in 10.0.10240. |


## APIs from api-ms-win-crt-convert-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [__toascii](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/toascii-toascii) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_atodbl](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/atodbl-atodbl-l-atoldbl-atoldbl-l-atoflt-atoflt-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_atodbl_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/atodbl-atodbl-l-atoldbl-atoldbl-l-atoflt-atoflt-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_atof_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/atof-atof-l-wtof-wtof-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_atoflt](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/atodbl-atodbl-l-atoldbl-atoldbl-l-atoflt-atoflt-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_atoflt_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/atodbl-atodbl-l-atoldbl-atoldbl-l-atoflt-atoflt-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_atoi_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/atoi-atoi-l-wtoi-wtoi-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_atoi64](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/atoi64-atoi64-l-wtoi64-wtoi64-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_atoi64_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/atoi64-atoi64-l-wtoi64-wtoi64-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_atol_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/atol-atol-l-wtol-wtol-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_atoldbl](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/atodbl-atodbl-l-atoldbl-atoldbl-l-atoflt-atoflt-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_atoldbl_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/atodbl-atodbl-l-atoldbl-atoldbl-l-atoflt-atoflt-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_atoll_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/atoll-atoll-l-wtoll-wtoll-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_ecvt](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ecvt) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_ecvt_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ecvt-s) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_fcvt](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fcvt) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_fcvt_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fcvt-s) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_gcvt](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/gcvt) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_gcvt_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/gcvt-s) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_i64toa](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/itoa-i64toa-ui64toa-itow-i64tow-ui64tow) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_i64toa_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/itoa-s-i64toa-s-ui64toa-s-itow-s-i64tow-s-ui64tow-s) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_i64tow](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/itoa-i64toa-ui64toa-itow-i64tow-ui64tow) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_i64tow_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/itoa-s-i64toa-s-ui64toa-s-itow-s-i64tow-s-ui64tow-s) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_itoa](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/itoa-i64toa-ui64toa-itow-i64tow-ui64tow) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_itoa_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/itoa-s-i64toa-s-ui64toa-s-itow-s-i64tow-s-ui64tow-s) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_itow](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/itoa-i64toa-ui64toa-itow-i64tow-ui64tow) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_itow_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/itoa-s-i64toa-s-ui64toa-s-itow-s-i64tow-s-ui64tow-s) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_ltoa](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ltoa-ltow) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_ltoa_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ltoa-s-ltow-s) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_ltow](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ltoa-ltow) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_ltow_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ltoa-s-ltow-s) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_strtod_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strtod-strtod-l-wcstod-wcstod-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_strtof_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strtof-strtof-l-wcstof-wcstof-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_strtoi64](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strtoi64-wcstoi64-strtoi64-l-wcstoi64-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_strtoi64_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strtoi64-wcstoi64-strtoi64-l-wcstoi64-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_strtoimax_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strtoimax-strtoimax-l-wcstoimax-wcstoimax-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_strtol_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strtol-wcstol-strtol-l-wcstol-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_strtold_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strtold-strtold-l-wcstold-wcstold-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_strtoll_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strtoll-strtoll-l-wcstoll-wcstoll-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_strtoui64](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strtoui64-wcstoui64-strtoui64-l-wcstoui64-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_strtoui64_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strtoui64-wcstoui64-strtoui64-l-wcstoui64-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_strtoul_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strtoul-strtoul-l-wcstoul-wcstoul-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_strtoull_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strtoull-strtoull-l-wcstoull-wcstoull-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_strtoumax_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strtoumax-strtoumax-l-wcstoumax-wcstoumax-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_ui64toa](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/itoa-i64toa-ui64toa-itow-i64tow-ui64tow) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_ui64toa_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/itoa-s-i64toa-s-ui64toa-s-itow-s-i64tow-s-ui64tow-s) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_ui64tow](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/itoa-i64toa-ui64toa-itow-i64tow-ui64tow) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_ui64tow_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/itoa-s-i64toa-s-ui64toa-s-itow-s-i64tow-s-ui64tow-s) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_ultoa](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ultoa-ultow) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_ultoa_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ultoa-s-ultow-s) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_ultow](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ultoa-ultow) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_ultow_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ultoa-s-ultow-s) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_wcstod_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strtod-strtod-l-wcstod-wcstod-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_wcstof_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strtof-strtof-l-wcstof-wcstof-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_wcstoi64](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strtoi64-wcstoi64-strtoi64-l-wcstoi64-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_wcstoi64_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strtoi64-wcstoi64-strtoi64-l-wcstoi64-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_wcstoimax_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strtoimax-strtoimax-l-wcstoimax-wcstoimax-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_wcstol_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strtol-wcstol-strtol-l-wcstol-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_wcstold_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strtold-strtold-l-wcstold-wcstold-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_wcstoll_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strtoll-strtoll-l-wcstoll-wcstoll-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_wcstombs_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/wcstombs-wcstombs-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_wcstombs_s_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/wcstombs-s-wcstombs-s-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_wcstoui64](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strtoui64-wcstoui64-strtoui64-l-wcstoui64-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_wcstoui64_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strtoui64-wcstoui64-strtoui64-l-wcstoui64-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_wcstoul_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strtoul-strtoul-l-wcstoul-wcstoul-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_wcstoull_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strtoull-strtoull-l-wcstoull-wcstoull-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_wcstoumax_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strtoumax-strtoumax-l-wcstoumax-wcstoumax-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_wctomb_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/wctomb-wctomb-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_wctomb_s_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/wctomb-s-wctomb-s-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_wtof](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/atof-atof-l-wtof-wtof-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_wtof_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/atof-atof-l-wtof-wtof-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_wtoi](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/atoi-atoi-l-wtoi-wtoi-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_wtoi_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/atoi-atoi-l-wtoi-wtoi-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_wtoi64](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/atoi64-atoi64-l-wtoi64-wtoi64-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_wtoi64_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/atoi64-atoi64-l-wtoi64-wtoi64-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_wtol](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/atol-atol-l-wtol-wtol-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_wtol_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/atol-atol-l-wtol-wtol-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_wtoll](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/atoll-atoll-l-wtoll-wtoll-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [_wtoll_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/atoll-atoll-l-wtoll-wtoll-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [atof](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/atof-atof-l-wtof-wtof-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [atoi](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/atoi-atoi-l-wtoi-wtoi-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [atol](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/atol-atol-l-wtol-wtol-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [atoll](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/atoll-atoll-l-wtoll-wtoll-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [btowc](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/btowc) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [c16rtomb](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/c16rtomb-c32rtomb1) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [c32rtomb](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/c16rtomb-c32rtomb1) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [mbrtoc16](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/mbrtoc16-mbrtoc323) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [mbrtoc32](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/mbrtoc16-mbrtoc323) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [mbrtowc](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/mbrtowc) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [mbsrtowcs](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/mbsrtowcs) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [mbsrtowcs_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/mbsrtowcs-s) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [mbstowcs](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/mbstowcs-mbstowcs-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [mbstowcs_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/mbstowcs-s-mbstowcs-s-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [mbtowc](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/mbtowc-mbtowc-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [strtod](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strtod-strtod-l-wcstod-wcstod-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [strtof](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strtof-strtof-l-wcstof-wcstof-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [strtoimax](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strtoimax-strtoimax-l-wcstoimax-wcstoimax-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [strtol](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strtol-wcstol-strtol-l-wcstol-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [strtold](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strtold-strtold-l-wcstold-wcstold-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [strtoll](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strtoll-strtoll-l-wcstoll-wcstoll-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [strtoul](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strtoul-strtoul-l-wcstoul-wcstoul-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [strtoull](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strtoull-strtoull-l-wcstoull-wcstoull-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [strtoumax](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strtoumax-strtoumax-l-wcstoumax-wcstoumax-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [wcrtomb](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/wcrtomb) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [wcrtomb_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/wcrtomb-s) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [wcsrtombs](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/wcsrtombs) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [wcsrtombs_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/wcsrtombs-s) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [wcstod](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strtod-strtod-l-wcstod-wcstod-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [wcstof](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strtof-strtof-l-wcstof-wcstof-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [wcstoimax](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strtoimax-strtoimax-l-wcstoimax-wcstoimax-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [wcstol](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strtol-wcstol-strtol-l-wcstol-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [wcstold](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strtold-strtold-l-wcstold-wcstold-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [wcstoll](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strtoll-strtoll-l-wcstoll-wcstoll-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [wcstombs](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/wcstombs-wcstombs-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [wcstombs_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/wcstombs-s-wcstombs-s-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [wcstoul](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strtoul-strtoul-l-wcstoul-wcstoul-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [wcstoull](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strtoull-strtoull-l-wcstoull-wcstoull-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [wcstoumax](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strtoumax-strtoumax-l-wcstoumax-wcstoumax-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [wctob](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/wctob) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [wctomb](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/wctomb-wctomb-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [wctomb_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/wctomb-s-wctomb-s-l) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| [wctrans](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/towctrans) | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |


## APIs from api-ms-win-crt-environment-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [__p__environ](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-environment-l1-1-0.dll in 10.0.10240. |
| [__p__wenviron](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-environment-l1-1-0.dll in 10.0.10240. |


## APIs from api-ms-win-crt-filesystem-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [_access](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/access-waccess) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [_access_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/access-s-waccess-s) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [_chdir](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/chdir-wchdir) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [_chmod](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/chmod-wchmod) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [_findclose](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/findclose) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [_findfirst32](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/findfirst-functions) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [_findfirst32i64](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/findfirst-functions) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [_findfirst64](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/findfirst-functions) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [_findfirst64i32](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/findfirst-functions) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [_findnext32](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/findnext-functions) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [_findnext32i64](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/findnext-functions) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [_findnext64](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/findnext-functions) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [_findnext64i32](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/findnext-functions) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [_fstat32](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fstat-fstat32-fstat64-fstati64-fstat32i64-fstat64i32) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [_fstat32i64](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fstat-fstat32-fstat64-fstati64-fstat32i64-fstat64i32) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [_fstat64](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fstat-fstat32-fstat64-fstati64-fstat32i64-fstat64i32) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [_fstat64i32](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fstat-fstat32-fstat64-fstati64-fstat32i64-fstat64i32) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [_fullpath](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fullpath-wfullpath) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [_getcwd](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/getcwd-wgetcwd) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [_getdcwd](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/getdcwd-wgetdcwd) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [_lock_file](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/lock-file) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [_makepath](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/makepath-wmakepath) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [_makepath_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/makepath-s-wmakepath-s) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [_mkdir](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/mkdir-wmkdir) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [_rmdir](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/rmdir-wrmdir) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [_splitpath](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/splitpath-wsplitpath) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [_splitpath_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/splitpath-s-wsplitpath-s) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [_stat32](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/stat-functions) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [_stat32i64](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/stat-functions) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [_stat64](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/stat-functions) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [_stat64i32](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/stat-functions) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [_umask](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/umask) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [_umask_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/umask-s) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [_unlink](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/unlink-wunlink) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [_unlock_file](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/unlock-file) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [_waccess](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/access-waccess) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [_waccess_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/access-s-waccess-s) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [_wchdir](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/chdir-wchdir) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [_wchmod](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/chmod-wchmod) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [_wfindfirst32](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/findfirst-functions) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [_wfindfirst32i64](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/findfirst-functions) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [_wfindfirst64](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/findfirst-functions) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [_wfindfirst64i32](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/findfirst-functions) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [_wfindnext32](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/findnext-functions) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [_wfindnext32i64](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/findnext-functions) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [_wfindnext64](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/findnext-functions) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [_wfindnext64i32](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/findnext-functions) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [_wfullpath](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fullpath-wfullpath) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [_wgetcwd](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/getcwd-wgetcwd) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [_wgetdcwd](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/getdcwd-wgetdcwd) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [_wmakepath](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/makepath-wmakepath) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [_wmakepath_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/makepath-s-wmakepath-s) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [_wmkdir](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/mkdir-wmkdir) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [_wremove](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/remove-wremove) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [_wrename](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/rename-wrename) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [_wrmdir](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/rmdir-wrmdir) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [_wsplitpath](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/splitpath-wsplitpath) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [_wsplitpath_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/splitpath-s-wsplitpath-s) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [_wstat32](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/stat-functions) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [_wstat32i64](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/stat-functions) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [_wstat64](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/stat-functions) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [_wstat64i32](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/stat-functions) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [_wunlink](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/unlink-wunlink) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [remove](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/remove-wremove) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [rename](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/rename-wrename) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |


## APIs from api-ms-win-crt-heap-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [_aligned_free](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/aligned-free) | Introduced into api-ms-win-crt-heap-l1-1-0.dll in 10.0.10240. |
| [_aligned_malloc](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/aligned-malloc) | Introduced into api-ms-win-crt-heap-l1-1-0.dll in 10.0.10240. |
| [_aligned_msize](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/aligned-msize) | Introduced into api-ms-win-crt-heap-l1-1-0.dll in 10.0.10240. |
| [_aligned_offset_malloc](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/aligned-offset-malloc) | Introduced into api-ms-win-crt-heap-l1-1-0.dll in 10.0.10240. |
| [_aligned_offset_realloc](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/aligned-offset-realloc) | Introduced into api-ms-win-crt-heap-l1-1-0.dll in 10.0.10240. |
| [_aligned_offset_recalloc](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/aligned-offset-recalloc) | Introduced into api-ms-win-crt-heap-l1-1-0.dll in 10.0.10240. |
| [_aligned_realloc](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/aligned-realloc) | Introduced into api-ms-win-crt-heap-l1-1-0.dll in 10.0.10240. |
| [_aligned_recalloc](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/aligned-recalloc) | Introduced into api-ms-win-crt-heap-l1-1-0.dll in 10.0.10240. |
| [_callnewh](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/callnewh) | Introduced into api-ms-win-crt-heap-l1-1-0.dll in 10.0.10240. |
| [_calloc_base](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-heap-l1-1-0.dll in 10.0.10240. |
| [_expand](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/expand) | Introduced into api-ms-win-crt-heap-l1-1-0.dll in 10.0.10240. |
| [_free_base](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-heap-l1-1-0.dll in 10.0.10240. |
| [_get_heap_handle](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/get-heap-handle) | Introduced into api-ms-win-crt-heap-l1-1-0.dll in 10.0.10240. |
| [_heapmin](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/heapmin) | Introduced into api-ms-win-crt-heap-l1-1-0.dll in 10.0.10240. |
| [_malloc_base](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-heap-l1-1-0.dll in 10.0.10240. |
| [_msize](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/aligned-msize) | Introduced into api-ms-win-crt-heap-l1-1-0.dll in 10.0.10240. |
| [_query_new_handler](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/query-new-handler) | Introduced into api-ms-win-crt-heap-l1-1-0.dll in 10.0.10240. |
| [_query_new_mode](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/query-new-mode) | Introduced into api-ms-win-crt-heap-l1-1-0.dll in 10.0.10240. |
| [_realloc_base](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-heap-l1-1-0.dll in 10.0.10240. |
| [_recalloc](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/aligned-offset-recalloc) | Introduced into api-ms-win-crt-heap-l1-1-0.dll in 10.0.10240. |
| [_set_new_mode](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/set-new-mode) | Introduced into api-ms-win-crt-heap-l1-1-0.dll in 10.0.10240. |
| [calloc](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/aligned-offset-recalloc) | Introduced into api-ms-win-crt-heap-l1-1-0.dll in 10.0.10240. |
| [free](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/aligned-free) | Introduced into api-ms-win-crt-heap-l1-1-0.dll in 10.0.10240. |
| [malloc](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/aligned-malloc) | Introduced into api-ms-win-crt-heap-l1-1-0.dll in 10.0.10240. |
| [realloc](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/aligned-offset-realloc) | Introduced into api-ms-win-crt-heap-l1-1-0.dll in 10.0.10240. |
| [_resetstkoflw](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/resetstkoflw) | Introduced into api-ms-win-crt-heap-l1-1-0.dll in 10.0.15063. |


## APIs from api-ms-win-crt-locale-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [___lc_codepage_func](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-locale-l1-1-0.dll in 10.0.10240. |
| [___lc_collate_cp_func](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-locale-l1-1-0.dll in 10.0.10240. |
| [___lc_locale_name_func](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-locale-l1-1-0.dll in 10.0.10240. |
| [___mb_cur_max_func](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-locale-l1-1-0.dll in 10.0.10240. |
| [___mb_cur_max_l_func](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-locale-l1-1-0.dll in 10.0.10240. |
| __initialize_lconv_for_unsigned_char | Introduced into api-ms-win-crt-locale-l1-1-0.dll in 10.0.10240. |
| [__pctype_func](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-locale-l1-1-0.dll in 10.0.10240. |
| [__pwctype_func](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-locale-l1-1-0.dll in 10.0.10240. |
| [_configthreadlocale](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/configthreadlocale) | Introduced into api-ms-win-crt-locale-l1-1-0.dll in 10.0.10240. |
| [_create_locale](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/create-locale-wcreate-locale) | Introduced into api-ms-win-crt-locale-l1-1-0.dll in 10.0.10240. |
| [_free_locale](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/free-locale) | Introduced into api-ms-win-crt-locale-l1-1-0.dll in 10.0.10240. |
| [_get_current_locale](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/get-current-locale) | Introduced into api-ms-win-crt-locale-l1-1-0.dll in 10.0.10240. |
| [_getmbcp](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/getmbcp) | Introduced into api-ms-win-crt-locale-l1-1-0.dll in 10.0.10240. |
| [_lock_locales](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-locale-l1-1-0.dll in 10.0.10240. |
| [_setmbcp](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/setmbcp) | Introduced into api-ms-win-crt-locale-l1-1-0.dll in 10.0.10240. |
| [_unlock_locales](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-locale-l1-1-0.dll in 10.0.10240. |
| [_wcreate_locale](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/create-locale-wcreate-locale) | Introduced into api-ms-win-crt-locale-l1-1-0.dll in 10.0.10240. |
| [_wsetlocale](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/setlocale-wsetlocale) | Introduced into api-ms-win-crt-locale-l1-1-0.dll in 10.0.10240. |
| [localeconv](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/localeconv) | Introduced into api-ms-win-crt-locale-l1-1-0.dll in 10.0.10240. |
| [setlocale](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/setlocale-wsetlocale) | Introduced into api-ms-win-crt-locale-l1-1-0.dll in 10.0.10240. |


## APIs from api-ms-win-crt-math-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [__libm_sse2_acos](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [__libm_sse2_acosf](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [__libm_sse2_asin](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [__libm_sse2_asinf](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [__libm_sse2_atan](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [__libm_sse2_atan2](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [__libm_sse2_atanf](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [__libm_sse2_cos](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [__libm_sse2_cosf](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [__libm_sse2_exp](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [__libm_sse2_expf](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [__libm_sse2_log](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [__libm_sse2_log10](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [__libm_sse2_log10f](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [__libm_sse2_logf](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [__libm_sse2_pow](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [__libm_sse2_powf](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [__libm_sse2_sin](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [__libm_sse2_sinf](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [__libm_sse2_tan](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [__libm_sse2_tanf](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [__setusermatherr](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_cabs](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/cabs) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _Cbuild | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_chgsign](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/chgsign-chgsignf-chgsignl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_chgsignf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/chgsign-chgsignf-chgsignl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_CIacos](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_CIasin](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_CIatan](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_CIatan2](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_CIcos](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_CIcosh](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_CIexp](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_CIfmod](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_CIlog](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_CIlog10](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_CIpow](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_CIsin](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_CIsinh](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_CIsqrt](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_CItan](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_CItanh](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _Cmulcc | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _Cmulcr | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_copysign](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/copysign-copysignf-copysignl-copysign-copysignf-copysignl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_copysignf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/copysign-copysignf-copysignl-copysign-copysignf-copysignl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _d_int | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_dclass](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _dexp | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _dlog | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _dnorm | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_dpcomp](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _dpoly | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _dscale | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_dsign](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _dsin | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_dtest](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _dunscale | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_except1](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _FCbuild | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _FCmulcc | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _FCmulcr | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _fd_int | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_fdclass](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _fdexp | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _fdlog | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _fdnorm | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_fdopen](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fdopen-wfdopen) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_fdpcomp](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _fdpoly | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _fdscale | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_fdsign](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _fdsin | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_fdtest](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _fdunscale | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_finite](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/finite-finitef) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_finitef](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/finite-finitef) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_fpclass](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fpclass-fpclassf) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_fpclassf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fpclass-fpclassf) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_FPE_Raise](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_ftol](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _get_FMA3_enable | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_hypot](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/hypot-hypotf-hypotl-hypot-hypotf-hypotl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_hypotf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/hypot-hypotf-hypotl-hypot-hypotf-hypotl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_isnan](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/isnan-isnan-isnanf) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_isnanf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/isnan-isnan-isnanf) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_j0](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/bessel-functions-j0-j1-jn-y0-y1-yn) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_j1](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/bessel-functions-j0-j1-jn-y0-y1-yn) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_jn](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/bessel-functions-j0-j1-jn-y0-y1-yn) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _LCbuild | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _LCmulcc | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _LCmulcr | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _ld_int | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_ldclass](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _ldexp | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _ldlog | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_ldpcomp](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _ldpoly | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _ldscale | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_ldsign](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _ldsin | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_ldtest](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _ldunscale | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_libm_sse2_acos_precise](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_libm_sse2_asin_precise](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_libm_sse2_atan_precise](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_libm_sse2_cos_precise](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_libm_sse2_exp_precise](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_libm_sse2_log_precise](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_libm_sse2_log10_precise](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_libm_sse2_pow_precise](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_libm_sse2_sin_precise](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_libm_sse2_sqrt_precise](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_libm_sse2_tan_precise](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_logb](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/logb-logbf-logbl-logb-logbf) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_logbf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/logb-logbf-logbl-logb-logbf) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_nextafter](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/nextafter-functions) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_nextafterf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/nextafter-functions) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_scalb](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/scalb) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _scalbf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _set_FMA3_enable | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_set_SSE2_enable](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/set-sse2-enable) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_y0](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/bessel-functions-j0-j1-jn-y0-y1-yn) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_y1](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/bessel-functions-j0-j1-jn-y0-y1-yn) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [_yn](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/bessel-functions-j0-j1-jn-y0-y1-yn) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [acos](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/acos-acosf-acosl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [acosf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/acos-acosf-acosl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [acosh](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/acosh-acoshf-acoshl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [acoshf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/acosh-acoshf-acoshl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [acoshl](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/acosh-acoshf-acoshl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [asin](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/asin-asinf-asinl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [asinf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/asin-asinf-asinl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [asinh](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/asinh-asinhf-asinhl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [asinhf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/asinh-asinhf-asinhl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [asinhl](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/asinh-asinhf-asinhl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [atan](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/atan-atanf-atanl-atan2-atan2f-atan2l) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [atan2](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/atan-atanf-atanl-atan2-atan2f-atan2l) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [atan2f](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/atan-atanf-atanl-atan2-atan2f-atan2l) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [atanf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/atan-atanf-atanl-atan2-atan2f-atan2l) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [atanh](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/atanh-atanhf-atanhl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [atanhf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/atanh-atanhf-atanhl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [atanhl](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/atanh-atanhf-atanhl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [cabs](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/cabs) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [cabsf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/cabs-cabsf-cabsl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [cabsl](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/cabs-cabsf-cabsl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [cacos](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/cacos-cacosf-cacosl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [cacosf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/cacos-cacosf-cacosl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [cacosh](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/cacosh-cacoshf-cacoshl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [cacoshf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/cacosh-cacoshf-cacoshl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [cacoshl](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/cacosh-cacoshf-cacoshl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [cacosl](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/cacos-cacosf-cacosl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [carg](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/carg-cargf-cargl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [cargf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/carg-cargf-cargl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [cargl](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/carg-cargf-cargl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [casin](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/casin-casinf-casinl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [casinf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/casin-casinf-casinl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [casinh](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/casinh-casinhf-casinhl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [casinhf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/casinh-casinhf-casinhl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [casinhl](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/casinh-casinhf-casinhl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [casinl](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/casin-casinf-casinl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [catan](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/catan-catanf-catanl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [catanf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/catan-catanf-catanl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [catanh](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/catanh-catanhf-catanhl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [catanhf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/catanh-catanhf-catanhl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [catanhl](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/catanh-catanhf-catanhl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [catanl](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/catan-catanf-catanl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [cbrt](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/cbrt-cbrtf-cbrtl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [cbrtf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/cbrt-cbrtf-cbrtl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [cbrtl](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/cbrt-cbrtf-cbrtl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [ccos](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ccos-ccosf-ccosl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [ccosf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ccos-ccosf-ccosl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [ccosh](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ccosh-ccoshf-ccoshl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [ccoshf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ccosh-ccoshf-ccoshl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [ccoshl](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ccosh-ccoshf-ccoshl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [ccosl](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ccos-ccosf-ccosl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [ceil](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ceil-ceilf-ceill) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [ceilf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ceil-ceilf-ceill) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [cexp](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/cexp-cexpf-cexpl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [cexpf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/cexp-cexpf-cexpl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [cexpl](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/cexp-cexpf-cexpl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [cimag](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/cimag-cimagf-cimagl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [cimagf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/cimag-cimagf-cimagl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [cimagl](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/cimag-cimagf-cimagl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [clog](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/clog-clogf-clogl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [clog10](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/clog10-clog10f-clog10l) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [clog10f](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/clog10-clog10f-clog10l) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [clog10l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/clog10-clog10f-clog10l) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [clogf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/clog-clogf-clogl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [clogl](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/clog-clogf-clogl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [conj](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/conj-conjf-conjl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [conjf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/conj-conjf-conjl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [conjl](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/conj-conjf-conjl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [copysign](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/copysign-copysignf-copysignl-copysign-copysignf-copysignl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [copysignf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/copysign-copysignf-copysignl-copysign-copysignf-copysignl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [copysignl](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/copysign-copysignf-copysignl-copysign-copysignf-copysignl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [cos](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/acos-acosf-acosl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [cosf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/acos-acosf-acosl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [cosh](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/acosh-acoshf-acoshl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [coshf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/acosh-acoshf-acoshl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [cpow](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/cpow-cpowf-cpowl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [cpowf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/cpow-cpowf-cpowl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [cpowl](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/cpow-cpowf-cpowl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [cproj](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/cproj-cprojf-cprojl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [cprojf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/cproj-cprojf-cprojl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [cprojl](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/cproj-cprojf-cprojl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [creal](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/creal-crealf-creall) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [crealf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/creal-crealf-creall) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [creall](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/creal-crealf-creall) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [csin](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/csin-csinf-csinl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [csinf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/csin-csinf-csinl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [csinh](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/csinh-csinhf-csinhl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [csinhf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/csinh-csinhf-csinhl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [csinhl](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/csinh-csinhf-csinhl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [csinl](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/csin-csinf-csinl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [csqrt](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/csqrt-csqrtf-csqrtl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [csqrtf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/csqrt-csqrtf-csqrtl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [csqrtl](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/csqrt-csqrtf-csqrtl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [ctan](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ctan-ctanf-ctanl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [ctanf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ctan-ctanf-ctanl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [ctanh](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ctanh-ctanhf-ctanhl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [ctanhf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ctanh-ctanhf-ctanhl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [ctanhl](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ctanh-ctanhf-ctanhl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [ctanl](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ctan-ctanf-ctanl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [erf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/erf-erff-erfl-erfc-erfcf-erfcl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [erfc](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/erf-erff-erfl-erfc-erfcf-erfcl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [erfcf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/erf-erff-erfl-erfc-erfcf-erfcl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [erfcl](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/erf-erff-erfl-erfc-erfcf-erfcl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [erff](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/erf-erff-erfl-erfc-erfcf-erfcl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [erfl](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/erf-erff-erfl-erfc-erfcf-erfcl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [exp](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/cexp-cexpf-cexpl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [exp2](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/exp2-exp2f-exp2l) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [exp2f](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/exp2-exp2f-exp2l) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [exp2l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/exp2-exp2f-exp2l) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [expf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/cexp-cexpf-cexpl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [expm1](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/expm1-expm1f-expm1l) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [expm1f](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/expm1-expm1f-expm1l) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [expm1l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/expm1-expm1f-expm1l) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [fabs](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fabs-fabsf-fabsl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [fabsf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fabs-fabsf-fabsl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [fdim](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fdim-fdimf-fdiml) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [fdimf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fdim-fdimf-fdiml) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [fdiml](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fdim-fdimf-fdiml) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [floor](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/floor-floorf-floorl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [floorf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/floor-floorf-floorl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [fma](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fma-fmaf-fmal) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [fmaf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fma-fmaf-fmal) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [fmal](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fma-fmaf-fmal) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [fmax](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fmax-fmaxf-fmaxl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [fmaxf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fmax-fmaxf-fmaxl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [fmaxl](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fmax-fmaxf-fmaxl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [fmin](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fmin-fminf-fminl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [fminf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fmin-fminf-fminl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [fminl](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fmin-fminf-fminl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [fmod](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fmod-fmodf) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [fmodf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fmod-fmodf) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [frexp](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/frexp) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [hypot](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/hypot-hypotf-hypotl-hypot-hypotf-hypotl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [ilogb](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ilogb-ilogbf-ilogbl2) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [ilogbf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ilogb-ilogbf-ilogbl2) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [ilogbl](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ilogb-ilogbf-ilogbl2) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [ldexp](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ldexp) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [lgamma](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/lgamma-lgammaf-lgammal) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [lgammaf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/lgamma-lgammaf-lgammal) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [lgammal](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/lgamma-lgammaf-lgammal) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [llrint](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/lrint-lrintf-lrintl-llrint-llrintf-llrintl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [llrintf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/lrint-lrintf-lrintl-llrint-llrintf-llrintl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [llrintl](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/lrint-lrintf-lrintl-llrint-llrintf-llrintl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [llround](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/lround-lroundf-lroundl-llround-llroundf-llroundl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [llroundf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/lround-lroundf-lroundl-llround-llroundf-llroundl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [llroundl](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/lround-lroundf-lroundl-llround-llroundf-llroundl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [log](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/clog-clogf-clogl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [log10](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/clog10-clog10f-clog10l) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [log10f](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/clog10-clog10f-clog10l) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [log1p](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/log1p-log1pf-log1pl2) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [log1pf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/log1p-log1pf-log1pl2) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [log1pl](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/log1p-log1pf-log1pl2) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [log2](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/log2-log2f-log2l) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [log2f](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/log2-log2f-log2l) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [log2l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/log2-log2f-log2l) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [logb](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ilogb-ilogbf-ilogbl2) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [logbf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ilogb-ilogbf-ilogbl2) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [logbl](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ilogb-ilogbf-ilogbl2) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [logf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/clog-clogf-clogl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [lrint](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/lrint-lrintf-lrintl-llrint-llrintf-llrintl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [lrintf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/lrint-lrintf-lrintl-llrint-llrintf-llrintl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [lrintl](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/lrint-lrintf-lrintl-llrint-llrintf-llrintl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [lround](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/lround-lroundf-lroundl-llround-llroundf-llroundl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [lroundf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/lround-lroundf-lroundl-llround-llroundf-llroundl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [lroundl](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/lround-lroundf-lroundl-llround-llroundf-llroundl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [modf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fmod-fmodf) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [modff](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/modf-modff-modfl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [nan](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/isnan-isnan-isnanf) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [nanf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/isnan-isnan-isnanf) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [nanl](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/nan-nanf-nanl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [nearbyint](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/nearbyint-nearbyintf-nearbyintl1) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [nearbyintf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/nearbyint-nearbyintf-nearbyintl1) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [nearbyintl](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/nearbyint-nearbyintf-nearbyintl1) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [nextafter](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/nextafter-functions) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [nextafterf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/nextafter-functions) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [nextafterl](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/nextafter-functions) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [nexttoward](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/nextafter-functions) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [nexttowardf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/nextafter-functions) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [nexttowardl](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/nextafter-functions) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [norm](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/norm-normf-norml1) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [normf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/norm-normf-norml1) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [norml](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/norm-normf-norml1) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [pow](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/cpow-cpowf-cpowl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [powf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/cpow-cpowf-cpowl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [remainder](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/remainder-remainderf-remainderl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [remainderf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/remainder-remainderf-remainderl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [remainderl](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/remainder-remainderf-remainderl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [remquo](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/remquo-remquof-remquol) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [remquof](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/remquo-remquof-remquol) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [remquol](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/remquo-remquof-remquol) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [rint](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/cprintf) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [rintf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/cprintf) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [rintl](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/lrint-lrintf-lrintl-llrint-llrintf-llrintl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [round](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fegetround-fesetround2) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [roundf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/lround-lroundf-lroundl-llround-llroundf-llroundl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [roundl](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/lround-lroundf-lroundl-llround-llroundf-llroundl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [scalbln](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/scalbn-scalbnf-scalbnl-scalbln-scalblnf-scalblnl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [scalblnf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/scalbn-scalbnf-scalbnl-scalbln-scalblnf-scalblnl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [scalblnl](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/scalbn-scalbnf-scalbnl-scalbln-scalblnf-scalblnl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [scalbn](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/scalbn-scalbnf-scalbnl-scalbln-scalblnf-scalblnl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [scalbnf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/scalbn-scalbnf-scalbnl-scalbln-scalblnf-scalblnl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [scalbnl](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/scalbn-scalbnf-scalbnl-scalbln-scalblnf-scalblnl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [sin](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/asin-asinf-asinl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [sinf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/asin-asinf-asinl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [sinh](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/asinh-asinhf-asinhl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [sinhf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/asinh-asinhf-asinhl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [sqrt](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/csqrt-csqrtf-csqrtl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [sqrtf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/csqrt-csqrtf-csqrtl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [tan](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/atan-atanf-atanl-atan2-atan2f-atan2l) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [tanf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/atan-atanf-atanl-atan2-atan2f-atan2l) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [tanh](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/atanh-atanhf-atanhl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [tanhf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/atanh-atanhf-atanhl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [tgamma](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/tgamma-tgammaf-tgammal) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [tgammaf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/tgamma-tgammaf-tgammal) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [tgammal](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/tgamma-tgammaf-tgammal) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [trunc](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/trunc-truncf-truncl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [truncf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/trunc-truncf-truncl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [truncl](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/trunc-truncf-truncl) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |


## APIs from api-ms-win-crt-multibyte-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [__p__mbcasemap](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| [__p__mbctype](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| [_ismbbalnum](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ismbbalnum-ismbbalnum-l) | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| [_ismbbalnum_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ismbbalnum-ismbbalnum-l) | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| [_ismbbalpha](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ismbbalpha-ismbbalpha-l) | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| [_ismbbalpha_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ismbbalpha-ismbbalpha-l) | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| [_ismbbblank](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ismbbblank-ismbbblank-l) | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| [_ismbbblank_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ismbbblank-ismbbblank-l) | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| [_ismbbgraph](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ismbbgraph-ismbbgraph-l) | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| [_ismbbgraph_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ismbbgraph-ismbbgraph-l) | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| [_ismbbkalnum](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ismbbkalnum-ismbbkalnum-l) | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| [_ismbbkalnum_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ismbbkalnum-ismbbkalnum-l) | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| [_ismbbkana](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ismbbkana-ismbbkana-l) | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| [_ismbbkana_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ismbbkana-ismbbkana-l) | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| [_ismbbkprint](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ismbbkprint-ismbbkprint-l) | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| [_ismbbkprint_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ismbbkprint-ismbbkprint-l) | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| [_ismbbkpunct](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ismbbkpunct-ismbbkpunct-l) | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| [_ismbbkpunct_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ismbbkpunct-ismbbkpunct-l) | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| [_ismbblead](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ismbblead-ismbblead-l) | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| [_ismbblead_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ismbblead-ismbblead-l) | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| [_ismbbprint](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ismbbprint-ismbbprint-l) | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| [_ismbbprint_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ismbbprint-ismbbprint-l) | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| [_ismbbpunct](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ismbbpunct-ismbbpunct-l) | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| [_ismbbpunct_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ismbbpunct-ismbbpunct-l) | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| [_ismbbtrail](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ismbbtrail-ismbbtrail-l) | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| [_ismbbtrail_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ismbbtrail-ismbbtrail-l) | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| [_ismbslead](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ismbslead-ismbstrail-ismbslead-l-ismbstrail-l) | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| [_ismbslead_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ismbslead-ismbstrail-ismbslead-l-ismbstrail-l) | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| [_ismbstrail](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ismbslead-ismbstrail-ismbslead-l-ismbstrail-l) | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| [_ismbstrail_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ismbslead-ismbstrail-ismbslead-l-ismbstrail-l) | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| _mbcasemap | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| [_mblen_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/mbclen-mblen-mblen-l) | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| [_mbsdup](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strdup-wcsdup-mbsdup) | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| [_mbstowcs_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/mbstowcs-mbstowcs-l) | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| [_mbstowcs_s_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/mbstowcs-s-mbstowcs-s-l) | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| [_mbstrlen](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strlen-wcslen-mbslen-mbslen-l-mbstrlen-mbstrlen-l) | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| [_mbstrlen_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strlen-wcslen-mbslen-mbslen-l-mbstrlen-mbstrlen-l) | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| [_mbstrnlen](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strnlen-strnlen-s) | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| [_mbstrnlen_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strnlen-strnlen-s) | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| [_mbtowc_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/mbtowc-mbtowc-l) | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |


## APIs from api-ms-win-crt-runtime-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [__control87_2](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/control87-controlfp-control87-2) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [__doserrno](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [__fpe_flt_rounds](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [__fpecode](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [__p___argc](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [__p___argv](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [__p___wargv](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [__p__acmdln](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [__p__pgmptr](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [__p__wcmdln](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [__p__wpgmptr](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [__pxcptinfoptrs](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [__sys_errlist](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [__sys_nerr](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [__threadhandle](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [__threadid](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [__wcserror](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strerror-strerror-wcserror-wcserror) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [__wcserror_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strerror-s-strerror-s-wcserror-s-wcserror-s) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [_assert](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/assert-macro-assert-wassert) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [_beginthread](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/beginthread-beginthreadex) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [_beginthreadex](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/beginthread-beginthreadex) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [_c_exit](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/cexit-c-exit) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [_cexit](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/cexit-c-exit) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [_clearfp](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/clear87-clearfp) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [_configure_narrow_argv](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [_configure_wide_argv](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [_control87](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/control87-controlfp-control87-2) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [_controlfp](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/control87-controlfp-control87-2) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [_controlfp_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/controlfp-s) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [_crt_at_quick_exit](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [_crt_atexit](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _crt_debugger_hook | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [_endthread](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/endthread-endthreadex) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [_endthreadex](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/endthread-endthreadex) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [_errno](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/get-errno) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [_execute_onexit_table](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [_Exit](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/exit-exit-exit) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [_exit](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/amsg-exit) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [_fpieee_flt](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fpieee-flt) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [_fpreset](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fpreset) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [_get_doserrno](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/get-doserrno) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [_get_errno](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/get-errno) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [_get_initial_narrow_environment](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [_get_initial_wide_environment](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [_get_invalid_parameter_handler](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/get-invalid-parameter-handler-get-thread-local-invalid-parameter-handler) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [_get_narrow_winmain_command_line](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [_get_pgmptr](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/get-pgmptr) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [_get_terminate](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/get-terminate) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [_get_thread_local_invalid_parameter_handler](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/get-invalid-parameter-handler-get-thread-local-invalid-parameter-handler) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [_get_wide_winmain_command_line](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [_get_wpgmptr](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/get-wpgmptr) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [_getpid](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/getpid) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [_initialize_narrow_environment](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [_initialize_onexit_table](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [_initialize_wide_environment](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [_initterm](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/initterm-initterm-e) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [_initterm_e](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/initterm-initterm-e) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [_invalid_parameter_noinfo](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/invalid-parameter-functions) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [_invalid_parameter_noinfo_noreturn](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/invalid-parameter-functions) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [_invoke_watson](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/invalid-parameter-functions) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _query_app_type | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [_register_onexit_function](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [_register_thread_local_exe_atexit_callback](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [_seh_filter_dll](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/seh-filter-dll-seh-filter-exe) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [_seh_filter_exe](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/seh-filter-dll-seh-filter-exe) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [_set_abort_behavior](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/set-abort-behavior) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _set_app_type | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [_set_controlfp](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/set-controlfp) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [_set_doserrno](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/set-doserrno) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [_set_errno](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/set-errno) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [_set_error_mode](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/set-error-mode) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [_set_invalid_parameter_handler](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/set-invalid-parameter-handler-set-thread-local-invalid-parameter-handler) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [_set_new_handler](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/set-new-handler) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [_set_thread_local_invalid_parameter_handler](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/set-invalid-parameter-handler-set-thread-local-invalid-parameter-handler) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _sleep | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [_statusfp](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/status87-statusfp-statusfp2) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [_statusfp2](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/status87-statusfp-statusfp2) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [_strerror](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strerror-strerror-wcserror-wcserror) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [_strerror_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strerror-s-strerror-s-wcserror-s-wcserror-s) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [_wassert](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/assert-macro-assert-wassert) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [_wcserror](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strerror-strerror-wcserror-wcserror) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [_wcserror_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strerror-s-strerror-s-wcserror-s-wcserror-s) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [_wperror](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/perror-wperror) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [abort](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/abort) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [exit](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/amsg-exit) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [feclearexcept](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/feclearexcept1) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [fegetenv](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fegetenv1) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [fegetexceptflag](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fegetexceptflag2) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [fegetround](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fegetround-fesetround2) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [feholdexcept](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/feholdexcept2) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [fesetenv](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fesetenv1) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [fesetexceptflag](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fesetexceptflag2) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [fesetround](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fegetround-fesetround2) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [fetestexcept](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fetestexcept1) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [perror](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/perror-wperror) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [quick_exit](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/quick-exit1) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [raise](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/feraiseexcept) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [set_terminate](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/set-terminate-crt) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [signal](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/signal) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [strerror](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strerror-strerror-wcserror-wcserror) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [strerror_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strerror-s-strerror-s-wcserror-s-wcserror-s) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [terminate](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/get-terminate) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |


## APIs from api-ms-win-crt-stdio-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [__acrt_iob_func](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [__p__commode](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [__p__fmode](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [__stdio_common_vfprintf](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [__stdio_common_vfprintf_p](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [__stdio_common_vfprintf_s](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [__stdio_common_vfscanf](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [__stdio_common_vfwprintf](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [__stdio_common_vfwprintf_p](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [__stdio_common_vfwprintf_s](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [__stdio_common_vfwscanf](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [__stdio_common_vsnprintf_s](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [__stdio_common_vsnwprintf_s](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [__stdio_common_vsprintf](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [__stdio_common_vsprintf_p](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [__stdio_common_vsprintf_s](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [__stdio_common_vsscanf](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [__stdio_common_vswprintf](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [__stdio_common_vswprintf_p](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [__stdio_common_vswprintf_s](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [__stdio_common_vswscanf](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_chsize](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/chsize) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_chsize_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/chsize-s) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_close](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/close) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_commit](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/commit) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_creat](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/creat-wcreat) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_dup](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/dup-dup2) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_dup2](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/dup-dup2) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_eof](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/eof) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_fclose_nolock](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fclose-nolock) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_fcloseall](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fclose-fcloseall) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_fflush_nolock](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fflush-nolock) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_fgetc_nolock](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fgetc-nolock-fgetwc-nolock) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_fgetchar](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fgetchar-fgetwchar) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_fgetwc_nolock](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fgetc-nolock-fgetwc-nolock) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_fgetwchar](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fgetchar-fgetwchar) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_filelength](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/filelength-filelengthi64) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_filelengthi64](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/filelength-filelengthi64) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_fileno](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fileno) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_flushall](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/flushall) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_fputc_nolock](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fputc-nolock-fputwc-nolock) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_fputchar](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fputchar-fputwchar) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_fputwc_nolock](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fputc-nolock-fputwc-nolock) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_fputwchar](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fputchar-fputwchar) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_fread_nolock](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fread-nolock) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_fread_nolock_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fread-nolock-s2) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_fseek_nolock](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fseek-nolock-fseeki64-nolock) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_fseeki64](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fseek-fseeki64) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_fseeki64_nolock](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fseek-nolock-fseeki64-nolock) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_fsopen](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fsopen-wfsopen) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_ftell_nolock](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ftell-nolock-ftelli64-nolock) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_ftelli64](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ftell-ftelli64) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_ftelli64_nolock](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ftell-nolock-ftelli64-nolock) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_fwrite_nolock](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fwrite-nolock) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_get_fmode](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/get-fmode) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_get_osfhandle](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/get-osfhandle) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_get_printf_count_output](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/get-printf-count-output) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_get_stream_buffer_pointers](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_getc_nolock](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/getc-nolock-getwc-nolock) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_getmaxstdio](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/getmaxstdio) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_getw](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/getw) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_getwc_nolock](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/getc-nolock-getwc-nolock) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_getws](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/gets-s-getws-s) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_getws_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/gets-s-getws-s) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_isatty](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/isatty) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_locking](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/locking) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_lseek](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/lseek-lseeki64) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_lseeki64](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/lseek-lseeki64) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_mktemp](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/mktemp-wmktemp) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_mktemp_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/mktemp-s-wmktemp-s) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_open](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/open-wopen) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_open_osfhandle](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/open-osfhandle) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_putc_nolock](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/putc-nolock-putwc-nolock) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_putw](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/putw) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_putwc_nolock](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/putc-nolock-putwc-nolock) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_putws](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/puts-putws) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_read](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/read) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_rmtmp](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/rmtmp) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_set_fmode](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/set-fmode) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_set_printf_count_output](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/set-printf-count-output) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_setmaxstdio](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/setmaxstdio) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_setmode](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/setmode) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_sopen](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/sopen-wsopen) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_sopen_dispatch](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_sopen_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/sopen-s-wsopen-s) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_tell](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/tell-telli64) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_telli64](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/tell-telli64) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_tempnam](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/tempnam-wtempnam-tmpnam-wtmpnam) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_ungetc_nolock](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ungetc-nolock-ungetwc-nolock) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_ungetwc_nolock](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ungetc-nolock-ungetwc-nolock) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_wcreat](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/creat-wcreat) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_wfdopen](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fdopen-wfdopen) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_wfopen](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fopen-wfopen) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_wfopen_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fopen-s-wfopen-s) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_wfreopen](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/freopen-wfreopen) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_wfreopen_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/freopen-s-wfreopen-s) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_wfsopen](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fsopen-wfsopen) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_wmktemp](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/mktemp-wmktemp) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_wmktemp_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/mktemp-s-wmktemp-s) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_wopen](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/open-wopen) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_write](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/write) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_wsopen](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/sopen-wsopen) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_wsopen_dispatch](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_wsopen_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/sopen-s-wsopen-s) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_wtempnam](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/tempnam-wtempnam-tmpnam-wtmpnam) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_wtmpnam](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/tempnam-wtempnam-tmpnam-wtmpnam) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [_wtmpnam_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/tmpnam-s-wtmpnam-s) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [clearerr](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/clearerr) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [clearerr_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/clearerr-s) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [fclose](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fclose-fcloseall) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [feof](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/feof) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [ferror](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ferror) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [fflush](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fflush) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [fgetc](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fgetc-fgetwc) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [fgetpos](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fgetpos) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [fgets](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fgets-fgetws) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [fgetwc](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fgetc-fgetwc) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [fgetws](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fgets-fgetws) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [fopen](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fopen-wfopen) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [fopen_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fopen-s-wfopen-s) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [fputc](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fputc-fputwc) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [fputs](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fputs-fputws) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [fputwc](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fputc-fputwc) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [fputws](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fputs-fputws) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [fread](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fread) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [fread_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fread-s) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [freopen](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/freopen-wfreopen) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [freopen_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/freopen-s-wfreopen-s) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [fseek](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fseek-fseeki64) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [fsetpos](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fsetpos) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [ftell](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ftell-ftelli64) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [fwrite](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fwrite) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [getc](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fgetc-fgetwc) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [getchar](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fgetchar) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [gets_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/cgets-s-cgetws-s) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [getwc](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fgetc-fgetwc) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [getwchar](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fgetchar-fgetwchar) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [putc](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fputc-fputwc) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [putchar](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fputchar) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [puts](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/cputs) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [putwc](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fputc-fputwc) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [putwchar](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/fputchar-fputwchar) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [rewind](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/rewind) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [setbuf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/setbuf) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [setvbuf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/setvbuf) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [tmpfile](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/tmpfile) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [tmpfile_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/tmpfile-s) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [tmpnam](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/tempnam-wtempnam-tmpnam-wtmpnam) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [tmpnam_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/tmpnam-s-wtmpnam-s) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [ungetc](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ungetc-ungetwc) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| [ungetwc](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ungetc-ungetwc) | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |


## APIs from api-ms-win-crt-string-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [__isascii](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/isascii-isascii-iswascii) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [__iscsym](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/iscsym-functions) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [__iscsymf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/iscsym-functions) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [__iswcsym](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/iscsym-functions) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [__iswcsymf](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/iscsym-functions) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [__strncnt](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [__wcsncnt](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_isalnum_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/isalnum-iswalnum-isalnum-l-iswalnum-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_isalpha_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/isalpha-iswalpha-isalpha-l-iswalpha-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_isblank_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/isblank-iswblank-isblank-l-iswblank-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_iscntrl_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/iscntrl-iswcntrl-iscntrl-l-iswcntrl-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_isctype](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/isctype-iswctype-isctype-l-iswctype-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_isctype_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/isctype-iswctype-isctype-l-iswctype-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_isdigit_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/isdigit-iswdigit-isdigit-l-iswdigit-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_isgraph_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/isgraph-iswgraph-isgraph-l-iswgraph-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_isleadbyte_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/isleadbyte-isleadbyte-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_islower_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/islower-iswlower-islower-l-iswlower-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_isprint_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/isprint-iswprint-isprint-l-iswprint-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_ispunct_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ispunct-iswpunct-ispunct-l-iswpunct-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_isspace_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/isspace-iswspace-isspace-l-iswspace-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_isupper_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/isupper-isupper-l-iswupper-iswupper-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_iswalnum_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/isalnum-iswalnum-isalnum-l-iswalnum-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_iswalpha_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/isalpha-iswalpha-isalpha-l-iswalpha-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_iswblank_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/isblank-iswblank-isblank-l-iswblank-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_iswcntrl_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/iscntrl-iswcntrl-iscntrl-l-iswcntrl-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_iswcsym_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/iscsym-functions) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_iswcsymf_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/iscsym-functions) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_iswctype_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/isctype-iswctype-isctype-l-iswctype-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_iswdigit_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/isdigit-iswdigit-isdigit-l-iswdigit-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_iswgraph_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/isgraph-iswgraph-isgraph-l-iswgraph-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_iswlower_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/islower-iswlower-islower-l-iswlower-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_iswprint_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/isprint-iswprint-isprint-l-iswprint-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_iswpunct_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ispunct-iswpunct-ispunct-l-iswpunct-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_iswspace_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/isspace-iswspace-isspace-l-iswspace-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_iswupper_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/isupper-isupper-l-iswupper-iswupper-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_iswxdigit_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/isxdigit-iswxdigit-isxdigit-l-iswxdigit-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_isxdigit_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/isxdigit-iswxdigit-isxdigit-l-iswxdigit-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_memccpy](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/memccpy) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_memicmp](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/memicmp-memicmp-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_memicmp_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/memicmp-memicmp-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_strcoll_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strcoll-wcscoll-mbscoll-strcoll-l-wcscoll-l-mbscoll-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_strdup](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strdup-wcsdup-mbsdup) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_stricmp](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/stricmp-wcsicmp-mbsicmp-stricmp-l-wcsicmp-l-mbsicmp-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_stricmp_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/stricmp-wcsicmp-mbsicmp-stricmp-l-wcsicmp-l-mbsicmp-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_stricoll](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/stricoll-wcsicoll-mbsicoll-stricoll-l-wcsicoll-l-mbsicoll-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_stricoll_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/stricoll-wcsicoll-mbsicoll-stricoll-l-wcsicoll-l-mbsicoll-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_strlwr](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strlwr-wcslwr-mbslwr-strlwr-l-wcslwr-l-mbslwr-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_strlwr_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strlwr-wcslwr-mbslwr-strlwr-l-wcslwr-l-mbslwr-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_strlwr_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strlwr-s-strlwr-s-l-mbslwr-s-mbslwr-s-l-wcslwr-s-wcslwr-s-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_strlwr_s_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strlwr-s-strlwr-s-l-mbslwr-s-mbslwr-s-l-wcslwr-s-wcslwr-s-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_strncoll](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strncoll-wcsncoll-mbsncoll-strncoll-l-wcsncoll-l-mbsncoll-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_strncoll_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strncoll-wcsncoll-mbsncoll-strncoll-l-wcsncoll-l-mbsncoll-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_strnicmp](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strnicmp-wcsnicmp-mbsnicmp-strnicmp-l-wcsnicmp-l-mbsnicmp-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_strnicmp_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strnicmp-wcsnicmp-mbsnicmp-strnicmp-l-wcsnicmp-l-mbsnicmp-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_strnicoll](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strnicoll-wcsnicoll-mbsnicoll-strnicoll-l-wcsnicoll-l-mbsnicoll-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_strnicoll_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strnicoll-wcsnicoll-mbsnicoll-strnicoll-l-wcsnicoll-l-mbsnicoll-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_strnset](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strnset-strnset-l-wcsnset-wcsnset-l-mbsnset-mbsnset-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_strnset_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strnset-s-strnset-s-l-wcsnset-s-wcsnset-s-l-mbsnset-s-mbsnset-s-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_strrev](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strrev-wcsrev-mbsrev-mbsrev-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_strset](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strset-strset-l-wcsset-wcsset-l-mbsset-mbsset-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_strset_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strset-s-strset-s-l-wcsset-s-wcsset-s-l-mbsset-s-mbsset-s-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_strupr](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strupr-strupr-l-mbsupr-mbsupr-l-wcsupr-l-wcsupr) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_strupr_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strupr-strupr-l-mbsupr-mbsupr-l-wcsupr-l-wcsupr) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_strupr_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strupr-s-strupr-s-l-mbsupr-s-mbsupr-s-l-wcsupr-s-wcsupr-s-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_strupr_s_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strupr-s-strupr-s-l-mbsupr-s-mbsupr-s-l-wcsupr-s-wcsupr-s-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_strxfrm_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strxfrm-wcsxfrm-strxfrm-l-wcsxfrm-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_tolower](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/tolower-tolower-towlower-tolower-l-towlower-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_tolower_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/tolower-tolower-towlower-tolower-l-towlower-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_toupper](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/toupper-toupper-towupper-toupper-l-towupper-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_toupper_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/toupper-toupper-towupper-toupper-l-towupper-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_towlower_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/tolower-tolower-towlower-tolower-l-towlower-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_towupper_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/toupper-toupper-towupper-toupper-l-towupper-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_wcscoll_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strcoll-wcscoll-mbscoll-strcoll-l-wcscoll-l-mbscoll-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_wcsdup](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strdup-wcsdup-mbsdup) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_wcsicmp](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/stricmp-wcsicmp-mbsicmp-stricmp-l-wcsicmp-l-mbsicmp-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_wcsicmp_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/stricmp-wcsicmp-mbsicmp-stricmp-l-wcsicmp-l-mbsicmp-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_wcsicoll](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/stricoll-wcsicoll-mbsicoll-stricoll-l-wcsicoll-l-mbsicoll-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_wcsicoll_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/stricoll-wcsicoll-mbsicoll-stricoll-l-wcsicoll-l-mbsicoll-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_wcslwr](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strlwr-wcslwr-mbslwr-strlwr-l-wcslwr-l-mbslwr-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_wcslwr_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strlwr-wcslwr-mbslwr-strlwr-l-wcslwr-l-mbslwr-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_wcslwr_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strlwr-s-strlwr-s-l-mbslwr-s-mbslwr-s-l-wcslwr-s-wcslwr-s-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_wcslwr_s_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strlwr-s-strlwr-s-l-mbslwr-s-mbslwr-s-l-wcslwr-s-wcslwr-s-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_wcsncoll](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strncoll-wcsncoll-mbsncoll-strncoll-l-wcsncoll-l-mbsncoll-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_wcsncoll_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strncoll-wcsncoll-mbsncoll-strncoll-l-wcsncoll-l-mbsncoll-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_wcsnicmp](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strnicmp-wcsnicmp-mbsnicmp-strnicmp-l-wcsnicmp-l-mbsnicmp-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_wcsnicmp_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strnicmp-wcsnicmp-mbsnicmp-strnicmp-l-wcsnicmp-l-mbsnicmp-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_wcsnicoll](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strnicoll-wcsnicoll-mbsnicoll-strnicoll-l-wcsnicoll-l-mbsnicoll-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_wcsnicoll_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strnicoll-wcsnicoll-mbsnicoll-strnicoll-l-wcsnicoll-l-mbsnicoll-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_wcsnset](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strnset-strnset-l-wcsnset-wcsnset-l-mbsnset-mbsnset-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_wcsnset_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strnset-s-strnset-s-l-wcsnset-s-wcsnset-s-l-mbsnset-s-mbsnset-s-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_wcsrev](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strrev-wcsrev-mbsrev-mbsrev-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_wcsset](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strset-strset-l-wcsset-wcsset-l-mbsset-mbsset-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_wcsset_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strset-s-strset-s-l-wcsset-s-wcsset-s-l-mbsset-s-mbsset-s-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_wcsupr](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strupr-strupr-l-mbsupr-mbsupr-l-wcsupr-l-wcsupr) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_wcsupr_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strupr-strupr-l-mbsupr-mbsupr-l-wcsupr-l-wcsupr) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_wcsupr_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strupr-s-strupr-s-l-mbsupr-s-mbsupr-s-l-wcsupr-s-wcsupr-s-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_wcsupr_s_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strupr-s-strupr-s-l-mbsupr-s-mbsupr-s-l-wcsupr-s-wcsupr-s-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_wcsxfrm_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strxfrm-wcsxfrm-strxfrm-l-wcsxfrm-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [_wctype](https://docs.microsoft.com/en-us/cpp/c-runtime-library/pctype-pwctype-wctype-mbctype-mbcasemap) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [isalnum](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/isalnum-iswalnum-isalnum-l-iswalnum-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [isalpha](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/isalpha-iswalpha-isalpha-l-iswalpha-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [isblank](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/isblank-iswblank-isblank-l-iswblank-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [iscntrl](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/iscntrl-iswcntrl-iscntrl-l-iswcntrl-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [isdigit](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/isdigit-iswdigit-isdigit-l-iswdigit-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [isgraph](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/isgraph-iswgraph-isgraph-l-iswgraph-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [isleadbyte](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/isleadbyte-isleadbyte-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [islower](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/islower-iswlower-islower-l-iswlower-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [isprint](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/isprint-iswprint-isprint-l-iswprint-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [ispunct](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ispunct-iswpunct-ispunct-l-iswpunct-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [isspace](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/isspace-iswspace-isspace-l-iswspace-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [isupper](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/isupper-isupper-l-iswupper-iswupper-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [iswalnum](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/isalnum-iswalnum-isalnum-l-iswalnum-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [iswalpha](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/isalpha-iswalpha-isalpha-l-iswalpha-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [iswascii](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/isascii-isascii-iswascii) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [iswblank](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/isblank-iswblank-isblank-l-iswblank-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [iswcntrl](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/iscntrl-iswcntrl-iscntrl-l-iswcntrl-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [iswctype](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/isctype-iswctype-isctype-l-iswctype-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [iswdigit](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/isdigit-iswdigit-isdigit-l-iswdigit-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [iswgraph](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/isgraph-iswgraph-isgraph-l-iswgraph-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [iswlower](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/islower-iswlower-islower-l-iswlower-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [iswprint](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/isprint-iswprint-isprint-l-iswprint-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [iswpunct](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ispunct-iswpunct-ispunct-l-iswpunct-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [iswspace](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/isspace-iswspace-isspace-l-iswspace-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [iswupper](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/isupper-isupper-l-iswupper-iswupper-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [iswxdigit](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/isxdigit-iswxdigit-isxdigit-l-iswxdigit-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [isxdigit](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/isxdigit-iswxdigit-isxdigit-l-iswxdigit-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [mblen](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/mbclen-mblen-mblen-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [mbrlen](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/mbrlen) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [memcpy_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/memcpy-s-wmemcpy-s) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [memset](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/memset-wmemset) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [strcat](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strcat-wcscat-mbscat) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [strcat_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strcat-s-wcscat-s-mbscat-s) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [strcmp](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strcmp-wcscmp-mbscmp) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [strcoll](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strcoll-wcscoll-mbscoll-strcoll-l-wcscoll-l-mbscoll-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [strcpy](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strcpy-wcscpy-mbscpy) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [strcpy_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strcpy-s-wcscpy-s-mbscpy-s) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [strcspn](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strcspn-wcscspn-mbscspn-mbscspn-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [strlen](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strlen-wcslen-mbslen-mbslen-l-mbstrlen-mbstrlen-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [strncat](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strncat-strncat-l-wcsncat-wcsncat-l-mbsncat-mbsncat-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [strncat_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strncat-s-strncat-s-l-wcsncat-s-wcsncat-s-l-mbsncat-s-mbsncat-s-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [strncmp](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strncmp-wcsncmp-mbsncmp-mbsncmp-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [strncpy](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strncpy-strncpy-l-wcsncpy-wcsncpy-l-mbsncpy-mbsncpy-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [strncpy_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strncpy-s-strncpy-s-l-wcsncpy-s-wcsncpy-s-l-mbsncpy-s-mbsncpy-s-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [strnlen](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strnlen-strnlen-s) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [strpbrk](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strpbrk-wcspbrk-mbspbrk-mbspbrk-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [strspn](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strspn-wcsspn-mbsspn-mbsspn-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [strtok](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strtok-strtok-l-wcstok-wcstok-l-mbstok-mbstok-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [strtok_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strtok-s-strtok-s-l-wcstok-s-wcstok-s-l-mbstok-s-mbstok-s-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [strxfrm](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strxfrm-wcsxfrm-strxfrm-l-wcsxfrm-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [tolower](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/mbctolower-mbctolower-l-mbctoupper-mbctoupper-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [toupper](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/mbctolower-mbctolower-l-mbctoupper-mbctoupper-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [towctrans](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/towctrans) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [towlower](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/tolower-tolower-towlower-tolower-l-towlower-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [towupper](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/toupper-toupper-towupper-toupper-l-towupper-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [wcscat](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strcat-wcscat-mbscat) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [wcscat_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strcat-s-wcscat-s-mbscat-s) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [wcscmp](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strcmp-wcscmp-mbscmp) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [wcscoll](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strcoll-wcscoll-mbscoll-strcoll-l-wcscoll-l-mbscoll-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [wcscpy](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strcpy-wcscpy-mbscpy) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [wcscpy_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strcpy-s-wcscpy-s-mbscpy-s) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [wcscspn](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strcspn-wcscspn-mbscspn-mbscspn-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [wcslen](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strlen-wcslen-mbslen-mbslen-l-mbstrlen-mbstrlen-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [wcsncat](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strncat-strncat-l-wcsncat-wcsncat-l-mbsncat-mbsncat-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [wcsncat_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strncat-s-strncat-s-l-wcsncat-s-wcsncat-s-l-mbsncat-s-mbsncat-s-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [wcsncmp](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strncmp-wcsncmp-mbsncmp-mbsncmp-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [wcsncpy](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strncpy-strncpy-l-wcsncpy-wcsncpy-l-mbsncpy-mbsncpy-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [wcsncpy_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strncpy-s-strncpy-s-l-wcsncpy-s-wcsncpy-s-l-mbsncpy-s-mbsncpy-s-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [wcsnlen](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strnlen-strnlen-s) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [wcspbrk](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strpbrk-wcspbrk-mbspbrk-mbspbrk-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [wcsspn](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strspn-wcsspn-mbsspn-mbsspn-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [wcstok](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strtok-strtok-l-wcstok-wcstok-l-mbstok-mbstok-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [wcstok_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strtok-s-strtok-s-l-wcstok-s-wcstok-s-l-mbstok-s-mbstok-s-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [wcsxfrm](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strxfrm-wcsxfrm-strxfrm-l-wcsxfrm-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [wctype](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/isctype-iswctype-isctype-l-iswctype-l) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [wmemcpy_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/memcpy-s-wmemcpy-s) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [wmemmove_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/memmove-s-wmemmove-s) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [memmove_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/memmove-s-wmemmove-s) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.15063. |


## APIs from api-ms-win-crt-time-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [__daylight](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [__dstbias](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [__timezone](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [__tzname](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [_ctime32](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ctime-ctime32-ctime64-wctime-wctime32-wctime64) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [_ctime32_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ctime-s-ctime32-s-ctime64-s-wctime-s-wctime32-s-wctime64-s) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [_ctime64](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ctime-ctime32-ctime64-wctime-wctime32-wctime64) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [_ctime64_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ctime-s-ctime32-s-ctime64-s-wctime-s-wctime32-s-wctime64-s) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [_difftime32](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/difftime-difftime32-difftime64) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [_difftime64](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/difftime-difftime32-difftime64) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [_ftime32](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ftime-ftime32-ftime64) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [_ftime32_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ftime-s-ftime32-s-ftime64-s) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [_ftime64](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ftime-ftime32-ftime64) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [_ftime64_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ftime-s-ftime32-s-ftime64-s) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [_futime32](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/futime-futime32-futime64) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [_futime64](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/futime-futime32-futime64) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [_get_daylight](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/get-daylight) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [_get_dstbias](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/get-dstbias) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [_get_timezone](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/get-timezone) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [_get_tzname](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/get-tzname) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [_Getdays](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [_Getmonths](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [_Gettnames](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [_gmtime32](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/gmtime-gmtime32-gmtime64) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [_gmtime32_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/gmtime-s-gmtime32-s-gmtime64-s) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [_gmtime64](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/gmtime-gmtime32-gmtime64) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [_gmtime64_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/gmtime-s-gmtime32-s-gmtime64-s) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [_localtime32](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/localtime-localtime32-localtime64) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [_localtime32_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/localtime-s-localtime32-s-localtime64-s) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [_localtime64](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/localtime-localtime32-localtime64) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [_localtime64_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/localtime-s-localtime32-s-localtime64-s) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [_mkgmtime32](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/mkgmtime-mkgmtime32-mkgmtime64) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [_mkgmtime64](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/mkgmtime-mkgmtime32-mkgmtime64) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [_mktime64](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/mktime-mktime32-mktime64) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [_mktime32](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/mktime-mktime32-mktime64) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [_strdate](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strdate-wstrdate) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [_strdate_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strdate-s-wstrdate-s) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [_Strftime](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [_strftime_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strftime-wcsftime-strftime-l-wcsftime-l) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [_strtime](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strtime-wstrtime) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [_strtime_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strtime-s-wstrtime-s) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [_time32](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/time-time32-time64) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [_time64](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/time-time32-time64) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [_timespec32_get](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/timespec-get-timespec32-get-timespec64-get1) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [_timespec64_get](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/timespec-get-timespec32-get-timespec64-get1) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [_tzset](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/tzset) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [_utime32](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/utime-utime32-utime64-wutime-wutime32-wutime64) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [_utime64](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/utime-utime32-utime64-wutime-wutime32-wutime64) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [_W_Getdays](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [_W_Getmonths](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| _W_Gettnames | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [_wasctime](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/asctime-wasctime) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [_wasctime_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/asctime-s-wasctime-s) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [_Wcsftime](https://msdn.microsoft.com/en-us/library/dn727675.aspx) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [_wcsftime_l](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strftime-wcsftime-strftime-l-wcsftime-l) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [_wctime32](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ctime-ctime32-ctime64-wctime-wctime32-wctime64) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [_wctime32_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ctime-s-ctime32-s-ctime64-s-wctime-s-wctime32-s-wctime64-s) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [_wctime64](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ctime-ctime32-ctime64-wctime-wctime32-wctime64) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [_wctime64_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ctime-s-ctime32-s-ctime64-s-wctime-s-wctime32-s-wctime64-s) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [_wstrdate](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strdate-wstrdate) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [_wstrdate_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strdate-s-wstrdate-s) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [_wstrtime](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strtime-wstrtime) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [_wstrtime_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strtime-s-wstrtime-s) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [_wutime32](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/utime-utime32-utime64-wutime-wutime32-wutime64) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [_wutime64](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/utime-utime32-utime64-wutime-wutime32-wutime64) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [asctime](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/asctime-wasctime) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [asctime_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/asctime-s-wasctime-s) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [clock](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/clock) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [strftime](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strftime-wcsftime-strftime-l-wcsftime-l) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| [wcsftime](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/strftime-wcsftime-strftime-l-wcsftime-l) | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |


## APIs from api-ms-win-crt-utility-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [_abs64](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/abs-labs-llabs-abs64) | Introduced into api-ms-win-crt-utility-l1-1-0.dll in 10.0.10240. |
| [_byteswap_uint64](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/byteswap-uint64-byteswap-ulong-byteswap-ushort) | Introduced into api-ms-win-crt-utility-l1-1-0.dll in 10.0.10240. |
| [_byteswap_ulong](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/byteswap-uint64-byteswap-ulong-byteswap-ushort) | Introduced into api-ms-win-crt-utility-l1-1-0.dll in 10.0.10240. |
| [_byteswap_ushort](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/byteswap-uint64-byteswap-ulong-byteswap-ushort) | Introduced into api-ms-win-crt-utility-l1-1-0.dll in 10.0.10240. |
| [_lfind](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/lfind) | Introduced into api-ms-win-crt-utility-l1-1-0.dll in 10.0.10240. |
| [_lfind_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/lfind-s) | Introduced into api-ms-win-crt-utility-l1-1-0.dll in 10.0.10240. |
| [_lrotl](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/lrotl-lrotr) | Introduced into api-ms-win-crt-utility-l1-1-0.dll in 10.0.10240. |
| [_lrotr](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/lrotl-lrotr) | Introduced into api-ms-win-crt-utility-l1-1-0.dll in 10.0.10240. |
| [_lsearch](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/lsearch) | Introduced into api-ms-win-crt-utility-l1-1-0.dll in 10.0.10240. |
| [_lsearch_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/lsearch-s) | Introduced into api-ms-win-crt-utility-l1-1-0.dll in 10.0.10240. |
| [_rotl](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/rotl-rotl64-rotr-rotr64) | Introduced into api-ms-win-crt-utility-l1-1-0.dll in 10.0.10240. |
| [_rotl64](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/rotl-rotl64-rotr-rotr64) | Introduced into api-ms-win-crt-utility-l1-1-0.dll in 10.0.10240. |
| [_rotr](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/rotl-rotl64-rotr-rotr64) | Introduced into api-ms-win-crt-utility-l1-1-0.dll in 10.0.10240. |
| [_rotr64](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/rotl-rotl64-rotr-rotr64) | Introduced into api-ms-win-crt-utility-l1-1-0.dll in 10.0.10240. |
| [_swab](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/swab) | Introduced into api-ms-win-crt-utility-l1-1-0.dll in 10.0.10240. |
| [abs](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/abs-labs-llabs-abs64) | Introduced into api-ms-win-crt-utility-l1-1-0.dll in 10.0.10240. |
| [bsearch](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/bsearch) | Introduced into api-ms-win-crt-utility-l1-1-0.dll in 10.0.10240. |
| [bsearch_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/bsearch-s) | Introduced into api-ms-win-crt-utility-l1-1-0.dll in 10.0.10240. |
| [div](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/div) | Introduced into api-ms-win-crt-utility-l1-1-0.dll in 10.0.10240. |
| [imaxabs](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/imaxabs) | Introduced into api-ms-win-crt-utility-l1-1-0.dll in 10.0.10240. |
| [imaxdiv](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/imaxdiv) | Introduced into api-ms-win-crt-utility-l1-1-0.dll in 10.0.10240. |
| [labs](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/abs-labs-llabs-abs64) | Introduced into api-ms-win-crt-utility-l1-1-0.dll in 10.0.10240. |
| [ldiv](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ldiv-lldiv) | Introduced into api-ms-win-crt-utility-l1-1-0.dll in 10.0.10240. |
| [llabs](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/abs-labs-llabs-abs64) | Introduced into api-ms-win-crt-utility-l1-1-0.dll in 10.0.10240. |
| [lldiv](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/ldiv-lldiv) | Introduced into api-ms-win-crt-utility-l1-1-0.dll in 10.0.10240. |
| [qsort](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/qsort) | Introduced into api-ms-win-crt-utility-l1-1-0.dll in 10.0.10240. |
| [qsort_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/qsort-s) | Introduced into api-ms-win-crt-utility-l1-1-0.dll in 10.0.10240. |
| [rand](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/rand) | Introduced into api-ms-win-crt-utility-l1-1-0.dll in 10.0.10240. |
| [rand_s](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/rand-s) | Introduced into api-ms-win-crt-utility-l1-1-0.dll in 10.0.10240. |
| [srand](https://docs.microsoft.com/en-us/cpp/c-runtime-library/reference/srand) | Introduced into api-ms-win-crt-utility-l1-1-0.dll in 10.0.10240. |


## APIs from api-ms-win-gaming-tcui-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [CheckGamingPrivilegeSilently](https://msdn.microsoft.com/en-us/library/Mt736759.aspx) | Introduced into api-ms-win-gaming-tcui-l1-1-0.dll in 10.0.10586. Removed in 10.0.14393. |
| [CheckGamingPrivilegeWithUI](https://msdn.microsoft.com/en-us/library/Mt736760.aspx) | Introduced into api-ms-win-gaming-tcui-l1-1-0.dll in 10.0.10586. Removed in 10.0.14393. |


## APIs from winsqlite3.dll

| API | Requirements |
| -----| --------------|
| [sqlite3_aggregate_context](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_aggregate_count](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_auto_extension](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_backup_finish](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_backup_init](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_backup_pagecount](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_backup_remaining](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_backup_step](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_bind_blob](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_bind_blob64](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_bind_double](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_bind_int](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_bind_int64](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_bind_null](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_bind_parameter_count](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_bind_parameter_index](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_bind_parameter_name](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_bind_text](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_bind_text16](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_bind_text64](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_bind_value](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_bind_zeroblob](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_blob_bytes](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_blob_close](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_blob_open](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_blob_read](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_blob_reopen](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_blob_write](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_busy_handler](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_busy_timeout](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_cancel_auto_extension](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_changes](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_clear_bindings](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_close](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_close_v2](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_collation_needed](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_collation_needed16](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_column_blob](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_column_bytes](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_column_bytes16](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_column_count](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_column_database_name](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_column_database_name16](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_column_decltype](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_column_decltype16](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_column_double](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_column_int](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_column_int64](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_column_name](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_column_name16](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_column_origin_name](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_column_origin_name16](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_column_table_name](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_column_table_name16](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_column_text](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_column_text16](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_column_type](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_column_value](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_commit_hook](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_compileoption_get](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_compileoption_used](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_complete](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_complete16](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_config](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_context_db_handle](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_create_collation](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_create_collation16](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_create_collation_v2](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_create_function](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_create_function16](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_create_function_v2](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_create_module](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_create_module_v2](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_data_count](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_data_directory](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_db_config](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_db_filename](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_db_handle](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_db_mutex](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_db_readonly](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_db_release_memory](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_db_status](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_declare_vtab](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_enable_load_extension](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_enable_shared_cache](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_errcode](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_errmsg](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_errmsg16](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_errstr](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_exec](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_expired](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_extended_errcode](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_extended_result_codes](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_file_control](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_finalize](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_free](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_free_table](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_get_autocommit](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_get_auxdata](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_get_table](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_global_recover](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_initialize](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_interrupt](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_last_insert_rowid](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_libversion](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_libversion_number](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_limit](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_load_extension](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_log](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_malloc](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_malloc64](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_memory_alarm](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_memory_highwater](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_memory_used](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_mprintf](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_msize](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_mutex_alloc](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_mutex_enter](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_mutex_free](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_mutex_leave](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_mutex_try](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_next_stmt](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_open](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_open16](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_open_v2](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_os_end](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_os_init](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_overload_function](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_prepare](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_prepare16](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_prepare16_v2](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_prepare_v2](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_profile](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_progress_handler](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_randomness](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_realloc](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_realloc64](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_release_memory](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_reset](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_reset_auto_extension](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_result_blob](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_result_blob64](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_result_double](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_result_error](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_result_error16](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_result_error_code](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_result_error_nomem](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_result_error_toobig](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_result_int](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_result_int64](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_result_null](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_result_text](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_result_text16](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_result_text16be](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_result_text16le](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_result_text64](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_result_value](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_result_zeroblob](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_rollback_hook](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_rtree_geometry_callback](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_rtree_query_callback](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_set_authorizer](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_set_auxdata](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_shutdown](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_sleep](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_snprintf](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_soft_heap_limit](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_soft_heap_limit64](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_sourceid](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_sql](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_status](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_step](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_stmt_busy](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_stmt_readonly](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_stmt_status](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_strglob](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_stricmp](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_strnicmp](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_table_column_metadata](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_temp_directory](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_test_control](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_thread_cleanup](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_threadsafe](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_total_changes](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_trace](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_transfer_bindings](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_update_hook](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_uri_boolean](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_uri_int64](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_uri_parameter](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_user_data](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_value_blob](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_value_bytes](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_value_bytes16](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_value_double](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_value_int](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_value_int64](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_value_numeric_type](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_value_text](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_value_text16](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_value_text16be](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_value_text16le](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_value_type](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_version](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_vfs_find](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_vfs_register](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_vfs_unregister](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_vmprintf](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_vsnprintf](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_vtab_config](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_vtab_on_conflict](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_wal_autocheckpoint](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_wal_checkpoint](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_wal_checkpoint_v2](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_wal_hook](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.10586. |
| [sqlite3_bind_zeroblob64](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.14393. |
| [sqlite3_db_cacheflush](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.14393. |
| [sqlite3_result_subtype](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.14393. |
| [sqlite3_result_zeroblob64](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.14393. |
| [sqlite3_status64](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.14393. |
| [sqlite3_strlike](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.14393. |
| [sqlite3_system_errno](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.14393. |
| [sqlite3_value_dup](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.14393. |
| [sqlite3_value_free](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.14393. |
| [sqlite3_value_subtype](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.14393. |
| [sqlite3_expanded_sql](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.15063. |
| [sqlite3_trace_v2](https://sqlite.org/docs.html) | Introduced into winsqlite3.dll in 10.0.15063. |


## APIs from user32.dll

| API | Requirements |
| -----| --------------|
| [SoundSentry](https://msdn.microsoft.com/en-us/library/aa969269.aspx) | Introduced into user32.dll in 10.0.14393. |
| [GetKeyNameTextA](https://msdn.microsoft.com/en-us/library/windows/desktop/ms646300.aspx) | Introduced into user32.dll in 10.0.14393. |
| [GetKeyNameTextW](https://msdn.microsoft.com/en-us/library/ms646300.aspx) | Introduced into user32.dll in 10.0.14393. |
| [MapVirtualKeyA](https://msdn.microsoft.com/en-us/library/ms646306.aspx) | Introduced into user32.dll in 10.0.14393. |
| [MapVirtualKeyW](https://msdn.microsoft.com/en-us/library/ms646306.aspx) | Introduced into user32.dll in 10.0.14393. |
| [MapVirtualKeyExA](https://msdn.microsoft.com/en-us/library/windows/desktop/ms646307.aspx) | Introduced into user32.dll in 10.0.14393. |
| [MapVirtualKeyExW](https://msdn.microsoft.com/en-us/library/ms646307.aspx) | Introduced into user32.dll in 10.0.14393. |
| [ClipCursor](https://msdn.microsoft.com/en-us/library/ms648383.aspx) | Introduced into user32.dll in 10.0.15063. |
| [GetLastInputInfo](https://msdn.microsoft.com/en-us/library/ms646302.aspx) | Introduced into user32.dll in 10.0.15063. |


## APIs from ResetPhoneForArm32.dll

| API | Requirements |
| -----| --------------|
| ResetPhoneForArm32 | Introduced into ResetPhoneForArm32.dll in 10.0.15063. |


## APIs from OPMXbox.dll

| API | Requirements |
| -----| --------------|
| OPMXboxEnableHDCP | Introduced into OPMXbox.dll in 10.0.15063. |
| OPMXboxGetHDCPStatus | Introduced into OPMXbox.dll in 10.0.15063. |
| OPMXboxGetHDCPStatusAndType | Introduced into OPMXbox.dll in 10.0.15063. |


## APIs from efswrt.dll

| API | Requirements |
| -----| --------------|
| [ProtectFileToEnterpriseIdentity](https://msdn.microsoft.com/en-us/library/Mt622168.aspx) | Introduced into efswrt.dll in 10.0.15063. |
| UnprotectFile | Introduced into efswrt.dll in 10.0.15063. |


## APIs from wer.dll

| API | Requirements |
| -----| --------------|
| [WerStoreOpen](https://msdn.microsoft.com/en-us/library/Mt492590.aspx) | Introduced into wer.dll in 10.0.15063. |
| [WerStoreClose](https://msdn.microsoft.com/en-us/library/Mt796907.aspx) | Introduced into wer.dll in 10.0.15063. |
| [WerFreeString](https://msdn.microsoft.com/en-us/library/Mt492584.aspx) | Introduced into wer.dll in 10.0.15063. |
| [WerStoreGetFirstReportKey](https://msdn.microsoft.com/en-us/library/Mt492588.aspx) | Introduced into wer.dll in 10.0.15063. |
| [WerStoreGetNextReportKey](https://msdn.microsoft.com/en-us/library/Mt492589.aspx) | Introduced into wer.dll in 10.0.15063. |
| [WerStoreQueryReportMetadataV2](https://msdn.microsoft.com/en-us/library/Mt492591.aspx) | Introduced into wer.dll in 10.0.15063. |


## APIs from atiadlxx.dll

| API | Requirements |
| -----| --------------|
| ADL2_Main_Control_GetProcAddress | Introduced into atiadlxx.dll in 10.0.15063. Moved into atiadlxy.dll in 10.0.15063. |


## APIs from aticfx32.dll

| API | Requirements |
| -----| --------------|
| AmdGetCfxModuleHandle | Introduced into aticfx32.dll in 10.0.15063. Moved into aticfx64.dll in 10.0.15063. |


## APIs from amdxc32.dll

| API | Requirements |
| -----| --------------|
| AmdGetDxcModuleHandle | Introduced into amdxc32.dll in 10.0.15063. Moved into amdxc64.dll in 10.0.15063. |


## APIs from atidxx32.dll

| API | Requirements |
| -----| --------------|
| AmdGetDxxModuleHandle | Introduced into atidxx32.dll in 10.0.15063. Moved into atidxx64.dll in 10.0.15063. |


## APIs from nvapi.dll

| API | Requirements |
| -----| --------------|
| nvapi_QueryInterface | Introduced into nvapi.dll in 10.0.15063. Moved into nvapi64.dll in 10.0.15063. |


## APIs from icuuc.dll

| API | Requirements |
| -----| --------------|
| utf8_nextCharSafeBody | Introduced into icuuc.dll in 10.0.15063. |
| utf8_appendCharSafeBody | Introduced into icuuc.dll in 10.0.15063. |
| utf8_prevCharSafeBody | Introduced into icuuc.dll in 10.0.15063. |
| utf8_back1SafeBody | Introduced into icuuc.dll in 10.0.15063. |
| u_versionFromString | Introduced into icuuc.dll in 10.0.15063. |
| u_versionFromUString | Introduced into icuuc.dll in 10.0.15063. |
| u_versionToString | Introduced into icuuc.dll in 10.0.15063. |
| u_getVersion | Introduced into icuuc.dll in 10.0.15063. |
| u_errorName | Introduced into icuuc.dll in 10.0.15063. |
| utrace_setLevel | Introduced into icuuc.dll in 10.0.15063. |
| utrace_getLevel | Introduced into icuuc.dll in 10.0.15063. |
| utrace_setFunctions | Introduced into icuuc.dll in 10.0.15063. |
| utrace_getFunctions | Introduced into icuuc.dll in 10.0.15063. |
| utrace_vformat | Introduced into icuuc.dll in 10.0.15063. |
| utrace_format | Introduced into icuuc.dll in 10.0.15063. |
| utrace_functionName | Introduced into icuuc.dll in 10.0.15063. |
| u_shapeArabic | Introduced into icuuc.dll in 10.0.15063. |
| uscript_getCode | Introduced into icuuc.dll in 10.0.15063. |
| uscript_getName | Introduced into icuuc.dll in 10.0.15063. |
| uscript_getShortName | Introduced into icuuc.dll in 10.0.15063. |
| uscript_getScript | Introduced into icuuc.dll in 10.0.15063. |
| uscript_hasScript | Introduced into icuuc.dll in 10.0.15063. |
| uscript_getScriptExtensions | Introduced into icuuc.dll in 10.0.15063. |
| uscript_getSampleString | Introduced into icuuc.dll in 10.0.15063. |
| uscript_getUsage | Introduced into icuuc.dll in 10.0.15063. |
| uscript_isRightToLeft | Introduced into icuuc.dll in 10.0.15063. |
| uscript_breaksBetweenLetters | Introduced into icuuc.dll in 10.0.15063. |
| uscript_isCased | Introduced into icuuc.dll in 10.0.15063. |
| ulistfmt_open | Introduced into icuuc.dll in 10.0.15063. |
| ulistfmt_close | Introduced into icuuc.dll in 10.0.15063. |
| ulistfmt_format | Introduced into icuuc.dll in 10.0.15063. |
| uiter_current32 | Introduced into icuuc.dll in 10.0.15063. |
| uiter_next32 | Introduced into icuuc.dll in 10.0.15063. |
| uiter_previous32 | Introduced into icuuc.dll in 10.0.15063. |
| uiter_getState | Introduced into icuuc.dll in 10.0.15063. |
| uiter_setState | Introduced into icuuc.dll in 10.0.15063. |
| uiter_setString | Introduced into icuuc.dll in 10.0.15063. |
| uiter_setUTF16BE | Introduced into icuuc.dll in 10.0.15063. |
| uiter_setUTF8 | Introduced into icuuc.dll in 10.0.15063. |
| uenum_close | Introduced into icuuc.dll in 10.0.15063. |
| uenum_count | Introduced into icuuc.dll in 10.0.15063. |
| uenum_unext | Introduced into icuuc.dll in 10.0.15063. |
| uenum_next | Introduced into icuuc.dll in 10.0.15063. |
| uenum_reset | Introduced into icuuc.dll in 10.0.15063. |
| uenum_openUCharStringsEnumeration | Introduced into icuuc.dll in 10.0.15063. |
| uenum_openCharStringsEnumeration | Introduced into icuuc.dll in 10.0.15063. |
| uloc_getDefault | Introduced into icuuc.dll in 10.0.15063. |
| uloc_setDefault | Introduced into icuuc.dll in 10.0.15063. |
| uloc_getLanguage | Introduced into icuuc.dll in 10.0.15063. |
| uloc_getScript | Introduced into icuuc.dll in 10.0.15063. |
| uloc_getCountry | Introduced into icuuc.dll in 10.0.15063. |
| uloc_getVariant | Introduced into icuuc.dll in 10.0.15063. |
| uloc_getName | Introduced into icuuc.dll in 10.0.15063. |
| uloc_canonicalize | Introduced into icuuc.dll in 10.0.15063. |
| uloc_getISO3Language | Introduced into icuuc.dll in 10.0.15063. |
| uloc_getISO3Country | Introduced into icuuc.dll in 10.0.15063. |
| uloc_getLCID | Introduced into icuuc.dll in 10.0.15063. |
| uloc_getDisplayLanguage | Introduced into icuuc.dll in 10.0.15063. |
| uloc_getDisplayScript | Introduced into icuuc.dll in 10.0.15063. |
| uloc_getDisplayCountry | Introduced into icuuc.dll in 10.0.15063. |
| uloc_getDisplayVariant | Introduced into icuuc.dll in 10.0.15063. |
| uloc_getDisplayKeyword | Introduced into icuuc.dll in 10.0.15063. |
| uloc_getDisplayKeywordValue | Introduced into icuuc.dll in 10.0.15063. |
| uloc_getDisplayName | Introduced into icuuc.dll in 10.0.15063. |
| uloc_getAvailable | Introduced into icuuc.dll in 10.0.15063. |
| uloc_countAvailable | Introduced into icuuc.dll in 10.0.15063. |
| uloc_getISOLanguages | Introduced into icuuc.dll in 10.0.15063. |
| uloc_getISOCountries | Introduced into icuuc.dll in 10.0.15063. |
| uloc_getParent | Introduced into icuuc.dll in 10.0.15063. |
| uloc_getBaseName | Introduced into icuuc.dll in 10.0.15063. |
| uloc_openKeywords | Introduced into icuuc.dll in 10.0.15063. |
| uloc_getKeywordValue | Introduced into icuuc.dll in 10.0.15063. |
| uloc_setKeywordValue | Introduced into icuuc.dll in 10.0.15063. |
| uloc_isRightToLeft | Introduced into icuuc.dll in 10.0.15063. |
| uloc_getCharacterOrientation | Introduced into icuuc.dll in 10.0.15063. |
| uloc_getLineOrientation | Introduced into icuuc.dll in 10.0.15063. |
| uloc_acceptLanguageFromHTTP | Introduced into icuuc.dll in 10.0.15063. |
| uloc_acceptLanguage | Introduced into icuuc.dll in 10.0.15063. |
| uloc_getLocaleForLCID | Introduced into icuuc.dll in 10.0.15063. |
| uloc_addLikelySubtags | Introduced into icuuc.dll in 10.0.15063. |
| uloc_minimizeSubtags | Introduced into icuuc.dll in 10.0.15063. |
| uloc_forLanguageTag | Introduced into icuuc.dll in 10.0.15063. |
| uloc_toLanguageTag | Introduced into icuuc.dll in 10.0.15063. |
| uloc_toUnicodeLocaleKey | Introduced into icuuc.dll in 10.0.15063. |
| uloc_toUnicodeLocaleType | Introduced into icuuc.dll in 10.0.15063. |
| uloc_toLegacyKey | Introduced into icuuc.dll in 10.0.15063. |
| uloc_toLegacyType | Introduced into icuuc.dll in 10.0.15063. |
| ures_open | Introduced into icuuc.dll in 10.0.15063. |
| ures_openDirect | Introduced into icuuc.dll in 10.0.15063. |
| ures_openU | Introduced into icuuc.dll in 10.0.15063. |
| ures_close | Introduced into icuuc.dll in 10.0.15063. |
| ures_getVersion | Introduced into icuuc.dll in 10.0.15063. |
| ures_getLocaleByType | Introduced into icuuc.dll in 10.0.15063. |
| ures_getString | Introduced into icuuc.dll in 10.0.15063. |
| ures_getUTF8String | Introduced into icuuc.dll in 10.0.15063. |
| ures_getBinary | Introduced into icuuc.dll in 10.0.15063. |
| ures_getIntVector | Introduced into icuuc.dll in 10.0.15063. |
| ures_getUInt | Introduced into icuuc.dll in 10.0.15063. |
| ures_getInt | Introduced into icuuc.dll in 10.0.15063. |
| ures_getSize | Introduced into icuuc.dll in 10.0.15063. |
| ures_getType | Introduced into icuuc.dll in 10.0.15063. |
| ures_getKey | Introduced into icuuc.dll in 10.0.15063. |
| ures_resetIterator | Introduced into icuuc.dll in 10.0.15063. |
| ures_hasNext | Introduced into icuuc.dll in 10.0.15063. |
| ures_getNextResource | Introduced into icuuc.dll in 10.0.15063. |
| ures_getNextString | Introduced into icuuc.dll in 10.0.15063. |
| ures_getByIndex | Introduced into icuuc.dll in 10.0.15063. |
| ures_getStringByIndex | Introduced into icuuc.dll in 10.0.15063. |
| ures_getUTF8StringByIndex | Introduced into icuuc.dll in 10.0.15063. |
| ures_getByKey | Introduced into icuuc.dll in 10.0.15063. |
| ures_getStringByKey | Introduced into icuuc.dll in 10.0.15063. |
| ures_getUTF8StringByKey | Introduced into icuuc.dll in 10.0.15063. |
| ures_openAvailableLocales | Introduced into icuuc.dll in 10.0.15063. |
| uldn_open | Introduced into icuuc.dll in 10.0.15063. |
| uldn_close | Introduced into icuuc.dll in 10.0.15063. |
| uldn_getLocale | Introduced into icuuc.dll in 10.0.15063. |
| uldn_getDialectHandling | Introduced into icuuc.dll in 10.0.15063. |
| uldn_localeDisplayName | Introduced into icuuc.dll in 10.0.15063. |
| uldn_languageDisplayName | Introduced into icuuc.dll in 10.0.15063. |
| uldn_scriptDisplayName | Introduced into icuuc.dll in 10.0.15063. |
| uldn_scriptCodeDisplayName | Introduced into icuuc.dll in 10.0.15063. |
| uldn_regionDisplayName | Introduced into icuuc.dll in 10.0.15063. |
| uldn_variantDisplayName | Introduced into icuuc.dll in 10.0.15063. |
| uldn_keyDisplayName | Introduced into icuuc.dll in 10.0.15063. |
| uldn_keyValueDisplayName | Introduced into icuuc.dll in 10.0.15063. |
| uldn_openForContext | Introduced into icuuc.dll in 10.0.15063. |
| uldn_getContext | Introduced into icuuc.dll in 10.0.15063. |
| ucurr_forLocale | Introduced into icuuc.dll in 10.0.15063. |
| ucurr_register | Introduced into icuuc.dll in 10.0.15063. |
| ucurr_unregister | Introduced into icuuc.dll in 10.0.15063. |
| ucurr_getName | Introduced into icuuc.dll in 10.0.15063. |
| ucurr_getPluralName | Introduced into icuuc.dll in 10.0.15063. |
| ucurr_getDefaultFractionDigits | Introduced into icuuc.dll in 10.0.15063. |
| ucurr_getDefaultFractionDigitsForUsage | Introduced into icuuc.dll in 10.0.15063. |
| ucurr_getRoundingIncrement | Introduced into icuuc.dll in 10.0.15063. |
| ucurr_getRoundingIncrementForUsage | Introduced into icuuc.dll in 10.0.15063. |
| ucurr_openISOCurrencies | Introduced into icuuc.dll in 10.0.15063. |
| ucurr_isAvailable | Introduced into icuuc.dll in 10.0.15063. |
| ucurr_countCurrencies | Introduced into icuuc.dll in 10.0.15063. |
| ucurr_forLocaleAndDate | Introduced into icuuc.dll in 10.0.15063. |
| ucurr_getKeywordValuesForLocale | Introduced into icuuc.dll in 10.0.15063. |
| ucurr_getNumericCode | Introduced into icuuc.dll in 10.0.15063. |
| UCNV_FROM_U_CALLBACK_STOP | Introduced into icuuc.dll in 10.0.15063. |
| UCNV_TO_U_CALLBACK_STOP | Introduced into icuuc.dll in 10.0.15063. |
| UCNV_FROM_U_CALLBACK_SKIP | Introduced into icuuc.dll in 10.0.15063. |
| UCNV_FROM_U_CALLBACK_SUBSTITUTE | Introduced into icuuc.dll in 10.0.15063. |
| UCNV_FROM_U_CALLBACK_ESCAPE | Introduced into icuuc.dll in 10.0.15063. |
| UCNV_TO_U_CALLBACK_SKIP | Introduced into icuuc.dll in 10.0.15063. |
| UCNV_TO_U_CALLBACK_SUBSTITUTE | Introduced into icuuc.dll in 10.0.15063. |
| UCNV_TO_U_CALLBACK_ESCAPE | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_compareNames | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_open | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_openU | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_openCCSID | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_openPackage | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_safeClone | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_close | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_getSubstChars | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_setSubstChars | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_setSubstString | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_getInvalidChars | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_getInvalidUChars | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_reset | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_resetToUnicode | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_resetFromUnicode | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_getMaxCharSize | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_getMinCharSize | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_getDisplayName | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_getName | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_getCCSID | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_getPlatform | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_getType | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_getStarters | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_getUnicodeSet | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_getToUCallBack | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_getFromUCallBack | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_setToUCallBack | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_setFromUCallBack | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_fromUnicode | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_toUnicode | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_fromUChars | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_toUChars | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_getNextUChar | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_convertEx | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_convert | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_toAlgorithmic | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_fromAlgorithmic | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_flushCache | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_countAvailable | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_getAvailableName | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_openAllNames | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_countAliases | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_getAlias | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_getAliases | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_openStandardNames | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_countStandards | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_getStandard | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_getStandardName | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_getCanonicalName | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_getDefaultName | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_setDefaultName | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_fixFileSeparator | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_isAmbiguous | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_setFallback | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_usesFallback | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_detectUnicodeSignature | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_fromUCountPending | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_toUCountPending | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_isFixedWidth | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_cbFromUWriteBytes | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_cbFromUWriteSub | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_cbFromUWriteUChars | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_cbToUWriteUChars | Introduced into icuuc.dll in 10.0.15063. |
| ucnv_cbToUWriteSub | Introduced into icuuc.dll in 10.0.15063. |
| u_init | Introduced into icuuc.dll in 10.0.15063. |
| u_cleanup | Introduced into icuuc.dll in 10.0.15063. |
| u_setMemoryFunctions | Introduced into icuuc.dll in 10.0.15063. |
| u_hasBinaryProperty | Introduced into icuuc.dll in 10.0.15063. |
| u_isUAlphabetic | Introduced into icuuc.dll in 10.0.15063. |
| u_isULowercase | Introduced into icuuc.dll in 10.0.15063. |
| u_isUUppercase | Introduced into icuuc.dll in 10.0.15063. |
| u_isUWhiteSpace | Introduced into icuuc.dll in 10.0.15063. |
| u_getIntPropertyValue | Introduced into icuuc.dll in 10.0.15063. |
| u_getIntPropertyMinValue | Introduced into icuuc.dll in 10.0.15063. |
| u_getIntPropertyMaxValue | Introduced into icuuc.dll in 10.0.15063. |
| u_getNumericValue | Introduced into icuuc.dll in 10.0.15063. |
| u_islower | Introduced into icuuc.dll in 10.0.15063. |
| u_isupper | Introduced into icuuc.dll in 10.0.15063. |
| u_istitle | Introduced into icuuc.dll in 10.0.15063. |
| u_isdigit | Introduced into icuuc.dll in 10.0.15063. |
| u_isalpha | Introduced into icuuc.dll in 10.0.15063. |
| u_isalnum | Introduced into icuuc.dll in 10.0.15063. |
| u_isxdigit | Introduced into icuuc.dll in 10.0.15063. |
| u_ispunct | Introduced into icuuc.dll in 10.0.15063. |
| u_isgraph | Introduced into icuuc.dll in 10.0.15063. |
| u_isblank | Introduced into icuuc.dll in 10.0.15063. |
| u_isdefined | Introduced into icuuc.dll in 10.0.15063. |
| u_isspace | Introduced into icuuc.dll in 10.0.15063. |
| u_isJavaSpaceChar | Introduced into icuuc.dll in 10.0.15063. |
| u_isWhitespace | Introduced into icuuc.dll in 10.0.15063. |
| u_iscntrl | Introduced into icuuc.dll in 10.0.15063. |
| u_isISOControl | Introduced into icuuc.dll in 10.0.15063. |
| u_isprint | Introduced into icuuc.dll in 10.0.15063. |
| u_isbase | Introduced into icuuc.dll in 10.0.15063. |
| u_charDirection | Introduced into icuuc.dll in 10.0.15063. |
| u_isMirrored | Introduced into icuuc.dll in 10.0.15063. |
| u_charMirror | Introduced into icuuc.dll in 10.0.15063. |
| u_getBidiPairedBracket | Introduced into icuuc.dll in 10.0.15063. |
| u_charType | Introduced into icuuc.dll in 10.0.15063. |
| u_enumCharTypes | Introduced into icuuc.dll in 10.0.15063. |
| u_getCombiningClass | Introduced into icuuc.dll in 10.0.15063. |
| u_charDigitValue | Introduced into icuuc.dll in 10.0.15063. |
| ublock_getCode | Introduced into icuuc.dll in 10.0.15063. |
| u_charName | Introduced into icuuc.dll in 10.0.15063. |
| u_charFromName | Introduced into icuuc.dll in 10.0.15063. |
| u_enumCharNames | Introduced into icuuc.dll in 10.0.15063. |
| u_getPropertyName | Introduced into icuuc.dll in 10.0.15063. |
| u_getPropertyEnum | Introduced into icuuc.dll in 10.0.15063. |
| u_getPropertyValueName | Introduced into icuuc.dll in 10.0.15063. |
| u_getPropertyValueEnum | Introduced into icuuc.dll in 10.0.15063. |
| u_isIDStart | Introduced into icuuc.dll in 10.0.15063. |
| u_isIDPart | Introduced into icuuc.dll in 10.0.15063. |
| u_isIDIgnorable | Introduced into icuuc.dll in 10.0.15063. |
| u_isJavaIDStart | Introduced into icuuc.dll in 10.0.15063. |
| u_isJavaIDPart | Introduced into icuuc.dll in 10.0.15063. |
| u_tolower | Introduced into icuuc.dll in 10.0.15063. |
| u_toupper | Introduced into icuuc.dll in 10.0.15063. |
| u_totitle | Introduced into icuuc.dll in 10.0.15063. |
| u_foldCase | Introduced into icuuc.dll in 10.0.15063. |
| u_digit | Introduced into icuuc.dll in 10.0.15063. |
| u_forDigit | Introduced into icuuc.dll in 10.0.15063. |
| u_charAge | Introduced into icuuc.dll in 10.0.15063. |
| u_getUnicodeVersion | Introduced into icuuc.dll in 10.0.15063. |
| u_getFC_NFKC_Closure | Introduced into icuuc.dll in 10.0.15063. |
| utext_close | Introduced into icuuc.dll in 10.0.15063. |
| utext_openUTF8 | Introduced into icuuc.dll in 10.0.15063. |
| utext_openUChars | Introduced into icuuc.dll in 10.0.15063. |
| utext_clone | Introduced into icuuc.dll in 10.0.15063. |
| utext_equals | Introduced into icuuc.dll in 10.0.15063. |
| utext_nativeLength | Introduced into icuuc.dll in 10.0.15063. |
| utext_isLengthExpensive | Introduced into icuuc.dll in 10.0.15063. |
| utext_char32At | Introduced into icuuc.dll in 10.0.15063. |
| utext_current32 | Introduced into icuuc.dll in 10.0.15063. |
| utext_next32 | Introduced into icuuc.dll in 10.0.15063. |
| utext_previous32 | Introduced into icuuc.dll in 10.0.15063. |
| utext_next32From | Introduced into icuuc.dll in 10.0.15063. |
| utext_previous32From | Introduced into icuuc.dll in 10.0.15063. |
| utext_getNativeIndex | Introduced into icuuc.dll in 10.0.15063. |
| utext_setNativeIndex | Introduced into icuuc.dll in 10.0.15063. |
| utext_moveIndex32 | Introduced into icuuc.dll in 10.0.15063. |
| utext_getPreviousNativeIndex | Introduced into icuuc.dll in 10.0.15063. |
| utext_extract | Introduced into icuuc.dll in 10.0.15063. |
| utext_isWritable | Introduced into icuuc.dll in 10.0.15063. |
| utext_hasMetaData | Introduced into icuuc.dll in 10.0.15063. |
| utext_replace | Introduced into icuuc.dll in 10.0.15063. |
| utext_copy | Introduced into icuuc.dll in 10.0.15063. |
| utext_freeze | Introduced into icuuc.dll in 10.0.15063. |
| utext_setup | Introduced into icuuc.dll in 10.0.15063. |
| uset_openEmpty | Introduced into icuuc.dll in 10.0.15063. |
| uset_open | Introduced into icuuc.dll in 10.0.15063. |
| uset_openPattern | Introduced into icuuc.dll in 10.0.15063. |
| uset_openPatternOptions | Introduced into icuuc.dll in 10.0.15063. |
| uset_close | Introduced into icuuc.dll in 10.0.15063. |
| uset_clone | Introduced into icuuc.dll in 10.0.15063. |
| uset_isFrozen | Introduced into icuuc.dll in 10.0.15063. |
| uset_freeze | Introduced into icuuc.dll in 10.0.15063. |
| uset_cloneAsThawed | Introduced into icuuc.dll in 10.0.15063. |
| uset_set | Introduced into icuuc.dll in 10.0.15063. |
| uset_applyPattern | Introduced into icuuc.dll in 10.0.15063. |
| uset_applyIntPropertyValue | Introduced into icuuc.dll in 10.0.15063. |
| uset_applyPropertyAlias | Introduced into icuuc.dll in 10.0.15063. |
| uset_resemblesPattern | Introduced into icuuc.dll in 10.0.15063. |
| uset_toPattern | Introduced into icuuc.dll in 10.0.15063. |
| uset_add | Introduced into icuuc.dll in 10.0.15063. |
| uset_addAll | Introduced into icuuc.dll in 10.0.15063. |
| uset_addRange | Introduced into icuuc.dll in 10.0.15063. |
| uset_addString | Introduced into icuuc.dll in 10.0.15063. |
| uset_addAllCodePoints | Introduced into icuuc.dll in 10.0.15063. |
| uset_remove | Introduced into icuuc.dll in 10.0.15063. |
| uset_removeRange | Introduced into icuuc.dll in 10.0.15063. |
| uset_removeString | Introduced into icuuc.dll in 10.0.15063. |
| uset_removeAll | Introduced into icuuc.dll in 10.0.15063. |
| uset_retain | Introduced into icuuc.dll in 10.0.15063. |
| uset_retainAll | Introduced into icuuc.dll in 10.0.15063. |
| uset_compact | Introduced into icuuc.dll in 10.0.15063. |
| uset_complement | Introduced into icuuc.dll in 10.0.15063. |
| uset_complementAll | Introduced into icuuc.dll in 10.0.15063. |
| uset_clear | Introduced into icuuc.dll in 10.0.15063. |
| uset_closeOver | Introduced into icuuc.dll in 10.0.15063. |
| uset_removeAllStrings | Introduced into icuuc.dll in 10.0.15063. |
| uset_isEmpty | Introduced into icuuc.dll in 10.0.15063. |
| uset_contains | Introduced into icuuc.dll in 10.0.15063. |
| uset_containsRange | Introduced into icuuc.dll in 10.0.15063. |
| uset_containsString | Introduced into icuuc.dll in 10.0.15063. |
| uset_indexOf | Introduced into icuuc.dll in 10.0.15063. |
| uset_charAt | Introduced into icuuc.dll in 10.0.15063. |
| uset_size | Introduced into icuuc.dll in 10.0.15063. |
| uset_getItemCount | Introduced into icuuc.dll in 10.0.15063. |
| uset_getItem | Introduced into icuuc.dll in 10.0.15063. |
| uset_containsAll | Introduced into icuuc.dll in 10.0.15063. |
| uset_containsAllCodePoints | Introduced into icuuc.dll in 10.0.15063. |
| uset_containsNone | Introduced into icuuc.dll in 10.0.15063. |
| uset_containsSome | Introduced into icuuc.dll in 10.0.15063. |
| uset_span | Introduced into icuuc.dll in 10.0.15063. |
| uset_spanBack | Introduced into icuuc.dll in 10.0.15063. |
| uset_spanUTF8 | Introduced into icuuc.dll in 10.0.15063. |
| uset_spanBackUTF8 | Introduced into icuuc.dll in 10.0.15063. |
| uset_equals | Introduced into icuuc.dll in 10.0.15063. |
| uset_serialize | Introduced into icuuc.dll in 10.0.15063. |
| uset_getSerializedSet | Introduced into icuuc.dll in 10.0.15063. |
| uset_setSerializedToOne | Introduced into icuuc.dll in 10.0.15063. |
| uset_serializedContains | Introduced into icuuc.dll in 10.0.15063. |
| uset_getSerializedRangeCount | Introduced into icuuc.dll in 10.0.15063. |
| uset_getSerializedRange | Introduced into icuuc.dll in 10.0.15063. |
| unorm2_getNFCInstance | Introduced into icuuc.dll in 10.0.15063. |
| unorm2_getNFDInstance | Introduced into icuuc.dll in 10.0.15063. |
| unorm2_getNFKCInstance | Introduced into icuuc.dll in 10.0.15063. |
| unorm2_getNFKDInstance | Introduced into icuuc.dll in 10.0.15063. |
| unorm2_getNFKCCasefoldInstance | Introduced into icuuc.dll in 10.0.15063. |
| unorm2_getInstance | Introduced into icuuc.dll in 10.0.15063. |
| unorm2_openFiltered | Introduced into icuuc.dll in 10.0.15063. |
| unorm2_close | Introduced into icuuc.dll in 10.0.15063. |
| unorm2_normalize | Introduced into icuuc.dll in 10.0.15063. |
| unorm2_normalizeSecondAndAppend | Introduced into icuuc.dll in 10.0.15063. |
| unorm2_append | Introduced into icuuc.dll in 10.0.15063. |
| unorm2_getDecomposition | Introduced into icuuc.dll in 10.0.15063. |
| unorm2_getRawDecomposition | Introduced into icuuc.dll in 10.0.15063. |
| unorm2_composePair | Introduced into icuuc.dll in 10.0.15063. |
| unorm2_getCombiningClass | Introduced into icuuc.dll in 10.0.15063. |
| unorm2_isNormalized | Introduced into icuuc.dll in 10.0.15063. |
| unorm2_quickCheck | Introduced into icuuc.dll in 10.0.15063. |
| unorm2_spanQuickCheckYes | Introduced into icuuc.dll in 10.0.15063. |
| unorm2_hasBoundaryBefore | Introduced into icuuc.dll in 10.0.15063. |
| unorm2_hasBoundaryAfter | Introduced into icuuc.dll in 10.0.15063. |
| unorm2_isInert | Introduced into icuuc.dll in 10.0.15063. |
| unorm_compare | Introduced into icuuc.dll in 10.0.15063. |
| ucnvsel_open | Introduced into icuuc.dll in 10.0.15063. |
| ucnvsel_close | Introduced into icuuc.dll in 10.0.15063. |
| ucnvsel_openFromSerialized | Introduced into icuuc.dll in 10.0.15063. |
| ucnvsel_serialize | Introduced into icuuc.dll in 10.0.15063. |
| ucnvsel_selectForString | Introduced into icuuc.dll in 10.0.15063. |
| ucnvsel_selectForUTF8 | Introduced into icuuc.dll in 10.0.15063. |
| u_catopen | Introduced into icuuc.dll in 10.0.15063. |
| u_catclose | Introduced into icuuc.dll in 10.0.15063. |
| u_catgets | Introduced into icuuc.dll in 10.0.15063. |
| ubidi_open | Introduced into icuuc.dll in 10.0.15063. |
| ubidi_openSized | Introduced into icuuc.dll in 10.0.15063. |
| ubidi_close | Introduced into icuuc.dll in 10.0.15063. |
| ubidi_setInverse | Introduced into icuuc.dll in 10.0.15063. |
| ubidi_isInverse | Introduced into icuuc.dll in 10.0.15063. |
| ubidi_orderParagraphsLTR | Introduced into icuuc.dll in 10.0.15063. |
| ubidi_isOrderParagraphsLTR | Introduced into icuuc.dll in 10.0.15063. |
| ubidi_setReorderingMode | Introduced into icuuc.dll in 10.0.15063. |
| ubidi_getReorderingMode | Introduced into icuuc.dll in 10.0.15063. |
| ubidi_setReorderingOptions | Introduced into icuuc.dll in 10.0.15063. |
| ubidi_getReorderingOptions | Introduced into icuuc.dll in 10.0.15063. |
| ubidi_setContext | Introduced into icuuc.dll in 10.0.15063. |
| ubidi_setPara | Introduced into icuuc.dll in 10.0.15063. |
| ubidi_setLine | Introduced into icuuc.dll in 10.0.15063. |
| ubidi_getDirection | Introduced into icuuc.dll in 10.0.15063. |
| ubidi_getBaseDirection | Introduced into icuuc.dll in 10.0.15063. |
| ubidi_getText | Introduced into icuuc.dll in 10.0.15063. |
| ubidi_getLength | Introduced into icuuc.dll in 10.0.15063. |
| ubidi_getParaLevel | Introduced into icuuc.dll in 10.0.15063. |
| ubidi_countParagraphs | Introduced into icuuc.dll in 10.0.15063. |
| ubidi_getParagraph | Introduced into icuuc.dll in 10.0.15063. |
| ubidi_getParagraphByIndex | Introduced into icuuc.dll in 10.0.15063. |
| ubidi_getLevelAt | Introduced into icuuc.dll in 10.0.15063. |
| ubidi_getLevels | Introduced into icuuc.dll in 10.0.15063. |
| ubidi_getLogicalRun | Introduced into icuuc.dll in 10.0.15063. |
| ubidi_countRuns | Introduced into icuuc.dll in 10.0.15063. |
| ubidi_getVisualRun | Introduced into icuuc.dll in 10.0.15063. |
| ubidi_getVisualIndex | Introduced into icuuc.dll in 10.0.15063. |
| ubidi_getLogicalIndex | Introduced into icuuc.dll in 10.0.15063. |
| ubidi_getLogicalMap | Introduced into icuuc.dll in 10.0.15063. |
| ubidi_getVisualMap | Introduced into icuuc.dll in 10.0.15063. |
| ubidi_reorderLogical | Introduced into icuuc.dll in 10.0.15063. |
| ubidi_reorderVisual | Introduced into icuuc.dll in 10.0.15063. |
| ubidi_invertMap | Introduced into icuuc.dll in 10.0.15063. |
| ubidi_getProcessedLength | Introduced into icuuc.dll in 10.0.15063. |
| ubidi_getResultLength | Introduced into icuuc.dll in 10.0.15063. |
| ubidi_getCustomizedClass | Introduced into icuuc.dll in 10.0.15063. |
| ubidi_setClassCallback | Introduced into icuuc.dll in 10.0.15063. |
| ubidi_getClassCallback | Introduced into icuuc.dll in 10.0.15063. |
| ubidi_writeReordered | Introduced into icuuc.dll in 10.0.15063. |
| ubidi_writeReverse | Introduced into icuuc.dll in 10.0.15063. |
| u_charsToUChars | Introduced into icuuc.dll in 10.0.15063. |
| u_UCharsToChars | Introduced into icuuc.dll in 10.0.15063. |
| u_strlen | Introduced into icuuc.dll in 10.0.15063. |
| u_countChar32 | Introduced into icuuc.dll in 10.0.15063. |
| u_strHasMoreChar32Than | Introduced into icuuc.dll in 10.0.15063. |
| u_strcat | Introduced into icuuc.dll in 10.0.15063. |
| u_strncat | Introduced into icuuc.dll in 10.0.15063. |
| u_strstr | Introduced into icuuc.dll in 10.0.15063. |
| u_strFindFirst | Introduced into icuuc.dll in 10.0.15063. |
| u_strchr | Introduced into icuuc.dll in 10.0.15063. |
| u_strchr32 | Introduced into icuuc.dll in 10.0.15063. |
| u_strrstr | Introduced into icuuc.dll in 10.0.15063. |
| u_strFindLast | Introduced into icuuc.dll in 10.0.15063. |
| u_strrchr | Introduced into icuuc.dll in 10.0.15063. |
| u_strrchr32 | Introduced into icuuc.dll in 10.0.15063. |
| u_strpbrk | Introduced into icuuc.dll in 10.0.15063. |
| u_strcspn | Introduced into icuuc.dll in 10.0.15063. |
| u_strspn | Introduced into icuuc.dll in 10.0.15063. |
| u_strtok_r | Introduced into icuuc.dll in 10.0.15063. |
| u_strcmp | Introduced into icuuc.dll in 10.0.15063. |
| u_strcmpCodePointOrder | Introduced into icuuc.dll in 10.0.15063. |
| u_strCompare | Introduced into icuuc.dll in 10.0.15063. |
| u_strCompareIter | Introduced into icuuc.dll in 10.0.15063. |
| u_strCaseCompare | Introduced into icuuc.dll in 10.0.15063. |
| u_strncmp | Introduced into icuuc.dll in 10.0.15063. |
| u_strncmpCodePointOrder | Introduced into icuuc.dll in 10.0.15063. |
| u_strcasecmp | Introduced into icuuc.dll in 10.0.15063. |
| u_strncasecmp | Introduced into icuuc.dll in 10.0.15063. |
| u_memcasecmp | Introduced into icuuc.dll in 10.0.15063. |
| u_strcpy | Introduced into icuuc.dll in 10.0.15063. |
| u_strncpy | Introduced into icuuc.dll in 10.0.15063. |
| u_uastrcpy | Introduced into icuuc.dll in 10.0.15063. |
| u_uastrncpy | Introduced into icuuc.dll in 10.0.15063. |
| u_austrcpy | Introduced into icuuc.dll in 10.0.15063. |
| u_austrncpy | Introduced into icuuc.dll in 10.0.15063. |
| u_memcpy | Introduced into icuuc.dll in 10.0.15063. |
| u_memmove | Introduced into icuuc.dll in 10.0.15063. |
| u_memset | Introduced into icuuc.dll in 10.0.15063. |
| u_memcmp | Introduced into icuuc.dll in 10.0.15063. |
| u_memcmpCodePointOrder | Introduced into icuuc.dll in 10.0.15063. |
| u_memchr | Introduced into icuuc.dll in 10.0.15063. |
| u_memchr32 | Introduced into icuuc.dll in 10.0.15063. |
| u_memrchr | Introduced into icuuc.dll in 10.0.15063. |
| u_memrchr32 | Introduced into icuuc.dll in 10.0.15063. |
| u_unescape | Introduced into icuuc.dll in 10.0.15063. |
| u_unescapeAt | Introduced into icuuc.dll in 10.0.15063. |
| u_strToUpper | Introduced into icuuc.dll in 10.0.15063. |
| u_strToLower | Introduced into icuuc.dll in 10.0.15063. |
| u_strToTitle | Introduced into icuuc.dll in 10.0.15063. |
| u_strFoldCase | Introduced into icuuc.dll in 10.0.15063. |
| u_strToWCS | Introduced into icuuc.dll in 10.0.15063. |
| u_strFromWCS | Introduced into icuuc.dll in 10.0.15063. |
| u_strToUTF8 | Introduced into icuuc.dll in 10.0.15063. |
| u_strFromUTF8 | Introduced into icuuc.dll in 10.0.15063. |
| u_strToUTF8WithSub | Introduced into icuuc.dll in 10.0.15063. |
| u_strFromUTF8WithSub | Introduced into icuuc.dll in 10.0.15063. |
| u_strFromUTF8Lenient | Introduced into icuuc.dll in 10.0.15063. |
| u_strToUTF32 | Introduced into icuuc.dll in 10.0.15063. |
| u_strFromUTF32 | Introduced into icuuc.dll in 10.0.15063. |
| u_strToUTF32WithSub | Introduced into icuuc.dll in 10.0.15063. |
| u_strFromUTF32WithSub | Introduced into icuuc.dll in 10.0.15063. |
| u_strToJavaModifiedUTF8 | Introduced into icuuc.dll in 10.0.15063. |
| u_strFromJavaModifiedUTF8WithSub | Introduced into icuuc.dll in 10.0.15063. |
| ucasemap_open | Introduced into icuuc.dll in 10.0.15063. |
| ucasemap_close | Introduced into icuuc.dll in 10.0.15063. |
| ucasemap_getLocale | Introduced into icuuc.dll in 10.0.15063. |
| ucasemap_getOptions | Introduced into icuuc.dll in 10.0.15063. |
| ucasemap_setLocale | Introduced into icuuc.dll in 10.0.15063. |
| ucasemap_setOptions | Introduced into icuuc.dll in 10.0.15063. |
| ucasemap_getBreakIterator | Introduced into icuuc.dll in 10.0.15063. |
| ucasemap_setBreakIterator | Introduced into icuuc.dll in 10.0.15063. |
| ucasemap_toTitle | Introduced into icuuc.dll in 10.0.15063. |
| ucasemap_utf8ToLower | Introduced into icuuc.dll in 10.0.15063. |
| ucasemap_utf8ToUpper | Introduced into icuuc.dll in 10.0.15063. |
| ucasemap_utf8ToTitle | Introduced into icuuc.dll in 10.0.15063. |
| ucasemap_utf8FoldCase | Introduced into icuuc.dll in 10.0.15063. |
| usprep_open | Introduced into icuuc.dll in 10.0.15063. |
| usprep_openByType | Introduced into icuuc.dll in 10.0.15063. |
| usprep_close | Introduced into icuuc.dll in 10.0.15063. |
| usprep_prepare | Introduced into icuuc.dll in 10.0.15063. |
| uidna_openUTS46 | Introduced into icuuc.dll in 10.0.15063. |
| uidna_close | Introduced into icuuc.dll in 10.0.15063. |
| uidna_labelToASCII | Introduced into icuuc.dll in 10.0.15063. |
| uidna_labelToUnicode | Introduced into icuuc.dll in 10.0.15063. |
| uidna_nameToASCII | Introduced into icuuc.dll in 10.0.15063. |
| uidna_nameToUnicode | Introduced into icuuc.dll in 10.0.15063. |
| uidna_labelToASCII_UTF8 | Introduced into icuuc.dll in 10.0.15063. |
| uidna_labelToUnicodeUTF8 | Introduced into icuuc.dll in 10.0.15063. |
| uidna_nameToASCII_UTF8 | Introduced into icuuc.dll in 10.0.15063. |
| uidna_nameToUnicodeUTF8 | Introduced into icuuc.dll in 10.0.15063. |
| ubrk_open | Introduced into icuuc.dll in 10.0.15063. |
| ubrk_openRules | Introduced into icuuc.dll in 10.0.15063. |
| ubrk_safeClone | Introduced into icuuc.dll in 10.0.15063. |
| ubrk_close | Introduced into icuuc.dll in 10.0.15063. |
| ubrk_setText | Introduced into icuuc.dll in 10.0.15063. |
| ubrk_setUText | Introduced into icuuc.dll in 10.0.15063. |
| ubrk_current | Introduced into icuuc.dll in 10.0.15063. |
| ubrk_next | Introduced into icuuc.dll in 10.0.15063. |
| ubrk_previous | Introduced into icuuc.dll in 10.0.15063. |
| ubrk_first | Introduced into icuuc.dll in 10.0.15063. |
| ubrk_last | Introduced into icuuc.dll in 10.0.15063. |
| ubrk_preceding | Introduced into icuuc.dll in 10.0.15063. |
| ubrk_following | Introduced into icuuc.dll in 10.0.15063. |
| ubrk_getAvailable | Introduced into icuuc.dll in 10.0.15063. |
| ubrk_countAvailable | Introduced into icuuc.dll in 10.0.15063. |
| ubrk_isBoundary | Introduced into icuuc.dll in 10.0.15063. |
| ubrk_getRuleStatus | Introduced into icuuc.dll in 10.0.15063. |
| ubrk_getRuleStatusVec | Introduced into icuuc.dll in 10.0.15063. |
| ubrk_getLocaleByType | Introduced into icuuc.dll in 10.0.15063. |
| ubrk_refreshUText | Introduced into icuuc.dll in 10.0.15063. |
| u_getDataVersion | Introduced into icuuc.dll in 10.0.15063. |


## APIs from icuin.dll

| API | Requirements |
| -----| --------------|
| ucal_openTimeZoneIDEnumeration | Introduced into icuin.dll in 10.0.15063. |
| ucal_openTimeZones | Introduced into icuin.dll in 10.0.15063. |
| ucal_openCountryTimeZones | Introduced into icuin.dll in 10.0.15063. |
| ucal_getDefaultTimeZone | Introduced into icuin.dll in 10.0.15063. |
| ucal_setDefaultTimeZone | Introduced into icuin.dll in 10.0.15063. |
| ucal_getDSTSavings | Introduced into icuin.dll in 10.0.15063. |
| ucal_getNow | Introduced into icuin.dll in 10.0.15063. |
| ucal_open | Introduced into icuin.dll in 10.0.15063. |
| ucal_close | Introduced into icuin.dll in 10.0.15063. |
| ucal_clone | Introduced into icuin.dll in 10.0.15063. |
| ucal_setTimeZone | Introduced into icuin.dll in 10.0.15063. |
| ucal_getTimeZoneID | Introduced into icuin.dll in 10.0.15063. |
| ucal_getTimeZoneDisplayName | Introduced into icuin.dll in 10.0.15063. |
| ucal_inDaylightTime | Introduced into icuin.dll in 10.0.15063. |
| ucal_setGregorianChange | Introduced into icuin.dll in 10.0.15063. |
| ucal_getGregorianChange | Introduced into icuin.dll in 10.0.15063. |
| ucal_getAttribute | Introduced into icuin.dll in 10.0.15063. |
| ucal_setAttribute | Introduced into icuin.dll in 10.0.15063. |
| ucal_getAvailable | Introduced into icuin.dll in 10.0.15063. |
| ucal_countAvailable | Introduced into icuin.dll in 10.0.15063. |
| ucal_getMillis | Introduced into icuin.dll in 10.0.15063. |
| ucal_setMillis | Introduced into icuin.dll in 10.0.15063. |
| ucal_setDate | Introduced into icuin.dll in 10.0.15063. |
| ucal_setDateTime | Introduced into icuin.dll in 10.0.15063. |
| ucal_equivalentTo | Introduced into icuin.dll in 10.0.15063. |
| ucal_add | Introduced into icuin.dll in 10.0.15063. |
| ucal_roll | Introduced into icuin.dll in 10.0.15063. |
| ucal_get | Introduced into icuin.dll in 10.0.15063. |
| ucal_set | Introduced into icuin.dll in 10.0.15063. |
| ucal_isSet | Introduced into icuin.dll in 10.0.15063. |
| ucal_clearField | Introduced into icuin.dll in 10.0.15063. |
| ucal_clear | Introduced into icuin.dll in 10.0.15063. |
| ucal_getLimit | Introduced into icuin.dll in 10.0.15063. |
| ucal_getLocaleByType | Introduced into icuin.dll in 10.0.15063. |
| ucal_getTZDataVersion | Introduced into icuin.dll in 10.0.15063. |
| ucal_getCanonicalTimeZoneID | Introduced into icuin.dll in 10.0.15063. |
| ucal_getType | Introduced into icuin.dll in 10.0.15063. |
| ucal_getKeywordValuesForLocale | Introduced into icuin.dll in 10.0.15063. |
| ucal_getDayOfWeekType | Introduced into icuin.dll in 10.0.15063. |
| ucal_getWeekendTransition | Introduced into icuin.dll in 10.0.15063. |
| ucal_isWeekend | Introduced into icuin.dll in 10.0.15063. |
| ucal_getFieldDifference | Introduced into icuin.dll in 10.0.15063. |
| ucal_getTimeZoneTransitionDate | Introduced into icuin.dll in 10.0.15063. |
| ucal_getWindowsTimeZoneID | Introduced into icuin.dll in 10.0.15063. |
| ucal_getTimeZoneIDForWindowsID | Introduced into icuin.dll in 10.0.15063. |
| ucol_open | Introduced into icuin.dll in 10.0.15063. |
| ucol_openRules | Introduced into icuin.dll in 10.0.15063. |
| ucol_getContractionsAndExpansions | Introduced into icuin.dll in 10.0.15063. |
| ucol_close | Introduced into icuin.dll in 10.0.15063. |
| ucol_strcoll | Introduced into icuin.dll in 10.0.15063. |
| ucol_strcollUTF8 | Introduced into icuin.dll in 10.0.15063. |
| ucol_greater | Introduced into icuin.dll in 10.0.15063. |
| ucol_greaterOrEqual | Introduced into icuin.dll in 10.0.15063. |
| ucol_equal | Introduced into icuin.dll in 10.0.15063. |
| ucol_strcollIter | Introduced into icuin.dll in 10.0.15063. |
| ucol_getStrength | Introduced into icuin.dll in 10.0.15063. |
| ucol_setStrength | Introduced into icuin.dll in 10.0.15063. |
| ucol_getReorderCodes | Introduced into icuin.dll in 10.0.15063. |
| ucol_setReorderCodes | Introduced into icuin.dll in 10.0.15063. |
| ucol_getEquivalentReorderCodes | Introduced into icuin.dll in 10.0.15063. |
| ucol_getDisplayName | Introduced into icuin.dll in 10.0.15063. |
| ucol_getAvailable | Introduced into icuin.dll in 10.0.15063. |
| ucol_countAvailable | Introduced into icuin.dll in 10.0.15063. |
| ucol_openAvailableLocales | Introduced into icuin.dll in 10.0.15063. |
| ucol_getKeywords | Introduced into icuin.dll in 10.0.15063. |
| ucol_getKeywordValues | Introduced into icuin.dll in 10.0.15063. |
| ucol_getKeywordValuesForLocale | Introduced into icuin.dll in 10.0.15063. |
| ucol_getFunctionalEquivalent | Introduced into icuin.dll in 10.0.15063. |
| ucol_getRules | Introduced into icuin.dll in 10.0.15063. |
| ucol_getSortKey | Introduced into icuin.dll in 10.0.15063. |
| ucol_nextSortKeyPart | Introduced into icuin.dll in 10.0.15063. |
| ucol_getBound | Introduced into icuin.dll in 10.0.15063. |
| ucol_getVersion | Introduced into icuin.dll in 10.0.15063. |
| ucol_getUCAVersion | Introduced into icuin.dll in 10.0.15063. |
| ucol_mergeSortkeys | Introduced into icuin.dll in 10.0.15063. |
| ucol_setAttribute | Introduced into icuin.dll in 10.0.15063. |
| ucol_getAttribute | Introduced into icuin.dll in 10.0.15063. |
| ucol_setMaxVariable | Introduced into icuin.dll in 10.0.15063. |
| ucol_getMaxVariable | Introduced into icuin.dll in 10.0.15063. |
| ucol_getVariableTop | Introduced into icuin.dll in 10.0.15063. |
| ucol_safeClone | Introduced into icuin.dll in 10.0.15063. |
| ucol_getRulesEx | Introduced into icuin.dll in 10.0.15063. |
| ucol_getLocaleByType | Introduced into icuin.dll in 10.0.15063. |
| ucol_getTailoredSet | Introduced into icuin.dll in 10.0.15063. |
| ucol_cloneBinary | Introduced into icuin.dll in 10.0.15063. |
| ucol_openBinary | Introduced into icuin.dll in 10.0.15063. |
| ucol_openElements | Introduced into icuin.dll in 10.0.15063. |
| ucol_keyHashCode | Introduced into icuin.dll in 10.0.15063. |
| ucol_closeElements | Introduced into icuin.dll in 10.0.15063. |
| ucol_reset | Introduced into icuin.dll in 10.0.15063. |
| ucol_next | Introduced into icuin.dll in 10.0.15063. |
| ucol_previous | Introduced into icuin.dll in 10.0.15063. |
| ucol_getMaxExpansion | Introduced into icuin.dll in 10.0.15063. |
| ucol_setText | Introduced into icuin.dll in 10.0.15063. |
| ucol_getOffset | Introduced into icuin.dll in 10.0.15063. |
| ucol_setOffset | Introduced into icuin.dll in 10.0.15063. |
| ucol_primaryOrder | Introduced into icuin.dll in 10.0.15063. |
| ucol_secondaryOrder | Introduced into icuin.dll in 10.0.15063. |
| ucol_tertiaryOrder | Introduced into icuin.dll in 10.0.15063. |
| ucsdet_open | Introduced into icuin.dll in 10.0.15063. |
| ucsdet_close | Introduced into icuin.dll in 10.0.15063. |
| ucsdet_setText | Introduced into icuin.dll in 10.0.15063. |
| ucsdet_setDeclaredEncoding | Introduced into icuin.dll in 10.0.15063. |
| ucsdet_detect | Introduced into icuin.dll in 10.0.15063. |
| ucsdet_detectAll | Introduced into icuin.dll in 10.0.15063. |
| ucsdet_getName | Introduced into icuin.dll in 10.0.15063. |
| ucsdet_getConfidence | Introduced into icuin.dll in 10.0.15063. |
| ucsdet_getLanguage | Introduced into icuin.dll in 10.0.15063. |
| ucsdet_getUChars | Introduced into icuin.dll in 10.0.15063. |
| ucsdet_getAllDetectableCharsets | Introduced into icuin.dll in 10.0.15063. |
| ucsdet_isInputFilterEnabled | Introduced into icuin.dll in 10.0.15063. |
| ucsdet_enableInputFilter | Introduced into icuin.dll in 10.0.15063. |
| udtitvfmt_open | Introduced into icuin.dll in 10.0.15063. |
| udtitvfmt_close | Introduced into icuin.dll in 10.0.15063. |
| udtitvfmt_format | Introduced into icuin.dll in 10.0.15063. |
| udatpg_open | Introduced into icuin.dll in 10.0.15063. |
| udatpg_openEmpty | Introduced into icuin.dll in 10.0.15063. |
| udatpg_close | Introduced into icuin.dll in 10.0.15063. |
| udatpg_clone | Introduced into icuin.dll in 10.0.15063. |
| udatpg_getBestPattern | Introduced into icuin.dll in 10.0.15063. |
| udatpg_getBestPatternWithOptions | Introduced into icuin.dll in 10.0.15063. |
| udatpg_getSkeleton | Introduced into icuin.dll in 10.0.15063. |
| udatpg_getBaseSkeleton | Introduced into icuin.dll in 10.0.15063. |
| udatpg_addPattern | Introduced into icuin.dll in 10.0.15063. |
| udatpg_setAppendItemFormat | Introduced into icuin.dll in 10.0.15063. |
| udatpg_getAppendItemFormat | Introduced into icuin.dll in 10.0.15063. |
| udatpg_setAppendItemName | Introduced into icuin.dll in 10.0.15063. |
| udatpg_getAppendItemName | Introduced into icuin.dll in 10.0.15063. |
| udatpg_setDateTimeFormat | Introduced into icuin.dll in 10.0.15063. |
| udatpg_getDateTimeFormat | Introduced into icuin.dll in 10.0.15063. |
| udatpg_setDecimal | Introduced into icuin.dll in 10.0.15063. |
| udatpg_getDecimal | Introduced into icuin.dll in 10.0.15063. |
| udatpg_replaceFieldTypes | Introduced into icuin.dll in 10.0.15063. |
| udatpg_replaceFieldTypesWithOptions | Introduced into icuin.dll in 10.0.15063. |
| udatpg_openSkeletons | Introduced into icuin.dll in 10.0.15063. |
| udatpg_openBaseSkeletons | Introduced into icuin.dll in 10.0.15063. |
| udatpg_getPatternForSkeleton | Introduced into icuin.dll in 10.0.15063. |
| ufieldpositer_open | Introduced into icuin.dll in 10.0.15063. |
| ufieldpositer_close | Introduced into icuin.dll in 10.0.15063. |
| ufieldpositer_next | Introduced into icuin.dll in 10.0.15063. |
| ufmt_open | Introduced into icuin.dll in 10.0.15063. |
| ufmt_close | Introduced into icuin.dll in 10.0.15063. |
| ufmt_getType | Introduced into icuin.dll in 10.0.15063. |
| ufmt_isNumeric | Introduced into icuin.dll in 10.0.15063. |
| ufmt_getDate | Introduced into icuin.dll in 10.0.15063. |
| ufmt_getDouble | Introduced into icuin.dll in 10.0.15063. |
| ufmt_getLong | Introduced into icuin.dll in 10.0.15063. |
| ufmt_getInt64 | Introduced into icuin.dll in 10.0.15063. |
| ufmt_getObject | Introduced into icuin.dll in 10.0.15063. |
| ufmt_getUChars | Introduced into icuin.dll in 10.0.15063. |
| ufmt_getArrayLength | Introduced into icuin.dll in 10.0.15063. |
| ufmt_getArrayItemByIndex | Introduced into icuin.dll in 10.0.15063. |
| ufmt_getDecNumChars | Introduced into icuin.dll in 10.0.15063. |
| ugender_getInstance | Introduced into icuin.dll in 10.0.15063. |
| ugender_getListGender | Introduced into icuin.dll in 10.0.15063. |
| ulocdata_open | Introduced into icuin.dll in 10.0.15063. |
| ulocdata_close | Introduced into icuin.dll in 10.0.15063. |
| ulocdata_setNoSubstitute | Introduced into icuin.dll in 10.0.15063. |
| ulocdata_getNoSubstitute | Introduced into icuin.dll in 10.0.15063. |
| ulocdata_getExemplarSet | Introduced into icuin.dll in 10.0.15063. |
| ulocdata_getDelimiter | Introduced into icuin.dll in 10.0.15063. |
| ulocdata_getMeasurementSystem | Introduced into icuin.dll in 10.0.15063. |
| ulocdata_getPaperSize | Introduced into icuin.dll in 10.0.15063. |
| ulocdata_getCLDRVersion | Introduced into icuin.dll in 10.0.15063. |
| ulocdata_getLocaleDisplayPattern | Introduced into icuin.dll in 10.0.15063. |
| ulocdata_getLocaleSeparator | Introduced into icuin.dll in 10.0.15063. |
| u_formatMessage | Introduced into icuin.dll in 10.0.15063. |
| u_vformatMessage | Introduced into icuin.dll in 10.0.15063. |
| u_parseMessage | Introduced into icuin.dll in 10.0.15063. |
| u_vparseMessage | Introduced into icuin.dll in 10.0.15063. |
| u_formatMessageWithError | Introduced into icuin.dll in 10.0.15063. |
| u_vformatMessageWithError | Introduced into icuin.dll in 10.0.15063. |
| u_parseMessageWithError | Introduced into icuin.dll in 10.0.15063. |
| u_vparseMessageWithError | Introduced into icuin.dll in 10.0.15063. |
| umsg_open | Introduced into icuin.dll in 10.0.15063. |
| umsg_close | Introduced into icuin.dll in 10.0.15063. |
| umsg_clone | Introduced into icuin.dll in 10.0.15063. |
| umsg_setLocale | Introduced into icuin.dll in 10.0.15063. |
| umsg_getLocale | Introduced into icuin.dll in 10.0.15063. |
| umsg_applyPattern | Introduced into icuin.dll in 10.0.15063. |
| umsg_toPattern | Introduced into icuin.dll in 10.0.15063. |
| umsg_format | Introduced into icuin.dll in 10.0.15063. |
| umsg_vformat | Introduced into icuin.dll in 10.0.15063. |
| umsg_parse | Introduced into icuin.dll in 10.0.15063. |
| umsg_vparse | Introduced into icuin.dll in 10.0.15063. |
| umsg_autoQuoteApostrophe | Introduced into icuin.dll in 10.0.15063. |
| unum_open | Introduced into icuin.dll in 10.0.15063. |
| unum_close | Introduced into icuin.dll in 10.0.15063. |
| unum_clone | Introduced into icuin.dll in 10.0.15063. |
| unum_format | Introduced into icuin.dll in 10.0.15063. |
| unum_formatInt64 | Introduced into icuin.dll in 10.0.15063. |
| unum_formatDouble | Introduced into icuin.dll in 10.0.15063. |
| unum_formatDecimal | Introduced into icuin.dll in 10.0.15063. |
| unum_formatDoubleCurrency | Introduced into icuin.dll in 10.0.15063. |
| unum_formatUFormattable | Introduced into icuin.dll in 10.0.15063. |
| unum_parse | Introduced into icuin.dll in 10.0.15063. |
| unum_parseInt64 | Introduced into icuin.dll in 10.0.15063. |
| unum_parseDouble | Introduced into icuin.dll in 10.0.15063. |
| unum_parseDecimal | Introduced into icuin.dll in 10.0.15063. |
| unum_parseDoubleCurrency | Introduced into icuin.dll in 10.0.15063. |
| unum_parseToUFormattable | Introduced into icuin.dll in 10.0.15063. |
| unum_applyPattern | Introduced into icuin.dll in 10.0.15063. |
| unum_getAvailable | Introduced into icuin.dll in 10.0.15063. |
| unum_countAvailable | Introduced into icuin.dll in 10.0.15063. |
| unum_getAttribute | Introduced into icuin.dll in 10.0.15063. |
| unum_setAttribute | Introduced into icuin.dll in 10.0.15063. |
| unum_getDoubleAttribute | Introduced into icuin.dll in 10.0.15063. |
| unum_setDoubleAttribute | Introduced into icuin.dll in 10.0.15063. |
| unum_getTextAttribute | Introduced into icuin.dll in 10.0.15063. |
| unum_setTextAttribute | Introduced into icuin.dll in 10.0.15063. |
| unum_toPattern | Introduced into icuin.dll in 10.0.15063. |
| unum_getSymbol | Introduced into icuin.dll in 10.0.15063. |
| unum_setSymbol | Introduced into icuin.dll in 10.0.15063. |
| unum_getLocaleByType | Introduced into icuin.dll in 10.0.15063. |
| unum_setContext | Introduced into icuin.dll in 10.0.15063. |
| unum_getContext | Introduced into icuin.dll in 10.0.15063. |
| udat_toCalendarDateField | Introduced into icuin.dll in 10.0.15063. |
| udat_open | Introduced into icuin.dll in 10.0.15063. |
| udat_close | Introduced into icuin.dll in 10.0.15063. |
| udat_getBooleanAttribute | Introduced into icuin.dll in 10.0.15063. |
| udat_setBooleanAttribute | Introduced into icuin.dll in 10.0.15063. |
| udat_clone | Introduced into icuin.dll in 10.0.15063. |
| udat_format | Introduced into icuin.dll in 10.0.15063. |
| udat_formatCalendar | Introduced into icuin.dll in 10.0.15063. |
| udat_formatForFields | Introduced into icuin.dll in 10.0.15063. |
| udat_formatCalendarForFields | Introduced into icuin.dll in 10.0.15063. |
| udat_parse | Introduced into icuin.dll in 10.0.15063. |
| udat_parseCalendar | Introduced into icuin.dll in 10.0.15063. |
| udat_isLenient | Introduced into icuin.dll in 10.0.15063. |
| udat_setLenient | Introduced into icuin.dll in 10.0.15063. |
| udat_getCalendar | Introduced into icuin.dll in 10.0.15063. |
| udat_setCalendar | Introduced into icuin.dll in 10.0.15063. |
| udat_getNumberFormat | Introduced into icuin.dll in 10.0.15063. |
| udat_getNumberFormatForField | Introduced into icuin.dll in 10.0.15063. |
| udat_adoptNumberFormatForFields | Introduced into icuin.dll in 10.0.15063. |
| udat_setNumberFormat | Introduced into icuin.dll in 10.0.15063. |
| udat_adoptNumberFormat | Introduced into icuin.dll in 10.0.15063. |
| udat_getAvailable | Introduced into icuin.dll in 10.0.15063. |
| udat_countAvailable | Introduced into icuin.dll in 10.0.15063. |
| udat_get2DigitYearStart | Introduced into icuin.dll in 10.0.15063. |
| udat_set2DigitYearStart | Introduced into icuin.dll in 10.0.15063. |
| udat_toPattern | Introduced into icuin.dll in 10.0.15063. |
| udat_applyPattern | Introduced into icuin.dll in 10.0.15063. |
| udat_getSymbols | Introduced into icuin.dll in 10.0.15063. |
| udat_countSymbols | Introduced into icuin.dll in 10.0.15063. |
| udat_setSymbols | Introduced into icuin.dll in 10.0.15063. |
| udat_getLocaleByType | Introduced into icuin.dll in 10.0.15063. |
| udat_setContext | Introduced into icuin.dll in 10.0.15063. |
| udat_getContext | Introduced into icuin.dll in 10.0.15063. |
| unumsys_open | Introduced into icuin.dll in 10.0.15063. |
| unumsys_openByName | Introduced into icuin.dll in 10.0.15063. |
| unumsys_close | Introduced into icuin.dll in 10.0.15063. |
| unumsys_openAvailableNames | Introduced into icuin.dll in 10.0.15063. |
| unumsys_getName | Introduced into icuin.dll in 10.0.15063. |
| unumsys_isAlgorithmic | Introduced into icuin.dll in 10.0.15063. |
| unumsys_getRadix | Introduced into icuin.dll in 10.0.15063. |
| unumsys_getDescription | Introduced into icuin.dll in 10.0.15063. |
| uplrules_open | Introduced into icuin.dll in 10.0.15063. |
| uplrules_openForType | Introduced into icuin.dll in 10.0.15063. |
| uplrules_close | Introduced into icuin.dll in 10.0.15063. |
| uplrules_select | Introduced into icuin.dll in 10.0.15063. |
| uregex_open | Introduced into icuin.dll in 10.0.15063. |
| uregex_openUText | Introduced into icuin.dll in 10.0.15063. |
| uregex_openC | Introduced into icuin.dll in 10.0.15063. |
| uregex_close | Introduced into icuin.dll in 10.0.15063. |
| uregex_clone | Introduced into icuin.dll in 10.0.15063. |
| uregex_pattern | Introduced into icuin.dll in 10.0.15063. |
| uregex_patternUText | Introduced into icuin.dll in 10.0.15063. |
| uregex_flags | Introduced into icuin.dll in 10.0.15063. |
| uregex_setText | Introduced into icuin.dll in 10.0.15063. |
| uregex_setUText | Introduced into icuin.dll in 10.0.15063. |
| uregex_getText | Introduced into icuin.dll in 10.0.15063. |
| uregex_getUText | Introduced into icuin.dll in 10.0.15063. |
| uregex_refreshUText | Introduced into icuin.dll in 10.0.15063. |
| uregex_matches | Introduced into icuin.dll in 10.0.15063. |
| uregex_matches64 | Introduced into icuin.dll in 10.0.15063. |
| uregex_lookingAt | Introduced into icuin.dll in 10.0.15063. |
| uregex_lookingAt64 | Introduced into icuin.dll in 10.0.15063. |
| uregex_find | Introduced into icuin.dll in 10.0.15063. |
| uregex_find64 | Introduced into icuin.dll in 10.0.15063. |
| uregex_findNext | Introduced into icuin.dll in 10.0.15063. |
| uregex_groupCount | Introduced into icuin.dll in 10.0.15063. |
| uregex_groupNumberFromName | Introduced into icuin.dll in 10.0.15063. |
| uregex_groupNumberFromCName | Introduced into icuin.dll in 10.0.15063. |
| uregex_group | Introduced into icuin.dll in 10.0.15063. |
| uregex_groupUText | Introduced into icuin.dll in 10.0.15063. |
| uregex_start | Introduced into icuin.dll in 10.0.15063. |
| uregex_start64 | Introduced into icuin.dll in 10.0.15063. |
| uregex_end | Introduced into icuin.dll in 10.0.15063. |
| uregex_end64 | Introduced into icuin.dll in 10.0.15063. |
| uregex_reset | Introduced into icuin.dll in 10.0.15063. |
| uregex_reset64 | Introduced into icuin.dll in 10.0.15063. |
| uregex_setRegion | Introduced into icuin.dll in 10.0.15063. |
| uregex_setRegion64 | Introduced into icuin.dll in 10.0.15063. |
| uregex_setRegionAndStart | Introduced into icuin.dll in 10.0.15063. |
| uregex_regionStart | Introduced into icuin.dll in 10.0.15063. |
| uregex_regionStart64 | Introduced into icuin.dll in 10.0.15063. |
| uregex_regionEnd | Introduced into icuin.dll in 10.0.15063. |
| uregex_regionEnd64 | Introduced into icuin.dll in 10.0.15063. |
| uregex_hasTransparentBounds | Introduced into icuin.dll in 10.0.15063. |
| uregex_useTransparentBounds | Introduced into icuin.dll in 10.0.15063. |
| uregex_hasAnchoringBounds | Introduced into icuin.dll in 10.0.15063. |
| uregex_useAnchoringBounds | Introduced into icuin.dll in 10.0.15063. |
| uregex_hitEnd | Introduced into icuin.dll in 10.0.15063. |
| uregex_requireEnd | Introduced into icuin.dll in 10.0.15063. |
| uregex_replaceAll | Introduced into icuin.dll in 10.0.15063. |
| uregex_replaceAllUText | Introduced into icuin.dll in 10.0.15063. |
| uregex_replaceFirst | Introduced into icuin.dll in 10.0.15063. |
| uregex_replaceFirstUText | Introduced into icuin.dll in 10.0.15063. |
| uregex_appendReplacement | Introduced into icuin.dll in 10.0.15063. |
| uregex_appendReplacementUText | Introduced into icuin.dll in 10.0.15063. |
| uregex_appendTail | Introduced into icuin.dll in 10.0.15063. |
| uregex_appendTailUText | Introduced into icuin.dll in 10.0.15063. |
| uregex_split | Introduced into icuin.dll in 10.0.15063. |
| uregex_splitUText | Introduced into icuin.dll in 10.0.15063. |
| uregex_setTimeLimit | Introduced into icuin.dll in 10.0.15063. |
| uregex_getTimeLimit | Introduced into icuin.dll in 10.0.15063. |
| uregex_setStackLimit | Introduced into icuin.dll in 10.0.15063. |
| uregex_getStackLimit | Introduced into icuin.dll in 10.0.15063. |
| uregex_setMatchCallback | Introduced into icuin.dll in 10.0.15063. |
| uregex_getMatchCallback | Introduced into icuin.dll in 10.0.15063. |
| uregex_setFindProgressCallback | Introduced into icuin.dll in 10.0.15063. |
| uregex_getFindProgressCallback | Introduced into icuin.dll in 10.0.15063. |
| uregion_getRegionFromCode | Introduced into icuin.dll in 10.0.15063. |
| uregion_getRegionFromNumericCode | Introduced into icuin.dll in 10.0.15063. |
| uregion_getAvailable | Introduced into icuin.dll in 10.0.15063. |
| uregion_areEqual | Introduced into icuin.dll in 10.0.15063. |
| uregion_getContainingRegion | Introduced into icuin.dll in 10.0.15063. |
| uregion_getContainingRegionOfType | Introduced into icuin.dll in 10.0.15063. |
| uregion_getContainedRegions | Introduced into icuin.dll in 10.0.15063. |
| uregion_getContainedRegionsOfType | Introduced into icuin.dll in 10.0.15063. |
| uregion_contains | Introduced into icuin.dll in 10.0.15063. |
| uregion_getPreferredValues | Introduced into icuin.dll in 10.0.15063. |
| uregion_getRegionCode | Introduced into icuin.dll in 10.0.15063. |
| uregion_getNumericCode | Introduced into icuin.dll in 10.0.15063. |
| uregion_getType | Introduced into icuin.dll in 10.0.15063. |
| usearch_open | Introduced into icuin.dll in 10.0.15063. |
| usearch_openFromCollator | Introduced into icuin.dll in 10.0.15063. |
| usearch_close | Introduced into icuin.dll in 10.0.15063. |
| usearch_setOffset | Introduced into icuin.dll in 10.0.15063. |
| usearch_getOffset | Introduced into icuin.dll in 10.0.15063. |
| usearch_setAttribute | Introduced into icuin.dll in 10.0.15063. |
| usearch_getAttribute | Introduced into icuin.dll in 10.0.15063. |
| usearch_getMatchedStart | Introduced into icuin.dll in 10.0.15063. |
| usearch_getMatchedLength | Introduced into icuin.dll in 10.0.15063. |
| usearch_getMatchedText | Introduced into icuin.dll in 10.0.15063. |
| usearch_setBreakIterator | Introduced into icuin.dll in 10.0.15063. |
| usearch_getBreakIterator | Introduced into icuin.dll in 10.0.15063. |
| usearch_setText | Introduced into icuin.dll in 10.0.15063. |
| usearch_getText | Introduced into icuin.dll in 10.0.15063. |
| usearch_getCollator | Introduced into icuin.dll in 10.0.15063. |
| usearch_setCollator | Introduced into icuin.dll in 10.0.15063. |
| usearch_setPattern | Introduced into icuin.dll in 10.0.15063. |
| usearch_getPattern | Introduced into icuin.dll in 10.0.15063. |
| usearch_first | Introduced into icuin.dll in 10.0.15063. |
| usearch_following | Introduced into icuin.dll in 10.0.15063. |
| usearch_last | Introduced into icuin.dll in 10.0.15063. |
| usearch_preceding | Introduced into icuin.dll in 10.0.15063. |
| usearch_next | Introduced into icuin.dll in 10.0.15063. |
| usearch_previous | Introduced into icuin.dll in 10.0.15063. |
| usearch_reset | Introduced into icuin.dll in 10.0.15063. |
| uspoof_open | Introduced into icuin.dll in 10.0.15063. |
| uspoof_openFromSerialized | Introduced into icuin.dll in 10.0.15063. |
| uspoof_openFromSource | Introduced into icuin.dll in 10.0.15063. |
| uspoof_close | Introduced into icuin.dll in 10.0.15063. |
| uspoof_clone | Introduced into icuin.dll in 10.0.15063. |
| uspoof_setChecks | Introduced into icuin.dll in 10.0.15063. |
| uspoof_getChecks | Introduced into icuin.dll in 10.0.15063. |
| uspoof_setRestrictionLevel | Introduced into icuin.dll in 10.0.15063. |
| uspoof_getRestrictionLevel | Introduced into icuin.dll in 10.0.15063. |
| uspoof_setAllowedLocales | Introduced into icuin.dll in 10.0.15063. |
| uspoof_getAllowedLocales | Introduced into icuin.dll in 10.0.15063. |
| uspoof_setAllowedChars | Introduced into icuin.dll in 10.0.15063. |
| uspoof_getAllowedChars | Introduced into icuin.dll in 10.0.15063. |
| uspoof_check | Introduced into icuin.dll in 10.0.15063. |
| uspoof_checkUTF8 | Introduced into icuin.dll in 10.0.15063. |
| uspoof_areConfusable | Introduced into icuin.dll in 10.0.15063. |
| uspoof_areConfusableUTF8 | Introduced into icuin.dll in 10.0.15063. |
| uspoof_getSkeleton | Introduced into icuin.dll in 10.0.15063. |
| uspoof_getSkeletonUTF8 | Introduced into icuin.dll in 10.0.15063. |
| uspoof_getInclusionSet | Introduced into icuin.dll in 10.0.15063. |
| uspoof_getRecommendedSet | Introduced into icuin.dll in 10.0.15063. |
| uspoof_serialize | Introduced into icuin.dll in 10.0.15063. |
| utmscale_getTimeScaleValue | Introduced into icuin.dll in 10.0.15063. |
| utmscale_fromInt64 | Introduced into icuin.dll in 10.0.15063. |
| utmscale_toInt64 | Introduced into icuin.dll in 10.0.15063. |
| utrans_openU | Introduced into icuin.dll in 10.0.15063. |
| utrans_openInverse | Introduced into icuin.dll in 10.0.15063. |
| utrans_clone | Introduced into icuin.dll in 10.0.15063. |
| utrans_close | Introduced into icuin.dll in 10.0.15063. |
| utrans_getUnicodeID | Introduced into icuin.dll in 10.0.15063. |
| utrans_register | Introduced into icuin.dll in 10.0.15063. |
| utrans_unregisterID | Introduced into icuin.dll in 10.0.15063. |
| utrans_setFilter | Introduced into icuin.dll in 10.0.15063. |
| utrans_countAvailableIDs | Introduced into icuin.dll in 10.0.15063. |
| utrans_openIDs | Introduced into icuin.dll in 10.0.15063. |
| utrans_trans | Introduced into icuin.dll in 10.0.15063. |
| utrans_transIncremental | Introduced into icuin.dll in 10.0.15063. |
| utrans_transUChars | Introduced into icuin.dll in 10.0.15063. |
| utrans_transIncrementalUChars | Introduced into icuin.dll in 10.0.15063. |
| utrans_toRules | Introduced into icuin.dll in 10.0.15063. |
| utrans_getSourceSet | Introduced into icuin.dll in 10.0.15063. |


COM interfaces

| API | Requirements |
| -----| --------------|
| [_IRDPSessionEvents](https://msdn.microsoft.com/en-us/library/windows/desktop/aa373879.aspx) | Introduced in 10.0.10240. |
| _IWorkspaceBrokerAxEvents | Introduced in 10.0.10240. |
| [IAccessibleEx](https://msdn.microsoft.com/en-us/library/windows/desktop/ee671234.aspx) | Introduced in 10.0.10240. |
| [IAccessibleHostingElementProviders](https://msdn.microsoft.com/en-us/library/windows/desktop/hh448733.aspx) | Introduced in 10.0.10240. |
| [IActivateAudioInterfaceAsyncOperation](https://msdn.microsoft.com/en-us/library/windows/desktop/jj128300.aspx) | Introduced in 10.0.10240. |
| [IActivateAudioInterfaceCompletionHandler](https://msdn.microsoft.com/en-us/library/windows/desktop/jj128302.aspx) | Introduced in 10.0.10240. |
| [IActivationFactory](https://msdn.microsoft.com/en-us/library/windows/desktop/br205779.aspx) | Introduced in 10.0.10240. |
| [IAdvancedMediaCapture](https://msdn.microsoft.com/en-us/library/windows/desktop/hh802709.aspx) | Introduced in 10.0.10240. |
| [IAdvancedMediaCaptureInitializationSettings](https://msdn.microsoft.com/en-us/library/windows/desktop/hh802710.aspx) | Introduced in 10.0.10240. |
| [IAdvancedMediaCaptureSettings](https://msdn.microsoft.com/en-us/library/windows/desktop/hh802712.aspx) | Introduced in 10.0.10240. |
| [IAgileObject](https://msdn.microsoft.com/en-us/library/windows/desktop/hh802476.aspx) | Introduced in 10.0.10240. |
| [IAgileReference](https://msdn.microsoft.com/en-us/library/windows/desktop/dn269837.aspx) | Introduced in 10.0.10240. |
| [IAnnotationProvider](https://msdn.microsoft.com/en-us/library/windows/desktop/hh448757.aspx) | Introduced in 10.0.10240. |
| IAoWAppActivatedRuntime | Introduced in 10.0.10240. Removed in 10.0.15063. |
| IAoWBackgroundTaskRuntime | Introduced in 10.0.10240. Removed in 10.0.15063. |
| [IApartmentShutdown](https://msdn.microsoft.com/en-us/library/windows/desktop/jj219263.aspx) | Introduced in 10.0.10240. |
| [IAsyncInfo](https://msdn.microsoft.com/en-us/library/windows/desktop/br205795.aspx) | Introduced in 10.0.10240. |
| [IAudioCaptureClient](https://msdn.microsoft.com/en-us/library/windows/desktop/dd370858.aspx) | Introduced in 10.0.10240. |
| [IAudioClient](https://msdn.microsoft.com/en-us/library/windows/desktop/dd370865.aspx) | Introduced in 10.0.10240. |
| [IAudioClient2](https://msdn.microsoft.com/en-us/library/windows/desktop/hh404179.aspx) | Introduced in 10.0.10240. |
| [IAudioClient3](https://msdn.microsoft.com/en-us/library/windows/desktop/dn911487.aspx) | Introduced in 10.0.10240. |
| [IAudioClock](https://msdn.microsoft.com/en-us/library/windows/desktop/dd370881.aspx) | Introduced in 10.0.10240. |
| [IAudioEndpointVolume](https://msdn.microsoft.com/en-us/library/windows/desktop/dd370892.aspx) | Introduced in 10.0.10240. |
| [IAudioEndpointVolumeCallback](https://msdn.microsoft.com/en-us/library/windows/desktop/dd370894.aspx) | Introduced in 10.0.10240. |
| [IAudioFrameNative](https://msdn.microsoft.com/en-us/library/windows/desktop/mt431700.aspx) | Introduced in 10.0.10240. |
| [IAudioFrameNativeFactory](https://msdn.microsoft.com/en-us/library/windows/desktop/mt431701.aspx) | Introduced in 10.0.10240. |
| [IAudioMeterInformation](https://msdn.microsoft.com/en-us/library/windows/desktop/dd368227.aspx) | Introduced in 10.0.10240. |
| [IAudioRenderClient](https://msdn.microsoft.com/en-us/library/windows/desktop/dd368242.aspx) | Introduced in 10.0.10240. |
| [IAudioSessionControl](https://msdn.microsoft.com/en-us/library/windows/desktop/dd368246.aspx) | Introduced in 10.0.10240. |
| [IAudioSessionEvents](https://msdn.microsoft.com/en-us/library/windows/desktop/dd368289.aspx) | Introduced in 10.0.10240. |
| [IAudioStreamVolume](https://msdn.microsoft.com/en-us/library/windows/desktop/dd370977.aspx) | Introduced in 10.0.10240. |
| IAudioVideoCaptureDeviceNative | Introduced in 10.0.10240. |
| [IBindCtx](https://msdn.microsoft.com/en-us/library/windows/desktop/ms693755.aspx) | Introduced in 10.0.10240. |
| ICameraCaptureDeviceNative | Introduced in 10.0.10240. |
| ICameraCaptureFrameNative | Introduced in 10.0.10240. |
| ICameraCapturePreviewSink | Introduced in 10.0.10240. |
| [ICameraUIControl](https://msdn.microsoft.com/en-us/library/windows/desktop/hh802717.aspx) | Introduced in 10.0.10240. |
| [ICameraUIControlEventCallback](https://msdn.microsoft.com/en-us/library/windows/desktop/hh802718.aspx) | Introduced in 10.0.10240. |
| [IClassFactory](https://msdn.microsoft.com/en-us/library/windows/desktop/ms694364.aspx) | Introduced in 10.0.10240. |
| [IClientSecurity](https://msdn.microsoft.com/en-us/library/windows/desktop/ms683964.aspx) | Introduced in 10.0.10240. |
| [ICodecAPI](https://msdn.microsoft.com/en-us/library/windows/desktop/dd311953.aspx) | Introduced in 10.0.10240. |
| [IConnectionPoint](https://msdn.microsoft.com/en-us/library/windows/desktop/ms694318.aspx) | Introduced in 10.0.10240. |
| [IConnectionPointContainer](https://msdn.microsoft.com/en-us/library/windows/desktop/ms683857.aspx) | Introduced in 10.0.10240. |
| [IContextCallback](https://msdn.microsoft.com/en-us/library/windows/desktop/ms682253.aspx) | Introduced in 10.0.10240. |
| [ICreateDeviceAccessAsync](https://msdn.microsoft.com/en-us/library/windows/desktop/hh404248.aspx) | Introduced in 10.0.10240. |
| [ICustomNavigationProvider](https://msdn.microsoft.com/en-us/library/Mt146441.aspx) | Introduced in 10.0.10240. |
| [ID2D1AnalysisTransform](https://msdn.microsoft.com/en-us/library/windows/desktop/hh404347.aspx) | Introduced in 10.0.10240. |
| [ID2D1Bitmap](https://msdn.microsoft.com/en-us/library/windows/desktop/dd371109.aspx) | Introduced in 10.0.10240. |
| [ID2D1Bitmap1](https://msdn.microsoft.com/en-us/library/windows/desktop/hh404349.aspx) | Introduced in 10.0.10240. |
| [ID2D1BitmapBrush](https://msdn.microsoft.com/en-us/library/windows/desktop/dd371122.aspx) | Introduced in 10.0.10240. |
| [ID2D1BitmapRenderTarget](https://msdn.microsoft.com/en-us/library/windows/desktop/dd371146.aspx) | Introduced in 10.0.10240. |
| [ID2D1BlendTransform](https://msdn.microsoft.com/en-us/library/windows/desktop/hh404361.aspx) | Introduced in 10.0.10240. |
| [ID2D1BorderTransform](https://msdn.microsoft.com/en-us/library/windows/desktop/hh404367.aspx) | Introduced in 10.0.10240. |
| [ID2D1BoundsAdjustmentTransform](https://msdn.microsoft.com/en-us/library/windows/desktop/hh847963.aspx) | Introduced in 10.0.10240. |
| [ID2D1Brush](https://msdn.microsoft.com/en-us/library/windows/desktop/dd371173.aspx) | Introduced in 10.0.10240. |
| [ID2D1ColorContext](https://msdn.microsoft.com/en-us/library/windows/desktop/hh404388.aspx) | Introduced in 10.0.10240. |
| [ID2D1CommandList](https://msdn.microsoft.com/en-us/library/windows/desktop/hh404392.aspx) | Introduced in 10.0.10240. |
| [ID2D1CommandSink](https://msdn.microsoft.com/en-us/library/windows/desktop/hh404394.aspx) | Introduced in 10.0.10240. |
| [ID2D1CommandSink1](https://msdn.microsoft.com/en-us/library/windows/desktop/dn280436.aspx) | Introduced in 10.0.10240. |
| [ID2D1CommandSink2](https://msdn.microsoft.com/en-us/library/windows/desktop/dn890781.aspx) | Introduced in 10.0.10240. |
| [ID2D1ComputeInfo](https://msdn.microsoft.com/en-us/library/windows/desktop/hh847966.aspx) | Introduced in 10.0.10240. |
| [ID2D1ComputeTransform](https://msdn.microsoft.com/en-us/library/windows/desktop/hh404434.aspx) | Introduced in 10.0.10240. |
| [ID2D1ConcreteTransform](https://msdn.microsoft.com/en-us/library/windows/desktop/hh404452.aspx) | Introduced in 10.0.10240. |
| [ID2D1DCRenderTarget](https://msdn.microsoft.com/en-us/library/windows/desktop/dd371213.aspx) | Introduced in 10.0.10240. |
| [ID2D1Device](https://msdn.microsoft.com/en-us/library/windows/desktop/hh404478.aspx) | Introduced in 10.0.10240. |
| [ID2D1Device1](https://msdn.microsoft.com/en-us/library/windows/desktop/dn280458.aspx) | Introduced in 10.0.10240. |
| [ID2D1Device2](https://msdn.microsoft.com/en-us/library/windows/desktop/dn890786.aspx) | Introduced in 10.0.10240. |
| [ID2D1DeviceContext](https://msdn.microsoft.com/en-us/library/windows/desktop/hh404479.aspx) | Introduced in 10.0.10240. |
| [ID2D1DeviceContext1](https://msdn.microsoft.com/en-us/library/windows/desktop/dn280461.aspx) | Introduced in 10.0.10240. |
| [ID2D1DeviceContext2](https://msdn.microsoft.com/en-us/library/windows/desktop/dn890789.aspx) | Introduced in 10.0.10240. |
| [ID2D1DrawInfo](https://msdn.microsoft.com/en-us/library/windows/desktop/hh847986.aspx) | Introduced in 10.0.10240. |
| [ID2D1DrawingStateBlock](https://msdn.microsoft.com/en-us/library/windows/desktop/dd371218.aspx) | Introduced in 10.0.10240. |
| [ID2D1DrawingStateBlock1](https://msdn.microsoft.com/en-us/library/windows/desktop/hh871452.aspx) | Introduced in 10.0.10240. |
| [ID2D1DrawTransform](https://msdn.microsoft.com/en-us/library/windows/desktop/hh847992.aspx) | Introduced in 10.0.10240. |
| [ID2D1Effect](https://msdn.microsoft.com/en-us/library/windows/desktop/hh404566.aspx) | Introduced in 10.0.10240. |
| [ID2D1EffectContext](https://msdn.microsoft.com/en-us/library/windows/desktop/hh404459.aspx) | Introduced in 10.0.10240. |
| [ID2D1EffectContext1](https://msdn.microsoft.com/en-us/library/windows/desktop/dn949338.aspx) | Introduced in 10.0.10240. |
| [ID2D1EffectImpl](https://msdn.microsoft.com/en-us/library/windows/desktop/hh404568.aspx) | Introduced in 10.0.10240. |
| [ID2D1EllipseGeometry](https://msdn.microsoft.com/en-us/library/windows/desktop/dd371239.aspx) | Introduced in 10.0.10240. |
| [ID2D1Factory](https://msdn.microsoft.com/en-us/library/windows/desktop/dd371246.aspx) | Introduced in 10.0.10240. |
| [ID2D1Factory1](https://msdn.microsoft.com/en-us/library/windows/desktop/hh404596.aspx) | Introduced in 10.0.10240. |
| [ID2D1Factory2](https://msdn.microsoft.com/en-us/library/windows/desktop/dn280481.aspx) | Introduced in 10.0.10240. |
| [ID2D1Factory3](https://msdn.microsoft.com/en-us/library/windows/desktop/dn900394.aspx) | Introduced in 10.0.10240. |
| [ID2D1GdiMetafile](https://msdn.microsoft.com/en-us/library/windows/desktop/hh871460.aspx) | Introduced in 10.0.10240. |
| [ID2D1GdiMetafile1](https://msdn.microsoft.com/en-us/library/windows/desktop/dn900400.aspx) | Introduced in 10.0.10240. |
| [ID2D1GdiMetafileSink](https://msdn.microsoft.com/en-us/library/windows/desktop/hh871461.aspx) | Introduced in 10.0.10240. |
| [ID2D1GdiMetafileSink1](https://msdn.microsoft.com/en-us/library/windows/desktop/dn900403.aspx) | Introduced in 10.0.10240. |
| [ID2D1Geometry](https://msdn.microsoft.com/en-us/library/windows/desktop/dd316578.aspx) | Introduced in 10.0.10240. |
| [ID2D1GeometryGroup](https://msdn.microsoft.com/en-us/library/windows/desktop/dd316581.aspx) | Introduced in 10.0.10240. |
| [ID2D1GeometryRealization](https://msdn.microsoft.com/en-us/library/windows/desktop/dn280515.aspx) | Introduced in 10.0.10240. |
| [ID2D1GeometrySink](https://msdn.microsoft.com/en-us/library/windows/desktop/dd316592.aspx) | Introduced in 10.0.10240. |
| [ID2D1GradientMesh](https://msdn.microsoft.com/en-us/library/windows/desktop/dn900410.aspx) | Introduced in 10.0.10240. |
| [ID2D1GradientStopCollection](https://msdn.microsoft.com/en-us/library/windows/desktop/dd316783.aspx) | Introduced in 10.0.10240. |
| [ID2D1GradientStopCollection1](https://msdn.microsoft.com/en-us/library/windows/desktop/hh446792.aspx) | Introduced in 10.0.10240. |
| [ID2D1HwndRenderTarget](https://msdn.microsoft.com/en-us/library/windows/desktop/dd371461.aspx) | Introduced in 10.0.10240. |
| [ID2D1Image](https://msdn.microsoft.com/en-us/library/windows/desktop/hh446803.aspx) | Introduced in 10.0.10240. |
| [ID2D1ImageBrush](https://msdn.microsoft.com/en-us/library/windows/desktop/hh446804.aspx) | Introduced in 10.0.10240. |
| [ID2D1ImageSource](https://msdn.microsoft.com/en-us/library/windows/desktop/dn900413.aspx) | Introduced in 10.0.10240. |
| [ID2D1ImageSourceFromWic](https://msdn.microsoft.com/en-us/library/windows/desktop/dn900414.aspx) | Introduced in 10.0.10240. |
| [ID2D1Ink](https://msdn.microsoft.com/en-us/library/windows/desktop/dn900426.aspx) | Introduced in 10.0.10240. |
| [ID2D1InkStyle](https://msdn.microsoft.com/en-us/library/windows/desktop/dn900427.aspx) | Introduced in 10.0.10240. |
| [ID2D1Layer](https://msdn.microsoft.com/en-us/library/windows/desktop/dd371483.aspx) | Introduced in 10.0.10240. |
| [ID2D1LinearGradientBrush](https://msdn.microsoft.com/en-us/library/windows/desktop/dd371488.aspx) | Introduced in 10.0.10240. |
| [ID2D1LookupTable3D](https://msdn.microsoft.com/en-us/library/windows/desktop/dn900453.aspx) | Introduced in 10.0.10240. |
| [ID2D1Mesh](https://msdn.microsoft.com/en-us/library/windows/desktop/dd371508.aspx) | Introduced in 10.0.10240. |
| [ID2D1Multithread](https://msdn.microsoft.com/en-us/library/windows/desktop/hh997713.aspx) | Introduced in 10.0.10240. |
| [ID2D1OffsetTransform](https://msdn.microsoft.com/en-us/library/windows/desktop/hh446820.aspx) | Introduced in 10.0.10240. |
| [ID2D1PathGeometry](https://msdn.microsoft.com/en-us/library/windows/desktop/dd371512.aspx) | Introduced in 10.0.10240. |
| [ID2D1PathGeometry1](https://msdn.microsoft.com/en-us/library/windows/desktop/hh446826.aspx) | Introduced in 10.0.10240. |
| [ID2D1PrintControl](https://msdn.microsoft.com/en-us/library/windows/desktop/hh847997.aspx) | Introduced in 10.0.10240. |
| [ID2D1Properties](https://msdn.microsoft.com/en-us/library/windows/desktop/hh446854.aspx) | Introduced in 10.0.10240. |
| [ID2D1RadialGradientBrush](https://msdn.microsoft.com/en-us/library/windows/desktop/dd371529.aspx) | Introduced in 10.0.10240. |
| [ID2D1RectangleGeometry](https://msdn.microsoft.com/en-us/library/windows/desktop/dd371561.aspx) | Introduced in 10.0.10240. |
| [ID2D1RenderInfo](https://msdn.microsoft.com/en-us/library/windows/desktop/hh446890.aspx) | Introduced in 10.0.10240. |
| [ID2D1RenderTarget](https://msdn.microsoft.com/en-us/library/windows/desktop/dd371766.aspx) | Introduced in 10.0.10240. |
| [ID2D1Resource](https://msdn.microsoft.com/en-us/library/windows/desktop/dd316908.aspx) | Introduced in 10.0.10240. |
| [ID2D1ResourceTexture](https://msdn.microsoft.com/en-us/library/windows/desktop/hh446904.aspx) | Introduced in 10.0.10240. |
| [ID2D1RoundedRectangleGeometry](https://msdn.microsoft.com/en-us/library/windows/desktop/dd316914.aspx) | Introduced in 10.0.10240. |
| [ID2D1SimplifiedGeometrySink](https://msdn.microsoft.com/en-us/library/windows/desktop/dd316919.aspx) | Introduced in 10.0.10240. |
| [ID2D1SolidColorBrush](https://msdn.microsoft.com/en-us/library/windows/desktop/dd372207.aspx) | Introduced in 10.0.10240. |
| [ID2D1SourceTransform](https://msdn.microsoft.com/en-us/library/windows/desktop/hh446908.aspx) | Introduced in 10.0.10240. |
| [ID2D1StrokeStyle](https://msdn.microsoft.com/en-us/library/windows/desktop/dd372217.aspx) | Introduced in 10.0.10240. |
| [ID2D1StrokeStyle1](https://msdn.microsoft.com/en-us/library/windows/desktop/hh446914.aspx) | Introduced in 10.0.10240. |
| [ID2D1TessellationSink](https://msdn.microsoft.com/en-us/library/windows/desktop/dd372245.aspx) | Introduced in 10.0.10240. |
| [ID2D1Transform](https://msdn.microsoft.com/en-us/library/windows/desktop/hh446919.aspx) | Introduced in 10.0.10240. |
| [ID2D1TransformedGeometry](https://msdn.microsoft.com/en-us/library/windows/desktop/dd372252.aspx) | Introduced in 10.0.10240. |
| [ID2D1TransformedImageSource](https://msdn.microsoft.com/en-us/library/windows/desktop/dn952305.aspx) | Introduced in 10.0.10240. |
| [ID2D1TransformGraph](https://msdn.microsoft.com/en-us/library/windows/desktop/hh446920.aspx) | Introduced in 10.0.10240. |
| [ID2D1TransformNode](https://msdn.microsoft.com/en-us/library/windows/desktop/hh446939.aspx) | Introduced in 10.0.10240. |
| [ID2D1VertexBuffer](https://msdn.microsoft.com/en-us/library/windows/desktop/hh446949.aspx) | Introduced in 10.0.10240. |
| [ID3D10Blob](https://msdn.microsoft.com/en-us/library/windows/desktop/bb173507.aspx) | Introduced in 10.0.10240. |
| [ID3D10Multithread](https://msdn.microsoft.com/en-us/library/windows/desktop/bb173816.aspx) | Introduced in 10.0.10240. |
| [ID3D11Asynchronous](https://msdn.microsoft.com/en-us/library/windows/desktop/ff476347.aspx) | Introduced in 10.0.10240. |
| [ID3D11AuthenticatedChannel](https://msdn.microsoft.com/en-us/library/windows/desktop/hh447690.aspx) | Introduced in 10.0.10240. |
| [ID3D11BlendState](https://msdn.microsoft.com/en-us/library/windows/desktop/ff476349.aspx) | Introduced in 10.0.10240. |
| [ID3D11BlendState1](https://msdn.microsoft.com/en-us/library/windows/desktop/hh404571.aspx) | Introduced in 10.0.10240. |
| [ID3D11Buffer](https://msdn.microsoft.com/en-us/library/windows/desktop/ff476351.aspx) | Introduced in 10.0.10240. |
| [ID3D11ClassInstance](https://msdn.microsoft.com/en-us/library/windows/desktop/ff476353.aspx) | Introduced in 10.0.10240. |
| [ID3D11ClassLinkage](https://msdn.microsoft.com/en-us/library/windows/desktop/ff476358.aspx) | Introduced in 10.0.10240. |
| [ID3D11CommandList](https://msdn.microsoft.com/en-us/library/windows/desktop/ff476361.aspx) | Introduced in 10.0.10240. |
| [ID3D11ComputeShader](https://msdn.microsoft.com/en-us/library/windows/desktop/ff476363.aspx) | Introduced in 10.0.10240. |
| [ID3D11Counter](https://msdn.microsoft.com/en-us/library/windows/desktop/ff476364.aspx) | Introduced in 10.0.10240. |
| [ID3D11CryptoSession](https://msdn.microsoft.com/en-us/library/windows/desktop/hh447691.aspx) | Introduced in 10.0.10240. |
| [ID3D11Debug](https://msdn.microsoft.com/en-us/library/windows/desktop/ff476366.aspx) | Introduced in 10.0.10240. |
| [ID3D11DepthStencilState](https://msdn.microsoft.com/en-us/library/windows/desktop/ff476375.aspx) | Introduced in 10.0.10240. |
| [ID3D11DepthStencilView](https://msdn.microsoft.com/en-us/library/windows/desktop/ff476377.aspx) | Introduced in 10.0.10240. |
| [ID3D11Device](https://msdn.microsoft.com/en-us/library/windows/desktop/ff476379.aspx) | Introduced in 10.0.10240. |
| [ID3D11Device1](https://msdn.microsoft.com/en-us/library/windows/desktop/hh404575.aspx) | Introduced in 10.0.10240. |
| [ID3D11Device2](https://msdn.microsoft.com/en-us/library/windows/desktop/dn280493.aspx) | Introduced in 10.0.10240. |
| [ID3D11DeviceChild](https://msdn.microsoft.com/en-us/library/windows/desktop/ff476380.aspx) | Introduced in 10.0.10240. |
| [ID3D11DeviceContext](https://msdn.microsoft.com/en-us/library/windows/desktop/ff476385.aspx) | Introduced in 10.0.10240. |
| [ID3D11DeviceContext1](https://msdn.microsoft.com/en-us/library/windows/desktop/hh404598.aspx) | Introduced in 10.0.10240. |
| [ID3D11DeviceContext2](https://msdn.microsoft.com/en-us/library/windows/desktop/dn280498.aspx) | Introduced in 10.0.10240. |
| [ID3D11DeviceContext3](https://msdn.microsoft.com/en-us/library/windows/desktop/dn912875.aspx) | Introduced in 10.0.10240. |
| [ID3D11Device3](https://msdn.microsoft.com/en-us/library/windows/desktop/dn899218.aspx) | Introduced in 10.0.10240. |
| [ID3D11Texture2D1](https://msdn.microsoft.com/en-us/library/windows/desktop/dn899244.aspx) | Introduced in 10.0.10240. |
| [ID3D11Texture3D1](https://msdn.microsoft.com/en-us/library/windows/desktop/dn899246.aspx) | Introduced in 10.0.10240. |
| [ID3D11DomainShader](https://msdn.microsoft.com/en-us/library/windows/desktop/ff476535.aspx) | Introduced in 10.0.10240. |
| [ID3D11FunctionLinkingGraph](https://msdn.microsoft.com/en-us/library/windows/desktop/dn280535.aspx) | Introduced in 10.0.10240. |
| [ID3D11GeometryShader](https://msdn.microsoft.com/en-us/library/windows/desktop/ff476536.aspx) | Introduced in 10.0.10240. |
| [ID3D11HullShader](https://msdn.microsoft.com/en-us/library/windows/desktop/ff476537.aspx) | Introduced in 10.0.10240. |
| [ID3D11InfoQueue](https://msdn.microsoft.com/en-us/library/windows/desktop/ff476538.aspx) | Introduced in 10.0.10240. |
| [ID3D11InputLayout](https://msdn.microsoft.com/en-us/library/windows/desktop/ff476575.aspx) | Introduced in 10.0.10240. |
| [ID3D11LibraryReflection](https://msdn.microsoft.com/en-us/library/windows/desktop/dn280554.aspx) | Introduced in 10.0.10240. |
| [ID3D11Linker](https://msdn.microsoft.com/en-us/library/windows/desktop/dn280558.aspx) | Introduced in 10.0.10240. |
| [ID3D11LinkingNode](https://msdn.microsoft.com/en-us/library/windows/desktop/dn280562.aspx) | Introduced in 10.0.10240. |
| [ID3D11Module](https://msdn.microsoft.com/en-us/library/windows/desktop/dn280563.aspx) | Introduced in 10.0.10240. |
| [ID3D11ModuleInstance](https://msdn.microsoft.com/en-us/library/windows/desktop/dn280564.aspx) | Introduced in 10.0.10240. |
| [ID3D11On12Device](https://msdn.microsoft.com/en-us/library/Dn913197.aspx) | Introduced in 10.0.10240. |
| [ID3D11PixelShader](https://msdn.microsoft.com/en-us/library/windows/desktop/ff476576.aspx) | Introduced in 10.0.10240. |
| [ID3D11Predicate](https://msdn.microsoft.com/en-us/library/windows/desktop/ff476577.aspx) | Introduced in 10.0.10240. |
| [ID3D11Query](https://msdn.microsoft.com/en-us/library/windows/desktop/ff476578.aspx) | Introduced in 10.0.10240. |
| [ID3D11Query1](https://msdn.microsoft.com/en-us/library/windows/desktop/dn899236.aspx) | Introduced in 10.0.10240. |
| [ID3D11RasterizerState](https://msdn.microsoft.com/en-us/library/windows/desktop/ff476580.aspx) | Introduced in 10.0.10240. |
| [ID3D11RasterizerState1](https://msdn.microsoft.com/en-us/library/windows/desktop/hh446828.aspx) | Introduced in 10.0.10240. |
| [ID3D11RasterizerState2](https://msdn.microsoft.com/en-us/library/windows/desktop/dn899238.aspx) | Introduced in 10.0.10240. |
| [ID3D11RefDefaultTrackingOptions](https://msdn.microsoft.com/en-us/library/windows/desktop/hh446832.aspx) | Introduced in 10.0.10240. |
| [ID3D11RefTrackingOptions](https://msdn.microsoft.com/en-us/library/windows/desktop/hh446836.aspx) | Introduced in 10.0.10240. |
| [ID3D11RenderTargetView](https://msdn.microsoft.com/en-us/library/windows/desktop/ff476582.aspx) | Introduced in 10.0.10240. |
| [ID3D11RenderTargetView1](https://msdn.microsoft.com/en-us/library/windows/desktop/dn899240.aspx) | Introduced in 10.0.10240. |
| [ID3D11Resource](https://msdn.microsoft.com/en-us/library/windows/desktop/ff476584.aspx) | Introduced in 10.0.10240. |
| [ID3D11SamplerState](https://msdn.microsoft.com/en-us/library/windows/desktop/ff476588.aspx) | Introduced in 10.0.10240. |
| [ID3D11ShaderReflection](https://msdn.microsoft.com/en-us/library/windows/desktop/ff476590.aspx) | Introduced in 10.0.10240. |
| [ID3D11ShaderReflectionConstantBuffer](https://msdn.microsoft.com/en-us/library/windows/desktop/ff476591.aspx) | Introduced in 10.0.10240. |
| [ID3D11ShaderReflectionType](https://msdn.microsoft.com/en-us/library/windows/desktop/ff476595.aspx) | Introduced in 10.0.10240. |
| [ID3D11ShaderReflectionVariable](https://msdn.microsoft.com/en-us/library/windows/desktop/ff476607.aspx) | Introduced in 10.0.10240. |
| [ID3D11ShaderResourceView](https://msdn.microsoft.com/en-us/library/windows/desktop/ff476628.aspx) | Introduced in 10.0.10240. |
| [ID3D11ShaderResourceView1](https://msdn.microsoft.com/en-us/library/windows/desktop/dn899242.aspx) | Introduced in 10.0.10240. |
| [ID3D11ShaderTrace](https://msdn.microsoft.com/en-us/library/windows/desktop/hh446840.aspx) | Introduced in 10.0.10240. |
| [ID3D11ShaderTraceFactory](https://msdn.microsoft.com/en-us/library/windows/desktop/hh446842.aspx) | Introduced in 10.0.10240. |
| [ID3D11Texture1D](https://msdn.microsoft.com/en-us/library/windows/desktop/ff476633.aspx) | Introduced in 10.0.10240. |
| [ID3D11Texture2D](https://msdn.microsoft.com/en-us/library/windows/desktop/ff476635.aspx) | Introduced in 10.0.10240. |
| [ID3D11Texture3D](https://msdn.microsoft.com/en-us/library/windows/desktop/ff476637.aspx) | Introduced in 10.0.10240. |
| [ID3D11TracingDevice](https://msdn.microsoft.com/en-us/library/windows/desktop/hh446868.aspx) | Introduced in 10.0.10240. |
| [ID3D11UnorderedAccessView](https://msdn.microsoft.com/en-us/library/windows/desktop/ff476639.aspx) | Introduced in 10.0.10240. |
| [ID3D11UnorderedAccessView1](https://msdn.microsoft.com/en-us/library/windows/desktop/dn899248.aspx) | Introduced in 10.0.10240. |
| [ID3D11VertexShader](https://msdn.microsoft.com/en-us/library/windows/desktop/ff476641.aspx) | Introduced in 10.0.10240. |
| [ID3D11VideoContext](https://msdn.microsoft.com/en-us/library/windows/desktop/hh447703.aspx) | Introduced in 10.0.10240. |
| [ID3D11VideoContext1](https://msdn.microsoft.com/en-us/library/windows/desktop/dn894126.aspx) | Introduced in 10.0.10240. |
| [ID3D11VideoDecoder](https://msdn.microsoft.com/en-us/library/windows/desktop/hh447766.aspx) | Introduced in 10.0.10240. |
| [ID3D11VideoDecoderOutputView](https://msdn.microsoft.com/en-us/library/windows/desktop/hh447767.aspx) | Introduced in 10.0.10240. |
| [ID3D11VideoDevice](https://msdn.microsoft.com/en-us/library/windows/desktop/hh447781.aspx) | Introduced in 10.0.10240. |
| [ID3D11VideoDevice1](https://msdn.microsoft.com/en-us/library/windows/desktop/dn894141.aspx) | Introduced in 10.0.10240. |
| [ID3D11VideoProcessor](https://msdn.microsoft.com/en-us/library/windows/desktop/hh447799.aspx) | Introduced in 10.0.10240. |
| [ID3D11VideoProcessorEnumerator](https://msdn.microsoft.com/en-us/library/windows/desktop/hh447800.aspx) | Introduced in 10.0.10240. |
| [ID3D11VideoProcessorEnumerator1](https://msdn.microsoft.com/en-us/library/windows/desktop/dn894146.aspx) | Introduced in 10.0.10240. |
| [ID3D11VideoProcessorInputView](https://msdn.microsoft.com/en-us/library/windows/desktop/hh447807.aspx) | Introduced in 10.0.10240. |
| [ID3D11VideoProcessorOutputView](https://msdn.microsoft.com/en-us/library/windows/desktop/hh447809.aspx) | Introduced in 10.0.10240. |
| [ID3D11View](https://msdn.microsoft.com/en-us/library/windows/desktop/ff476642.aspx) | Introduced in 10.0.10240. |
| [ID3D12CommandAllocator](https://msdn.microsoft.com/en-us/library/Dn770463.aspx) | Introduced in 10.0.10240. |
| [ID3D12CommandList](https://msdn.microsoft.com/en-us/library/Dn770465.aspx) | Introduced in 10.0.10240. |
| [ID3D12CommandQueue](https://msdn.microsoft.com/en-us/library/Dn788627.aspx) | Introduced in 10.0.10240. |
| [ID3D12CommandSignature](https://msdn.microsoft.com/en-us/library/Dn891446.aspx) | Introduced in 10.0.10240. |
| [ID3D12Debug](https://msdn.microsoft.com/en-us/library/Dn950153.aspx) | Introduced in 10.0.10240. |
| [ID3D12DebugCommandList](https://msdn.microsoft.com/en-us/library/Dn950154.aspx) | Introduced in 10.0.10240. |
| [ID3D12DebugCommandQueue](https://msdn.microsoft.com/en-us/library/Dn950158.aspx) | Introduced in 10.0.10240. |
| [ID3D12DebugDevice](https://msdn.microsoft.com/en-us/library/Dn986873.aspx) | Introduced in 10.0.10240. |
| [ID3D12DescriptorHeap](https://msdn.microsoft.com/en-us/library/Dn788648.aspx) | Introduced in 10.0.10240. |
| [ID3D12Device](https://msdn.microsoft.com/en-us/library/Dn788650.aspx) | Introduced in 10.0.10240. |
| [ID3D12DeviceChild](https://msdn.microsoft.com/en-us/library/Dn788651.aspx) | Introduced in 10.0.10240. |
| [ID3D12Fence](https://msdn.microsoft.com/en-us/library/Dn899188.aspx) | Introduced in 10.0.10240. |
| [ID3D12GraphicsCommandList](https://msdn.microsoft.com/en-us/library/Dn903537.aspx) | Introduced in 10.0.10240. |
| [ID3D12Heap](https://msdn.microsoft.com/en-us/library/Dn788687.aspx) | Introduced in 10.0.10240. |
| [ID3D12InfoQueue](https://msdn.microsoft.com/en-us/library/Dn950163.aspx) | Introduced in 10.0.10240. |
| [ID3D12LibraryReflection](https://msdn.microsoft.com/en-us/library/Dn933676.aspx) | Introduced in 10.0.10240. |
| [ID3D12Object](https://msdn.microsoft.com/en-us/library/Dn788699.aspx) | Introduced in 10.0.10240. |
| [ID3D12Pageable](https://msdn.microsoft.com/en-us/library/Dn788704.aspx) | Introduced in 10.0.10240. |
| [ID3D12PipelineState](https://msdn.microsoft.com/en-us/library/Dn788705.aspx) | Introduced in 10.0.10240. |
| [ID3D12QueryHeap](https://msdn.microsoft.com/en-us/library/Dn891447.aspx) | Introduced in 10.0.10240. |
| [ID3D12Resource](https://msdn.microsoft.com/en-us/library/Dn788709.aspx) | Introduced in 10.0.10240. |
| [ID3D12RootSignature](https://msdn.microsoft.com/en-us/library/Dn788714.aspx) | Introduced in 10.0.10240. |
| [ID3D12RootSignatureDeserializer](https://msdn.microsoft.com/en-us/library/Dn899192.aspx) | Introduced in 10.0.10240. |
| [ID3D12ShaderReflection](https://msdn.microsoft.com/en-us/library/Dn933679.aspx) | Introduced in 10.0.10240. |
| [ID3DDeviceContextState](https://msdn.microsoft.com/en-us/library/windows/desktop/hh446878.aspx) | Introduced in 10.0.10240. |
| [ID3DUserDefinedAnnotation](https://msdn.microsoft.com/en-us/library/windows/desktop/hh446881.aspx) | Introduced in 10.0.10240. |
| [IDeviceIoControl](https://msdn.microsoft.com/en-us/library/windows/desktop/hh404258.aspx) | Introduced in 10.0.10240. |
| [IDeviceRequestCompletionCallback](https://msdn.microsoft.com/en-us/library/windows/desktop/hh404262.aspx) | Introduced in 10.0.10240. |
| [IDirect3DDxgiInterfaceAccess](https://msdn.microsoft.com/en-us/library/Dn895103.aspx) | Introduced in 10.0.10240. |
| [IDirectWriterLock](https://msdn.microsoft.com/en-us/library/windows/desktop/aa379158.aspx) | Introduced in 10.0.10240. |
| [IDispatch](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221608.aspx) | Introduced in 10.0.10240. |
| [IDockProvider](https://msdn.microsoft.com/en-us/library/windows/desktop/ee671239.aspx) | Introduced in 10.0.10240. |
| [IDragProvider](https://msdn.microsoft.com/en-us/library/windows/desktop/hh707338.aspx) | Introduced in 10.0.10240. |
| [IDropTargetProvider](https://msdn.microsoft.com/en-us/library/windows/desktop/hh707345.aspx) | Introduced in 10.0.10240. |
| [IDvdControl2](https://msdn.microsoft.com/en-us/library/windows/desktop/dd389895.aspx) | Introduced in 10.0.10240. |
| [IDvdInfo2](https://msdn.microsoft.com/en-us/library/windows/desktop/dd376432.aspx) | Introduced in 10.0.10240. |
| [IDWriteBitmapRenderTarget](https://msdn.microsoft.com/en-us/library/windows/desktop/dd368165.aspx) | Introduced in 10.0.10240. |
| [IDWriteBitmapRenderTarget1](https://msdn.microsoft.com/en-us/library/windows/desktop/hh780398.aspx) | Introduced in 10.0.10240. |
| [IDWriteColorGlyphRunEnumerator](https://msdn.microsoft.com/en-us/library/windows/desktop/dn280445.aspx) | Introduced in 10.0.10240. |
| [IDWriteFactory](https://msdn.microsoft.com/en-us/library/windows/desktop/dd368183.aspx) | Introduced in 10.0.10240. |
| [IDWriteFactory1](https://msdn.microsoft.com/en-us/library/windows/desktop/hh780401.aspx) | Introduced in 10.0.10240. |
| [IDWriteFactory2](https://msdn.microsoft.com/en-us/library/windows/desktop/dn280448.aspx) | Introduced in 10.0.10240. |
| [IDWriteFactory3](https://msdn.microsoft.com/en-us/library/windows/desktop/dn890753.aspx) | Introduced in 10.0.10240. |
| [IDWriteFont](https://msdn.microsoft.com/en-us/library/windows/desktop/dd368213.aspx) | Introduced in 10.0.10240. |
| [IDWriteFont1](https://msdn.microsoft.com/en-us/library/windows/desktop/hh780404.aspx) | Introduced in 10.0.10240. |
| [IDWriteFont2](https://msdn.microsoft.com/en-us/library/windows/desktop/dn280452.aspx) | Introduced in 10.0.10240. |
| [IDWriteFont3](https://msdn.microsoft.com/en-us/library/windows/desktop/dn890766.aspx) | Introduced in 10.0.10240. |
| [IDWriteFontCollection](https://msdn.microsoft.com/en-us/library/windows/desktop/dd368214.aspx) | Introduced in 10.0.10240. |
| [IDWriteFontCollection1](https://msdn.microsoft.com/en-us/library/windows/desktop/dn933224.aspx) | Introduced in 10.0.10240. |
| [IDWriteFontCollectionLoader](https://msdn.microsoft.com/en-us/library/windows/desktop/dd368215.aspx) | Introduced in 10.0.10240. |
| [IDWriteFontDownloadListener](https://msdn.microsoft.com/en-us/library/windows/desktop/dn890775.aspx) | Introduced in 10.0.10240. |
| [IDWriteFontDownloadQueue](https://msdn.microsoft.com/en-us/library/windows/desktop/dn890778.aspx) | Introduced in 10.0.10240. |
| [IDWriteFontFace](https://msdn.microsoft.com/en-us/library/windows/desktop/dd370983.aspx) | Introduced in 10.0.10240. |
| [IDWriteFontFace1](https://msdn.microsoft.com/en-us/library/windows/desktop/hh780409.aspx) | Introduced in 10.0.10240. |
| [IDWriteFontFace2](https://msdn.microsoft.com/en-us/library/windows/desktop/dn280454.aspx) | Introduced in 10.0.10240. |
| [IDWriteFontFace3](https://msdn.microsoft.com/en-us/library/windows/desktop/dn894561.aspx) | Introduced in 10.0.10240. |
| [IDWriteFontFaceReference](https://msdn.microsoft.com/en-us/library/windows/desktop/dn894576.aspx) | Introduced in 10.0.10240. |
| [IDWriteFontFallback](https://msdn.microsoft.com/en-us/library/windows/desktop/dn280474.aspx) | Introduced in 10.0.10240. |
| [IDWriteFontFallbackBuilder](https://msdn.microsoft.com/en-us/library/windows/desktop/dn280476.aspx) | Introduced in 10.0.10240. |
| [IDWriteFontFamily](https://msdn.microsoft.com/en-us/library/windows/desktop/dd371042.aspx) | Introduced in 10.0.10240. |
| [IDWriteFontFamily1](https://msdn.microsoft.com/en-us/library/windows/desktop/dn894590.aspx) | Introduced in 10.0.10240. |
| [IDWriteFontFile](https://msdn.microsoft.com/en-us/library/windows/desktop/dd371060.aspx) | Introduced in 10.0.10240. |
| [IDWriteFontFileEnumerator](https://msdn.microsoft.com/en-us/library/windows/desktop/dd371063.aspx) | Introduced in 10.0.10240. |
| [IDWriteFontFileLoader](https://msdn.microsoft.com/en-us/library/windows/desktop/dd371075.aspx) | Introduced in 10.0.10240. |
| [IDWriteFontFileStream](https://msdn.microsoft.com/en-us/library/windows/desktop/dd371081.aspx) | Introduced in 10.0.10240. |
| [IDWriteFontList](https://msdn.microsoft.com/en-us/library/windows/desktop/dd371120.aspx) | Introduced in 10.0.10240. |
| [IDWriteFontList1](https://msdn.microsoft.com/en-us/library/windows/desktop/dn894594.aspx) | Introduced in 10.0.10240. |
| [IDWriteFontSet](https://msdn.microsoft.com/en-us/library/windows/desktop/dn933235.aspx) | Introduced in 10.0.10240. |
| [IDWriteFontSetBuilder](https://msdn.microsoft.com/en-us/library/windows/desktop/dn933236.aspx) | Introduced in 10.0.10240. |
| [IDWriteGdiInterop](https://msdn.microsoft.com/en-us/library/windows/desktop/dd371172.aspx) | Introduced in 10.0.10240. |
| [IDWriteGdiInterop1](https://msdn.microsoft.com/en-us/library/windows/desktop/dn958415.aspx) | Introduced in 10.0.10240. |
| [IDWriteGlyphRunAnalysis](https://msdn.microsoft.com/en-us/library/windows/desktop/dd371188.aspx) | Introduced in 10.0.10240. |
| [IDWriteInlineObject](https://msdn.microsoft.com/en-us/library/windows/desktop/dd371221.aspx) | Introduced in 10.0.10240. |
| [IDWriteLocalFontFileLoader](https://msdn.microsoft.com/en-us/library/windows/desktop/dd371238.aspx) | Introduced in 10.0.10240. |
| [IDWriteLocalizedStrings](https://msdn.microsoft.com/en-us/library/windows/desktop/dd371250.aspx) | Introduced in 10.0.10240. |
| [IDWriteNumberSubstitution](https://msdn.microsoft.com/en-us/library/windows/desktop/dd371271.aspx) | Introduced in 10.0.10240. |
| [IDWritePixelSnapping](https://msdn.microsoft.com/en-us/library/windows/desktop/dd371274.aspx) | Introduced in 10.0.10240. |
| [IDWriteRenderingParams](https://msdn.microsoft.com/en-us/library/windows/desktop/dd371285.aspx) | Introduced in 10.0.10240. |
| [IDWriteRenderingParams1](https://msdn.microsoft.com/en-us/library/windows/desktop/hh780422.aspx) | Introduced in 10.0.10240. |
| [IDWriteRenderingParams2](https://msdn.microsoft.com/en-us/library/windows/desktop/dn900387.aspx) | Introduced in 10.0.10240. |
| [IDWriteRenderingParams3](https://msdn.microsoft.com/en-us/library/windows/desktop/dn900389.aspx) | Introduced in 10.0.10240. |
| [IDWriteStringList](https://msdn.microsoft.com/en-us/library/windows/desktop/dn958421.aspx) | Introduced in 10.0.10240. |
| [IDWriteTextAnalysisSink](https://msdn.microsoft.com/en-us/library/windows/desktop/dd371303.aspx) | Introduced in 10.0.10240. |
| [IDWriteTextAnalysisSink1](https://msdn.microsoft.com/en-us/library/windows/desktop/hh780424.aspx) | Introduced in 10.0.10240. |
| [IDWriteTextAnalysisSource](https://msdn.microsoft.com/en-us/library/windows/desktop/dd371318.aspx) | Introduced in 10.0.10240. |
| [IDWriteTextAnalysisSource1](https://msdn.microsoft.com/en-us/library/windows/desktop/hh780426.aspx) | Introduced in 10.0.10240. |
| [IDWriteTextAnalyzer](https://msdn.microsoft.com/en-us/library/windows/desktop/dd316607.aspx) | Introduced in 10.0.10240. |
| [IDWriteTextAnalyzer1](https://msdn.microsoft.com/en-us/library/windows/desktop/hh780428.aspx) | Introduced in 10.0.10240. |
| [IDWriteTextAnalyzer2](https://msdn.microsoft.com/en-us/library/windows/desktop/dn280483.aspx) | Introduced in 10.0.10240. |
| [IDWriteTextFormat](https://msdn.microsoft.com/en-us/library/windows/desktop/dd316628.aspx) | Introduced in 10.0.10240. |
| [IDWriteTextFormat1](https://msdn.microsoft.com/en-us/library/windows/desktop/dn280485.aspx) | Introduced in 10.0.10240. |
| [IDWriteTextFormat2](https://msdn.microsoft.com/en-us/library/windows/desktop/mt574121.aspx) | Introduced in 10.0.10240. |
| [IDWriteTextLayout](https://msdn.microsoft.com/en-us/library/windows/desktop/dd316718.aspx) | Introduced in 10.0.10240. |
| [IDWriteTextLayout1](https://msdn.microsoft.com/en-us/library/windows/desktop/hh780438.aspx) | Introduced in 10.0.10240. |
| [IDWriteTextLayout2](https://msdn.microsoft.com/en-us/library/windows/desktop/dn280491.aspx) | Introduced in 10.0.10240. |
| [IDWriteTextLayout3](https://msdn.microsoft.com/en-us/library/windows/desktop/dn900405.aspx) | Introduced in 10.0.10240. |
| [IDWriteTextRenderer](https://msdn.microsoft.com/en-us/library/windows/desktop/dd371523.aspx) | Introduced in 10.0.10240. |
| [IDWriteTextRenderer1](https://msdn.microsoft.com/en-us/library/windows/desktop/dn280513.aspx) | Introduced in 10.0.10240. |
| [IDWriteTypography](https://msdn.microsoft.com/en-us/library/windows/desktop/dd371541.aspx) | Introduced in 10.0.10240. |
| [IDXGIAdapter](https://msdn.microsoft.com/en-us/library/windows/desktop/bb174523.aspx) | Introduced in 10.0.10240. |
| [IDXGIAdapter1](https://msdn.microsoft.com/en-us/library/windows/desktop/ff471329.aspx) | Introduced in 10.0.10240. |
| [IDXGIAdapter2](https://msdn.microsoft.com/en-us/library/windows/desktop/hh404537.aspx) | Introduced in 10.0.10240. |
| [IDXGIAdapter3](https://msdn.microsoft.com/en-us/library/windows/desktop/dn933221.aspx) | Introduced in 10.0.10240. |
| [IDXGIDebug](https://msdn.microsoft.com/en-us/library/windows/desktop/hh780351.aspx) | Introduced in 10.0.10240. |
| [IDXGIDebug1](https://msdn.microsoft.com/en-us/library/windows/desktop/dn457938.aspx) | Introduced in 10.0.10240. |
| [IDXGIDevice](https://msdn.microsoft.com/en-us/library/windows/desktop/bb174527.aspx) | Introduced in 10.0.10240. |
| [IDXGIDevice1](https://msdn.microsoft.com/en-us/library/windows/desktop/ff471331.aspx) | Introduced in 10.0.10240. |
| [IDXGIDevice2](https://msdn.microsoft.com/en-us/library/windows/desktop/hh404543.aspx) | Introduced in 10.0.10240. |
| [IDXGIDevice3](https://msdn.microsoft.com/en-us/library/windows/desktop/dn280345.aspx) | Introduced in 10.0.10240. |
| [IDXGIDeviceSubObject](https://msdn.microsoft.com/en-us/library/windows/desktop/bb174528.aspx) | Introduced in 10.0.10240. |
| [IDXGIFactory](https://msdn.microsoft.com/en-us/library/windows/desktop/bb174535.aspx) | Introduced in 10.0.10240. |
| [IDXGIFactory1](https://msdn.microsoft.com/en-us/library/windows/desktop/ff471335.aspx) | Introduced in 10.0.10240. |
| [IDXGIFactory2](https://msdn.microsoft.com/en-us/library/windows/desktop/hh404556.aspx) | Introduced in 10.0.10240. |
| [IDXGIFactory3](https://msdn.microsoft.com/en-us/library/windows/desktop/dn457942.aspx) | Introduced in 10.0.10240. |
| [IDXGIFactory4](https://msdn.microsoft.com/en-us/library/windows/desktop/mt427785.aspx) | Introduced in 10.0.10240. |
| [IDXGIInfoQueue](https://msdn.microsoft.com/en-us/library/windows/desktop/hh780355.aspx) | Introduced in 10.0.10240. |
| [IDXGIKeyedMutex](https://msdn.microsoft.com/en-us/library/windows/desktop/ff471338.aspx) | Introduced in 10.0.10240. |
| [IDXGIObject](https://msdn.microsoft.com/en-us/library/windows/desktop/bb174541.aspx) | Introduced in 10.0.10240. |
| [IDXGIOutput](https://msdn.microsoft.com/en-us/library/windows/desktop/bb174546.aspx) | Introduced in 10.0.10240. |
| [IDXGIOutput1](https://msdn.microsoft.com/en-us/library/windows/desktop/hh404597.aspx) | Introduced in 10.0.10240. |
| [IDXGIOutput2](https://msdn.microsoft.com/en-us/library/windows/desktop/dn280410.aspx) | Introduced in 10.0.10240. |
| [IDXGIOutput3](https://msdn.microsoft.com/en-us/library/windows/desktop/dn903669.aspx) | Introduced in 10.0.10240. |
| [IDXGIOutput4](https://msdn.microsoft.com/en-us/library/windows/desktop/dn903671.aspx) | Introduced in 10.0.10240. |
| [IDXGIResource](https://msdn.microsoft.com/en-us/library/windows/desktop/bb174560.aspx) | Introduced in 10.0.10240. |
| [IDXGIResource1](https://msdn.microsoft.com/en-us/library/windows/desktop/hh404625.aspx) | Introduced in 10.0.10240. |
| [IDXGISurface](https://msdn.microsoft.com/en-us/library/windows/desktop/bb174565.aspx) | Introduced in 10.0.10240. |
| [IDXGISurface1](https://msdn.microsoft.com/en-us/library/windows/desktop/ff471343.aspx) | Introduced in 10.0.10240. |
| [IDXGISurface2](https://msdn.microsoft.com/en-us/library/windows/desktop/hh404628.aspx) | Introduced in 10.0.10240. |
| [IDXGISwapChain](https://msdn.microsoft.com/en-us/library/windows/desktop/bb174569.aspx) | Introduced in 10.0.10240. |
| [IDXGISwapChain1](https://msdn.microsoft.com/en-us/library/windows/desktop/hh404631.aspx) | Introduced in 10.0.10240. |
| [IDXGISwapChain2](https://msdn.microsoft.com/en-us/library/windows/desktop/dn280420.aspx) | Introduced in 10.0.10240. |
| [IDXGISwapChain3](https://msdn.microsoft.com/en-us/library/windows/desktop/dn903673.aspx) | Introduced in 10.0.10240. |
| [IEditionUpgradeHelper](https://msdn.microsoft.com/en-us/library/Mt459283.aspx) | Introduced in 10.0.10240. |
| [IEnumCodePage](https://msdn.microsoft.com/en-us/library/windows/desktop/aa741101.aspx) | Introduced in 10.0.10240. |
| [IEnumConnectionPoints](https://msdn.microsoft.com/en-us/library/windows/desktop/ms688265.aspx) | Introduced in 10.0.10240. |
| [IEnumConnections](https://msdn.microsoft.com/en-us/library/windows/desktop/ms682237.aspx) | Introduced in 10.0.10240. |
| [IEnumGUID](https://msdn.microsoft.com/en-us/library/windows/desktop/ms682393.aspx) | Introduced in 10.0.10240. |
| [IEnumITfCompositionView](https://msdn.microsoft.com/en-us/library/windows/desktop/ms538115.aspx) | Introduced in 10.0.10240. |
| [IEnumMoniker](https://msdn.microsoft.com/en-us/library/windows/desktop/ms692852.aspx) | Introduced in 10.0.10240. |
| [IEnumPortableDeviceObjectIDs](https://msdn.microsoft.com/en-us/library/windows/desktop/dd319350.aspx) | Introduced in 10.0.10240. |
| [IEnumRfc1766](https://msdn.microsoft.com/en-us/library/windows/desktop/aa741095.aspx) | Introduced in 10.0.10240. |
| [IEnumScript](https://msdn.microsoft.com/en-us/library/windows/desktop/aa741082.aspx) | Introduced in 10.0.10240. |
| [IEnumSpellingError](https://msdn.microsoft.com/en-us/library/windows/desktop/hh869751.aspx) | Introduced in 10.0.10240. |
| [IEnumSTATDATA](https://msdn.microsoft.com/en-us/library/windows/desktop/ms688589.aspx) | Introduced in 10.0.10240. |
| [IEnumSTATPROPSETSTG](https://msdn.microsoft.com/en-us/library/windows/desktop/aa379184.aspx) | Introduced in 10.0.10240. |
| [IEnumSTATPROPSTG](https://msdn.microsoft.com/en-us/library/windows/desktop/aa379210.aspx) | Introduced in 10.0.10240. |
| [IEnumSTATSTG](https://msdn.microsoft.com/en-us/library/windows/desktop/aa379217.aspx) | Introduced in 10.0.10240. |
| [IEnumString](https://msdn.microsoft.com/en-us/library/windows/desktop/ms687257.aspx) | Introduced in 10.0.10240. |
| [IEnumTfCandidates](https://msdn.microsoft.com/en-us/library/windows/desktop/ms538125.aspx) | Introduced in 10.0.10240. |
| [IEnumTfContexts](https://msdn.microsoft.com/en-us/library/windows/desktop/ms538135.aspx) | Introduced in 10.0.10240. |
| [IEnumTfContextViews](https://msdn.microsoft.com/en-us/library/windows/desktop/ms538144.aspx) | Introduced in 10.0.10240. |
| [IEnumTfDisplayAttributeInfo](https://msdn.microsoft.com/en-us/library/windows/desktop/ms538154.aspx) | Introduced in 10.0.10240. |
| [IEnumTfDocumentMgrs](https://msdn.microsoft.com/en-us/library/windows/desktop/ms538164.aspx) | Introduced in 10.0.10240. |
| [IEnumTfFunctionProviders](https://msdn.microsoft.com/en-us/library/windows/desktop/ms538172.aspx) | Introduced in 10.0.10240. |
| [IEnumTfInputProcessorProfiles](https://msdn.microsoft.com/en-us/library/windows/desktop/aa380591.aspx) | Introduced in 10.0.10240. |
| [IEnumTfProperties](https://msdn.microsoft.com/en-us/library/windows/desktop/ms538218.aspx) | Introduced in 10.0.10240. |
| [IEnumTfPropertyValue](https://msdn.microsoft.com/en-us/library/windows/desktop/ms538230.aspx) | Introduced in 10.0.10240. |
| [IEnumTfRanges](https://msdn.microsoft.com/en-us/library/windows/desktop/ms538241.aspx) | Introduced in 10.0.10240. |
| [IEnumTfUIElements](https://msdn.microsoft.com/en-us/library/windows/desktop/aa380866.aspx) | Introduced in 10.0.10240. |
| [IEnumUnknown](https://msdn.microsoft.com/en-us/library/windows/desktop/ms683764.aspx) | Introduced in 10.0.10240. |
| [IEnumVARIANT](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221053.aspx) | Introduced in 10.0.10240. |
| [IExpandCollapseProvider](https://msdn.microsoft.com/en-us/library/windows/desktop/ee671242.aspx) | Introduced in 10.0.10240. |
| [IFillLockBytes](https://msdn.microsoft.com/en-us/library/windows/desktop/aa379224.aspx) | Introduced in 10.0.10240. |
| [IFindReferenceTargetsCallback](https://msdn.microsoft.com/en-us/library/windows/desktop/jj542493.aspx) | Introduced in 10.0.10240. |
| [IGlobalInterfaceTable](https://msdn.microsoft.com/en-us/library/windows/desktop/ms678517.aspx) | Introduced in 10.0.10240. |
| [IGlobalOptions](https://msdn.microsoft.com/en-us/library/windows/desktop/aa344211.aspx) | Introduced in 10.0.10240. |
| [IGridItemProvider](https://msdn.microsoft.com/en-us/library/windows/desktop/ee671246.aspx) | Introduced in 10.0.10240. |
| [IGridProvider](https://msdn.microsoft.com/en-us/library/windows/desktop/ee671252.aspx) | Introduced in 10.0.10240. |
| [IInkD2DRenderer](https://msdn.microsoft.com/en-us/library/Mt147263.aspx) | Introduced in 10.0.10240. |
| [IInspectable](https://msdn.microsoft.com/en-us/library/windows/desktop/br205821.aspx) | Introduced in 10.0.10240. |
| [IInvokeProvider](https://msdn.microsoft.com/en-us/library/windows/desktop/ee671256.aspx) | Introduced in 10.0.10240. |
| [IItemContainerProvider](https://msdn.microsoft.com/en-us/library/windows/desktop/ee671258.aspx) | Introduced in 10.0.10240. |
| [ILanguageExceptionErrorInfo](https://msdn.microsoft.com/en-us/library/windows/desktop/dn302120.aspx) | Introduced in 10.0.10240. |
| [ILayoutStorage](https://msdn.microsoft.com/en-us/library/windows/desktop/aa379232.aspx) | Introduced in 10.0.10240. |
| [ILegacyIAccessibleProvider](https://msdn.microsoft.com/en-us/library/windows/desktop/ee671260.aspx) | Introduced in 10.0.10240. |
| [ILockBytes](https://msdn.microsoft.com/en-us/library/windows/desktop/aa379238.aspx) | Introduced in 10.0.10240. |
| [IMarshal](https://msdn.microsoft.com/en-us/library/windows/desktop/ms688712.aspx) | Introduced in 10.0.10240. |
| [IMbnConnection](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430368.aspx) | Introduced in 10.0.10240. |
| [IMbnConnectionEvents](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430375.aspx) | Introduced in 10.0.10240. |
| [IMbnConnectionManager](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430380.aspx) | Introduced in 10.0.10240. |
| [IMbnConnectionManagerEvents](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430381.aspx) | Introduced in 10.0.10240. |
| [IMbnDeviceService](https://msdn.microsoft.com/en-us/library/windows/desktop/hh780509.aspx) | Introduced in 10.0.10240. |
| [IMbnDeviceServicesContext](https://msdn.microsoft.com/en-us/library/windows/desktop/hh780510.aspx) | Introduced in 10.0.10240. |
| [IMbnDeviceServicesEvents](https://msdn.microsoft.com/en-us/library/windows/desktop/hh780515.aspx) | Introduced in 10.0.10240. |
| [IMbnDeviceServicesManager](https://msdn.microsoft.com/en-us/library/windows/desktop/hh780527.aspx) | Introduced in 10.0.10240. |
| [IMbnInterface](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430406.aspx) | Introduced in 10.0.10240. |
| [IMbnInterfaceEvents](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430407.aspx) | Introduced in 10.0.10240. |
| [IMbnInterfaceManager](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430416.aspx) | Introduced in 10.0.10240. |
| [IMbnInterfaceManagerEvents](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430417.aspx) | Introduced in 10.0.10240. |
| [IMbnPin](https://msdn.microsoft.com/en-us/library/windows/desktop/dd323109.aspx) | Introduced in 10.0.10240. |
| [IMbnPinEvents](https://msdn.microsoft.com/en-us/library/windows/desktop/dd323110.aspx) | Introduced in 10.0.10240. |
| [IMbnPinManager](https://msdn.microsoft.com/en-us/library/windows/desktop/dd323117.aspx) | Introduced in 10.0.10240. |
| [IMbnPinManagerEvents](https://msdn.microsoft.com/en-us/library/windows/desktop/dd323118.aspx) | Introduced in 10.0.10240. |
| [IMbnRegistration](https://msdn.microsoft.com/en-us/library/windows/desktop/dd323142.aspx) | Introduced in 10.0.10240. |
| [IMbnRegistrationEvents](https://msdn.microsoft.com/en-us/library/windows/desktop/dd323143.aspx) | Introduced in 10.0.10240. |
| [IMetaDataAssemblyImport](https://msdn.microsoft.com/en-us/library/windows/desktop/hh870550.aspx) | Introduced in 10.0.10240. |
| [IMetaDataDispenser](https://msdn.microsoft.com/en-us/library/windows/desktop/hh870566.aspx) | Introduced in 10.0.10240. |
| [IMetaDataDispenserEx](https://msdn.microsoft.com/en-us/library/windows/desktop/hh870567.aspx) | Introduced in 10.0.10240. |
| [IMetaDataImport](https://msdn.microsoft.com/en-us/library/windows/desktop/hh870577.aspx) | Introduced in 10.0.10240. |
| [IMetaDataImport2](https://msdn.microsoft.com/en-us/library/windows/desktop/hh870578.aspx) | Introduced in 10.0.10240. |
| [IMetaDataTables](https://msdn.microsoft.com/en-us/library/windows/desktop/hh870643.aspx) | Introduced in 10.0.10240. |
| [IMetaDataTables2](https://msdn.microsoft.com/en-us/library/windows/desktop/hh870644.aspx) | Introduced in 10.0.10240. |
| [IMF2DBuffer](https://msdn.microsoft.com/en-us/library/windows/desktop/ms699894.aspx) | Introduced in 10.0.10240. |
| [IMF2DBuffer2](https://msdn.microsoft.com/en-us/library/windows/desktop/hh447827.aspx) | Introduced in 10.0.10240. |
| [IMFActivate](https://msdn.microsoft.com/en-us/library/windows/desktop/ms703039.aspx) | Introduced in 10.0.10240. |
| [IMFAsyncCallback](https://msdn.microsoft.com/en-us/library/windows/desktop/ms699856.aspx) | Introduced in 10.0.10240. |
| [IMFAsyncResult](https://msdn.microsoft.com/en-us/library/windows/desktop/ms700196.aspx) | Introduced in 10.0.10240. |
| [IMFAttributes](https://msdn.microsoft.com/en-us/library/windows/desktop/ms704598.aspx) | Introduced in 10.0.10240. |
| [IMFByteStream](https://msdn.microsoft.com/en-us/library/windows/desktop/ms698720.aspx) | Introduced in 10.0.10240. |
| [IMFByteStreamBuffering](https://msdn.microsoft.com/en-us/library/windows/desktop/aa372548.aspx) | Introduced in 10.0.10240. |
| [IMFByteStreamCacheControl](https://msdn.microsoft.com/en-us/library/windows/desktop/dd368785.aspx) | Introduced in 10.0.10240. |
| [IMFByteStreamCacheControl2](https://msdn.microsoft.com/en-us/library/windows/desktop/hh447830.aspx) | Introduced in 10.0.10240. |
| [IMFByteStreamTimeSeek](https://msdn.microsoft.com/en-us/library/windows/desktop/hh447836.aspx) | Introduced in 10.0.10240. |
| [IMFClock](https://msdn.microsoft.com/en-us/library/windows/desktop/ms696248.aspx) | Introduced in 10.0.10240. |
| [IMFClockStateSink](https://msdn.microsoft.com/en-us/library/windows/desktop/ms701593.aspx) | Introduced in 10.0.10240. |
| [IMFCollection](https://msdn.microsoft.com/en-us/library/windows/desktop/ms705661.aspx) | Introduced in 10.0.10240. |
| [IMFContentDecryptorContext](https://msdn.microsoft.com/en-us/library/windows/desktop/mt219182.aspx) | Introduced in 10.0.10240. |
| [IMFContentProtectionDevice](https://msdn.microsoft.com/en-us/library/windows/desktop/mt219184.aspx) | Introduced in 10.0.10240. |
| [IMFDXGIBuffer](https://msdn.microsoft.com/en-us/library/windows/desktop/hh447901.aspx) | Introduced in 10.0.10240. |
| [IMFDXGIDeviceManager](https://msdn.microsoft.com/en-us/library/windows/desktop/hh447906.aspx) | Introduced in 10.0.10240. |
| [IMFDXGIDeviceManagerSource](https://msdn.microsoft.com/en-us/library/windows/desktop/dn280687.aspx) | Introduced in 10.0.10240. |
| [IMFGetService](https://msdn.microsoft.com/en-us/library/windows/desktop/ms694261.aspx) | Introduced in 10.0.10240. |
| [IMFInputTrustAuthority](https://msdn.microsoft.com/en-us/library/windows/desktop/ms697500.aspx) | Introduced in 10.0.10240. |
| [IMFMediaBuffer](https://msdn.microsoft.com/en-us/library/windows/desktop/ms696261.aspx) | Introduced in 10.0.10240. |
| [IMFMediaEngine](https://msdn.microsoft.com/en-us/library/windows/desktop/hh447918.aspx) | Introduced in 10.0.10240. |
| [IMFMediaEngineClassFactory](https://msdn.microsoft.com/en-us/library/windows/desktop/hh447919.aspx) | Introduced in 10.0.10240. |
| [IMFMediaEngineEx](https://msdn.microsoft.com/en-us/library/windows/desktop/hh447923.aspx) | Introduced in 10.0.10240. |
| [IMFMediaEngineExtension](https://msdn.microsoft.com/en-us/library/windows/desktop/hh447924.aspx) | Introduced in 10.0.10240. |
| [IMFMediaEngineNotify](https://msdn.microsoft.com/en-us/library/windows/desktop/hh447962.aspx) | Introduced in 10.0.10240. |
| [IMFMediaEngineProtectedContent](https://msdn.microsoft.com/en-us/library/windows/desktop/hh447964.aspx) | Introduced in 10.0.10240. |
| [IMFMediaEngineSrcElements](https://msdn.microsoft.com/en-us/library/windows/desktop/hh447971.aspx) | Introduced in 10.0.10240. |
| [IMFMediaError](https://msdn.microsoft.com/en-us/library/windows/desktop/hh448022.aspx) | Introduced in 10.0.10240. |
| [IMFMediaEvent](https://msdn.microsoft.com/en-us/library/windows/desktop/ms702249.aspx) | Introduced in 10.0.10240. |
| [IMFMediaEventGenerator](https://msdn.microsoft.com/en-us/library/windows/desktop/ms701755.aspx) | Introduced in 10.0.10240. |
| [IMFMediaEventQueue](https://msdn.microsoft.com/en-us/library/windows/desktop/ms704617.aspx) | Introduced in 10.0.10240. |
| [IMFMediaSink](https://msdn.microsoft.com/en-us/library/windows/desktop/ms694262.aspx) | Introduced in 10.0.10240. |
| [IMFMediaSinkPreroll](https://msdn.microsoft.com/en-us/library/windows/desktop/ms699832.aspx) | Introduced in 10.0.10240. |
| [IMFMediaSource](https://msdn.microsoft.com/en-us/library/windows/desktop/ms700189.aspx) | Introduced in 10.0.10240. |
| [IMFMediaSourceEx](https://msdn.microsoft.com/en-us/library/windows/desktop/hh448029.aspx) | Introduced in 10.0.10240. |
| [IMFMediaStream](https://msdn.microsoft.com/en-us/library/windows/desktop/ms697561.aspx) | Introduced in 10.0.10240. |
| [IMFMediaStreamSourceSampleRequest](https://msdn.microsoft.com/en-us/library/windows/desktop/dn280741.aspx) | Introduced in 10.0.10240. |
| [IMFMediaTimeRange](https://msdn.microsoft.com/en-us/library/windows/desktop/hh448033.aspx) | Introduced in 10.0.10240. |
| [IMFMediaType](https://msdn.microsoft.com/en-us/library/windows/desktop/ms704850.aspx) | Introduced in 10.0.10240. |
| [IMFMediaTypeHandler](https://msdn.microsoft.com/en-us/library/windows/desktop/ms697311.aspx) | Introduced in 10.0.10240. |
| [IMFMetadata](https://msdn.microsoft.com/en-us/library/windows/desktop/ms696970.aspx) | Introduced in 10.0.10240. |
| [IMFMetadataProvider](https://msdn.microsoft.com/en-us/library/windows/desktop/ms705606.aspx) | Introduced in 10.0.10240. |
| [IMFOutputPolicy](https://msdn.microsoft.com/en-us/library/windows/desktop/ms698985.aspx) | Introduced in 10.0.10240. |
| [IMFOutputSchema](https://msdn.microsoft.com/en-us/library/windows/desktop/ms703800.aspx) | Introduced in 10.0.10240. |
| [IMFOutputTrustAuthority](https://msdn.microsoft.com/en-us/library/windows/desktop/ms695254.aspx) | Introduced in 10.0.10240. |
| [IMFPMPClientApp](https://msdn.microsoft.com/en-us/library/windows/desktop/jj128316.aspx) | Introduced in 10.0.10240. |
| [IMFPMPHostApp](https://msdn.microsoft.com/en-us/library/windows/desktop/jj128318.aspx) | Introduced in 10.0.10240. |
| [IMFPresentationClock](https://msdn.microsoft.com/en-us/library/windows/desktop/ms701581.aspx) | Introduced in 10.0.10240. |
| [IMFPresentationDescriptor](https://msdn.microsoft.com/en-us/library/windows/desktop/ms703990.aspx) | Introduced in 10.0.10240. |
| [IMFPresentationTimeSource](https://msdn.microsoft.com/en-us/library/windows/desktop/ms704711.aspx) | Introduced in 10.0.10240. |
| [IMFProtectedEnvironmentAccess](https://msdn.microsoft.com/en-us/library/windows/desktop/hh448045.aspx) | Introduced in 10.0.10240. |
| [IMFQualityAdvise](https://msdn.microsoft.com/en-us/library/windows/desktop/ms695241.aspx) | Introduced in 10.0.10240. |
| [IMFQualityAdvise2](https://msdn.microsoft.com/en-us/library/windows/desktop/dd743249.aspx) | Introduced in 10.0.10240. |
| [IMFQualityAdviseLimits](https://msdn.microsoft.com/en-us/library/windows/desktop/dd374511.aspx) | Introduced in 10.0.10240. |
| [IMFRateControl](https://msdn.microsoft.com/en-us/library/windows/desktop/ms697193.aspx) | Introduced in 10.0.10240. |
| [IMFRateSupport](https://msdn.microsoft.com/en-us/library/windows/desktop/ms701858.aspx) | Introduced in 10.0.10240. |
| [IMFReadWriteClassFactory](https://msdn.microsoft.com/en-us/library/windows/desktop/dd374514.aspx) | Introduced in 10.0.10240. |
| [IMFRealTimeClientEx](https://msdn.microsoft.com/en-us/library/windows/desktop/hh448047.aspx) | Introduced in 10.0.10240. |
| [IMFSample](https://msdn.microsoft.com/en-us/library/windows/desktop/ms702192.aspx) | Introduced in 10.0.10240. |
| [IMFSampleOutputStream](https://msdn.microsoft.com/en-us/library/windows/desktop/hh448051.aspx) | Introduced in 10.0.10240. |
| [IMFSampleProtection](https://msdn.microsoft.com/en-us/library/windows/desktop/ms703018.aspx) | Introduced in 10.0.10240. |
| [IMFSchemeHandler](https://msdn.microsoft.com/en-us/library/windows/desktop/ms701638.aspx) | Introduced in 10.0.10240. |
| [IMFSeekInfo](https://msdn.microsoft.com/en-us/library/windows/desktop/hh448054.aspx) | Introduced in 10.0.10240. |
| [IMFShutdown](https://msdn.microsoft.com/en-us/library/windows/desktop/ms703054.aspx) | Introduced in 10.0.10240. |
| [IMFSignedLibrary](https://msdn.microsoft.com/en-us/library/windows/desktop/hh448058.aspx) | Introduced in 10.0.10240. |
| [IMFSinkWriter](https://msdn.microsoft.com/en-us/library/windows/desktop/dd374642.aspx) | Introduced in 10.0.10240. |
| [IMFSinkWriterCallback](https://msdn.microsoft.com/en-us/library/windows/desktop/dd374643.aspx) | Introduced in 10.0.10240. |
| [IMFSinkWriterCallback2](https://msdn.microsoft.com/en-us/library/windows/desktop/dn949415.aspx) | Introduced in 10.0.10240. |
| [IMFSinkWriterEx](https://msdn.microsoft.com/en-us/library/windows/desktop/hh448060.aspx) | Introduced in 10.0.10240. |
| [IMFSinkWriterEncoderConfig](https://msdn.microsoft.com/en-us/library/windows/desktop/dn302046.aspx) | Introduced in 10.0.10240. |
| [IMFSourceReader](https://msdn.microsoft.com/en-us/library/windows/desktop/dd374655.aspx) | Introduced in 10.0.10240. |
| [IMFSourceReaderCallback](https://msdn.microsoft.com/en-us/library/windows/desktop/dd374656.aspx) | Introduced in 10.0.10240. |
| [IMFSourceReaderCallback2](https://msdn.microsoft.com/en-us/library/windows/desktop/dn949418.aspx) | Introduced in 10.0.10240. |
| [IMFSourceReaderEx](https://msdn.microsoft.com/en-us/library/windows/desktop/hh448062.aspx) | Introduced in 10.0.10240. |
| [IMFSourceResolver](https://msdn.microsoft.com/en-us/library/windows/desktop/ms694009.aspx) | Introduced in 10.0.10240. |
| [IMFStreamDescriptor](https://msdn.microsoft.com/en-us/library/windows/desktop/ms701622.aspx) | Introduced in 10.0.10240. |
| [IMFStreamingSinkConfig](https://msdn.microsoft.com/en-us/library/windows/desktop/dd374676.aspx) | Introduced in 10.0.10240. |
| [IMFStreamSink](https://msdn.microsoft.com/en-us/library/windows/desktop/ms705657.aspx) | Introduced in 10.0.10240. |
| [IMFSystemId](https://msdn.microsoft.com/en-us/library/windows/desktop/hh448067.aspx) | Introduced in 10.0.10240. |
| [IMFTrackedSample](https://msdn.microsoft.com/en-us/library/windows/desktop/ms697026.aspx) | Introduced in 10.0.10240. |
| [IMFTransform](https://msdn.microsoft.com/en-us/library/windows/desktop/ms696260.aspx) | Introduced in 10.0.10240. |
| [IMFTrustedInput](https://msdn.microsoft.com/en-us/library/windows/desktop/ms697279.aspx) | Introduced in 10.0.10240. |
| [IMFTrustedOutput](https://msdn.microsoft.com/en-us/library/windows/desktop/ms694305.aspx) | Introduced in 10.0.10240. |
| [IMFVideoSampleAllocator](https://msdn.microsoft.com/en-us/library/windows/desktop/aa473823.aspx) | Introduced in 10.0.10240. |
| [IMFVideoSampleAllocatorCallback](https://msdn.microsoft.com/en-us/library/windows/desktop/dd374900.aspx) | Introduced in 10.0.10240. |
| [IMFVideoSampleAllocatorEx](https://msdn.microsoft.com/en-us/library/windows/desktop/hh448076.aspx) | Introduced in 10.0.10240. |
| [IMFVideoSampleAllocatorNotify](https://msdn.microsoft.com/en-us/library/windows/desktop/dd374906.aspx) | Introduced in 10.0.10240. |
| [IMFVideoSampleAllocatorNotifyEx](https://msdn.microsoft.com/en-us/library/windows/desktop/mt627756.aspx) | Introduced in 10.0.10240. |
| [IMFVideoProcessorControl](https://msdn.microsoft.com/en-us/library/windows/desktop/hh448069.aspx) | Introduced in 10.0.10240. |
| [IMFVideoProcessorControl2](https://msdn.microsoft.com/en-us/library/windows/desktop/dn800741.aspx) | Introduced in 10.0.10240. |
| [IMLangConvertCharset](https://msdn.microsoft.com/en-us/library/windows/desktop/aa741058.aspx) | Introduced in 10.0.10240. |
| [IMultiLanguage](https://msdn.microsoft.com/en-us/library/windows/desktop/aa741022.aspx) | Introduced in 10.0.10240. |
| [IMultiLanguage2](https://msdn.microsoft.com/en-us/library/windows/desktop/aa741001.aspx) | Introduced in 10.0.10240. |
| [IMultipleViewProvider](https://msdn.microsoft.com/en-us/library/windows/desktop/ee671296.aspx) | Introduced in 10.0.10240. |
| [IMultiQI](https://msdn.microsoft.com/en-us/library/windows/desktop/ms683863.aspx) | Introduced in 10.0.10240. |
| [INoMarshal](https://msdn.microsoft.com/en-us/library/windows/desktop/hh802477.aspx) | Introduced in 10.0.10240. |
| [IObjectModelProvider](https://msdn.microsoft.com/en-us/library/windows/desktop/hh448776.aspx) | Introduced in 10.0.10240. |
| [IOpcCertificateEnumerator](https://msdn.microsoft.com/en-us/library/windows/desktop/dd368258.aspx) | Introduced in 10.0.10240. |
| [IOpcCertificateSet](https://msdn.microsoft.com/en-us/library/windows/desktop/dd368269.aspx) | Introduced in 10.0.10240. |
| [IOpcDigitalSignature](https://msdn.microsoft.com/en-us/library/windows/desktop/dd368278.aspx) | Introduced in 10.0.10240. |
| [IOpcDigitalSignatureEnumerator](https://msdn.microsoft.com/en-us/library/windows/desktop/dd368280.aspx) | Introduced in 10.0.10240. |
| [IOpcDigitalSignatureManager](https://msdn.microsoft.com/en-us/library/windows/desktop/dd368288.aspx) | Introduced in 10.0.10240. |
| [IOpcFactory](https://msdn.microsoft.com/en-us/library/windows/desktop/dd370991.aspx) | Introduced in 10.0.10240. |
| [IOpcPackage](https://msdn.microsoft.com/en-us/library/windows/desktop/dd371025.aspx) | Introduced in 10.0.10240. |
| [IOpcPart](https://msdn.microsoft.com/en-us/library/windows/desktop/dd371038.aspx) | Introduced in 10.0.10240. |
| [IOpcPartEnumerator](https://msdn.microsoft.com/en-us/library/windows/desktop/dd371043.aspx) | Introduced in 10.0.10240. |
| [IOpcPartSet](https://msdn.microsoft.com/en-us/library/windows/desktop/dd371062.aspx) | Introduced in 10.0.10240. |
| [IOpcPartUri](https://msdn.microsoft.com/en-us/library/windows/desktop/dd371083.aspx) | Introduced in 10.0.10240. |
| [IOpcRelationship](https://msdn.microsoft.com/en-us/library/windows/desktop/dd371131.aspx) | Introduced in 10.0.10240. |
| [IOpcRelationshipEnumerator](https://msdn.microsoft.com/en-us/library/windows/desktop/dd371135.aspx) | Introduced in 10.0.10240. |
| [IOpcRelationshipSelector](https://msdn.microsoft.com/en-us/library/windows/desktop/dd371151.aspx) | Introduced in 10.0.10240. |
| [IOpcRelationshipSelectorEnumerator](https://msdn.microsoft.com/en-us/library/windows/desktop/dd371154.aspx) | Introduced in 10.0.10240. |
| [IOpcRelationshipSelectorSet](https://msdn.microsoft.com/en-us/library/windows/desktop/dd371169.aspx) | Introduced in 10.0.10240. |
| [IOpcRelationshipSet](https://msdn.microsoft.com/en-us/library/windows/desktop/dd371217.aspx) | Introduced in 10.0.10240. |
| [IOpcSignatureCustomObject](https://msdn.microsoft.com/en-us/library/windows/desktop/dd316546.aspx) | Introduced in 10.0.10240. |
| [IOpcSignatureCustomObjectEnumerator](https://msdn.microsoft.com/en-us/library/windows/desktop/dd316548.aspx) | Introduced in 10.0.10240. |
| [IOpcSignatureCustomObjectSet](https://msdn.microsoft.com/en-us/library/windows/desktop/dd316560.aspx) | Introduced in 10.0.10240. |
| [IOpcSignaturePartReference](https://msdn.microsoft.com/en-us/library/windows/desktop/dd316570.aspx) | Introduced in 10.0.10240. |
| [IOpcSignaturePartReferenceEnumerator](https://msdn.microsoft.com/en-us/library/windows/desktop/dd316571.aspx) | Introduced in 10.0.10240. |
| [IOpcSignaturePartReferenceSet](https://msdn.microsoft.com/en-us/library/windows/desktop/dd316585.aspx) | Introduced in 10.0.10240. |
| [IOpcSignatureReference](https://msdn.microsoft.com/en-us/library/windows/desktop/dd316612.aspx) | Introduced in 10.0.10240. |
| [IOpcSignatureReferenceEnumerator](https://msdn.microsoft.com/en-us/library/windows/desktop/dd316615.aspx) | Introduced in 10.0.10240. |
| [IOpcSignatureReferenceSet](https://msdn.microsoft.com/en-us/library/windows/desktop/dd316629.aspx) | Introduced in 10.0.10240. |
| [IOpcSignatureRelationshipReference](https://msdn.microsoft.com/en-us/library/windows/desktop/dd316670.aspx) | Introduced in 10.0.10240. |
| [IOpcSignatureRelationshipReferenceEnumerator](https://msdn.microsoft.com/en-us/library/windows/desktop/dd316673.aspx) | Introduced in 10.0.10240. |
| [IOpcSignatureRelationshipReferenceSet](https://msdn.microsoft.com/en-us/library/windows/desktop/dd316689.aspx) | Introduced in 10.0.10240. |
| [IOpcSigningOptions](https://msdn.microsoft.com/en-us/library/windows/desktop/dd316719.aspx) | Introduced in 10.0.10240. |
| [IOpcUri](https://msdn.microsoft.com/en-us/library/windows/desktop/dd316778.aspx) | Introduced in 10.0.10240. |
| [IOptionDescription](https://msdn.microsoft.com/en-us/library/windows/desktop/hh869762.aspx) | Introduced in 10.0.10240. |
| [IPdfRendererNative](https://msdn.microsoft.com/en-us/library/windows/desktop/dn302125.aspx) | Introduced in 10.0.10240. |
| IPMApplicationInfo | Introduced in 10.0.10240. |
| IPMApplicationInfoEnumerator | Introduced in 10.0.10240. |
| IPMBackgroundServiceAgentInfo | Introduced in 10.0.10240. |
| IPMBackgroundServiceAgentInfoEnumerator | Introduced in 10.0.10240. |
| IPMBackgroundWorkerInfo | Introduced in 10.0.10240. |
| IPMBackgroundWorkerInfoEnumerator | Introduced in 10.0.10240. |
| IPMEnumerationManager | Introduced in 10.0.10240. |
| IPMExtensionCachedFileUpdaterInfo | Introduced in 10.0.10240. |
| IPMExtensionContractInfo | Introduced in 10.0.10240. |
| IPMExtensionFileExtensionInfo | Introduced in 10.0.10240. |
| IPMExtensionFileOpenPickerInfo | Introduced in 10.0.10240. |
| IPMExtensionFileSavePickerInfo | Introduced in 10.0.10240. |
| IPMExtensionInfo | Introduced in 10.0.10240. |
| IPMExtensionInfoEnumerator | Introduced in 10.0.10240. |
| IPMExtensionProtocolInfo | Introduced in 10.0.10240. |
| IPMExtensionShareTargetInfo | Introduced in 10.0.10240. |
| IPMLiveTileJobInfo | Introduced in 10.0.10240. |
| IPMLiveTileJobInfoEnumerator | Introduced in 10.0.10240. |
| IPMTaskInfo | Introduced in 10.0.10240. |
| IPMTaskInfoEnumerator | Introduced in 10.0.10240. |
| IPMTileInfo | Introduced in 10.0.10240. |
| IPMTileInfoEnumerator | Introduced in 10.0.10240. |
| IPMTilePropertyEnumerator | Introduced in 10.0.10240. |
| IPMTilePropertyInfo | Introduced in 10.0.10240. |
| [IPortableDevice](https://msdn.microsoft.com/en-us/library/windows/desktop/dd319361.aspx) | Introduced in 10.0.10240. |
| [IPortableDeviceCapabilities](https://msdn.microsoft.com/en-us/library/windows/desktop/dd319362.aspx) | Introduced in 10.0.10240. |
| [IPortableDeviceContent](https://msdn.microsoft.com/en-us/library/windows/desktop/dd388529.aspx) | Introduced in 10.0.10240. |
| [IPortableDeviceContent2](https://msdn.microsoft.com/en-us/library/windows/desktop/dd388530.aspx) | Introduced in 10.0.10240. |
| [IPortableDeviceDataStream](https://msdn.microsoft.com/en-us/library/windows/desktop/dd388542.aspx) | Introduced in 10.0.10240. |
| [IPortableDeviceDispatchFactory](https://msdn.microsoft.com/en-us/library/windows/desktop/dd389218.aspx) | Introduced in 10.0.10240. |
| [IPortableDeviceEventCallback](https://msdn.microsoft.com/en-us/library/windows/desktop/dd388545.aspx) | Introduced in 10.0.10240. |
| [IPortableDeviceKeyCollection](https://msdn.microsoft.com/en-us/library/windows/desktop/dd388547.aspx) | Introduced in 10.0.10240. |
| [IPortableDeviceManager](https://msdn.microsoft.com/en-us/library/windows/desktop/dd388688.aspx) | Introduced in 10.0.10240. |
| [IPortableDeviceProperties](https://msdn.microsoft.com/en-us/library/windows/desktop/dd388696.aspx) | Introduced in 10.0.10240. |
| [IPortableDevicePropertiesBulk](https://msdn.microsoft.com/en-us/library/windows/desktop/dd388697.aspx) | Introduced in 10.0.10240. |
| [IPortableDevicePropertiesBulkCallback](https://msdn.microsoft.com/en-us/library/windows/desktop/dd388698.aspx) | Introduced in 10.0.10240. |
| [IPortableDevicePropVariantCollection](https://msdn.microsoft.com/en-us/library/windows/desktop/dd388719.aspx) | Introduced in 10.0.10240. |
| [IPortableDeviceResources](https://msdn.microsoft.com/en-us/library/windows/desktop/dd388733.aspx) | Introduced in 10.0.10240. |
| [IPortableDeviceService](https://msdn.microsoft.com/en-us/library/windows/desktop/dd388753.aspx) | Introduced in 10.0.10240. |
| IPortableDeviceServiceActivation | Introduced in 10.0.10240. |
| [IPortableDeviceServiceCapabilities](https://msdn.microsoft.com/en-us/library/windows/desktop/dd388755.aspx) | Introduced in 10.0.10240. |
| [IPortableDeviceServiceManager](https://msdn.microsoft.com/en-us/library/windows/desktop/dd319402.aspx) | Introduced in 10.0.10240. |
| [IPortableDeviceServiceMethodCallback](https://msdn.microsoft.com/en-us/library/windows/desktop/dd319411.aspx) | Introduced in 10.0.10240. |
| [IPortableDeviceServiceMethods](https://msdn.microsoft.com/en-us/library/windows/desktop/dd319418.aspx) | Introduced in 10.0.10240. |
| IPortableDeviceServiceOpenCallback | Introduced in 10.0.10240. |
| [IPortableDeviceUnitsStream](https://msdn.microsoft.com/en-us/library/windows/desktop/hh707376.aspx) | Introduced in 10.0.10240. |
| [IPortableDeviceValues](https://msdn.microsoft.com/en-us/library/windows/desktop/dd319461.aspx) | Introduced in 10.0.10240. |
| [IPortableDeviceValuesCollection](https://msdn.microsoft.com/en-us/library/windows/desktop/dd319463.aspx) | Introduced in 10.0.10240. |
| [IPrintDocumentPackageTarget](https://msdn.microsoft.com/en-us/library/windows/desktop/hh448393.aspx) | Introduced in 10.0.10240. |
| [IPrintDocumentPageSource](https://msdn.microsoft.com/en-us/library/windows/desktop/jj710015.aspx) | Introduced in 10.0.10240. |
| [IPrinterBidiSetRequestCallback](https://msdn.microsoft.com/en-us/library/windows/desktop/dn265385.aspx) | Introduced in 10.0.10240. |
| [IPrinterExtensionAsyncOperation](https://msdn.microsoft.com/en-us/library/windows/desktop/dn265387.aspx) | Introduced in 10.0.10240. |
| [IPrinterExtensionContext](https://msdn.microsoft.com/en-us/library/windows/desktop/hh406649.aspx) | Introduced in 10.0.10240. |
| [IPrinterPropertyBag](https://msdn.microsoft.com/en-us/library/windows/desktop/hh439547.aspx) | Introduced in 10.0.10240. |
| [IPrinterQueue](https://msdn.microsoft.com/en-us/library/windows/desktop/hh439635.aspx) | Introduced in 10.0.10240. |
| [IPrinterQueue2](https://msdn.microsoft.com/en-us/library/windows/desktop/dn265389.aspx) | Introduced in 10.0.10240. |
| [IPrinterQueueEvent](https://msdn.microsoft.com/en-us/library/windows/desktop/hh439618.aspx) | Introduced in 10.0.10240. |
| [IPrinterQueueView](https://msdn.microsoft.com/en-us/library/windows/desktop/dn265392.aspx) | Introduced in 10.0.10240. |
| [IPrinterQueueViewEvent](https://msdn.microsoft.com/en-us/library/windows/desktop/dn265393.aspx) | Introduced in 10.0.10240. |
| [IPrintJob](https://msdn.microsoft.com/en-us/library/windows/desktop/dn265396.aspx) | Introduced in 10.0.10240. |
| [IPrintJobCollection](https://msdn.microsoft.com/en-us/library/windows/desktop/dn265397.aspx) | Introduced in 10.0.10240. |
| [IPrintPreviewDxgiPackageTarget](https://msdn.microsoft.com/en-us/library/windows/desktop/jj553554.aspx) | Introduced in 10.0.10240. |
| [IPrintPreviewPageCollection](https://msdn.microsoft.com/en-us/library/windows/desktop/jj710018.aspx) | Introduced in 10.0.10240. |
| [IPrintSchemaAsyncOperation](https://msdn.microsoft.com/en-us/library/windows/desktop/hh451224.aspx) | Introduced in 10.0.10240. |
| [IPrintSchemaAsyncOperationEvent](https://msdn.microsoft.com/en-us/library/windows/desktop/hh451211.aspx) | Introduced in 10.0.10240. |
| [IPrintSchemaCapabilities](https://msdn.microsoft.com/en-us/library/windows/desktop/hh451256.aspx) | Introduced in 10.0.10240. |
| [IPrintSchemaCapabilities2](https://msdn.microsoft.com/en-us/library/Dn465887.aspx) | Introduced in 10.0.10240. |
| [IPrintSchemaDisplayableElement](https://msdn.microsoft.com/en-us/library/windows/desktop/hh451262.aspx) | Introduced in 10.0.10240. |
| [IPrintSchemaElement](https://msdn.microsoft.com/en-us/library/windows/desktop/hh451270.aspx) | Introduced in 10.0.10240. |
| [IPrintSchemaFeature](https://msdn.microsoft.com/en-us/library/windows/desktop/hh451284.aspx) | Introduced in 10.0.10240. |
| [IPrintSchemaNUpOption](https://msdn.microsoft.com/en-us/library/windows/desktop/hh451302.aspx) | Introduced in 10.0.10240. |
| [IPrintSchemaOption](https://msdn.microsoft.com/en-us/library/windows/desktop/hh451335.aspx) | Introduced in 10.0.10240. |
| [IPrintSchemaOptionCollection](https://msdn.microsoft.com/en-us/library/windows/desktop/hh846198.aspx) | Introduced in 10.0.10240. |
| [IPrintSchemaPageImageableSize](https://msdn.microsoft.com/en-us/library/windows/desktop/hh451366.aspx) | Introduced in 10.0.10240. |
| [IPrintSchemaPageMediaSizeOption](https://msdn.microsoft.com/en-us/library/windows/desktop/hh451378.aspx) | Introduced in 10.0.10240. |
| [IPrintSchemaParameterDefinition](https://msdn.microsoft.com/en-us/library/Dn465890.aspx) | Introduced in 10.0.10240. |
| [IPrintSchemaParameterInitializer](https://msdn.microsoft.com/en-us/library/Dn454557.aspx) | Introduced in 10.0.10240. |
| [IPrintSchemaTicket](https://msdn.microsoft.com/en-us/library/windows/desktop/hh451398.aspx) | Introduced in 10.0.10240. |
| [IPrintSchemaTicket2](https://msdn.microsoft.com/en-us/library/Dn454560.aspx) | Introduced in 10.0.10240. |
| IPropertyBag2 | Introduced in 10.0.10240. |
| [IPropertySetStorage](https://msdn.microsoft.com/en-us/library/windows/desktop/aa379840.aspx) | Introduced in 10.0.10240. |
| [IPropertyStorage](https://msdn.microsoft.com/en-us/library/windows/desktop/aa379968.aspx) | Introduced in 10.0.10240. |
| [IPropertyStore](https://msdn.microsoft.com/en-us/library/windows/desktop/bb761474.aspx) | Introduced in 10.0.10240. |
| [IProxyProviderWinEventHandler](https://msdn.microsoft.com/en-us/library/windows/desktop/ee671303.aspx) | Introduced in 10.0.10240. |
| [IProxyProviderWinEventSink](https://msdn.microsoft.com/en-us/library/windows/desktop/ee671305.aspx) | Introduced in 10.0.10240. |
| [IPSFactoryBuffer](https://msdn.microsoft.com/en-us/library/windows/desktop/ms695281.aspx) | Introduced in 10.0.10240. |
| [IQuickActivate](https://msdn.microsoft.com/en-us/library/windows/desktop/ms690146.aspx) | Introduced in 10.0.10240. |
| [IRangeValueProvider](https://msdn.microsoft.com/en-us/library/windows/desktop/ee671309.aspx) | Introduced in 10.0.10240. |
| [IRawElementProviderAdviseEvents](https://msdn.microsoft.com/en-us/library/windows/desktop/ee671317.aspx) | Introduced in 10.0.10240. |
| [IRawElementProviderFragment](https://msdn.microsoft.com/en-us/library/windows/desktop/ee671320.aspx) | Introduced in 10.0.10240. |
| [IRawElementProviderFragmentRoot](https://msdn.microsoft.com/en-us/library/windows/desktop/ee671321.aspx) | Introduced in 10.0.10240. |
| [IRawElementProviderHostingAccessibles](https://msdn.microsoft.com/en-us/library/windows/desktop/hh448785.aspx) | Introduced in 10.0.10240. |
| [IRawElementProviderHwndOverride](https://msdn.microsoft.com/en-us/library/windows/desktop/ee671330.aspx) | Introduced in 10.0.10240. |
| [IRawElementProviderSimple](https://msdn.microsoft.com/en-us/library/windows/desktop/ee671332.aspx) | Introduced in 10.0.10240. |
| [IRawElementProviderSimple2](https://msdn.microsoft.com/en-us/library/windows/desktop/dn302133.aspx) | Introduced in 10.0.10240. |
| [IRawElementProviderWindowlessSite](https://msdn.microsoft.com/en-us/library/windows/desktop/hh448787.aspx) | Introduced in 10.0.10240. |
| [IRDPSRAPIApplication](https://msdn.microsoft.com/en-us/library/windows/desktop/aa373266.aspx) | Introduced in 10.0.10240. |
| [IRDPSRAPIApplicationFilter](https://msdn.microsoft.com/en-us/library/windows/desktop/aa373267.aspx) | Introduced in 10.0.10240. |
| [IRDPSRAPIApplicationList](https://msdn.microsoft.com/en-us/library/windows/desktop/aa373271.aspx) | Introduced in 10.0.10240. |
| [IRDPSRAPIAttendee](https://msdn.microsoft.com/en-us/library/windows/desktop/aa373279.aspx) | Introduced in 10.0.10240. |
| [IRDPSRAPIAttendeeDisconnectInfo](https://msdn.microsoft.com/en-us/library/windows/desktop/aa373280.aspx) | Introduced in 10.0.10240. |
| [IRDPSRAPIAttendeeManager](https://msdn.microsoft.com/en-us/library/windows/desktop/aa373284.aspx) | Introduced in 10.0.10240. |
| [IRDPSRAPIAudioStream](https://msdn.microsoft.com/en-us/library/windows/desktop/dn408582.aspx) | Introduced in 10.0.10240. |
| IRDPSRAPIDebug | Introduced in 10.0.10240. |
| [IRDPSRAPIFrameBuffer](https://msdn.microsoft.com/en-us/library/windows/desktop/dn894394.aspx) | Introduced in 10.0.10240. |
| [IRDPSRAPIInvitation](https://msdn.microsoft.com/en-us/library/windows/desktop/aa373294.aspx) | Introduced in 10.0.10240. |
| [IRDPSRAPIInvitationManager](https://msdn.microsoft.com/en-us/library/windows/desktop/aa373295.aspx) | Introduced in 10.0.10240. |
| [IRDPSRAPIPerfCounterLogger](https://msdn.microsoft.com/en-us/library/windows/desktop/dn408589.aspx) | Introduced in 10.0.10240. |
| [IRDPSRAPIPerfCounterLoggingManager](https://msdn.microsoft.com/en-us/library/windows/desktop/dn408592.aspx) | Introduced in 10.0.10240. |
| [IRDPSRAPISessionProperties](https://msdn.microsoft.com/en-us/library/windows/desktop/aa373305.aspx) | Introduced in 10.0.10240. |
| [IRDPSRAPISharingSession](https://msdn.microsoft.com/en-us/library/windows/desktop/aa373307.aspx) | Introduced in 10.0.10240. |
| [IRDPSRAPISharingSession2](https://msdn.microsoft.com/en-us/library/windows/desktop/dn894401.aspx) | Introduced in 10.0.10240. |
| [IRDPSRAPITcpConnectionInfo](https://msdn.microsoft.com/en-us/library/windows/desktop/aa373321.aspx) | Introduced in 10.0.10240. |
| [IRDPSRAPITransportStream](https://msdn.microsoft.com/en-us/library/windows/desktop/ee620975.aspx) | Introduced in 10.0.10240. |
| [IRDPSRAPITransportStreamBuffer](https://msdn.microsoft.com/en-us/library/windows/desktop/ee620976.aspx) | Introduced in 10.0.10240. |
| [IRDPSRAPITransportStreamEvents](https://msdn.microsoft.com/en-us/library/windows/desktop/ee620984.aspx) | Introduced in 10.0.10240. |
| [IRDPSRAPIViewer](https://msdn.microsoft.com/en-us/library/windows/desktop/aa373327.aspx) | Introduced in 10.0.10240. |
| [IRDPSRAPIVirtualChannel](https://msdn.microsoft.com/en-us/library/windows/desktop/aa373361.aspx) | Introduced in 10.0.10240. |
| [IRDPSRAPIVirtualChannelManager](https://msdn.microsoft.com/en-us/library/windows/desktop/aa373362.aspx) | Introduced in 10.0.10240. |
| [IRDPSRAPIWindow](https://msdn.microsoft.com/en-us/library/windows/desktop/aa373371.aspx) | Introduced in 10.0.10240. |
| [IRDPSRAPIWindowList](https://msdn.microsoft.com/en-us/library/windows/desktop/aa373372.aspx) | Introduced in 10.0.10240. |
| [IRDPViewerInputSink](https://msdn.microsoft.com/en-us/library/windows/desktop/dn408595.aspx) | Introduced in 10.0.10240. |
| [IRDPViewerRenderingSurface](https://msdn.microsoft.com/en-us/library/windows/desktop/hh802746.aspx) | Introduced in 10.0.10240. |
| [IReferenceTracker](https://msdn.microsoft.com/en-us/library/windows/desktop/jj542495.aspx) | Introduced in 10.0.10240. |
| [IReferenceTrackerHost](https://msdn.microsoft.com/en-us/library/windows/desktop/jj542496.aspx) | Introduced in 10.0.10240. |
| [IReferenceTrackerManager](https://msdn.microsoft.com/en-us/library/windows/desktop/jj542503.aspx) | Introduced in 10.0.10240. |
| [IReferenceTrackerTarget](https://msdn.microsoft.com/en-us/library/windows/desktop/jj542508.aspx) | Introduced in 10.0.10240. |
| [IRemoteDesktopClient](https://msdn.microsoft.com/en-us/library/windows/desktop/hh448564.aspx) | Introduced in 10.0.10240. |
| [IRemoteDesktopClientActions](https://msdn.microsoft.com/en-us/library/windows/desktop/hh448581.aspx) | Introduced in 10.0.10240. |
| [IRemoteDesktopClientEvents](https://msdn.microsoft.com/en-us/library/windows/desktop/hh448568.aspx) | Introduced in 10.0.10240. |
| [IRemoteDesktopClientSettings](https://msdn.microsoft.com/en-us/library/windows/desktop/hh448590.aspx) | Introduced in 10.0.10240. |
| [IRestrictedErrorInfo](https://msdn.microsoft.com/en-us/library/windows/desktop/br224587.aspx) | Introduced in 10.0.10240. |
| [IRootStorage](https://msdn.microsoft.com/en-us/library/windows/desktop/aa379987.aspx) | Introduced in 10.0.10240. |
| [IRpcChannelBuffer](https://msdn.microsoft.com/en-us/library/windows/desktop/ms679738.aspx) | Introduced in 10.0.10240. |
| [IRpcStubBuffer](https://msdn.microsoft.com/en-us/library/windows/desktop/ms678504.aspx) | Introduced in 10.0.10240. |
| [IScrollItemProvider](https://msdn.microsoft.com/en-us/library/windows/desktop/ee671338.aspx) | Introduced in 10.0.10240. |
| [IScrollProvider](https://msdn.microsoft.com/en-us/library/windows/desktop/ee671340.aspx) | Introduced in 10.0.10240. |
| [ISelectionItemProvider](https://msdn.microsoft.com/en-us/library/windows/desktop/ee671349.aspx) | Introduced in 10.0.10240. |
| [ISelectionProvider](https://msdn.microsoft.com/en-us/library/windows/desktop/ee671355.aspx) | Introduced in 10.0.10240. |
| [ISequentialStream](https://msdn.microsoft.com/en-us/library/windows/desktop/aa380010.aspx) | Introduced in 10.0.10240. |
| [ISignalableNotifier](https://msdn.microsoft.com/en-us/library/Dn298319.aspx) | Introduced in 10.0.10240. |
| [ISimpleAudioVolume](https://msdn.microsoft.com/en-us/library/windows/desktop/dd316531.aspx) | Introduced in 10.0.10240. |
| [ISoftwareBitmapNative](https://msdn.microsoft.com/en-us/library/windows/desktop/dn878036.aspx) | Introduced in 10.0.10240. |
| [ISoftwareBitmapNativeFactory](https://msdn.microsoft.com/en-us/library/windows/desktop/dn878037.aspx) | Introduced in 10.0.10240. |
| [ISpellChecker](https://msdn.microsoft.com/en-us/library/windows/desktop/hh869767.aspx) | Introduced in 10.0.10240. |
| [ISpellChecker2](https://msdn.microsoft.com/en-us/library/windows/desktop/mt422900.aspx) | Introduced in 10.0.10240. |
| [ISpellCheckerChangedEventHandler](https://msdn.microsoft.com/en-us/library/windows/desktop/hh869768.aspx) | Introduced in 10.0.10240. |
| [ISpellCheckerFactory](https://msdn.microsoft.com/en-us/library/windows/desktop/hh869770.aspx) | Introduced in 10.0.10240. |
| [ISpellingError](https://msdn.microsoft.com/en-us/library/windows/desktop/hh869805.aspx) | Introduced in 10.0.10240. |
| [ISpreadsheetItemProvider](https://msdn.microsoft.com/en-us/library/windows/desktop/hh448790.aspx) | Introduced in 10.0.10240. |
| [ISpreadsheetProvider](https://msdn.microsoft.com/en-us/library/windows/desktop/hh448796.aspx) | Introduced in 10.0.10240. |
| [IStorage](https://msdn.microsoft.com/en-us/library/windows/desktop/aa380015.aspx) | Introduced in 10.0.10240. |
| [IStream](https://msdn.microsoft.com/en-us/library/windows/desktop/aa380034.aspx) | Introduced in 10.0.10240. |
| [IStylesProvider](https://msdn.microsoft.com/en-us/library/windows/desktop/hh448800.aspx) | Introduced in 10.0.10240. |
| [ISurfaceImageSourceManagerNative](https://msdn.microsoft.com/en-us/library/windows/desktop/dn448959.aspx) | Introduced in 10.0.10240. |
| [ISurfaceImageSourceNative](https://msdn.microsoft.com/en-us/library/windows/desktop/hh848322.aspx) | Introduced in 10.0.10240. |
| [ISurfaceImageSourceNativeWithD2D](https://msdn.microsoft.com/en-us/library/windows/desktop/dn302137.aspx) | Introduced in 10.0.10240. |
| [ISurrogate](https://msdn.microsoft.com/en-us/library/windows/desktop/ms695062.aspx) | Introduced in 10.0.10240. |
| [ISwapChainBackgroundPanelNative](https://msdn.microsoft.com/en-us/library/windows/desktop/hh848326.aspx) | Introduced in 10.0.10240. |
| [ISwapChainPanelNative](https://msdn.microsoft.com/en-us/library/windows/desktop/dn302143.aspx) | Introduced in 10.0.10240. |
| [ISwapChainPanelNative2](https://msdn.microsoft.com/en-us/library/windows/desktop/dn858172.aspx) | Introduced in 10.0.10240. |
| [ISynchronizedInputProvider](https://msdn.microsoft.com/en-us/library/windows/desktop/ee671359.aspx) | Introduced in 10.0.10240. |
| [ITableItemProvider](https://msdn.microsoft.com/en-us/library/windows/desktop/ee671362.aspx) | Introduced in 10.0.10240. |
| [ITableProvider](https://msdn.microsoft.com/en-us/library/windows/desktop/ee671365.aspx) | Introduced in 10.0.10240. |
| [ITextChildProvider](https://msdn.microsoft.com/en-us/library/windows/desktop/hh437317.aspx) | Introduced in 10.0.10240. |
| [ITextEditProvider](https://msdn.microsoft.com/en-us/library/windows/desktop/dn302166.aspx) | Introduced in 10.0.10240. |
| [ITextProvider](https://msdn.microsoft.com/en-us/library/windows/desktop/ee671370.aspx) | Introduced in 10.0.10240. |
| [ITextProvider2](https://msdn.microsoft.com/en-us/library/windows/desktop/hh448818.aspx) | Introduced in 10.0.10240. |
| [ITextRangeProvider](https://msdn.microsoft.com/en-us/library/windows/desktop/ee671377.aspx) | Introduced in 10.0.10240. |
| [ITextRangeProvider2](https://msdn.microsoft.com/en-us/library/windows/desktop/dn302169.aspx) | Introduced in 10.0.10240. |
| [ITextStoreACP2](https://msdn.microsoft.com/en-us/library/windows/desktop/jj670566.aspx) | Introduced in 10.0.10240. |
| [ITextStoreACPServices](https://msdn.microsoft.com/en-us/library/windows/desktop/ms538387.aspx) | Introduced in 10.0.10240. |
| [ITextStoreACPSink](https://msdn.microsoft.com/en-us/library/windows/desktop/ms538395.aspx) | Introduced in 10.0.10240. |
| [ITextStoreAnchor](https://msdn.microsoft.com/en-us/library/windows/desktop/ms538453.aspx) | Introduced in 10.0.10240. |
| [ITextStoreAnchorSink](https://msdn.microsoft.com/en-us/library/windows/desktop/ms538454.aspx) | Introduced in 10.0.10240. |
| [ITfCandidateList](https://msdn.microsoft.com/en-us/library/windows/desktop/ms538492.aspx) | Introduced in 10.0.10240. |
| [ITfCandidateListUIElement](https://msdn.microsoft.com/en-us/library/windows/desktop/aa380892.aspx) | Introduced in 10.0.10240. |
| [ITfCandidateListUIElementBehavior](https://msdn.microsoft.com/en-us/library/windows/desktop/aa381004.aspx) | Introduced in 10.0.10240. |
| [ITfCandidateString](https://msdn.microsoft.com/en-us/library/windows/desktop/ms538497.aspx) | Introduced in 10.0.10240. |
| [ITfCategoryMgr](https://msdn.microsoft.com/en-us/library/windows/desktop/ms538500.aspx) | Introduced in 10.0.10240. |
| [ITfCompartment](https://msdn.microsoft.com/en-us/library/windows/desktop/ms538621.aspx) | Introduced in 10.0.10240. |
| [ITfCompartmentEventSink](https://msdn.microsoft.com/en-us/library/windows/desktop/ms538625.aspx) | Introduced in 10.0.10240. |
| [ITfCompartmentMgr](https://msdn.microsoft.com/en-us/library/windows/desktop/ms538631.aspx) | Introduced in 10.0.10240. |
| [ITfComposition](https://msdn.microsoft.com/en-us/library/windows/desktop/ms538653.aspx) | Introduced in 10.0.10240. |
| [ITfCompositionSink](https://msdn.microsoft.com/en-us/library/windows/desktop/ms538654.aspx) | Introduced in 10.0.10240. |
| [ITfCompositionView](https://msdn.microsoft.com/en-us/library/windows/desktop/ms538660.aspx) | Introduced in 10.0.10240. |
| [ITfConfigureSystemKeystrokeFeed](https://msdn.microsoft.com/en-us/library/windows/desktop/ms538692.aspx) | Introduced in 10.0.10240. |
| [ITfContext](https://msdn.microsoft.com/en-us/library/windows/desktop/ms538703.aspx) | Introduced in 10.0.10240. |
| [ITfContextComposition](https://msdn.microsoft.com/en-us/library/windows/desktop/ms538705.aspx) | Introduced in 10.0.10240. |
| [ITfContextOwnerCompositionServices](https://msdn.microsoft.com/en-us/library/windows/desktop/ms538734.aspx) | Introduced in 10.0.10240. |
| [ITfContextOwnerCompositionSink](https://msdn.microsoft.com/en-us/library/windows/desktop/ms538740.aspx) | Introduced in 10.0.10240. |
| [ITfContextOwnerServices](https://msdn.microsoft.com/en-us/library/windows/desktop/ms538750.aspx) | Introduced in 10.0.10240. |
| [ITfContextView](https://msdn.microsoft.com/en-us/library/windows/desktop/ms538779.aspx) | Introduced in 10.0.10240. |
| [ITfDisplayAttributeInfo](https://msdn.microsoft.com/en-us/library/windows/desktop/ms538802.aspx) | Introduced in 10.0.10240. |
| [ITfDisplayAttributeMgr](https://msdn.microsoft.com/en-us/library/windows/desktop/ms538808.aspx) | Introduced in 10.0.10240. |
| [ITfDisplayAttributeNotifySink](https://msdn.microsoft.com/en-us/library/windows/desktop/ms538869.aspx) | Introduced in 10.0.10240. |
| [ITfDisplayAttributeProvider](https://msdn.microsoft.com/en-us/library/windows/desktop/ms538873.aspx) | Introduced in 10.0.10240. |
| [ITfDocumentMgr](https://msdn.microsoft.com/en-us/library/windows/desktop/ms538878.aspx) | Introduced in 10.0.10240. |
| [ITfEditRecord](https://msdn.microsoft.com/en-us/library/windows/desktop/ms538901.aspx) | Introduced in 10.0.10240. |
| [ITfEditSession](https://msdn.microsoft.com/en-us/library/windows/desktop/ms538906.aspx) | Introduced in 10.0.10240. |
| [ITfFnGetSAPIObject](https://msdn.microsoft.com/en-us/library/windows/desktop/ms538932.aspx) | Introduced in 10.0.10240. |
| [ITfFnReconversion](https://msdn.microsoft.com/en-us/library/windows/desktop/ms538970.aspx) | Introduced in 10.0.10240. |
| [ITfFunction](https://msdn.microsoft.com/en-us/library/windows/desktop/ms538978.aspx) | Introduced in 10.0.10240. |
| [ITfFunctionProvider](https://msdn.microsoft.com/en-us/library/windows/desktop/ms538979.aspx) | Introduced in 10.0.10240. |
| [ITfInputProcessorProfileActivationSink](https://msdn.microsoft.com/en-us/library/windows/desktop/aa381928.aspx) | Introduced in 10.0.10240. |
| [ITfInputProcessorProfileMgr](https://msdn.microsoft.com/en-us/library/windows/desktop/aa381941.aspx) | Introduced in 10.0.10240. |
| [ITfInputScope](https://msdn.microsoft.com/en-us/library/windows/desktop/ms628582.aspx) | Introduced in 10.0.10240. |
| [ITfInputScope2](https://msdn.microsoft.com/en-us/library/windows/desktop/aa382054.aspx) | Introduced in 10.0.10240. |
| [ITfKeyEventSink](https://msdn.microsoft.com/en-us/library/windows/desktop/ms628601.aspx) | Introduced in 10.0.10240. |
| [ITfKeystrokeMgr](https://msdn.microsoft.com/en-us/library/windows/desktop/ms628676.aspx) | Introduced in 10.0.10240. |
| [ITfKeyTraceEventSink](https://msdn.microsoft.com/en-us/library/windows/desktop/ms628691.aspx) | Introduced in 10.0.10240. |
| [ITfLanguageProfileNotifySink](https://msdn.microsoft.com/en-us/library/windows/desktop/ms628769.aspx) | Introduced in 10.0.10240. |
| [ITfPersistentPropertyLoaderACP](https://msdn.microsoft.com/en-us/library/windows/desktop/ms628877.aspx) | Introduced in 10.0.10240. |
| [ITfPreservedKeyNotifySink](https://msdn.microsoft.com/en-us/library/windows/desktop/ms628879.aspx) | Introduced in 10.0.10240. |
| [ITfProperty](https://msdn.microsoft.com/en-us/library/windows/desktop/ms628891.aspx) | Introduced in 10.0.10240. |
| [ITfPropertyStore](https://msdn.microsoft.com/en-us/library/windows/desktop/ms628892.aspx) | Introduced in 10.0.10240. |
| [ITfRange](https://msdn.microsoft.com/en-us/library/windows/desktop/ms628908.aspx) | Introduced in 10.0.10240. |
| [ITfRangeACP](https://msdn.microsoft.com/en-us/library/windows/desktop/ms628909.aspx) | Introduced in 10.0.10240. |
| [ITfRangeBackup](https://msdn.microsoft.com/en-us/library/windows/desktop/ms628912.aspx) | Introduced in 10.0.10240. |
| [ITfReadingInformationUIElement](https://msdn.microsoft.com/en-us/library/windows/desktop/aa382576.aspx) | Introduced in 10.0.10240. |
| [ITfReadOnlyProperty](https://msdn.microsoft.com/en-us/library/windows/desktop/ms628936.aspx) | Introduced in 10.0.10240. |
| [ITfSource](https://msdn.microsoft.com/en-us/library/windows/desktop/ms628941.aspx) | Introduced in 10.0.10240. |
| [ITfSourceSingle](https://msdn.microsoft.com/en-us/library/windows/desktop/ms628942.aspx) | Introduced in 10.0.10240. |
| [ITfTextEditSink](https://msdn.microsoft.com/en-us/library/windows/desktop/ms628962.aspx) | Introduced in 10.0.10240. |
| [ITfThreadMgr2](https://msdn.microsoft.com/en-us/library/windows/desktop/hh920960.aspx) | Introduced in 10.0.10240. |
| [ITfUIElement](https://msdn.microsoft.com/en-us/library/windows/desktop/aa383175.aspx) | Introduced in 10.0.10240. |
| [ITfUIElementMgr](https://msdn.microsoft.com/en-us/library/windows/desktop/aa383178.aspx) | Introduced in 10.0.10240. |
| [ITfUIElementSink](https://msdn.microsoft.com/en-us/library/windows/desktop/aa383201.aspx) | Introduced in 10.0.10240. |
| [IThumbnailStreamCache](https://msdn.microsoft.com/en-us/library/windows/desktop/mt438734.aspx) | Introduced in 10.0.10240. |
| [IToggleProvider](https://msdn.microsoft.com/en-us/library/windows/desktop/ee671396.aspx) | Introduced in 10.0.10240. |
| [ITransformProvider](https://msdn.microsoft.com/en-us/library/windows/desktop/ee671399.aspx) | Introduced in 10.0.10240. |
| [ITransformProvider2](https://msdn.microsoft.com/en-us/library/windows/desktop/hh448824.aspx) | Introduced in 10.0.10240. |
| [IUIAnimationInterpolator](https://msdn.microsoft.com/en-us/library/windows/desktop/dd371665.aspx) | Introduced in 10.0.10240. |
| [IUIAnimationInterpolator2](https://msdn.microsoft.com/en-us/library/windows/desktop/hh437121.aspx) | Introduced in 10.0.10240. |
| [IUIAnimationLoopIterationChangeHandler2](https://msdn.microsoft.com/en-us/library/windows/desktop/hh437133.aspx) | Introduced in 10.0.10240. |
| [IUIAnimationManager](https://msdn.microsoft.com/en-us/library/windows/desktop/dd371687.aspx) | Introduced in 10.0.10240. |
| [IUIAnimationManager2](https://msdn.microsoft.com/en-us/library/windows/desktop/hh437135.aspx) | Introduced in 10.0.10240. |
| [IUIAnimationManagerEventHandler](https://msdn.microsoft.com/en-us/library/windows/desktop/dd371690.aspx) | Introduced in 10.0.10240. |
| [IUIAnimationManagerEventHandler2](https://msdn.microsoft.com/en-us/library/windows/desktop/hh437172.aspx) | Introduced in 10.0.10240. |
| [IUIAnimationPrimitiveInterpolation](https://msdn.microsoft.com/en-us/library/windows/desktop/hh437174.aspx) | Introduced in 10.0.10240. |
| [IUIAnimationPriorityComparison](https://msdn.microsoft.com/en-us/library/windows/desktop/dd371757.aspx) | Introduced in 10.0.10240. |
| [IUIAnimationPriorityComparison2](https://msdn.microsoft.com/en-us/library/windows/desktop/hh437176.aspx) | Introduced in 10.0.10240. |
| [IUIAnimationStoryboard](https://msdn.microsoft.com/en-us/library/windows/desktop/dd371761.aspx) | Introduced in 10.0.10240. |
| [IUIAnimationStoryboard2](https://msdn.microsoft.com/en-us/library/windows/desktop/hh437178.aspx) | Introduced in 10.0.10240. |
| [IUIAnimationStoryboardEventHandler](https://msdn.microsoft.com/en-us/library/windows/desktop/dd371764.aspx) | Introduced in 10.0.10240. |
| [IUIAnimationStoryboardEventHandler2](https://msdn.microsoft.com/en-us/library/windows/desktop/hh448599.aspx) | Introduced in 10.0.10240. |
| [IUIAnimationTimer](https://msdn.microsoft.com/en-us/library/windows/desktop/dd371831.aspx) | Introduced in 10.0.10240. |
| [IUIAnimationTimerClientEventHandler](https://msdn.microsoft.com/en-us/library/windows/desktop/dd371834.aspx) | Introduced in 10.0.10240. |
| [IUIAnimationTimerEventHandler](https://msdn.microsoft.com/en-us/library/windows/desktop/dd371841.aspx) | Introduced in 10.0.10240. |
| [IUIAnimationTimerUpdateHandler](https://msdn.microsoft.com/en-us/library/windows/desktop/dd371853.aspx) | Introduced in 10.0.10240. |
| [IUIAnimationTransition](https://msdn.microsoft.com/en-us/library/windows/desktop/dd371887.aspx) | Introduced in 10.0.10240. |
| [IUIAnimationTransition2](https://msdn.microsoft.com/en-us/library/windows/desktop/hh448602.aspx) | Introduced in 10.0.10240. |
| [IUIAnimationTransitionFactory](https://msdn.microsoft.com/en-us/library/windows/desktop/dd371891.aspx) | Introduced in 10.0.10240. |
| [IUIAnimationTransitionFactory2](https://msdn.microsoft.com/en-us/library/windows/desktop/hh448610.aspx) | Introduced in 10.0.10240. |
| [IUIAnimationTransitionLibrary](https://msdn.microsoft.com/en-us/library/windows/desktop/dd371897.aspx) | Introduced in 10.0.10240. |
| [IUIAnimationTransitionLibrary2](https://msdn.microsoft.com/en-us/library/windows/desktop/hh448612.aspx) | Introduced in 10.0.10240. |
| [IUIAnimationVariable](https://msdn.microsoft.com/en-us/library/windows/desktop/dd316797.aspx) | Introduced in 10.0.10240. |
| [IUIAnimationVariable2](https://msdn.microsoft.com/en-us/library/windows/desktop/hh448632.aspx) | Introduced in 10.0.10240. |
| [IUIAnimationVariableChangeHandler](https://msdn.microsoft.com/en-us/library/windows/desktop/dd316806.aspx) | Introduced in 10.0.10240. |
| [IUIAnimationVariableChangeHandler2](https://msdn.microsoft.com/en-us/library/windows/desktop/hh448659.aspx) | Introduced in 10.0.10240. |
| [IUIAnimationVariableCurveChangeHandler2](https://msdn.microsoft.com/en-us/library/windows/desktop/hh448661.aspx) | Introduced in 10.0.10240. |
| [IUIAnimationVariableIntegerChangeHandler](https://msdn.microsoft.com/en-us/library/windows/desktop/dd316819.aspx) | Introduced in 10.0.10240. |
| [IUIAnimationVariableIntegerChangeHandler2](https://msdn.microsoft.com/en-us/library/windows/desktop/hh448663.aspx) | Introduced in 10.0.10240. |
| [IUIAutomationPatternHandler](https://msdn.microsoft.com/en-us/library/windows/desktop/ee696113.aspx) | Introduced in 10.0.10240. |
| [IUIAutomationPatternInstance](https://msdn.microsoft.com/en-us/library/windows/desktop/ee696116.aspx) | Introduced in 10.0.10240. |
| [IUIAutomationRegistrar](https://msdn.microsoft.com/en-us/library/windows/desktop/ee696161.aspx) | Introduced in 10.0.10240. |
| [IUnknown](https://msdn.microsoft.com/en-us/library/windows/desktop/ms680509.aspx) | Introduced in 10.0.10240. |
| [IValueProvider](https://msdn.microsoft.com/en-us/library/windows/desktop/ee671565.aspx) | Introduced in 10.0.10240. |
| [IVideoFrameNative](https://msdn.microsoft.com/en-us/library/windows/desktop/mt431704.aspx) | Introduced in 10.0.10240. |
| [IVideoFrameNativeFactory](https://msdn.microsoft.com/en-us/library/windows/desktop/mt431705.aspx) | Introduced in 10.0.10240. |
| [IVirtualizedItemProvider](https://msdn.microsoft.com/en-us/library/windows/desktop/ee671569.aspx) | Introduced in 10.0.10240. |
| [IVirtualSurfaceImageSourceNative](https://msdn.microsoft.com/en-us/library/windows/desktop/hh848328.aspx) | Introduced in 10.0.10240. |
| [IVirtualSurfaceUpdatesCallbackNative](https://msdn.microsoft.com/en-us/library/windows/desktop/hh848336.aspx) | Introduced in 10.0.10240. |
| [IWeakReference](https://msdn.microsoft.com/en-us/library/windows/desktop/br224608.aspx) | Introduced in 10.0.10240. |
| [IWeakReferenceSource](https://msdn.microsoft.com/en-us/library/windows/desktop/br224609.aspx) | Introduced in 10.0.10240. |
| [IWICBitmap](https://msdn.microsoft.com/en-us/library/windows/desktop/ee719675.aspx) | Introduced in 10.0.10240. |
| [IWICBitmapClipper](https://msdn.microsoft.com/en-us/library/windows/desktop/ee719676.aspx) | Introduced in 10.0.10240. |
| [IWICBitmapCodecInfo](https://msdn.microsoft.com/en-us/library/windows/desktop/ee719679.aspx) | Introduced in 10.0.10240. |
| [IWICBitmapCodecProgressNotification](https://msdn.microsoft.com/en-us/library/windows/desktop/ee690084.aspx) | Introduced in 10.0.10240. |
| [IWICBitmapDecoder](https://msdn.microsoft.com/en-us/library/windows/desktop/ee690086.aspx) | Introduced in 10.0.10240. |
| [IWICBitmapDecoderInfo](https://msdn.microsoft.com/en-us/library/windows/desktop/ee690087.aspx) | Introduced in 10.0.10240. |
| [IWICBitmapEncoder](https://msdn.microsoft.com/en-us/library/windows/desktop/ee690110.aspx) | Introduced in 10.0.10240. |
| [IWICBitmapEncoderInfo](https://msdn.microsoft.com/en-us/library/windows/desktop/ee690112.aspx) | Introduced in 10.0.10240. |
| [IWICBitmapFlipRotator](https://msdn.microsoft.com/en-us/library/windows/desktop/ee690131.aspx) | Introduced in 10.0.10240. |
| [IWICBitmapFrameDecode](https://msdn.microsoft.com/en-us/library/windows/desktop/ee690134.aspx) | Introduced in 10.0.10240. |
| [IWICBitmapFrameEncode](https://msdn.microsoft.com/en-us/library/windows/desktop/ee690141.aspx) | Introduced in 10.0.10240. |
| [IWICBitmapLock](https://msdn.microsoft.com/en-us/library/windows/desktop/ee690161.aspx) | Introduced in 10.0.10240. |
| [IWICBitmapScaler](https://msdn.microsoft.com/en-us/library/windows/desktop/ee690168.aspx) | Introduced in 10.0.10240. |
| [IWICBitmapSource](https://msdn.microsoft.com/en-us/library/windows/desktop/ee690171.aspx) | Introduced in 10.0.10240. |
| [IWICBitmapSourceTransform](https://msdn.microsoft.com/en-us/library/windows/desktop/ee690172.aspx) | Introduced in 10.0.10240. |
| [IWICColorContext](https://msdn.microsoft.com/en-us/library/windows/desktop/ee690193.aspx) | Introduced in 10.0.10240. |
| [IWICColorTransform](https://msdn.microsoft.com/en-us/library/windows/desktop/ee690201.aspx) | Introduced in 10.0.10240. |
| [IWICComponentFactory](https://msdn.microsoft.com/en-us/library/windows/desktop/ee690203.aspx) | Introduced in 10.0.10240. |
| [IWICComponentInfo](https://msdn.microsoft.com/en-us/library/windows/desktop/ee690213.aspx) | Introduced in 10.0.10240. |
| [IWICDevelopRaw](https://msdn.microsoft.com/en-us/library/windows/desktop/ee690228.aspx) | Introduced in 10.0.10240. |
| [IWICDevelopRawNotificationCallback](https://msdn.microsoft.com/en-us/library/windows/desktop/ee690229.aspx) | Introduced in 10.0.10240. |
| [IWICEnumMetadataItem](https://msdn.microsoft.com/en-us/library/windows/desktop/ee690264.aspx) | Introduced in 10.0.10240. |
| [IWICFastMetadataEncoder](https://msdn.microsoft.com/en-us/library/windows/desktop/ee690269.aspx) | Introduced in 10.0.10240. |
| [IWICFormatConverter](https://msdn.microsoft.com/en-us/library/windows/desktop/ee690274.aspx) | Introduced in 10.0.10240. |
| [IWICFormatConverterInfo](https://msdn.microsoft.com/en-us/library/windows/desktop/ee690275.aspx) | Introduced in 10.0.10240. |
| [IWICImageEncoder](https://msdn.microsoft.com/en-us/library/windows/desktop/hh880844.aspx) | Introduced in 10.0.10240. |
| [IWICImagingFactory](https://msdn.microsoft.com/en-us/library/windows/desktop/ee690281.aspx) | Introduced in 10.0.10240. |
| [IWICImagingFactory2](https://msdn.microsoft.com/en-us/library/windows/desktop/hh880848.aspx) | Introduced in 10.0.10240. |
| [IWICMetadataBlockReader](https://msdn.microsoft.com/en-us/library/windows/desktop/ee690327.aspx) | Introduced in 10.0.10240. |
| [IWICMetadataBlockWriter](https://msdn.microsoft.com/en-us/library/windows/desktop/ee690335.aspx) | Introduced in 10.0.10240. |
| [IWICMetadataHandlerInfo](https://msdn.microsoft.com/en-us/library/windows/desktop/ee719700.aspx) | Introduced in 10.0.10240. |
| [IWICMetadataQueryReader](https://msdn.microsoft.com/en-us/library/windows/desktop/ee719708.aspx) | Introduced in 10.0.10240. |
| [IWICMetadataQueryWriter](https://msdn.microsoft.com/en-us/library/windows/desktop/ee719717.aspx) | Introduced in 10.0.10240. |
| [IWICMetadataReader](https://msdn.microsoft.com/en-us/library/windows/desktop/ee719722.aspx) | Introduced in 10.0.10240. |
| [IWICMetadataReaderInfo](https://msdn.microsoft.com/en-us/library/windows/desktop/ee719723.aspx) | Introduced in 10.0.10240. |
| [IWICMetadataWriter](https://msdn.microsoft.com/en-us/library/windows/desktop/ee719733.aspx) | Introduced in 10.0.10240. |
| [IWICMetadataWriterInfo](https://msdn.microsoft.com/en-us/library/windows/desktop/ee719734.aspx) | Introduced in 10.0.10240. |
| [IWICPalette](https://msdn.microsoft.com/en-us/library/windows/desktop/ee719741.aspx) | Introduced in 10.0.10240. |
| [IWICPersistStream](https://msdn.microsoft.com/en-us/library/windows/desktop/ee719760.aspx) | Introduced in 10.0.10240. |
| [IWICPixelFormatInfo](https://msdn.microsoft.com/en-us/library/windows/desktop/ee719763.aspx) | Introduced in 10.0.10240. |
| [IWICPixelFormatInfo2](https://msdn.microsoft.com/en-us/library/windows/desktop/ee719764.aspx) | Introduced in 10.0.10240. |
| [IWICProgressCallback](https://msdn.microsoft.com/en-us/library/windows/desktop/ee719775.aspx) | Introduced in 10.0.10240. |
| [IWICProgressiveLevelControl](https://msdn.microsoft.com/en-us/library/windows/desktop/ee719778.aspx) | Introduced in 10.0.10240. |
| [IWICStream](https://msdn.microsoft.com/en-us/library/windows/desktop/ee719782.aspx) | Introduced in 10.0.10240. |
| [IWICStreamProvider](https://msdn.microsoft.com/en-us/library/windows/desktop/ee719783.aspx) | Introduced in 10.0.10240. |
| [IWICDdsDecoder](https://msdn.microsoft.com/en-us/library/windows/desktop/dn302079.aspx) | Introduced in 10.0.10240. |
| [IWICDdsEncoder](https://msdn.microsoft.com/en-us/library/windows/desktop/dn302082.aspx) | Introduced in 10.0.10240. |
| [IWICDdsFrameDecode](https://msdn.microsoft.com/en-us/library/windows/desktop/dn302086.aspx) | Introduced in 10.0.10240. |
| [IWICPlanarBitmapFrameEncode](https://msdn.microsoft.com/en-us/library/windows/desktop/dn302090.aspx) | Introduced in 10.0.10240. |
| [IWICPlanarBitmapSourceTransform](https://msdn.microsoft.com/en-us/library/windows/desktop/dn302093.aspx) | Introduced in 10.0.10240. |
| [IWICPlanarFormatConverter](https://msdn.microsoft.com/en-us/library/windows/desktop/dn302096.aspx) | Introduced in 10.0.10240. |
| [IWICJpegFrameDecode](https://msdn.microsoft.com/en-us/library/windows/desktop/dn903834.aspx) | Introduced in 10.0.10240. |
| [IWICJpegFrameEncode](https://msdn.microsoft.com/en-us/library/windows/desktop/dn903864.aspx) | Introduced in 10.0.10240. |
| [IWindowProvider](https://msdn.microsoft.com/en-us/library/windows/desktop/ee671571.aspx) | Introduced in 10.0.10240. |
| [IWindowsDevicesAllJoynBusAttachmentFactoryInterop](https://msdn.microsoft.com/en-us/library/Mt573659.aspx) | Introduced in 10.0.10240. |
| [IWindowsDevicesAllJoynBusAttachmentInterop](https://msdn.microsoft.com/en-us/library/Mt573661.aspx) | Introduced in 10.0.10240. |
| IWorkspaceBrokerAx | Introduced in 10.0.10240. |
| IWorkspaceBrokerAx2 | Introduced in 10.0.10240. |
| [IXAPO](https://msdn.microsoft.com/en-us/library/windows/desktop/microsoft.directx_sdk.ixapo.ixapo.aspx) | Introduced in 10.0.10240. |
| [IXAPOHrtfParameters](https://msdn.microsoft.com/en-us/library/windows/desktop/mt186608.aspx) | Introduced in 10.0.10240. |
| [IXAPOParameters](https://msdn.microsoft.com/en-us/library/windows/desktop/microsoft.directx_sdk.ixapoparameters.ixapoparameters.aspx) | Introduced in 10.0.10240. |
| [IXAudio2](https://msdn.microsoft.com/en-us/library/windows/desktop/microsoft.directx_sdk.ixaudio2.ixaudio2.aspx) | Introduced in 10.0.10240. |
| [IXAudio2EngineCallback](https://msdn.microsoft.com/en-us/library/windows/desktop/microsoft.directx_sdk.ixaudio2enginecallback.ixaudio2enginecallback.aspx) | Introduced in 10.0.10240. |
| [IXAudio2MasteringVoice](https://msdn.microsoft.com/en-us/library/windows/desktop/microsoft.directx_sdk.ixaudio2masteringvoice.ixaudio2masteringvoice.aspx) | Introduced in 10.0.10240. |
| [IXAudio2SourceVoice](https://msdn.microsoft.com/en-us/library/windows/desktop/microsoft.directx_sdk.ixaudio2sourcevoice.ixaudio2sourcevoice.aspx) | Introduced in 10.0.10240. |
| [IXAudio2SubmixVoice](https://msdn.microsoft.com/en-us/library/windows/desktop/microsoft.directx_sdk.ixaudio2submixvoice.ixaudio2submixvoice.aspx) | Introduced in 10.0.10240. |
| [IXAudio2Voice](https://msdn.microsoft.com/en-us/library/windows/desktop/microsoft.directx_sdk.ixaudio2voice.ixaudio2voice.aspx) | Introduced in 10.0.10240. |
| [IXAudio2VoiceCallback](https://msdn.microsoft.com/en-us/library/windows/desktop/microsoft.directx_sdk.ixaudio2voicecallback.ixaudio2voicecallback.aspx) | Introduced in 10.0.10240. |
| [IXMLHTTPRequest2](https://msdn.microsoft.com/en-us/library/windows/desktop/hh831151.aspx) | Introduced in 10.0.10240. |
| [IXMLHTTPRequest2Callback](https://msdn.microsoft.com/en-us/library/windows/desktop/hh831152.aspx) | Introduced in 10.0.10240. |
| [IXMLHTTPRequest3](https://msdn.microsoft.com/en-us/library/windows/desktop/dn376398.aspx) | Introduced in 10.0.10240. |
| [IXMLHTTPRequest3Callback](https://msdn.microsoft.com/en-us/library/windows/desktop/dn376399.aspx) | Introduced in 10.0.10240. |
| [IXmlReader](https://msdn.microsoft.com/en-us/library/windows/desktop/ms752743.aspx) | Introduced in 10.0.10240. |
| [IXmlReaderInput](https://msdn.microsoft.com/en-us/library/windows/desktop/ms752817.aspx) | Introduced in 10.0.10240. |
| [IXmlResolver](https://msdn.microsoft.com/en-us/library/windows/desktop/ms752841.aspx) | Introduced in 10.0.10240. |
| [IXmlWriter](https://msdn.microsoft.com/en-us/library/windows/desktop/ms752860.aspx) | Introduced in 10.0.10240. |
| IXmlWriterLite | Introduced in 10.0.10240. |
| [IXmlWriterOutput](https://msdn.microsoft.com/en-us/library/windows/desktop/ms752843.aspx) | Introduced in 10.0.10240. |
| [IXpsDocumentPackageTarget](https://msdn.microsoft.com/en-us/library/windows/desktop/hh994456.aspx) | Introduced in 10.0.10240. |
| [IXpsDocumentPackageTarget3D](https://msdn.microsoft.com/en-us/library/windows/desktop/dn280684.aspx) | Introduced in 10.0.10240. |
| [IXpsOMBrush](https://msdn.microsoft.com/en-us/library/windows/desktop/dd317026.aspx) | Introduced in 10.0.10240. |
| [IXpsOMCanvas](https://msdn.microsoft.com/en-us/library/windows/desktop/dd317033.aspx) | Introduced in 10.0.10240. |
| [IXpsOMColorProfileResource](https://msdn.microsoft.com/en-us/library/windows/desktop/dd372020.aspx) | Introduced in 10.0.10240. |
| [IXpsOMColorProfileResourceCollection](https://msdn.microsoft.com/en-us/library/windows/desktop/dd372023.aspx) | Introduced in 10.0.10240. |
| [IXpsOMCoreProperties](https://msdn.microsoft.com/en-us/library/windows/desktop/dd372040.aspx) | Introduced in 10.0.10240. |
| [IXpsOMDashCollection](https://msdn.microsoft.com/en-us/library/windows/desktop/dd372105.aspx) | Introduced in 10.0.10240. |
| [IXpsOMDictionary](https://msdn.microsoft.com/en-us/library/windows/desktop/dd372128.aspx) | Introduced in 10.0.10240. |
| [IXpsOMDocument](https://msdn.microsoft.com/en-us/library/windows/desktop/dd372155.aspx) | Introduced in 10.0.10240. |
| [IXpsOMDocumentCollection](https://msdn.microsoft.com/en-us/library/windows/desktop/dd372157.aspx) | Introduced in 10.0.10240. |
| [IXpsOMDocumentSequence](https://msdn.microsoft.com/en-us/library/windows/desktop/dd372363.aspx) | Introduced in 10.0.10240. |
| [IXpsOMDocumentStructureResource](https://msdn.microsoft.com/en-us/library/windows/desktop/dd372377.aspx) | Introduced in 10.0.10240. |
| [IXpsOMFontResource](https://msdn.microsoft.com/en-us/library/windows/desktop/dd372415.aspx) | Introduced in 10.0.10240. |
| [IXpsOMFontResourceCollection](https://msdn.microsoft.com/en-us/library/windows/desktop/dd372419.aspx) | Introduced in 10.0.10240. |
| [IXpsOMGeometry](https://msdn.microsoft.com/en-us/library/windows/desktop/dd372455.aspx) | Introduced in 10.0.10240. |
| [IXpsOMGeometryFigure](https://msdn.microsoft.com/en-us/library/windows/desktop/dd372457.aspx) | Introduced in 10.0.10240. |
| [IXpsOMGeometryFigureCollection](https://msdn.microsoft.com/en-us/library/windows/desktop/dd372461.aspx) | Introduced in 10.0.10240. |
| [IXpsOMGlyphs](https://msdn.microsoft.com/en-us/library/windows/desktop/dd317087.aspx) | Introduced in 10.0.10240. |
| [IXpsOMGlyphsEditor](https://msdn.microsoft.com/en-us/library/windows/desktop/dd317088.aspx) | Introduced in 10.0.10240. |
| [IXpsOMGradientBrush](https://msdn.microsoft.com/en-us/library/windows/desktop/dd317230.aspx) | Introduced in 10.0.10240. |
| [IXpsOMGradientStop](https://msdn.microsoft.com/en-us/library/windows/desktop/dd317250.aspx) | Introduced in 10.0.10240. |
| [IXpsOMGradientStopCollection](https://msdn.microsoft.com/en-us/library/windows/desktop/dd317252.aspx) | Introduced in 10.0.10240. |
| [IXpsOMImageBrush](https://msdn.microsoft.com/en-us/library/windows/desktop/dd317277.aspx) | Introduced in 10.0.10240. |
| [IXpsOMImageResource](https://msdn.microsoft.com/en-us/library/windows/desktop/dd317289.aspx) | Introduced in 10.0.10240. |
| [IXpsOMImageResourceCollection](https://msdn.microsoft.com/en-us/library/windows/desktop/dd317291.aspx) | Introduced in 10.0.10240. |
| [IXpsOMLinearGradientBrush](https://msdn.microsoft.com/en-us/library/windows/desktop/dd317306.aspx) | Introduced in 10.0.10240. |
| [IXpsOMMatrixTransform](https://msdn.microsoft.com/en-us/library/windows/desktop/dd372495.aspx) | Introduced in 10.0.10240. |
| [IXpsOMNameCollection](https://msdn.microsoft.com/en-us/library/windows/desktop/dd372502.aspx) | Introduced in 10.0.10240. |
| [IXpsOMObjectFactory](https://msdn.microsoft.com/en-us/library/windows/desktop/dd372509.aspx) | Introduced in 10.0.10240. |
| [IXpsOMObjectFactory1](https://msdn.microsoft.com/en-us/library/windows/desktop/hh448399.aspx) | Introduced in 10.0.10240. |
| [IXpsOMPackage](https://msdn.microsoft.com/en-us/library/windows/desktop/dd372618.aspx) | Introduced in 10.0.10240. |
| [IXpsOMPackage1](https://msdn.microsoft.com/en-us/library/windows/desktop/hh448410.aspx) | Introduced in 10.0.10240. |
| [IXpsOMPackageTarget](https://msdn.microsoft.com/en-us/library/windows/desktop/ff970304.aspx) | Introduced in 10.0.10240. |
| [IXpsOMPackageWriter](https://msdn.microsoft.com/en-us/library/windows/desktop/dd372619.aspx) | Introduced in 10.0.10240. |
| [IXpsOMPackageWriter3D](https://msdn.microsoft.com/en-us/library/windows/desktop/dn280743.aspx) | Introduced in 10.0.10240. |
| [IXpsOMPage](https://msdn.microsoft.com/en-us/library/windows/desktop/dd372635.aspx) | Introduced in 10.0.10240. |
| [IXpsOMPage1](https://msdn.microsoft.com/en-us/library/windows/desktop/hh448414.aspx) | Introduced in 10.0.10240. |
| [IXpsOMPageReference](https://msdn.microsoft.com/en-us/library/windows/desktop/dd372636.aspx) | Introduced in 10.0.10240. |
| [IXpsOMPageReferenceCollection](https://msdn.microsoft.com/en-us/library/windows/desktop/dd372637.aspx) | Introduced in 10.0.10240. |
| [IXpsOMPart](https://msdn.microsoft.com/en-us/library/windows/desktop/dd372684.aspx) | Introduced in 10.0.10240. |
| [IXpsOMPartResources](https://msdn.microsoft.com/en-us/library/windows/desktop/dd372685.aspx) | Introduced in 10.0.10240. |
| [IXpsOMPartUriCollection](https://msdn.microsoft.com/en-us/library/windows/desktop/dd372690.aspx) | Introduced in 10.0.10240. |
| [IXpsOMPath](https://msdn.microsoft.com/en-us/library/windows/desktop/dd372699.aspx) | Introduced in 10.0.10240. |
| [IXpsOMPrintTicketResource](https://msdn.microsoft.com/en-us/library/windows/desktop/dd372740.aspx) | Introduced in 10.0.10240. |
| [IXpsOMRadialGradientBrush](https://msdn.microsoft.com/en-us/library/windows/desktop/dd372743.aspx) | Introduced in 10.0.10240. |
| [IXpsOMRemoteDictionaryResource](https://msdn.microsoft.com/en-us/library/windows/desktop/dd372751.aspx) | Introduced in 10.0.10240. |
| [IXpsOMRemoteDictionaryResource1](https://msdn.microsoft.com/en-us/library/windows/desktop/jj159899.aspx) | Introduced in 10.0.10240. |
| [IXpsOMRemoteDictionaryResourceCollection](https://msdn.microsoft.com/en-us/library/windows/desktop/dd372752.aspx) | Introduced in 10.0.10240. |
| [IXpsOMResource](https://msdn.microsoft.com/en-us/library/windows/desktop/dd372762.aspx) | Introduced in 10.0.10240. |
| [IXpsOMShareable](https://msdn.microsoft.com/en-us/library/windows/desktop/dd372763.aspx) | Introduced in 10.0.10240. |
| [IXpsOMSignatureBlockResource](https://msdn.microsoft.com/en-us/library/windows/desktop/dd372766.aspx) | Introduced in 10.0.10240. |
| [IXpsOMSignatureBlockResourceCollection](https://msdn.microsoft.com/en-us/library/windows/desktop/dd372767.aspx) | Introduced in 10.0.10240. |
| [IXpsOMSolidColorBrush](https://msdn.microsoft.com/en-us/library/windows/desktop/dd372779.aspx) | Introduced in 10.0.10240. |
| [IXpsOMStoryFragmentsResource](https://msdn.microsoft.com/en-us/library/windows/desktop/dd372783.aspx) | Introduced in 10.0.10240. |
| [IXpsOMTileBrush](https://msdn.microsoft.com/en-us/library/windows/desktop/dd372789.aspx) | Introduced in 10.0.10240. |
| [IXpsOMVisual](https://msdn.microsoft.com/en-us/library/windows/desktop/dd372801.aspx) | Introduced in 10.0.10240. |
| [IXpsOMVisualBrush](https://msdn.microsoft.com/en-us/library/windows/desktop/dd372802.aspx) | Introduced in 10.0.10240. |
| [IXpsOMVisualCollection](https://msdn.microsoft.com/en-us/library/windows/desktop/dd372809.aspx) | Introduced in 10.0.10240. |
| IBtRadioController | Introduced in 10.0.10586. |
| IBtCommandCallback | Introduced in 10.0.10586. |
| IBtConnectionObserver | Introduced in 10.0.10586. |
| IBtConnectionObserverCallback | Introduced in 10.0.10586. |
| IBtConnectionObserverCallback2 | Introduced in 10.0.10586. |
| IBtPairingRequest | Introduced in 10.0.10586. |
| IBtPairingRequestCallback | Introduced in 10.0.10586. |
| IBtIncomingPairingCallback | Introduced in 10.0.10586. |
| [ID3D11Device4](https://msdn.microsoft.com/en-us/library/windows/desktop/mt589889.aspx) | Introduced in 10.0.10586. |
| [IAppxBlockMapBlock](https://msdn.microsoft.com/en-us/library/windows/desktop/hh446630.aspx) | Introduced in 10.0.14393. |
| [IAppxBlockMapBlocksEnumerator](https://msdn.microsoft.com/en-us/library/windows/desktop/hh446631.aspx) | Introduced in 10.0.14393. |
| [IAppxBlockMapFile](https://msdn.microsoft.com/en-us/library/windows/desktop/hh446637.aspx) | Introduced in 10.0.14393. |
| [IAppxBlockMapFilesEnumerator](https://msdn.microsoft.com/en-us/library/windows/desktop/hh446638.aspx) | Introduced in 10.0.14393. |
| [IAppxBlockMapReader](https://msdn.microsoft.com/en-us/library/windows/desktop/hh446651.aspx) | Introduced in 10.0.14393. |
| [IAppxBundleFactory](https://msdn.microsoft.com/en-us/library/windows/desktop/dn280277.aspx) | Introduced in 10.0.14393. |
| [IAppxBundleWriter](https://msdn.microsoft.com/en-us/library/windows/desktop/dn280302.aspx) | Introduced in 10.0.14393. |
| [IAppxBundleReader](https://msdn.microsoft.com/en-us/library/windows/desktop/dn280296.aspx) | Introduced in 10.0.14393. |
| [IAppxBundleManifestReader](https://msdn.microsoft.com/en-us/library/windows/desktop/dn280292.aspx) | Introduced in 10.0.14393. |
| [IAppxBundleManifestPackageInfoEnumerator](https://msdn.microsoft.com/en-us/library/windows/desktop/dn280282.aspx) | Introduced in 10.0.14393. |
| [IAppxBundleManifestPackageInfo](https://msdn.microsoft.com/en-us/library/windows/desktop/dn280281.aspx) | Introduced in 10.0.14393. |
| [IAppxFactory](https://msdn.microsoft.com/en-us/library/windows/desktop/hh446671.aspx) | Introduced in 10.0.14393. |
| [IAppxFile](https://msdn.microsoft.com/en-us/library/windows/desktop/hh446683.aspx) | Introduced in 10.0.14393. |
| [IAppxFilesEnumerator](https://msdn.microsoft.com/en-us/library/windows/desktop/hh446685.aspx) | Introduced in 10.0.14393. |
| [IAppxManifestApplication](https://msdn.microsoft.com/en-us/library/windows/desktop/hh446697.aspx) | Introduced in 10.0.14393. |
| [IAppxManifestApplicationsEnumerator](https://msdn.microsoft.com/en-us/library/windows/desktop/hh446698.aspx) | Introduced in 10.0.14393. |
| [IAppxManifestQualifiedResource](https://msdn.microsoft.com/en-us/library/windows/desktop/dn280305.aspx) | Introduced in 10.0.14393. |
| [IAppxManifestQualifiedResourcesEnumerator](https://msdn.microsoft.com/en-us/library/windows/desktop/dn280306.aspx) | Introduced in 10.0.14393. |
| [IAppxPackageReader](https://msdn.microsoft.com/en-us/library/windows/desktop/hh446756.aspx) | Introduced in 10.0.14393. |
| [IAppxPackageWriter](https://msdn.microsoft.com/en-us/library/windows/desktop/hh446762.aspx) | Introduced in 10.0.14393. |
| [IAppxManifestDeviceCapabilitiesEnumerator](https://msdn.microsoft.com/en-us/library/windows/desktop/hh446704.aspx) | Introduced in 10.0.14393. |
| [IAppxManifestPackageId](https://msdn.microsoft.com/en-us/library/windows/desktop/hh446717.aspx) | Introduced in 10.0.14393. |
| [IAppxManifestPackageDependency](https://msdn.microsoft.com/en-us/library/windows/desktop/hh446713.aspx) | Introduced in 10.0.14393. |
| [IAppxManifestPackageDependenciesEnumerator](https://msdn.microsoft.com/en-us/library/windows/desktop/hh446708.aspx) | Introduced in 10.0.14393. |
| [IAppxManifestProperties](https://msdn.microsoft.com/en-us/library/windows/desktop/hh446731.aspx) | Introduced in 10.0.14393. |
| [IAppxManifestReader](https://msdn.microsoft.com/en-us/library/windows/desktop/hh446737.aspx) | Introduced in 10.0.14393. |
| [IAppxManifestReader2](https://msdn.microsoft.com/en-us/library/windows/desktop/dn280312.aspx) | Introduced in 10.0.14393. |
| [IAppxManifestReader3](https://msdn.microsoft.com/en-us/library/Mt796945.aspx) | Introduced in 10.0.14393. |
| [IAppxManifestCapabilitiesEnumerator](https://msdn.microsoft.com/en-us/library/Mt796938.aspx) | Introduced in 10.0.14393. |
| [IAppxManifestTargetDeviceFamiliesEnumerator](https://msdn.microsoft.com/en-us/library/Mt796950.aspx) | Introduced in 10.0.14393. |
| [IAppxManifestTargetDeviceFamily](https://msdn.microsoft.com/en-us/library/Mt796954.aspx) | Introduced in 10.0.14393. |
| IAppxManifestPackageDependency2 | Introduced in 10.0.14393. |
| [IAppxManifestResourcesEnumerator](https://msdn.microsoft.com/en-us/library/windows/desktop/hh446752.aspx) | Introduced in 10.0.14393. |
| [IAppxManifestReader4](https://msdn.microsoft.com/en-us/library/Mt796948.aspx) | Introduced in 10.0.14393. |
| [IAppxManifestOptionalPackageInfo](https://msdn.microsoft.com/en-us/library/Mt796942.aspx) | Introduced in 10.0.14393. |
| [IXblIdpAuthManager](https://msdn.microsoft.com/en-us/library/Mt709230.aspx) | Introduced in 10.0.14393. |
| [IXblIdpAuthTokenResult](https://msdn.microsoft.com/en-us/library/Mt709237.aspx) | Introduced in 10.0.14393. |
| [IAudioFormatEnumerator](https://msdn.microsoft.com/en-us/library/Mt779256.aspx) | Introduced in 10.0.15063. |
| [ID2D1CommandSink3](https://msdn.microsoft.com/en-us/library/Mt619822.aspx) | Introduced in 10.0.15063. |
| [ID2D1CommandSink4](https://msdn.microsoft.com/en-us/library/Mt797801.aspx) | Introduced in 10.0.15063. |
| [ID2D1Device3](https://msdn.microsoft.com/en-us/library/Mt619824.aspx) | Introduced in 10.0.15063. |
| [ID2D1Device4](https://msdn.microsoft.com/en-us/library/Mt736464.aspx) | Introduced in 10.0.15063. |
| [ID2D1Device5](https://msdn.microsoft.com/en-us/library/Mt797803.aspx) | Introduced in 10.0.15063. |
| [ID2D1DeviceContext3](https://msdn.microsoft.com/en-us/library/Mt619826.aspx) | Introduced in 10.0.15063. |
| [ID2D1DeviceContext4](https://msdn.microsoft.com/en-us/library/Mt736468.aspx) | Introduced in 10.0.15063. |
| [ID2D1DeviceContext5](https://msdn.microsoft.com/en-us/library/Mt797806.aspx) | Introduced in 10.0.15063. |
| [ID2D1Factory4](https://msdn.microsoft.com/en-us/library/Mt619831.aspx) | Introduced in 10.0.15063. |
| [ID2D1Factory5](https://msdn.microsoft.com/en-us/library/Mt750191.aspx) | Introduced in 10.0.15063. |
| [ID2D1Factory6](https://msdn.microsoft.com/en-us/library/Mt797812.aspx) | Introduced in 10.0.15063. |
| [ID2D1SpriteBatch](https://msdn.microsoft.com/en-us/library/Mt619833.aspx) | Introduced in 10.0.15063. |
| [ID2D1SvgAttribute](https://msdn.microsoft.com/en-us/library/Mt797814.aspx) | Introduced in 10.0.15063. |
| [ID2D1SvgDocument](https://msdn.microsoft.com/en-us/library/Mt797817.aspx) | Introduced in 10.0.15063. |
| [ID2D1SvgElement](https://msdn.microsoft.com/en-us/library/Mt797830.aspx) | Introduced in 10.0.15063. |
| [ID2D1SvgGlyphStyle](https://msdn.microsoft.com/en-us/library/Mt750193.aspx) | Introduced in 10.0.15063. |
| [ID2D1SvgPaint](https://msdn.microsoft.com/en-us/library/Mt797893.aspx) | Introduced in 10.0.15063. |
| [ID2D1SvgPathData](https://msdn.microsoft.com/en-us/library/Mt797902.aspx) | Introduced in 10.0.15063. |
| [ID2D1SvgPointCollection](https://msdn.microsoft.com/en-us/library/Mt797912.aspx) | Introduced in 10.0.15063. |
| [ID2D1SvgStrokeDashArray](https://msdn.microsoft.com/en-us/library/Mt797917.aspx) | Introduced in 10.0.15063. |
| IDXGIAdapter4 | Introduced in 10.0.15063. |
| [IMFSpatialAudioObjectBuffer](https://msdn.microsoft.com/en-us/library/Mt797969.aspx) | Introduced in 10.0.15063. |
| [IMFSpatialAudioSample](https://msdn.microsoft.com/en-us/library/Mt797975.aspx) | Introduced in 10.0.15063. |
| [ISpatialAudioObject](https://msdn.microsoft.com/en-us/library/Mt779268.aspx) | Introduced in 10.0.15063. |
| [ISpatialAudioObjectRenderStream](https://msdn.microsoft.com/en-us/library/Mt779280.aspx) | Introduced in 10.0.15063. |
| [ISpatialAudioObjectRenderStreamNotify](https://msdn.microsoft.com/en-us/library/Mt779281.aspx) | Introduced in 10.0.15063. |
| [ISpatialAudioClient](https://msdn.microsoft.com/en-us/library/Mt779259.aspx) | Introduced in 10.0.15063. |


COM coclasses

| API | Requirements |
| -----| --------------|
| AudioReverb | Introduced in 10.0.10240. |
| AudioVolumeMeter | Introduced in 10.0.10240. |
| AoWAppActivatedRuntime | Introduced in 10.0.10240. Removed in 10.0.15063. |
| AoWBackgroundTaskRuntime | Introduced in 10.0.10240. Removed in 10.0.15063. |
| CameraUIControl | Introduced in 10.0.10240. |
| CLSID_AudioFrameNativeFactory | Introduced in 10.0.10240. |
| CLSID_CMultiLanguage | Introduced in 10.0.10240. |
| CLSID_CUIAutomationRegistrar | Introduced in 10.0.10240. |
| CLSID_DeviceIoControl | Introduced in 10.0.10240. |
| CLSID_DShowSourceResolver | Introduced in 10.0.10240. |
| CLSID_FreeThreadedXMLHTTP60 | Introduced in 10.0.10240. |
| CLSID_GlobalOptions | Introduced in 10.0.10240. |
| CLSID_InProcFreeMarshaler | Introduced in 10.0.10240. |
| CLSID_MbnConnectionManager | Introduced in 10.0.10240. |
| CLSID_MbnDeviceServicesManager | Introduced in 10.0.10240. |
| CLSID_MbnInterfaceManager | Introduced in 10.0.10240. |
| CLSID_MFMediaEngineClassFactory | Introduced in 10.0.10240. |
| CLSID_MFReadWriteClassFactory | Introduced in 10.0.10240. |
| CLSID_MPEG2ByteStreamPlugin | Introduced in 10.0.10240. |
| CLSID_NetSchemePlugin | Introduced in 10.0.10240. |
| CLSID_OpcFactory | Introduced in 10.0.10240. |
| CLSID_PortableDevice | Introduced in 10.0.10240. |
| CLSID_PortableDeviceDispatchFactory | Introduced in 10.0.10240. |
| CLSID_PortableDeviceFTM | Introduced in 10.0.10240. |
| CLSID_PortableDeviceKeyCollection | Introduced in 10.0.10240. |
| CLSID_PortableDeviceManager | Introduced in 10.0.10240. |
| CLSID_PortableDevicePropVariantCollection | Introduced in 10.0.10240. |
| CLSID_PortableDeviceService | Introduced in 10.0.10240. |
| CLSID_PortableDeviceServiceFTM | Introduced in 10.0.10240. |
| CLSID_PortableDeviceValues | Introduced in 10.0.10240. |
| CLSID_PortableDeviceValuesCollection | Introduced in 10.0.10240. |
| CLSID_RemoteDesktopClient | Introduced in 10.0.10240. |
| CLSID_SoftwareBitmapNativeFactory | Introduced in 10.0.10240. |
| CLSID_StdGlobalInterfaceTable | Introduced in 10.0.10240. |
| CLSID_TF_CategoryMgr | Introduced in 10.0.10240. |
| CLSID_TF_DisplayAttributeMgr | Introduced in 10.0.10240. |
| CLSID_TF_InputProcessorProfiles | Introduced in 10.0.10240. |
| CLSID_TF_ThreadMgr | Introduced in 10.0.10240. |
| CLSID_ThumbnailStreamCache | Introduced in 10.0.10240. |
| CLSID_UIAnimationManager | Introduced in 10.0.10240. |
| CLSID_UIAnimationManager2 | Introduced in 10.0.10240. |
| CLSID_UIAnimationTimer | Introduced in 10.0.10240. |
| CLSID_UIAnimationTransitionFactory | Introduced in 10.0.10240. |
| CLSID_UIAnimationTransitionFactory2 | Introduced in 10.0.10240. |
| CLSID_UIAnimationTransitionLibrary | Introduced in 10.0.10240. |
| CLSID_UIAnimationTransitionLibrary2 | Introduced in 10.0.10240. |
| CLSID_VideoFrameNativeFactory | Introduced in 10.0.10240. |
| CLSID_WICImagingFactory | Introduced in 10.0.10240. |
| CLSID_WICImagingFactory1 | Introduced in 10.0.10240. |
| CLSID_WICImagingFactory2 | Introduced in 10.0.10240. |
| CLSID_XpsOMObjectFactory | Introduced in 10.0.10240. |
| FXEcho | Introduced in 10.0.10240. |
| FXEQ | Introduced in 10.0.10240. |
| FXMasteringLimiter | Introduced in 10.0.10240. |
| FXReverb | Introduced in 10.0.10240. |
| [RDPSession](https://msdn.microsoft.com/en-us/library/Mt446078.aspx) | Introduced in 10.0.10240. |
| RDPSRAPIApplication | Introduced in 10.0.10240. |
| RDPSRAPIApplicationFilter | Introduced in 10.0.10240. |
| RDPSRAPIApplicationList | Introduced in 10.0.10240. |
| RDPSRAPIAttendee | Introduced in 10.0.10240. |
| RDPSRAPIAttendeeDisconnectInfo | Introduced in 10.0.10240. |
| RDPSRAPIAttendeeManager | Introduced in 10.0.10240. |
| RDPSRAPIInvitation | Introduced in 10.0.10240. |
| RDPSRAPIInvitationManager | Introduced in 10.0.10240. |
| RDPSRAPISessionProperties | Introduced in 10.0.10240. |
| RDPSRAPITcpConnectionInfo | Introduced in 10.0.10240. |
| RDPSRAPIWindow | Introduced in 10.0.10240. |
| RDPSRAPIWindowList | Introduced in 10.0.10240. |
| RDPViewer | Introduced in 10.0.10240. |
| SignalableNotifier | Introduced in 10.0.10240. |
| SpellCheckerFactory | Introduced in 10.0.10240. |
| [WorkspaceBrokerAx](https://msdn.microsoft.com/en-us/library/Hh974747.aspx) | Introduced in 10.0.10240. |
| AppxFactory | Introduced in 10.0.14393. |
| CLSID_AudioResamplerMediaObject | Introduced in 10.0.14393. |
| CLSID_MSAACDecMFT | Introduced in 10.0.14393. |
| CLSID_MSDDPlusDecMFT | Introduced in 10.0.14393. |
| CLSID_MSH264DecoderMFT | Introduced in 10.0.14393. |
| CLSID_MSH264EncoderMFT | Introduced in 10.0.14393. |
| CLSID_MSH265DecoderMFT | Introduced in 10.0.14393. |
| CLSID_MSMPEGAudDecMFT | Introduced in 10.0.14393. |
| CLSID_MSMPEGDecoderMFT | Introduced in 10.0.14393. |
| CLSID_MSVPxDecoder | Introduced in 10.0.14393. |
| CLSID_MP3DecMediaObject | Introduced in 10.0.14393. |
| CLSID_PublicShellFeedbackBroker | Introduced in 10.0.14393. |
| CLSID_VideoProcessorMFT | Introduced in 10.0.14393. |
| CLSID_WMADecMediaObject | Introduced in 10.0.14393. |
| CLSID_WMVDecoderMFT | Introduced in 10.0.14393. |
| XblIdpAuthManager | Introduced in 10.0.14393. |


