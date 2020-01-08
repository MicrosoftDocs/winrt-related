---

description: This topic lists the Win32 and COM APIs that are part of the Universal Windows Platform (UWP) and that are implemented by some Windows 10 devices.
title: Extension APIs for Windows 10 devices (grouped by module)

ms.topic: article


keywords: windows 10, uwp, win32, COM
ms.date: 10/10/2018
ms.assetid: e8d54f37-9969-4f33-8b1b-fcb3d659c507
---

# Extension APIs for Windows 10 devices
This topic lists the Win32 and COM APIs that are part of the Universal Windows Platform (UWP) and that are implemented by some Windows 10 devices, so your calls to these APIs must be guarded with conditions that first confirm the presence of the API on the device your app is running on. The union of [APIs present on all Windows 10 devices](win32-apis.md) and the APIs listed in this topic make up the entire Win32 and COM surface area of UWP.

This topic lists the APIs grouped by module (where the module is either an [API set](https://msdn.microsoft.com/library/windows/apps/mt683763.aspx#api_sets) or a dll). For delay load, use the module name.

## APIs from PhoneAudioSes.dll

| API | Requirements |
| -----| --------------|
| ActivateAudioInterface | Introduced into PhoneAudioSes.dll in 10.0.10240. |


## APIs from MSAJApi.dll

| API | Requirements |
| -----| --------------|
| alljoyn_aboutdata_createfromxml | Introduced into MSAJApi.dll in 10.0.10240. Removed in 10.0.14393. |
| alljoyn_routerinit | Introduced into MSAJApi.dll in 10.0.10240. Removed in 10.0.14393. |
| alljoyn_routershutdown | Introduced into MSAJApi.dll in 10.0.10240. Removed in 10.0.14393. |


## APIs from Bcrypt.dll

| API | Requirements |
| -----| --------------|
| [BCryptCreateMultiHash](https://msdn.microsoft.com/library/Mt845763(v=VS.85).aspx) | Introduced into Bcrypt.dll in 10.0.10240. Removed in 10.0.10586. |
| [BCryptProcessMultiOperations](https://msdn.microsoft.com/library/Mt845764(v=VS.85).aspx) | Introduced into Bcrypt.dll in 10.0.10240. Removed in 10.0.10586. |


## APIs from ole32.dll

| API | Requirements |
| -----| --------------|
| [BindMoniker](https://msdn.microsoft.com/library/windows/desktop/ms683759.aspx) | Introduced into ole32.dll in 10.0.10240. |
| [CoGetObject](https://msdn.microsoft.com/library/windows/desktop/ms678805.aspx) | Introduced into ole32.dll in 10.0.10240. |
| [CreateAntiMoniker](https://msdn.microsoft.com/library/windows/desktop/ms679750.aspx) | Introduced into ole32.dll in 10.0.10240. |
| [CreateBindCtx](https://msdn.microsoft.com/library/windows/desktop/ms678542.aspx) | Introduced into ole32.dll in 10.0.10240. |
| [CreateClassMoniker](https://msdn.microsoft.com/library/windows/desktop/ms688698.aspx) | Introduced into ole32.dll in 10.0.10240. |
| [CreateFileMoniker](https://msdn.microsoft.com/library/windows/desktop/ms693465.aspx) | Introduced into ole32.dll in 10.0.10240. |
| [CreateGenericComposite](https://msdn.microsoft.com/library/windows/desktop/ms687265.aspx) | Introduced into ole32.dll in 10.0.10240. |
| [CreateItemMoniker](https://msdn.microsoft.com/library/windows/desktop/ms680140.aspx) | Introduced into ole32.dll in 10.0.10240. |
| [CreateObjrefMoniker](https://msdn.microsoft.com/library/windows/desktop/ms678493.aspx) | Introduced into ole32.dll in 10.0.10240. |
| [CreatePointerMoniker](https://msdn.microsoft.com/library/windows/desktop/ms693427.aspx) | Introduced into ole32.dll in 10.0.10240. |
| [GetClassFile](https://msdn.microsoft.com/library/windows/desktop/ms693715.aspx) | Introduced into ole32.dll in 10.0.10240. |
| [IsEqualGUID](https://msdn.microsoft.com/library/windows/desktop/ms680575.aspx) | Introduced into ole32.dll in 10.0.10240. |
| [MkParseDisplayName](https://msdn.microsoft.com/library/windows/desktop/ms691253.aspx) | Introduced into ole32.dll in 10.0.10240. |
| [MonikerCommonPrefixWith](https://msdn.microsoft.com/library/windows/desktop/ms686583.aspx) | Introduced into ole32.dll in 10.0.10240. |
| [MonikerRelativePathTo](https://msdn.microsoft.com/library/windows/desktop/ms682532.aspx) | Introduced into ole32.dll in 10.0.10240. |


## APIs from dmprocessxmlfiltered.dll

| API | Requirements |
| -----| --------------|
| [DMProcessConfigXMLFiltered](https://msdn.microsoft.com/library/Mt591928(v=VS.85).aspx) | Introduced into dmprocessxmlfiltered.dll in 10.0.10240. |


## APIs from iphlpapi.dll

| API | Requirements |
| -----| --------------|
| [GetAdaptersAddresses](https://msdn.microsoft.com/library/windows/desktop/aa365915.aspx) | Introduced into iphlpapi.dll in 10.0.10240. Removed in 10.0.14393. |
| [FreeMibTable](https://msdn.microsoft.com/library/windows/desktop/aa814408.aspx) | Introduced into iphlpapi.dll in 10.0.10586. Removed in 10.0.14393. |
| [GetBestRoute2](https://msdn.microsoft.com/library/windows/desktop/aa814411.aspx) | Introduced into iphlpapi.dll in 10.0.10586. Removed in 10.0.14393. |
| [GetUnicastIpAddressTable](https://msdn.microsoft.com/library/windows/desktop/aa814428.aspx) | Introduced into iphlpapi.dll in 10.0.10586. Removed in 10.0.14393. |


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
| [InterlockedCompareExchange](https://msdn.microsoft.com/library/windows/desktop/ff471409.aspx) | Introduced into kernel32.dll in 10.0.10240. Removed in 10.0.16299. |
| [InterlockedCompareExchange64](https://msdn.microsoft.com/library/windows/desktop/ms683562.aspx) | Introduced into kernel32.dll in 10.0.10240. Removed in 10.0.16299. |
| [InterlockedDecrement](https://msdn.microsoft.com/library/windows/desktop/ms683580.aspx) | Introduced into kernel32.dll in 10.0.10240. Removed in 10.0.16299. |
| [InterlockedExchange](https://msdn.microsoft.com/library/windows/desktop/ff471411.aspx) | Introduced into kernel32.dll in 10.0.10240. Removed in 10.0.16299. |
| [InterlockedExchangeAdd](https://msdn.microsoft.com/library/windows/desktop/ms683597.aspx) | Introduced into kernel32.dll in 10.0.10240. Removed in 10.0.16299. |
| [InterlockedIncrement](https://msdn.microsoft.com/library/windows/desktop/ms683614.aspx) | Introduced into kernel32.dll in 10.0.10240. Removed in 10.0.16299. |
| [GetModuleBaseNameA](https://msdn.microsoft.com/library/ms683196(v=VS.85).aspx) | Introduced into kernel32.dll in 10.0.16299. |
| [GetModuleBaseNameW](https://msdn.microsoft.com/library/ms683196(v=VS.85).aspx) | Introduced into kernel32.dll in 10.0.16299. |
| [GetModuleFileNameExA](https://msdn.microsoft.com/library/ms683198(v=VS.85).aspx) | Introduced into kernel32.dll in 10.0.16299. |
| [GetModuleFileNameExW](https://msdn.microsoft.com/library/ms683198(v=VS.85).aspx) | Introduced into kernel32.dll in 10.0.16299. |
| [GetModuleInformation](https://msdn.microsoft.com/library/ms683201(v=VS.85).aspx) | Introduced into kernel32.dll in 10.0.16299. |
| [SetEnvironmentVariable](https://msdn.microsoft.com/library/ms686206(v=VS.85).aspx) | Introduced into kernel32.dll in 10.0.16299. Moved into api-ms-win-core-processenvironment-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-processenvironment-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Removed in 10.0.17134. |
| [GetModuleFileNameEx](https://msdn.microsoft.com/library/ms683198(v=VS.85).aspx) | Introduced into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [VerLanguageName](https://msdn.microsoft.com/library/ms647463(v=VS.85).aspx) | Introduced into kernel32.dll in 10.0.16299. Moved into api-ms-win-core-localization-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-localization-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-localization-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-core-localization-l1-2-2.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from kernelbase.dll

| API | Requirements |
| -----| --------------|
| [GetProcessMemoryInfo](https://msdn.microsoft.com/library/windows/desktop/ms683219.aspx) | Introduced into kernelbase.dll in 10.0.10240. Removed in 10.0.14393. Moved into kernel32.dll in 10.0.16299. |


## APIs from elscore.dll

| API | Requirements |
| -----| --------------|
| [MappingFreePropertyBag](https://msdn.microsoft.com/library/windows/desktop/dd319058.aspx) | Introduced into elscore.dll in 10.0.10240. |
| [MappingFreeServices](https://msdn.microsoft.com/library/windows/desktop/dd319059.aspx) | Introduced into elscore.dll in 10.0.10240. |
| [MappingGetServices](https://msdn.microsoft.com/library/windows/desktop/dd319060.aspx) | Introduced into elscore.dll in 10.0.10240. |
| [MappingRecognizeText](https://msdn.microsoft.com/library/windows/desktop/dd319063.aspx) | Introduced into elscore.dll in 10.0.10240. |


## APIs from rpcrt4.dll

| API | Requirements |
| -----| --------------|
| [NdrAsyncClientCall2](https://msdn.microsoft.com/library/windows/desktop/mt297483.aspx) | Introduced into rpcrt4.dll in 10.0.10240. Removed in 10.0.16299. |
| [NdrClientCall4](https://msdn.microsoft.com/library/windows/desktop/mt297484.aspx) | Introduced into rpcrt4.dll in 10.0.10240. Removed in 10.0.16299. |
| [DceErrorInqText](https://msdn.microsoft.com/library/Aa373623(v=VS.85).aspx) | Introduced into rpcrt4.dll in 10.0.16299. Removed in 10.0.17134. |
| [RpcBindingCreate](https://msdn.microsoft.com/library/Aa375587(v=VS.85).aspx) | Introduced into rpcrt4.dll in 10.0.16299. Removed in 10.0.17134. |
| [RpcBindingFromStringBinding](https://msdn.microsoft.com/library/Aa375590(v=VS.85).aspx) | Introduced into rpcrt4.dll in 10.0.16299. Removed in 10.0.17134. |
| [RpcBindingInqAuthInfo](https://msdn.microsoft.com/library/Aa375593(v=VS.85).aspx) | Introduced into rpcrt4.dll in 10.0.16299. Removed in 10.0.17134. |
| [RpcBindingInqAuthInfoEx](https://msdn.microsoft.com/library/Aa375595(v=VS.85).aspx) | Introduced into rpcrt4.dll in 10.0.16299. Removed in 10.0.17134. |
| [RpcBindingSetAuthInfo](https://msdn.microsoft.com/library/Aa375606(v=VS.85).aspx) | Introduced into rpcrt4.dll in 10.0.16299. Removed in 10.0.17134. |
| [RpcBindingSetAuthInfoEx](https://msdn.microsoft.com/library/Aa375608(v=VS.85).aspx) | Introduced into rpcrt4.dll in 10.0.16299. Removed in 10.0.17134. |
| [RpcBindingToStringBinding](https://msdn.microsoft.com/library/Aa375612(v=VS.85).aspx) | Introduced into rpcrt4.dll in 10.0.16299. Removed in 10.0.17134. |
| [RpcMgmtInqServerPrincName](https://msdn.microsoft.com/library/Aa375756(v=VS.85).aspx) | Introduced into rpcrt4.dll in 10.0.16299. Removed in 10.0.17134. |
| [RpcNetworkIsProtseqValid](https://msdn.microsoft.com/library/Aa375804(v=VS.85).aspx) | Introduced into rpcrt4.dll in 10.0.16299. Removed in 10.0.17134. |
| [RpcStringBindingCompose](https://msdn.microsoft.com/library/Aa378481(v=VS.85).aspx) | Introduced into rpcrt4.dll in 10.0.16299. Removed in 10.0.17134. |
| [RpcStringBindingParse](https://msdn.microsoft.com/library/Aa378482(v=VS.85).aspx) | Introduced into rpcrt4.dll in 10.0.16299. Removed in 10.0.17134. |
| [RpcStringFree](https://msdn.microsoft.com/library/Aa378483(v=VS.85).aspx) | Introduced into rpcrt4.dll in 10.0.16299. Removed in 10.0.17134. |
| [UuidFromString](https://msdn.microsoft.com/library/Aa379336(v=VS.85).aspx) | Introduced into rpcrt4.dll in 10.0.16299. Removed in 10.0.17134. |
| [UuidToString](https://msdn.microsoft.com/library/Aa379352(v=VS.85).aspx) | Introduced into rpcrt4.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from windows.data.pdf.dll

| API | Requirements |
| -----| --------------|
| [PdfRenderParams](https://msdn.microsoft.com/library/windows/desktop/mt604123.aspx) | Introduced into windows.data.pdf.dll in 10.0.10240. Removed in 10.0.14393. |


## APIs from api-ms-win-core-slapi-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [SLQueryLicenseValueFromApp](https://msdn.microsoft.com/library/windows/desktop/mt403327.aspx) | Introduced into api-ms-win-core-slapi-l1-1-0.dll in 10.0.10240. Removed in 10.0.14393. |
| SLQueryLicenseValueFromApp2 | Introduced into api-ms-win-core-slapi-l1-1-0.dll in 10.0.10240. Removed in 10.0.14393. |


## APIs from srpapi.dll

| API | Requirements |
| -----| --------------|
| [SrpDoesPolicyAllowAppExecution](https://msdn.microsoft.com/library/Mt757271(v=VS.85).aspx) | Introduced into srpapi.dll in 10.0.10240. |


## APIs from api-ms-win-crt-convert-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| __toascii | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _atodbl | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _atodbl_l | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _atof_l | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _atoflt | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _atoflt_l | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _atoi_l | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _atoi64 | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _atoi64_l | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _atol_l | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _atoldbl | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _atoldbl_l | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _atoll_l | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _ecvt | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _ecvt_s | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _fcvt | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _fcvt_s | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _gcvt | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _gcvt_s | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _i64toa | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _i64toa_s | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _i64tow | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _i64tow_s | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _itoa | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _itoa_s | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _itow | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _itow_s | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _ltoa | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _ltoa_s | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _ltow | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _ltow_s | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _strtod_l | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _strtof_l | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _strtoi64 | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _strtoi64_l | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _strtoimax_l | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _strtol_l | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _strtold_l | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _strtoll_l | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _strtoui64 | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _strtoui64_l | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _strtoul_l | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _strtoull_l | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _strtoumax_l | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _ui64toa | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _ui64toa_s | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _ui64tow | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _ui64tow_s | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _ultoa | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _ultoa_s | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _ultow | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _ultow_s | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _wcstod_l | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _wcstof_l | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _wcstoi64 | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _wcstoi64_l | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _wcstoimax_l | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _wcstol_l | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _wcstold_l | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _wcstoll_l | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _wcstombs_l | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _wcstombs_s_l | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _wcstoui64 | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _wcstoui64_l | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _wcstoul_l | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _wcstoull_l | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _wcstoumax_l | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _wctomb_l | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _wctomb_s_l | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _wtof | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _wtof_l | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _wtoi | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _wtoi_l | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _wtoi64 | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _wtoi64_l | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _wtol | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _wtol_l | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _wtoll | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| _wtoll_l | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| atof | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| atoi | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| atol | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| atoll | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| btowc | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| c16rtomb | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| c32rtomb | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| mbrtoc16 | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| mbrtoc32 | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| mbrtowc | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| mbsrtowcs | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| mbsrtowcs_s | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| mbstowcs | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| mbstowcs_s | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| mbtowc | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| strtod | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| strtof | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| strtoimax | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| strtol | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| strtold | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| strtoll | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| strtoul | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| strtoull | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| strtoumax | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| wcrtomb | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| wcrtomb_s | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| wcsrtombs | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| wcsrtombs_s | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| wcstod | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| wcstof | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| wcstoimax | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| wcstol | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| wcstold | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| wcstoll | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| wcstombs | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| wcstombs_s | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| wcstoul | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| wcstoull | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| wcstoumax | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| wctob | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| wctomb | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| wctomb_s | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |
| wctrans | Introduced into api-ms-win-crt-convert-l1-1-0.dll in 10.0.10240. |


## APIs from api-ms-win-crt-environment-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| __p__environ | Introduced into api-ms-win-crt-environment-l1-1-0.dll in 10.0.10240. |
| __p__wenviron | Introduced into api-ms-win-crt-environment-l1-1-0.dll in 10.0.10240. |
| _dupenv_s | Introduced into api-ms-win-crt-environment-l1-1-0.dll in 10.0.17134. |
| getenv | Introduced into api-ms-win-crt-environment-l1-1-0.dll in 10.0.17134. |
| getenv_s | Introduced into api-ms-win-crt-environment-l1-1-0.dll in 10.0.17134. |
| _putenv | Introduced into api-ms-win-crt-environment-l1-1-0.dll in 10.0.17134. |
| _putenv_s | Introduced into api-ms-win-crt-environment-l1-1-0.dll in 10.0.17134. |
| _searchenv | Introduced into api-ms-win-crt-environment-l1-1-0.dll in 10.0.17134. |
| _searchenv_s | Introduced into api-ms-win-crt-environment-l1-1-0.dll in 10.0.17134. |
| _wdupenv_s | Introduced into api-ms-win-crt-environment-l1-1-0.dll in 10.0.17134. |
| _wgetenv | Introduced into api-ms-win-crt-environment-l1-1-0.dll in 10.0.17134. |
| _wgetenv_s | Introduced into api-ms-win-crt-environment-l1-1-0.dll in 10.0.17134. |
| _wputenv | Introduced into api-ms-win-crt-environment-l1-1-0.dll in 10.0.17134. |
| _wputenv_s | Introduced into api-ms-win-crt-environment-l1-1-0.dll in 10.0.17134. |
| _wsearchenv_s | Introduced into api-ms-win-crt-environment-l1-1-0.dll in 10.0.17134. |
| _wsearchenv | Introduced into api-ms-win-crt-environment-l1-1-0.dll in 10.0.17134. |


## APIs from api-ms-win-crt-filesystem-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| _access | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| _access_s | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| _chdir | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| _chmod | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| _findclose | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| _findfirst32 | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| _findfirst32i64 | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| _findfirst64 | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| _findfirst64i32 | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| _findnext32 | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| _findnext32i64 | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| _findnext64 | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| _findnext64i32 | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| _fstat32 | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| _fstat32i64 | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| _fstat64 | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| _fstat64i32 | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| _fullpath | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| _getcwd | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| _getdcwd | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| _lock_file | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| _makepath | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| _makepath_s | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| _mkdir | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| _rmdir | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| _splitpath | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| _splitpath_s | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| _stat32 | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| _stat32i64 | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| _stat64 | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| _stat64i32 | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| _umask | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| _umask_s | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| _unlink | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| _unlock_file | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| _waccess | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| _waccess_s | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| _wchdir | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| _wchmod | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| _wfindfirst32 | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| _wfindfirst32i64 | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| _wfindfirst64 | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| _wfindfirst64i32 | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| _wfindnext32 | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| _wfindnext32i64 | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| _wfindnext64 | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| _wfindnext64i32 | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| _wfullpath | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| _wgetcwd | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| _wgetdcwd | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| _wmakepath | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| _wmakepath_s | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| _wmkdir | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| _wremove | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| _wrename | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| _wrmdir | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| _wsplitpath | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| _wsplitpath_s | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| _wstat32 | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| _wstat32i64 | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| _wstat64 | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| _wstat64i32 | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| _wunlink | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [remove](https://msdn.microsoft.com/library/Aa371194(v=VS.85).aspx) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [rename](https://msdn.microsoft.com/library/Aa964881(v=VS.85).aspx) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |


## APIs from api-ms-win-crt-heap-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| _aligned_free | Introduced into api-ms-win-crt-heap-l1-1-0.dll in 10.0.10240. |
| _aligned_malloc | Introduced into api-ms-win-crt-heap-l1-1-0.dll in 10.0.10240. |
| _aligned_msize | Introduced into api-ms-win-crt-heap-l1-1-0.dll in 10.0.10240. |
| _aligned_offset_malloc | Introduced into api-ms-win-crt-heap-l1-1-0.dll in 10.0.10240. |
| _aligned_offset_realloc | Introduced into api-ms-win-crt-heap-l1-1-0.dll in 10.0.10240. |
| _aligned_offset_recalloc | Introduced into api-ms-win-crt-heap-l1-1-0.dll in 10.0.10240. |
| _aligned_realloc | Introduced into api-ms-win-crt-heap-l1-1-0.dll in 10.0.10240. |
| _aligned_recalloc | Introduced into api-ms-win-crt-heap-l1-1-0.dll in 10.0.10240. |
| _callnewh | Introduced into api-ms-win-crt-heap-l1-1-0.dll in 10.0.10240. |
| _calloc_base | Introduced into api-ms-win-crt-heap-l1-1-0.dll in 10.0.10240. |
| _expand | Introduced into api-ms-win-crt-heap-l1-1-0.dll in 10.0.10240. |
| _free_base | Introduced into api-ms-win-crt-heap-l1-1-0.dll in 10.0.10240. |
| _get_heap_handle | Introduced into api-ms-win-crt-heap-l1-1-0.dll in 10.0.10240. |
| _heapmin | Introduced into api-ms-win-crt-heap-l1-1-0.dll in 10.0.10240. |
| _malloc_base | Introduced into api-ms-win-crt-heap-l1-1-0.dll in 10.0.10240. |
| _msize | Introduced into api-ms-win-crt-heap-l1-1-0.dll in 10.0.10240. |
| _query_new_handler | Introduced into api-ms-win-crt-heap-l1-1-0.dll in 10.0.10240. |
| _query_new_mode | Introduced into api-ms-win-crt-heap-l1-1-0.dll in 10.0.10240. |
| _realloc_base | Introduced into api-ms-win-crt-heap-l1-1-0.dll in 10.0.10240. |
| _recalloc | Introduced into api-ms-win-crt-heap-l1-1-0.dll in 10.0.10240. |
| _set_new_mode | Introduced into api-ms-win-crt-heap-l1-1-0.dll in 10.0.10240. |
| calloc | Introduced into api-ms-win-crt-heap-l1-1-0.dll in 10.0.10240. |
| free | Introduced into api-ms-win-crt-heap-l1-1-0.dll in 10.0.10240. |
| malloc | Introduced into api-ms-win-crt-heap-l1-1-0.dll in 10.0.10240. |
| realloc | Introduced into api-ms-win-crt-heap-l1-1-0.dll in 10.0.10240. |
| _resetstkoflw | Introduced into api-ms-win-crt-heap-l1-1-0.dll in 10.0.16299. |


## APIs from api-ms-win-crt-locale-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| ___lc_codepage_func | Introduced into api-ms-win-crt-locale-l1-1-0.dll in 10.0.10240. |
| ___lc_collate_cp_func | Introduced into api-ms-win-crt-locale-l1-1-0.dll in 10.0.10240. |
| ___lc_locale_name_func | Introduced into api-ms-win-crt-locale-l1-1-0.dll in 10.0.10240. |
| ___mb_cur_max_func | Introduced into api-ms-win-crt-locale-l1-1-0.dll in 10.0.10240. |
| ___mb_cur_max_l_func | Introduced into api-ms-win-crt-locale-l1-1-0.dll in 10.0.10240. |
| __initialize_lconv_for_unsigned_char | Introduced into api-ms-win-crt-locale-l1-1-0.dll in 10.0.10240. |
| __pctype_func | Introduced into api-ms-win-crt-locale-l1-1-0.dll in 10.0.10240. |
| __pwctype_func | Introduced into api-ms-win-crt-locale-l1-1-0.dll in 10.0.10240. |
| _configthreadlocale | Introduced into api-ms-win-crt-locale-l1-1-0.dll in 10.0.10240. |
| _create_locale | Introduced into api-ms-win-crt-locale-l1-1-0.dll in 10.0.10240. |
| _free_locale | Introduced into api-ms-win-crt-locale-l1-1-0.dll in 10.0.10240. |
| _get_current_locale | Introduced into api-ms-win-crt-locale-l1-1-0.dll in 10.0.10240. |
| _getmbcp | Introduced into api-ms-win-crt-locale-l1-1-0.dll in 10.0.10240. |
| _lock_locales | Introduced into api-ms-win-crt-locale-l1-1-0.dll in 10.0.10240. |
| _setmbcp | Introduced into api-ms-win-crt-locale-l1-1-0.dll in 10.0.10240. |
| _unlock_locales | Introduced into api-ms-win-crt-locale-l1-1-0.dll in 10.0.10240. |
| _wcreate_locale | Introduced into api-ms-win-crt-locale-l1-1-0.dll in 10.0.10240. |
| _wsetlocale | Introduced into api-ms-win-crt-locale-l1-1-0.dll in 10.0.10240. |
| localeconv | Introduced into api-ms-win-crt-locale-l1-1-0.dll in 10.0.10240. |
| [setlocale](https://msdn.microsoft.com/library/5xf99h19(v=VS.85).aspx) | Introduced into api-ms-win-crt-locale-l1-1-0.dll in 10.0.10240. |


## APIs from api-ms-win-crt-math-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| __libm_sse2_acos | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| __libm_sse2_acosf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| __libm_sse2_asin | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| __libm_sse2_asinf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| __libm_sse2_atan | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| __libm_sse2_atan2 | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| __libm_sse2_atanf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| __libm_sse2_cos | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| __libm_sse2_cosf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| __libm_sse2_exp | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| __libm_sse2_expf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| __libm_sse2_log | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| __libm_sse2_log10 | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| __libm_sse2_log10f | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| __libm_sse2_logf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| __libm_sse2_pow | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| __libm_sse2_powf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| __libm_sse2_sin | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| __libm_sse2_sinf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| __libm_sse2_tan | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| __libm_sse2_tanf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| __setusermatherr | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _cabs | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _Cbuild | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _chgsign | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _chgsignf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _CIacos | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _CIasin | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _CIatan | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _CIatan2 | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _CIcos | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _CIcosh | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _CIexp | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _CIfmod | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _CIlog | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _CIlog10 | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _CIpow | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _CIsin | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _CIsinh | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _CIsqrt | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _CItan | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _CItanh | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _Cmulcc | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _Cmulcr | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _copysign | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _copysignf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _d_int | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _dclass | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _dexp | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _dlog | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _dnorm | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _dpcomp | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _dpoly | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _dscale | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _dsign | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _dsin | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _dtest | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _dunscale | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _except1 | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _FCbuild | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _FCmulcc | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _FCmulcr | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _fd_int | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _fdclass | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _fdexp | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _fdlog | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _fdnorm | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _fdopen | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _fdpcomp | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _fdpoly | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _fdscale | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _fdsign | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _fdsin | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _fdtest | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _fdunscale | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _finite | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _finitef | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _fpclass | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _fpclassf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _FPE_Raise | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _ftol | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _get_FMA3_enable | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _hypot | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _hypotf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _isnan | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _isnanf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _j0 | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _j1 | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _jn | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _LCbuild | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _LCmulcc | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _LCmulcr | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _ld_int | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _ldclass | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _ldexp | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _ldlog | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _ldpcomp | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _ldpoly | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _ldscale | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _ldsign | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _ldsin | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _ldtest | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _ldunscale | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _libm_sse2_acos_precise | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _libm_sse2_asin_precise | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _libm_sse2_atan_precise | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _libm_sse2_cos_precise | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _libm_sse2_exp_precise | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _libm_sse2_log_precise | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _libm_sse2_log10_precise | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _libm_sse2_pow_precise | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _libm_sse2_sin_precise | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _libm_sse2_sqrt_precise | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _libm_sse2_tan_precise | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _logb | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _logbf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _nextafter | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _nextafterf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _scalb | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _scalbf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _set_FMA3_enable | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _set_SSE2_enable | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _y0 | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _y1 | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| _yn | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [acos](https://msdn.microsoft.com/library/Bb509563(v=VS.85).aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| acosf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| acosh | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| acoshf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| acoshl | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [asin](https://msdn.microsoft.com/library/Bb509571(v=VS.85).aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| asinf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| asinh | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| asinhf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| asinhl | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [atan](https://msdn.microsoft.com/library/Bb509574(v=VS.85).aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [atan2](https://msdn.microsoft.com/library/Bb509575(v=VS.85).aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| atan2f | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| atanf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| atanh | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| atanhf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| atanhl | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| cabs | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| cabsf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| cabsl | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| cacos | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| cacosf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| cacosh | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| cacoshf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| cacoshl | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| cacosl | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| carg | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| cargf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| cargl | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| casin | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| casinf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| casinh | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| casinhf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| casinhl | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| casinl | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| catan | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| catanf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| catanh | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| catanhf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| catanhl | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| catanl | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| cbrt | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| cbrtf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| cbrtl | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| ccos | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| ccosf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| ccosh | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| ccoshf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| ccoshl | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| ccosl | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [ceil](https://msdn.microsoft.com/library/Bb509577(v=VS.85).aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| ceilf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| cexp | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| cexpf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| cexpl | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| cimag | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| cimagf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| cimagl | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| clog | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| clog10 | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| clog10f | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| clog10l | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| clogf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| clogl | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| conj | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| conjf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| conjl | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| copysign | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| copysignf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| copysignl | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [cos](https://msdn.microsoft.com/library/66bkzah2(v=VS.85).aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| cosf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [cosh](https://msdn.microsoft.com/library/Bb509584(v=VS.85).aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| coshf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| cpow | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| cpowf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| cpowl | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| cproj | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| cprojf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| cprojl | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| creal | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| crealf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| creall | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| csin | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| csinf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| csinh | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| csinhf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| csinhl | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| csinl | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| csqrt | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| csqrtf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| csqrtl | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| ctan | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| ctanf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| ctanh | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| ctanhf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| ctanhl | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| ctanl | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| erf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| erfc | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| erfcf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| erfcl | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| erff | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| erfl | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [exp](https://msdn.microsoft.com/library/aw8fzd30(v=VS.85).aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [exp2](https://msdn.microsoft.com/library/Bb509596(v=VS.85).aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| exp2f | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| exp2l | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| expf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| expm1 | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| expm1f | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| expm1l | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| fabs | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| fabsf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| fdim | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| fdimf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| fdiml | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [floor](https://msdn.microsoft.com/library/Bb509599(v=VS.85).aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| floorf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [fma](https://msdn.microsoft.com/library/Hh768893(v=VS.85).aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| fmaf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| fmal | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| fmax | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| fmaxf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| fmaxl | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| fmin | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| fminf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| fminl | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [fmod](https://msdn.microsoft.com/library/Bb509601(v=VS.85).aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| fmodf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [frexp](https://msdn.microsoft.com/library/Bb509604(v=VS.85).aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| hypot | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| ilogb | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| ilogbf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| ilogbl | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [ldexp](https://msdn.microsoft.com/library/Bb509616(v=VS.85).aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| lgamma | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| lgammaf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| lgammal | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| llrint | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| llrintf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| llrintl | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| llround | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| llroundf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| llroundl | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [log](https://msdn.microsoft.com/library/5xkbf3yw(v=VS.85).aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [log10](https://msdn.microsoft.com/library/Bb509621(v=VS.85).aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| log10f | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| log1p | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| log1pf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| log1pl | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [log2](https://msdn.microsoft.com/library/Bb509622(v=VS.85).aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| log2f | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| log2l | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| logb | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| logbf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| logbl | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| logf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| lrint | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| lrintf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| lrintl | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| lround | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| lroundf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| lroundl | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [modf](https://msdn.microsoft.com/library/Bb509627(v=VS.85).aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| modff | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [nan](https://msdn.microsoft.com/library/Dd372582(v=VS.85).aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| nanf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| nanl | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| nearbyint | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| nearbyintf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| nearbyintl | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| nextafter | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| nextafterf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| nextafterl | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| nexttoward | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| nexttowardf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| nexttowardl | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| norm | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| normf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| norml | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [pow](https://msdn.microsoft.com/library/Bb509636(v=VS.85).aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| powf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| remainder | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| remainderf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| remainderl | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| remquo | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| remquof | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| remquol | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| rint | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| rintf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| rintl | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [round](https://msdn.microsoft.com/library/Bb509642(v=VS.85).aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| roundf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| roundl | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| scalbln | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| scalblnf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| scalblnl | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| scalbn | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| scalbnf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| scalbnl | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [sin](https://msdn.microsoft.com/library/Bb509651(v=VS.85).aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| sinf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [sinh](https://msdn.microsoft.com/library/Bb509653(v=VS.85).aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| sinhf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [sqrt](https://msdn.microsoft.com/library/Bb509662(v=VS.85).aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| sqrtf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [tan](https://msdn.microsoft.com/library/Bb509670(v=VS.85).aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| tanf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [tanh](https://msdn.microsoft.com/library/Bb509671(v=VS.85).aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| tanhf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| tgamma | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| tgammaf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| tgammal | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [trunc](https://msdn.microsoft.com/library/Cc308065(v=VS.85).aspx) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| truncf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| truncl | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |


## APIs from api-ms-win-crt-multibyte-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| __p__mbcasemap | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| __p__mbctype | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| _ismbbalnum | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| _ismbbalnum_l | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| _ismbbalpha | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| _ismbbalpha_l | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| _ismbbblank | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| _ismbbblank_l | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| _ismbbgraph | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| _ismbbgraph_l | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| _ismbbkalnum | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| _ismbbkalnum_l | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| _ismbbkana | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| _ismbbkana_l | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| _ismbbkprint | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| _ismbbkprint_l | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| _ismbbkpunct | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| _ismbbkpunct_l | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| _ismbblead | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| _ismbblead_l | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| _ismbbprint | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| _ismbbprint_l | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| _ismbbpunct | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| _ismbbpunct_l | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| _ismbbtrail | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| _ismbbtrail_l | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| _ismbslead | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| _ismbslead_l | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| _ismbstrail | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| _ismbstrail_l | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| _mbcasemap | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| _mblen_l | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| _mbsdup | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| _mbstowcs_l | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| _mbstowcs_s_l | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| _mbstrlen | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| _mbstrlen_l | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| _mbstrnlen | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| _mbstrnlen_l | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |
| _mbtowc_l | Introduced into api-ms-win-crt-multibyte-l1-1-0.dll in 10.0.10240. |


## APIs from api-ms-win-crt-runtime-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| __control87_2 | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| __doserrno | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| __fpe_flt_rounds | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| __fpecode | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| __p___argc | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| __p___argv | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| __p___wargv | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| __p__acmdln | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| __p__pgmptr | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| __p__wcmdln | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| __p__wpgmptr | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| __pxcptinfoptrs | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| __sys_errlist | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| __sys_nerr | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| __threadhandle | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| __threadid | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| __wcserror | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| __wcserror_s | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _assert | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _beginthread | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _beginthreadex | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _c_exit | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _cexit | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _clearfp | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _configure_narrow_argv | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _configure_wide_argv | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _control87 | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _controlfp | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _controlfp_s | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _crt_at_quick_exit | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _crt_atexit | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _crt_debugger_hook | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _endthread | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _endthreadex | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _errno | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _execute_onexit_table | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _Exit | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _exit | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _fpieee_flt | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _fpreset | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _get_doserrno | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _get_errno | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _get_initial_narrow_environment | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _get_initial_wide_environment | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _get_invalid_parameter_handler | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _get_narrow_winmain_command_line | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _get_pgmptr | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _get_terminate | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _get_thread_local_invalid_parameter_handler | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _get_wide_winmain_command_line | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _get_wpgmptr | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _getpid | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _initialize_narrow_environment | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _initialize_onexit_table | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _initialize_wide_environment | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _initterm | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _initterm_e | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _invalid_parameter_noinfo | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _invalid_parameter_noinfo_noreturn | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _invoke_watson | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _query_app_type | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _register_onexit_function | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _register_thread_local_exe_atexit_callback | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _seh_filter_dll | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _seh_filter_exe | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _set_abort_behavior | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _set_app_type | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _set_controlfp | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _set_doserrno | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _set_errno | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _set_error_mode | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _set_invalid_parameter_handler | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _set_new_handler | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _set_thread_local_invalid_parameter_handler | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _sleep | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _statusfp | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _statusfp2 | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _strerror | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _strerror_s | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _wassert | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _wcserror | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _wcserror_s | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _wperror | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [abort](https://msdn.microsoft.com/library/windows/desktop/ff728669.aspx) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| exit | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| feclearexcept | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| fegetenv | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| fegetexceptflag | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| fegetround | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| feholdexcept | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| fesetenv | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| fesetexceptflag | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| fesetround | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| fetestexcept | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| perror | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| quick_exit | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [raise](https://msdn.microsoft.com/library/h1hea41c(v=VS.85).aspx) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| set_terminate | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [signal](https://msdn.microsoft.com/library/Dd798670(v=VS.85).aspx) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| strerror | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| strerror_s | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [terminate](https://msdn.microsoft.com/library/Aa372939(v=VS.85).aspx) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _seterrormode | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.17134. |
| [system](https://msdn.microsoft.com/library/Aa385207(v=VS.85).aspx) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.17134. |
| _wsystem | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.17134. |


## APIs from api-ms-win-crt-stdio-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| __acrt_iob_func | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| __p__commode | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| __p__fmode | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| __stdio_common_vfprintf | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| __stdio_common_vfprintf_p | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| __stdio_common_vfprintf_s | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| __stdio_common_vfscanf | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| __stdio_common_vfwprintf | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| __stdio_common_vfwprintf_p | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| __stdio_common_vfwprintf_s | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| __stdio_common_vfwscanf | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| __stdio_common_vsnprintf_s | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| __stdio_common_vsnwprintf_s | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| __stdio_common_vsprintf | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| __stdio_common_vsprintf_p | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| __stdio_common_vsprintf_s | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| __stdio_common_vsscanf | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| __stdio_common_vswprintf | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| __stdio_common_vswprintf_p | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| __stdio_common_vswprintf_s | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| __stdio_common_vswscanf | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _chsize | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _chsize_s | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _close | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _commit | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _creat | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _dup | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _dup2 | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _eof | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _fclose_nolock | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _fcloseall | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _fflush_nolock | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _fgetc_nolock | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _fgetchar | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _fgetwc_nolock | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _fgetwchar | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _filelength | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _filelengthi64 | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _fileno | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _flushall | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _fputc_nolock | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _fputchar | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _fputwc_nolock | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _fputwchar | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _fread_nolock | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _fread_nolock_s | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _fseek_nolock | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _fseeki64 | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _fseeki64_nolock | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _fsopen | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _ftell_nolock | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _ftelli64 | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _ftelli64_nolock | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _fwrite_nolock | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _get_fmode | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _get_osfhandle | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _get_printf_count_output | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _get_stream_buffer_pointers | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _getc_nolock | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _getmaxstdio | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _getw | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _getwc_nolock | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _getws | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _getws_s | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _isatty | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _locking | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _lseek | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _lseeki64 | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _mktemp | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _mktemp_s | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _open | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _open_osfhandle | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _putc_nolock | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _putw | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _putwc_nolock | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _putws | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _read | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _rmtmp | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _set_fmode | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _set_printf_count_output | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _setmaxstdio | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _setmode | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _sopen | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _sopen_dispatch | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _sopen_s | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _tell | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _telli64 | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _tempnam | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _ungetc_nolock | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _ungetwc_nolock | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _wcreat | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _wfdopen | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _wfopen | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _wfopen_s | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _wfreopen | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _wfreopen_s | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _wfsopen | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _wmktemp | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _wmktemp_s | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _wopen | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _write | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _wsopen | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _wsopen_dispatch | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _wsopen_s | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _wtempnam | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _wtmpnam | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| _wtmpnam_s | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| clearerr | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| clearerr_s | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| fclose | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| feof | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| ferror | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| fflush | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| fgetc | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| fgetpos | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| fgets | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| fgetwc | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| fgetws | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| fopen | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| fopen_s | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| fputc | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| fputs | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| fputwc | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| fputws | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| fread | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| fread_s | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| freopen | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| freopen_s | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| fseek | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| fsetpos | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| ftell | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| fwrite | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| getc | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| getchar | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| gets_s | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| getwc | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| getwchar | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| putc | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| putchar | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| puts | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| putwc | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| putwchar | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| rewind | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| setbuf | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| setvbuf | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| tmpfile | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| tmpfile_s | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| tmpnam | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| tmpnam_s | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| ungetc | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| ungetwc | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.10240. |
| putenv | Introduced into api-ms-win-crt-stdio-l1-1-0.dll in 10.0.17134. |


## APIs from api-ms-win-crt-string-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| __isascii | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| __iscsym | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| __iscsymf | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| __iswcsym | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| __iswcsymf | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| __strncnt | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| __wcsncnt | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _isalnum_l | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _isalpha_l | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _isblank_l | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _iscntrl_l | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _isctype | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _isctype_l | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _isdigit_l | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _isgraph_l | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _isleadbyte_l | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _islower_l | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _isprint_l | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _ispunct_l | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _isspace_l | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _isupper_l | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _iswalnum_l | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _iswalpha_l | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _iswblank_l | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _iswcntrl_l | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _iswcsym_l | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _iswcsymf_l | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _iswctype_l | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _iswdigit_l | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _iswgraph_l | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _iswlower_l | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _iswprint_l | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _iswpunct_l | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _iswspace_l | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _iswupper_l | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _iswxdigit_l | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _isxdigit_l | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _memccpy | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _memicmp | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _memicmp_l | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _strcoll_l | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _strdup | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _stricmp | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _stricmp_l | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _stricoll | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _stricoll_l | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _strlwr | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _strlwr_l | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _strlwr_s | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _strlwr_s_l | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _strncoll | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _strncoll_l | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _strnicmp | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _strnicmp_l | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _strnicoll | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _strnicoll_l | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _strnset | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _strnset_s | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _strrev | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _strset | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _strset_s | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _strupr | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _strupr_l | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _strupr_s | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _strupr_s_l | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _strxfrm_l | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _tolower | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _tolower_l | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _toupper | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _toupper_l | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _towlower_l | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _towupper_l | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _wcscoll_l | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _wcsdup | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _wcsicmp | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _wcsicmp_l | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _wcsicoll | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _wcsicoll_l | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _wcslwr | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _wcslwr_l | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _wcslwr_s | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _wcslwr_s_l | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _wcsncoll | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _wcsncoll_l | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _wcsnicmp | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _wcsnicmp_l | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _wcsnicoll | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _wcsnicoll_l | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _wcsnset | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _wcsnset_s | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _wcsrev | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _wcsset | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _wcsset_s | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _wcsupr | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _wcsupr_l | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _wcsupr_s | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _wcsupr_s_l | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _wcsxfrm_l | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| _wctype | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| isalnum | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| isalpha | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| isblank | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| iscntrl | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| isdigit | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| isgraph | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| isleadbyte | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| islower | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| isprint | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| ispunct | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| isspace | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| isupper | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| iswalnum | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| iswalpha | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| iswascii | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| iswblank | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| iswcntrl | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| iswctype | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| iswdigit | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| iswgraph | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| iswlower | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| iswprint | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| iswpunct | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| iswspace | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| iswupper | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| iswxdigit | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| isxdigit | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| mblen | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| mbrlen | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| memcpy_s | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| memset | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [strcat](https://msdn.microsoft.com/library/windows/desktop/bb759925.aspx) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| strcat_s | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [strcmp](https://msdn.microsoft.com/library/windows/desktop/bb759938.aspx) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| strcoll | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [strcpy](https://msdn.microsoft.com/library/windows/desktop/bb759960.aspx) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| strcpy_s | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [strcspn](https://msdn.microsoft.com/library/windows/desktop/bb759964.aspx) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| strlen | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [strncat](https://msdn.microsoft.com/library/windows/desktop/bb759987.aspx) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| strncat_s | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| strncmp | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| strncpy | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| strncpy_s | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| strnlen | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [strpbrk](https://msdn.microsoft.com/library/windows/desktop/bb760010.aspx) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [strspn](https://msdn.microsoft.com/library/windows/desktop/bb773435.aspx) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| strtok | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| strtok_s | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| strxfrm | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| tolower | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| toupper | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| towctrans | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| towlower | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| towupper | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| wcscat | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| wcscat_s | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| wcscmp | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| wcscoll | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| wcscpy | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| wcscpy_s | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| wcscspn | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| wcslen | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| wcsncat | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| wcsncat_s | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| wcsncmp | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| wcsncpy | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| wcsncpy_s | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| wcsnlen | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| wcspbrk | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| wcsspn | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| wcstok | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| wcstok_s | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| wcsxfrm | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| wctype | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| wmemcpy_s | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| wmemmove_s | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| memmove_s | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.16299. |


## APIs from api-ms-win-crt-time-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| __daylight | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| __dstbias | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| __timezone | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| __tzname | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| _ctime32 | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| _ctime32_s | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| _ctime64 | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| _ctime64_s | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| _difftime32 | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| _difftime64 | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| _ftime32 | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| _ftime32_s | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| _ftime64 | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| _ftime64_s | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| _futime32 | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| _futime64 | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| _get_daylight | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| _get_dstbias | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| _get_timezone | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| _get_tzname | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| _Getdays | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| _Getmonths | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| _Gettnames | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| _gmtime32 | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| _gmtime32_s | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| _gmtime64 | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| _gmtime64_s | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| _localtime32 | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| _localtime32_s | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| _localtime64 | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| _localtime64_s | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| _mkgmtime32 | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| _mkgmtime64 | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| _mktime32 | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| _mktime64 | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| _strdate | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| _strdate_s | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| _Strftime | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| _strftime_l | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| _strtime | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| _strtime_s | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| _time32 | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| _time64 | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| _timespec32_get | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| _timespec64_get | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| _tzset | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| _utime32 | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| _utime64 | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| _W_Getdays | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| _W_Getmonths | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| _W_Gettnames | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| _wasctime | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| _wasctime_s | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| _Wcsftime | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| _wcsftime_l | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| _wctime32 | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| _wctime32_s | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| _wctime64 | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| _wctime64_s | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| _wstrdate | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| _wstrdate_s | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| _wstrtime | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| _wstrtime_s | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| _wutime32 | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| _wutime64 | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| asctime | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| asctime_s | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| clock | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| strftime | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |
| wcsftime | Introduced into api-ms-win-crt-time-l1-1-0.dll in 10.0.10240. |


## APIs from api-ms-win-crt-utility-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| _abs64 | Introduced into api-ms-win-crt-utility-l1-1-0.dll in 10.0.10240. |
| _byteswap_uint64 | Introduced into api-ms-win-crt-utility-l1-1-0.dll in 10.0.10240. |
| _byteswap_ulong | Introduced into api-ms-win-crt-utility-l1-1-0.dll in 10.0.10240. |
| _byteswap_ushort | Introduced into api-ms-win-crt-utility-l1-1-0.dll in 10.0.10240. |
| _lfind | Introduced into api-ms-win-crt-utility-l1-1-0.dll in 10.0.10240. |
| _lfind_s | Introduced into api-ms-win-crt-utility-l1-1-0.dll in 10.0.10240. |
| _lrotl | Introduced into api-ms-win-crt-utility-l1-1-0.dll in 10.0.10240. |
| _lrotr | Introduced into api-ms-win-crt-utility-l1-1-0.dll in 10.0.10240. |
| _lsearch | Introduced into api-ms-win-crt-utility-l1-1-0.dll in 10.0.10240. |
| _lsearch_s | Introduced into api-ms-win-crt-utility-l1-1-0.dll in 10.0.10240. |
| _rotl | Introduced into api-ms-win-crt-utility-l1-1-0.dll in 10.0.10240. |
| _rotl64 | Introduced into api-ms-win-crt-utility-l1-1-0.dll in 10.0.10240. |
| _rotr | Introduced into api-ms-win-crt-utility-l1-1-0.dll in 10.0.10240. |
| _rotr64 | Introduced into api-ms-win-crt-utility-l1-1-0.dll in 10.0.10240. |
| _swab | Introduced into api-ms-win-crt-utility-l1-1-0.dll in 10.0.10240. |
| [abs](https://msdn.microsoft.com/library/307330xe(v=VS.85).aspx) | Introduced into api-ms-win-crt-utility-l1-1-0.dll in 10.0.10240. |
| bsearch | Introduced into api-ms-win-crt-utility-l1-1-0.dll in 10.0.10240. |
| bsearch_s | Introduced into api-ms-win-crt-utility-l1-1-0.dll in 10.0.10240. |
| [div](https://msdn.microsoft.com/library/ms535240(v=VS.85).aspx) | Introduced into api-ms-win-crt-utility-l1-1-0.dll in 10.0.10240. |
| imaxabs | Introduced into api-ms-win-crt-utility-l1-1-0.dll in 10.0.10240. |
| imaxdiv | Introduced into api-ms-win-crt-utility-l1-1-0.dll in 10.0.10240. |
| labs | Introduced into api-ms-win-crt-utility-l1-1-0.dll in 10.0.10240. |
| ldiv | Introduced into api-ms-win-crt-utility-l1-1-0.dll in 10.0.10240. |
| llabs | Introduced into api-ms-win-crt-utility-l1-1-0.dll in 10.0.10240. |
| lldiv | Introduced into api-ms-win-crt-utility-l1-1-0.dll in 10.0.10240. |
| qsort | Introduced into api-ms-win-crt-utility-l1-1-0.dll in 10.0.10240. |
| qsort_s | Introduced into api-ms-win-crt-utility-l1-1-0.dll in 10.0.10240. |
| rand | Introduced into api-ms-win-crt-utility-l1-1-0.dll in 10.0.10240. |
| rand_s | Introduced into api-ms-win-crt-utility-l1-1-0.dll in 10.0.10240. |
| srand | Introduced into api-ms-win-crt-utility-l1-1-0.dll in 10.0.10240. |


## APIs from api-ms-win-gaming-tcui-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| CheckGamingPrivilegeSilently | Introduced into api-ms-win-gaming-tcui-l1-1-0.dll in 10.0.10586. Removed in 10.0.14393. |
| [CheckGamingPrivilegeWithUI](https://msdn.microsoft.com/library/Mt736760(v=VS.85).aspx) | Introduced into api-ms-win-gaming-tcui-l1-1-0.dll in 10.0.10586. Removed in 10.0.14393. |


## APIs from winsqlite3.dll

| API | Requirements |
| -----| --------------|
| sqlite3_aggregate_context | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_aggregate_count | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_auto_extension | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_backup_finish | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_backup_init | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_backup_pagecount | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_backup_remaining | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_backup_step | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_bind_blob | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_bind_blob64 | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_bind_double | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_bind_int | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_bind_int64 | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_bind_null | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_bind_parameter_count | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_bind_parameter_index | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_bind_parameter_name | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_bind_text | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_bind_text16 | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_bind_text64 | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_bind_value | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_bind_zeroblob | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_blob_bytes | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_blob_close | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_blob_open | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_blob_read | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_blob_reopen | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_blob_write | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_busy_handler | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_busy_timeout | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_cancel_auto_extension | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_changes | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_clear_bindings | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_close | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_close_v2 | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_collation_needed | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_collation_needed16 | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_column_blob | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_column_bytes | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_column_bytes16 | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_column_count | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_column_database_name | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_column_database_name16 | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_column_decltype | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_column_decltype16 | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_column_double | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_column_int | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_column_int64 | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_column_name | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_column_name16 | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_column_origin_name | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_column_origin_name16 | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_column_table_name | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_column_table_name16 | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_column_text | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_column_text16 | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_column_type | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_column_value | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_commit_hook | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_compileoption_get | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_compileoption_used | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_complete | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_complete16 | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_config | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_context_db_handle | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_create_collation | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_create_collation16 | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_create_collation_v2 | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_create_function | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_create_function16 | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_create_function_v2 | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_create_module | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_create_module_v2 | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_data_count | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_data_directory | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_db_config | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_db_filename | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_db_handle | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_db_mutex | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_db_readonly | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_db_release_memory | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_db_status | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_declare_vtab | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_enable_load_extension | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_enable_shared_cache | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_errcode | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_errmsg | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_errmsg16 | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_errstr | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_exec | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_expired | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_extended_errcode | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_extended_result_codes | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_file_control | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_finalize | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_free | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_free_table | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_get_autocommit | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_get_auxdata | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_get_table | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_global_recover | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_initialize | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_interrupt | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_last_insert_rowid | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_libversion | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_libversion_number | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_limit | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_load_extension | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_log | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_malloc | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_malloc64 | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_memory_alarm | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_memory_highwater | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_memory_used | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_mprintf | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_msize | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_mutex_alloc | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_mutex_enter | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_mutex_free | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_mutex_leave | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_mutex_try | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_next_stmt | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_open | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_open16 | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_open_v2 | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_os_end | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_os_init | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_overload_function | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_prepare | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_prepare16 | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_prepare16_v2 | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_prepare_v2 | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_profile | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_progress_handler | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_randomness | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_realloc | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_realloc64 | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_release_memory | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_reset | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_reset_auto_extension | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_result_blob | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_result_blob64 | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_result_double | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_result_error | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_result_error16 | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_result_error_code | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_result_error_nomem | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_result_error_toobig | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_result_int | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_result_int64 | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_result_null | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_result_text | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_result_text16 | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_result_text16be | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_result_text16le | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_result_text64 | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_result_value | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_result_zeroblob | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_rollback_hook | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_rtree_geometry_callback | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_rtree_query_callback | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_set_authorizer | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_set_auxdata | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_shutdown | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_sleep | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_snprintf | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_soft_heap_limit | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_soft_heap_limit64 | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_sourceid | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_sql | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_status | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_step | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_stmt_busy | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_stmt_readonly | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_stmt_status | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_strglob | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_stricmp | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_strnicmp | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_table_column_metadata | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_temp_directory | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_test_control | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_thread_cleanup | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_threadsafe | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_total_changes | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_trace | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_transfer_bindings | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_update_hook | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_uri_boolean | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_uri_int64 | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_uri_parameter | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_user_data | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_value_blob | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_value_bytes | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_value_bytes16 | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_value_double | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_value_int | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_value_int64 | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_value_numeric_type | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_value_text | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_value_text16 | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_value_text16be | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_value_text16le | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_value_type | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_version | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_vfs_find | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_vfs_register | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_vfs_unregister | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_vmprintf | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_vsnprintf | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_vtab_config | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_vtab_on_conflict | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_wal_autocheckpoint | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_wal_checkpoint | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_wal_checkpoint_v2 | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_wal_hook | Introduced into winsqlite3.dll in 10.0.10586. |
| sqlite3_bind_zeroblob64 | Introduced into winsqlite3.dll in 10.0.14393. |
| sqlite3_db_cacheflush | Introduced into winsqlite3.dll in 10.0.14393. |
| sqlite3_result_subtype | Introduced into winsqlite3.dll in 10.0.14393. |
| sqlite3_result_zeroblob64 | Introduced into winsqlite3.dll in 10.0.14393. |
| sqlite3_status64 | Introduced into winsqlite3.dll in 10.0.14393. |
| sqlite3_strlike | Introduced into winsqlite3.dll in 10.0.14393. |
| sqlite3_system_errno | Introduced into winsqlite3.dll in 10.0.14393. |
| sqlite3_value_dup | Introduced into winsqlite3.dll in 10.0.14393. |
| sqlite3_value_free | Introduced into winsqlite3.dll in 10.0.14393. |
| sqlite3_value_subtype | Introduced into winsqlite3.dll in 10.0.14393. |
| sqlite3_expanded_sql | Introduced into winsqlite3.dll in 10.0.16299. |
| sqlite3_set_last_insert_rowid | Introduced into winsqlite3.dll in 10.0.16299. |
| sqlite3_trace_v2 | Introduced into winsqlite3.dll in 10.0.16299. |
| sqlite3_bind_pointer | Introduced into winsqlite3.dll in 10.0.17134. |
| sqlite3_prepare16_v3 | Introduced into winsqlite3.dll in 10.0.17134. |
| sqlite3_prepare_v3 | Introduced into winsqlite3.dll in 10.0.17134. |
| sqlite3_result_pointer | Introduced into winsqlite3.dll in 10.0.17134. |
| sqlite3_value_pointer | Introduced into winsqlite3.dll in 10.0.17134. |
| sqlite3_value_nochange | Introduced into winsqlite3.dll in 10.0.17763. |
| sqlite3_vtab_collation | Introduced into winsqlite3.dll in 10.0.17763. |
| sqlite3_vtab_nochange | Introduced into winsqlite3.dll in 10.0.17763. |
| sqlite3_win32_set_directory | Introduced into winsqlite3.dll in 10.0.17763. |
| sqlite3_win32_set_directory16 | Introduced into winsqlite3.dll in 10.0.17763. |
| sqlite3_win32_set_directory8 | Introduced into winsqlite3.dll in 10.0.17763. |


## APIs from user32.dll

| API | Requirements |
| -----| --------------|
| [SoundSentry](https://msdn.microsoft.com/library/aa969269.aspx) | Introduced into user32.dll in 10.0.14393. |
| [GetKeyNameTextA](https://msdn.microsoft.com/library/windows/desktop/ms646300.aspx) | Introduced into user32.dll in 10.0.14393. |
| [GetKeyNameTextW](https://msdn.microsoft.com/library/ms646300.aspx) | Introduced into user32.dll in 10.0.14393. |
| [MapVirtualKeyA](https://msdn.microsoft.com/library/ms646306.aspx) | Introduced into user32.dll in 10.0.14393. |
| [MapVirtualKeyW](https://msdn.microsoft.com/library/ms646306.aspx) | Introduced into user32.dll in 10.0.14393. |
| [MapVirtualKeyExA](https://msdn.microsoft.com/library/windows/desktop/ms646307.aspx) | Introduced into user32.dll in 10.0.14393. |
| [MapVirtualKeyExW](https://msdn.microsoft.com/library/ms646307.aspx) | Introduced into user32.dll in 10.0.14393. |
| [ClipCursor](https://msdn.microsoft.com/library/ms648383(v=VS.85).aspx) | Introduced into user32.dll in 10.0.16299. |
| [GetKeyState](https://msdn.microsoft.com/library/ms646301(v=VS.85).aspx) | Introduced into user32.dll in 10.0.16299. |
| [GetLastInputInfo](https://msdn.microsoft.com/library/ms646302(v=VS.85).aspx) | Introduced into user32.dll in 10.0.16299. |


## APIs from ResetPhoneForArm32.dll

| API | Requirements |
| -----| --------------|
| ResetPhoneForArm32 | Introduced into ResetPhoneForArm32.dll in 10.0.16299. |


## APIs from Credui.dll

| API | Requirements |
| -----| --------------|
| [CredUIParseUserNameW](https://msdn.microsoft.com/library/Aa375175(v=VS.85).aspx) | Introduced into Credui.dll in 10.0.16299. |


## APIs from ntdll.dll

| API | Requirements |
| -----| --------------|
| [NtQueryDirectoryFile](https://msdn.microsoft.com/library/Ff556633(v=VS.85).aspx) | Introduced into ntdll.dll in 10.0.16299. |
| [RtlEthernetAddressToString](https://msdn.microsoft.com/library/Dn550721(v=VS.85).aspx) | Introduced into ntdll.dll in 10.0.16299. Removed in 10.0.17134. |
| [RtlEthernetStringToAddress](https://msdn.microsoft.com/library/Dn550722(v=VS.85).aspx) | Introduced into ntdll.dll in 10.0.16299. Removed in 10.0.17134. |
| [RtlIpv4AddressToString](https://msdn.microsoft.com/library/Aa814456(v=VS.85).aspx) | Introduced into ntdll.dll in 10.0.16299. Removed in 10.0.17134. |
| [RtlIpv4AddressToStringEx](https://msdn.microsoft.com/library/windows/desktop/aa814457.aspx) | Introduced into ntdll.dll in 10.0.16299. Removed in 10.0.17134. |
| [RtlIpv4StringToAddress](https://msdn.microsoft.com/library/Aa814458(v=VS.85).aspx) | Introduced into ntdll.dll in 10.0.16299. Removed in 10.0.17134. |
| [RtlIpv4StringToAddressEx](https://msdn.microsoft.com/library/Aa814459(v=VS.85).aspx) | Introduced into ntdll.dll in 10.0.16299. Removed in 10.0.17134. |
| [RtlIpv6AddressToString](https://msdn.microsoft.com/library/Aa814460(v=VS.85).aspx) | Introduced into ntdll.dll in 10.0.16299. Removed in 10.0.17134. |
| [RtlIpv6AddressToStringEx](https://msdn.microsoft.com/library/Aa814461(v=VS.85).aspx) | Introduced into ntdll.dll in 10.0.16299. Removed in 10.0.17134. |
| [RtlIpv6StringToAddress](https://msdn.microsoft.com/library/Aa814462(v=VS.85).aspx) | Introduced into ntdll.dll in 10.0.16299. Removed in 10.0.17134. |
| [RtlIpv6StringToAddressEx](https://msdn.microsoft.com/library/Aa814463(v=VS.85).aspx) | Introduced into ntdll.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from OPMXbox.dll

| API | Requirements |
| -----| --------------|
| OPMXboxEnableHDCP | Introduced into OPMXbox.dll in 10.0.16299. |
| OPMXboxGetHDCPStatus | Introduced into OPMXbox.dll in 10.0.16299. |
| OPMXboxGetHDCPStatusAndType | Introduced into OPMXbox.dll in 10.0.16299. |


## APIs from efswrt.dll

| API | Requirements |
| -----| --------------|
| [ProtectFileToEnterpriseIdentity](https://msdn.microsoft.com/library/Mt622168(v=VS.85).aspx) | Introduced into efswrt.dll in 10.0.16299. |
| UnprotectFile | Introduced into efswrt.dll in 10.0.16299. |


## APIs from wer.dll

| API | Requirements |
| -----| --------------|
| [WerStoreOpen](https://msdn.microsoft.com/library/Mt492590(v=VS.85).aspx) | Introduced into wer.dll in 10.0.16299. |
| [WerStoreClose](https://msdn.microsoft.com/library/Mt796907(v=VS.85).aspx) | Introduced into wer.dll in 10.0.16299. |
| [WerFreeString](https://msdn.microsoft.com/library/Mt492584(v=VS.85).aspx) | Introduced into wer.dll in 10.0.16299. |
| [WerStoreGetFirstReportKey](https://msdn.microsoft.com/library/Mt492588(v=VS.85).aspx) | Introduced into wer.dll in 10.0.16299. |
| [WerStoreGetNextReportKey](https://msdn.microsoft.com/library/Mt492589(v=VS.85).aspx) | Introduced into wer.dll in 10.0.16299. |
| [WerStoreQueryReportMetadataV2](https://msdn.microsoft.com/library/Mt492591(v=VS.85).aspx) | Introduced into wer.dll in 10.0.16299. |
| [WerReportCreate](https://msdn.microsoft.com/library/Bb513625(v=VS.85).aspx) | Introduced into wer.dll in 10.0.16299. |
| [WerReportSetParameter](https://msdn.microsoft.com/library/Bb513626(v=VS.85).aspx) | Introduced into wer.dll in 10.0.16299. |
| [WerReportAddFile](https://msdn.microsoft.com/library/Bb513623(v=VS.85).aspx) | Introduced into wer.dll in 10.0.16299. |
| [WerReportSubmit](https://msdn.microsoft.com/library/Bb513628(v=VS.85).aspx) | Introduced into wer.dll in 10.0.16299. |
| [WerReportAddDump](https://msdn.microsoft.com/library/Bb513622(v=VS.85).aspx) | Introduced into wer.dll in 10.0.16299. |
| [WerReportCloseHandle](https://msdn.microsoft.com/library/Bb513624(v=VS.85).aspx) | Introduced into wer.dll in 10.0.16299. |


## APIs from atiadlxx.dll

| API | Requirements |
| -----| --------------|
| ADL2_Main_Control_GetProcAddress | Introduced into atiadlxx.dll in 10.0.16299. Moved into atiadlxy.dll in 10.0.16299. Moved into atiadlxx.dll in 10.0.17134. Moved into atiadlxy.dll in 10.0.17134. Moved into atiadlxx.dll in 10.0.17763. Moved into atiadlxy.dll in 10.0.17763. |


## APIs from aticfx32.dll

| API | Requirements |
| -----| --------------|
| AmdGetCfxModuleHandle | Introduced into aticfx32.dll in 10.0.16299. Moved into aticfx64.dll in 10.0.16299. Moved into aticfx32.dll in 10.0.17134. Moved into aticfx64.dll in 10.0.17134. Moved into aticfx32.dll in 10.0.17763. Moved into aticfx64.dll in 10.0.17763. |


## APIs from amdxc32.dll

| API | Requirements |
| -----| --------------|
| AmdGetDxcModuleHandle | Introduced into amdxc32.dll in 10.0.16299. Moved into amdxc64.dll in 10.0.16299. Moved into amdxc32.dll in 10.0.17134. Moved into amdxc64.dll in 10.0.17134. Moved into amdxc32.dll in 10.0.17763. Moved into amdxc64.dll in 10.0.17763. |


## APIs from atidxx32.dll

| API | Requirements |
| -----| --------------|
| AmdGetDxxModuleHandle | Introduced into atidxx32.dll in 10.0.16299. Moved into atidxx64.dll in 10.0.16299. Moved into atidxx32.dll in 10.0.17134. Moved into atidxx64.dll in 10.0.17134. Moved into atidxx32.dll in 10.0.17763. Moved into atidxx64.dll in 10.0.17763. |


## APIs from nvapi.dll

| API | Requirements |
| -----| --------------|
| nvapi_QueryInterface | Introduced into nvapi.dll in 10.0.16299. Moved into nvapi64.dll in 10.0.16299. Moved into nvapi.dll in 10.0.17134. Moved into nvapi64.dll in 10.0.17134. Moved into nvapi.dll in 10.0.17763. Moved into nvapi64.dll in 10.0.17763. |


## APIs from icuuc.dll

| API | Requirements |
| -----| --------------|
| utf8_nextCharSafeBody | Introduced into icuuc.dll in 10.0.16299. |
| utf8_appendCharSafeBody | Introduced into icuuc.dll in 10.0.16299. |
| utf8_prevCharSafeBody | Introduced into icuuc.dll in 10.0.16299. |
| utf8_back1SafeBody | Introduced into icuuc.dll in 10.0.16299. |
| u_versionFromString | Introduced into icuuc.dll in 10.0.16299. |
| u_versionFromUString | Introduced into icuuc.dll in 10.0.16299. |
| u_versionToString | Introduced into icuuc.dll in 10.0.16299. |
| u_getVersion | Introduced into icuuc.dll in 10.0.16299. |
| u_errorName | Introduced into icuuc.dll in 10.0.16299. |
| utrace_setLevel | Introduced into icuuc.dll in 10.0.16299. |
| utrace_getLevel | Introduced into icuuc.dll in 10.0.16299. |
| utrace_setFunctions | Introduced into icuuc.dll in 10.0.16299. |
| utrace_getFunctions | Introduced into icuuc.dll in 10.0.16299. |
| utrace_vformat | Introduced into icuuc.dll in 10.0.16299. |
| utrace_format | Introduced into icuuc.dll in 10.0.16299. |
| utrace_functionName | Introduced into icuuc.dll in 10.0.16299. |
| u_shapeArabic | Introduced into icuuc.dll in 10.0.16299. |
| uscript_getCode | Introduced into icuuc.dll in 10.0.16299. |
| uscript_getName | Introduced into icuuc.dll in 10.0.16299. |
| uscript_getShortName | Introduced into icuuc.dll in 10.0.16299. |
| uscript_getScript | Introduced into icuuc.dll in 10.0.16299. |
| uscript_hasScript | Introduced into icuuc.dll in 10.0.16299. |
| uscript_getScriptExtensions | Introduced into icuuc.dll in 10.0.16299. |
| uscript_getSampleString | Introduced into icuuc.dll in 10.0.16299. |
| uscript_getUsage | Introduced into icuuc.dll in 10.0.16299. |
| uscript_isRightToLeft | Introduced into icuuc.dll in 10.0.16299. |
| uscript_breaksBetweenLetters | Introduced into icuuc.dll in 10.0.16299. |
| uscript_isCased | Introduced into icuuc.dll in 10.0.16299. |
| ulistfmt_open | Introduced into icuuc.dll in 10.0.16299. |
| ulistfmt_close | Introduced into icuuc.dll in 10.0.16299. |
| ulistfmt_format | Introduced into icuuc.dll in 10.0.16299. |
| uiter_current32 | Introduced into icuuc.dll in 10.0.16299. |
| uiter_next32 | Introduced into icuuc.dll in 10.0.16299. |
| uiter_previous32 | Introduced into icuuc.dll in 10.0.16299. |
| uiter_getState | Introduced into icuuc.dll in 10.0.16299. |
| uiter_setState | Introduced into icuuc.dll in 10.0.16299. |
| uiter_setString | Introduced into icuuc.dll in 10.0.16299. |
| uiter_setUTF16BE | Introduced into icuuc.dll in 10.0.16299. |
| uiter_setUTF8 | Introduced into icuuc.dll in 10.0.16299. |
| uenum_close | Introduced into icuuc.dll in 10.0.16299. |
| uenum_count | Introduced into icuuc.dll in 10.0.16299. |
| uenum_unext | Introduced into icuuc.dll in 10.0.16299. |
| uenum_next | Introduced into icuuc.dll in 10.0.16299. |
| uenum_reset | Introduced into icuuc.dll in 10.0.16299. |
| uenum_openUCharStringsEnumeration | Introduced into icuuc.dll in 10.0.16299. |
| uenum_openCharStringsEnumeration | Introduced into icuuc.dll in 10.0.16299. |
| uloc_getDefault | Introduced into icuuc.dll in 10.0.16299. |
| uloc_setDefault | Introduced into icuuc.dll in 10.0.16299. |
| uloc_getLanguage | Introduced into icuuc.dll in 10.0.16299. |
| uloc_getScript | Introduced into icuuc.dll in 10.0.16299. |
| uloc_getCountry | Introduced into icuuc.dll in 10.0.16299. |
| uloc_getVariant | Introduced into icuuc.dll in 10.0.16299. |
| uloc_getName | Introduced into icuuc.dll in 10.0.16299. |
| uloc_canonicalize | Introduced into icuuc.dll in 10.0.16299. |
| uloc_getISO3Language | Introduced into icuuc.dll in 10.0.16299. |
| uloc_getISO3Country | Introduced into icuuc.dll in 10.0.16299. |
| uloc_getLCID | Introduced into icuuc.dll in 10.0.16299. |
| uloc_getDisplayLanguage | Introduced into icuuc.dll in 10.0.16299. |
| uloc_getDisplayScript | Introduced into icuuc.dll in 10.0.16299. |
| uloc_getDisplayCountry | Introduced into icuuc.dll in 10.0.16299. |
| uloc_getDisplayVariant | Introduced into icuuc.dll in 10.0.16299. |
| uloc_getDisplayKeyword | Introduced into icuuc.dll in 10.0.16299. |
| uloc_getDisplayKeywordValue | Introduced into icuuc.dll in 10.0.16299. |
| uloc_getDisplayName | Introduced into icuuc.dll in 10.0.16299. |
| uloc_getAvailable | Introduced into icuuc.dll in 10.0.16299. |
| uloc_countAvailable | Introduced into icuuc.dll in 10.0.16299. |
| uloc_getISOLanguages | Introduced into icuuc.dll in 10.0.16299. |
| uloc_getISOCountries | Introduced into icuuc.dll in 10.0.16299. |
| uloc_getParent | Introduced into icuuc.dll in 10.0.16299. |
| uloc_getBaseName | Introduced into icuuc.dll in 10.0.16299. |
| uloc_openKeywords | Introduced into icuuc.dll in 10.0.16299. |
| uloc_getKeywordValue | Introduced into icuuc.dll in 10.0.16299. |
| uloc_setKeywordValue | Introduced into icuuc.dll in 10.0.16299. |
| uloc_isRightToLeft | Introduced into icuuc.dll in 10.0.16299. |
| uloc_getCharacterOrientation | Introduced into icuuc.dll in 10.0.16299. |
| uloc_getLineOrientation | Introduced into icuuc.dll in 10.0.16299. |
| uloc_acceptLanguageFromHTTP | Introduced into icuuc.dll in 10.0.16299. |
| uloc_acceptLanguage | Introduced into icuuc.dll in 10.0.16299. |
| uloc_getLocaleForLCID | Introduced into icuuc.dll in 10.0.16299. |
| uloc_addLikelySubtags | Introduced into icuuc.dll in 10.0.16299. |
| uloc_minimizeSubtags | Introduced into icuuc.dll in 10.0.16299. |
| uloc_forLanguageTag | Introduced into icuuc.dll in 10.0.16299. |
| uloc_toLanguageTag | Introduced into icuuc.dll in 10.0.16299. |
| uloc_toUnicodeLocaleKey | Introduced into icuuc.dll in 10.0.16299. |
| uloc_toUnicodeLocaleType | Introduced into icuuc.dll in 10.0.16299. |
| uloc_toLegacyKey | Introduced into icuuc.dll in 10.0.16299. |
| uloc_toLegacyType | Introduced into icuuc.dll in 10.0.16299. |
| ures_open | Introduced into icuuc.dll in 10.0.16299. |
| ures_openDirect | Introduced into icuuc.dll in 10.0.16299. |
| ures_openU | Introduced into icuuc.dll in 10.0.16299. |
| ures_close | Introduced into icuuc.dll in 10.0.16299. |
| ures_getVersion | Introduced into icuuc.dll in 10.0.16299. |
| ures_getLocaleByType | Introduced into icuuc.dll in 10.0.16299. |
| ures_getString | Introduced into icuuc.dll in 10.0.16299. |
| ures_getUTF8String | Introduced into icuuc.dll in 10.0.16299. |
| ures_getBinary | Introduced into icuuc.dll in 10.0.16299. |
| ures_getIntVector | Introduced into icuuc.dll in 10.0.16299. |
| ures_getUInt | Introduced into icuuc.dll in 10.0.16299. |
| ures_getInt | Introduced into icuuc.dll in 10.0.16299. |
| ures_getSize | Introduced into icuuc.dll in 10.0.16299. |
| ures_getType | Introduced into icuuc.dll in 10.0.16299. |
| ures_getKey | Introduced into icuuc.dll in 10.0.16299. |
| ures_resetIterator | Introduced into icuuc.dll in 10.0.16299. |
| ures_hasNext | Introduced into icuuc.dll in 10.0.16299. |
| ures_getNextResource | Introduced into icuuc.dll in 10.0.16299. |
| ures_getNextString | Introduced into icuuc.dll in 10.0.16299. |
| ures_getByIndex | Introduced into icuuc.dll in 10.0.16299. |
| ures_getStringByIndex | Introduced into icuuc.dll in 10.0.16299. |
| ures_getUTF8StringByIndex | Introduced into icuuc.dll in 10.0.16299. |
| ures_getByKey | Introduced into icuuc.dll in 10.0.16299. |
| ures_getStringByKey | Introduced into icuuc.dll in 10.0.16299. |
| ures_getUTF8StringByKey | Introduced into icuuc.dll in 10.0.16299. |
| ures_openAvailableLocales | Introduced into icuuc.dll in 10.0.16299. |
| uldn_open | Introduced into icuuc.dll in 10.0.16299. |
| uldn_close | Introduced into icuuc.dll in 10.0.16299. |
| uldn_getLocale | Introduced into icuuc.dll in 10.0.16299. |
| uldn_getDialectHandling | Introduced into icuuc.dll in 10.0.16299. |
| uldn_localeDisplayName | Introduced into icuuc.dll in 10.0.16299. |
| uldn_languageDisplayName | Introduced into icuuc.dll in 10.0.16299. |
| uldn_scriptDisplayName | Introduced into icuuc.dll in 10.0.16299. |
| uldn_scriptCodeDisplayName | Introduced into icuuc.dll in 10.0.16299. |
| uldn_regionDisplayName | Introduced into icuuc.dll in 10.0.16299. |
| uldn_variantDisplayName | Introduced into icuuc.dll in 10.0.16299. |
| uldn_keyDisplayName | Introduced into icuuc.dll in 10.0.16299. |
| uldn_keyValueDisplayName | Introduced into icuuc.dll in 10.0.16299. |
| uldn_openForContext | Introduced into icuuc.dll in 10.0.16299. |
| uldn_getContext | Introduced into icuuc.dll in 10.0.16299. |
| ucurr_forLocale | Introduced into icuuc.dll in 10.0.16299. |
| ucurr_register | Introduced into icuuc.dll in 10.0.16299. |
| ucurr_unregister | Introduced into icuuc.dll in 10.0.16299. |
| ucurr_getName | Introduced into icuuc.dll in 10.0.16299. |
| ucurr_getPluralName | Introduced into icuuc.dll in 10.0.16299. |
| ucurr_getDefaultFractionDigits | Introduced into icuuc.dll in 10.0.16299. |
| ucurr_getDefaultFractionDigitsForUsage | Introduced into icuuc.dll in 10.0.16299. |
| ucurr_getRoundingIncrement | Introduced into icuuc.dll in 10.0.16299. |
| ucurr_getRoundingIncrementForUsage | Introduced into icuuc.dll in 10.0.16299. |
| ucurr_openISOCurrencies | Introduced into icuuc.dll in 10.0.16299. |
| ucurr_isAvailable | Introduced into icuuc.dll in 10.0.16299. |
| ucurr_countCurrencies | Introduced into icuuc.dll in 10.0.16299. |
| ucurr_forLocaleAndDate | Introduced into icuuc.dll in 10.0.16299. |
| ucurr_getKeywordValuesForLocale | Introduced into icuuc.dll in 10.0.16299. |
| ucurr_getNumericCode | Introduced into icuuc.dll in 10.0.16299. |
| UCNV_FROM_U_CALLBACK_STOP | Introduced into icuuc.dll in 10.0.16299. |
| UCNV_TO_U_CALLBACK_STOP | Introduced into icuuc.dll in 10.0.16299. |
| UCNV_FROM_U_CALLBACK_SKIP | Introduced into icuuc.dll in 10.0.16299. |
| UCNV_FROM_U_CALLBACK_SUBSTITUTE | Introduced into icuuc.dll in 10.0.16299. |
| UCNV_FROM_U_CALLBACK_ESCAPE | Introduced into icuuc.dll in 10.0.16299. |
| UCNV_TO_U_CALLBACK_SKIP | Introduced into icuuc.dll in 10.0.16299. |
| UCNV_TO_U_CALLBACK_SUBSTITUTE | Introduced into icuuc.dll in 10.0.16299. |
| UCNV_TO_U_CALLBACK_ESCAPE | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_compareNames | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_open | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_openU | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_openCCSID | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_openPackage | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_safeClone | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_close | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_getSubstChars | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_setSubstChars | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_setSubstString | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_getInvalidChars | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_getInvalidUChars | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_reset | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_resetToUnicode | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_resetFromUnicode | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_getMaxCharSize | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_getMinCharSize | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_getDisplayName | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_getName | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_getCCSID | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_getPlatform | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_getType | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_getStarters | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_getUnicodeSet | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_getToUCallBack | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_getFromUCallBack | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_setToUCallBack | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_setFromUCallBack | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_fromUnicode | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_toUnicode | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_fromUChars | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_toUChars | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_getNextUChar | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_convertEx | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_convert | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_toAlgorithmic | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_fromAlgorithmic | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_flushCache | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_countAvailable | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_getAvailableName | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_openAllNames | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_countAliases | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_getAlias | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_getAliases | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_openStandardNames | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_countStandards | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_getStandard | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_getStandardName | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_getCanonicalName | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_getDefaultName | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_setDefaultName | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_fixFileSeparator | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_isAmbiguous | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_setFallback | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_usesFallback | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_detectUnicodeSignature | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_fromUCountPending | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_toUCountPending | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_isFixedWidth | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_cbFromUWriteBytes | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_cbFromUWriteSub | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_cbFromUWriteUChars | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_cbToUWriteUChars | Introduced into icuuc.dll in 10.0.16299. |
| ucnv_cbToUWriteSub | Introduced into icuuc.dll in 10.0.16299. |
| u_init | Introduced into icuuc.dll in 10.0.16299. |
| u_cleanup | Introduced into icuuc.dll in 10.0.16299. |
| u_setMemoryFunctions | Introduced into icuuc.dll in 10.0.16299. |
| u_hasBinaryProperty | Introduced into icuuc.dll in 10.0.16299. |
| u_isUAlphabetic | Introduced into icuuc.dll in 10.0.16299. |
| u_isULowercase | Introduced into icuuc.dll in 10.0.16299. |
| u_isUUppercase | Introduced into icuuc.dll in 10.0.16299. |
| u_isUWhiteSpace | Introduced into icuuc.dll in 10.0.16299. |
| u_getIntPropertyValue | Introduced into icuuc.dll in 10.0.16299. |
| u_getIntPropertyMinValue | Introduced into icuuc.dll in 10.0.16299. |
| u_getIntPropertyMaxValue | Introduced into icuuc.dll in 10.0.16299. |
| u_getNumericValue | Introduced into icuuc.dll in 10.0.16299. |
| u_islower | Introduced into icuuc.dll in 10.0.16299. |
| u_isupper | Introduced into icuuc.dll in 10.0.16299. |
| u_istitle | Introduced into icuuc.dll in 10.0.16299. |
| u_isdigit | Introduced into icuuc.dll in 10.0.16299. |
| u_isalpha | Introduced into icuuc.dll in 10.0.16299. |
| u_isalnum | Introduced into icuuc.dll in 10.0.16299. |
| u_isxdigit | Introduced into icuuc.dll in 10.0.16299. |
| u_ispunct | Introduced into icuuc.dll in 10.0.16299. |
| u_isgraph | Introduced into icuuc.dll in 10.0.16299. |
| u_isblank | Introduced into icuuc.dll in 10.0.16299. |
| u_isdefined | Introduced into icuuc.dll in 10.0.16299. |
| u_isspace | Introduced into icuuc.dll in 10.0.16299. |
| u_isJavaSpaceChar | Introduced into icuuc.dll in 10.0.16299. |
| u_isWhitespace | Introduced into icuuc.dll in 10.0.16299. |
| u_iscntrl | Introduced into icuuc.dll in 10.0.16299. |
| u_isISOControl | Introduced into icuuc.dll in 10.0.16299. |
| u_isprint | Introduced into icuuc.dll in 10.0.16299. |
| u_isbase | Introduced into icuuc.dll in 10.0.16299. |
| u_charDirection | Introduced into icuuc.dll in 10.0.16299. |
| u_isMirrored | Introduced into icuuc.dll in 10.0.16299. |
| u_charMirror | Introduced into icuuc.dll in 10.0.16299. |
| u_getBidiPairedBracket | Introduced into icuuc.dll in 10.0.16299. |
| u_charType | Introduced into icuuc.dll in 10.0.16299. |
| u_enumCharTypes | Introduced into icuuc.dll in 10.0.16299. |
| u_getCombiningClass | Introduced into icuuc.dll in 10.0.16299. |
| u_charDigitValue | Introduced into icuuc.dll in 10.0.16299. |
| ublock_getCode | Introduced into icuuc.dll in 10.0.16299. |
| u_charName | Introduced into icuuc.dll in 10.0.16299. |
| u_charFromName | Introduced into icuuc.dll in 10.0.16299. |
| u_enumCharNames | Introduced into icuuc.dll in 10.0.16299. |
| u_getPropertyName | Introduced into icuuc.dll in 10.0.16299. |
| u_getPropertyEnum | Introduced into icuuc.dll in 10.0.16299. |
| u_getPropertyValueName | Introduced into icuuc.dll in 10.0.16299. |
| u_getPropertyValueEnum | Introduced into icuuc.dll in 10.0.16299. |
| u_isIDStart | Introduced into icuuc.dll in 10.0.16299. |
| u_isIDPart | Introduced into icuuc.dll in 10.0.16299. |
| u_isIDIgnorable | Introduced into icuuc.dll in 10.0.16299. |
| u_isJavaIDStart | Introduced into icuuc.dll in 10.0.16299. |
| u_isJavaIDPart | Introduced into icuuc.dll in 10.0.16299. |
| u_tolower | Introduced into icuuc.dll in 10.0.16299. |
| u_toupper | Introduced into icuuc.dll in 10.0.16299. |
| u_totitle | Introduced into icuuc.dll in 10.0.16299. |
| u_foldCase | Introduced into icuuc.dll in 10.0.16299. |
| u_digit | Introduced into icuuc.dll in 10.0.16299. |
| u_forDigit | Introduced into icuuc.dll in 10.0.16299. |
| u_charAge | Introduced into icuuc.dll in 10.0.16299. |
| u_getUnicodeVersion | Introduced into icuuc.dll in 10.0.16299. |
| u_getFC_NFKC_Closure | Introduced into icuuc.dll in 10.0.16299. |
| utext_close | Introduced into icuuc.dll in 10.0.16299. |
| utext_openUTF8 | Introduced into icuuc.dll in 10.0.16299. |
| utext_openUChars | Introduced into icuuc.dll in 10.0.16299. |
| utext_clone | Introduced into icuuc.dll in 10.0.16299. |
| utext_equals | Introduced into icuuc.dll in 10.0.16299. |
| utext_nativeLength | Introduced into icuuc.dll in 10.0.16299. |
| utext_isLengthExpensive | Introduced into icuuc.dll in 10.0.16299. |
| utext_char32At | Introduced into icuuc.dll in 10.0.16299. |
| utext_current32 | Introduced into icuuc.dll in 10.0.16299. |
| utext_next32 | Introduced into icuuc.dll in 10.0.16299. |
| utext_previous32 | Introduced into icuuc.dll in 10.0.16299. |
| utext_next32From | Introduced into icuuc.dll in 10.0.16299. |
| utext_previous32From | Introduced into icuuc.dll in 10.0.16299. |
| utext_getNativeIndex | Introduced into icuuc.dll in 10.0.16299. |
| utext_setNativeIndex | Introduced into icuuc.dll in 10.0.16299. |
| utext_moveIndex32 | Introduced into icuuc.dll in 10.0.16299. |
| utext_getPreviousNativeIndex | Introduced into icuuc.dll in 10.0.16299. |
| utext_extract | Introduced into icuuc.dll in 10.0.16299. |
| utext_isWritable | Introduced into icuuc.dll in 10.0.16299. |
| utext_hasMetaData | Introduced into icuuc.dll in 10.0.16299. |
| utext_replace | Introduced into icuuc.dll in 10.0.16299. |
| utext_copy | Introduced into icuuc.dll in 10.0.16299. |
| utext_freeze | Introduced into icuuc.dll in 10.0.16299. |
| utext_setup | Introduced into icuuc.dll in 10.0.16299. |
| uset_openEmpty | Introduced into icuuc.dll in 10.0.16299. |
| uset_open | Introduced into icuuc.dll in 10.0.16299. |
| uset_openPattern | Introduced into icuuc.dll in 10.0.16299. |
| uset_openPatternOptions | Introduced into icuuc.dll in 10.0.16299. |
| uset_close | Introduced into icuuc.dll in 10.0.16299. |
| uset_clone | Introduced into icuuc.dll in 10.0.16299. |
| uset_isFrozen | Introduced into icuuc.dll in 10.0.16299. |
| uset_freeze | Introduced into icuuc.dll in 10.0.16299. |
| uset_cloneAsThawed | Introduced into icuuc.dll in 10.0.16299. |
| uset_set | Introduced into icuuc.dll in 10.0.16299. |
| uset_applyPattern | Introduced into icuuc.dll in 10.0.16299. |
| uset_applyIntPropertyValue | Introduced into icuuc.dll in 10.0.16299. |
| uset_applyPropertyAlias | Introduced into icuuc.dll in 10.0.16299. |
| uset_resemblesPattern | Introduced into icuuc.dll in 10.0.16299. |
| uset_toPattern | Introduced into icuuc.dll in 10.0.16299. |
| uset_add | Introduced into icuuc.dll in 10.0.16299. |
| uset_addAll | Introduced into icuuc.dll in 10.0.16299. |
| uset_addRange | Introduced into icuuc.dll in 10.0.16299. |
| uset_addString | Introduced into icuuc.dll in 10.0.16299. |
| uset_addAllCodePoints | Introduced into icuuc.dll in 10.0.16299. |
| uset_remove | Introduced into icuuc.dll in 10.0.16299. |
| uset_removeRange | Introduced into icuuc.dll in 10.0.16299. |
| uset_removeString | Introduced into icuuc.dll in 10.0.16299. |
| uset_removeAll | Introduced into icuuc.dll in 10.0.16299. |
| uset_retain | Introduced into icuuc.dll in 10.0.16299. |
| uset_retainAll | Introduced into icuuc.dll in 10.0.16299. |
| uset_compact | Introduced into icuuc.dll in 10.0.16299. |
| uset_complement | Introduced into icuuc.dll in 10.0.16299. |
| uset_complementAll | Introduced into icuuc.dll in 10.0.16299. |
| uset_clear | Introduced into icuuc.dll in 10.0.16299. |
| uset_closeOver | Introduced into icuuc.dll in 10.0.16299. |
| uset_removeAllStrings | Introduced into icuuc.dll in 10.0.16299. |
| uset_isEmpty | Introduced into icuuc.dll in 10.0.16299. |
| uset_contains | Introduced into icuuc.dll in 10.0.16299. |
| uset_containsRange | Introduced into icuuc.dll in 10.0.16299. |
| uset_containsString | Introduced into icuuc.dll in 10.0.16299. |
| uset_indexOf | Introduced into icuuc.dll in 10.0.16299. |
| uset_charAt | Introduced into icuuc.dll in 10.0.16299. |
| uset_size | Introduced into icuuc.dll in 10.0.16299. |
| uset_getItemCount | Introduced into icuuc.dll in 10.0.16299. |
| uset_getItem | Introduced into icuuc.dll in 10.0.16299. |
| uset_containsAll | Introduced into icuuc.dll in 10.0.16299. |
| uset_containsAllCodePoints | Introduced into icuuc.dll in 10.0.16299. |
| uset_containsNone | Introduced into icuuc.dll in 10.0.16299. |
| uset_containsSome | Introduced into icuuc.dll in 10.0.16299. |
| uset_span | Introduced into icuuc.dll in 10.0.16299. |
| uset_spanBack | Introduced into icuuc.dll in 10.0.16299. |
| uset_spanUTF8 | Introduced into icuuc.dll in 10.0.16299. |
| uset_spanBackUTF8 | Introduced into icuuc.dll in 10.0.16299. |
| uset_equals | Introduced into icuuc.dll in 10.0.16299. |
| uset_serialize | Introduced into icuuc.dll in 10.0.16299. |
| uset_getSerializedSet | Introduced into icuuc.dll in 10.0.16299. |
| uset_setSerializedToOne | Introduced into icuuc.dll in 10.0.16299. |
| uset_serializedContains | Introduced into icuuc.dll in 10.0.16299. |
| uset_getSerializedRangeCount | Introduced into icuuc.dll in 10.0.16299. |
| uset_getSerializedRange | Introduced into icuuc.dll in 10.0.16299. |
| unorm2_getNFCInstance | Introduced into icuuc.dll in 10.0.16299. |
| unorm2_getNFDInstance | Introduced into icuuc.dll in 10.0.16299. |
| unorm2_getNFKCInstance | Introduced into icuuc.dll in 10.0.16299. |
| unorm2_getNFKDInstance | Introduced into icuuc.dll in 10.0.16299. |
| unorm2_getNFKCCasefoldInstance | Introduced into icuuc.dll in 10.0.16299. |
| unorm2_getInstance | Introduced into icuuc.dll in 10.0.16299. |
| unorm2_openFiltered | Introduced into icuuc.dll in 10.0.16299. |
| unorm2_close | Introduced into icuuc.dll in 10.0.16299. |
| unorm2_normalize | Introduced into icuuc.dll in 10.0.16299. |
| unorm2_normalizeSecondAndAppend | Introduced into icuuc.dll in 10.0.16299. |
| unorm2_append | Introduced into icuuc.dll in 10.0.16299. |
| unorm2_getDecomposition | Introduced into icuuc.dll in 10.0.16299. |
| unorm2_getRawDecomposition | Introduced into icuuc.dll in 10.0.16299. |
| unorm2_composePair | Introduced into icuuc.dll in 10.0.16299. |
| unorm2_getCombiningClass | Introduced into icuuc.dll in 10.0.16299. |
| unorm2_isNormalized | Introduced into icuuc.dll in 10.0.16299. |
| unorm2_quickCheck | Introduced into icuuc.dll in 10.0.16299. |
| unorm2_spanQuickCheckYes | Introduced into icuuc.dll in 10.0.16299. |
| unorm2_hasBoundaryBefore | Introduced into icuuc.dll in 10.0.16299. |
| unorm2_hasBoundaryAfter | Introduced into icuuc.dll in 10.0.16299. |
| unorm2_isInert | Introduced into icuuc.dll in 10.0.16299. |
| unorm_compare | Introduced into icuuc.dll in 10.0.16299. |
| ucnvsel_open | Introduced into icuuc.dll in 10.0.16299. |
| ucnvsel_close | Introduced into icuuc.dll in 10.0.16299. |
| ucnvsel_openFromSerialized | Introduced into icuuc.dll in 10.0.16299. |
| ucnvsel_serialize | Introduced into icuuc.dll in 10.0.16299. |
| ucnvsel_selectForString | Introduced into icuuc.dll in 10.0.16299. |
| ucnvsel_selectForUTF8 | Introduced into icuuc.dll in 10.0.16299. |
| u_catopen | Introduced into icuuc.dll in 10.0.16299. |
| u_catclose | Introduced into icuuc.dll in 10.0.16299. |
| u_catgets | Introduced into icuuc.dll in 10.0.16299. |
| ubidi_open | Introduced into icuuc.dll in 10.0.16299. |
| ubidi_openSized | Introduced into icuuc.dll in 10.0.16299. |
| ubidi_close | Introduced into icuuc.dll in 10.0.16299. |
| ubidi_setInverse | Introduced into icuuc.dll in 10.0.16299. |
| ubidi_isInverse | Introduced into icuuc.dll in 10.0.16299. |
| ubidi_orderParagraphsLTR | Introduced into icuuc.dll in 10.0.16299. |
| ubidi_isOrderParagraphsLTR | Introduced into icuuc.dll in 10.0.16299. |
| ubidi_setReorderingMode | Introduced into icuuc.dll in 10.0.16299. |
| ubidi_getReorderingMode | Introduced into icuuc.dll in 10.0.16299. |
| ubidi_setReorderingOptions | Introduced into icuuc.dll in 10.0.16299. |
| ubidi_getReorderingOptions | Introduced into icuuc.dll in 10.0.16299. |
| ubidi_setContext | Introduced into icuuc.dll in 10.0.16299. |
| ubidi_setPara | Introduced into icuuc.dll in 10.0.16299. |
| ubidi_setLine | Introduced into icuuc.dll in 10.0.16299. |
| ubidi_getDirection | Introduced into icuuc.dll in 10.0.16299. |
| ubidi_getBaseDirection | Introduced into icuuc.dll in 10.0.16299. |
| ubidi_getText | Introduced into icuuc.dll in 10.0.16299. |
| ubidi_getLength | Introduced into icuuc.dll in 10.0.16299. |
| ubidi_getParaLevel | Introduced into icuuc.dll in 10.0.16299. |
| ubidi_countParagraphs | Introduced into icuuc.dll in 10.0.16299. |
| ubidi_getParagraph | Introduced into icuuc.dll in 10.0.16299. |
| ubidi_getParagraphByIndex | Introduced into icuuc.dll in 10.0.16299. |
| ubidi_getLevelAt | Introduced into icuuc.dll in 10.0.16299. |
| ubidi_getLevels | Introduced into icuuc.dll in 10.0.16299. |
| ubidi_getLogicalRun | Introduced into icuuc.dll in 10.0.16299. |
| ubidi_countRuns | Introduced into icuuc.dll in 10.0.16299. |
| ubidi_getVisualRun | Introduced into icuuc.dll in 10.0.16299. |
| ubidi_getVisualIndex | Introduced into icuuc.dll in 10.0.16299. |
| ubidi_getLogicalIndex | Introduced into icuuc.dll in 10.0.16299. |
| ubidi_getLogicalMap | Introduced into icuuc.dll in 10.0.16299. |
| ubidi_getVisualMap | Introduced into icuuc.dll in 10.0.16299. |
| ubidi_reorderLogical | Introduced into icuuc.dll in 10.0.16299. |
| ubidi_reorderVisual | Introduced into icuuc.dll in 10.0.16299. |
| ubidi_invertMap | Introduced into icuuc.dll in 10.0.16299. |
| ubidi_getProcessedLength | Introduced into icuuc.dll in 10.0.16299. |
| ubidi_getResultLength | Introduced into icuuc.dll in 10.0.16299. |
| ubidi_getCustomizedClass | Introduced into icuuc.dll in 10.0.16299. |
| ubidi_setClassCallback | Introduced into icuuc.dll in 10.0.16299. |
| ubidi_getClassCallback | Introduced into icuuc.dll in 10.0.16299. |
| ubidi_writeReordered | Introduced into icuuc.dll in 10.0.16299. |
| ubidi_writeReverse | Introduced into icuuc.dll in 10.0.16299. |
| u_charsToUChars | Introduced into icuuc.dll in 10.0.16299. |
| u_UCharsToChars | Introduced into icuuc.dll in 10.0.16299. |
| u_strlen | Introduced into icuuc.dll in 10.0.16299. |
| u_countChar32 | Introduced into icuuc.dll in 10.0.16299. |
| u_strHasMoreChar32Than | Introduced into icuuc.dll in 10.0.16299. |
| u_strcat | Introduced into icuuc.dll in 10.0.16299. |
| u_strncat | Introduced into icuuc.dll in 10.0.16299. |
| u_strstr | Introduced into icuuc.dll in 10.0.16299. |
| u_strFindFirst | Introduced into icuuc.dll in 10.0.16299. |
| u_strchr | Introduced into icuuc.dll in 10.0.16299. |
| u_strchr32 | Introduced into icuuc.dll in 10.0.16299. |
| u_strrstr | Introduced into icuuc.dll in 10.0.16299. |
| u_strFindLast | Introduced into icuuc.dll in 10.0.16299. |
| u_strrchr | Introduced into icuuc.dll in 10.0.16299. |
| u_strrchr32 | Introduced into icuuc.dll in 10.0.16299. |
| u_strpbrk | Introduced into icuuc.dll in 10.0.16299. |
| u_strcspn | Introduced into icuuc.dll in 10.0.16299. |
| u_strspn | Introduced into icuuc.dll in 10.0.16299. |
| u_strtok_r | Introduced into icuuc.dll in 10.0.16299. |
| u_strcmp | Introduced into icuuc.dll in 10.0.16299. |
| u_strcmpCodePointOrder | Introduced into icuuc.dll in 10.0.16299. |
| u_strCompare | Introduced into icuuc.dll in 10.0.16299. |
| u_strCompareIter | Introduced into icuuc.dll in 10.0.16299. |
| u_strCaseCompare | Introduced into icuuc.dll in 10.0.16299. |
| u_strncmp | Introduced into icuuc.dll in 10.0.16299. |
| u_strncmpCodePointOrder | Introduced into icuuc.dll in 10.0.16299. |
| u_strcasecmp | Introduced into icuuc.dll in 10.0.16299. |
| u_strncasecmp | Introduced into icuuc.dll in 10.0.16299. |
| u_memcasecmp | Introduced into icuuc.dll in 10.0.16299. |
| u_strcpy | Introduced into icuuc.dll in 10.0.16299. |
| u_strncpy | Introduced into icuuc.dll in 10.0.16299. |
| u_uastrcpy | Introduced into icuuc.dll in 10.0.16299. |
| u_uastrncpy | Introduced into icuuc.dll in 10.0.16299. |
| u_austrcpy | Introduced into icuuc.dll in 10.0.16299. |
| u_austrncpy | Introduced into icuuc.dll in 10.0.16299. |
| u_memcpy | Introduced into icuuc.dll in 10.0.16299. |
| u_memmove | Introduced into icuuc.dll in 10.0.16299. |
| u_memset | Introduced into icuuc.dll in 10.0.16299. |
| u_memcmp | Introduced into icuuc.dll in 10.0.16299. |
| u_memcmpCodePointOrder | Introduced into icuuc.dll in 10.0.16299. |
| u_memchr | Introduced into icuuc.dll in 10.0.16299. |
| u_memchr32 | Introduced into icuuc.dll in 10.0.16299. |
| u_memrchr | Introduced into icuuc.dll in 10.0.16299. |
| u_memrchr32 | Introduced into icuuc.dll in 10.0.16299. |
| u_unescape | Introduced into icuuc.dll in 10.0.16299. |
| u_unescapeAt | Introduced into icuuc.dll in 10.0.16299. |
| u_strToUpper | Introduced into icuuc.dll in 10.0.16299. |
| u_strToLower | Introduced into icuuc.dll in 10.0.16299. |
| u_strToTitle | Introduced into icuuc.dll in 10.0.16299. |
| u_strFoldCase | Introduced into icuuc.dll in 10.0.16299. |
| u_strToWCS | Introduced into icuuc.dll in 10.0.16299. |
| u_strFromWCS | Introduced into icuuc.dll in 10.0.16299. |
| u_strToUTF8 | Introduced into icuuc.dll in 10.0.16299. |
| u_strFromUTF8 | Introduced into icuuc.dll in 10.0.16299. |
| u_strToUTF8WithSub | Introduced into icuuc.dll in 10.0.16299. |
| u_strFromUTF8WithSub | Introduced into icuuc.dll in 10.0.16299. |
| u_strFromUTF8Lenient | Introduced into icuuc.dll in 10.0.16299. |
| u_strToUTF32 | Introduced into icuuc.dll in 10.0.16299. |
| u_strFromUTF32 | Introduced into icuuc.dll in 10.0.16299. |
| u_strToUTF32WithSub | Introduced into icuuc.dll in 10.0.16299. |
| u_strFromUTF32WithSub | Introduced into icuuc.dll in 10.0.16299. |
| u_strToJavaModifiedUTF8 | Introduced into icuuc.dll in 10.0.16299. |
| u_strFromJavaModifiedUTF8WithSub | Introduced into icuuc.dll in 10.0.16299. |
| ucasemap_open | Introduced into icuuc.dll in 10.0.16299. |
| ucasemap_close | Introduced into icuuc.dll in 10.0.16299. |
| ucasemap_getLocale | Introduced into icuuc.dll in 10.0.16299. |
| ucasemap_getOptions | Introduced into icuuc.dll in 10.0.16299. |
| ucasemap_setLocale | Introduced into icuuc.dll in 10.0.16299. |
| ucasemap_setOptions | Introduced into icuuc.dll in 10.0.16299. |
| ucasemap_getBreakIterator | Introduced into icuuc.dll in 10.0.16299. |
| ucasemap_setBreakIterator | Introduced into icuuc.dll in 10.0.16299. |
| ucasemap_toTitle | Introduced into icuuc.dll in 10.0.16299. |
| ucasemap_utf8ToLower | Introduced into icuuc.dll in 10.0.16299. |
| ucasemap_utf8ToUpper | Introduced into icuuc.dll in 10.0.16299. |
| ucasemap_utf8ToTitle | Introduced into icuuc.dll in 10.0.16299. |
| ucasemap_utf8FoldCase | Introduced into icuuc.dll in 10.0.16299. |
| usprep_open | Introduced into icuuc.dll in 10.0.16299. |
| usprep_openByType | Introduced into icuuc.dll in 10.0.16299. |
| usprep_close | Introduced into icuuc.dll in 10.0.16299. |
| usprep_prepare | Introduced into icuuc.dll in 10.0.16299. |
| uidna_openUTS46 | Introduced into icuuc.dll in 10.0.16299. |
| uidna_close | Introduced into icuuc.dll in 10.0.16299. |
| uidna_labelToASCII | Introduced into icuuc.dll in 10.0.16299. |
| uidna_labelToUnicode | Introduced into icuuc.dll in 10.0.16299. |
| uidna_nameToASCII | Introduced into icuuc.dll in 10.0.16299. |
| uidna_nameToUnicode | Introduced into icuuc.dll in 10.0.16299. |
| uidna_labelToASCII_UTF8 | Introduced into icuuc.dll in 10.0.16299. |
| uidna_labelToUnicodeUTF8 | Introduced into icuuc.dll in 10.0.16299. |
| uidna_nameToASCII_UTF8 | Introduced into icuuc.dll in 10.0.16299. |
| uidna_nameToUnicodeUTF8 | Introduced into icuuc.dll in 10.0.16299. |
| ubrk_open | Introduced into icuuc.dll in 10.0.16299. |
| ubrk_openRules | Introduced into icuuc.dll in 10.0.16299. |
| ubrk_safeClone | Introduced into icuuc.dll in 10.0.16299. |
| ubrk_close | Introduced into icuuc.dll in 10.0.16299. |
| ubrk_setText | Introduced into icuuc.dll in 10.0.16299. |
| ubrk_setUText | Introduced into icuuc.dll in 10.0.16299. |
| ubrk_current | Introduced into icuuc.dll in 10.0.16299. |
| ubrk_next | Introduced into icuuc.dll in 10.0.16299. |
| ubrk_previous | Introduced into icuuc.dll in 10.0.16299. |
| ubrk_first | Introduced into icuuc.dll in 10.0.16299. |
| ubrk_last | Introduced into icuuc.dll in 10.0.16299. |
| ubrk_preceding | Introduced into icuuc.dll in 10.0.16299. |
| ubrk_following | Introduced into icuuc.dll in 10.0.16299. |
| ubrk_getAvailable | Introduced into icuuc.dll in 10.0.16299. |
| ubrk_countAvailable | Introduced into icuuc.dll in 10.0.16299. |
| ubrk_isBoundary | Introduced into icuuc.dll in 10.0.16299. |
| ubrk_getRuleStatus | Introduced into icuuc.dll in 10.0.16299. |
| ubrk_getRuleStatusVec | Introduced into icuuc.dll in 10.0.16299. |
| ubrk_getLocaleByType | Introduced into icuuc.dll in 10.0.16299. |
| ubrk_refreshUText | Introduced into icuuc.dll in 10.0.16299. |
| u_getDataVersion | Introduced into icuuc.dll in 10.0.16299. |
| ubiditransform_close | Introduced into icuuc.dll in 10.0.17763. |
| ubiditransform_open | Introduced into icuuc.dll in 10.0.17763. |
| ubiditransform_transform | Introduced into icuuc.dll in 10.0.17763. |
| ubrk_openBinaryRules | Introduced into icuuc.dll in 10.0.17763. |
| ubrk_getBinaryRules | Introduced into icuuc.dll in 10.0.17763. |


## APIs from icuin.dll

| API | Requirements |
| -----| --------------|
| ucal_openTimeZoneIDEnumeration | Introduced into icuin.dll in 10.0.16299. |
| ucal_openTimeZones | Introduced into icuin.dll in 10.0.16299. |
| ucal_openCountryTimeZones | Introduced into icuin.dll in 10.0.16299. |
| ucal_getDefaultTimeZone | Introduced into icuin.dll in 10.0.16299. |
| ucal_setDefaultTimeZone | Introduced into icuin.dll in 10.0.16299. |
| ucal_getDSTSavings | Introduced into icuin.dll in 10.0.16299. |
| ucal_getNow | Introduced into icuin.dll in 10.0.16299. |
| ucal_open | Introduced into icuin.dll in 10.0.16299. |
| ucal_close | Introduced into icuin.dll in 10.0.16299. |
| ucal_clone | Introduced into icuin.dll in 10.0.16299. |
| ucal_setTimeZone | Introduced into icuin.dll in 10.0.16299. |
| ucal_getTimeZoneID | Introduced into icuin.dll in 10.0.16299. |
| ucal_getTimeZoneDisplayName | Introduced into icuin.dll in 10.0.16299. |
| ucal_inDaylightTime | Introduced into icuin.dll in 10.0.16299. |
| ucal_setGregorianChange | Introduced into icuin.dll in 10.0.16299. |
| ucal_getGregorianChange | Introduced into icuin.dll in 10.0.16299. |
| ucal_getAttribute | Introduced into icuin.dll in 10.0.16299. |
| ucal_setAttribute | Introduced into icuin.dll in 10.0.16299. |
| ucal_getAvailable | Introduced into icuin.dll in 10.0.16299. |
| ucal_countAvailable | Introduced into icuin.dll in 10.0.16299. |
| ucal_getMillis | Introduced into icuin.dll in 10.0.16299. |
| ucal_setMillis | Introduced into icuin.dll in 10.0.16299. |
| ucal_setDate | Introduced into icuin.dll in 10.0.16299. |
| ucal_setDateTime | Introduced into icuin.dll in 10.0.16299. |
| ucal_equivalentTo | Introduced into icuin.dll in 10.0.16299. |
| ucal_add | Introduced into icuin.dll in 10.0.16299. |
| ucal_roll | Introduced into icuin.dll in 10.0.16299. |
| ucal_get | Introduced into icuin.dll in 10.0.16299. |
| ucal_set | Introduced into icuin.dll in 10.0.16299. |
| ucal_isSet | Introduced into icuin.dll in 10.0.16299. |
| ucal_clearField | Introduced into icuin.dll in 10.0.16299. |
| ucal_clear | Introduced into icuin.dll in 10.0.16299. |
| ucal_getLimit | Introduced into icuin.dll in 10.0.16299. |
| ucal_getLocaleByType | Introduced into icuin.dll in 10.0.16299. |
| ucal_getTZDataVersion | Introduced into icuin.dll in 10.0.16299. |
| ucal_getCanonicalTimeZoneID | Introduced into icuin.dll in 10.0.16299. |
| ucal_getType | Introduced into icuin.dll in 10.0.16299. |
| ucal_getKeywordValuesForLocale | Introduced into icuin.dll in 10.0.16299. |
| ucal_getDayOfWeekType | Introduced into icuin.dll in 10.0.16299. |
| ucal_getWeekendTransition | Introduced into icuin.dll in 10.0.16299. |
| ucal_isWeekend | Introduced into icuin.dll in 10.0.16299. |
| ucal_getFieldDifference | Introduced into icuin.dll in 10.0.16299. |
| ucal_getTimeZoneTransitionDate | Introduced into icuin.dll in 10.0.16299. |
| ucal_getWindowsTimeZoneID | Introduced into icuin.dll in 10.0.16299. |
| ucal_getTimeZoneIDForWindowsID | Introduced into icuin.dll in 10.0.16299. |
| ucol_open | Introduced into icuin.dll in 10.0.16299. |
| ucol_openRules | Introduced into icuin.dll in 10.0.16299. |
| ucol_getContractionsAndExpansions | Introduced into icuin.dll in 10.0.16299. |
| ucol_close | Introduced into icuin.dll in 10.0.16299. |
| ucol_strcoll | Introduced into icuin.dll in 10.0.16299. |
| ucol_strcollUTF8 | Introduced into icuin.dll in 10.0.16299. |
| ucol_greater | Introduced into icuin.dll in 10.0.16299. |
| ucol_greaterOrEqual | Introduced into icuin.dll in 10.0.16299. |
| ucol_equal | Introduced into icuin.dll in 10.0.16299. |
| ucol_strcollIter | Introduced into icuin.dll in 10.0.16299. |
| ucol_getStrength | Introduced into icuin.dll in 10.0.16299. |
| ucol_setStrength | Introduced into icuin.dll in 10.0.16299. |
| ucol_getReorderCodes | Introduced into icuin.dll in 10.0.16299. |
| ucol_setReorderCodes | Introduced into icuin.dll in 10.0.16299. |
| ucol_getEquivalentReorderCodes | Introduced into icuin.dll in 10.0.16299. |
| ucol_getDisplayName | Introduced into icuin.dll in 10.0.16299. |
| ucol_getAvailable | Introduced into icuin.dll in 10.0.16299. |
| ucol_countAvailable | Introduced into icuin.dll in 10.0.16299. |
| ucol_openAvailableLocales | Introduced into icuin.dll in 10.0.16299. |
| ucol_getKeywords | Introduced into icuin.dll in 10.0.16299. |
| ucol_getKeywordValues | Introduced into icuin.dll in 10.0.16299. |
| ucol_getKeywordValuesForLocale | Introduced into icuin.dll in 10.0.16299. |
| ucol_getFunctionalEquivalent | Introduced into icuin.dll in 10.0.16299. |
| ucol_getRules | Introduced into icuin.dll in 10.0.16299. |
| ucol_getSortKey | Introduced into icuin.dll in 10.0.16299. |
| ucol_nextSortKeyPart | Introduced into icuin.dll in 10.0.16299. |
| ucol_getBound | Introduced into icuin.dll in 10.0.16299. |
| ucol_getVersion | Introduced into icuin.dll in 10.0.16299. |
| ucol_getUCAVersion | Introduced into icuin.dll in 10.0.16299. |
| ucol_mergeSortkeys | Introduced into icuin.dll in 10.0.16299. |
| ucol_setAttribute | Introduced into icuin.dll in 10.0.16299. |
| ucol_getAttribute | Introduced into icuin.dll in 10.0.16299. |
| ucol_setMaxVariable | Introduced into icuin.dll in 10.0.16299. |
| ucol_getMaxVariable | Introduced into icuin.dll in 10.0.16299. |
| ucol_getVariableTop | Introduced into icuin.dll in 10.0.16299. |
| ucol_safeClone | Introduced into icuin.dll in 10.0.16299. |
| ucol_getRulesEx | Introduced into icuin.dll in 10.0.16299. |
| ucol_getLocaleByType | Introduced into icuin.dll in 10.0.16299. |
| ucol_getTailoredSet | Introduced into icuin.dll in 10.0.16299. |
| ucol_cloneBinary | Introduced into icuin.dll in 10.0.16299. |
| ucol_openBinary | Introduced into icuin.dll in 10.0.16299. |
| ucol_openElements | Introduced into icuin.dll in 10.0.16299. |
| ucol_keyHashCode | Introduced into icuin.dll in 10.0.16299. |
| ucol_closeElements | Introduced into icuin.dll in 10.0.16299. |
| ucol_reset | Introduced into icuin.dll in 10.0.16299. |
| ucol_next | Introduced into icuin.dll in 10.0.16299. |
| ucol_previous | Introduced into icuin.dll in 10.0.16299. |
| ucol_getMaxExpansion | Introduced into icuin.dll in 10.0.16299. |
| ucol_setText | Introduced into icuin.dll in 10.0.16299. |
| ucol_getOffset | Introduced into icuin.dll in 10.0.16299. |
| ucol_setOffset | Introduced into icuin.dll in 10.0.16299. |
| ucol_primaryOrder | Introduced into icuin.dll in 10.0.16299. |
| ucol_secondaryOrder | Introduced into icuin.dll in 10.0.16299. |
| ucol_tertiaryOrder | Introduced into icuin.dll in 10.0.16299. |
| ucsdet_open | Introduced into icuin.dll in 10.0.16299. |
| ucsdet_close | Introduced into icuin.dll in 10.0.16299. |
| ucsdet_setText | Introduced into icuin.dll in 10.0.16299. |
| ucsdet_setDeclaredEncoding | Introduced into icuin.dll in 10.0.16299. |
| ucsdet_detect | Introduced into icuin.dll in 10.0.16299. |
| ucsdet_detectAll | Introduced into icuin.dll in 10.0.16299. |
| ucsdet_getName | Introduced into icuin.dll in 10.0.16299. |
| ucsdet_getConfidence | Introduced into icuin.dll in 10.0.16299. |
| ucsdet_getLanguage | Introduced into icuin.dll in 10.0.16299. |
| ucsdet_getUChars | Introduced into icuin.dll in 10.0.16299. |
| ucsdet_getAllDetectableCharsets | Introduced into icuin.dll in 10.0.16299. |
| ucsdet_isInputFilterEnabled | Introduced into icuin.dll in 10.0.16299. |
| ucsdet_enableInputFilter | Introduced into icuin.dll in 10.0.16299. |
| udtitvfmt_open | Introduced into icuin.dll in 10.0.16299. |
| udtitvfmt_close | Introduced into icuin.dll in 10.0.16299. |
| udtitvfmt_format | Introduced into icuin.dll in 10.0.16299. |
| udatpg_open | Introduced into icuin.dll in 10.0.16299. |
| udatpg_openEmpty | Introduced into icuin.dll in 10.0.16299. |
| udatpg_close | Introduced into icuin.dll in 10.0.16299. |
| udatpg_clone | Introduced into icuin.dll in 10.0.16299. |
| udatpg_getBestPattern | Introduced into icuin.dll in 10.0.16299. |
| udatpg_getBestPatternWithOptions | Introduced into icuin.dll in 10.0.16299. |
| udatpg_getSkeleton | Introduced into icuin.dll in 10.0.16299. |
| udatpg_getBaseSkeleton | Introduced into icuin.dll in 10.0.16299. |
| udatpg_addPattern | Introduced into icuin.dll in 10.0.16299. |
| udatpg_setAppendItemFormat | Introduced into icuin.dll in 10.0.16299. |
| udatpg_getAppendItemFormat | Introduced into icuin.dll in 10.0.16299. |
| udatpg_setAppendItemName | Introduced into icuin.dll in 10.0.16299. |
| udatpg_getAppendItemName | Introduced into icuin.dll in 10.0.16299. |
| udatpg_setDateTimeFormat | Introduced into icuin.dll in 10.0.16299. |
| udatpg_getDateTimeFormat | Introduced into icuin.dll in 10.0.16299. |
| udatpg_setDecimal | Introduced into icuin.dll in 10.0.16299. |
| udatpg_getDecimal | Introduced into icuin.dll in 10.0.16299. |
| udatpg_replaceFieldTypes | Introduced into icuin.dll in 10.0.16299. |
| udatpg_replaceFieldTypesWithOptions | Introduced into icuin.dll in 10.0.16299. |
| udatpg_openSkeletons | Introduced into icuin.dll in 10.0.16299. |
| udatpg_openBaseSkeletons | Introduced into icuin.dll in 10.0.16299. |
| udatpg_getPatternForSkeleton | Introduced into icuin.dll in 10.0.16299. |
| ufieldpositer_open | Introduced into icuin.dll in 10.0.16299. |
| ufieldpositer_close | Introduced into icuin.dll in 10.0.16299. |
| ufieldpositer_next | Introduced into icuin.dll in 10.0.16299. |
| ufmt_open | Introduced into icuin.dll in 10.0.16299. |
| ufmt_close | Introduced into icuin.dll in 10.0.16299. |
| ufmt_getType | Introduced into icuin.dll in 10.0.16299. |
| ufmt_isNumeric | Introduced into icuin.dll in 10.0.16299. |
| ufmt_getDate | Introduced into icuin.dll in 10.0.16299. |
| ufmt_getDouble | Introduced into icuin.dll in 10.0.16299. |
| ufmt_getLong | Introduced into icuin.dll in 10.0.16299. |
| ufmt_getInt64 | Introduced into icuin.dll in 10.0.16299. |
| ufmt_getObject | Introduced into icuin.dll in 10.0.16299. |
| ufmt_getUChars | Introduced into icuin.dll in 10.0.16299. |
| ufmt_getArrayLength | Introduced into icuin.dll in 10.0.16299. |
| ufmt_getArrayItemByIndex | Introduced into icuin.dll in 10.0.16299. |
| ufmt_getDecNumChars | Introduced into icuin.dll in 10.0.16299. |
| ugender_getInstance | Introduced into icuin.dll in 10.0.16299. |
| ugender_getListGender | Introduced into icuin.dll in 10.0.16299. |
| ulocdata_open | Introduced into icuin.dll in 10.0.16299. |
| ulocdata_close | Introduced into icuin.dll in 10.0.16299. |
| ulocdata_setNoSubstitute | Introduced into icuin.dll in 10.0.16299. |
| ulocdata_getNoSubstitute | Introduced into icuin.dll in 10.0.16299. |
| ulocdata_getExemplarSet | Introduced into icuin.dll in 10.0.16299. |
| ulocdata_getDelimiter | Introduced into icuin.dll in 10.0.16299. |
| ulocdata_getMeasurementSystem | Introduced into icuin.dll in 10.0.16299. |
| ulocdata_getPaperSize | Introduced into icuin.dll in 10.0.16299. |
| ulocdata_getCLDRVersion | Introduced into icuin.dll in 10.0.16299. |
| ulocdata_getLocaleDisplayPattern | Introduced into icuin.dll in 10.0.16299. |
| ulocdata_getLocaleSeparator | Introduced into icuin.dll in 10.0.16299. |
| u_formatMessage | Introduced into icuin.dll in 10.0.16299. |
| u_vformatMessage | Introduced into icuin.dll in 10.0.16299. |
| u_parseMessage | Introduced into icuin.dll in 10.0.16299. |
| u_vparseMessage | Introduced into icuin.dll in 10.0.16299. |
| u_formatMessageWithError | Introduced into icuin.dll in 10.0.16299. |
| u_vformatMessageWithError | Introduced into icuin.dll in 10.0.16299. |
| u_parseMessageWithError | Introduced into icuin.dll in 10.0.16299. |
| u_vparseMessageWithError | Introduced into icuin.dll in 10.0.16299. |
| umsg_open | Introduced into icuin.dll in 10.0.16299. |
| umsg_close | Introduced into icuin.dll in 10.0.16299. |
| umsg_clone | Introduced into icuin.dll in 10.0.16299. |
| umsg_setLocale | Introduced into icuin.dll in 10.0.16299. |
| umsg_getLocale | Introduced into icuin.dll in 10.0.16299. |
| umsg_applyPattern | Introduced into icuin.dll in 10.0.16299. |
| umsg_toPattern | Introduced into icuin.dll in 10.0.16299. |
| umsg_format | Introduced into icuin.dll in 10.0.16299. |
| umsg_vformat | Introduced into icuin.dll in 10.0.16299. |
| umsg_parse | Introduced into icuin.dll in 10.0.16299. |
| umsg_vparse | Introduced into icuin.dll in 10.0.16299. |
| umsg_autoQuoteApostrophe | Introduced into icuin.dll in 10.0.16299. |
| unum_open | Introduced into icuin.dll in 10.0.16299. |
| unum_close | Introduced into icuin.dll in 10.0.16299. |
| unum_clone | Introduced into icuin.dll in 10.0.16299. |
| unum_format | Introduced into icuin.dll in 10.0.16299. |
| unum_formatInt64 | Introduced into icuin.dll in 10.0.16299. |
| unum_formatDouble | Introduced into icuin.dll in 10.0.16299. |
| unum_formatDecimal | Introduced into icuin.dll in 10.0.16299. |
| unum_formatDoubleCurrency | Introduced into icuin.dll in 10.0.16299. |
| unum_formatUFormattable | Introduced into icuin.dll in 10.0.16299. |
| unum_parse | Introduced into icuin.dll in 10.0.16299. |
| unum_parseInt64 | Introduced into icuin.dll in 10.0.16299. |
| unum_parseDouble | Introduced into icuin.dll in 10.0.16299. |
| unum_parseDecimal | Introduced into icuin.dll in 10.0.16299. |
| unum_parseDoubleCurrency | Introduced into icuin.dll in 10.0.16299. |
| unum_parseToUFormattable | Introduced into icuin.dll in 10.0.16299. |
| unum_applyPattern | Introduced into icuin.dll in 10.0.16299. |
| unum_getAvailable | Introduced into icuin.dll in 10.0.16299. |
| unum_countAvailable | Introduced into icuin.dll in 10.0.16299. |
| unum_getAttribute | Introduced into icuin.dll in 10.0.16299. |
| unum_setAttribute | Introduced into icuin.dll in 10.0.16299. |
| unum_getDoubleAttribute | Introduced into icuin.dll in 10.0.16299. |
| unum_setDoubleAttribute | Introduced into icuin.dll in 10.0.16299. |
| unum_getTextAttribute | Introduced into icuin.dll in 10.0.16299. |
| unum_setTextAttribute | Introduced into icuin.dll in 10.0.16299. |
| unum_toPattern | Introduced into icuin.dll in 10.0.16299. |
| unum_getSymbol | Introduced into icuin.dll in 10.0.16299. |
| unum_setSymbol | Introduced into icuin.dll in 10.0.16299. |
| unum_getLocaleByType | Introduced into icuin.dll in 10.0.16299. |
| unum_setContext | Introduced into icuin.dll in 10.0.16299. |
| unum_getContext | Introduced into icuin.dll in 10.0.16299. |
| udat_toCalendarDateField | Introduced into icuin.dll in 10.0.16299. |
| udat_open | Introduced into icuin.dll in 10.0.16299. |
| udat_close | Introduced into icuin.dll in 10.0.16299. |
| udat_getBooleanAttribute | Introduced into icuin.dll in 10.0.16299. |
| udat_setBooleanAttribute | Introduced into icuin.dll in 10.0.16299. |
| udat_clone | Introduced into icuin.dll in 10.0.16299. |
| udat_format | Introduced into icuin.dll in 10.0.16299. |
| udat_formatCalendar | Introduced into icuin.dll in 10.0.16299. |
| udat_formatForFields | Introduced into icuin.dll in 10.0.16299. |
| udat_formatCalendarForFields | Introduced into icuin.dll in 10.0.16299. |
| udat_parse | Introduced into icuin.dll in 10.0.16299. |
| udat_parseCalendar | Introduced into icuin.dll in 10.0.16299. |
| udat_isLenient | Introduced into icuin.dll in 10.0.16299. |
| udat_setLenient | Introduced into icuin.dll in 10.0.16299. |
| udat_getCalendar | Introduced into icuin.dll in 10.0.16299. |
| udat_setCalendar | Introduced into icuin.dll in 10.0.16299. |
| udat_getNumberFormat | Introduced into icuin.dll in 10.0.16299. |
| udat_getNumberFormatForField | Introduced into icuin.dll in 10.0.16299. |
| udat_adoptNumberFormatForFields | Introduced into icuin.dll in 10.0.16299. |
| udat_setNumberFormat | Introduced into icuin.dll in 10.0.16299. |
| udat_adoptNumberFormat | Introduced into icuin.dll in 10.0.16299. |
| udat_getAvailable | Introduced into icuin.dll in 10.0.16299. |
| udat_countAvailable | Introduced into icuin.dll in 10.0.16299. |
| udat_get2DigitYearStart | Introduced into icuin.dll in 10.0.16299. |
| udat_set2DigitYearStart | Introduced into icuin.dll in 10.0.16299. |
| udat_toPattern | Introduced into icuin.dll in 10.0.16299. |
| udat_applyPattern | Introduced into icuin.dll in 10.0.16299. |
| udat_getSymbols | Introduced into icuin.dll in 10.0.16299. |
| udat_countSymbols | Introduced into icuin.dll in 10.0.16299. |
| udat_setSymbols | Introduced into icuin.dll in 10.0.16299. |
| udat_getLocaleByType | Introduced into icuin.dll in 10.0.16299. |
| udat_setContext | Introduced into icuin.dll in 10.0.16299. |
| udat_getContext | Introduced into icuin.dll in 10.0.16299. |
| unumsys_open | Introduced into icuin.dll in 10.0.16299. |
| unumsys_openByName | Introduced into icuin.dll in 10.0.16299. |
| unumsys_close | Introduced into icuin.dll in 10.0.16299. |
| unumsys_openAvailableNames | Introduced into icuin.dll in 10.0.16299. |
| unumsys_getName | Introduced into icuin.dll in 10.0.16299. |
| unumsys_isAlgorithmic | Introduced into icuin.dll in 10.0.16299. |
| unumsys_getRadix | Introduced into icuin.dll in 10.0.16299. |
| unumsys_getDescription | Introduced into icuin.dll in 10.0.16299. |
| uplrules_open | Introduced into icuin.dll in 10.0.16299. |
| uplrules_openForType | Introduced into icuin.dll in 10.0.16299. |
| uplrules_close | Introduced into icuin.dll in 10.0.16299. |
| uplrules_select | Introduced into icuin.dll in 10.0.16299. |
| ureldatefmt_open | Introduced into icuin.dll in 10.0.16299. |
| ureldatefmt_close | Introduced into icuin.dll in 10.0.16299. |
| ureldatefmt_formatNumeric | Introduced into icuin.dll in 10.0.16299. |
| ureldatefmt_format | Introduced into icuin.dll in 10.0.16299. |
| ureldatefmt_combineDateAndTime | Introduced into icuin.dll in 10.0.16299. |
| uregex_open | Introduced into icuin.dll in 10.0.16299. |
| uregex_openUText | Introduced into icuin.dll in 10.0.16299. |
| uregex_openC | Introduced into icuin.dll in 10.0.16299. |
| uregex_close | Introduced into icuin.dll in 10.0.16299. |
| uregex_clone | Introduced into icuin.dll in 10.0.16299. |
| uregex_pattern | Introduced into icuin.dll in 10.0.16299. |
| uregex_patternUText | Introduced into icuin.dll in 10.0.16299. |
| uregex_flags | Introduced into icuin.dll in 10.0.16299. |
| uregex_setText | Introduced into icuin.dll in 10.0.16299. |
| uregex_setUText | Introduced into icuin.dll in 10.0.16299. |
| uregex_getText | Introduced into icuin.dll in 10.0.16299. |
| uregex_getUText | Introduced into icuin.dll in 10.0.16299. |
| uregex_refreshUText | Introduced into icuin.dll in 10.0.16299. |
| uregex_matches | Introduced into icuin.dll in 10.0.16299. |
| uregex_matches64 | Introduced into icuin.dll in 10.0.16299. |
| uregex_lookingAt | Introduced into icuin.dll in 10.0.16299. |
| uregex_lookingAt64 | Introduced into icuin.dll in 10.0.16299. |
| uregex_find | Introduced into icuin.dll in 10.0.16299. |
| uregex_find64 | Introduced into icuin.dll in 10.0.16299. |
| uregex_findNext | Introduced into icuin.dll in 10.0.16299. |
| uregex_groupCount | Introduced into icuin.dll in 10.0.16299. |
| uregex_groupNumberFromName | Introduced into icuin.dll in 10.0.16299. |
| uregex_groupNumberFromCName | Introduced into icuin.dll in 10.0.16299. |
| uregex_group | Introduced into icuin.dll in 10.0.16299. |
| uregex_groupUText | Introduced into icuin.dll in 10.0.16299. |
| uregex_start | Introduced into icuin.dll in 10.0.16299. |
| uregex_start64 | Introduced into icuin.dll in 10.0.16299. |
| uregex_end | Introduced into icuin.dll in 10.0.16299. |
| uregex_end64 | Introduced into icuin.dll in 10.0.16299. |
| uregex_reset | Introduced into icuin.dll in 10.0.16299. |
| uregex_reset64 | Introduced into icuin.dll in 10.0.16299. |
| uregex_setRegion | Introduced into icuin.dll in 10.0.16299. |
| uregex_setRegion64 | Introduced into icuin.dll in 10.0.16299. |
| uregex_setRegionAndStart | Introduced into icuin.dll in 10.0.16299. |
| uregex_regionStart | Introduced into icuin.dll in 10.0.16299. |
| uregex_regionStart64 | Introduced into icuin.dll in 10.0.16299. |
| uregex_regionEnd | Introduced into icuin.dll in 10.0.16299. |
| uregex_regionEnd64 | Introduced into icuin.dll in 10.0.16299. |
| uregex_hasTransparentBounds | Introduced into icuin.dll in 10.0.16299. |
| uregex_useTransparentBounds | Introduced into icuin.dll in 10.0.16299. |
| uregex_hasAnchoringBounds | Introduced into icuin.dll in 10.0.16299. |
| uregex_useAnchoringBounds | Introduced into icuin.dll in 10.0.16299. |
| uregex_hitEnd | Introduced into icuin.dll in 10.0.16299. |
| uregex_requireEnd | Introduced into icuin.dll in 10.0.16299. |
| uregex_replaceAll | Introduced into icuin.dll in 10.0.16299. |
| uregex_replaceAllUText | Introduced into icuin.dll in 10.0.16299. |
| uregex_replaceFirst | Introduced into icuin.dll in 10.0.16299. |
| uregex_replaceFirstUText | Introduced into icuin.dll in 10.0.16299. |
| uregex_appendReplacement | Introduced into icuin.dll in 10.0.16299. |
| uregex_appendReplacementUText | Introduced into icuin.dll in 10.0.16299. |
| uregex_appendTail | Introduced into icuin.dll in 10.0.16299. |
| uregex_appendTailUText | Introduced into icuin.dll in 10.0.16299. |
| uregex_split | Introduced into icuin.dll in 10.0.16299. |
| uregex_splitUText | Introduced into icuin.dll in 10.0.16299. |
| uregex_setTimeLimit | Introduced into icuin.dll in 10.0.16299. |
| uregex_getTimeLimit | Introduced into icuin.dll in 10.0.16299. |
| uregex_setStackLimit | Introduced into icuin.dll in 10.0.16299. |
| uregex_getStackLimit | Introduced into icuin.dll in 10.0.16299. |
| uregex_setMatchCallback | Introduced into icuin.dll in 10.0.16299. |
| uregex_getMatchCallback | Introduced into icuin.dll in 10.0.16299. |
| uregex_setFindProgressCallback | Introduced into icuin.dll in 10.0.16299. |
| uregex_getFindProgressCallback | Introduced into icuin.dll in 10.0.16299. |
| uregion_getRegionFromCode | Introduced into icuin.dll in 10.0.16299. |
| uregion_getRegionFromNumericCode | Introduced into icuin.dll in 10.0.16299. |
| uregion_getAvailable | Introduced into icuin.dll in 10.0.16299. |
| uregion_areEqual | Introduced into icuin.dll in 10.0.16299. |
| uregion_getContainingRegion | Introduced into icuin.dll in 10.0.16299. |
| uregion_getContainingRegionOfType | Introduced into icuin.dll in 10.0.16299. |
| uregion_getContainedRegions | Introduced into icuin.dll in 10.0.16299. |
| uregion_getContainedRegionsOfType | Introduced into icuin.dll in 10.0.16299. |
| uregion_contains | Introduced into icuin.dll in 10.0.16299. |
| uregion_getPreferredValues | Introduced into icuin.dll in 10.0.16299. |
| uregion_getRegionCode | Introduced into icuin.dll in 10.0.16299. |
| uregion_getNumericCode | Introduced into icuin.dll in 10.0.16299. |
| uregion_getType | Introduced into icuin.dll in 10.0.16299. |
| usearch_open | Introduced into icuin.dll in 10.0.16299. |
| usearch_openFromCollator | Introduced into icuin.dll in 10.0.16299. |
| usearch_close | Introduced into icuin.dll in 10.0.16299. |
| usearch_setOffset | Introduced into icuin.dll in 10.0.16299. |
| usearch_getOffset | Introduced into icuin.dll in 10.0.16299. |
| usearch_setAttribute | Introduced into icuin.dll in 10.0.16299. |
| usearch_getAttribute | Introduced into icuin.dll in 10.0.16299. |
| usearch_getMatchedStart | Introduced into icuin.dll in 10.0.16299. |
| usearch_getMatchedLength | Introduced into icuin.dll in 10.0.16299. |
| usearch_getMatchedText | Introduced into icuin.dll in 10.0.16299. |
| usearch_setBreakIterator | Introduced into icuin.dll in 10.0.16299. |
| usearch_getBreakIterator | Introduced into icuin.dll in 10.0.16299. |
| usearch_setText | Introduced into icuin.dll in 10.0.16299. |
| usearch_getText | Introduced into icuin.dll in 10.0.16299. |
| usearch_getCollator | Introduced into icuin.dll in 10.0.16299. |
| usearch_setCollator | Introduced into icuin.dll in 10.0.16299. |
| usearch_setPattern | Introduced into icuin.dll in 10.0.16299. |
| usearch_getPattern | Introduced into icuin.dll in 10.0.16299. |
| usearch_first | Introduced into icuin.dll in 10.0.16299. |
| usearch_following | Introduced into icuin.dll in 10.0.16299. |
| usearch_last | Introduced into icuin.dll in 10.0.16299. |
| usearch_preceding | Introduced into icuin.dll in 10.0.16299. |
| usearch_next | Introduced into icuin.dll in 10.0.16299. |
| usearch_previous | Introduced into icuin.dll in 10.0.16299. |
| usearch_reset | Introduced into icuin.dll in 10.0.16299. |
| uspoof_open | Introduced into icuin.dll in 10.0.16299. |
| uspoof_openFromSerialized | Introduced into icuin.dll in 10.0.16299. |
| uspoof_openFromSource | Introduced into icuin.dll in 10.0.16299. |
| uspoof_close | Introduced into icuin.dll in 10.0.16299. |
| uspoof_clone | Introduced into icuin.dll in 10.0.16299. |
| uspoof_setChecks | Introduced into icuin.dll in 10.0.16299. |
| uspoof_getChecks | Introduced into icuin.dll in 10.0.16299. |
| uspoof_setRestrictionLevel | Introduced into icuin.dll in 10.0.16299. |
| uspoof_getRestrictionLevel | Introduced into icuin.dll in 10.0.16299. |
| uspoof_setAllowedLocales | Introduced into icuin.dll in 10.0.16299. |
| uspoof_getAllowedLocales | Introduced into icuin.dll in 10.0.16299. |
| uspoof_setAllowedChars | Introduced into icuin.dll in 10.0.16299. |
| uspoof_getAllowedChars | Introduced into icuin.dll in 10.0.16299. |
| uspoof_check | Introduced into icuin.dll in 10.0.16299. |
| uspoof_checkUTF8 | Introduced into icuin.dll in 10.0.16299. |
| uspoof_areConfusable | Introduced into icuin.dll in 10.0.16299. |
| uspoof_areConfusableUTF8 | Introduced into icuin.dll in 10.0.16299. |
| uspoof_getSkeleton | Introduced into icuin.dll in 10.0.16299. |
| uspoof_getSkeletonUTF8 | Introduced into icuin.dll in 10.0.16299. |
| uspoof_getInclusionSet | Introduced into icuin.dll in 10.0.16299. |
| uspoof_getRecommendedSet | Introduced into icuin.dll in 10.0.16299. |
| uspoof_serialize | Introduced into icuin.dll in 10.0.16299. |
| utmscale_getTimeScaleValue | Introduced into icuin.dll in 10.0.16299. |
| utmscale_fromInt64 | Introduced into icuin.dll in 10.0.16299. |
| utmscale_toInt64 | Introduced into icuin.dll in 10.0.16299. |
| utrans_openU | Introduced into icuin.dll in 10.0.16299. |
| utrans_openInverse | Introduced into icuin.dll in 10.0.16299. |
| utrans_clone | Introduced into icuin.dll in 10.0.16299. |
| utrans_close | Introduced into icuin.dll in 10.0.16299. |
| utrans_getUnicodeID | Introduced into icuin.dll in 10.0.16299. |
| utrans_register | Introduced into icuin.dll in 10.0.16299. |
| utrans_unregisterID | Introduced into icuin.dll in 10.0.16299. |
| utrans_setFilter | Introduced into icuin.dll in 10.0.16299. |
| utrans_countAvailableIDs | Introduced into icuin.dll in 10.0.16299. |
| utrans_openIDs | Introduced into icuin.dll in 10.0.16299. |
| utrans_trans | Introduced into icuin.dll in 10.0.16299. |
| utrans_transIncremental | Introduced into icuin.dll in 10.0.16299. |
| utrans_transUChars | Introduced into icuin.dll in 10.0.16299. |
| utrans_transIncrementalUChars | Introduced into icuin.dll in 10.0.16299. |
| utrans_toRules | Introduced into icuin.dll in 10.0.16299. |
| utrans_getSourceSet | Introduced into icuin.dll in 10.0.16299. |
| uspoof_check2 | Introduced into icuin.dll in 10.0.17763. |
| uspoof_check2UTF8 | Introduced into icuin.dll in 10.0.17763. |
| uspoof_closeCheckResult | Introduced into icuin.dll in 10.0.17763. |
| uspoof_getCheckResultChecks | Introduced into icuin.dll in 10.0.17763. |
| uspoof_getCheckResultNumerics | Introduced into icuin.dll in 10.0.17763. |
| uspoof_getCheckResultRestrictionLevel | Introduced into icuin.dll in 10.0.17763. |
| uspoof_openCheckResult | Introduced into icuin.dll in 10.0.17763. |
| unum_formatDoubleForFields | Introduced into icuin.dll in 10.0.17763. |
| uplrules_getKeywords | Introduced into icuin.dll in 10.0.17763. |


## APIs from api-ms-win-core-namedpipe-ansi-l1-1-1.dll

| API | Requirements |
| -----| --------------|
| [CallNamedPipe](https://msdn.microsoft.com/library/Aa365144(v=VS.85).aspx) | Introduced into api-ms-win-core-namedpipe-ansi-l1-1-1.dll in 10.0.16299. Moved into api-ms-win-core-namedpipe-l1-2-2.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from crypt32.dll

| API | Requirements |
| -----| --------------|
| [CertGetNameString](https://msdn.microsoft.com/library/Aa376086(v=VS.85).aspx) | Introduced into crypt32.dll in 10.0.16299. Removed in 10.0.17134. |
| [CertNameToStr](https://msdn.microsoft.com/library/Aa376556(v=VS.85).aspx) | Introduced into crypt32.dll in 10.0.16299. Removed in 10.0.17134. |
| [CertRDNValueToStr](https://msdn.microsoft.com/library/Aa376561(v=VS.85).aspx) | Introduced into crypt32.dll in 10.0.16299. Removed in 10.0.17134. |
| [CertStrToName](https://msdn.microsoft.com/library/Aa377160(v=VS.85).aspx) | Introduced into crypt32.dll in 10.0.16299. Removed in 10.0.17134. |
| [CryptBinaryToString](https://msdn.microsoft.com/library/Aa379887(v=VS.85).aspx) | Introduced into crypt32.dll in 10.0.16299. Removed in 10.0.17134. |
| [CryptStringToBinary](https://msdn.microsoft.com/library/Aa380285(v=VS.85).aspx) | Introduced into crypt32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-downlevel-advapi32-l2-1-1.dll

| API | Requirements |
| -----| --------------|
| [ControlTrace](https://msdn.microsoft.com/library/windows/desktop/aa363696.aspx) | Introduced into api-ms-win-downlevel-advapi32-l2-1-1.dll in 10.0.16299. Moved into api-ms-win-eventing-controller-l1-1-0.dll in 10.0.16299. Moved into advapi32.dll in 10.0.16299. Removed in 10.0.17134. |
| [ConvertSecurityDescriptorToStringSecurityDescriptor](https://msdn.microsoft.com/library/Aa376397(v=VS.85).aspx) | Introduced into api-ms-win-downlevel-advapi32-l2-1-1.dll in 10.0.16299. Moved into api-ms-win-security-sddl-l1-1-0.dll in 10.0.16299. Moved into advapi32.dll in 10.0.16299. Removed in 10.0.17134. |
| [OpenTrace](https://msdn.microsoft.com/library/windows/desktop/aa364089.aspx) | Introduced into api-ms-win-downlevel-advapi32-l2-1-1.dll in 10.0.16299. Moved into api-ms-win-eventing-consumer-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-eventing-consumer-l1-1-1.dll in 10.0.16299. Moved into advapi32.dll in 10.0.16299. Removed in 10.0.17134. |
| [StartTrace](https://msdn.microsoft.com/library/windows/desktop/aa364117.aspx) | Introduced into api-ms-win-downlevel-advapi32-l2-1-1.dll in 10.0.16299. Moved into api-ms-win-eventing-controller-l1-1-0.dll in 10.0.16299. Moved into advapi32.dll in 10.0.16299. Removed in 10.0.17134. |
| [StopTrace](https://msdn.microsoft.com/library/windows/desktop/aa364119.aspx) | Introduced into api-ms-win-downlevel-advapi32-l2-1-1.dll in 10.0.16299. Moved into api-ms-win-eventing-controller-l1-1-0.dll in 10.0.16299. Moved into advapi32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-security-sddl-ansi-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [ConvertSidToStringSid](https://msdn.microsoft.com/library/Aa376399(v=VS.85).aspx) | Introduced into api-ms-win-security-sddl-ansi-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-advapi32-l2-1-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-advapi32-l2-1-1.dll in 10.0.16299. Moved into api-ms-win-security-sddl-l1-1-0.dll in 10.0.16299. Moved into advapi32.dll in 10.0.16299. Removed in 10.0.17134. |
| [ConvertStringSidToSid](https://msdn.microsoft.com/library/Aa376402(v=VS.85).aspx) | Introduced into api-ms-win-security-sddl-ansi-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-advapi32-l2-1-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-advapi32-l2-1-1.dll in 10.0.16299. Moved into api-ms-win-security-sddl-l1-1-0.dll in 10.0.16299. Moved into advapi32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-core-kernel32-legacy-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [CopyFile](https://msdn.microsoft.com/library/Aa363851(v=VS.85).aspx) | Introduced into api-ms-win-core-kernel32-legacy-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-1.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-2.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-3.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-4.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-5.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-6.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l2-1-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l2-1-2.dll in 10.0.16299. Moved into api-ms-win-core-file-l2-1-3.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [CreateNamedPipe](https://msdn.microsoft.com/library/Aa365150(v=VS.85).aspx) | Introduced into api-ms-win-core-kernel32-legacy-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-1.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-2.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-3.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-4.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-5.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-6.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l2-1-0.dll in 10.0.16299. Moved into api-ms-win-core-namedpipe-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-namedpipe-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-namedpipe-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-core-namedpipe-l1-2-2.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [GetComputerName](https://msdn.microsoft.com/library/ms724295(v=VS.85).aspx) | Introduced into api-ms-win-core-kernel32-legacy-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-1.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-2.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-3.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-4.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-5.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-6.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l2-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [GetStringTypeEx](https://msdn.microsoft.com/library/windows/desktop/dd318118.aspx) | Introduced into api-ms-win-core-kernel32-legacy-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-1.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-2.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-3.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-4.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-5.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-6.dll in 10.0.16299. Moved into api-ms-win-core-localization-ansi-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-deprecated-apis-legacy-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-deprecated-apis-legacy-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l2-1-0.dll in 10.0.16299. Moved into api-ms-win-core-string-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [MoveFileEx](https://msdn.microsoft.com/library/windows/desktop/aa365240.aspx) | Introduced into api-ms-win-core-kernel32-legacy-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-1.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-2.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-3.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-4.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-5.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-6.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l2-1-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l2-1-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l2-1-1.dll in 10.0.16299. Moved into api-ms-win-core-file-l2-1-2.dll in 10.0.16299. Moved into api-ms-win-core-file-l2-1-3.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-core-file-ansi-l2-1-0.dll

| API | Requirements |
| -----| --------------|
| [CopyFileEx](https://msdn.microsoft.com/library/Aa363852(v=VS.85).aspx) | Introduced into api-ms-win-core-file-ansi-l2-1-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l2-1-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l2-1-1.dll in 10.0.16299. Moved into api-ms-win-core-file-l2-1-2.dll in 10.0.16299. Moved into api-ms-win-core-file-l2-1-3.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [ReplaceFile](https://msdn.microsoft.com/library/Aa365512(v=VS.85).aspx) | Introduced into api-ms-win-core-file-ansi-l2-1-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l2-1-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l2-1-1.dll in 10.0.16299. Moved into api-ms-win-core-file-l2-1-2.dll in 10.0.16299. Moved into api-ms-win-core-file-l2-1-3.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-core-namespace-ansi-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [CreateBoundaryDescriptor](https://msdn.microsoft.com/library/ms682121(v=VS.85).aspx) | Introduced into api-ms-win-core-namespace-ansi-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-namespace-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [CreatePrivateNamespace](https://msdn.microsoft.com/library/ms682419(v=VS.85).aspx) | Introduced into api-ms-win-core-namespace-ansi-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-namespace-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [OpenPrivateNamespace](https://msdn.microsoft.com/library/ms684318(v=VS.85).aspx) | Introduced into api-ms-win-core-namespace-ansi-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-namespace-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-core-file-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [CreateDirectory](https://msdn.microsoft.com/library/windows/desktop/aa363855.aspx) | Introduced into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [DeleteFile](https://msdn.microsoft.com/library/windows/desktop/aa363915.aspx) | Introduced into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [FindNextFile](https://msdn.microsoft.com/library/windows/desktop/aa364428.aspx) | Introduced into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [FindFirstFile](https://msdn.microsoft.com/library/Aa364418(v=VS.85).aspx) | Introduced into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [FindFirstFileEx](https://msdn.microsoft.com/library/windows/desktop/aa364419.aspx) | Introduced into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [GetDiskFreeSpace](https://msdn.microsoft.com/library/Aa364935(v=VS.85).aspx) | Introduced into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [GetDriveType](https://msdn.microsoft.com/library/Aa364939(v=VS.85).aspx) | Introduced into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [GetFileAttributes](https://msdn.microsoft.com/library/Aa364944(v=VS.85).aspx) | Introduced into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [GetFullPathName](https://msdn.microsoft.com/library/Aa364963(v=VS.85).aspx) | Introduced into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [GetDiskFreeSpaceEx](https://msdn.microsoft.com/library/windows/desktop/aa364937.aspx) | Introduced into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [GetFileAttributesEx](https://msdn.microsoft.com/library/windows/desktop/aa364946.aspx) | Introduced into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [GetFinalPathNameByHandle](https://msdn.microsoft.com/library/Aa364962(v=VS.85).aspx) | Introduced into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [GetLongPathName](https://msdn.microsoft.com/library/Aa364980(v=VS.85).aspx) | Introduced into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [RemoveDirectory](https://msdn.microsoft.com/library/windows/desktop/aa365488.aspx) | Introduced into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [SetFileAttributes](https://msdn.microsoft.com/library/windows/desktop/aa365535.aspx) | Introduced into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-core-synch-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [CreateEvent](https://msdn.microsoft.com/library/Ff975304(v=VS.85).aspx) | Introduced into api-ms-win-core-synch-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [CreateEventEx](https://msdn.microsoft.com/library/windows/desktop/ms682400.aspx) | Introduced into api-ms-win-core-synch-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [CreateMutex](https://msdn.microsoft.com/library/ms682411(v=VS.85).aspx) | Introduced into api-ms-win-core-synch-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [CreateMutexEx](https://msdn.microsoft.com/library/windows/desktop/ms682418.aspx) | Introduced into api-ms-win-core-synch-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [OpenEvent](https://msdn.microsoft.com/library/windows/desktop/ms684305.aspx) | Introduced into api-ms-win-core-synch-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [OpenSemaphore](https://msdn.microsoft.com/library/windows/desktop/ms684326.aspx) | Introduced into api-ms-win-core-synch-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-security-cpwl-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| CreateProcessWithLogon | Introduced into api-ms-win-security-cpwl-l1-1-0.dll in 10.0.16299. Moved into advapi32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-core-processthreads-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [CreateProcess](https://msdn.microsoft.com/library/Hh437462(v=VS.85).aspx) | Introduced into api-ms-win-core-processthreads-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-processthreads-l1-1-1.dll in 10.0.16299. Moved into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.16299. Moved into api-ms-win-core-processthreads-l1-1-3.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-core-kernel32-legacy-l1-1-2.dll

| API | Requirements |
| -----| --------------|
| [CreateSemaphore](https://msdn.microsoft.com/library/ms682438(v=VS.85).aspx) | Introduced into api-ms-win-core-kernel32-legacy-l1-1-2.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-3.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-4.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-5.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-6.dll in 10.0.16299. Moved into api-ms-win-core-synch-ansi-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-1.dll in 10.0.16299. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l2-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [OpenMutex](https://msdn.microsoft.com/library/windows/desktop/ms684315.aspx) | Introduced into api-ms-win-core-kernel32-legacy-l1-1-2.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-3.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-4.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-5.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-6.dll in 10.0.16299. Moved into api-ms-win-core-synch-ansi-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-synch-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-core-synch-ansi-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [CreateSemaphoreEx](https://msdn.microsoft.com/library/windows/desktop/ms682446.aspx) | Introduced into api-ms-win-core-synch-ansi-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-synch-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [CreateWaitableTimer](https://msdn.microsoft.com/library/ms682492(v=VS.85).aspx) | Introduced into api-ms-win-core-synch-ansi-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [CreateWaitableTimerEx](https://msdn.microsoft.com/library/ms682494(v=VS.85).aspx) | Introduced into api-ms-win-core-synch-ansi-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-synch-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [OpenWaitableTimer](https://msdn.microsoft.com/library/ms684337(v=VS.85).aspx) | Introduced into api-ms-win-core-synch-ansi-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-synch-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from ext-ms-win-security-credui-l1-1-1.dll

| API | Requirements |
| -----| --------------|
| [CredUIParseUserName](https://msdn.microsoft.com/library/Aa375175(v=VS.85).aspx) | Introduced into ext-ms-win-security-credui-l1-1-1.dll in 10.0.16299. Moved into Credui.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-security-cryptoapi-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [CryptAcquireContext](https://msdn.microsoft.com/library/Aa379886(v=VS.85).aspx) | Introduced into api-ms-win-security-cryptoapi-l1-1-0.dll in 10.0.16299. Moved into advapi32.dll in 10.0.16299. Removed in 10.0.17134. |
| [CryptGetDefaultProvider](https://msdn.microsoft.com/library/Aa379945(v=VS.85).aspx) | Introduced into api-ms-win-security-cryptoapi-l1-1-0.dll in 10.0.16299. Moved into advapi32.dll in 10.0.16299. Removed in 10.0.17134. |
| [CryptSignHash](https://msdn.microsoft.com/library/Aa380280(v=VS.85).aspx) | Introduced into api-ms-win-security-cryptoapi-l1-1-0.dll in 10.0.16299. Moved into advapi32.dll in 10.0.16299. Removed in 10.0.17134. |
| [CryptVerifySignature](https://msdn.microsoft.com/library/Aa381097(v=VS.85).aspx) | Introduced into api-ms-win-security-cryptoapi-l1-1-0.dll in 10.0.16299. Moved into advapi32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-core-file-ansi-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [DeleteVolumeMountPoint](https://msdn.microsoft.com/library/Aa363927(v=VS.85).aspx) | Introduced into api-ms-win-core-file-ansi-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-core-localization-l2-1-0.dll

| API | Requirements |
| -----| --------------|
| [EnumSystemCodePages](https://msdn.microsoft.com/library/windows/desktop/dd317825.aspx) | Introduced into api-ms-win-core-localization-l2-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-core-localization-ansi-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [EnumUILanguages](https://msdn.microsoft.com/library/Dd317834(v=VS.85).aspx) | Introduced into api-ms-win-core-localization-ansi-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-localization-obsolete-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-localization-obsolete-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-localization-obsolete-l1-3-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-core-processenvironment-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [ExpandEnvironmentStrings](https://msdn.microsoft.com/library/ms724265(v=VS.85).aspx) | Introduced into api-ms-win-core-processenvironment-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-processenvironment-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [FreeEnvironmentStrings](https://msdn.microsoft.com/library/ms683151(v=VS.85).aspx) | Introduced into api-ms-win-core-processenvironment-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-processenvironment-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [GetCommandLine](https://msdn.microsoft.com/library/windows/desktop/ms683156.aspx) | Introduced into api-ms-win-core-processenvironment-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-processenvironment-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [GetCurrentDirectory](https://msdn.microsoft.com/library/Aa364934(v=VS.85).aspx) | Introduced into api-ms-win-core-processenvironment-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-processenvironment-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [GetEnvironmentVariable](https://msdn.microsoft.com/library/ms683188(v=VS.85).aspx) | Introduced into api-ms-win-core-processenvironment-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-processenvironment-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [SetCurrentDirectory](https://msdn.microsoft.com/library/Aa365530(v=VS.85).aspx) | Introduced into api-ms-win-core-processenvironment-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-processenvironment-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-core-console-l2-1-0.dll

| API | Requirements |
| -----| --------------|
| [FillConsoleOutputCharacter](https://msdn.microsoft.com/library/ms682663(v=VS.85).aspx) | Introduced into api-ms-win-core-console-l2-1-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [GetConsoleTitle](https://msdn.microsoft.com/library/ms683174(v=VS.85).aspx) | Introduced into api-ms-win-core-console-l2-1-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [PeekConsoleInput](https://msdn.microsoft.com/library/ms684344(v=VS.85).aspx) | Introduced into api-ms-win-core-console-l2-1-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [ReadConsoleOutput](https://msdn.microsoft.com/library/ms684965(v=VS.85).aspx) | Introduced into api-ms-win-core-console-l2-1-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [SetConsoleTitle](https://msdn.microsoft.com/library/ms686050(v=VS.85).aspx) | Introduced into api-ms-win-core-console-l2-1-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [WriteConsoleOutput](https://msdn.microsoft.com/library/ms687404(v=VS.85).aspx) | Introduced into api-ms-win-core-console-l2-1-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-eventing-legacy-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [FlushTrace](https://msdn.microsoft.com/library/windows/desktop/aa363891.aspx) | Introduced into api-ms-win-eventing-legacy-l1-1-0.dll in 10.0.16299. Moved into advapi32.dll in 10.0.16299. Removed in 10.0.17134. |
| [QueryTrace](https://msdn.microsoft.com/library/windows/desktop/aa364103.aspx) | Introduced into api-ms-win-eventing-legacy-l1-1-0.dll in 10.0.16299. Moved into advapi32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-core-localization-l1-2-0.dll

| API | Requirements |
| -----| --------------|
| [FormatMessage](https://msdn.microsoft.com/library/windows/desktop/ms679351.aspx) | Introduced into api-ms-win-core-localization-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-localization-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-core-localization-l1-2-2.dll in 10.0.16299. Moved into api-ms-win-core-misc-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [GetGeoInfo](https://msdn.microsoft.com/library/windows/desktop/dd318099.aspx) | Introduced into api-ms-win-core-localization-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-localization-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-core-localization-l1-2-2.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [GetLocaleInfo](https://msdn.microsoft.com/library/Dd318101(v=VS.85).aspx) | Introduced into api-ms-win-core-localization-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-localization-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-core-localization-l1-2-2.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-localization-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from ws2_32.dll

| API | Requirements |
| -----| --------------|
| [FreeAddrInfo](https://msdn.microsoft.com/library/ms737931(v=VS.85).aspx) | Introduced into ws2_32.dll in 10.0.16299. Removed in 10.0.17134. |
| [GetAddrInfoEx](https://msdn.microsoft.com/library/ms738518(v=VS.85).aspx) | Introduced into ws2_32.dll in 10.0.16299. Removed in 10.0.17134. |
| [GetAddrInfo](https://msdn.microsoft.com/library/ms738520(v=VS.85).aspx) | Introduced into ws2_32.dll in 10.0.16299. Removed in 10.0.17134. |
| [GetHostName](https://msdn.microsoft.com/library/ms738527(v=VS.85).aspx) | Introduced into ws2_32.dll in 10.0.16299. Removed in 10.0.17134. |
| [GetNameInfo](https://msdn.microsoft.com/library/ms738532(v=VS.85).aspx) | Introduced into ws2_32.dll in 10.0.16299. Removed in 10.0.17134. |
| [InetNtop](https://msdn.microsoft.com/library/Cc805843(v=VS.85).aspx) | Introduced into ws2_32.dll in 10.0.16299. Removed in 10.0.17134. |
| [InetPton](https://msdn.microsoft.com/library/Cc805844(v=VS.85).aspx) | Introduced into ws2_32.dll in 10.0.16299. Removed in 10.0.17134. |
| [SetAddrInfoEx](https://msdn.microsoft.com/library/windows/desktop/ms740473.aspx) | Introduced into ws2_32.dll in 10.0.16299. Removed in 10.0.17134. |
| [WSAAddressToString](https://msdn.microsoft.com/library/ms741516(v=VS.85).aspx) | Introduced into ws2_32.dll in 10.0.16299. Removed in 10.0.17134. |
| [WSAConnectByName](https://msdn.microsoft.com/library/ms741557(v=VS.85).aspx) | Introduced into ws2_32.dll in 10.0.16299. Removed in 10.0.17134. |
| [WSADuplicateSocket](https://msdn.microsoft.com/library/ms741565(v=VS.85).aspx) | Introduced into ws2_32.dll in 10.0.16299. Removed in 10.0.17134. |
| [WSAEnumNameSpaceProviders](https://msdn.microsoft.com/library/ms741570(v=VS.85).aspx) | Introduced into ws2_32.dll in 10.0.16299. Removed in 10.0.17134. |
| [WSAEnumNameSpaceProvidersEx](https://msdn.microsoft.com/library/ms741568(v=VS.85).aspx) | Introduced into ws2_32.dll in 10.0.16299. Removed in 10.0.17134. |
| [WSAEnumProtocols](https://msdn.microsoft.com/library/ms741574(v=VS.85).aspx) | Introduced into ws2_32.dll in 10.0.16299. Removed in 10.0.17134. |
| [WSAGetServiceClassInfo](https://msdn.microsoft.com/library/ms741592(v=VS.85).aspx) | Introduced into ws2_32.dll in 10.0.16299. Removed in 10.0.17134. |
| [WSAGetServiceClassNameByClassId](https://msdn.microsoft.com/library/ms741598(v=VS.85).aspx) | Introduced into ws2_32.dll in 10.0.16299. Removed in 10.0.17134. |
| [WSALookupServiceBegin](https://msdn.microsoft.com/library/ms741633(v=VS.85).aspx) | Introduced into ws2_32.dll in 10.0.16299. Removed in 10.0.17134. |
| [WSALookupServiceNext](https://msdn.microsoft.com/library/ms741641(v=VS.85).aspx) | Introduced into ws2_32.dll in 10.0.16299. Removed in 10.0.17134. |
| [WSASetService](https://msdn.microsoft.com/library/ms742211(v=VS.85).aspx) | Introduced into ws2_32.dll in 10.0.16299. Removed in 10.0.17134. |
| [WSASocket](https://msdn.microsoft.com/library/ms742212(v=VS.85).aspx) | Introduced into ws2_32.dll in 10.0.16299. Removed in 10.0.17134. |
| [WSAStringToAddress](https://msdn.microsoft.com/library/ms742214(v=VS.85).aspx) | Introduced into ws2_32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-core-namedpipe-ansi-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [GetNamedPipeClientComputerName](https://msdn.microsoft.com/library/Aa365437(v=VS.85).aspx) | Introduced into api-ms-win-core-namedpipe-ansi-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-namedpipe-ansi-l1-1-1.dll in 10.0.16299. Moved into api-ms-win-core-namedpipe-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-namedpipe-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-namedpipe-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-core-namedpipe-l1-2-2.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [GetNamedPipeHandleState](https://msdn.microsoft.com/library/Aa365443(v=VS.85).aspx) | Introduced into api-ms-win-core-namedpipe-ansi-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-namedpipe-ansi-l1-1-1.dll in 10.0.16299. Moved into api-ms-win-core-namedpipe-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-core-namedpipe-l1-2-2.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [WaitNamedPipe](https://msdn.microsoft.com/library/Aa365800(v=VS.85).aspx) | Introduced into api-ms-win-core-namedpipe-ansi-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-namedpipe-ansi-l1-1-1.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Moved into api-ms-win-core-namedpipe-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-namedpipe-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-namedpipe-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-core-namedpipe-l1-2-2.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-core-url-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [GetAcceptLanguages](https://msdn.microsoft.com/library/Bb759898(v=VS.85).aspx) | Introduced into api-ms-win-core-url-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-shlwapi-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-shlwapi-l1-1-1.dll in 10.0.16299. Moved into shlwapi.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-core-localization-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [GetCPInfoEx](https://msdn.microsoft.com/library/windows/desktop/dd318081.aspx) | Introduced into api-ms-win-core-localization-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-localization-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-localization-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-core-localization-l1-2-2.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-security-provider-ansi-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [GetExplicitEntriesFromAcl](https://msdn.microsoft.com/library/Aa446638(v=VS.85).aspx) | Introduced into api-ms-win-security-provider-ansi-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-advapi32-l3-1-0.dll in 10.0.16299. Moved into api-ms-win-security-provider-l1-1-0.dll in 10.0.16299. Moved into advapi32.dll in 10.0.16299. Removed in 10.0.17134. |
| [GetNamedSecurityInfo](https://msdn.microsoft.com/library/Aa446645(v=VS.85).aspx) | Introduced into api-ms-win-security-provider-ansi-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-advapi32-l3-1-0.dll in 10.0.16299. Moved into api-ms-win-security-provider-l1-1-0.dll in 10.0.16299. Moved into advapi32.dll in 10.0.16299. Removed in 10.0.17134. |
| [SetEntriesInAcl](https://msdn.microsoft.com/library/Aa379576(v=VS.85).aspx) | Introduced into api-ms-win-security-provider-ansi-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-advapi32-l3-1-0.dll in 10.0.16299. Moved into api-ms-win-security-provider-l1-1-0.dll in 10.0.16299. Moved into advapi32.dll in 10.0.16299. Removed in 10.0.17134. |
| [SetNamedSecurityInfo](https://msdn.microsoft.com/library/Aa379579(v=VS.85).aspx) | Introduced into api-ms-win-security-provider-ansi-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-advapi32-l3-1-0.dll in 10.0.16299. Moved into api-ms-win-security-provider-l1-1-0.dll in 10.0.16299. Moved into advapi32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from version.dll

| API | Requirements |
| -----| --------------|
| [GetFileVersionInfoEx](https://msdn.microsoft.com/library/Aa969434(v=VS.85).aspx) | Introduced into version.dll in 10.0.16299. Moved into api-ms-win-core-versionansi-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-versionansi-l1-1-1.dll in 10.0.16299. Moved into api-ms-win-core-version-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-version-l1-1-1.dll in 10.0.16299. Moved into api-ms-win-downlevel-version-l1-1-0.dll in 10.0.16299. Removed in 10.0.17134. |
| [GetFileVersionInfoSizeEx](https://msdn.microsoft.com/library/Aa969435(v=VS.85).aspx) | Introduced into version.dll in 10.0.16299. Moved into api-ms-win-core-versionansi-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-versionansi-l1-1-1.dll in 10.0.16299. Moved into api-ms-win-core-version-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-version-l1-1-1.dll in 10.0.16299. Moved into api-ms-win-downlevel-version-l1-1-0.dll in 10.0.16299. Removed in 10.0.17134. |
| [VerQueryValue](https://msdn.microsoft.com/library/ms647464(v=VS.85).aspx) | Introduced into version.dll in 10.0.16299. Moved into api-ms-win-core-versionansi-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-versionansi-l1-1-1.dll in 10.0.16299. Moved into api-ms-win-downlevel-version-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-version-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-version-l1-1-1.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from ext-ms-win-ntuser-keyboard-l1-2-0.dll

| API | Requirements |
| -----| --------------|
| [GetKeyNameText](https://msdn.microsoft.com/library/ms646300(v=VS.85).aspx) | Introduced into ext-ms-win-ntuser-keyboard-l1-2-0.dll in 10.0.16299. Moved into ext-ms-win-ntuser-keyboard-l1-3-0.dll in 10.0.16299. Moved into user32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from ext-ms-win-base-psapi-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [GetModuleBaseName](https://msdn.microsoft.com/library/ms683196(v=VS.85).aspx) | Introduced into ext-ms-win-base-psapi-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-core-libraryloader-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [GetModuleFileName](https://msdn.microsoft.com/library/ms683197(v=VS.85).aspx) | Introduced into api-ms-win-core-libraryloader-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-libraryloader-l1-1-1.dll in 10.0.16299. Moved into api-ms-win-core-libraryloader-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-libraryloader-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-core-libraryloader-l1-2-2.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-core-string-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| GetStringType | Introduced into api-ms-win-core-string-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-core-sysinfo-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [GetSystemDirectory](https://msdn.microsoft.com/library/ms724373(v=VS.85).aspx) | Introduced into api-ms-win-core-sysinfo-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-sysinfo-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-sysinfo-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-core-sysinfo-l1-2-2.dll in 10.0.16299. Moved into api-ms-win-core-sysinfo-l1-2-3.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [GetVersionEx](https://msdn.microsoft.com/library/ms724451(v=VS.85).aspx) | Introduced into api-ms-win-core-sysinfo-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-sysinfo-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-sysinfo-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-core-sysinfo-l1-2-2.dll in 10.0.16299. Moved into api-ms-win-core-sysinfo-l1-2-3.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-core-file-l1-2-2.dll

| API | Requirements |
| -----| --------------|
| [GetTempFileName](https://msdn.microsoft.com/library/Aa364991(v=VS.85).aspx) | Introduced into api-ms-win-core-file-l1-2-2.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [GetTempPath](https://msdn.microsoft.com/library/Aa364992(v=VS.85).aspx) | Introduced into api-ms-win-core-file-l1-2-2.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-1.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-2.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-3.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-4.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-5.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-6.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l2-1-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [GetVolumeInformation](https://msdn.microsoft.com/library/Aa364993(v=VS.85).aspx) | Introduced into api-ms-win-core-file-l1-2-2.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-core-kernel32-legacy-ansi-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [SetVolumeLabel](https://msdn.microsoft.com/library/Aa365560(v=VS.85).aspx) | Introduced into api-ms-win-core-kernel32-legacy-ansi-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-1.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-2.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-3.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-4.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-5.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-6.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l2-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from esent.dll

| API | Requirements |
| -----| --------------|
| JetCreateIndex4 | Introduced into esent.dll in 10.0.16299. Removed in 10.0.17134. |
| JetCreateTableColumnIndex4 | Introduced into esent.dll in 10.0.16299. Removed in 10.0.17134. |
| JetGetErrorInfo | Introduced into esent.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-core-psapi-ansi-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [K32GetModuleBaseName](https://msdn.microsoft.com/library/ms683196(v=VS.85).aspx) | Introduced into api-ms-win-core-psapi-ansi-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-psapi-obsolete-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-psapi-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [K32GetModuleFileNameEx](https://msdn.microsoft.com/library/ms683198(v=VS.85).aspx) | Introduced into api-ms-win-core-psapi-ansi-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-psapi-obsolete-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-psapi-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-security-lsalookup-ansi-l2-1-0.dll

| API | Requirements |
| -----| --------------|
| [LookupAccountName](https://msdn.microsoft.com/library/Aa379159(v=VS.85).aspx) | Introduced into api-ms-win-security-lsalookup-ansi-l2-1-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-advapi32-l4-1-0.dll in 10.0.16299. Moved into api-ms-win-security-lsalookup-l2-1-0.dll in 10.0.16299. Moved into api-ms-win-security-lsalookup-l2-1-1.dll in 10.0.16299. Moved into advapi32.dll in 10.0.16299. Removed in 10.0.17134. |
| [LookupAccountSid](https://msdn.microsoft.com/library/Aa379166(v=VS.85).aspx) | Introduced into api-ms-win-security-lsalookup-ansi-l2-1-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-advapi32-l4-1-0.dll in 10.0.16299. Moved into api-ms-win-security-lsalookup-l2-1-0.dll in 10.0.16299. Moved into api-ms-win-security-lsalookup-l2-1-1.dll in 10.0.16299. Moved into advapi32.dll in 10.0.16299. Removed in 10.0.17134. |
| [LookupPrivilegeDisplayName](https://msdn.microsoft.com/library/Aa379168(v=VS.85).aspx) | Introduced into api-ms-win-security-lsalookup-ansi-l2-1-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-advapi32-l4-1-0.dll in 10.0.16299. Moved into api-ms-win-security-lsalookup-l2-1-0.dll in 10.0.16299. Moved into api-ms-win-security-lsalookup-l2-1-1.dll in 10.0.16299. Moved into advapi32.dll in 10.0.16299. Removed in 10.0.17134. |
| [LookupPrivilegeName](https://msdn.microsoft.com/library/Aa379176(v=VS.85).aspx) | Introduced into api-ms-win-security-lsalookup-ansi-l2-1-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-advapi32-l4-1-0.dll in 10.0.16299. Moved into api-ms-win-security-lsalookup-l2-1-0.dll in 10.0.16299. Moved into api-ms-win-security-lsalookup-l2-1-1.dll in 10.0.16299. Moved into advapi32.dll in 10.0.16299. Removed in 10.0.17134. |
| [LookupPrivilegeValue](https://msdn.microsoft.com/library/Aa379180(v=VS.85).aspx) | Introduced into api-ms-win-security-lsalookup-ansi-l2-1-0.dll in 10.0.16299. Moved into ext-ms-win-advapi32-auth-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-advapi32-l4-1-0.dll in 10.0.16299. Moved into api-ms-win-security-lsalookup-l2-1-0.dll in 10.0.16299. Moved into api-ms-win-security-lsalookup-l2-1-1.dll in 10.0.16299. Moved into advapi32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from ext-ms-win-ntuser-keyboard-l1-3-0.dll

| API | Requirements |
| -----| --------------|
| [MapVirtualKey](https://msdn.microsoft.com/library/ms646306(v=VS.85).aspx) | Introduced into ext-ms-win-ntuser-keyboard-l1-3-0.dll in 10.0.16299. Moved into ext-ms-win-ntuser-keyboard-l1-1-0.dll in 10.0.16299. Moved into ext-ms-win-ntuser-keyboard-l1-1-1.dll in 10.0.16299. Moved into ext-ms-win-ntuser-keyboard-l1-2-0.dll in 10.0.16299. Moved into user32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from ext-ms-win-ntuser-keyboard-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [MapVirtualKeyEx](https://msdn.microsoft.com/library/ms646307(v=VS.85).aspx) | Introduced into ext-ms-win-ntuser-keyboard-l1-1-0.dll in 10.0.16299. Moved into ext-ms-win-ntuser-keyboard-l1-1-1.dll in 10.0.16299. Moved into ext-ms-win-ntuser-keyboard-l1-2-0.dll in 10.0.16299. Moved into ext-ms-win-ntuser-keyboard-l1-3-0.dll in 10.0.16299. Moved into user32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-core-debug-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [OutputDebugString](https://msdn.microsoft.com/library/windows/desktop/aa363362.aspx) | Introduced into api-ms-win-core-debug-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-debug-l1-1-1.dll in 10.0.16299. Moved into api-ms-win-core-debug-l1-1-2.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-core-console-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [ReadConsoleInput](https://msdn.microsoft.com/library/ms684961(v=VS.85).aspx) | Introduced into api-ms-win-core-console-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [ReadConsole](https://msdn.microsoft.com/library/ms684958(v=VS.85).aspx) | Introduced into api-ms-win-core-console-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [WriteConsole](https://msdn.microsoft.com/library/ms687401(v=VS.85).aspx) | Introduced into api-ms-win-core-console-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-core-file-l2-1-0.dll

| API | Requirements |
| -----| --------------|
| ReadDirectoryChanges | Introduced into api-ms-win-core-file-l2-1-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l2-1-1.dll in 10.0.16299. Moved into api-ms-win-core-file-l2-1-2.dll in 10.0.16299. Moved into api-ms-win-core-file-l2-1-3.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-downlevel-advapi32-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [RegisterTraceGuids](https://msdn.microsoft.com/library/windows/desktop/aa364105.aspx) | Introduced into api-ms-win-downlevel-advapi32-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-advapi32-l1-1-1.dll in 10.0.16299. Moved into api-ms-win-eventing-classicprovider-l1-1-0.dll in 10.0.16299. Moved into advapi32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-core-synch-l1-2-0.dll

| API | Requirements |
| -----| --------------|
| SleepConditionVariableSR | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-crt-process-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| _beep | Introduced into api-ms-win-crt-process-l1-1-0.dll in 10.0.17134. |


## APIs from tbs.dll

| API | Requirements |
| -----| --------------|
| [Tbsi_Context_Create](https://msdn.microsoft.com/library/Aa446800(v=VS.85).aspx) | Introduced into tbs.dll in 10.0.17134. |
| [Tbsi_GetDeviceInfo](https://msdn.microsoft.com/library/JJ553827(v=VS.85).aspx) | Introduced into tbs.dll in 10.0.17134. |
| [Tbsi_Get_OwnerAuth](https://msdn.microsoft.com/library/JJ553828(v=VS.85).aspx) | Introduced into tbs.dll in 10.0.17134. |
| [Tbsi_Get_TCG_Log](https://msdn.microsoft.com/library/Bb530712(v=VS.85).aspx) | Introduced into tbs.dll in 10.0.17134. |
| [Tbsi_Physical_Presence_Command](https://msdn.microsoft.com/library/Aa446801(v=VS.85).aspx) | Introduced into tbs.dll in 10.0.17134. |
| [Tbsi_Revoke_Attestation](https://msdn.microsoft.com/library/JJ553829(v=VS.85).aspx) | Introduced into tbs.dll in 10.0.17134. |
| [Tbsip_Cancel_Commands](https://msdn.microsoft.com/library/Aa446797(v=VS.85).aspx) | Introduced into tbs.dll in 10.0.17134. |
| [Tbsip_Context_Close](https://msdn.microsoft.com/library/Aa446798(v=VS.85).aspx) | Introduced into tbs.dll in 10.0.17134. |
| [Tbsip_Submit_Command](https://msdn.microsoft.com/library/Aa446799(v=VS.85).aspx) | Introduced into tbs.dll in 10.0.17134. |


## APIs from api-ms-win-core-rtlsupport-l1-2-0.dll

| API | Requirements |
| -----| --------------|
| [RtlVirtualUnwind](https://msdn.microsoft.com/library/ms680617(v=VS.85).aspx) | Introduced into api-ms-win-core-rtlsupport-l1-2-0.dll in 10.0.17763. |


COM interfaces

| API | Requirements |
| -----| --------------|
| [_IRDPSessionEvents](https://msdn.microsoft.com/library/windows/desktop/aa373879.aspx) | Introduced in 10.0.10240. |
| _IWorkspaceBrokerAxEvents | Introduced in 10.0.10240. |
| [IAccessibleEx](https://msdn.microsoft.com/library/windows/desktop/ee671234.aspx) | Introduced in 10.0.10240. |
| [IAccessibleHostingElementProviders](https://msdn.microsoft.com/library/windows/desktop/hh448733.aspx) | Introduced in 10.0.10240. |
| [IActivateAudioInterfaceAsyncOperation](https://msdn.microsoft.com/library/windows/desktop/jj128300.aspx) | Introduced in 10.0.10240. |
| [IActivateAudioInterfaceCompletionHandler](https://msdn.microsoft.com/library/windows/desktop/jj128302.aspx) | Introduced in 10.0.10240. |
| [IActivationFactory](https://msdn.microsoft.com/library/windows/desktop/br205779.aspx) | Introduced in 10.0.10240. |
| [IAdvancedMediaCapture](https://msdn.microsoft.com/library/windows/desktop/hh802709.aspx) | Introduced in 10.0.10240. |
| [IAdvancedMediaCaptureInitializationSettings](https://msdn.microsoft.com/library/windows/desktop/hh802710.aspx) | Introduced in 10.0.10240. |
| [IAdvancedMediaCaptureSettings](https://msdn.microsoft.com/library/windows/desktop/hh802712.aspx) | Introduced in 10.0.10240. |
| [IAgileObject](https://msdn.microsoft.com/library/windows/desktop/hh802476.aspx) | Introduced in 10.0.10240. |
| [IAgileReference](https://msdn.microsoft.com/library/windows/desktop/dn269837.aspx) | Introduced in 10.0.10240. |
| [IAnnotationProvider](https://msdn.microsoft.com/library/windows/desktop/hh448757.aspx) | Introduced in 10.0.10240. |
| IAoWAppActivatedRuntime | Introduced in 10.0.10240. Removed in 10.0.16299. |
| IAoWBackgroundTaskRuntime | Introduced in 10.0.10240. Removed in 10.0.16299. |
| [IApartmentShutdown](https://msdn.microsoft.com/library/windows/desktop/jj219263.aspx) | Introduced in 10.0.10240. |
| [IAsyncInfo](https://msdn.microsoft.com/library/windows/desktop/br205795.aspx) | Introduced in 10.0.10240. |
| [IAudioCaptureClient](https://msdn.microsoft.com/library/windows/desktop/dd370858.aspx) | Introduced in 10.0.10240. |
| [IAudioClient](https://msdn.microsoft.com/library/windows/desktop/dd370865.aspx) | Introduced in 10.0.10240. |
| [IAudioClient2](https://msdn.microsoft.com/library/windows/desktop/hh404179.aspx) | Introduced in 10.0.10240. |
| [IAudioClient3](https://msdn.microsoft.com/library/windows/desktop/dn911487.aspx) | Introduced in 10.0.10240. |
| [IAudioClock](https://msdn.microsoft.com/library/windows/desktop/dd370881.aspx) | Introduced in 10.0.10240. |
| [IAudioEndpointVolume](https://msdn.microsoft.com/library/windows/desktop/dd370892.aspx) | Introduced in 10.0.10240. |
| [IAudioEndpointVolumeCallback](https://msdn.microsoft.com/library/windows/desktop/dd370894.aspx) | Introduced in 10.0.10240. |
| [IAudioFrameNative](https://msdn.microsoft.com/library/windows/desktop/mt431700.aspx) | Introduced in 10.0.10240. |
| [IAudioFrameNativeFactory](https://msdn.microsoft.com/library/windows/desktop/mt431701.aspx) | Introduced in 10.0.10240. |
| [IAudioMeterInformation](https://msdn.microsoft.com/library/windows/desktop/dd368227.aspx) | Introduced in 10.0.10240. |
| [IAudioRenderClient](https://msdn.microsoft.com/library/windows/desktop/dd368242.aspx) | Introduced in 10.0.10240. |
| [IAudioSessionControl](https://msdn.microsoft.com/library/windows/desktop/dd368246.aspx) | Introduced in 10.0.10240. |
| [IAudioSessionEvents](https://msdn.microsoft.com/library/windows/desktop/dd368289.aspx) | Introduced in 10.0.10240. |
| [IAudioStreamVolume](https://msdn.microsoft.com/library/windows/desktop/dd370977.aspx) | Introduced in 10.0.10240. |
| IAudioVideoCaptureDeviceNative | Introduced in 10.0.10240. |
| [IBindCtx](https://msdn.microsoft.com/library/windows/desktop/ms693755.aspx) | Introduced in 10.0.10240. |
| ICameraCaptureDeviceNative | Introduced in 10.0.10240. |
| ICameraCaptureFrameNative | Introduced in 10.0.10240. |
| ICameraCapturePreviewSink | Introduced in 10.0.10240. |
| [ICameraUIControl](https://msdn.microsoft.com/library/windows/desktop/hh802717.aspx) | Introduced in 10.0.10240. |
| [ICameraUIControlEventCallback](https://msdn.microsoft.com/library/windows/desktop/hh802718.aspx) | Introduced in 10.0.10240. |
| [IClassFactory](https://msdn.microsoft.com/library/windows/desktop/ms694364.aspx) | Introduced in 10.0.10240. |
| [IClientSecurity](https://msdn.microsoft.com/library/windows/desktop/ms683964.aspx) | Introduced in 10.0.10240. |
| [ICodecAPI](https://msdn.microsoft.com/library/windows/desktop/dd311953.aspx) | Introduced in 10.0.10240. |
| [IConnectionPoint](https://msdn.microsoft.com/library/windows/desktop/ms694318.aspx) | Introduced in 10.0.10240. |
| [IConnectionPointContainer](https://msdn.microsoft.com/library/windows/desktop/ms683857.aspx) | Introduced in 10.0.10240. |
| [IContextCallback](https://msdn.microsoft.com/library/windows/desktop/ms682253.aspx) | Introduced in 10.0.10240. |
| [ICreateDeviceAccessAsync](https://msdn.microsoft.com/library/windows/desktop/hh404248.aspx) | Introduced in 10.0.10240. |
| ICustomNavigationProvider | Introduced in 10.0.10240. |
| [ID2D1AnalysisTransform](https://msdn.microsoft.com/library/windows/desktop/hh404347.aspx) | Introduced in 10.0.10240. |
| [ID2D1Bitmap](https://msdn.microsoft.com/library/windows/desktop/dd371109.aspx) | Introduced in 10.0.10240. |
| [ID2D1Bitmap1](https://msdn.microsoft.com/library/windows/desktop/hh404349.aspx) | Introduced in 10.0.10240. |
| [ID2D1BitmapBrush](https://msdn.microsoft.com/library/windows/desktop/dd371122.aspx) | Introduced in 10.0.10240. |
| [ID2D1BitmapRenderTarget](https://msdn.microsoft.com/library/windows/desktop/dd371146.aspx) | Introduced in 10.0.10240. |
| [ID2D1BlendTransform](https://msdn.microsoft.com/library/windows/desktop/hh404361.aspx) | Introduced in 10.0.10240. |
| [ID2D1BorderTransform](https://msdn.microsoft.com/library/windows/desktop/hh404367.aspx) | Introduced in 10.0.10240. |
| [ID2D1BoundsAdjustmentTransform](https://msdn.microsoft.com/library/windows/desktop/hh847963.aspx) | Introduced in 10.0.10240. |
| [ID2D1Brush](https://msdn.microsoft.com/library/windows/desktop/dd371173.aspx) | Introduced in 10.0.10240. |
| [ID2D1ColorContext](https://msdn.microsoft.com/library/windows/desktop/hh404388.aspx) | Introduced in 10.0.10240. |
| [ID2D1CommandList](https://msdn.microsoft.com/library/windows/desktop/hh404392.aspx) | Introduced in 10.0.10240. |
| [ID2D1CommandSink](https://msdn.microsoft.com/library/windows/desktop/hh404394.aspx) | Introduced in 10.0.10240. |
| [ID2D1CommandSink1](https://msdn.microsoft.com/library/windows/desktop/dn280436.aspx) | Introduced in 10.0.10240. |
| [ID2D1CommandSink2](https://msdn.microsoft.com/library/windows/desktop/dn890781.aspx) | Introduced in 10.0.10240. |
| [ID2D1ComputeInfo](https://msdn.microsoft.com/library/windows/desktop/hh847966.aspx) | Introduced in 10.0.10240. |
| [ID2D1ComputeTransform](https://msdn.microsoft.com/library/windows/desktop/hh404434.aspx) | Introduced in 10.0.10240. |
| [ID2D1ConcreteTransform](https://msdn.microsoft.com/library/windows/desktop/hh404452.aspx) | Introduced in 10.0.10240. |
| [ID2D1DCRenderTarget](https://msdn.microsoft.com/library/windows/desktop/dd371213.aspx) | Introduced in 10.0.10240. |
| [ID2D1Device](https://msdn.microsoft.com/library/windows/desktop/hh404478.aspx) | Introduced in 10.0.10240. |
| [ID2D1Device1](https://msdn.microsoft.com/library/windows/desktop/dn280458.aspx) | Introduced in 10.0.10240. |
| [ID2D1Device2](https://msdn.microsoft.com/library/windows/desktop/dn890786.aspx) | Introduced in 10.0.10240. |
| [ID2D1DeviceContext](https://msdn.microsoft.com/library/windows/desktop/hh404479.aspx) | Introduced in 10.0.10240. |
| [ID2D1DeviceContext1](https://msdn.microsoft.com/library/windows/desktop/dn280461.aspx) | Introduced in 10.0.10240. |
| [ID2D1DeviceContext2](https://msdn.microsoft.com/library/windows/desktop/dn890789.aspx) | Introduced in 10.0.10240. |
| [ID2D1DrawInfo](https://msdn.microsoft.com/library/windows/desktop/hh847986.aspx) | Introduced in 10.0.10240. |
| [ID2D1DrawingStateBlock](https://msdn.microsoft.com/library/windows/desktop/dd371218.aspx) | Introduced in 10.0.10240. |
| [ID2D1DrawingStateBlock1](https://msdn.microsoft.com/library/windows/desktop/hh871452.aspx) | Introduced in 10.0.10240. |
| [ID2D1DrawTransform](https://msdn.microsoft.com/library/windows/desktop/hh847992.aspx) | Introduced in 10.0.10240. |
| [ID2D1Effect](https://msdn.microsoft.com/library/windows/desktop/hh404566.aspx) | Introduced in 10.0.10240. |
| [ID2D1EffectContext](https://msdn.microsoft.com/library/windows/desktop/hh404459.aspx) | Introduced in 10.0.10240. |
| [ID2D1EffectContext1](https://msdn.microsoft.com/library/windows/desktop/dn949338.aspx) | Introduced in 10.0.10240. |
| [ID2D1EffectImpl](https://msdn.microsoft.com/library/windows/desktop/hh404568.aspx) | Introduced in 10.0.10240. |
| [ID2D1EllipseGeometry](https://msdn.microsoft.com/library/windows/desktop/dd371239.aspx) | Introduced in 10.0.10240. |
| [ID2D1Factory](https://msdn.microsoft.com/library/windows/desktop/dd371246.aspx) | Introduced in 10.0.10240. |
| [ID2D1Factory1](https://msdn.microsoft.com/library/windows/desktop/hh404596.aspx) | Introduced in 10.0.10240. |
| [ID2D1Factory2](https://msdn.microsoft.com/library/windows/desktop/dn280481.aspx) | Introduced in 10.0.10240. |
| [ID2D1Factory3](https://msdn.microsoft.com/library/windows/desktop/dn900394.aspx) | Introduced in 10.0.10240. |
| [ID2D1GdiMetafile](https://msdn.microsoft.com/library/windows/desktop/hh871460.aspx) | Introduced in 10.0.10240. |
| [ID2D1GdiMetafile1](https://msdn.microsoft.com/library/windows/desktop/dn900400.aspx) | Introduced in 10.0.10240. |
| [ID2D1GdiMetafileSink](https://msdn.microsoft.com/library/windows/desktop/hh871461.aspx) | Introduced in 10.0.10240. |
| [ID2D1GdiMetafileSink1](https://msdn.microsoft.com/library/windows/desktop/dn900403.aspx) | Introduced in 10.0.10240. |
| [ID2D1Geometry](https://msdn.microsoft.com/library/windows/desktop/dd316578.aspx) | Introduced in 10.0.10240. |
| [ID2D1GeometryGroup](https://msdn.microsoft.com/library/windows/desktop/dd316581.aspx) | Introduced in 10.0.10240. |
| [ID2D1GeometryRealization](https://msdn.microsoft.com/library/windows/desktop/dn280515.aspx) | Introduced in 10.0.10240. |
| [ID2D1GeometrySink](https://msdn.microsoft.com/library/windows/desktop/dd316592.aspx) | Introduced in 10.0.10240. |
| [ID2D1GradientMesh](https://msdn.microsoft.com/library/windows/desktop/dn900410.aspx) | Introduced in 10.0.10240. |
| [ID2D1GradientStopCollection](https://msdn.microsoft.com/library/windows/desktop/dd316783.aspx) | Introduced in 10.0.10240. |
| [ID2D1GradientStopCollection1](https://msdn.microsoft.com/library/windows/desktop/hh446792.aspx) | Introduced in 10.0.10240. |
| [ID2D1HwndRenderTarget](https://msdn.microsoft.com/library/windows/desktop/dd371461.aspx) | Introduced in 10.0.10240. |
| [ID2D1Image](https://msdn.microsoft.com/library/windows/desktop/hh446803.aspx) | Introduced in 10.0.10240. |
| [ID2D1ImageBrush](https://msdn.microsoft.com/library/windows/desktop/hh446804.aspx) | Introduced in 10.0.10240. |
| [ID2D1ImageSource](https://msdn.microsoft.com/library/windows/desktop/dn900413.aspx) | Introduced in 10.0.10240. |
| [ID2D1ImageSourceFromWic](https://msdn.microsoft.com/library/windows/desktop/dn900414.aspx) | Introduced in 10.0.10240. |
| [ID2D1Ink](https://msdn.microsoft.com/library/windows/desktop/dn900426.aspx) | Introduced in 10.0.10240. |
| [ID2D1InkStyle](https://msdn.microsoft.com/library/windows/desktop/dn900427.aspx) | Introduced in 10.0.10240. |
| [ID2D1Layer](https://msdn.microsoft.com/library/windows/desktop/dd371483.aspx) | Introduced in 10.0.10240. |
| [ID2D1LinearGradientBrush](https://msdn.microsoft.com/library/windows/desktop/dd371488.aspx) | Introduced in 10.0.10240. |
| [ID2D1LookupTable3D](https://msdn.microsoft.com/library/windows/desktop/dn900453.aspx) | Introduced in 10.0.10240. |
| [ID2D1Mesh](https://msdn.microsoft.com/library/windows/desktop/dd371508.aspx) | Introduced in 10.0.10240. |
| [ID2D1Multithread](https://msdn.microsoft.com/library/windows/desktop/hh997713.aspx) | Introduced in 10.0.10240. |
| [ID2D1OffsetTransform](https://msdn.microsoft.com/library/windows/desktop/hh446820.aspx) | Introduced in 10.0.10240. |
| [ID2D1PathGeometry](https://msdn.microsoft.com/library/windows/desktop/dd371512.aspx) | Introduced in 10.0.10240. |
| [ID2D1PathGeometry1](https://msdn.microsoft.com/library/windows/desktop/hh446826.aspx) | Introduced in 10.0.10240. |
| [ID2D1PrintControl](https://msdn.microsoft.com/library/windows/desktop/hh847997.aspx) | Introduced in 10.0.10240. |
| [ID2D1Properties](https://msdn.microsoft.com/library/windows/desktop/hh446854.aspx) | Introduced in 10.0.10240. |
| [ID2D1RadialGradientBrush](https://msdn.microsoft.com/library/windows/desktop/dd371529.aspx) | Introduced in 10.0.10240. |
| [ID2D1RectangleGeometry](https://msdn.microsoft.com/library/windows/desktop/dd371561.aspx) | Introduced in 10.0.10240. |
| [ID2D1RenderInfo](https://msdn.microsoft.com/library/windows/desktop/hh446890.aspx) | Introduced in 10.0.10240. |
| [ID2D1RenderTarget](https://msdn.microsoft.com/library/windows/desktop/dd371766.aspx) | Introduced in 10.0.10240. |
| [ID2D1Resource](https://msdn.microsoft.com/library/windows/desktop/dd316908.aspx) | Introduced in 10.0.10240. |
| [ID2D1ResourceTexture](https://msdn.microsoft.com/library/windows/desktop/hh446904.aspx) | Introduced in 10.0.10240. |
| [ID2D1RoundedRectangleGeometry](https://msdn.microsoft.com/library/windows/desktop/dd316914.aspx) | Introduced in 10.0.10240. |
| [ID2D1SimplifiedGeometrySink](https://msdn.microsoft.com/library/windows/desktop/dd316919.aspx) | Introduced in 10.0.10240. |
| [ID2D1SolidColorBrush](https://msdn.microsoft.com/library/windows/desktop/dd372207.aspx) | Introduced in 10.0.10240. |
| [ID2D1SourceTransform](https://msdn.microsoft.com/library/windows/desktop/hh446908.aspx) | Introduced in 10.0.10240. |
| [ID2D1StrokeStyle](https://msdn.microsoft.com/library/windows/desktop/dd372217.aspx) | Introduced in 10.0.10240. |
| [ID2D1StrokeStyle1](https://msdn.microsoft.com/library/windows/desktop/hh446914.aspx) | Introduced in 10.0.10240. |
| [ID2D1TessellationSink](https://msdn.microsoft.com/library/windows/desktop/dd372245.aspx) | Introduced in 10.0.10240. |
| [ID2D1Transform](https://msdn.microsoft.com/library/windows/desktop/hh446919.aspx) | Introduced in 10.0.10240. |
| [ID2D1TransformedGeometry](https://msdn.microsoft.com/library/windows/desktop/dd372252.aspx) | Introduced in 10.0.10240. |
| [ID2D1TransformedImageSource](https://msdn.microsoft.com/library/windows/desktop/dn952305.aspx) | Introduced in 10.0.10240. |
| [ID2D1TransformGraph](https://msdn.microsoft.com/library/windows/desktop/hh446920.aspx) | Introduced in 10.0.10240. |
| [ID2D1TransformNode](https://msdn.microsoft.com/library/windows/desktop/hh446939.aspx) | Introduced in 10.0.10240. |
| [ID2D1VertexBuffer](https://msdn.microsoft.com/library/windows/desktop/hh446949.aspx) | Introduced in 10.0.10240. |
| [ID3D10Blob](https://msdn.microsoft.com/library/windows/desktop/bb173507.aspx) | Introduced in 10.0.10240. |
| [ID3D10Multithread](https://msdn.microsoft.com/library/windows/desktop/bb173816.aspx) | Introduced in 10.0.10240. |
| [ID3D11Asynchronous](https://msdn.microsoft.com/library/windows/desktop/ff476347.aspx) | Introduced in 10.0.10240. |
| [ID3D11AuthenticatedChannel](https://msdn.microsoft.com/library/windows/desktop/hh447690.aspx) | Introduced in 10.0.10240. |
| [ID3D11BlendState](https://msdn.microsoft.com/library/windows/desktop/ff476349.aspx) | Introduced in 10.0.10240. |
| [ID3D11BlendState1](https://msdn.microsoft.com/library/windows/desktop/hh404571.aspx) | Introduced in 10.0.10240. |
| [ID3D11Buffer](https://msdn.microsoft.com/library/windows/desktop/ff476351.aspx) | Introduced in 10.0.10240. |
| [ID3D11ClassInstance](https://msdn.microsoft.com/library/windows/desktop/ff476353.aspx) | Introduced in 10.0.10240. |
| [ID3D11ClassLinkage](https://msdn.microsoft.com/library/windows/desktop/ff476358.aspx) | Introduced in 10.0.10240. |
| [ID3D11CommandList](https://msdn.microsoft.com/library/windows/desktop/ff476361.aspx) | Introduced in 10.0.10240. |
| [ID3D11ComputeShader](https://msdn.microsoft.com/library/windows/desktop/ff476363.aspx) | Introduced in 10.0.10240. |
| [ID3D11Counter](https://msdn.microsoft.com/library/windows/desktop/ff476364.aspx) | Introduced in 10.0.10240. |
| [ID3D11CryptoSession](https://msdn.microsoft.com/library/windows/desktop/hh447691.aspx) | Introduced in 10.0.10240. |
| [ID3D11Debug](https://msdn.microsoft.com/library/windows/desktop/ff476366.aspx) | Introduced in 10.0.10240. |
| [ID3D11DepthStencilState](https://msdn.microsoft.com/library/windows/desktop/ff476375.aspx) | Introduced in 10.0.10240. |
| [ID3D11DepthStencilView](https://msdn.microsoft.com/library/windows/desktop/ff476377.aspx) | Introduced in 10.0.10240. |
| [ID3D11Device](https://msdn.microsoft.com/library/windows/desktop/ff476379.aspx) | Introduced in 10.0.10240. |
| [ID3D11Device1](https://msdn.microsoft.com/library/windows/desktop/hh404575.aspx) | Introduced in 10.0.10240. |
| [ID3D11Device2](https://msdn.microsoft.com/library/windows/desktop/dn280493.aspx) | Introduced in 10.0.10240. |
| [ID3D11DeviceChild](https://msdn.microsoft.com/library/windows/desktop/ff476380.aspx) | Introduced in 10.0.10240. |
| [ID3D11DeviceContext](https://msdn.microsoft.com/library/windows/desktop/ff476385.aspx) | Introduced in 10.0.10240. |
| [ID3D11DeviceContext1](https://msdn.microsoft.com/library/windows/desktop/hh404598.aspx) | Introduced in 10.0.10240. |
| [ID3D11DeviceContext2](https://msdn.microsoft.com/library/windows/desktop/dn280498.aspx) | Introduced in 10.0.10240. |
| [ID3D11DeviceContext3](https://msdn.microsoft.com/library/windows/desktop/dn912875.aspx) | Introduced in 10.0.10240. |
| [ID3D11Device3](https://msdn.microsoft.com/library/windows/desktop/dn899218.aspx) | Introduced in 10.0.10240. |
| [ID3D11Texture2D1](https://msdn.microsoft.com/library/windows/desktop/dn899244.aspx) | Introduced in 10.0.10240. |
| [ID3D11Texture3D1](https://msdn.microsoft.com/library/windows/desktop/dn899246.aspx) | Introduced in 10.0.10240. |
| [ID3D11DomainShader](https://msdn.microsoft.com/library/windows/desktop/ff476535.aspx) | Introduced in 10.0.10240. |
| [ID3D11FunctionLinkingGraph](https://msdn.microsoft.com/library/windows/desktop/dn280535.aspx) | Introduced in 10.0.10240. |
| [ID3D11GeometryShader](https://msdn.microsoft.com/library/windows/desktop/ff476536.aspx) | Introduced in 10.0.10240. |
| [ID3D11HullShader](https://msdn.microsoft.com/library/windows/desktop/ff476537.aspx) | Introduced in 10.0.10240. |
| [ID3D11InfoQueue](https://msdn.microsoft.com/library/windows/desktop/ff476538.aspx) | Introduced in 10.0.10240. |
| [ID3D11InputLayout](https://msdn.microsoft.com/library/windows/desktop/ff476575.aspx) | Introduced in 10.0.10240. |
| [ID3D11LibraryReflection](https://msdn.microsoft.com/library/windows/desktop/dn280554.aspx) | Introduced in 10.0.10240. |
| [ID3D11Linker](https://msdn.microsoft.com/library/windows/desktop/dn280558.aspx) | Introduced in 10.0.10240. |
| [ID3D11LinkingNode](https://msdn.microsoft.com/library/windows/desktop/dn280562.aspx) | Introduced in 10.0.10240. |
| [ID3D11Module](https://msdn.microsoft.com/library/windows/desktop/dn280563.aspx) | Introduced in 10.0.10240. |
| [ID3D11ModuleInstance](https://msdn.microsoft.com/library/windows/desktop/dn280564.aspx) | Introduced in 10.0.10240. |
| [ID3D11On12Device](https://msdn.microsoft.com/library/Dn913197(v=VS.85).aspx) | Introduced in 10.0.10240. |
| [ID3D11PixelShader](https://msdn.microsoft.com/library/windows/desktop/ff476576.aspx) | Introduced in 10.0.10240. |
| [ID3D11Predicate](https://msdn.microsoft.com/library/windows/desktop/ff476577.aspx) | Introduced in 10.0.10240. |
| [ID3D11Query](https://msdn.microsoft.com/library/windows/desktop/ff476578.aspx) | Introduced in 10.0.10240. |
| [ID3D11Query1](https://msdn.microsoft.com/library/windows/desktop/dn899236.aspx) | Introduced in 10.0.10240. |
| [ID3D11RasterizerState](https://msdn.microsoft.com/library/windows/desktop/ff476580.aspx) | Introduced in 10.0.10240. |
| [ID3D11RasterizerState1](https://msdn.microsoft.com/library/windows/desktop/hh446828.aspx) | Introduced in 10.0.10240. |
| [ID3D11RasterizerState2](https://msdn.microsoft.com/library/windows/desktop/dn899238.aspx) | Introduced in 10.0.10240. |
| [ID3D11RefDefaultTrackingOptions](https://msdn.microsoft.com/library/windows/desktop/hh446832.aspx) | Introduced in 10.0.10240. |
| [ID3D11RefTrackingOptions](https://msdn.microsoft.com/library/windows/desktop/hh446836.aspx) | Introduced in 10.0.10240. |
| [ID3D11RenderTargetView](https://msdn.microsoft.com/library/windows/desktop/ff476582.aspx) | Introduced in 10.0.10240. |
| [ID3D11RenderTargetView1](https://msdn.microsoft.com/library/windows/desktop/dn899240.aspx) | Introduced in 10.0.10240. |
| [ID3D11Resource](https://msdn.microsoft.com/library/windows/desktop/ff476584.aspx) | Introduced in 10.0.10240. |
| [ID3D11SamplerState](https://msdn.microsoft.com/library/windows/desktop/ff476588.aspx) | Introduced in 10.0.10240. |
| [ID3D11ShaderReflection](https://msdn.microsoft.com/library/windows/desktop/ff476590.aspx) | Introduced in 10.0.10240. |
| [ID3D11ShaderReflectionConstantBuffer](https://msdn.microsoft.com/library/windows/desktop/ff476591.aspx) | Introduced in 10.0.10240. |
| [ID3D11ShaderReflectionType](https://msdn.microsoft.com/library/windows/desktop/ff476595.aspx) | Introduced in 10.0.10240. |
| [ID3D11ShaderReflectionVariable](https://msdn.microsoft.com/library/windows/desktop/ff476607.aspx) | Introduced in 10.0.10240. |
| [ID3D11ShaderResourceView](https://msdn.microsoft.com/library/windows/desktop/ff476628.aspx) | Introduced in 10.0.10240. |
| [ID3D11ShaderResourceView1](https://msdn.microsoft.com/library/windows/desktop/dn899242.aspx) | Introduced in 10.0.10240. |
| [ID3D11ShaderTrace](https://msdn.microsoft.com/library/windows/desktop/hh446840.aspx) | Introduced in 10.0.10240. |
| [ID3D11ShaderTraceFactory](https://msdn.microsoft.com/library/windows/desktop/hh446842.aspx) | Introduced in 10.0.10240. |
| [ID3D11Texture1D](https://msdn.microsoft.com/library/windows/desktop/ff476633.aspx) | Introduced in 10.0.10240. |
| [ID3D11Texture2D](https://msdn.microsoft.com/library/windows/desktop/ff476635.aspx) | Introduced in 10.0.10240. |
| [ID3D11Texture3D](https://msdn.microsoft.com/library/windows/desktop/ff476637.aspx) | Introduced in 10.0.10240. |
| [ID3D11TracingDevice](https://msdn.microsoft.com/library/windows/desktop/hh446868.aspx) | Introduced in 10.0.10240. |
| [ID3D11UnorderedAccessView](https://msdn.microsoft.com/library/windows/desktop/ff476639.aspx) | Introduced in 10.0.10240. |
| [ID3D11UnorderedAccessView1](https://msdn.microsoft.com/library/windows/desktop/dn899248.aspx) | Introduced in 10.0.10240. |
| [ID3D11VertexShader](https://msdn.microsoft.com/library/windows/desktop/ff476641.aspx) | Introduced in 10.0.10240. |
| [ID3D11VideoContext](https://msdn.microsoft.com/library/windows/desktop/hh447703.aspx) | Introduced in 10.0.10240. |
| [ID3D11VideoContext1](https://msdn.microsoft.com/library/windows/desktop/dn894126.aspx) | Introduced in 10.0.10240. |
| [ID3D11VideoDecoder](https://msdn.microsoft.com/library/windows/desktop/hh447766.aspx) | Introduced in 10.0.10240. |
| [ID3D11VideoDecoderOutputView](https://msdn.microsoft.com/library/windows/desktop/hh447767.aspx) | Introduced in 10.0.10240. |
| [ID3D11VideoDevice](https://msdn.microsoft.com/library/windows/desktop/hh447781.aspx) | Introduced in 10.0.10240. |
| [ID3D11VideoDevice1](https://msdn.microsoft.com/library/windows/desktop/dn894141.aspx) | Introduced in 10.0.10240. |
| [ID3D11VideoProcessor](https://msdn.microsoft.com/library/windows/desktop/hh447799.aspx) | Introduced in 10.0.10240. |
| [ID3D11VideoProcessorEnumerator](https://msdn.microsoft.com/library/windows/desktop/hh447800.aspx) | Introduced in 10.0.10240. |
| [ID3D11VideoProcessorEnumerator1](https://msdn.microsoft.com/library/windows/desktop/dn894146.aspx) | Introduced in 10.0.10240. |
| [ID3D11VideoProcessorInputView](https://msdn.microsoft.com/library/windows/desktop/hh447807.aspx) | Introduced in 10.0.10240. |
| [ID3D11VideoProcessorOutputView](https://msdn.microsoft.com/library/windows/desktop/hh447809.aspx) | Introduced in 10.0.10240. |
| [ID3D11View](https://msdn.microsoft.com/library/windows/desktop/ff476642.aspx) | Introduced in 10.0.10240. |
| [ID3D12CommandAllocator](https://msdn.microsoft.com/library/Dn770463(v=VS.85).aspx) | Introduced in 10.0.10240. |
| [ID3D12CommandList](https://msdn.microsoft.com/library/Dn770465(v=VS.85).aspx) | Introduced in 10.0.10240. |
| [ID3D12CommandQueue](https://msdn.microsoft.com/library/Dn788627(v=VS.85).aspx) | Introduced in 10.0.10240. |
| [ID3D12CommandSignature](https://msdn.microsoft.com/library/Dn891446(v=VS.85).aspx) | Introduced in 10.0.10240. |
| [ID3D12Debug](https://msdn.microsoft.com/library/Dn950153(v=VS.85).aspx) | Introduced in 10.0.10240. |
| [ID3D12DebugCommandList](https://msdn.microsoft.com/library/Dn950154(v=VS.85).aspx) | Introduced in 10.0.10240. |
| [ID3D12DebugCommandQueue](https://msdn.microsoft.com/library/Dn950158(v=VS.85).aspx) | Introduced in 10.0.10240. |
| [ID3D12DebugDevice](https://msdn.microsoft.com/library/Dn986873(v=VS.85).aspx) | Introduced in 10.0.10240. |
| [ID3D12DescriptorHeap](https://msdn.microsoft.com/library/Dn788648(v=VS.85).aspx) | Introduced in 10.0.10240. |
| [ID3D12Device](https://msdn.microsoft.com/library/Dn788650(v=VS.85).aspx) | Introduced in 10.0.10240. |
| [ID3D12DeviceChild](https://msdn.microsoft.com/library/Dn788651(v=VS.85).aspx) | Introduced in 10.0.10240. |
| [ID3D12Fence](https://msdn.microsoft.com/library/Dn899188(v=VS.85).aspx) | Introduced in 10.0.10240. |
| [ID3D12GraphicsCommandList](https://msdn.microsoft.com/library/Dn903537(v=VS.85).aspx) | Introduced in 10.0.10240. |
| [ID3D12Heap](https://msdn.microsoft.com/library/Dn788687(v=VS.85).aspx) | Introduced in 10.0.10240. |
| [ID3D12InfoQueue](https://msdn.microsoft.com/library/Dn950163(v=VS.85).aspx) | Introduced in 10.0.10240. |
| [ID3D12LibraryReflection](https://msdn.microsoft.com/library/Dn933676(v=VS.85).aspx) | Introduced in 10.0.10240. |
| [ID3D12Object](https://msdn.microsoft.com/library/Dn788699(v=VS.85).aspx) | Introduced in 10.0.10240. |
| [ID3D12Pageable](https://msdn.microsoft.com/library/Dn788704(v=VS.85).aspx) | Introduced in 10.0.10240. |
| [ID3D12PipelineState](https://msdn.microsoft.com/library/Dn788705(v=VS.85).aspx) | Introduced in 10.0.10240. |
| [ID3D12QueryHeap](https://msdn.microsoft.com/library/Dn891447(v=VS.85).aspx) | Introduced in 10.0.10240. |
| [ID3D12Resource](https://msdn.microsoft.com/library/Dn788709(v=VS.85).aspx) | Introduced in 10.0.10240. |
| [ID3D12RootSignature](https://msdn.microsoft.com/library/Dn788714(v=VS.85).aspx) | Introduced in 10.0.10240. |
| [ID3D12RootSignatureDeserializer](https://msdn.microsoft.com/library/Dn899192(v=VS.85).aspx) | Introduced in 10.0.10240. |
| [ID3D12ShaderReflection](https://msdn.microsoft.com/library/Dn933679(v=VS.85).aspx) | Introduced in 10.0.10240. |
| [ID3DDeviceContextState](https://msdn.microsoft.com/library/windows/desktop/hh446878.aspx) | Introduced in 10.0.10240. |
| [ID3DUserDefinedAnnotation](https://msdn.microsoft.com/library/windows/desktop/hh446881.aspx) | Introduced in 10.0.10240. |
| [IDeviceIoControl](https://msdn.microsoft.com/library/windows/desktop/hh404258.aspx) | Introduced in 10.0.10240. |
| [IDeviceRequestCompletionCallback](https://msdn.microsoft.com/library/windows/desktop/hh404262.aspx) | Introduced in 10.0.10240. |
| IDirect3DDxgiInterfaceAccess | Introduced in 10.0.10240. |
| [IDirectWriterLock](https://msdn.microsoft.com/library/windows/desktop/aa379158.aspx) | Introduced in 10.0.10240. |
| [IDispatch](https://msdn.microsoft.com/library/windows/desktop/ms221608.aspx) | Introduced in 10.0.10240. |
| [IDockProvider](https://msdn.microsoft.com/library/windows/desktop/ee671239.aspx) | Introduced in 10.0.10240. |
| [IDragProvider](https://msdn.microsoft.com/library/windows/desktop/hh707338.aspx) | Introduced in 10.0.10240. |
| [IDropTargetProvider](https://msdn.microsoft.com/library/windows/desktop/hh707345.aspx) | Introduced in 10.0.10240. |
| [IDvdControl2](https://msdn.microsoft.com/library/windows/desktop/dd389895.aspx) | Introduced in 10.0.10240. |
| [IDvdInfo2](https://msdn.microsoft.com/library/windows/desktop/dd376432.aspx) | Introduced in 10.0.10240. |
| [IDWriteBitmapRenderTarget](https://msdn.microsoft.com/library/windows/desktop/dd368165.aspx) | Introduced in 10.0.10240. |
| [IDWriteBitmapRenderTarget1](https://msdn.microsoft.com/library/windows/desktop/hh780398.aspx) | Introduced in 10.0.10240. |
| [IDWriteColorGlyphRunEnumerator](https://msdn.microsoft.com/library/windows/desktop/dn280445.aspx) | Introduced in 10.0.10240. |
| [IDWriteFactory](https://msdn.microsoft.com/library/windows/desktop/dd368183.aspx) | Introduced in 10.0.10240. |
| [IDWriteFactory1](https://msdn.microsoft.com/library/windows/desktop/hh780401.aspx) | Introduced in 10.0.10240. |
| [IDWriteFactory2](https://msdn.microsoft.com/library/windows/desktop/dn280448.aspx) | Introduced in 10.0.10240. |
| [IDWriteFactory3](https://msdn.microsoft.com/library/windows/desktop/dn890753.aspx) | Introduced in 10.0.10240. |
| [IDWriteFont](https://msdn.microsoft.com/library/windows/desktop/dd368213.aspx) | Introduced in 10.0.10240. |
| [IDWriteFont1](https://msdn.microsoft.com/library/windows/desktop/hh780404.aspx) | Introduced in 10.0.10240. |
| [IDWriteFont2](https://msdn.microsoft.com/library/windows/desktop/dn280452.aspx) | Introduced in 10.0.10240. |
| [IDWriteFont3](https://msdn.microsoft.com/library/windows/desktop/dn890766.aspx) | Introduced in 10.0.10240. |
| [IDWriteFontCollection](https://msdn.microsoft.com/library/windows/desktop/dd368214.aspx) | Introduced in 10.0.10240. |
| [IDWriteFontCollection1](https://msdn.microsoft.com/library/windows/desktop/dn933224.aspx) | Introduced in 10.0.10240. |
| [IDWriteFontCollectionLoader](https://msdn.microsoft.com/library/windows/desktop/dd368215.aspx) | Introduced in 10.0.10240. |
| [IDWriteFontDownloadListener](https://msdn.microsoft.com/library/windows/desktop/dn890775.aspx) | Introduced in 10.0.10240. |
| [IDWriteFontDownloadQueue](https://msdn.microsoft.com/library/windows/desktop/dn890778.aspx) | Introduced in 10.0.10240. |
| [IDWriteFontFace](https://msdn.microsoft.com/library/windows/desktop/dd370983.aspx) | Introduced in 10.0.10240. |
| [IDWriteFontFace1](https://msdn.microsoft.com/library/windows/desktop/hh780409.aspx) | Introduced in 10.0.10240. |
| [IDWriteFontFace2](https://msdn.microsoft.com/library/windows/desktop/dn280454.aspx) | Introduced in 10.0.10240. |
| [IDWriteFontFace3](https://msdn.microsoft.com/library/windows/desktop/dn894561.aspx) | Introduced in 10.0.10240. |
| [IDWriteFontFaceReference](https://msdn.microsoft.com/library/windows/desktop/dn894576.aspx) | Introduced in 10.0.10240. |
| [IDWriteFontFallback](https://msdn.microsoft.com/library/windows/desktop/dn280474.aspx) | Introduced in 10.0.10240. |
| [IDWriteFontFallbackBuilder](https://msdn.microsoft.com/library/windows/desktop/dn280476.aspx) | Introduced in 10.0.10240. |
| [IDWriteFontFamily](https://msdn.microsoft.com/library/windows/desktop/dd371042.aspx) | Introduced in 10.0.10240. |
| [IDWriteFontFamily1](https://msdn.microsoft.com/library/windows/desktop/dn894590.aspx) | Introduced in 10.0.10240. |
| [IDWriteFontFile](https://msdn.microsoft.com/library/windows/desktop/dd371060.aspx) | Introduced in 10.0.10240. |
| [IDWriteFontFileEnumerator](https://msdn.microsoft.com/library/windows/desktop/dd371063.aspx) | Introduced in 10.0.10240. |
| [IDWriteFontFileLoader](https://msdn.microsoft.com/library/windows/desktop/dd371075.aspx) | Introduced in 10.0.10240. |
| [IDWriteFontFileStream](https://msdn.microsoft.com/library/windows/desktop/dd371081.aspx) | Introduced in 10.0.10240. |
| [IDWriteFontList](https://msdn.microsoft.com/library/windows/desktop/dd371120.aspx) | Introduced in 10.0.10240. |
| [IDWriteFontList1](https://msdn.microsoft.com/library/windows/desktop/dn894594.aspx) | Introduced in 10.0.10240. |
| [IDWriteFontSet](https://msdn.microsoft.com/library/windows/desktop/dn933235.aspx) | Introduced in 10.0.10240. |
| [IDWriteFontSetBuilder](https://msdn.microsoft.com/library/windows/desktop/dn933236.aspx) | Introduced in 10.0.10240. |
| [IDWriteGdiInterop](https://msdn.microsoft.com/library/windows/desktop/dd371172.aspx) | Introduced in 10.0.10240. |
| [IDWriteGdiInterop1](https://msdn.microsoft.com/library/windows/desktop/dn958415.aspx) | Introduced in 10.0.10240. |
| [IDWriteGlyphRunAnalysis](https://msdn.microsoft.com/library/windows/desktop/dd371188.aspx) | Introduced in 10.0.10240. |
| [IDWriteInlineObject](https://msdn.microsoft.com/library/windows/desktop/dd371221.aspx) | Introduced in 10.0.10240. |
| [IDWriteLocalFontFileLoader](https://msdn.microsoft.com/library/windows/desktop/dd371238.aspx) | Introduced in 10.0.10240. |
| [IDWriteLocalizedStrings](https://msdn.microsoft.com/library/windows/desktop/dd371250.aspx) | Introduced in 10.0.10240. |
| [IDWriteNumberSubstitution](https://msdn.microsoft.com/library/windows/desktop/dd371271.aspx) | Introduced in 10.0.10240. |
| [IDWritePixelSnapping](https://msdn.microsoft.com/library/windows/desktop/dd371274.aspx) | Introduced in 10.0.10240. |
| [IDWriteRenderingParams](https://msdn.microsoft.com/library/windows/desktop/dd371285.aspx) | Introduced in 10.0.10240. |
| [IDWriteRenderingParams1](https://msdn.microsoft.com/library/windows/desktop/hh780422.aspx) | Introduced in 10.0.10240. |
| [IDWriteRenderingParams2](https://msdn.microsoft.com/library/windows/desktop/dn900387.aspx) | Introduced in 10.0.10240. |
| [IDWriteRenderingParams3](https://msdn.microsoft.com/library/windows/desktop/dn900389.aspx) | Introduced in 10.0.10240. |
| [IDWriteStringList](https://msdn.microsoft.com/library/windows/desktop/dn958421.aspx) | Introduced in 10.0.10240. |
| [IDWriteTextAnalysisSink](https://msdn.microsoft.com/library/windows/desktop/dd371303.aspx) | Introduced in 10.0.10240. |
| [IDWriteTextAnalysisSink1](https://msdn.microsoft.com/library/windows/desktop/hh780424.aspx) | Introduced in 10.0.10240. |
| [IDWriteTextAnalysisSource](https://msdn.microsoft.com/library/windows/desktop/dd371318.aspx) | Introduced in 10.0.10240. |
| [IDWriteTextAnalysisSource1](https://msdn.microsoft.com/library/windows/desktop/hh780426.aspx) | Introduced in 10.0.10240. |
| [IDWriteTextAnalyzer](https://msdn.microsoft.com/library/windows/desktop/dd316607.aspx) | Introduced in 10.0.10240. |
| [IDWriteTextAnalyzer1](https://msdn.microsoft.com/library/windows/desktop/hh780428.aspx) | Introduced in 10.0.10240. |
| [IDWriteTextAnalyzer2](https://msdn.microsoft.com/library/windows/desktop/dn280483.aspx) | Introduced in 10.0.10240. |
| [IDWriteTextFormat](https://msdn.microsoft.com/library/windows/desktop/dd316628.aspx) | Introduced in 10.0.10240. |
| [IDWriteTextFormat1](https://msdn.microsoft.com/library/windows/desktop/dn280485.aspx) | Introduced in 10.0.10240. |
| [IDWriteTextFormat2](https://msdn.microsoft.com/library/windows/desktop/mt574121.aspx) | Introduced in 10.0.10240. |
| [IDWriteTextLayout](https://msdn.microsoft.com/library/windows/desktop/dd316718.aspx) | Introduced in 10.0.10240. |
| [IDWriteTextLayout1](https://msdn.microsoft.com/library/windows/desktop/hh780438.aspx) | Introduced in 10.0.10240. |
| [IDWriteTextLayout2](https://msdn.microsoft.com/library/windows/desktop/dn280491.aspx) | Introduced in 10.0.10240. |
| [IDWriteTextLayout3](https://msdn.microsoft.com/library/windows/desktop/dn900405.aspx) | Introduced in 10.0.10240. |
| [IDWriteTextRenderer](https://msdn.microsoft.com/library/windows/desktop/dd371523.aspx) | Introduced in 10.0.10240. |
| [IDWriteTextRenderer1](https://msdn.microsoft.com/library/windows/desktop/dn280513.aspx) | Introduced in 10.0.10240. |
| [IDWriteTypography](https://msdn.microsoft.com/library/windows/desktop/dd371541.aspx) | Introduced in 10.0.10240. |
| [IDXGIAdapter](https://msdn.microsoft.com/library/windows/desktop/bb174523.aspx) | Introduced in 10.0.10240. |
| [IDXGIAdapter1](https://msdn.microsoft.com/library/windows/desktop/ff471329.aspx) | Introduced in 10.0.10240. |
| [IDXGIAdapter2](https://msdn.microsoft.com/library/windows/desktop/hh404537.aspx) | Introduced in 10.0.10240. |
| [IDXGIAdapter3](https://msdn.microsoft.com/library/windows/desktop/dn933221.aspx) | Introduced in 10.0.10240. |
| [IDXGIDebug](https://msdn.microsoft.com/library/windows/desktop/hh780351.aspx) | Introduced in 10.0.10240. |
| [IDXGIDebug1](https://msdn.microsoft.com/library/windows/desktop/dn457938.aspx) | Introduced in 10.0.10240. |
| [IDXGIDevice](https://msdn.microsoft.com/library/windows/desktop/bb174527.aspx) | Introduced in 10.0.10240. |
| [IDXGIDevice1](https://msdn.microsoft.com/library/windows/desktop/ff471331.aspx) | Introduced in 10.0.10240. |
| [IDXGIDevice2](https://msdn.microsoft.com/library/windows/desktop/hh404543.aspx) | Introduced in 10.0.10240. |
| [IDXGIDevice3](https://msdn.microsoft.com/library/windows/desktop/dn280345.aspx) | Introduced in 10.0.10240. |
| [IDXGIDeviceSubObject](https://msdn.microsoft.com/library/windows/desktop/bb174528.aspx) | Introduced in 10.0.10240. |
| [IDXGIFactory](https://msdn.microsoft.com/library/windows/desktop/bb174535.aspx) | Introduced in 10.0.10240. |
| [IDXGIFactory1](https://msdn.microsoft.com/library/windows/desktop/ff471335.aspx) | Introduced in 10.0.10240. |
| [IDXGIFactory2](https://msdn.microsoft.com/library/windows/desktop/hh404556.aspx) | Introduced in 10.0.10240. |
| [IDXGIFactory3](https://msdn.microsoft.com/library/windows/desktop/dn457942.aspx) | Introduced in 10.0.10240. |
| [IDXGIFactory4](https://msdn.microsoft.com/library/windows/desktop/mt427785.aspx) | Introduced in 10.0.10240. |
| [IDXGIInfoQueue](https://msdn.microsoft.com/library/windows/desktop/hh780355.aspx) | Introduced in 10.0.10240. |
| [IDXGIKeyedMutex](https://msdn.microsoft.com/library/windows/desktop/ff471338.aspx) | Introduced in 10.0.10240. |
| [IDXGIObject](https://msdn.microsoft.com/library/windows/desktop/bb174541.aspx) | Introduced in 10.0.10240. |
| [IDXGIOutput](https://msdn.microsoft.com/library/windows/desktop/bb174546.aspx) | Introduced in 10.0.10240. |
| [IDXGIOutput1](https://msdn.microsoft.com/library/windows/desktop/hh404597.aspx) | Introduced in 10.0.10240. |
| [IDXGIOutput2](https://msdn.microsoft.com/library/windows/desktop/dn280410.aspx) | Introduced in 10.0.10240. |
| [IDXGIOutput3](https://msdn.microsoft.com/library/windows/desktop/dn903669.aspx) | Introduced in 10.0.10240. |
| [IDXGIOutput4](https://msdn.microsoft.com/library/windows/desktop/dn903671.aspx) | Introduced in 10.0.10240. |
| [IDXGIResource](https://msdn.microsoft.com/library/windows/desktop/bb174560.aspx) | Introduced in 10.0.10240. |
| [IDXGIResource1](https://msdn.microsoft.com/library/windows/desktop/hh404625.aspx) | Introduced in 10.0.10240. |
| [IDXGISurface](https://msdn.microsoft.com/library/windows/desktop/bb174565.aspx) | Introduced in 10.0.10240. |
| [IDXGISurface1](https://msdn.microsoft.com/library/windows/desktop/ff471343.aspx) | Introduced in 10.0.10240. |
| [IDXGISurface2](https://msdn.microsoft.com/library/windows/desktop/hh404628.aspx) | Introduced in 10.0.10240. |
| [IDXGISwapChain](https://msdn.microsoft.com/library/windows/desktop/bb174569.aspx) | Introduced in 10.0.10240. |
| [IDXGISwapChain1](https://msdn.microsoft.com/library/windows/desktop/hh404631.aspx) | Introduced in 10.0.10240. |
| [IDXGISwapChain2](https://msdn.microsoft.com/library/windows/desktop/dn280420.aspx) | Introduced in 10.0.10240. |
| [IDXGISwapChain3](https://msdn.microsoft.com/library/windows/desktop/dn903673.aspx) | Introduced in 10.0.10240. |
| [IEditionUpgradeHelper](https://msdn.microsoft.com/library/Mt459283(v=VS.85).aspx) | Introduced in 10.0.10240. |
| [IEnumCodePage](https://msdn.microsoft.com/library/windows/desktop/aa741101.aspx) | Introduced in 10.0.10240. |
| [IEnumConnectionPoints](https://msdn.microsoft.com/library/windows/desktop/ms688265.aspx) | Introduced in 10.0.10240. |
| [IEnumConnections](https://msdn.microsoft.com/library/windows/desktop/ms682237.aspx) | Introduced in 10.0.10240. |
| [IEnumGUID](https://msdn.microsoft.com/library/windows/desktop/ms682393.aspx) | Introduced in 10.0.10240. |
| [IEnumITfCompositionView](https://msdn.microsoft.com/library/windows/desktop/ms538115.aspx) | Introduced in 10.0.10240. |
| [IEnumMoniker](https://msdn.microsoft.com/library/windows/desktop/ms692852.aspx) | Introduced in 10.0.10240. |
| [IEnumPortableDeviceObjectIDs](https://msdn.microsoft.com/library/windows/desktop/dd319350.aspx) | Introduced in 10.0.10240. |
| [IEnumRfc1766](https://msdn.microsoft.com/library/windows/desktop/aa741095.aspx) | Introduced in 10.0.10240. |
| [IEnumScript](https://msdn.microsoft.com/library/windows/desktop/aa741082.aspx) | Introduced in 10.0.10240. |
| [IEnumSpellingError](https://msdn.microsoft.com/library/windows/desktop/hh869751.aspx) | Introduced in 10.0.10240. |
| [IEnumSTATDATA](https://msdn.microsoft.com/library/windows/desktop/ms688589.aspx) | Introduced in 10.0.10240. |
| [IEnumSTATPROPSETSTG](https://msdn.microsoft.com/library/windows/desktop/aa379184.aspx) | Introduced in 10.0.10240. |
| [IEnumSTATPROPSTG](https://msdn.microsoft.com/library/windows/desktop/aa379210.aspx) | Introduced in 10.0.10240. |
| [IEnumSTATSTG](https://msdn.microsoft.com/library/windows/desktop/aa379217.aspx) | Introduced in 10.0.10240. |
| [IEnumString](https://msdn.microsoft.com/library/windows/desktop/ms687257.aspx) | Introduced in 10.0.10240. |
| [IEnumTfCandidates](https://msdn.microsoft.com/library/windows/desktop/ms538125.aspx) | Introduced in 10.0.10240. |
| [IEnumTfContexts](https://msdn.microsoft.com/library/windows/desktop/ms538135.aspx) | Introduced in 10.0.10240. |
| [IEnumTfContextViews](https://msdn.microsoft.com/library/windows/desktop/ms538144.aspx) | Introduced in 10.0.10240. |
| [IEnumTfDisplayAttributeInfo](https://msdn.microsoft.com/library/windows/desktop/ms538154.aspx) | Introduced in 10.0.10240. |
| [IEnumTfDocumentMgrs](https://msdn.microsoft.com/library/windows/desktop/ms538164.aspx) | Introduced in 10.0.10240. |
| [IEnumTfFunctionProviders](https://msdn.microsoft.com/library/windows/desktop/ms538172.aspx) | Introduced in 10.0.10240. |
| [IEnumTfInputProcessorProfiles](https://msdn.microsoft.com/library/windows/desktop/aa380591.aspx) | Introduced in 10.0.10240. |
| [IEnumTfProperties](https://msdn.microsoft.com/library/windows/desktop/ms538218.aspx) | Introduced in 10.0.10240. |
| [IEnumTfPropertyValue](https://msdn.microsoft.com/library/windows/desktop/ms538230.aspx) | Introduced in 10.0.10240. |
| [IEnumTfRanges](https://msdn.microsoft.com/library/windows/desktop/ms538241.aspx) | Introduced in 10.0.10240. |
| [IEnumTfUIElements](https://msdn.microsoft.com/library/windows/desktop/aa380866.aspx) | Introduced in 10.0.10240. |
| [IEnumUnknown](https://msdn.microsoft.com/library/windows/desktop/ms683764.aspx) | Introduced in 10.0.10240. |
| [IEnumVARIANT](https://msdn.microsoft.com/library/windows/desktop/ms221053.aspx) | Introduced in 10.0.10240. |
| [IExpandCollapseProvider](https://msdn.microsoft.com/library/windows/desktop/ee671242.aspx) | Introduced in 10.0.10240. |
| [IFillLockBytes](https://msdn.microsoft.com/library/windows/desktop/aa379224.aspx) | Introduced in 10.0.10240. |
| [IFindReferenceTargetsCallback](https://msdn.microsoft.com/library/windows/desktop/jj542493.aspx) | Introduced in 10.0.10240. |
| [IGlobalInterfaceTable](https://msdn.microsoft.com/library/windows/desktop/ms678517.aspx) | Introduced in 10.0.10240. |
| [IGlobalOptions](https://msdn.microsoft.com/library/windows/desktop/aa344211.aspx) | Introduced in 10.0.10240. |
| [IGridItemProvider](https://msdn.microsoft.com/library/windows/desktop/ee671246.aspx) | Introduced in 10.0.10240. |
| [IGridProvider](https://msdn.microsoft.com/library/windows/desktop/ee671252.aspx) | Introduced in 10.0.10240. |
| [IInkD2DRenderer](https://msdn.microsoft.com/library/Mt147263(v=VS.85).aspx) | Introduced in 10.0.10240. |
| [IInspectable](https://msdn.microsoft.com/library/windows/desktop/br205821.aspx) | Introduced in 10.0.10240. |
| [IInvokeProvider](https://msdn.microsoft.com/library/windows/desktop/ee671256.aspx) | Introduced in 10.0.10240. |
| [IItemContainerProvider](https://msdn.microsoft.com/library/windows/desktop/ee671258.aspx) | Introduced in 10.0.10240. |
| [ILanguageExceptionErrorInfo](https://msdn.microsoft.com/library/windows/desktop/dn302120.aspx) | Introduced in 10.0.10240. |
| [ILayoutStorage](https://msdn.microsoft.com/library/windows/desktop/aa379232.aspx) | Introduced in 10.0.10240. |
| [ILegacyIAccessibleProvider](https://msdn.microsoft.com/library/windows/desktop/ee671260.aspx) | Introduced in 10.0.10240. |
| [ILockBytes](https://msdn.microsoft.com/library/windows/desktop/aa379238.aspx) | Introduced in 10.0.10240. |
| [IMarshal](https://msdn.microsoft.com/library/windows/desktop/ms688712.aspx) | Introduced in 10.0.10240. |
| [IMbnConnection](https://msdn.microsoft.com/library/windows/desktop/dd430368.aspx) | Introduced in 10.0.10240. |
| [IMbnConnectionEvents](https://msdn.microsoft.com/library/windows/desktop/dd430375.aspx) | Introduced in 10.0.10240. |
| [IMbnConnectionManager](https://msdn.microsoft.com/library/windows/desktop/dd430380.aspx) | Introduced in 10.0.10240. |
| [IMbnConnectionManagerEvents](https://msdn.microsoft.com/library/windows/desktop/dd430381.aspx) | Introduced in 10.0.10240. |
| [IMbnDeviceService](https://msdn.microsoft.com/library/windows/desktop/hh780509.aspx) | Introduced in 10.0.10240. |
| [IMbnDeviceServicesContext](https://msdn.microsoft.com/library/windows/desktop/hh780510.aspx) | Introduced in 10.0.10240. |
| [IMbnDeviceServicesEvents](https://msdn.microsoft.com/library/windows/desktop/hh780515.aspx) | Introduced in 10.0.10240. |
| [IMbnDeviceServicesManager](https://msdn.microsoft.com/library/windows/desktop/hh780527.aspx) | Introduced in 10.0.10240. |
| [IMbnInterface](https://msdn.microsoft.com/library/windows/desktop/dd430406.aspx) | Introduced in 10.0.10240. |
| [IMbnInterfaceEvents](https://msdn.microsoft.com/library/windows/desktop/dd430407.aspx) | Introduced in 10.0.10240. |
| [IMbnInterfaceManager](https://msdn.microsoft.com/library/windows/desktop/dd430416.aspx) | Introduced in 10.0.10240. |
| [IMbnInterfaceManagerEvents](https://msdn.microsoft.com/library/windows/desktop/dd430417.aspx) | Introduced in 10.0.10240. |
| [IMbnPin](https://msdn.microsoft.com/library/windows/desktop/dd323109.aspx) | Introduced in 10.0.10240. |
| [IMbnPinEvents](https://msdn.microsoft.com/library/windows/desktop/dd323110.aspx) | Introduced in 10.0.10240. |
| [IMbnPinManager](https://msdn.microsoft.com/library/windows/desktop/dd323117.aspx) | Introduced in 10.0.10240. |
| [IMbnPinManagerEvents](https://msdn.microsoft.com/library/windows/desktop/dd323118.aspx) | Introduced in 10.0.10240. |
| [IMbnRegistration](https://msdn.microsoft.com/library/windows/desktop/dd323142.aspx) | Introduced in 10.0.10240. |
| [IMbnRegistrationEvents](https://msdn.microsoft.com/library/windows/desktop/dd323143.aspx) | Introduced in 10.0.10240. |
| [IMetaDataAssemblyImport](https://msdn.microsoft.com/library/windows/desktop/hh870550.aspx) | Introduced in 10.0.10240. |
| [IMetaDataDispenser](https://msdn.microsoft.com/library/windows/desktop/hh870566.aspx) | Introduced in 10.0.10240. |
| [IMetaDataDispenserEx](https://msdn.microsoft.com/library/windows/desktop/hh870567.aspx) | Introduced in 10.0.10240. |
| [IMetaDataImport](https://msdn.microsoft.com/library/windows/desktop/hh870577.aspx) | Introduced in 10.0.10240. |
| [IMetaDataImport2](https://msdn.microsoft.com/library/windows/desktop/hh870578.aspx) | Introduced in 10.0.10240. |
| [IMetaDataTables](https://msdn.microsoft.com/library/windows/desktop/hh870643.aspx) | Introduced in 10.0.10240. |
| [IMetaDataTables2](https://msdn.microsoft.com/library/windows/desktop/hh870644.aspx) | Introduced in 10.0.10240. |
| [IMF2DBuffer](https://msdn.microsoft.com/library/windows/desktop/ms699894.aspx) | Introduced in 10.0.10240. |
| [IMF2DBuffer2](https://msdn.microsoft.com/library/windows/desktop/hh447827.aspx) | Introduced in 10.0.10240. |
| [IMFActivate](https://msdn.microsoft.com/library/windows/desktop/ms703039.aspx) | Introduced in 10.0.10240. |
| [IMFAsyncCallback](https://msdn.microsoft.com/library/windows/desktop/ms699856.aspx) | Introduced in 10.0.10240. |
| [IMFAsyncResult](https://msdn.microsoft.com/library/windows/desktop/ms700196.aspx) | Introduced in 10.0.10240. |
| [IMFAttributes](https://msdn.microsoft.com/library/windows/desktop/ms704598.aspx) | Introduced in 10.0.10240. |
| [IMFByteStream](https://msdn.microsoft.com/library/windows/desktop/ms698720.aspx) | Introduced in 10.0.10240. |
| [IMFByteStreamBuffering](https://msdn.microsoft.com/library/windows/desktop/aa372548.aspx) | Introduced in 10.0.10240. |
| [IMFByteStreamCacheControl](https://msdn.microsoft.com/library/windows/desktop/dd368785.aspx) | Introduced in 10.0.10240. |
| [IMFByteStreamCacheControl2](https://msdn.microsoft.com/library/windows/desktop/hh447830.aspx) | Introduced in 10.0.10240. |
| [IMFByteStreamTimeSeek](https://msdn.microsoft.com/library/windows/desktop/hh447836.aspx) | Introduced in 10.0.10240. |
| [IMFClock](https://msdn.microsoft.com/library/windows/desktop/ms696248.aspx) | Introduced in 10.0.10240. |
| [IMFClockStateSink](https://msdn.microsoft.com/library/windows/desktop/ms701593.aspx) | Introduced in 10.0.10240. |
| [IMFCollection](https://msdn.microsoft.com/library/windows/desktop/ms705661.aspx) | Introduced in 10.0.10240. |
| [IMFContentDecryptorContext](https://msdn.microsoft.com/library/windows/desktop/mt219182.aspx) | Introduced in 10.0.10240. |
| [IMFContentProtectionDevice](https://msdn.microsoft.com/library/windows/desktop/mt219184.aspx) | Introduced in 10.0.10240. |
| [IMFDXGIBuffer](https://msdn.microsoft.com/library/windows/desktop/hh447901.aspx) | Introduced in 10.0.10240. |
| [IMFDXGIDeviceManager](https://msdn.microsoft.com/library/windows/desktop/hh447906.aspx) | Introduced in 10.0.10240. |
| [IMFDXGIDeviceManagerSource](https://msdn.microsoft.com/library/windows/desktop/dn280687.aspx) | Introduced in 10.0.10240. |
| [IMFGetService](https://msdn.microsoft.com/library/windows/desktop/ms694261.aspx) | Introduced in 10.0.10240. |
| [IMFInputTrustAuthority](https://msdn.microsoft.com/library/windows/desktop/ms697500.aspx) | Introduced in 10.0.10240. |
| [IMFMediaBuffer](https://msdn.microsoft.com/library/windows/desktop/ms696261.aspx) | Introduced in 10.0.10240. |
| [IMFMediaEngine](https://msdn.microsoft.com/library/windows/desktop/hh447918.aspx) | Introduced in 10.0.10240. |
| [IMFMediaEngineClassFactory](https://msdn.microsoft.com/library/windows/desktop/hh447919.aspx) | Introduced in 10.0.10240. |
| [IMFMediaEngineEx](https://msdn.microsoft.com/library/windows/desktop/hh447923.aspx) | Introduced in 10.0.10240. |
| [IMFMediaEngineExtension](https://msdn.microsoft.com/library/windows/desktop/hh447924.aspx) | Introduced in 10.0.10240. |
| [IMFMediaEngineNotify](https://msdn.microsoft.com/library/windows/desktop/hh447962.aspx) | Introduced in 10.0.10240. |
| [IMFMediaEngineProtectedContent](https://msdn.microsoft.com/library/windows/desktop/hh447964.aspx) | Introduced in 10.0.10240. |
| [IMFMediaEngineSrcElements](https://msdn.microsoft.com/library/windows/desktop/hh447971.aspx) | Introduced in 10.0.10240. |
| [IMFMediaError](https://msdn.microsoft.com/library/windows/desktop/hh448022.aspx) | Introduced in 10.0.10240. |
| [IMFMediaEvent](https://msdn.microsoft.com/library/windows/desktop/ms702249.aspx) | Introduced in 10.0.10240. |
| [IMFMediaEventGenerator](https://msdn.microsoft.com/library/windows/desktop/ms701755.aspx) | Introduced in 10.0.10240. |
| [IMFMediaEventQueue](https://msdn.microsoft.com/library/windows/desktop/ms704617.aspx) | Introduced in 10.0.10240. |
| [IMFMediaSink](https://msdn.microsoft.com/library/windows/desktop/ms694262.aspx) | Introduced in 10.0.10240. |
| [IMFMediaSinkPreroll](https://msdn.microsoft.com/library/windows/desktop/ms699832.aspx) | Introduced in 10.0.10240. |
| [IMFMediaSource](https://msdn.microsoft.com/library/windows/desktop/ms700189.aspx) | Introduced in 10.0.10240. |
| [IMFMediaSourceEx](https://msdn.microsoft.com/library/windows/desktop/hh448029.aspx) | Introduced in 10.0.10240. |
| [IMFMediaStream](https://msdn.microsoft.com/library/windows/desktop/ms697561.aspx) | Introduced in 10.0.10240. |
| [IMFMediaStreamSourceSampleRequest](https://msdn.microsoft.com/library/windows/desktop/dn280741.aspx) | Introduced in 10.0.10240. |
| [IMFMediaTimeRange](https://msdn.microsoft.com/library/windows/desktop/hh448033.aspx) | Introduced in 10.0.10240. |
| [IMFMediaType](https://msdn.microsoft.com/library/windows/desktop/ms704850.aspx) | Introduced in 10.0.10240. |
| [IMFMediaTypeHandler](https://msdn.microsoft.com/library/windows/desktop/ms697311.aspx) | Introduced in 10.0.10240. |
| [IMFMetadata](https://msdn.microsoft.com/library/windows/desktop/ms696970.aspx) | Introduced in 10.0.10240. |
| [IMFMetadataProvider](https://msdn.microsoft.com/library/windows/desktop/ms705606.aspx) | Introduced in 10.0.10240. |
| [IMFOutputPolicy](https://msdn.microsoft.com/library/windows/desktop/ms698985.aspx) | Introduced in 10.0.10240. |
| [IMFOutputSchema](https://msdn.microsoft.com/library/windows/desktop/ms703800.aspx) | Introduced in 10.0.10240. |
| [IMFOutputTrustAuthority](https://msdn.microsoft.com/library/windows/desktop/ms695254.aspx) | Introduced in 10.0.10240. |
| [IMFPMPClientApp](https://msdn.microsoft.com/library/windows/desktop/jj128316.aspx) | Introduced in 10.0.10240. |
| [IMFPMPHostApp](https://msdn.microsoft.com/library/windows/desktop/jj128318.aspx) | Introduced in 10.0.10240. |
| [IMFPresentationClock](https://msdn.microsoft.com/library/windows/desktop/ms701581.aspx) | Introduced in 10.0.10240. |
| [IMFPresentationDescriptor](https://msdn.microsoft.com/library/windows/desktop/ms703990.aspx) | Introduced in 10.0.10240. |
| [IMFPresentationTimeSource](https://msdn.microsoft.com/library/windows/desktop/ms704711.aspx) | Introduced in 10.0.10240. |
| [IMFProtectedEnvironmentAccess](https://msdn.microsoft.com/library/windows/desktop/hh448045.aspx) | Introduced in 10.0.10240. |
| [IMFQualityAdvise](https://msdn.microsoft.com/library/windows/desktop/ms695241.aspx) | Introduced in 10.0.10240. |
| [IMFQualityAdvise2](https://msdn.microsoft.com/library/windows/desktop/dd743249.aspx) | Introduced in 10.0.10240. |
| [IMFQualityAdviseLimits](https://msdn.microsoft.com/library/windows/desktop/dd374511.aspx) | Introduced in 10.0.10240. |
| [IMFRateControl](https://msdn.microsoft.com/library/windows/desktop/ms697193.aspx) | Introduced in 10.0.10240. |
| [IMFRateSupport](https://msdn.microsoft.com/library/windows/desktop/ms701858.aspx) | Introduced in 10.0.10240. |
| [IMFReadWriteClassFactory](https://msdn.microsoft.com/library/windows/desktop/dd374514.aspx) | Introduced in 10.0.10240. |
| [IMFRealTimeClientEx](https://msdn.microsoft.com/library/windows/desktop/hh448047.aspx) | Introduced in 10.0.10240. |
| [IMFSample](https://msdn.microsoft.com/library/windows/desktop/ms702192.aspx) | Introduced in 10.0.10240. |
| [IMFSampleOutputStream](https://msdn.microsoft.com/library/windows/desktop/hh448051.aspx) | Introduced in 10.0.10240. |
| [IMFSampleProtection](https://msdn.microsoft.com/library/windows/desktop/ms703018.aspx) | Introduced in 10.0.10240. |
| [IMFSchemeHandler](https://msdn.microsoft.com/library/windows/desktop/ms701638.aspx) | Introduced in 10.0.10240. |
| [IMFSeekInfo](https://msdn.microsoft.com/library/windows/desktop/hh448054.aspx) | Introduced in 10.0.10240. |
| [IMFShutdown](https://msdn.microsoft.com/library/windows/desktop/ms703054.aspx) | Introduced in 10.0.10240. |
| [IMFSignedLibrary](https://msdn.microsoft.com/library/windows/desktop/hh448058.aspx) | Introduced in 10.0.10240. |
| [IMFSinkWriter](https://msdn.microsoft.com/library/windows/desktop/dd374642.aspx) | Introduced in 10.0.10240. |
| [IMFSinkWriterCallback](https://msdn.microsoft.com/library/windows/desktop/dd374643.aspx) | Introduced in 10.0.10240. |
| [IMFSinkWriterCallback2](https://msdn.microsoft.com/library/windows/desktop/dn949415.aspx) | Introduced in 10.0.10240. |
| [IMFSinkWriterEx](https://msdn.microsoft.com/library/windows/desktop/hh448060.aspx) | Introduced in 10.0.10240. |
| [IMFSinkWriterEncoderConfig](https://msdn.microsoft.com/library/windows/desktop/dn302046.aspx) | Introduced in 10.0.10240. |
| [IMFSourceReader](https://msdn.microsoft.com/library/windows/desktop/dd374655.aspx) | Introduced in 10.0.10240. |
| [IMFSourceReaderCallback](https://msdn.microsoft.com/library/windows/desktop/dd374656.aspx) | Introduced in 10.0.10240. |
| [IMFSourceReaderCallback2](https://msdn.microsoft.com/library/windows/desktop/dn949418.aspx) | Introduced in 10.0.10240. |
| [IMFSourceReaderEx](https://msdn.microsoft.com/library/windows/desktop/hh448062.aspx) | Introduced in 10.0.10240. |
| [IMFSourceResolver](https://msdn.microsoft.com/library/windows/desktop/ms694009.aspx) | Introduced in 10.0.10240. |
| [IMFStreamDescriptor](https://msdn.microsoft.com/library/windows/desktop/ms701622.aspx) | Introduced in 10.0.10240. |
| [IMFStreamingSinkConfig](https://msdn.microsoft.com/library/windows/desktop/dd374676.aspx) | Introduced in 10.0.10240. |
| [IMFStreamSink](https://msdn.microsoft.com/library/windows/desktop/ms705657.aspx) | Introduced in 10.0.10240. |
| [IMFSystemId](https://msdn.microsoft.com/library/windows/desktop/hh448067.aspx) | Introduced in 10.0.10240. |
| [IMFTrackedSample](https://msdn.microsoft.com/library/windows/desktop/ms697026.aspx) | Introduced in 10.0.10240. |
| [IMFTransform](https://msdn.microsoft.com/library/windows/desktop/ms696260.aspx) | Introduced in 10.0.10240. |
| [IMFTrustedInput](https://msdn.microsoft.com/library/windows/desktop/ms697279.aspx) | Introduced in 10.0.10240. |
| [IMFTrustedOutput](https://msdn.microsoft.com/library/windows/desktop/ms694305.aspx) | Introduced in 10.0.10240. |
| [IMFVideoSampleAllocator](https://msdn.microsoft.com/library/windows/desktop/aa473823.aspx) | Introduced in 10.0.10240. |
| [IMFVideoSampleAllocatorCallback](https://msdn.microsoft.com/library/windows/desktop/dd374900.aspx) | Introduced in 10.0.10240. |
| [IMFVideoSampleAllocatorEx](https://msdn.microsoft.com/library/windows/desktop/hh448076.aspx) | Introduced in 10.0.10240. |
| [IMFVideoSampleAllocatorNotify](https://msdn.microsoft.com/library/windows/desktop/dd374906.aspx) | Introduced in 10.0.10240. |
| [IMFVideoSampleAllocatorNotifyEx](https://msdn.microsoft.com/library/windows/desktop/mt627756.aspx) | Introduced in 10.0.10240. |
| [IMFVideoProcessorControl](https://msdn.microsoft.com/library/windows/desktop/hh448069.aspx) | Introduced in 10.0.10240. |
| [IMFVideoProcessorControl2](https://msdn.microsoft.com/library/windows/desktop/dn800741.aspx) | Introduced in 10.0.10240. |
| [IMLangConvertCharset](https://msdn.microsoft.com/library/windows/desktop/aa741058.aspx) | Introduced in 10.0.10240. |
| [IMultiLanguage](https://msdn.microsoft.com/library/windows/desktop/aa741022.aspx) | Introduced in 10.0.10240. |
| [IMultiLanguage2](https://msdn.microsoft.com/library/windows/desktop/aa741001.aspx) | Introduced in 10.0.10240. |
| [IMultipleViewProvider](https://msdn.microsoft.com/library/windows/desktop/ee671296.aspx) | Introduced in 10.0.10240. |
| [IMultiQI](https://msdn.microsoft.com/library/windows/desktop/ms683863.aspx) | Introduced in 10.0.10240. |
| [INoMarshal](https://msdn.microsoft.com/library/windows/desktop/hh802477.aspx) | Introduced in 10.0.10240. |
| [IObjectModelProvider](https://msdn.microsoft.com/library/windows/desktop/hh448776.aspx) | Introduced in 10.0.10240. |
| [IOpcCertificateEnumerator](https://msdn.microsoft.com/library/windows/desktop/dd368258.aspx) | Introduced in 10.0.10240. |
| [IOpcCertificateSet](https://msdn.microsoft.com/library/windows/desktop/dd368269.aspx) | Introduced in 10.0.10240. |
| [IOpcDigitalSignature](https://msdn.microsoft.com/library/windows/desktop/dd368278.aspx) | Introduced in 10.0.10240. |
| [IOpcDigitalSignatureEnumerator](https://msdn.microsoft.com/library/windows/desktop/dd368280.aspx) | Introduced in 10.0.10240. |
| [IOpcDigitalSignatureManager](https://msdn.microsoft.com/library/windows/desktop/dd368288.aspx) | Introduced in 10.0.10240. |
| [IOpcFactory](https://msdn.microsoft.com/library/windows/desktop/dd370991.aspx) | Introduced in 10.0.10240. |
| [IOpcPackage](https://msdn.microsoft.com/library/windows/desktop/dd371025.aspx) | Introduced in 10.0.10240. |
| [IOpcPart](https://msdn.microsoft.com/library/windows/desktop/dd371038.aspx) | Introduced in 10.0.10240. |
| [IOpcPartEnumerator](https://msdn.microsoft.com/library/windows/desktop/dd371043.aspx) | Introduced in 10.0.10240. |
| [IOpcPartSet](https://msdn.microsoft.com/library/windows/desktop/dd371062.aspx) | Introduced in 10.0.10240. |
| [IOpcPartUri](https://msdn.microsoft.com/library/windows/desktop/dd371083.aspx) | Introduced in 10.0.10240. |
| [IOpcRelationship](https://msdn.microsoft.com/library/windows/desktop/dd371131.aspx) | Introduced in 10.0.10240. |
| [IOpcRelationshipEnumerator](https://msdn.microsoft.com/library/windows/desktop/dd371135.aspx) | Introduced in 10.0.10240. |
| [IOpcRelationshipSelector](https://msdn.microsoft.com/library/windows/desktop/dd371151.aspx) | Introduced in 10.0.10240. |
| [IOpcRelationshipSelectorEnumerator](https://msdn.microsoft.com/library/windows/desktop/dd371154.aspx) | Introduced in 10.0.10240. |
| [IOpcRelationshipSelectorSet](https://msdn.microsoft.com/library/windows/desktop/dd371169.aspx) | Introduced in 10.0.10240. |
| [IOpcRelationshipSet](https://msdn.microsoft.com/library/windows/desktop/dd371217.aspx) | Introduced in 10.0.10240. |
| [IOpcSignatureCustomObject](https://msdn.microsoft.com/library/windows/desktop/dd316546.aspx) | Introduced in 10.0.10240. |
| [IOpcSignatureCustomObjectEnumerator](https://msdn.microsoft.com/library/windows/desktop/dd316548.aspx) | Introduced in 10.0.10240. |
| [IOpcSignatureCustomObjectSet](https://msdn.microsoft.com/library/windows/desktop/dd316560.aspx) | Introduced in 10.0.10240. |
| [IOpcSignaturePartReference](https://msdn.microsoft.com/library/windows/desktop/dd316570.aspx) | Introduced in 10.0.10240. |
| [IOpcSignaturePartReferenceEnumerator](https://msdn.microsoft.com/library/windows/desktop/dd316571.aspx) | Introduced in 10.0.10240. |
| [IOpcSignaturePartReferenceSet](https://msdn.microsoft.com/library/windows/desktop/dd316585.aspx) | Introduced in 10.0.10240. |
| [IOpcSignatureReference](https://msdn.microsoft.com/library/windows/desktop/dd316612.aspx) | Introduced in 10.0.10240. |
| [IOpcSignatureReferenceEnumerator](https://msdn.microsoft.com/library/windows/desktop/dd316615.aspx) | Introduced in 10.0.10240. |
| [IOpcSignatureReferenceSet](https://msdn.microsoft.com/library/windows/desktop/dd316629.aspx) | Introduced in 10.0.10240. |
| [IOpcSignatureRelationshipReference](https://msdn.microsoft.com/library/windows/desktop/dd316670.aspx) | Introduced in 10.0.10240. |
| [IOpcSignatureRelationshipReferenceEnumerator](https://msdn.microsoft.com/library/windows/desktop/dd316673.aspx) | Introduced in 10.0.10240. |
| [IOpcSignatureRelationshipReferenceSet](https://msdn.microsoft.com/library/windows/desktop/dd316689.aspx) | Introduced in 10.0.10240. |
| [IOpcSigningOptions](https://msdn.microsoft.com/library/windows/desktop/dd316719.aspx) | Introduced in 10.0.10240. |
| [IOpcUri](https://msdn.microsoft.com/library/windows/desktop/dd316778.aspx) | Introduced in 10.0.10240. |
| [IOptionDescription](https://msdn.microsoft.com/library/windows/desktop/hh869762.aspx) | Introduced in 10.0.10240. |
| [IPdfRendererNative](https://msdn.microsoft.com/library/windows/desktop/dn302125.aspx) | Introduced in 10.0.10240. |
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
| [IPortableDevice](https://msdn.microsoft.com/library/windows/desktop/dd319361.aspx) | Introduced in 10.0.10240. |
| [IPortableDeviceCapabilities](https://msdn.microsoft.com/library/windows/desktop/dd319362.aspx) | Introduced in 10.0.10240. |
| [IPortableDeviceContent](https://msdn.microsoft.com/library/windows/desktop/dd388529.aspx) | Introduced in 10.0.10240. |
| [IPortableDeviceContent2](https://msdn.microsoft.com/library/windows/desktop/dd388530.aspx) | Introduced in 10.0.10240. |
| [IPortableDeviceDataStream](https://msdn.microsoft.com/library/windows/desktop/dd388542.aspx) | Introduced in 10.0.10240. |
| [IPortableDeviceDispatchFactory](https://msdn.microsoft.com/library/windows/desktop/dd389218.aspx) | Introduced in 10.0.10240. |
| [IPortableDeviceEventCallback](https://msdn.microsoft.com/library/windows/desktop/dd388545.aspx) | Introduced in 10.0.10240. |
| [IPortableDeviceKeyCollection](https://msdn.microsoft.com/library/windows/desktop/dd388547.aspx) | Introduced in 10.0.10240. |
| [IPortableDeviceManager](https://msdn.microsoft.com/library/windows/desktop/dd388688.aspx) | Introduced in 10.0.10240. |
| [IPortableDeviceProperties](https://msdn.microsoft.com/library/windows/desktop/dd388696.aspx) | Introduced in 10.0.10240. |
| [IPortableDevicePropertiesBulk](https://msdn.microsoft.com/library/windows/desktop/dd388697.aspx) | Introduced in 10.0.10240. |
| [IPortableDevicePropertiesBulkCallback](https://msdn.microsoft.com/library/windows/desktop/dd388698.aspx) | Introduced in 10.0.10240. |
| [IPortableDevicePropVariantCollection](https://msdn.microsoft.com/library/windows/desktop/dd388719.aspx) | Introduced in 10.0.10240. |
| [IPortableDeviceResources](https://msdn.microsoft.com/library/windows/desktop/dd388733.aspx) | Introduced in 10.0.10240. |
| [IPortableDeviceService](https://msdn.microsoft.com/library/windows/desktop/dd388753.aspx) | Introduced in 10.0.10240. |
| IPortableDeviceServiceActivation | Introduced in 10.0.10240. |
| [IPortableDeviceServiceCapabilities](https://msdn.microsoft.com/library/windows/desktop/dd388755.aspx) | Introduced in 10.0.10240. |
| [IPortableDeviceServiceManager](https://msdn.microsoft.com/library/windows/desktop/dd319402.aspx) | Introduced in 10.0.10240. |
| [IPortableDeviceServiceMethodCallback](https://msdn.microsoft.com/library/windows/desktop/dd319411.aspx) | Introduced in 10.0.10240. |
| [IPortableDeviceServiceMethods](https://msdn.microsoft.com/library/windows/desktop/dd319418.aspx) | Introduced in 10.0.10240. |
| IPortableDeviceServiceOpenCallback | Introduced in 10.0.10240. |
| [IPortableDeviceUnitsStream](https://msdn.microsoft.com/library/windows/desktop/hh707376.aspx) | Introduced in 10.0.10240. |
| [IPortableDeviceValues](https://msdn.microsoft.com/library/windows/desktop/dd319461.aspx) | Introduced in 10.0.10240. |
| [IPortableDeviceValuesCollection](https://msdn.microsoft.com/library/windows/desktop/dd319463.aspx) | Introduced in 10.0.10240. |
| [IPrintDocumentPackageTarget](https://msdn.microsoft.com/library/windows/desktop/hh448393.aspx) | Introduced in 10.0.10240. |
| [IPrintDocumentPageSource](https://msdn.microsoft.com/library/windows/desktop/jj710015.aspx) | Introduced in 10.0.10240. |
| [IPrinterBidiSetRequestCallback](https://msdn.microsoft.com/library/windows/desktop/dn265385.aspx) | Introduced in 10.0.10240. |
| [IPrinterExtensionAsyncOperation](https://msdn.microsoft.com/library/windows/desktop/dn265387.aspx) | Introduced in 10.0.10240. |
| [IPrinterExtensionContext](https://msdn.microsoft.com/library/windows/desktop/hh406649.aspx) | Introduced in 10.0.10240. |
| [IPrinterPropertyBag](https://msdn.microsoft.com/library/windows/desktop/hh439547.aspx) | Introduced in 10.0.10240. |
| [IPrinterQueue](https://msdn.microsoft.com/library/windows/desktop/hh439635.aspx) | Introduced in 10.0.10240. |
| [IPrinterQueue2](https://msdn.microsoft.com/library/windows/desktop/dn265389.aspx) | Introduced in 10.0.10240. |
| [IPrinterQueueEvent](https://msdn.microsoft.com/library/windows/desktop/hh439618.aspx) | Introduced in 10.0.10240. |
| [IPrinterQueueView](https://msdn.microsoft.com/library/windows/desktop/dn265392.aspx) | Introduced in 10.0.10240. |
| [IPrinterQueueViewEvent](https://msdn.microsoft.com/library/windows/desktop/dn265393.aspx) | Introduced in 10.0.10240. |
| [IPrintJob](https://msdn.microsoft.com/library/windows/desktop/dn265396.aspx) | Introduced in 10.0.10240. |
| [IPrintJobCollection](https://msdn.microsoft.com/library/windows/desktop/dn265397.aspx) | Introduced in 10.0.10240. |
| [IPrintPreviewDxgiPackageTarget](https://msdn.microsoft.com/library/windows/desktop/jj553554.aspx) | Introduced in 10.0.10240. |
| [IPrintPreviewPageCollection](https://msdn.microsoft.com/library/windows/desktop/jj710018.aspx) | Introduced in 10.0.10240. |
| [IPrintSchemaAsyncOperation](https://msdn.microsoft.com/library/windows/desktop/hh451224.aspx) | Introduced in 10.0.10240. |
| [IPrintSchemaAsyncOperationEvent](https://msdn.microsoft.com/library/windows/desktop/hh451211.aspx) | Introduced in 10.0.10240. |
| [IPrintSchemaCapabilities](https://msdn.microsoft.com/library/windows/desktop/hh451256.aspx) | Introduced in 10.0.10240. |
| [IPrintSchemaCapabilities2](https://msdn.microsoft.com/library/Dn465887(v=VS.85).aspx) | Introduced in 10.0.10240. |
| [IPrintSchemaDisplayableElement](https://msdn.microsoft.com/library/windows/desktop/hh451262.aspx) | Introduced in 10.0.10240. |
| [IPrintSchemaElement](https://msdn.microsoft.com/library/windows/desktop/hh451270.aspx) | Introduced in 10.0.10240. |
| [IPrintSchemaFeature](https://msdn.microsoft.com/library/windows/desktop/hh451284.aspx) | Introduced in 10.0.10240. |
| [IPrintSchemaNUpOption](https://msdn.microsoft.com/library/windows/desktop/hh451302.aspx) | Introduced in 10.0.10240. |
| [IPrintSchemaOption](https://msdn.microsoft.com/library/windows/desktop/hh451335.aspx) | Introduced in 10.0.10240. |
| [IPrintSchemaOptionCollection](https://msdn.microsoft.com/library/windows/desktop/hh846198.aspx) | Introduced in 10.0.10240. |
| [IPrintSchemaPageImageableSize](https://msdn.microsoft.com/library/windows/desktop/hh451366.aspx) | Introduced in 10.0.10240. |
| [IPrintSchemaPageMediaSizeOption](https://msdn.microsoft.com/library/windows/desktop/hh451378.aspx) | Introduced in 10.0.10240. |
| [IPrintSchemaParameterDefinition](https://msdn.microsoft.com/library/Dn465890(v=VS.85).aspx) | Introduced in 10.0.10240. |
| [IPrintSchemaParameterInitializer](https://msdn.microsoft.com/library/Dn454557(v=VS.85).aspx) | Introduced in 10.0.10240. |
| [IPrintSchemaTicket](https://msdn.microsoft.com/library/windows/desktop/hh451398.aspx) | Introduced in 10.0.10240. |
| [IPrintSchemaTicket2](https://msdn.microsoft.com/library/Dn454560(v=VS.85).aspx) | Introduced in 10.0.10240. |
| [IPropertyBag2](https://msdn.microsoft.com/library/Aa768192(v=VS.85).aspx) | Introduced in 10.0.10240. |
| [IPropertySetStorage](https://msdn.microsoft.com/library/windows/desktop/aa379840.aspx) | Introduced in 10.0.10240. |
| [IPropertyStorage](https://msdn.microsoft.com/library/windows/desktop/aa379968.aspx) | Introduced in 10.0.10240. |
| [IPropertyStore](https://msdn.microsoft.com/library/windows/desktop/bb761474.aspx) | Introduced in 10.0.10240. |
| [IProxyProviderWinEventHandler](https://msdn.microsoft.com/library/windows/desktop/ee671303.aspx) | Introduced in 10.0.10240. |
| [IProxyProviderWinEventSink](https://msdn.microsoft.com/library/windows/desktop/ee671305.aspx) | Introduced in 10.0.10240. |
| [IPSFactoryBuffer](https://msdn.microsoft.com/library/windows/desktop/ms695281.aspx) | Introduced in 10.0.10240. |
| [IQuickActivate](https://msdn.microsoft.com/library/windows/desktop/ms690146.aspx) | Introduced in 10.0.10240. |
| [IRangeValueProvider](https://msdn.microsoft.com/library/windows/desktop/ee671309.aspx) | Introduced in 10.0.10240. |
| [IRawElementProviderAdviseEvents](https://msdn.microsoft.com/library/windows/desktop/ee671317.aspx) | Introduced in 10.0.10240. |
| [IRawElementProviderFragment](https://msdn.microsoft.com/library/windows/desktop/ee671320.aspx) | Introduced in 10.0.10240. |
| [IRawElementProviderFragmentRoot](https://msdn.microsoft.com/library/windows/desktop/ee671321.aspx) | Introduced in 10.0.10240. |
| [IRawElementProviderHostingAccessibles](https://msdn.microsoft.com/library/windows/desktop/hh448785.aspx) | Introduced in 10.0.10240. |
| [IRawElementProviderHwndOverride](https://msdn.microsoft.com/library/windows/desktop/ee671330.aspx) | Introduced in 10.0.10240. |
| [IRawElementProviderSimple](https://msdn.microsoft.com/library/windows/desktop/ee671332.aspx) | Introduced in 10.0.10240. |
| [IRawElementProviderSimple2](https://msdn.microsoft.com/library/windows/desktop/dn302133.aspx) | Introduced in 10.0.10240. |
| [IRawElementProviderWindowlessSite](https://msdn.microsoft.com/library/windows/desktop/hh448787.aspx) | Introduced in 10.0.10240. |
| [IRDPSRAPIApplication](https://msdn.microsoft.com/library/windows/desktop/aa373266.aspx) | Introduced in 10.0.10240. |
| [IRDPSRAPIApplicationFilter](https://msdn.microsoft.com/library/windows/desktop/aa373267.aspx) | Introduced in 10.0.10240. |
| [IRDPSRAPIApplicationList](https://msdn.microsoft.com/library/windows/desktop/aa373271.aspx) | Introduced in 10.0.10240. |
| [IRDPSRAPIAttendee](https://msdn.microsoft.com/library/windows/desktop/aa373279.aspx) | Introduced in 10.0.10240. |
| [IRDPSRAPIAttendeeDisconnectInfo](https://msdn.microsoft.com/library/windows/desktop/aa373280.aspx) | Introduced in 10.0.10240. |
| [IRDPSRAPIAttendeeManager](https://msdn.microsoft.com/library/windows/desktop/aa373284.aspx) | Introduced in 10.0.10240. |
| [IRDPSRAPIAudioStream](https://msdn.microsoft.com/library/windows/desktop/dn408582.aspx) | Introduced in 10.0.10240. |
| IRDPSRAPIDebug | Introduced in 10.0.10240. |
| [IRDPSRAPIFrameBuffer](https://msdn.microsoft.com/library/windows/desktop/dn894394.aspx) | Introduced in 10.0.10240. |
| [IRDPSRAPIInvitation](https://msdn.microsoft.com/library/windows/desktop/aa373294.aspx) | Introduced in 10.0.10240. |
| [IRDPSRAPIInvitationManager](https://msdn.microsoft.com/library/windows/desktop/aa373295.aspx) | Introduced in 10.0.10240. |
| [IRDPSRAPIPerfCounterLogger](https://msdn.microsoft.com/library/windows/desktop/dn408589.aspx) | Introduced in 10.0.10240. |
| [IRDPSRAPIPerfCounterLoggingManager](https://msdn.microsoft.com/library/windows/desktop/dn408592.aspx) | Introduced in 10.0.10240. |
| [IRDPSRAPISessionProperties](https://msdn.microsoft.com/library/windows/desktop/aa373305.aspx) | Introduced in 10.0.10240. |
| [IRDPSRAPISharingSession](https://msdn.microsoft.com/library/windows/desktop/aa373307.aspx) | Introduced in 10.0.10240. |
| [IRDPSRAPISharingSession2](https://msdn.microsoft.com/library/windows/desktop/dn894401.aspx) | Introduced in 10.0.10240. |
| [IRDPSRAPITcpConnectionInfo](https://msdn.microsoft.com/library/windows/desktop/aa373321.aspx) | Introduced in 10.0.10240. |
| [IRDPSRAPITransportStream](https://msdn.microsoft.com/library/windows/desktop/ee620975.aspx) | Introduced in 10.0.10240. |
| [IRDPSRAPITransportStreamBuffer](https://msdn.microsoft.com/library/windows/desktop/ee620976.aspx) | Introduced in 10.0.10240. |
| [IRDPSRAPITransportStreamEvents](https://msdn.microsoft.com/library/windows/desktop/ee620984.aspx) | Introduced in 10.0.10240. |
| [IRDPSRAPIViewer](https://msdn.microsoft.com/library/windows/desktop/aa373327.aspx) | Introduced in 10.0.10240. |
| [IRDPSRAPIVirtualChannel](https://msdn.microsoft.com/library/windows/desktop/aa373361.aspx) | Introduced in 10.0.10240. |
| [IRDPSRAPIVirtualChannelManager](https://msdn.microsoft.com/library/windows/desktop/aa373362.aspx) | Introduced in 10.0.10240. |
| [IRDPSRAPIWindow](https://msdn.microsoft.com/library/windows/desktop/aa373371.aspx) | Introduced in 10.0.10240. |
| [IRDPSRAPIWindowList](https://msdn.microsoft.com/library/windows/desktop/aa373372.aspx) | Introduced in 10.0.10240. |
| [IRDPViewerInputSink](https://msdn.microsoft.com/library/windows/desktop/dn408595.aspx) | Introduced in 10.0.10240. |
| [IRDPViewerRenderingSurface](https://msdn.microsoft.com/library/windows/desktop/hh802746.aspx) | Introduced in 10.0.10240. |
| [IReferenceTracker](https://msdn.microsoft.com/library/windows/desktop/jj542495.aspx) | Introduced in 10.0.10240. |
| [IReferenceTrackerHost](https://msdn.microsoft.com/library/windows/desktop/jj542496.aspx) | Introduced in 10.0.10240. |
| [IReferenceTrackerManager](https://msdn.microsoft.com/library/windows/desktop/jj542503.aspx) | Introduced in 10.0.10240. |
| [IReferenceTrackerTarget](https://msdn.microsoft.com/library/windows/desktop/jj542508.aspx) | Introduced in 10.0.10240. |
| [IRemoteDesktopClient](https://msdn.microsoft.com/library/windows/desktop/hh448564.aspx) | Introduced in 10.0.10240. |
| [IRemoteDesktopClientActions](https://msdn.microsoft.com/library/windows/desktop/hh448581.aspx) | Introduced in 10.0.10240. |
| [IRemoteDesktopClientEvents](https://msdn.microsoft.com/library/windows/desktop/hh448568.aspx) | Introduced in 10.0.10240. |
| [IRemoteDesktopClientSettings](https://msdn.microsoft.com/library/windows/desktop/hh448590.aspx) | Introduced in 10.0.10240. |
| [IRestrictedErrorInfo](https://msdn.microsoft.com/library/windows/desktop/br224587.aspx) | Introduced in 10.0.10240. |
| [IRootStorage](https://msdn.microsoft.com/library/windows/desktop/aa379987.aspx) | Introduced in 10.0.10240. |
| [IRpcChannelBuffer](https://msdn.microsoft.com/library/windows/desktop/ms679738.aspx) | Introduced in 10.0.10240. |
| [IRpcStubBuffer](https://msdn.microsoft.com/library/windows/desktop/ms678504.aspx) | Introduced in 10.0.10240. |
| [IScrollItemProvider](https://msdn.microsoft.com/library/windows/desktop/ee671338.aspx) | Introduced in 10.0.10240. |
| [IScrollProvider](https://msdn.microsoft.com/library/windows/desktop/ee671340.aspx) | Introduced in 10.0.10240. |
| [ISelectionItemProvider](https://msdn.microsoft.com/library/windows/desktop/ee671349.aspx) | Introduced in 10.0.10240. |
| [ISelectionProvider](https://msdn.microsoft.com/library/windows/desktop/ee671355.aspx) | Introduced in 10.0.10240. |
| [ISequentialStream](https://msdn.microsoft.com/library/windows/desktop/aa380010.aspx) | Introduced in 10.0.10240. |
| ISignalableNotifier | Introduced in 10.0.10240. |
| [ISimpleAudioVolume](https://msdn.microsoft.com/library/windows/desktop/dd316531.aspx) | Introduced in 10.0.10240. |
| [ISoftwareBitmapNative](https://msdn.microsoft.com/library/windows/desktop/dn878036.aspx) | Introduced in 10.0.10240. |
| [ISoftwareBitmapNativeFactory](https://msdn.microsoft.com/library/windows/desktop/dn878037.aspx) | Introduced in 10.0.10240. |
| [ISpellChecker](https://msdn.microsoft.com/library/windows/desktop/hh869767.aspx) | Introduced in 10.0.10240. |
| [ISpellChecker2](https://msdn.microsoft.com/library/windows/desktop/mt422900.aspx) | Introduced in 10.0.10240. |
| [ISpellCheckerChangedEventHandler](https://msdn.microsoft.com/library/windows/desktop/hh869768.aspx) | Introduced in 10.0.10240. |
| [ISpellCheckerFactory](https://msdn.microsoft.com/library/windows/desktop/hh869770.aspx) | Introduced in 10.0.10240. |
| [ISpellingError](https://msdn.microsoft.com/library/windows/desktop/hh869805.aspx) | Introduced in 10.0.10240. |
| [ISpreadsheetItemProvider](https://msdn.microsoft.com/library/windows/desktop/hh448790.aspx) | Introduced in 10.0.10240. |
| [ISpreadsheetProvider](https://msdn.microsoft.com/library/windows/desktop/hh448796.aspx) | Introduced in 10.0.10240. |
| [IStorage](https://msdn.microsoft.com/library/windows/desktop/aa380015.aspx) | Introduced in 10.0.10240. |
| [IStream](https://msdn.microsoft.com/library/windows/desktop/aa380034.aspx) | Introduced in 10.0.10240. |
| [IStylesProvider](https://msdn.microsoft.com/library/windows/desktop/hh448800.aspx) | Introduced in 10.0.10240. |
| [ISurfaceImageSourceManagerNative](https://msdn.microsoft.com/library/windows/desktop/dn448959.aspx) | Introduced in 10.0.10240. |
| [ISurfaceImageSourceNative](https://msdn.microsoft.com/library/windows/desktop/hh848322.aspx) | Introduced in 10.0.10240. |
| [ISurfaceImageSourceNativeWithD2D](https://msdn.microsoft.com/library/windows/desktop/dn302137.aspx) | Introduced in 10.0.10240. |
| [ISurrogate](https://msdn.microsoft.com/library/windows/desktop/ms695062.aspx) | Introduced in 10.0.10240. |
| [ISwapChainBackgroundPanelNative](https://msdn.microsoft.com/library/windows/desktop/hh848326.aspx) | Introduced in 10.0.10240. |
| [ISwapChainPanelNative](https://msdn.microsoft.com/library/windows/desktop/dn302143.aspx) | Introduced in 10.0.10240. |
| [ISwapChainPanelNative2](https://msdn.microsoft.com/library/windows/desktop/dn858172.aspx) | Introduced in 10.0.10240. |
| [ISynchronizedInputProvider](https://msdn.microsoft.com/library/windows/desktop/ee671359.aspx) | Introduced in 10.0.10240. |
| [ITableItemProvider](https://msdn.microsoft.com/library/windows/desktop/ee671362.aspx) | Introduced in 10.0.10240. |
| [ITableProvider](https://msdn.microsoft.com/library/windows/desktop/ee671365.aspx) | Introduced in 10.0.10240. |
| [ITextChildProvider](https://msdn.microsoft.com/library/windows/desktop/hh437317.aspx) | Introduced in 10.0.10240. |
| [ITextEditProvider](https://msdn.microsoft.com/library/windows/desktop/dn302166.aspx) | Introduced in 10.0.10240. |
| [ITextProvider](https://msdn.microsoft.com/library/windows/desktop/ee671370.aspx) | Introduced in 10.0.10240. |
| [ITextProvider2](https://msdn.microsoft.com/library/windows/desktop/hh448818.aspx) | Introduced in 10.0.10240. |
| [ITextRangeProvider](https://msdn.microsoft.com/library/windows/desktop/ee671377.aspx) | Introduced in 10.0.10240. |
| [ITextRangeProvider2](https://msdn.microsoft.com/library/windows/desktop/dn302169.aspx) | Introduced in 10.0.10240. |
| [ITextStoreACP2](https://msdn.microsoft.com/library/windows/desktop/jj670566.aspx) | Introduced in 10.0.10240. |
| [ITextStoreACPServices](https://msdn.microsoft.com/library/windows/desktop/ms538387.aspx) | Introduced in 10.0.10240. |
| [ITextStoreACPSink](https://msdn.microsoft.com/library/windows/desktop/ms538395.aspx) | Introduced in 10.0.10240. |
| [ITextStoreAnchor](https://msdn.microsoft.com/library/windows/desktop/ms538453.aspx) | Introduced in 10.0.10240. |
| [ITextStoreAnchorSink](https://msdn.microsoft.com/library/windows/desktop/ms538454.aspx) | Introduced in 10.0.10240. |
| [ITfCandidateList](https://msdn.microsoft.com/library/windows/desktop/ms538492.aspx) | Introduced in 10.0.10240. |
| [ITfCandidateListUIElement](https://msdn.microsoft.com/library/windows/desktop/aa380892.aspx) | Introduced in 10.0.10240. |
| [ITfCandidateListUIElementBehavior](https://msdn.microsoft.com/library/windows/desktop/aa381004.aspx) | Introduced in 10.0.10240. |
| [ITfCandidateString](https://msdn.microsoft.com/library/windows/desktop/ms538497.aspx) | Introduced in 10.0.10240. |
| [ITfCategoryMgr](https://msdn.microsoft.com/library/windows/desktop/ms538500.aspx) | Introduced in 10.0.10240. |
| [ITfCompartment](https://msdn.microsoft.com/library/windows/desktop/ms538621.aspx) | Introduced in 10.0.10240. |
| [ITfCompartmentEventSink](https://msdn.microsoft.com/library/windows/desktop/ms538625.aspx) | Introduced in 10.0.10240. |
| [ITfCompartmentMgr](https://msdn.microsoft.com/library/windows/desktop/ms538631.aspx) | Introduced in 10.0.10240. |
| [ITfComposition](https://msdn.microsoft.com/library/windows/desktop/ms538653.aspx) | Introduced in 10.0.10240. |
| [ITfCompositionSink](https://msdn.microsoft.com/library/windows/desktop/ms538654.aspx) | Introduced in 10.0.10240. |
| [ITfCompositionView](https://msdn.microsoft.com/library/windows/desktop/ms538660.aspx) | Introduced in 10.0.10240. |
| [ITfConfigureSystemKeystrokeFeed](https://msdn.microsoft.com/library/windows/desktop/ms538692.aspx) | Introduced in 10.0.10240. |
| [ITfContext](https://msdn.microsoft.com/library/windows/desktop/ms538703.aspx) | Introduced in 10.0.10240. |
| [ITfContextComposition](https://msdn.microsoft.com/library/windows/desktop/ms538705.aspx) | Introduced in 10.0.10240. |
| [ITfContextOwnerCompositionServices](https://msdn.microsoft.com/library/windows/desktop/ms538734.aspx) | Introduced in 10.0.10240. |
| [ITfContextOwnerCompositionSink](https://msdn.microsoft.com/library/windows/desktop/ms538740.aspx) | Introduced in 10.0.10240. |
| [ITfContextOwnerServices](https://msdn.microsoft.com/library/windows/desktop/ms538750.aspx) | Introduced in 10.0.10240. |
| [ITfContextView](https://msdn.microsoft.com/library/windows/desktop/ms538779.aspx) | Introduced in 10.0.10240. |
| [ITfDisplayAttributeInfo](https://msdn.microsoft.com/library/windows/desktop/ms538802.aspx) | Introduced in 10.0.10240. |
| [ITfDisplayAttributeMgr](https://msdn.microsoft.com/library/windows/desktop/ms538808.aspx) | Introduced in 10.0.10240. |
| [ITfDisplayAttributeNotifySink](https://msdn.microsoft.com/library/windows/desktop/ms538869.aspx) | Introduced in 10.0.10240. |
| [ITfDisplayAttributeProvider](https://msdn.microsoft.com/library/windows/desktop/ms538873.aspx) | Introduced in 10.0.10240. |
| [ITfDocumentMgr](https://msdn.microsoft.com/library/windows/desktop/ms538878.aspx) | Introduced in 10.0.10240. |
| [ITfEditRecord](https://msdn.microsoft.com/library/windows/desktop/ms538901.aspx) | Introduced in 10.0.10240. |
| [ITfEditSession](https://msdn.microsoft.com/library/windows/desktop/ms538906.aspx) | Introduced in 10.0.10240. |
| [ITfFnGetSAPIObject](https://msdn.microsoft.com/library/windows/desktop/ms538932.aspx) | Introduced in 10.0.10240. |
| [ITfFnReconversion](https://msdn.microsoft.com/library/windows/desktop/ms538970.aspx) | Introduced in 10.0.10240. |
| [ITfFunction](https://msdn.microsoft.com/library/windows/desktop/ms538978.aspx) | Introduced in 10.0.10240. |
| [ITfFunctionProvider](https://msdn.microsoft.com/library/windows/desktop/ms538979.aspx) | Introduced in 10.0.10240. |
| [ITfInputProcessorProfileActivationSink](https://msdn.microsoft.com/library/windows/desktop/aa381928.aspx) | Introduced in 10.0.10240. |
| [ITfInputProcessorProfileMgr](https://msdn.microsoft.com/library/windows/desktop/aa381941.aspx) | Introduced in 10.0.10240. |
| [ITfInputScope](https://msdn.microsoft.com/library/windows/desktop/ms628582.aspx) | Introduced in 10.0.10240. |
| [ITfInputScope2](https://msdn.microsoft.com/library/windows/desktop/aa382054.aspx) | Introduced in 10.0.10240. |
| [ITfKeyEventSink](https://msdn.microsoft.com/library/windows/desktop/ms628601.aspx) | Introduced in 10.0.10240. |
| [ITfKeystrokeMgr](https://msdn.microsoft.com/library/windows/desktop/ms628676.aspx) | Introduced in 10.0.10240. |
| [ITfKeyTraceEventSink](https://msdn.microsoft.com/library/windows/desktop/ms628691.aspx) | Introduced in 10.0.10240. |
| [ITfLanguageProfileNotifySink](https://msdn.microsoft.com/library/windows/desktop/ms628769.aspx) | Introduced in 10.0.10240. |
| [ITfPersistentPropertyLoaderACP](https://msdn.microsoft.com/library/windows/desktop/ms628877.aspx) | Introduced in 10.0.10240. |
| [ITfPreservedKeyNotifySink](https://msdn.microsoft.com/library/windows/desktop/ms628879.aspx) | Introduced in 10.0.10240. |
| [ITfProperty](https://msdn.microsoft.com/library/windows/desktop/ms628891.aspx) | Introduced in 10.0.10240. |
| [ITfPropertyStore](https://msdn.microsoft.com/library/windows/desktop/ms628892.aspx) | Introduced in 10.0.10240. |
| [ITfRange](https://msdn.microsoft.com/library/windows/desktop/ms628908.aspx) | Introduced in 10.0.10240. |
| [ITfRangeACP](https://msdn.microsoft.com/library/windows/desktop/ms628909.aspx) | Introduced in 10.0.10240. |
| [ITfRangeBackup](https://msdn.microsoft.com/library/windows/desktop/ms628912.aspx) | Introduced in 10.0.10240. |
| [ITfReadingInformationUIElement](https://msdn.microsoft.com/library/windows/desktop/aa382576.aspx) | Introduced in 10.0.10240. |
| [ITfReadOnlyProperty](https://msdn.microsoft.com/library/windows/desktop/ms628936.aspx) | Introduced in 10.0.10240. |
| [ITfSource](https://msdn.microsoft.com/library/windows/desktop/ms628941.aspx) | Introduced in 10.0.10240. |
| [ITfSourceSingle](https://msdn.microsoft.com/library/windows/desktop/ms628942.aspx) | Introduced in 10.0.10240. |
| [ITfTextEditSink](https://msdn.microsoft.com/library/windows/desktop/ms628962.aspx) | Introduced in 10.0.10240. |
| [ITfThreadMgr2](https://msdn.microsoft.com/library/windows/desktop/hh920960.aspx) | Introduced in 10.0.10240. |
| [ITfUIElement](https://msdn.microsoft.com/library/windows/desktop/aa383175.aspx) | Introduced in 10.0.10240. |
| [ITfUIElementMgr](https://msdn.microsoft.com/library/windows/desktop/aa383178.aspx) | Introduced in 10.0.10240. |
| [ITfUIElementSink](https://msdn.microsoft.com/library/windows/desktop/aa383201.aspx) | Introduced in 10.0.10240. |
| [IThumbnailStreamCache](https://msdn.microsoft.com/library/windows/desktop/mt438734.aspx) | Introduced in 10.0.10240. |
| [IToggleProvider](https://msdn.microsoft.com/library/windows/desktop/ee671396.aspx) | Introduced in 10.0.10240. |
| [ITransformProvider](https://msdn.microsoft.com/library/windows/desktop/ee671399.aspx) | Introduced in 10.0.10240. |
| [ITransformProvider2](https://msdn.microsoft.com/library/windows/desktop/hh448824.aspx) | Introduced in 10.0.10240. |
| [IUIAnimationInterpolator](https://msdn.microsoft.com/library/windows/desktop/dd371665.aspx) | Introduced in 10.0.10240. |
| [IUIAnimationInterpolator2](https://msdn.microsoft.com/library/windows/desktop/hh437121.aspx) | Introduced in 10.0.10240. |
| [IUIAnimationLoopIterationChangeHandler2](https://msdn.microsoft.com/library/windows/desktop/hh437133.aspx) | Introduced in 10.0.10240. |
| [IUIAnimationManager](https://msdn.microsoft.com/library/windows/desktop/dd371687.aspx) | Introduced in 10.0.10240. |
| [IUIAnimationManager2](https://msdn.microsoft.com/library/windows/desktop/hh437135.aspx) | Introduced in 10.0.10240. |
| [IUIAnimationManagerEventHandler](https://msdn.microsoft.com/library/windows/desktop/dd371690.aspx) | Introduced in 10.0.10240. |
| [IUIAnimationManagerEventHandler2](https://msdn.microsoft.com/library/windows/desktop/hh437172.aspx) | Introduced in 10.0.10240. |
| [IUIAnimationPrimitiveInterpolation](https://msdn.microsoft.com/library/windows/desktop/hh437174.aspx) | Introduced in 10.0.10240. |
| [IUIAnimationPriorityComparison](https://msdn.microsoft.com/library/windows/desktop/dd371757.aspx) | Introduced in 10.0.10240. |
| [IUIAnimationPriorityComparison2](https://msdn.microsoft.com/library/windows/desktop/hh437176.aspx) | Introduced in 10.0.10240. |
| [IUIAnimationStoryboard](https://msdn.microsoft.com/library/windows/desktop/dd371761.aspx) | Introduced in 10.0.10240. |
| [IUIAnimationStoryboard2](https://msdn.microsoft.com/library/windows/desktop/hh437178.aspx) | Introduced in 10.0.10240. |
| [IUIAnimationStoryboardEventHandler](https://msdn.microsoft.com/library/windows/desktop/dd371764.aspx) | Introduced in 10.0.10240. |
| [IUIAnimationStoryboardEventHandler2](https://msdn.microsoft.com/library/windows/desktop/hh448599.aspx) | Introduced in 10.0.10240. |
| [IUIAnimationTimer](https://msdn.microsoft.com/library/windows/desktop/dd371831.aspx) | Introduced in 10.0.10240. |
| [IUIAnimationTimerClientEventHandler](https://msdn.microsoft.com/library/windows/desktop/dd371834.aspx) | Introduced in 10.0.10240. |
| [IUIAnimationTimerEventHandler](https://msdn.microsoft.com/library/windows/desktop/dd371841.aspx) | Introduced in 10.0.10240. |
| [IUIAnimationTimerUpdateHandler](https://msdn.microsoft.com/library/windows/desktop/dd371853.aspx) | Introduced in 10.0.10240. |
| [IUIAnimationTransition](https://msdn.microsoft.com/library/windows/desktop/dd371887.aspx) | Introduced in 10.0.10240. |
| [IUIAnimationTransition2](https://msdn.microsoft.com/library/windows/desktop/hh448602.aspx) | Introduced in 10.0.10240. |
| [IUIAnimationTransitionFactory](https://msdn.microsoft.com/library/windows/desktop/dd371891.aspx) | Introduced in 10.0.10240. |
| [IUIAnimationTransitionFactory2](https://msdn.microsoft.com/library/windows/desktop/hh448610.aspx) | Introduced in 10.0.10240. |
| [IUIAnimationTransitionLibrary](https://msdn.microsoft.com/library/windows/desktop/dd371897.aspx) | Introduced in 10.0.10240. |
| [IUIAnimationTransitionLibrary2](https://msdn.microsoft.com/library/windows/desktop/hh448612.aspx) | Introduced in 10.0.10240. |
| [IUIAnimationVariable](https://msdn.microsoft.com/library/windows/desktop/dd316797.aspx) | Introduced in 10.0.10240. |
| [IUIAnimationVariable2](https://msdn.microsoft.com/library/windows/desktop/hh448632.aspx) | Introduced in 10.0.10240. |
| [IUIAnimationVariableChangeHandler](https://msdn.microsoft.com/library/windows/desktop/dd316806.aspx) | Introduced in 10.0.10240. |
| [IUIAnimationVariableChangeHandler2](https://msdn.microsoft.com/library/windows/desktop/hh448659.aspx) | Introduced in 10.0.10240. |
| [IUIAnimationVariableCurveChangeHandler2](https://msdn.microsoft.com/library/windows/desktop/hh448661.aspx) | Introduced in 10.0.10240. |
| [IUIAnimationVariableIntegerChangeHandler](https://msdn.microsoft.com/library/windows/desktop/dd316819.aspx) | Introduced in 10.0.10240. |
| [IUIAnimationVariableIntegerChangeHandler2](https://msdn.microsoft.com/library/windows/desktop/hh448663.aspx) | Introduced in 10.0.10240. |
| [IUIAutomationPatternHandler](https://msdn.microsoft.com/library/windows/desktop/ee696113.aspx) | Introduced in 10.0.10240. |
| [IUIAutomationPatternInstance](https://msdn.microsoft.com/library/windows/desktop/ee696116.aspx) | Introduced in 10.0.10240. |
| [IUIAutomationRegistrar](https://msdn.microsoft.com/library/windows/desktop/ee696161.aspx) | Introduced in 10.0.10240. |
| [IUnknown](https://msdn.microsoft.com/library/windows/desktop/ms680509.aspx) | Introduced in 10.0.10240. |
| [IValueProvider](https://msdn.microsoft.com/library/windows/desktop/ee671565.aspx) | Introduced in 10.0.10240. |
| [IVideoFrameNative](https://msdn.microsoft.com/library/windows/desktop/mt431704.aspx) | Introduced in 10.0.10240. |
| [IVideoFrameNativeFactory](https://msdn.microsoft.com/library/windows/desktop/mt431705.aspx) | Introduced in 10.0.10240. |
| [IVirtualizedItemProvider](https://msdn.microsoft.com/library/windows/desktop/ee671569.aspx) | Introduced in 10.0.10240. |
| [IVirtualSurfaceImageSourceNative](https://msdn.microsoft.com/library/windows/desktop/hh848328.aspx) | Introduced in 10.0.10240. |
| [IVirtualSurfaceUpdatesCallbackNative](https://msdn.microsoft.com/library/windows/desktop/hh848336.aspx) | Introduced in 10.0.10240. |
| [IWeakReference](https://msdn.microsoft.com/library/windows/desktop/br224608.aspx) | Introduced in 10.0.10240. |
| [IWeakReferenceSource](https://msdn.microsoft.com/library/windows/desktop/br224609.aspx) | Introduced in 10.0.10240. |
| [IWICBitmap](https://msdn.microsoft.com/library/windows/desktop/ee719675.aspx) | Introduced in 10.0.10240. |
| [IWICBitmapClipper](https://msdn.microsoft.com/library/windows/desktop/ee719676.aspx) | Introduced in 10.0.10240. |
| [IWICBitmapCodecInfo](https://msdn.microsoft.com/library/windows/desktop/ee719679.aspx) | Introduced in 10.0.10240. |
| [IWICBitmapCodecProgressNotification](https://msdn.microsoft.com/library/windows/desktop/ee690084.aspx) | Introduced in 10.0.10240. |
| [IWICBitmapDecoder](https://msdn.microsoft.com/library/windows/desktop/ee690086.aspx) | Introduced in 10.0.10240. |
| [IWICBitmapDecoderInfo](https://msdn.microsoft.com/library/windows/desktop/ee690087.aspx) | Introduced in 10.0.10240. |
| [IWICBitmapEncoder](https://msdn.microsoft.com/library/windows/desktop/ee690110.aspx) | Introduced in 10.0.10240. |
| [IWICBitmapEncoderInfo](https://msdn.microsoft.com/library/windows/desktop/ee690112.aspx) | Introduced in 10.0.10240. |
| [IWICBitmapFlipRotator](https://msdn.microsoft.com/library/windows/desktop/ee690131.aspx) | Introduced in 10.0.10240. |
| [IWICBitmapFrameDecode](https://msdn.microsoft.com/library/windows/desktop/ee690134.aspx) | Introduced in 10.0.10240. |
| [IWICBitmapFrameEncode](https://msdn.microsoft.com/library/windows/desktop/ee690141.aspx) | Introduced in 10.0.10240. |
| [IWICBitmapLock](https://msdn.microsoft.com/library/windows/desktop/ee690161.aspx) | Introduced in 10.0.10240. |
| [IWICBitmapScaler](https://msdn.microsoft.com/library/windows/desktop/ee690168.aspx) | Introduced in 10.0.10240. |
| [IWICBitmapSource](https://msdn.microsoft.com/library/windows/desktop/ee690171.aspx) | Introduced in 10.0.10240. |
| [IWICBitmapSourceTransform](https://msdn.microsoft.com/library/windows/desktop/ee690172.aspx) | Introduced in 10.0.10240. |
| [IWICColorContext](https://msdn.microsoft.com/library/windows/desktop/ee690193.aspx) | Introduced in 10.0.10240. |
| [IWICColorTransform](https://msdn.microsoft.com/library/windows/desktop/ee690201.aspx) | Introduced in 10.0.10240. |
| [IWICComponentFactory](https://msdn.microsoft.com/library/windows/desktop/ee690203.aspx) | Introduced in 10.0.10240. |
| [IWICComponentInfo](https://msdn.microsoft.com/library/windows/desktop/ee690213.aspx) | Introduced in 10.0.10240. |
| [IWICDevelopRaw](https://msdn.microsoft.com/library/windows/desktop/ee690228.aspx) | Introduced in 10.0.10240. |
| [IWICDevelopRawNotificationCallback](https://msdn.microsoft.com/library/windows/desktop/ee690229.aspx) | Introduced in 10.0.10240. |
| [IWICEnumMetadataItem](https://msdn.microsoft.com/library/windows/desktop/ee690264.aspx) | Introduced in 10.0.10240. |
| [IWICFastMetadataEncoder](https://msdn.microsoft.com/library/windows/desktop/ee690269.aspx) | Introduced in 10.0.10240. |
| [IWICFormatConverter](https://msdn.microsoft.com/library/windows/desktop/ee690274.aspx) | Introduced in 10.0.10240. |
| [IWICFormatConverterInfo](https://msdn.microsoft.com/library/windows/desktop/ee690275.aspx) | Introduced in 10.0.10240. |
| [IWICImageEncoder](https://msdn.microsoft.com/library/windows/desktop/hh880844.aspx) | Introduced in 10.0.10240. |
| [IWICImagingFactory](https://msdn.microsoft.com/library/windows/desktop/ee690281.aspx) | Introduced in 10.0.10240. |
| [IWICImagingFactory2](https://msdn.microsoft.com/library/windows/desktop/hh880848.aspx) | Introduced in 10.0.10240. |
| [IWICMetadataBlockReader](https://msdn.microsoft.com/library/windows/desktop/ee690327.aspx) | Introduced in 10.0.10240. |
| [IWICMetadataBlockWriter](https://msdn.microsoft.com/library/windows/desktop/ee690335.aspx) | Introduced in 10.0.10240. |
| [IWICMetadataHandlerInfo](https://msdn.microsoft.com/library/windows/desktop/ee719700.aspx) | Introduced in 10.0.10240. |
| [IWICMetadataQueryReader](https://msdn.microsoft.com/library/windows/desktop/ee719708.aspx) | Introduced in 10.0.10240. |
| [IWICMetadataQueryWriter](https://msdn.microsoft.com/library/windows/desktop/ee719717.aspx) | Introduced in 10.0.10240. |
| [IWICMetadataReader](https://msdn.microsoft.com/library/windows/desktop/ee719722.aspx) | Introduced in 10.0.10240. |
| [IWICMetadataReaderInfo](https://msdn.microsoft.com/library/windows/desktop/ee719723.aspx) | Introduced in 10.0.10240. |
| [IWICMetadataWriter](https://msdn.microsoft.com/library/windows/desktop/ee719733.aspx) | Introduced in 10.0.10240. |
| [IWICMetadataWriterInfo](https://msdn.microsoft.com/library/windows/desktop/ee719734.aspx) | Introduced in 10.0.10240. |
| [IWICPalette](https://msdn.microsoft.com/library/windows/desktop/ee719741.aspx) | Introduced in 10.0.10240. |
| [IWICPersistStream](https://msdn.microsoft.com/library/windows/desktop/ee719760.aspx) | Introduced in 10.0.10240. |
| [IWICPixelFormatInfo](https://msdn.microsoft.com/library/windows/desktop/ee719763.aspx) | Introduced in 10.0.10240. |
| [IWICPixelFormatInfo2](https://msdn.microsoft.com/library/windows/desktop/ee719764.aspx) | Introduced in 10.0.10240. |
| [IWICProgressCallback](https://msdn.microsoft.com/library/windows/desktop/ee719775.aspx) | Introduced in 10.0.10240. |
| [IWICProgressiveLevelControl](https://msdn.microsoft.com/library/windows/desktop/ee719778.aspx) | Introduced in 10.0.10240. |
| [IWICStream](https://msdn.microsoft.com/library/windows/desktop/ee719782.aspx) | Introduced in 10.0.10240. |
| [IWICStreamProvider](https://msdn.microsoft.com/library/windows/desktop/ee719783.aspx) | Introduced in 10.0.10240. |
| [IWICDdsDecoder](https://msdn.microsoft.com/library/windows/desktop/dn302079.aspx) | Introduced in 10.0.10240. |
| [IWICDdsEncoder](https://msdn.microsoft.com/library/windows/desktop/dn302082.aspx) | Introduced in 10.0.10240. |
| [IWICDdsFrameDecode](https://msdn.microsoft.com/library/windows/desktop/dn302086.aspx) | Introduced in 10.0.10240. |
| [IWICPlanarBitmapFrameEncode](https://msdn.microsoft.com/library/windows/desktop/dn302090.aspx) | Introduced in 10.0.10240. |
| [IWICPlanarBitmapSourceTransform](https://msdn.microsoft.com/library/windows/desktop/dn302093.aspx) | Introduced in 10.0.10240. |
| [IWICPlanarFormatConverter](https://msdn.microsoft.com/library/windows/desktop/dn302096.aspx) | Introduced in 10.0.10240. |
| [IWICJpegFrameDecode](https://msdn.microsoft.com/library/windows/desktop/dn903834.aspx) | Introduced in 10.0.10240. |
| [IWICJpegFrameEncode](https://msdn.microsoft.com/library/windows/desktop/dn903864.aspx) | Introduced in 10.0.10240. |
| [IWindowProvider](https://msdn.microsoft.com/library/windows/desktop/ee671571.aspx) | Introduced in 10.0.10240. |
| [IWindowsDevicesAllJoynBusAttachmentFactoryInterop](https://msdn.microsoft.com/library/Mt573659(v=VS.85).aspx) | Introduced in 10.0.10240. |
| [IWindowsDevicesAllJoynBusAttachmentInterop](https://msdn.microsoft.com/library/Mt573661(v=VS.85).aspx) | Introduced in 10.0.10240. |
| IWorkspaceBrokerAx | Introduced in 10.0.10240. |
| IWorkspaceBrokerAx2 | Introduced in 10.0.10240. |
| [IXAPO](https://msdn.microsoft.com/library/windows/desktop/microsoft.directx_sdk.ixapo.ixapo.aspx) | Introduced in 10.0.10240. |
| [IXAPOHrtfParameters](https://msdn.microsoft.com/library/windows/desktop/mt186608.aspx) | Introduced in 10.0.10240. |
| [IXAPOParameters](https://msdn.microsoft.com/library/windows/desktop/microsoft.directx_sdk.ixapoparameters.ixapoparameters.aspx) | Introduced in 10.0.10240. |
| [IXAudio2](https://msdn.microsoft.com/library/windows/desktop/microsoft.directx_sdk.ixaudio2.ixaudio2.aspx) | Introduced in 10.0.10240. |
| [IXAudio2EngineCallback](https://msdn.microsoft.com/library/windows/desktop/microsoft.directx_sdk.ixaudio2enginecallback.ixaudio2enginecallback.aspx) | Introduced in 10.0.10240. |
| [IXAudio2MasteringVoice](https://msdn.microsoft.com/library/windows/desktop/microsoft.directx_sdk.ixaudio2masteringvoice.ixaudio2masteringvoice.aspx) | Introduced in 10.0.10240. |
| [IXAudio2SourceVoice](https://msdn.microsoft.com/library/windows/desktop/microsoft.directx_sdk.ixaudio2sourcevoice.ixaudio2sourcevoice.aspx) | Introduced in 10.0.10240. |
| [IXAudio2SubmixVoice](https://msdn.microsoft.com/library/windows/desktop/microsoft.directx_sdk.ixaudio2submixvoice.ixaudio2submixvoice.aspx) | Introduced in 10.0.10240. |
| [IXAudio2Voice](https://msdn.microsoft.com/library/windows/desktop/microsoft.directx_sdk.ixaudio2voice.ixaudio2voice.aspx) | Introduced in 10.0.10240. |
| [IXAudio2VoiceCallback](https://msdn.microsoft.com/library/windows/desktop/microsoft.directx_sdk.ixaudio2voicecallback.ixaudio2voicecallback.aspx) | Introduced in 10.0.10240. |
| [IXMLHTTPRequest2](https://msdn.microsoft.com/library/windows/desktop/hh831151.aspx) | Introduced in 10.0.10240. |
| [IXMLHTTPRequest2Callback](https://msdn.microsoft.com/library/windows/desktop/hh831152.aspx) | Introduced in 10.0.10240. |
| [IXMLHTTPRequest3](https://msdn.microsoft.com/library/windows/desktop/dn376398.aspx) | Introduced in 10.0.10240. |
| [IXMLHTTPRequest3Callback](https://msdn.microsoft.com/library/windows/desktop/dn376399.aspx) | Introduced in 10.0.10240. |
| [IXmlReader](https://msdn.microsoft.com/library/windows/desktop/ms752743.aspx) | Introduced in 10.0.10240. |
| [IXmlReaderInput](https://msdn.microsoft.com/library/windows/desktop/ms752817.aspx) | Introduced in 10.0.10240. |
| [IXmlResolver](https://msdn.microsoft.com/library/windows/desktop/ms752841.aspx) | Introduced in 10.0.10240. |
| [IXmlWriter](https://msdn.microsoft.com/library/windows/desktop/ms752860.aspx) | Introduced in 10.0.10240. |
| [IXmlWriterLite](https://msdn.microsoft.com/library/Mt143569(v=VS.85).aspx) | Introduced in 10.0.10240. |
| [IXmlWriterOutput](https://msdn.microsoft.com/library/windows/desktop/ms752843.aspx) | Introduced in 10.0.10240. |
| [IXpsDocumentPackageTarget](https://msdn.microsoft.com/library/windows/desktop/hh994456.aspx) | Introduced in 10.0.10240. |
| [IXpsDocumentPackageTarget3D](https://msdn.microsoft.com/library/windows/desktop/dn280684.aspx) | Introduced in 10.0.10240. |
| [IXpsOMBrush](https://msdn.microsoft.com/library/windows/desktop/dd317026.aspx) | Introduced in 10.0.10240. |
| [IXpsOMCanvas](https://msdn.microsoft.com/library/windows/desktop/dd317033.aspx) | Introduced in 10.0.10240. |
| [IXpsOMColorProfileResource](https://msdn.microsoft.com/library/windows/desktop/dd372020.aspx) | Introduced in 10.0.10240. |
| [IXpsOMColorProfileResourceCollection](https://msdn.microsoft.com/library/windows/desktop/dd372023.aspx) | Introduced in 10.0.10240. |
| [IXpsOMCoreProperties](https://msdn.microsoft.com/library/windows/desktop/dd372040.aspx) | Introduced in 10.0.10240. |
| [IXpsOMDashCollection](https://msdn.microsoft.com/library/windows/desktop/dd372105.aspx) | Introduced in 10.0.10240. |
| [IXpsOMDictionary](https://msdn.microsoft.com/library/windows/desktop/dd372128.aspx) | Introduced in 10.0.10240. |
| [IXpsOMDocument](https://msdn.microsoft.com/library/windows/desktop/dd372155.aspx) | Introduced in 10.0.10240. |
| [IXpsOMDocumentCollection](https://msdn.microsoft.com/library/windows/desktop/dd372157.aspx) | Introduced in 10.0.10240. |
| [IXpsOMDocumentSequence](https://msdn.microsoft.com/library/windows/desktop/dd372363.aspx) | Introduced in 10.0.10240. |
| [IXpsOMDocumentStructureResource](https://msdn.microsoft.com/library/windows/desktop/dd372377.aspx) | Introduced in 10.0.10240. |
| [IXpsOMFontResource](https://msdn.microsoft.com/library/windows/desktop/dd372415.aspx) | Introduced in 10.0.10240. |
| [IXpsOMFontResourceCollection](https://msdn.microsoft.com/library/windows/desktop/dd372419.aspx) | Introduced in 10.0.10240. |
| [IXpsOMGeometry](https://msdn.microsoft.com/library/windows/desktop/dd372455.aspx) | Introduced in 10.0.10240. |
| [IXpsOMGeometryFigure](https://msdn.microsoft.com/library/windows/desktop/dd372457.aspx) | Introduced in 10.0.10240. |
| [IXpsOMGeometryFigureCollection](https://msdn.microsoft.com/library/windows/desktop/dd372461.aspx) | Introduced in 10.0.10240. |
| [IXpsOMGlyphs](https://msdn.microsoft.com/library/windows/desktop/dd317087.aspx) | Introduced in 10.0.10240. |
| [IXpsOMGlyphsEditor](https://msdn.microsoft.com/library/windows/desktop/dd317088.aspx) | Introduced in 10.0.10240. |
| [IXpsOMGradientBrush](https://msdn.microsoft.com/library/windows/desktop/dd317230.aspx) | Introduced in 10.0.10240. |
| [IXpsOMGradientStop](https://msdn.microsoft.com/library/windows/desktop/dd317250.aspx) | Introduced in 10.0.10240. |
| [IXpsOMGradientStopCollection](https://msdn.microsoft.com/library/windows/desktop/dd317252.aspx) | Introduced in 10.0.10240. |
| [IXpsOMImageBrush](https://msdn.microsoft.com/library/windows/desktop/dd317277.aspx) | Introduced in 10.0.10240. |
| [IXpsOMImageResource](https://msdn.microsoft.com/library/windows/desktop/dd317289.aspx) | Introduced in 10.0.10240. |
| [IXpsOMImageResourceCollection](https://msdn.microsoft.com/library/windows/desktop/dd317291.aspx) | Introduced in 10.0.10240. |
| [IXpsOMLinearGradientBrush](https://msdn.microsoft.com/library/windows/desktop/dd317306.aspx) | Introduced in 10.0.10240. |
| [IXpsOMMatrixTransform](https://msdn.microsoft.com/library/windows/desktop/dd372495.aspx) | Introduced in 10.0.10240. |
| [IXpsOMNameCollection](https://msdn.microsoft.com/library/windows/desktop/dd372502.aspx) | Introduced in 10.0.10240. |
| [IXpsOMObjectFactory](https://msdn.microsoft.com/library/windows/desktop/dd372509.aspx) | Introduced in 10.0.10240. |
| [IXpsOMObjectFactory1](https://msdn.microsoft.com/library/windows/desktop/hh448399.aspx) | Introduced in 10.0.10240. |
| [IXpsOMPackage](https://msdn.microsoft.com/library/windows/desktop/dd372618.aspx) | Introduced in 10.0.10240. |
| [IXpsOMPackage1](https://msdn.microsoft.com/library/windows/desktop/hh448410.aspx) | Introduced in 10.0.10240. |
| [IXpsOMPackageTarget](https://msdn.microsoft.com/library/windows/desktop/ff970304.aspx) | Introduced in 10.0.10240. |
| [IXpsOMPackageWriter](https://msdn.microsoft.com/library/windows/desktop/dd372619.aspx) | Introduced in 10.0.10240. |
| [IXpsOMPackageWriter3D](https://msdn.microsoft.com/library/windows/desktop/dn280743.aspx) | Introduced in 10.0.10240. |
| [IXpsOMPage](https://msdn.microsoft.com/library/windows/desktop/dd372635.aspx) | Introduced in 10.0.10240. |
| [IXpsOMPage1](https://msdn.microsoft.com/library/windows/desktop/hh448414.aspx) | Introduced in 10.0.10240. |
| [IXpsOMPageReference](https://msdn.microsoft.com/library/windows/desktop/dd372636.aspx) | Introduced in 10.0.10240. |
| [IXpsOMPageReferenceCollection](https://msdn.microsoft.com/library/windows/desktop/dd372637.aspx) | Introduced in 10.0.10240. |
| [IXpsOMPart](https://msdn.microsoft.com/library/windows/desktop/dd372684.aspx) | Introduced in 10.0.10240. |
| [IXpsOMPartResources](https://msdn.microsoft.com/library/windows/desktop/dd372685.aspx) | Introduced in 10.0.10240. |
| [IXpsOMPartUriCollection](https://msdn.microsoft.com/library/windows/desktop/dd372690.aspx) | Introduced in 10.0.10240. |
| [IXpsOMPath](https://msdn.microsoft.com/library/windows/desktop/dd372699.aspx) | Introduced in 10.0.10240. |
| [IXpsOMPrintTicketResource](https://msdn.microsoft.com/library/windows/desktop/dd372740.aspx) | Introduced in 10.0.10240. |
| [IXpsOMRadialGradientBrush](https://msdn.microsoft.com/library/windows/desktop/dd372743.aspx) | Introduced in 10.0.10240. |
| [IXpsOMRemoteDictionaryResource](https://msdn.microsoft.com/library/windows/desktop/dd372751.aspx) | Introduced in 10.0.10240. |
| [IXpsOMRemoteDictionaryResource1](https://msdn.microsoft.com/library/windows/desktop/jj159899.aspx) | Introduced in 10.0.10240. |
| [IXpsOMRemoteDictionaryResourceCollection](https://msdn.microsoft.com/library/windows/desktop/dd372752.aspx) | Introduced in 10.0.10240. |
| [IXpsOMResource](https://msdn.microsoft.com/library/windows/desktop/dd372762.aspx) | Introduced in 10.0.10240. |
| [IXpsOMShareable](https://msdn.microsoft.com/library/windows/desktop/dd372763.aspx) | Introduced in 10.0.10240. |
| [IXpsOMSignatureBlockResource](https://msdn.microsoft.com/library/windows/desktop/dd372766.aspx) | Introduced in 10.0.10240. |
| [IXpsOMSignatureBlockResourceCollection](https://msdn.microsoft.com/library/windows/desktop/dd372767.aspx) | Introduced in 10.0.10240. |
| [IXpsOMSolidColorBrush](https://msdn.microsoft.com/library/windows/desktop/dd372779.aspx) | Introduced in 10.0.10240. |
| [IXpsOMStoryFragmentsResource](https://msdn.microsoft.com/library/windows/desktop/dd372783.aspx) | Introduced in 10.0.10240. |
| [IXpsOMTileBrush](https://msdn.microsoft.com/library/windows/desktop/dd372789.aspx) | Introduced in 10.0.10240. |
| [IXpsOMVisual](https://msdn.microsoft.com/library/windows/desktop/dd372801.aspx) | Introduced in 10.0.10240. |
| [IXpsOMVisualBrush](https://msdn.microsoft.com/library/windows/desktop/dd372802.aspx) | Introduced in 10.0.10240. |
| [IXpsOMVisualCollection](https://msdn.microsoft.com/library/windows/desktop/dd372809.aspx) | Introduced in 10.0.10240. |
| IBtRadioController | Introduced in 10.0.10586. |
| IBtCommandCallback | Introduced in 10.0.10586. |
| IBtConnectionObserver | Introduced in 10.0.10586. |
| IBtConnectionObserverCallback | Introduced in 10.0.10586. |
| IBtConnectionObserverCallback2 | Introduced in 10.0.10586. |
| IBtPairingRequest | Introduced in 10.0.10586. |
| IBtPairingRequestCallback | Introduced in 10.0.10586. |
| IBtIncomingPairingCallback | Introduced in 10.0.10586. |
| [ID3D11Device4](https://msdn.microsoft.com/library/windows/desktop/mt589889.aspx) | Introduced in 10.0.10586. |
| [IAppxBlockMapBlock](https://msdn.microsoft.com/library/windows/desktop/hh446630.aspx) | Introduced in 10.0.14393. |
| [IAppxBlockMapBlocksEnumerator](https://msdn.microsoft.com/library/windows/desktop/hh446631.aspx) | Introduced in 10.0.14393. |
| [IAppxBlockMapFile](https://msdn.microsoft.com/library/windows/desktop/hh446637.aspx) | Introduced in 10.0.14393. |
| [IAppxBlockMapFilesEnumerator](https://msdn.microsoft.com/library/windows/desktop/hh446638.aspx) | Introduced in 10.0.14393. |
| [IAppxBlockMapReader](https://msdn.microsoft.com/library/windows/desktop/hh446651.aspx) | Introduced in 10.0.14393. |
| [IAppxBundleFactory](https://msdn.microsoft.com/library/windows/desktop/dn280277.aspx) | Introduced in 10.0.14393. |
| [IAppxBundleWriter](https://msdn.microsoft.com/library/windows/desktop/dn280302.aspx) | Introduced in 10.0.14393. |
| [IAppxBundleReader](https://msdn.microsoft.com/library/windows/desktop/dn280296.aspx) | Introduced in 10.0.14393. |
| [IAppxBundleManifestReader](https://msdn.microsoft.com/library/windows/desktop/dn280292.aspx) | Introduced in 10.0.14393. |
| [IAppxBundleManifestPackageInfoEnumerator](https://msdn.microsoft.com/library/windows/desktop/dn280282.aspx) | Introduced in 10.0.14393. |
| [IAppxBundleManifestPackageInfo](https://msdn.microsoft.com/library/windows/desktop/dn280281.aspx) | Introduced in 10.0.14393. |
| [IAppxFactory](https://msdn.microsoft.com/library/windows/desktop/hh446671.aspx) | Introduced in 10.0.14393. |
| [IAppxFile](https://msdn.microsoft.com/library/windows/desktop/hh446683.aspx) | Introduced in 10.0.14393. |
| [IAppxFilesEnumerator](https://msdn.microsoft.com/library/windows/desktop/hh446685.aspx) | Introduced in 10.0.14393. |
| [IAppxManifestApplication](https://msdn.microsoft.com/library/windows/desktop/hh446697.aspx) | Introduced in 10.0.14393. |
| [IAppxManifestApplicationsEnumerator](https://msdn.microsoft.com/library/windows/desktop/hh446698.aspx) | Introduced in 10.0.14393. |
| [IAppxManifestQualifiedResource](https://msdn.microsoft.com/library/windows/desktop/dn280305.aspx) | Introduced in 10.0.14393. |
| [IAppxManifestQualifiedResourcesEnumerator](https://msdn.microsoft.com/library/windows/desktop/dn280306.aspx) | Introduced in 10.0.14393. |
| [IAppxPackageReader](https://msdn.microsoft.com/library/windows/desktop/hh446756.aspx) | Introduced in 10.0.14393. |
| [IAppxPackageWriter](https://msdn.microsoft.com/library/windows/desktop/hh446762.aspx) | Introduced in 10.0.14393. |
| [IAppxManifestDeviceCapabilitiesEnumerator](https://msdn.microsoft.com/library/windows/desktop/hh446704.aspx) | Introduced in 10.0.14393. |
| [IAppxManifestPackageId](https://msdn.microsoft.com/library/windows/desktop/hh446717.aspx) | Introduced in 10.0.14393. |
| [IAppxManifestPackageDependency](https://msdn.microsoft.com/library/windows/desktop/hh446713.aspx) | Introduced in 10.0.14393. |
| [IAppxManifestPackageDependenciesEnumerator](https://msdn.microsoft.com/library/windows/desktop/hh446708.aspx) | Introduced in 10.0.14393. |
| [IAppxManifestProperties](https://msdn.microsoft.com/library/windows/desktop/hh446731.aspx) | Introduced in 10.0.14393. |
| [IAppxManifestReader](https://msdn.microsoft.com/library/windows/desktop/hh446737.aspx) | Introduced in 10.0.14393. |
| [IAppxManifestReader2](https://msdn.microsoft.com/library/windows/desktop/dn280312.aspx) | Introduced in 10.0.14393. |
| [IAppxManifestReader3](https://msdn.microsoft.com/library/Mt796945(v=VS.85).aspx) | Introduced in 10.0.14393. |
| [IAppxManifestCapabilitiesEnumerator](https://msdn.microsoft.com/library/Mt796938(v=VS.85).aspx) | Introduced in 10.0.14393. |
| [IAppxManifestTargetDeviceFamiliesEnumerator](https://msdn.microsoft.com/library/Mt796950(v=VS.85).aspx) | Introduced in 10.0.14393. |
| [IAppxManifestTargetDeviceFamily](https://msdn.microsoft.com/library/Mt796954(v=VS.85).aspx) | Introduced in 10.0.14393. |
| [IAppxManifestPackageDependency2](https://msdn.microsoft.com/library/Mt845795(v=VS.85).aspx) | Introduced in 10.0.14393. |
| [IAppxManifestResourcesEnumerator](https://msdn.microsoft.com/library/windows/desktop/hh446752.aspx) | Introduced in 10.0.14393. |
| [IAppxManifestReader4](https://msdn.microsoft.com/library/Mt796948(v=VS.85).aspx) | Introduced in 10.0.14393. |
| [IAppxManifestOptionalPackageInfo](https://msdn.microsoft.com/library/Mt796942(v=VS.85).aspx) | Introduced in 10.0.14393. |
| [IXblIdpAuthManager](https://msdn.microsoft.com/library/Mt709230(v=VS.85).aspx) | Introduced in 10.0.14393. |
| [IXblIdpAuthTokenResult](https://msdn.microsoft.com/library/Mt709237(v=VS.85).aspx) | Introduced in 10.0.14393. |
| [IAudioFormatEnumerator](https://msdn.microsoft.com/library/Mt779256(v=VS.85).aspx) | Introduced in 10.0.16299. |
| [ID2D1CommandSink3](https://msdn.microsoft.com/library/Mt619822(v=VS.85).aspx) | Introduced in 10.0.16299. |
| [ID2D1CommandSink4](https://msdn.microsoft.com/library/Mt797801(v=VS.85).aspx) | Introduced in 10.0.16299. |
| [ID2D1Device3](https://msdn.microsoft.com/library/Mt619824(v=VS.85).aspx) | Introduced in 10.0.16299. |
| [ID2D1Device4](https://msdn.microsoft.com/library/Mt736464(v=VS.85).aspx) | Introduced in 10.0.16299. |
| [ID2D1Device5](https://msdn.microsoft.com/library/Mt797803(v=VS.85).aspx) | Introduced in 10.0.16299. |
| [ID2D1DeviceContext3](https://msdn.microsoft.com/library/Mt619826(v=VS.85).aspx) | Introduced in 10.0.16299. |
| [ID2D1DeviceContext4](https://msdn.microsoft.com/library/Mt736468(v=VS.85).aspx) | Introduced in 10.0.16299. |
| [ID2D1DeviceContext5](https://msdn.microsoft.com/library/Mt797806(v=VS.85).aspx) | Introduced in 10.0.16299. |
| [ID2D1Factory4](https://msdn.microsoft.com/library/Mt619831(v=VS.85).aspx) | Introduced in 10.0.16299. |
| [ID2D1Factory5](https://msdn.microsoft.com/library/Mt750191(v=VS.85).aspx) | Introduced in 10.0.16299. |
| [ID2D1Factory6](https://msdn.microsoft.com/library/Mt797812(v=VS.85).aspx) | Introduced in 10.0.16299. |
| [ID2D1SpriteBatch](https://msdn.microsoft.com/library/Mt619833(v=VS.85).aspx) | Introduced in 10.0.16299. |
| [ID2D1SvgAttribute](https://msdn.microsoft.com/library/Mt797814(v=VS.85).aspx) | Introduced in 10.0.16299. |
| [ID2D1SvgDocument](https://msdn.microsoft.com/library/Mt797817(v=VS.85).aspx) | Introduced in 10.0.16299. |
| [ID2D1SvgElement](https://msdn.microsoft.com/library/Mt797830(v=VS.85).aspx) | Introduced in 10.0.16299. |
| [ID2D1SvgGlyphStyle](https://msdn.microsoft.com/library/Mt750193(v=VS.85).aspx) | Introduced in 10.0.16299. |
| [ID2D1SvgPaint](https://msdn.microsoft.com/library/Mt797893(v=VS.85).aspx) | Introduced in 10.0.16299. |
| [ID2D1SvgPathData](https://msdn.microsoft.com/library/Mt797902(v=VS.85).aspx) | Introduced in 10.0.16299. |
| [ID2D1SvgPointCollection](https://msdn.microsoft.com/library/Mt797912(v=VS.85).aspx) | Introduced in 10.0.16299. |
| [ID2D1SvgStrokeDashArray](https://msdn.microsoft.com/library/Mt797917(v=VS.85).aspx) | Introduced in 10.0.16299. |
| [IDXGIAdapter4](https://msdn.microsoft.com/library/Mt825229(v=VS.85).aspx) | Introduced in 10.0.16299. |
| [IMFSpatialAudioObjectBuffer](https://msdn.microsoft.com/library/Mt797969(v=VS.85).aspx) | Introduced in 10.0.16299. |
| [IMFSpatialAudioSample](https://msdn.microsoft.com/library/Mt797975(v=VS.85).aspx) | Introduced in 10.0.16299. |
| [IOplockBreakingHandler](https://msdn.microsoft.com/library/Mt743185(v=VS.85).aspx) | Introduced in 10.0.16299. |
| [ISpatialAudioObject](https://msdn.microsoft.com/library/Mt779268(v=VS.85).aspx) | Introduced in 10.0.16299. |
| [ISpatialAudioObjectRenderStream](https://msdn.microsoft.com/library/Mt779280(v=VS.85).aspx) | Introduced in 10.0.16299. |
| [ISpatialAudioObjectRenderStreamNotify](https://msdn.microsoft.com/library/Mt779281(v=VS.85).aspx) | Introduced in 10.0.16299. |
| [ISpatialAudioClient](https://msdn.microsoft.com/library/Mt779259(v=VS.85).aspx) | Introduced in 10.0.16299. |
| [IStorageItemHandleAccess](https://msdn.microsoft.com/library/Mt765063(v=VS.85).aspx) | Introduced in 10.0.16299. |
| [IStorageFolderHandleAccess](https://msdn.microsoft.com/library/Mt765061(v=VS.85).aspx) | Introduced in 10.0.16299. |
| IRemoteSystemAdditionalInfoProvider | Introduced in 10.0.17134. |
| IDesktopWindowXamlSourceNative | Introduced in 10.0.17763. |
| ILearningModelDeviceFactoryNative | Introduced in 10.0.17763. |
| ILearningModelOperatorProviderNative | Introduced in 10.0.17763. |
| ITensorNative | Introduced in 10.0.17763. |
| ITensorStaticsNative | Introduced in 10.0.17763. |


COM coclasses

| API | Requirements |
| -----| --------------|
| AudioReverb | Introduced in 10.0.10240. |
| AudioVolumeMeter | Introduced in 10.0.10240. |
| AoWAppActivatedRuntime | Introduced in 10.0.10240. Removed in 10.0.16299. |
| AoWBackgroundTaskRuntime | Introduced in 10.0.10240. Removed in 10.0.16299. |
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
| [RDPSession](https://msdn.microsoft.com/library/Mt446078(v=VS.85).aspx) | Introduced in 10.0.10240. |
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
| WorkspaceBrokerAx | Introduced in 10.0.10240. |
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


