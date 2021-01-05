---

description: This topic lists the Win32 and COM APIs that are part of the Universal Windows Platform (UWP) and that are implemented by some Windows 10 devices.
title: Extension APIs for Windows 10 devices (grouped by module)

ms.topic: article


keywords: windows 10, uwp, win32, COM
ms.date: 1/4/2021
ms.assetid: e8d54f37-9969-4f33-8b1b-fcb3d659c507
---

# Extension APIs for Windows 10 devices
This topic lists the Win32 and COM APIs that are part of the Universal Windows Platform (UWP) and that are implemented by some Windows 10 devices, so your calls to these APIs must be guarded with conditions that first confirm the presence of the API on the device your app is running on. The union of [APIs present on all Windows 10 devices](win32-apis.md) and the APIs listed in this topic make up the entire Win32 and COM surface area of UWP.

This topic lists the APIs grouped by module (where the module is either an [API set](/windows/win32/apiindex/windows-umbrella-libraries#api_sets) or a dll). For delay load, use the module name.

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
| [BCryptCreateMultiHash](/windows/win32/api/bcrypt/nf-bcrypt-bcryptcreatemultihash) | Introduced into Bcrypt.dll in 10.0.10240. Removed in 10.0.10586. |
| [BCryptProcessMultiOperations](/windows/win32/api/bcrypt/nf-bcrypt-bcryptprocessmultioperations) | Introduced into Bcrypt.dll in 10.0.10240. Removed in 10.0.10586. |


## APIs from ole32.dll

| API | Requirements |
| -----| --------------|
| [BindMoniker](/windows/win32/api/objbase/nf-objbase-bindmoniker) | Introduced into ole32.dll in 10.0.10240. |
| [CoGetObject](/windows/win32/api/objbase/nf-objbase-cogetobject) | Introduced into ole32.dll in 10.0.10240. |
| [CreateAntiMoniker](/windows/win32/api/objbase/nf-objbase-createantimoniker) | Introduced into ole32.dll in 10.0.10240. |
| [CreateBindCtx](/windows/win32/api/objbase/nf-objbase-createbindctx) | Introduced into ole32.dll in 10.0.10240. |
| [CreateClassMoniker](/windows/win32/api/objbase/nf-objbase-createclassmoniker) | Introduced into ole32.dll in 10.0.10240. |
| [CreateFileMoniker](/windows/win32/api/objbase/nf-objbase-createfilemoniker) | Introduced into ole32.dll in 10.0.10240. |
| [CreateGenericComposite](/windows/win32/api/objbase/nf-objbase-creategenericcomposite) | Introduced into ole32.dll in 10.0.10240. |
| [CreateItemMoniker](/windows/win32/api/objbase/nf-objbase-createitemmoniker) | Introduced into ole32.dll in 10.0.10240. |
| [CreateObjrefMoniker](/windows/win32/api/objbase/nf-objbase-createobjrefmoniker) | Introduced into ole32.dll in 10.0.10240. |
| [CreatePointerMoniker](/windows/win32/api/objbase/nf-objbase-createpointermoniker) | Introduced into ole32.dll in 10.0.10240. |
| [GetClassFile](/windows/win32/api/objbase/nf-objbase-getclassfile) | Introduced into ole32.dll in 10.0.10240. |
| [IsEqualGUID](/windows/win32/api/guiddef/nf-guiddef-isequalguid) | Introduced into ole32.dll in 10.0.10240. |
| [MkParseDisplayName](/windows/win32/api/objbase/nf-objbase-mkparsedisplayname) | Introduced into ole32.dll in 10.0.10240. |
| [MonikerCommonPrefixWith](/windows/win32/api/objbase/nf-objbase-monikercommonprefixwith) | Introduced into ole32.dll in 10.0.10240. |
| [MonikerRelativePathTo](/windows/win32/api/objbase/nf-objbase-monikerrelativepathto) | Introduced into ole32.dll in 10.0.10240. |


## APIs from dmprocessxmlfiltered.dll

| API | Requirements |
| -----| --------------|
| [DMProcessConfigXMLFiltered](/windows/client-management/mdm/dmprocessconfigxmlfiltered) | Introduced into dmprocessxmlfiltered.dll in 10.0.10240. |


## APIs from iphlpapi.dll

| API | Requirements |
| -----| --------------|
| [GetAdaptersAddresses](/windows/win32/api/iphlpapi/nf-iphlpapi-getadaptersaddresses) | Introduced into iphlpapi.dll in 10.0.10240. Removed in 10.0.14393. |
| [FreeMibTable](/windows/win32/api/netioapi/nf-netioapi-freemibtable) | Introduced into iphlpapi.dll in 10.0.10586. Removed in 10.0.14393. |
| [GetBestRoute2](/windows/win32/api/netioapi/nf-netioapi-getbestroute2) | Introduced into iphlpapi.dll in 10.0.10586. Removed in 10.0.14393. |
| [GetUnicastIpAddressTable](/windows/win32/api/netioapi/nf-netioapi-getunicastipaddresstable) | Introduced into iphlpapi.dll in 10.0.10586. Removed in 10.0.14393. |


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
| [InterlockedCompareExchange](/windows/win32/direct3dhlsl/interlockedcompareexchange) | Introduced into kernel32.dll in 10.0.10240. Removed in 10.0.16299. |
| [InterlockedCompareExchange64](/windows/win32/api/winnt/nf-winnt-interlockedcompareexchange64) | Introduced into kernel32.dll in 10.0.10240. Removed in 10.0.16299. |
| [InterlockedDecrement](/windows/win32/api/winnt/nf-winnt-interlockeddecrement) | Introduced into kernel32.dll in 10.0.10240. Removed in 10.0.16299. |
| [InterlockedExchange](/windows/win32/direct3dhlsl/interlockedexchange) | Introduced into kernel32.dll in 10.0.10240. Removed in 10.0.16299. |
| [InterlockedExchangeAdd](/windows/win32/api/winnt/nf-winnt-interlockedexchangeadd) | Introduced into kernel32.dll in 10.0.10240. Removed in 10.0.16299. |
| [InterlockedIncrement](/windows/win32/api/winnt/nf-winnt-interlockedincrement) | Introduced into kernel32.dll in 10.0.10240. Removed in 10.0.16299. |
| [GetModuleBaseNameA](/windows/win32/api/psapi/nf-psapi-getmodulebasenamea) | Introduced into kernel32.dll in 10.0.16299. |
| [GetModuleBaseNameW](/windows/win32/api/psapi/nf-psapi-getmodulebasenamea) | Introduced into kernel32.dll in 10.0.16299. |
| [GetModuleFileNameExA](/windows/win32/api/psapi/nf-psapi-getmodulefilenameexa) | Introduced into kernel32.dll in 10.0.16299. |
| [GetModuleFileNameExW](/windows/win32/api/psapi/nf-psapi-getmodulefilenameexa) | Introduced into kernel32.dll in 10.0.16299. |
| [GetModuleInformation](/windows/win32/api/psapi/nf-psapi-getmoduleinformation) | Introduced into kernel32.dll in 10.0.16299. |
| [SetEnvironmentVariable](/windows/win32/api/processenv/nf-processenv-setenvironmentvariablea) | Introduced into kernel32.dll in 10.0.16299. Moved into api-ms-win-core-processenvironment-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-processenvironment-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Removed in 10.0.17134. |
| [GetModuleFileNameEx](/windows/win32/api/psapi/nf-psapi-getmodulefilenameexa) | Introduced into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [VerLanguageName](/windows/win32/api/winver/nf-winver-verlanguagenamea) | Introduced into kernel32.dll in 10.0.16299. Moved into api-ms-win-core-localization-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-localization-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-localization-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-core-localization-l1-2-2.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from kernelbase.dll

| API | Requirements |
| -----| --------------|
| [GetProcessMemoryInfo](/windows/win32/api/psapi/nf-psapi-getprocessmemoryinfo) | Introduced into kernelbase.dll in 10.0.10240. Removed in 10.0.14393. Moved into kernel32.dll in 10.0.16299. |


## APIs from elscore.dll

| API | Requirements |
| -----| --------------|
| [MappingFreePropertyBag](/windows/win32/api/elscore/nf-elscore-mappingfreepropertybag) | Introduced into elscore.dll in 10.0.10240. |
| [MappingFreeServices](/windows/win32/api/elscore/nf-elscore-mappingfreeservices) | Introduced into elscore.dll in 10.0.10240. |
| [MappingGetServices](/windows/win32/api/elscore/nf-elscore-mappinggetservices) | Introduced into elscore.dll in 10.0.10240. |
| [MappingRecognizeText](/windows/win32/api/elscore/nf-elscore-mappingrecognizetext) | Introduced into elscore.dll in 10.0.10240. |


## APIs from rpcrt4.dll

| API | Requirements |
| -----| --------------|
| [NdrAsyncClientCall2](/windows/win32/api/rpcndr/nf-rpcndr-ndrasyncclientcall2) | Introduced into rpcrt4.dll in 10.0.10240. Removed in 10.0.16299. |
| [NdrClientCall4](/windows/win32/api/rpcndr/nf-rpcndr-ndrclientcall4) | Introduced into rpcrt4.dll in 10.0.10240. Removed in 10.0.16299. |
| [DceErrorInqText](/windows/win32/api/rpcdce/nf-rpcdce-dceerrorinqtext) | Introduced into rpcrt4.dll in 10.0.16299. Removed in 10.0.17134. |
| [RpcBindingCreate](/windows/win32/api/rpcdce/nf-rpcdce-rpcbindingcreatea) | Introduced into rpcrt4.dll in 10.0.16299. Removed in 10.0.17134. |
| [RpcBindingFromStringBinding](/windows/win32/api/rpcdce/nf-rpcdce-rpcbindingfromstringbinding) | Introduced into rpcrt4.dll in 10.0.16299. Removed in 10.0.17134. |
| [RpcBindingInqAuthInfo](/windows/win32/api/rpcdce/nf-rpcdce-rpcbindinginqauthinfo) | Introduced into rpcrt4.dll in 10.0.16299. Removed in 10.0.17134. |
| [RpcBindingInqAuthInfoEx](/windows/win32/api/rpcdce/nf-rpcdce-rpcbindinginqauthinfoexa) | Introduced into rpcrt4.dll in 10.0.16299. Removed in 10.0.17134. |
| [RpcBindingSetAuthInfo](/windows/win32/api/rpcdce/nf-rpcdce-rpcbindingsetauthinfo) | Introduced into rpcrt4.dll in 10.0.16299. Removed in 10.0.17134. |
| [RpcBindingSetAuthInfoEx](/windows/win32/api/rpcdce/nf-rpcdce-rpcbindingsetauthinfoexa) | Introduced into rpcrt4.dll in 10.0.16299. Removed in 10.0.17134. |
| [RpcBindingToStringBinding](/windows/win32/api/rpcdce/nf-rpcdce-rpcbindingtostringbinding) | Introduced into rpcrt4.dll in 10.0.16299. Removed in 10.0.17134. |
| [RpcMgmtInqServerPrincName](/windows/win32/api/rpcdce/nf-rpcdce-rpcmgmtinqserverprincname) | Introduced into rpcrt4.dll in 10.0.16299. Removed in 10.0.17134. |
| [RpcNetworkIsProtseqValid](/windows/win32/api/rpcdce/nf-rpcdce-rpcnetworkisprotseqvalid) | Introduced into rpcrt4.dll in 10.0.16299. Removed in 10.0.17134. |
| [RpcStringBindingCompose](/windows/win32/api/rpcdce/nf-rpcdce-rpcstringbindingcompose) | Introduced into rpcrt4.dll in 10.0.16299. Removed in 10.0.17134. |
| [RpcStringBindingParse](/windows/win32/api/rpcdce/nf-rpcdce-rpcstringbindingparse) | Introduced into rpcrt4.dll in 10.0.16299. Removed in 10.0.17134. |
| [RpcStringFree](/windows/win32/api/rpcdce/nf-rpcdce-rpcstringfree) | Introduced into rpcrt4.dll in 10.0.16299. Removed in 10.0.17134. |
| [UuidFromString](/windows/win32/api/rpcdce/nf-rpcdce-uuidfromstring) | Introduced into rpcrt4.dll in 10.0.16299. Removed in 10.0.17134. |
| [UuidToString](/windows/win32/api/rpcdce/nf-rpcdce-uuidtostring) | Introduced into rpcrt4.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from windows.data.pdf.dll

| API | Requirements |
| -----| --------------|
| [PdfRenderParams](/windows/win32/api/windows.data.pdf.interop/nf-windows-data-pdf-interop-pdfrenderparams) | Introduced into windows.data.pdf.dll in 10.0.10240. Removed in 10.0.14393. |


## APIs from api-ms-win-core-slapi-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [SLQueryLicenseValueFromApp](/windows/win32/api/slpublic/nf-slpublic-slquerylicensevaluefromapp) | Introduced into api-ms-win-core-slapi-l1-1-0.dll in 10.0.10240. Removed in 10.0.14393. |
| SLQueryLicenseValueFromApp2 | Introduced into api-ms-win-core-slapi-l1-1-0.dll in 10.0.10240. Removed in 10.0.14393. |


## APIs from srpapi.dll

| API | Requirements |
| -----| --------------|
| [SrpDoesPolicyAllowAppExecution](/windows/win32/api/srpapi/nf-srpapi-srpdoespolicyallowappexecution) | Introduced into srpapi.dll in 10.0.10240. |


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
| [remove](/windows/win32/msi/remove) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |
| [rename](/previous-versions/windows/desktop/aa964881(v=vs.85)) | Introduced into api-ms-win-crt-filesystem-l1-1-0.dll in 10.0.10240. |


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
| [setlocale](/previous-versions//5xf99h19(v=vs.85)) | Introduced into api-ms-win-crt-locale-l1-1-0.dll in 10.0.10240. |


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
| [acos](/windows/win32/direct3dhlsl/dx-graphics-hlsl-acos) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| acosf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| acosh | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| acoshf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| acoshl | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [asin](/windows/win32/direct3dhlsl/dx-graphics-hlsl-asin) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| asinf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| asinh | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| asinhf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| asinhl | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [atan](/windows/win32/direct3dhlsl/dx-graphics-hlsl-atan) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [atan2](/windows/win32/direct3dhlsl/dx-graphics-hlsl-atan2) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
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
| [ceil](/windows/win32/direct3dhlsl/dx-graphics-hlsl-ceil) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
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
| [cos](/previous-versions//66bkzah2(v=vs.85)) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| cosf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [cosh](/windows/win32/direct3dhlsl/dx-graphics-hlsl-cosh) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
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
| [exp](/previous-versions//aw8fzd30(v=vs.85)) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [exp2](/windows/win32/direct3dhlsl/dx-graphics-hlsl-exp2) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
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
| [floor](/windows/win32/direct3dhlsl/dx-graphics-hlsl-floor) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| floorf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [fma](/windows/win32/direct3dhlsl/dx-graphics-hlsl-fma) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| fmaf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| fmal | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| fmax | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| fmaxf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| fmaxl | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| fmin | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| fminf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| fminl | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [fmod](/windows/win32/direct3dhlsl/dx-graphics-hlsl-fmod) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| fmodf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [frexp](/windows/win32/direct3dhlsl/dx-graphics-hlsl-frexp) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| hypot | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| ilogb | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| ilogbf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| ilogbl | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [ldexp](/windows/win32/direct3dhlsl/dx-graphics-hlsl-ldexp) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| lgamma | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| lgammaf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| lgammal | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| llrint | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| llrintf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| llrintl | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| llround | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| llroundf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| llroundl | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [log](/previous-versions//5xkbf3yw(v=vs.85)) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [log10](/windows/win32/direct3dhlsl/dx-graphics-hlsl-log10) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| log10f | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| log1p | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| log1pf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| log1pl | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [log2](/windows/win32/direct3dhlsl/dx-graphics-hlsl-log2) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
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
| [modf](/windows/win32/direct3dhlsl/dx-graphics-hlsl-modf) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| modff | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [nan](/windows/win32/wintouch/imanipulationprocessor-constants) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
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
| [pow](/windows/win32/direct3dhlsl/dx-graphics-hlsl-pow) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
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
| [round](/windows/win32/direct3dhlsl/dx-graphics-hlsl-round) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| roundf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| roundl | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| scalbln | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| scalblnf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| scalblnl | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| scalbn | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| scalbnf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| scalbnl | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [sin](/windows/win32/direct3dhlsl/dx-graphics-hlsl-sin) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| sinf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [sinh](/windows/win32/direct3dhlsl/dx-graphics-hlsl-sinh) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| sinhf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [sqrt](/windows/win32/direct3dhlsl/dx-graphics-hlsl-sqrt) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| sqrtf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [tan](/windows/win32/direct3dhlsl/dx-graphics-hlsl-tan) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| tanf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [tanh](/windows/win32/direct3dhlsl/dx-graphics-hlsl-tanh) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| tanhf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| tgamma | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| tgammaf | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| tgammal | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
| [trunc](/windows/win32/direct3dhlsl/dx-graphics-hlsl-trunc) | Introduced into api-ms-win-crt-math-l1-1-0.dll in 10.0.10240. |
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
| [abort](/windows/win32/direct3dhlsl/abort) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
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
| [raise](/previous-versions//h1hea41c(v=vs.85)) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| set_terminate | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [signal](/windows/win32/multimedia/signal) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| strerror | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| strerror_s | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| [terminate](/windows/win32/api/resapi/nc-resapi-pterminate_routine) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.10240. |
| _seterrormode | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.17134. |
| [system](/windows/win32/wes/eventschema-system-eventtype-element) | Introduced into api-ms-win-crt-runtime-l1-1-0.dll in 10.0.17134. |
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
| [strcat](/windows/win32/api/shlwapi/nf-shlwapi-strcatw) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| strcat_s | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [strcmp](/windows/win32/api/shlwapi/nf-shlwapi-strcmpw) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| strcoll | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [strcpy](/windows/win32/api/shlwapi/nf-shlwapi-strcpyw) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| strcpy_s | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [strcspn](/windows/win32/api/shlwapi/nf-shlwapi-strcspna) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| strlen | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [strncat](/windows/win32/api/shlwapi/nf-shlwapi-strncata) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| strncat_s | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| strncmp | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| strncpy | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| strncpy_s | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| strnlen | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [strpbrk](/windows/win32/api/shlwapi/nf-shlwapi-strpbrka) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
| [strspn](/windows/win32/api/shlwapi/nf-shlwapi-strspna) | Introduced into api-ms-win-crt-string-l1-1-0.dll in 10.0.10240. |
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
| [abs](/previous-versions//307330xe(v=vs.85)) | Introduced into api-ms-win-crt-utility-l1-1-0.dll in 10.0.10240. |
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
| [CheckGamingPrivilegeWithUI](/windows/win32/api/gamingtcui/nf-gamingtcui-checkgamingprivilegewithui) | Introduced into api-ms-win-gaming-tcui-l1-1-0.dll in 10.0.10586. Removed in 10.0.14393. |


## APIs from winsqlite3.dll

For more information about these APIs, please see the official [SQLite documentation](https://sqlite.org/c3ref/funclist.html ).


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
| [SoundSentry](/windows/win32/api/winuser/nf-winuser-soundsentry) | Introduced into user32.dll in 10.0.14393. |
| [GetKeyNameTextA](/windows/win32/api/winuser/nf-winuser-getkeynametexta) | Introduced into user32.dll in 10.0.14393. |
| [GetKeyNameTextW](/windows/win32/api/winuser/nf-winuser-getkeynametexta) | Introduced into user32.dll in 10.0.14393. |
| [MapVirtualKeyA](/windows/win32/api/winuser/nf-winuser-mapvirtualkeya) | Introduced into user32.dll in 10.0.14393. |
| [MapVirtualKeyW](/windows/win32/api/winuser/nf-winuser-mapvirtualkeya) | Introduced into user32.dll in 10.0.14393. |
| [MapVirtualKeyExA](/windows/win32/api/winuser/nf-winuser-mapvirtualkeyexa) | Introduced into user32.dll in 10.0.14393. |
| [MapVirtualKeyExW](/windows/win32/api/winuser/nf-winuser-mapvirtualkeyexa) | Introduced into user32.dll in 10.0.14393. |
| [ClipCursor](/windows/win32/api/winuser/nf-winuser-clipcursor) | Introduced into user32.dll in 10.0.16299. |
| [GetKeyState](/windows/win32/api/winuser/nf-winuser-getkeystate) | Introduced into user32.dll in 10.0.16299. |
| [GetLastInputInfo](/windows/win32/api/winuser/nf-winuser-getlastinputinfo) | Introduced into user32.dll in 10.0.16299. |


## APIs from ResetPhoneForArm32.dll

| API | Requirements |
| -----| --------------|
| ResetPhoneForArm32 | Introduced into ResetPhoneForArm32.dll in 10.0.16299. |


## APIs from Credui.dll

| API | Requirements |
| -----| --------------|
| [CredUIParseUserNameW](/windows/win32/api/wincred/nf-wincred-creduiparseusernamea) | Introduced into Credui.dll in 10.0.16299. |


## APIs from ntdll.dll

| API | Requirements |
| -----| --------------|
| [NtQueryDirectoryFile](/previous-versions/ff567047(v=vs.85)) | Introduced into ntdll.dll in 10.0.16299. |
| [RtlEthernetAddressToString](/windows/win32/api/ip2string/nf-ip2string-rtlethernetaddresstostringa) | Introduced into ntdll.dll in 10.0.16299. Removed in 10.0.17134. |
| [RtlEthernetStringToAddress](/windows/win32/api/ip2string/nf-ip2string-rtlethernetstringtoaddressa) | Introduced into ntdll.dll in 10.0.16299. Removed in 10.0.17134. |
| [RtlIpv4AddressToString](/windows/win32/api/ip2string/nf-ip2string-rtlipv4addresstostringa) | Introduced into ntdll.dll in 10.0.16299. Removed in 10.0.17134. |
| [RtlIpv4AddressToStringEx](/windows/win32/api/ip2string/nf-ip2string-rtlipv4addresstostringexw) | Introduced into ntdll.dll in 10.0.16299. Removed in 10.0.17134. |
| [RtlIpv4StringToAddress](/windows/win32/api/ip2string/nf-ip2string-rtlipv4stringtoaddressa) | Introduced into ntdll.dll in 10.0.16299. Removed in 10.0.17134. |
| [RtlIpv4StringToAddressEx](/windows/win32/api/ip2string/nf-ip2string-rtlipv4stringtoaddressexw) | Introduced into ntdll.dll in 10.0.16299. Removed in 10.0.17134. |
| [RtlIpv6AddressToString](/windows/win32/api/ip2string/nf-ip2string-rtlipv6addresstostringa) | Introduced into ntdll.dll in 10.0.16299. Removed in 10.0.17134. |
| [RtlIpv6AddressToStringEx](/windows/win32/api/ip2string/nf-ip2string-rtlipv6addresstostringexw) | Introduced into ntdll.dll in 10.0.16299. Removed in 10.0.17134. |
| [RtlIpv6StringToAddress](/windows/win32/api/ip2string/nf-ip2string-rtlipv6stringtoaddressa) | Introduced into ntdll.dll in 10.0.16299. Removed in 10.0.17134. |
| [RtlIpv6StringToAddressEx](/windows/win32/api/ip2string/nf-ip2string-rtlipv6stringtoaddressexw) | Introduced into ntdll.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from OPMXbox.dll

| API | Requirements |
| -----| --------------|
| OPMXboxEnableHDCP | Introduced into OPMXbox.dll in 10.0.16299. |
| OPMXboxGetHDCPStatus | Introduced into OPMXbox.dll in 10.0.16299. |
| OPMXboxGetHDCPStatusAndType | Introduced into OPMXbox.dll in 10.0.16299. |


## APIs from efswrt.dll

| API | Requirements |
| -----| --------------|
| [ProtectFileToEnterpriseIdentity](/windows/win32/api/edpwin32/nf-edpwin32-protectfiletoenterpriseidentity) | Introduced into efswrt.dll in 10.0.16299. |
| UnprotectFile | Introduced into efswrt.dll in 10.0.16299. |


## APIs from wer.dll

| API | Requirements |
| -----| --------------|
| [WerStoreOpen](/windows/win32/api/werapi/nf-werapi-werstoreopen) | Introduced into wer.dll in 10.0.16299. |
| [WerStoreClose](/windows/win32/api/werapi/nf-werapi-werstoreclose) | Introduced into wer.dll in 10.0.16299. |
| [WerFreeString](/windows/win32/api/werapi/nf-werapi-werfreestring) | Introduced into wer.dll in 10.0.16299. |
| [WerStoreGetFirstReportKey](/windows/win32/api/werapi/nf-werapi-werstoregetfirstreportkey) | Introduced into wer.dll in 10.0.16299. |
| [WerStoreGetNextReportKey](/windows/win32/api/werapi/nf-werapi-werstoregetnextreportkey) | Introduced into wer.dll in 10.0.16299. |
| [WerStoreQueryReportMetadataV2](/windows/win32/api/werapi/nf-werapi-werstorequeryreportmetadatav2) | Introduced into wer.dll in 10.0.16299. |
| [WerReportCreate](/windows/win32/api/werapi/nf-werapi-werreportcreate) | Introduced into wer.dll in 10.0.16299. |
| [WerReportSetParameter](/windows/win32/api/werapi/nf-werapi-werreportsetparameter) | Introduced into wer.dll in 10.0.16299. |
| [WerReportAddFile](/windows/win32/api/werapi/nf-werapi-werreportaddfile) | Introduced into wer.dll in 10.0.16299. |
| [WerReportSubmit](/windows/win32/api/werapi/nf-werapi-werreportsubmit) | Introduced into wer.dll in 10.0.16299. |
| [WerReportAddDump](/windows/win32/api/werapi/nf-werapi-werreportadddump) | Introduced into wer.dll in 10.0.16299. |
| [WerReportCloseHandle](/windows/win32/api/werapi/nf-werapi-werreportclosehandle) | Introduced into wer.dll in 10.0.16299. |


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
| [CallNamedPipe](/windows/win32/api/winbase/nf-winbase-callnamedpipea) | Introduced into api-ms-win-core-namedpipe-ansi-l1-1-1.dll in 10.0.16299. Moved into api-ms-win-core-namedpipe-l1-2-2.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from crypt32.dll

| API | Requirements |
| -----| --------------|
| [CertGetNameString](/windows/win32/api/wincrypt/nf-wincrypt-certgetnamestringa) | Introduced into crypt32.dll in 10.0.16299. Removed in 10.0.17134. |
| [CertNameToStr](/windows/win32/api/wincrypt/nf-wincrypt-certnametostra) | Introduced into crypt32.dll in 10.0.16299. Removed in 10.0.17134. |
| [CertRDNValueToStr](/windows/win32/api/wincrypt/nf-wincrypt-certrdnvaluetostra) | Introduced into crypt32.dll in 10.0.16299. Removed in 10.0.17134. |
| [CertStrToName](/windows/win32/api/wincrypt/nf-wincrypt-certstrtonamea) | Introduced into crypt32.dll in 10.0.16299. Removed in 10.0.17134. |
| [CryptBinaryToString](/windows/win32/api/wincrypt/nf-wincrypt-cryptbinarytostringa) | Introduced into crypt32.dll in 10.0.16299. Removed in 10.0.17134. |
| [CryptStringToBinary](/windows/win32/api/wincrypt/nf-wincrypt-cryptstringtobinarya) | Introduced into crypt32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-downlevel-advapi32-l2-1-1.dll

| API | Requirements |
| -----| --------------|
| [ControlTrace](/windows/win32/api/evntrace/nf-evntrace-controltracea) | Introduced into api-ms-win-downlevel-advapi32-l2-1-1.dll in 10.0.16299. Moved into api-ms-win-eventing-controller-l1-1-0.dll in 10.0.16299. Moved into advapi32.dll in 10.0.16299. Removed in 10.0.17134. |
| [ConvertSecurityDescriptorToStringSecurityDescriptor](/windows/win32/api/sddl/nf-sddl-convertsecuritydescriptortostringsecuritydescriptora) | Introduced into api-ms-win-downlevel-advapi32-l2-1-1.dll in 10.0.16299. Moved into api-ms-win-security-sddl-l1-1-0.dll in 10.0.16299. Moved into advapi32.dll in 10.0.16299. Removed in 10.0.17134. |
| [OpenTrace](/windows/win32/api/evntrace/nf-evntrace-opentracea) | Introduced into api-ms-win-downlevel-advapi32-l2-1-1.dll in 10.0.16299. Moved into api-ms-win-eventing-consumer-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-eventing-consumer-l1-1-1.dll in 10.0.16299. Moved into advapi32.dll in 10.0.16299. Removed in 10.0.17134. |
| [StartTrace](/windows/win32/api/evntrace/nf-evntrace-starttracea) | Introduced into api-ms-win-downlevel-advapi32-l2-1-1.dll in 10.0.16299. Moved into api-ms-win-eventing-controller-l1-1-0.dll in 10.0.16299. Moved into advapi32.dll in 10.0.16299. Removed in 10.0.17134. |
| [StopTrace](/windows/win32/api/evntrace/nf-evntrace-stoptrace) | Introduced into api-ms-win-downlevel-advapi32-l2-1-1.dll in 10.0.16299. Moved into api-ms-win-eventing-controller-l1-1-0.dll in 10.0.16299. Moved into advapi32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-security-sddl-ansi-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [ConvertSidToStringSid](/windows/win32/api/sddl/nf-sddl-convertsidtostringsida) | Introduced into api-ms-win-security-sddl-ansi-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-advapi32-l2-1-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-advapi32-l2-1-1.dll in 10.0.16299. Moved into api-ms-win-security-sddl-l1-1-0.dll in 10.0.16299. Moved into advapi32.dll in 10.0.16299. Removed in 10.0.17134. |
| [ConvertStringSidToSid](/windows/win32/api/sddl/nf-sddl-convertstringsidtosida) | Introduced into api-ms-win-security-sddl-ansi-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-advapi32-l2-1-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-advapi32-l2-1-1.dll in 10.0.16299. Moved into api-ms-win-security-sddl-l1-1-0.dll in 10.0.16299. Moved into advapi32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-core-kernel32-legacy-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [CopyFile](/windows/win32/api/winbase/nf-winbase-copyfile) | Introduced into api-ms-win-core-kernel32-legacy-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-1.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-2.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-3.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-4.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-5.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-6.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l2-1-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l2-1-2.dll in 10.0.16299. Moved into api-ms-win-core-file-l2-1-3.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [CreateNamedPipe](/windows/win32/api/winbase/nf-winbase-createnamedpipea) | Introduced into api-ms-win-core-kernel32-legacy-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-1.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-2.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-3.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-4.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-5.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-6.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l2-1-0.dll in 10.0.16299. Moved into api-ms-win-core-namedpipe-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-namedpipe-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-namedpipe-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-core-namedpipe-l1-2-2.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [GetComputerName](/windows/win32/api/winbase/nf-winbase-getcomputernamea) | Introduced into api-ms-win-core-kernel32-legacy-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-1.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-2.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-3.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-4.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-5.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-6.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l2-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [GetStringTypeEx](/windows/win32/api/stringapiset/nf-stringapiset-getstringtypeexw) | Introduced into api-ms-win-core-kernel32-legacy-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-1.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-2.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-3.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-4.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-5.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-6.dll in 10.0.16299. Moved into api-ms-win-core-localization-ansi-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-deprecated-apis-legacy-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-deprecated-apis-legacy-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l2-1-0.dll in 10.0.16299. Moved into api-ms-win-core-string-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [MoveFileEx](/windows/win32/api/winbase/nf-winbase-movefileexa) | Introduced into api-ms-win-core-kernel32-legacy-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-1.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-2.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-3.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-4.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-5.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-6.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l2-1-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l2-1-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l2-1-1.dll in 10.0.16299. Moved into api-ms-win-core-file-l2-1-2.dll in 10.0.16299. Moved into api-ms-win-core-file-l2-1-3.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-core-file-ansi-l2-1-0.dll

| API | Requirements |
| -----| --------------|
| [CopyFileEx](/windows/win32/api/winbase/nf-winbase-copyfileexa) | Introduced into api-ms-win-core-file-ansi-l2-1-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l2-1-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l2-1-1.dll in 10.0.16299. Moved into api-ms-win-core-file-l2-1-2.dll in 10.0.16299. Moved into api-ms-win-core-file-l2-1-3.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [ReplaceFile](/windows/win32/api/winbase/nf-winbase-replacefilea) | Introduced into api-ms-win-core-file-ansi-l2-1-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l2-1-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l2-1-1.dll in 10.0.16299. Moved into api-ms-win-core-file-l2-1-2.dll in 10.0.16299. Moved into api-ms-win-core-file-l2-1-3.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-core-namespace-ansi-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [CreateBoundaryDescriptor](/windows/win32/api/winbase/nf-winbase-createboundarydescriptora) | Introduced into api-ms-win-core-namespace-ansi-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-namespace-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [CreatePrivateNamespace](/windows/win32/api/winbase/nf-winbase-createprivatenamespacea) | Introduced into api-ms-win-core-namespace-ansi-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-namespace-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [OpenPrivateNamespace](/windows/win32/api/winbase/nf-winbase-openprivatenamespacea) | Introduced into api-ms-win-core-namespace-ansi-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-namespace-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-core-file-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [CreateDirectory](/windows/win32/api/fileapi/nf-fileapi-createdirectorya) | Introduced into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [DeleteFile](/windows/win32/api/fileapi/nf-fileapi-deletefilea) | Introduced into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [FindNextFile](/windows/win32/api/fileapi/nf-fileapi-findnextfilea) | Introduced into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [FindFirstFile](/windows/win32/api/fileapi/nf-fileapi-findfirstfilea) | Introduced into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [FindFirstFileEx](/windows/win32/api/fileapi/nf-fileapi-findfirstfileexa) | Introduced into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [GetDiskFreeSpace](/windows/win32/api/fileapi/nf-fileapi-getdiskfreespacea) | Introduced into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [GetDriveType](/windows/win32/api/fileapi/nf-fileapi-getdrivetypea) | Introduced into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [GetFileAttributes](/windows/win32/api/fileapi/nf-fileapi-getfileattributesa) | Introduced into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [GetFullPathName](/windows/win32/api/fileapi/nf-fileapi-getfullpathnamea) | Introduced into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [GetDiskFreeSpaceEx](/windows/win32/api/fileapi/nf-fileapi-getdiskfreespaceexa) | Introduced into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [GetFileAttributesEx](/windows/win32/api/fileapi/nf-fileapi-getfileattributesexa) | Introduced into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [GetFinalPathNameByHandle](/windows/win32/api/fileapi/nf-fileapi-getfinalpathnamebyhandlea) | Introduced into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [GetLongPathName](/windows/win32/api/fileapi/nf-fileapi-getlongpathnamea) | Introduced into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [RemoveDirectory](/windows/win32/api/fileapi/nf-fileapi-removedirectorya) | Introduced into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [SetFileAttributes](/windows/win32/api/fileapi/nf-fileapi-setfileattributesa) | Introduced into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-core-synch-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [CreateEvent](https://msdn.microsoft.com/library/Ff975304(v=VS.85).aspx) | Introduced into api-ms-win-core-synch-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [CreateEventEx](/windows/win32/api/synchapi/nf-synchapi-createeventexa) | Introduced into api-ms-win-core-synch-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [CreateMutex](/windows/win32/api/synchapi/nf-synchapi-createmutexa) | Introduced into api-ms-win-core-synch-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [CreateMutexEx](/windows/win32/api/synchapi/nf-synchapi-createmutexexa) | Introduced into api-ms-win-core-synch-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [OpenEvent](/windows/win32/api/synchapi/nf-synchapi-openeventa) | Introduced into api-ms-win-core-synch-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [OpenSemaphore](/windows/win32/api/synchapi/nf-synchapi-opensemaphorew) | Introduced into api-ms-win-core-synch-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-security-cpwl-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| CreateProcessWithLogon | Introduced into api-ms-win-security-cpwl-l1-1-0.dll in 10.0.16299. Moved into advapi32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-core-processthreads-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [CreateProcess](/previous-versions/windows/desktop/axe/createprocess) | Introduced into api-ms-win-core-processthreads-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-processthreads-l1-1-1.dll in 10.0.16299. Moved into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.16299. Moved into api-ms-win-core-processthreads-l1-1-3.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-core-kernel32-legacy-l1-1-2.dll

| API | Requirements |
| -----| --------------|
| [CreateSemaphore](/windows/win32/api/synchapi/nf-synchapi-createsemaphorew) | Introduced into api-ms-win-core-kernel32-legacy-l1-1-2.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-3.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-4.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-5.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-6.dll in 10.0.16299. Moved into api-ms-win-core-synch-ansi-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-1.dll in 10.0.16299. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l2-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [OpenMutex](/windows/win32/api/synchapi/nf-synchapi-openmutexw) | Introduced into api-ms-win-core-kernel32-legacy-l1-1-2.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-3.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-4.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-5.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-6.dll in 10.0.16299. Moved into api-ms-win-core-synch-ansi-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-synch-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-core-synch-ansi-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [CreateSemaphoreEx](/windows/win32/api/synchapi/nf-synchapi-createsemaphoreexw) | Introduced into api-ms-win-core-synch-ansi-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-synch-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [CreateWaitableTimer](/windows/win32/api/synchapi/nf-synchapi-createwaitabletimerw) | Introduced into api-ms-win-core-synch-ansi-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [CreateWaitableTimerEx](/windows/win32/api/synchapi/nf-synchapi-createwaitabletimerexw) | Introduced into api-ms-win-core-synch-ansi-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-synch-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [OpenWaitableTimer](/windows/win32/api/synchapi/nf-synchapi-openwaitabletimerw) | Introduced into api-ms-win-core-synch-ansi-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-synch-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from ext-ms-win-security-credui-l1-1-1.dll

| API | Requirements |
| -----| --------------|
| [CredUIParseUserName](/windows/win32/api/wincred/nf-wincred-creduiparseusernamea) | Introduced into ext-ms-win-security-credui-l1-1-1.dll in 10.0.16299. Moved into Credui.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-security-cryptoapi-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [CryptAcquireContext](/windows/win32/api/wincrypt/nf-wincrypt-cryptacquirecontexta) | Introduced into api-ms-win-security-cryptoapi-l1-1-0.dll in 10.0.16299. Moved into advapi32.dll in 10.0.16299. Removed in 10.0.17134. |
| [CryptGetDefaultProvider](/windows/win32/api/wincrypt/nf-wincrypt-cryptgetdefaultprovidera) | Introduced into api-ms-win-security-cryptoapi-l1-1-0.dll in 10.0.16299. Moved into advapi32.dll in 10.0.16299. Removed in 10.0.17134. |
| [CryptSignHash](/windows/win32/api/wincrypt/nf-wincrypt-cryptsignhasha) | Introduced into api-ms-win-security-cryptoapi-l1-1-0.dll in 10.0.16299. Moved into advapi32.dll in 10.0.16299. Removed in 10.0.17134. |
| [CryptVerifySignature](/windows/win32/api/wincrypt/nf-wincrypt-cryptverifysignaturea) | Introduced into api-ms-win-security-cryptoapi-l1-1-0.dll in 10.0.16299. Moved into advapi32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-core-file-ansi-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [DeleteVolumeMountPoint](/windows/win32/api/fileapi/nf-fileapi-deletevolumemountpointw) | Introduced into api-ms-win-core-file-ansi-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-core-localization-l2-1-0.dll

| API | Requirements |
| -----| --------------|
| [EnumSystemCodePages](/windows/win32/api/winnls/nf-winnls-enumsystemcodepagesa) | Introduced into api-ms-win-core-localization-l2-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-core-localization-ansi-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [EnumUILanguages](/windows/win32/api/winnls/nf-winnls-enumuilanguagesa) | Introduced into api-ms-win-core-localization-ansi-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-localization-obsolete-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-localization-obsolete-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-localization-obsolete-l1-3-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-core-processenvironment-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [ExpandEnvironmentStrings](/windows/win32/api/processenv/nf-processenv-expandenvironmentstringsa) | Introduced into api-ms-win-core-processenvironment-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-processenvironment-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [FreeEnvironmentStrings](/windows/win32/api/processenv/nf-processenv-freeenvironmentstringsa) | Introduced into api-ms-win-core-processenvironment-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-processenvironment-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [GetCommandLine](/windows/win32/api/processenv/nf-processenv-getcommandlinea) | Introduced into api-ms-win-core-processenvironment-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-processenvironment-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [GetCurrentDirectory](/windows/win32/api/winbase/nf-winbase-getcurrentdirectory) | Introduced into api-ms-win-core-processenvironment-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-processenvironment-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [GetEnvironmentVariable](/windows/win32/api/processenv/nf-processenv-getenvironmentvariablea) | Introduced into api-ms-win-core-processenvironment-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-processenvironment-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [SetCurrentDirectory](/windows/win32/api/winbase/nf-winbase-setcurrentdirectory) | Introduced into api-ms-win-core-processenvironment-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-processenvironment-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-core-console-l2-1-0.dll

| API | Requirements |
| -----| --------------|
| [FillConsoleOutputCharacter](/windows/console/fillconsoleoutputcharacter) | Introduced into api-ms-win-core-console-l2-1-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [GetConsoleTitle](/windows/console/getconsoletitle) | Introduced into api-ms-win-core-console-l2-1-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [PeekConsoleInput](/windows/console/peekconsoleinput) | Introduced into api-ms-win-core-console-l2-1-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [ReadConsoleOutput](/windows/console/readconsoleoutput) | Introduced into api-ms-win-core-console-l2-1-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [SetConsoleTitle](/windows/console/setconsoletitle) | Introduced into api-ms-win-core-console-l2-1-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [WriteConsoleOutput](/windows/console/writeconsoleoutput) | Introduced into api-ms-win-core-console-l2-1-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-eventing-legacy-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [FlushTrace](/windows/win32/api/evntrace/nf-evntrace-flushtracea) | Introduced into api-ms-win-eventing-legacy-l1-1-0.dll in 10.0.16299. Moved into advapi32.dll in 10.0.16299. Removed in 10.0.17134. |
| [QueryTrace](/windows/win32/api/evntrace/nf-evntrace-querytrace) | Introduced into api-ms-win-eventing-legacy-l1-1-0.dll in 10.0.16299. Moved into advapi32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-core-localization-l1-2-0.dll

| API | Requirements |
| -----| --------------|
| [FormatMessage](/windows/win32/api/winbase/nf-winbase-formatmessage) | Introduced into api-ms-win-core-localization-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-localization-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-core-localization-l1-2-2.dll in 10.0.16299. Moved into api-ms-win-core-misc-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [GetGeoInfo](/windows/win32/api/winnls/nf-winnls-getgeoinfoa) | Introduced into api-ms-win-core-localization-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-localization-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-core-localization-l1-2-2.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [GetLocaleInfo](/windows/win32/api/winnls/nf-winnls-getlocaleinfoa) | Introduced into api-ms-win-core-localization-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-localization-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-core-localization-l1-2-2.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-localization-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from ws2_32.dll

| API | Requirements |
| -----| --------------|
| [FreeAddrInfo](/windows/win32/api/ws2tcpip/nf-ws2tcpip-freeaddrinfo) | Introduced into ws2_32.dll in 10.0.16299. Removed in 10.0.17134. |
| [GetAddrInfoEx](/windows/win32/api/ws2tcpip/nf-ws2tcpip-getaddrinfoexa) | Introduced into ws2_32.dll in 10.0.16299. Removed in 10.0.17134. |
| [GetAddrInfo](/windows/win32/api/ws2tcpip/nf-ws2tcpip-getaddrinfo) | Introduced into ws2_32.dll in 10.0.16299. Removed in 10.0.17134. |
| [GetHostName](/windows/win32/api/winsock/nf-winsock-gethostname) | Introduced into ws2_32.dll in 10.0.16299. Removed in 10.0.17134. |
| [GetNameInfo](/windows/win32/api/ws2tcpip/nf-ws2tcpip-getnameinfo) | Introduced into ws2_32.dll in 10.0.16299. Removed in 10.0.17134. |
| [InetNtop](/windows/win32/api/ws2tcpip/nf-ws2tcpip-inetntopw) | Introduced into ws2_32.dll in 10.0.16299. Removed in 10.0.17134. |
| [InetPton](/windows/win32/api/ws2tcpip/nf-ws2tcpip-inetptonw) | Introduced into ws2_32.dll in 10.0.16299. Removed in 10.0.17134. |
| [SetAddrInfoEx](/windows/win32/api/ws2tcpip/nf-ws2tcpip-setaddrinfoexa) | Introduced into ws2_32.dll in 10.0.16299. Removed in 10.0.17134. |
| [WSAAddressToString](/windows/win32/api/winsock2/nf-winsock2-wsaaddresstostringa) | Introduced into ws2_32.dll in 10.0.16299. Removed in 10.0.17134. |
| [WSAConnectByName](/windows/win32/api/winsock2/nf-winsock2-wsaconnectbynamea) | Introduced into ws2_32.dll in 10.0.16299. Removed in 10.0.17134. |
| [WSADuplicateSocket](/windows/win32/api/winsock2/nf-winsock2-wsaduplicatesocketa) | Introduced into ws2_32.dll in 10.0.16299. Removed in 10.0.17134. |
| [WSAEnumNameSpaceProviders](/windows/win32/api/winsock2/nf-winsock2-wsaenumnamespaceprovidersa) | Introduced into ws2_32.dll in 10.0.16299. Removed in 10.0.17134. |
| [WSAEnumNameSpaceProvidersEx](/windows/win32/api/winsock2/nf-winsock2-wsaenumnamespaceprovidersexa) | Introduced into ws2_32.dll in 10.0.16299. Removed in 10.0.17134. |
| [WSAEnumProtocols](/windows/win32/api/winsock2/nf-winsock2-wsaenumprotocolsa) | Introduced into ws2_32.dll in 10.0.16299. Removed in 10.0.17134. |
| [WSAGetServiceClassInfo](/windows/win32/api/winsock2/nf-winsock2-wsagetserviceclassinfoa) | Introduced into ws2_32.dll in 10.0.16299. Removed in 10.0.17134. |
| [WSAGetServiceClassNameByClassId](/windows/win32/api/winsock2/nf-winsock2-wsagetserviceclassnamebyclassida) | Introduced into ws2_32.dll in 10.0.16299. Removed in 10.0.17134. |
| [WSALookupServiceBegin](/windows/win32/api/winsock2/nf-winsock2-wsalookupservicebegina) | Introduced into ws2_32.dll in 10.0.16299. Removed in 10.0.17134. |
| [WSALookupServiceNext](/windows/win32/api/winsock2/nf-winsock2-wsalookupservicenexta) | Introduced into ws2_32.dll in 10.0.16299. Removed in 10.0.17134. |
| [WSASetService](/windows/win32/api/winsock2/nf-winsock2-wsasetservicea) | Introduced into ws2_32.dll in 10.0.16299. Removed in 10.0.17134. |
| [WSASocket](/windows/win32/api/winsock2/nf-winsock2-wsasocketa) | Introduced into ws2_32.dll in 10.0.16299. Removed in 10.0.17134. |
| [WSAStringToAddress](/windows/win32/api/winsock2/nf-winsock2-wsastringtoaddressa) | Introduced into ws2_32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-core-namedpipe-ansi-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [GetNamedPipeClientComputerName](/windows/win32/api/winbase/nf-winbase-getnamedpipeclientcomputernamea) | Introduced into api-ms-win-core-namedpipe-ansi-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-namedpipe-ansi-l1-1-1.dll in 10.0.16299. Moved into api-ms-win-core-namedpipe-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-namedpipe-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-namedpipe-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-core-namedpipe-l1-2-2.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [GetNamedPipeHandleState](/windows/win32/api/winbase/nf-winbase-getnamedpipehandlestatea) | Introduced into api-ms-win-core-namedpipe-ansi-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-namedpipe-ansi-l1-1-1.dll in 10.0.16299. Moved into api-ms-win-core-namedpipe-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-core-namedpipe-l1-2-2.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [WaitNamedPipe](/windows/win32/api/winbase/nf-winbase-waitnamedpipea) | Introduced into api-ms-win-core-namedpipe-ansi-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-namedpipe-ansi-l1-1-1.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Moved into api-ms-win-core-namedpipe-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-namedpipe-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-namedpipe-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-core-namedpipe-l1-2-2.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-core-url-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [GetAcceptLanguages](/windows/win32/api/shlwapi/nf-shlwapi-getacceptlanguagesa) | Introduced into api-ms-win-core-url-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-shlwapi-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-shlwapi-l1-1-1.dll in 10.0.16299. Moved into shlwapi.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-core-localization-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [GetCPInfoEx](/windows/win32/api/winnls/nf-winnls-getcpinfoexa) | Introduced into api-ms-win-core-localization-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-localization-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-localization-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-core-localization-l1-2-2.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-security-provider-ansi-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [GetExplicitEntriesFromAcl](/windows/win32/api/aclapi/nf-aclapi-getexplicitentriesfromacla) | Introduced into api-ms-win-security-provider-ansi-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-advapi32-l3-1-0.dll in 10.0.16299. Moved into api-ms-win-security-provider-l1-1-0.dll in 10.0.16299. Moved into advapi32.dll in 10.0.16299. Removed in 10.0.17134. |
| [GetNamedSecurityInfo](/windows/win32/api/aclapi/nf-aclapi-getnamedsecurityinfoa) | Introduced into api-ms-win-security-provider-ansi-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-advapi32-l3-1-0.dll in 10.0.16299. Moved into api-ms-win-security-provider-l1-1-0.dll in 10.0.16299. Moved into advapi32.dll in 10.0.16299. Removed in 10.0.17134. |
| [SetEntriesInAcl](/windows/win32/api/aclapi/nf-aclapi-setentriesinacla) | Introduced into api-ms-win-security-provider-ansi-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-advapi32-l3-1-0.dll in 10.0.16299. Moved into api-ms-win-security-provider-l1-1-0.dll in 10.0.16299. Moved into advapi32.dll in 10.0.16299. Removed in 10.0.17134. |
| [SetNamedSecurityInfo](/windows/win32/api/aclapi/nf-aclapi-setnamedsecurityinfoa) | Introduced into api-ms-win-security-provider-ansi-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-advapi32-l3-1-0.dll in 10.0.16299. Moved into api-ms-win-security-provider-l1-1-0.dll in 10.0.16299. Moved into advapi32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from version.dll

| API | Requirements |
| -----| --------------|
| [GetFileVersionInfoEx](/windows/win32/api/winver/nf-winver-getfileversioninfoexa) | Introduced into version.dll in 10.0.16299. Moved into api-ms-win-core-versionansi-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-versionansi-l1-1-1.dll in 10.0.16299. Moved into api-ms-win-core-version-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-version-l1-1-1.dll in 10.0.16299. Moved into api-ms-win-downlevel-version-l1-1-0.dll in 10.0.16299. Removed in 10.0.17134. |
| [GetFileVersionInfoSizeEx](/windows/win32/api/winver/nf-winver-getfileversioninfosizeexa) | Introduced into version.dll in 10.0.16299. Moved into api-ms-win-core-versionansi-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-versionansi-l1-1-1.dll in 10.0.16299. Moved into api-ms-win-core-version-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-version-l1-1-1.dll in 10.0.16299. Moved into api-ms-win-downlevel-version-l1-1-0.dll in 10.0.16299. Removed in 10.0.17134. |
| [VerQueryValue](/windows/win32/api/winver/nf-winver-verqueryvaluea) | Introduced into version.dll in 10.0.16299. Moved into api-ms-win-core-versionansi-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-versionansi-l1-1-1.dll in 10.0.16299. Moved into api-ms-win-downlevel-version-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-version-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-version-l1-1-1.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from ext-ms-win-ntuser-keyboard-l1-2-0.dll

| API | Requirements |
| -----| --------------|
| [GetKeyNameText](/windows/win32/api/winuser/nf-winuser-getkeynametexta) | Introduced into ext-ms-win-ntuser-keyboard-l1-2-0.dll in 10.0.16299. Moved into ext-ms-win-ntuser-keyboard-l1-3-0.dll in 10.0.16299. Moved into user32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from ext-ms-win-base-psapi-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [GetModuleBaseName](/windows/win32/api/psapi/nf-psapi-getmodulebasenamea) | Introduced into ext-ms-win-base-psapi-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-core-libraryloader-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [GetModuleFileName](/windows/win32/api/libloaderapi/nf-libloaderapi-getmodulefilenamea) | Introduced into api-ms-win-core-libraryloader-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-libraryloader-l1-1-1.dll in 10.0.16299. Moved into api-ms-win-core-libraryloader-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-libraryloader-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-core-libraryloader-l1-2-2.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-core-string-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| GetStringType | Introduced into api-ms-win-core-string-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-core-sysinfo-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [GetSystemDirectory](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getsystemdirectorya) | Introduced into api-ms-win-core-sysinfo-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-sysinfo-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-sysinfo-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-core-sysinfo-l1-2-2.dll in 10.0.16299. Moved into api-ms-win-core-sysinfo-l1-2-3.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [GetVersionEx](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getversionexa) | Introduced into api-ms-win-core-sysinfo-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-sysinfo-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-sysinfo-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-core-sysinfo-l1-2-2.dll in 10.0.16299. Moved into api-ms-win-core-sysinfo-l1-2-3.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-core-file-l1-2-2.dll

| API | Requirements |
| -----| --------------|
| [GetTempFileName](/windows/win32/api/fileapi/nf-fileapi-gettempfilenamea) | Introduced into api-ms-win-core-file-l1-2-2.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [GetTempPath](/windows/win32/api/fileapi/nf-fileapi-gettemppatha) | Introduced into api-ms-win-core-file-l1-2-2.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-1.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-2.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-3.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-4.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-5.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-6.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l2-1-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [GetVolumeInformation](/windows/win32/api/fileapi/nf-fileapi-getvolumeinformationa) | Introduced into api-ms-win-core-file-l1-2-2.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-core-kernel32-legacy-ansi-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [SetVolumeLabel](/windows/win32/api/winbase/nf-winbase-setvolumelabela) | Introduced into api-ms-win-core-kernel32-legacy-ansi-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-1.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-2.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-3.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-4.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-5.dll in 10.0.16299. Moved into api-ms-win-core-kernel32-legacy-l1-1-6.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l2-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from esent.dll

| API | Requirements |
| -----| --------------|
| JetCreateIndex4 | Introduced into esent.dll in 10.0.16299. Removed in 10.0.17134. |
| JetCreateTableColumnIndex4 | Introduced into esent.dll in 10.0.16299. Removed in 10.0.17134. |
| JetGetErrorInfo | Introduced into esent.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-core-psapi-ansi-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [K32GetModuleBaseName](/windows/win32/api/psapi/nf-psapi-getmodulebasenamea) | Introduced into api-ms-win-core-psapi-ansi-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-psapi-obsolete-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-psapi-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [K32GetModuleFileNameEx](/windows/win32/api/psapi/nf-psapi-getmodulefilenameexa) | Introduced into api-ms-win-core-psapi-ansi-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-psapi-obsolete-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-psapi-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-security-lsalookup-ansi-l2-1-0.dll

| API | Requirements |
| -----| --------------|
| [LookupAccountName](/windows/win32/api/winbase/nf-winbase-lookupaccountnamea) | Introduced into api-ms-win-security-lsalookup-ansi-l2-1-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-advapi32-l4-1-0.dll in 10.0.16299. Moved into api-ms-win-security-lsalookup-l2-1-0.dll in 10.0.16299. Moved into api-ms-win-security-lsalookup-l2-1-1.dll in 10.0.16299. Moved into advapi32.dll in 10.0.16299. Removed in 10.0.17134. |
| [LookupAccountSid](/windows/win32/api/winbase/nf-winbase-lookupaccountsida) | Introduced into api-ms-win-security-lsalookup-ansi-l2-1-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-advapi32-l4-1-0.dll in 10.0.16299. Moved into api-ms-win-security-lsalookup-l2-1-0.dll in 10.0.16299. Moved into api-ms-win-security-lsalookup-l2-1-1.dll in 10.0.16299. Moved into advapi32.dll in 10.0.16299. Removed in 10.0.17134. |
| [LookupPrivilegeDisplayName](/windows/win32/api/winbase/nf-winbase-lookupprivilegedisplaynamea) | Introduced into api-ms-win-security-lsalookup-ansi-l2-1-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-advapi32-l4-1-0.dll in 10.0.16299. Moved into api-ms-win-security-lsalookup-l2-1-0.dll in 10.0.16299. Moved into api-ms-win-security-lsalookup-l2-1-1.dll in 10.0.16299. Moved into advapi32.dll in 10.0.16299. Removed in 10.0.17134. |
| [LookupPrivilegeName](/windows/win32/api/winbase/nf-winbase-lookupprivilegenamea) | Introduced into api-ms-win-security-lsalookup-ansi-l2-1-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-advapi32-l4-1-0.dll in 10.0.16299. Moved into api-ms-win-security-lsalookup-l2-1-0.dll in 10.0.16299. Moved into api-ms-win-security-lsalookup-l2-1-1.dll in 10.0.16299. Moved into advapi32.dll in 10.0.16299. Removed in 10.0.17134. |
| [LookupPrivilegeValue](/windows/win32/api/winbase/nf-winbase-lookupprivilegevaluea) | Introduced into api-ms-win-security-lsalookup-ansi-l2-1-0.dll in 10.0.16299. Moved into ext-ms-win-advapi32-auth-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-advapi32-l4-1-0.dll in 10.0.16299. Moved into api-ms-win-security-lsalookup-l2-1-0.dll in 10.0.16299. Moved into api-ms-win-security-lsalookup-l2-1-1.dll in 10.0.16299. Moved into advapi32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from ext-ms-win-ntuser-keyboard-l1-3-0.dll

| API | Requirements |
| -----| --------------|
| [MapVirtualKey](/windows/win32/api/winuser/nf-winuser-mapvirtualkeya) | Introduced into ext-ms-win-ntuser-keyboard-l1-3-0.dll in 10.0.16299. Moved into ext-ms-win-ntuser-keyboard-l1-1-0.dll in 10.0.16299. Moved into ext-ms-win-ntuser-keyboard-l1-1-1.dll in 10.0.16299. Moved into ext-ms-win-ntuser-keyboard-l1-2-0.dll in 10.0.16299. Moved into user32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from ext-ms-win-ntuser-keyboard-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [MapVirtualKeyEx](/windows/win32/api/winuser/nf-winuser-mapvirtualkeyexa) | Introduced into ext-ms-win-ntuser-keyboard-l1-1-0.dll in 10.0.16299. Moved into ext-ms-win-ntuser-keyboard-l1-1-1.dll in 10.0.16299. Moved into ext-ms-win-ntuser-keyboard-l1-2-0.dll in 10.0.16299. Moved into ext-ms-win-ntuser-keyboard-l1-3-0.dll in 10.0.16299. Moved into user32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-core-debug-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [OutputDebugString](/windows/win32/api/debugapi/nf-debugapi-outputdebugstringa) | Introduced into api-ms-win-core-debug-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-core-debug-l1-1-1.dll in 10.0.16299. Moved into api-ms-win-core-debug-l1-1-2.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-core-console-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [ReadConsoleInput](/windows/console/readconsoleinput) | Introduced into api-ms-win-core-console-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [ReadConsole](/windows/console/readconsole) | Introduced into api-ms-win-core-console-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |
| [WriteConsole](/windows/console/writeconsole) | Introduced into api-ms-win-core-console-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-core-file-l2-1-0.dll

| API | Requirements |
| -----| --------------|
| ReadDirectoryChanges | Introduced into api-ms-win-core-file-l2-1-0.dll in 10.0.16299. Moved into api-ms-win-core-file-l2-1-1.dll in 10.0.16299. Moved into api-ms-win-core-file-l2-1-2.dll in 10.0.16299. Moved into api-ms-win-core-file-l2-1-3.dll in 10.0.16299. Moved into api-ms-win-downlevel-kernel32-l1-1-0.dll in 10.0.16299. Moved into kernel32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from api-ms-win-downlevel-advapi32-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [RegisterTraceGuids](/windows/win32/api/evntrace/nf-evntrace-registertraceguidsa) | Introduced into api-ms-win-downlevel-advapi32-l1-1-0.dll in 10.0.16299. Moved into api-ms-win-downlevel-advapi32-l1-1-1.dll in 10.0.16299. Moved into api-ms-win-eventing-classicprovider-l1-1-0.dll in 10.0.16299. Moved into advapi32.dll in 10.0.16299. Removed in 10.0.17134. |


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
| [Tbsi_Context_Create](/windows/win32/api/tbs/nf-tbs-tbsi_context_create) | Introduced into tbs.dll in 10.0.17134. |
| [Tbsi_GetDeviceInfo](/windows/win32/api/tbs/nf-tbs-tbsi_getdeviceinfo) | Introduced into tbs.dll in 10.0.17134. |
| [Tbsi_Get_OwnerAuth](/windows/win32/api/tbs/nf-tbs-tbsi_get_ownerauth) | Introduced into tbs.dll in 10.0.17134. |
| [Tbsi_Get_TCG_Log](/windows/win32/api/tbs/nf-tbs-tbsi_get_tcg_log) | Introduced into tbs.dll in 10.0.17134. |
| [Tbsi_Physical_Presence_Command](/windows/win32/api/tbs/nf-tbs-tbsi_physical_presence_command) | Introduced into tbs.dll in 10.0.17134. |
| [Tbsi_Revoke_Attestation](/windows/win32/api/tbs/nf-tbs-tbsi_revoke_attestation) | Introduced into tbs.dll in 10.0.17134. |
| [Tbsip_Cancel_Commands](/windows/win32/api/tbs/nf-tbs-tbsip_cancel_commands) | Introduced into tbs.dll in 10.0.17134. |
| [Tbsip_Context_Close](/windows/win32/api/tbs/nf-tbs-tbsip_context_close) | Introduced into tbs.dll in 10.0.17134. |
| [Tbsip_Submit_Command](/windows/win32/api/tbs/nf-tbs-tbsip_submit_command) | Introduced into tbs.dll in 10.0.17134. |


## APIs from api-ms-win-core-rtlsupport-l1-2-0.dll

| API | Requirements |
| -----| --------------|
| [RtlVirtualUnwind](/windows/win32/api/winnt/nf-winnt-rtlvirtualunwind) | Introduced into api-ms-win-core-rtlsupport-l1-2-0.dll in 10.0.17763. |


COM interfaces

| API | Requirements |
| -----| --------------|
| [_IRDPSessionEvents](/windows/win32/api/rdpencomapi/nn-rdpencomapi-_irdpsessionevents) | Introduced in 10.0.10240. |
| _IWorkspaceBrokerAxEvents | Introduced in 10.0.10240. |
| [IAccessibleEx](/windows/win32/api/uiautomationcore/nn-uiautomationcore-iaccessibleex) | Introduced in 10.0.10240. |
| [IAccessibleHostingElementProviders](/windows/win32/api/uiautomationcore/nn-uiautomationcore-iaccessiblehostingelementproviders) | Introduced in 10.0.10240. |
| [IActivateAudioInterfaceAsyncOperation](/windows/win32/api/mmdeviceapi/nn-mmdeviceapi-iactivateaudiointerfaceasyncoperation) | Introduced in 10.0.10240. |
| [IActivateAudioInterfaceCompletionHandler](/windows/win32/api/mmdeviceapi/nn-mmdeviceapi-iactivateaudiointerfacecompletionhandler) | Introduced in 10.0.10240. |
| [IActivationFactory](/windows/win32/api/activation/nn-activation-iactivationfactory) | Introduced in 10.0.10240. |
| [IAdvancedMediaCapture](/windows/win32/api/mfmediacapture/nn-mfmediacapture-iadvancedmediacapture) | Introduced in 10.0.10240. |
| [IAdvancedMediaCaptureInitializationSettings](/windows/win32/api/mfmediacapture/nn-mfmediacapture-iadvancedmediacaptureinitializationsettings) | Introduced in 10.0.10240. |
| [IAdvancedMediaCaptureSettings](/windows/win32/api/mfmediacapture/nn-mfmediacapture-iadvancedmediacapturesettings) | Introduced in 10.0.10240. |
| [IAgileObject](/windows/win32/api/objidlbase/nn-objidlbase-iagileobject) | Introduced in 10.0.10240. |
| [IAgileReference](/windows/win32/api/objidl/nn-objidl-iagilereference) | Introduced in 10.0.10240. |
| [IAnnotationProvider](/windows/win32/api/uiautomationcore/nn-uiautomationcore-iannotationprovider) | Introduced in 10.0.10240. |
| IAoWAppActivatedRuntime | Introduced in 10.0.10240. Removed in 10.0.16299. |
| IAoWBackgroundTaskRuntime | Introduced in 10.0.10240. Removed in 10.0.16299. |
| [IApartmentShutdown](/windows/win32/api/objidl/nn-objidl-iapartmentshutdown) | Introduced in 10.0.10240. |
| [IAsyncInfo](/windows/win32/api/asyncinfo/nn-asyncinfo-iasyncinfo) | Introduced in 10.0.10240. |
| [IAudioCaptureClient](/windows/win32/api/audioclient/nn-audioclient-iaudiocaptureclient) | Introduced in 10.0.10240. |
| [IAudioClient](/windows/win32/api/audioclient/nn-audioclient-iaudioclient) | Introduced in 10.0.10240. |
| [IAudioClient2](/windows/win32/api/audioclient/nn-audioclient-iaudioclient2) | Introduced in 10.0.10240. |
| [IAudioClient3](/windows/win32/api/audioclient/nn-audioclient-iaudioclient3) | Introduced in 10.0.10240. |
| [IAudioClock](/windows/win32/api/audioclient/nn-audioclient-iaudioclock) | Introduced in 10.0.10240. |
| [IAudioEndpointVolume](/windows/win32/api/endpointvolume/nn-endpointvolume-iaudioendpointvolume) | Introduced in 10.0.10240. |
| [IAudioEndpointVolumeCallback](/windows/win32/api/endpointvolume/nn-endpointvolume-iaudioendpointvolumecallback) | Introduced in 10.0.10240. |
| [IAudioFrameNative](/windows/win32/api/windows.media.core.interop/nn-windows-media-core-interop-iaudioframenative) | Introduced in 10.0.10240. |
| [IAudioFrameNativeFactory](/windows/win32/api/windows.media.core.interop/nn-windows-media-core-interop-iaudioframenativefactory) | Introduced in 10.0.10240. |
| [IAudioMeterInformation](/windows/win32/api/endpointvolume/nn-endpointvolume-iaudiometerinformation) | Introduced in 10.0.10240. |
| [IAudioRenderClient](/windows/win32/api/audioclient/nn-audioclient-iaudiorenderclient) | Introduced in 10.0.10240. |
| [IAudioSessionControl](/windows/win32/api/audiopolicy/nn-audiopolicy-iaudiosessioncontrol) | Introduced in 10.0.10240. |
| [IAudioSessionEvents](/windows/win32/api/audiopolicy/nn-audiopolicy-iaudiosessionevents) | Introduced in 10.0.10240. |
| [IAudioStreamVolume](/windows/win32/api/audioclient/nn-audioclient-iaudiostreamvolume) | Introduced in 10.0.10240. |
| IAudioVideoCaptureDeviceNative | Introduced in 10.0.10240. |
| [IBindCtx](/windows/win32/api/objidl/nn-objidl-ibindctx) | Introduced in 10.0.10240. |
| ICameraCaptureDeviceNative | Introduced in 10.0.10240. |
| ICameraCaptureFrameNative | Introduced in 10.0.10240. |
| ICameraCapturePreviewSink | Introduced in 10.0.10240. |
| [ICameraUIControl](/windows/win32/api/camerauicontrol/nn-camerauicontrol-icamerauicontrol) | Introduced in 10.0.10240. |
| [ICameraUIControlEventCallback](/windows/win32/api/camerauicontrol/nn-camerauicontrol-icamerauicontroleventcallback) | Introduced in 10.0.10240. |
| [IClassFactory](/windows/win32/api/unknwn/nn-unknwn-iclassfactory) | Introduced in 10.0.10240. |
| [IClientSecurity](/windows/win32/api/objidl/nn-objidl-iclientsecurity) | Introduced in 10.0.10240. |
| [ICodecAPI](/windows/win32/api/strmif/nn-strmif-icodecapi) | Introduced in 10.0.10240. |
| [IConnectionPoint](/windows/win32/api/ocidl/nn-ocidl-iconnectionpoint) | Introduced in 10.0.10240. |
| [IConnectionPointContainer](/windows/win32/api/ocidl/nn-ocidl-iconnectionpointcontainer) | Introduced in 10.0.10240. |
| [IContextCallback](/windows/win32/api/ctxtcall/nn-ctxtcall-icontextcallback) | Introduced in 10.0.10240. |
| [ICreateDeviceAccessAsync](/windows/win32/api/deviceaccess/nn-deviceaccess-icreatedeviceaccessasync) | Introduced in 10.0.10240. |
| ICustomNavigationProvider | Introduced in 10.0.10240. |
| [ID2D1AnalysisTransform](/windows/win32/api/d2d1effectauthor/nn-d2d1effectauthor-id2d1analysistransform) | Introduced in 10.0.10240. |
| [ID2D1Bitmap](/windows/win32/api/d2d1/nn-d2d1-id2d1bitmap) | Introduced in 10.0.10240. |
| [ID2D1Bitmap1](/windows/win32/api/d2d1_1/nn-d2d1_1-id2d1bitmap1) | Introduced in 10.0.10240. |
| [ID2D1BitmapBrush](/windows/win32/api/d2d1/nn-d2d1-id2d1bitmapbrush) | Introduced in 10.0.10240. |
| [ID2D1BitmapRenderTarget](/windows/win32/api/d2d1/nn-d2d1-id2d1bitmaprendertarget) | Introduced in 10.0.10240. |
| [ID2D1BlendTransform](/windows/win32/api/d2d1effectauthor/nn-d2d1effectauthor-id2d1blendtransform) | Introduced in 10.0.10240. |
| [ID2D1BorderTransform](/windows/win32/api/d2d1effectauthor/nn-d2d1effectauthor-id2d1bordertransform) | Introduced in 10.0.10240. |
| [ID2D1BoundsAdjustmentTransform](/windows/win32/api/d2d1effectauthor/nn-d2d1effectauthor-id2d1boundsadjustmenttransform) | Introduced in 10.0.10240. |
| [ID2D1Brush](/windows/win32/api/d2d1/nn-d2d1-id2d1brush) | Introduced in 10.0.10240. |
| [ID2D1ColorContext](/windows/win32/api/d2d1_1/nn-d2d1_1-id2d1colorcontext) | Introduced in 10.0.10240. |
| [ID2D1CommandList](/windows/win32/api/d2d1_1/nn-d2d1_1-id2d1commandlist) | Introduced in 10.0.10240. |
| [ID2D1CommandSink](/windows/win32/api/d2d1_1/nn-d2d1_1-id2d1commandsink) | Introduced in 10.0.10240. |
| [ID2D1CommandSink1](/windows/win32/api/d2d1_2/nn-d2d1_2-id2d1commandsink1) | Introduced in 10.0.10240. |
| [ID2D1CommandSink2](/windows/win32/api/d2d1_3/nn-d2d1_3-id2d1commandsink2) | Introduced in 10.0.10240. |
| [ID2D1ComputeInfo](/windows/win32/api/d2d1effectauthor/nn-d2d1effectauthor-id2d1computeinfo) | Introduced in 10.0.10240. |
| [ID2D1ComputeTransform](/windows/win32/api/d2d1effectauthor/nn-d2d1effectauthor-id2d1computetransform) | Introduced in 10.0.10240. |
| [ID2D1ConcreteTransform](/windows/win32/api/d2d1effectauthor/nn-d2d1effectauthor-id2d1concretetransform) | Introduced in 10.0.10240. |
| [ID2D1DCRenderTarget](/windows/win32/api/d2d1/nn-d2d1-id2d1dcrendertarget) | Introduced in 10.0.10240. |
| [ID2D1Device](/windows/win32/api/d2d1_1/nn-d2d1_1-id2d1device) | Introduced in 10.0.10240. |
| [ID2D1Device1](/windows/win32/api/d2d1_2/nn-d2d1_2-id2d1device1) | Introduced in 10.0.10240. |
| [ID2D1Device2](/windows/win32/api/d2d1_3/nn-d2d1_3-id2d1device2) | Introduced in 10.0.10240. |
| [ID2D1DeviceContext](/windows/win32/api/d2d1_1/nn-d2d1_1-id2d1devicecontext) | Introduced in 10.0.10240. |
| [ID2D1DeviceContext1](/windows/win32/api/d2d1_2/nn-d2d1_2-id2d1devicecontext1) | Introduced in 10.0.10240. |
| [ID2D1DeviceContext2](/windows/win32/api/d2d1_3/nn-d2d1_3-id2d1devicecontext2) | Introduced in 10.0.10240. |
| [ID2D1DrawInfo](/windows/win32/api/d2d1effectauthor/nn-d2d1effectauthor-id2d1drawinfo) | Introduced in 10.0.10240. |
| [ID2D1DrawingStateBlock](/windows/win32/api/d2d1/nn-d2d1-id2d1drawingstateblock) | Introduced in 10.0.10240. |
| [ID2D1DrawingStateBlock1](/windows/win32/api/d2d1_1/nn-d2d1_1-id2d1drawingstateblock1) | Introduced in 10.0.10240. |
| [ID2D1DrawTransform](/windows/win32/api/d2d1effectauthor/nn-d2d1effectauthor-id2d1drawtransform) | Introduced in 10.0.10240. |
| [ID2D1Effect](/windows/win32/api/d2d1_1/nn-d2d1_1-id2d1effect) | Introduced in 10.0.10240. |
| [ID2D1EffectContext](/windows/win32/api/d2d1effectauthor/nn-d2d1effectauthor-id2d1effectcontext) | Introduced in 10.0.10240. |
| [ID2D1EffectContext1](/windows/win32/api/d2d1effectauthor_1/nn-d2d1effectauthor_1-id2d1effectcontext1) | Introduced in 10.0.10240. |
| [ID2D1EffectImpl](/windows/win32/api/d2d1effectauthor/nn-d2d1effectauthor-id2d1effectimpl) | Introduced in 10.0.10240. |
| [ID2D1EllipseGeometry](/windows/win32/api/d2d1/nn-d2d1-id2d1ellipsegeometry) | Introduced in 10.0.10240. |
| [ID2D1Factory](/windows/win32/api/d2d1/nn-d2d1-id2d1factory) | Introduced in 10.0.10240. |
| [ID2D1Factory1](/windows/win32/api/d2d1_1/nn-d2d1_1-id2d1factory1) | Introduced in 10.0.10240. |
| [ID2D1Factory2](/windows/win32/api/d2d1_2/nn-d2d1_2-id2d1factory2) | Introduced in 10.0.10240. |
| [ID2D1Factory3](/windows/win32/api/d2d1_3/nn-d2d1_3-id2d1factory3) | Introduced in 10.0.10240. |
| [ID2D1GdiMetafile](/windows/win32/api/d2d1_1/nn-d2d1_1-id2d1gdimetafile) | Introduced in 10.0.10240. |
| [ID2D1GdiMetafile1](/windows/win32/api/d2d1_3/nn-d2d1_3-id2d1gdimetafile1) | Introduced in 10.0.10240. |
| [ID2D1GdiMetafileSink](/windows/win32/api/d2d1_1/nn-d2d1_1-id2d1gdimetafilesink) | Introduced in 10.0.10240. |
| [ID2D1GdiMetafileSink1](/windows/win32/api/d2d1_3/nn-d2d1_3-id2d1gdimetafilesink1) | Introduced in 10.0.10240. |
| [ID2D1Geometry](/windows/win32/api/d2d1/nn-d2d1-id2d1geometry) | Introduced in 10.0.10240. |
| [ID2D1GeometryGroup](/windows/win32/api/d2d1/nn-d2d1-id2d1geometrygroup) | Introduced in 10.0.10240. |
| [ID2D1GeometryRealization](/windows/win32/api/d2d1_2/nn-d2d1_2-id2d1geometryrealization) | Introduced in 10.0.10240. |
| [ID2D1GeometrySink](/windows/win32/api/d2d1/nn-d2d1-id2d1geometrysink) | Introduced in 10.0.10240. |
| [ID2D1GradientMesh](/windows/win32/api/d2d1_3/nn-d2d1_3-id2d1gradientmesh) | Introduced in 10.0.10240. |
| [ID2D1GradientStopCollection](/windows/win32/api/d2d1/nn-d2d1-id2d1gradientstopcollection) | Introduced in 10.0.10240. |
| [ID2D1GradientStopCollection1](/windows/win32/api/d2d1_1/nn-d2d1_1-id2d1gradientstopcollection1) | Introduced in 10.0.10240. |
| [ID2D1HwndRenderTarget](/windows/win32/api/d2d1/nn-d2d1-id2d1hwndrendertarget) | Introduced in 10.0.10240. |
| [ID2D1Image](/windows/win32/api/d2d1/nn-d2d1-id2d1image) | Introduced in 10.0.10240. |
| [ID2D1ImageBrush](/windows/win32/api/d2d1_1/nn-d2d1_1-id2d1imagebrush) | Introduced in 10.0.10240. |
| [ID2D1ImageSource](/windows/win32/api/d2d1_3/nn-d2d1_3-id2d1imagesource) | Introduced in 10.0.10240. |
| [ID2D1ImageSourceFromWic](/windows/win32/api/d2d1_3/nn-d2d1_3-id2d1imagesourcefromwic) | Introduced in 10.0.10240. |
| [ID2D1Ink](/windows/win32/api/d2d1_3/nn-d2d1_3-id2d1ink) | Introduced in 10.0.10240. |
| [ID2D1InkStyle](/windows/win32/api/d2d1_3/nn-d2d1_3-id2d1inkstyle) | Introduced in 10.0.10240. |
| [ID2D1Layer](/windows/win32/api/d2d1/nn-d2d1-id2d1layer) | Introduced in 10.0.10240. |
| [ID2D1LinearGradientBrush](/windows/win32/api/d2d1/nn-d2d1-id2d1lineargradientbrush) | Introduced in 10.0.10240. |
| [ID2D1LookupTable3D](/windows/win32/api/d2d1_3/nn-d2d1_3-id2d1lookuptable3d) | Introduced in 10.0.10240. |
| [ID2D1Mesh](/windows/win32/api/d2d1/nn-d2d1-id2d1mesh) | Introduced in 10.0.10240. |
| [ID2D1Multithread](/windows/win32/api/d2d1_1/nn-d2d1_1-id2d1multithread) | Introduced in 10.0.10240. |
| [ID2D1OffsetTransform](/windows/win32/api/d2d1effectauthor/nn-d2d1effectauthor-id2d1offsettransform) | Introduced in 10.0.10240. |
| [ID2D1PathGeometry](/windows/win32/api/d2d1/nn-d2d1-id2d1pathgeometry) | Introduced in 10.0.10240. |
| [ID2D1PathGeometry1](/windows/win32/api/d2d1_1/nn-d2d1_1-id2d1pathgeometry1) | Introduced in 10.0.10240. |
| [ID2D1PrintControl](/windows/win32/api/d2d1_1/nn-d2d1_1-id2d1printcontrol) | Introduced in 10.0.10240. |
| [ID2D1Properties](/windows/win32/api/d2d1_1/nn-d2d1_1-id2d1properties) | Introduced in 10.0.10240. |
| [ID2D1RadialGradientBrush](/windows/win32/api/d2d1/nn-d2d1-id2d1radialgradientbrush) | Introduced in 10.0.10240. |
| [ID2D1RectangleGeometry](/windows/win32/api/d2d1/nn-d2d1-id2d1rectanglegeometry) | Introduced in 10.0.10240. |
| [ID2D1RenderInfo](/windows/win32/api/d2d1effectauthor/nn-d2d1effectauthor-id2d1renderinfo) | Introduced in 10.0.10240. |
| [ID2D1RenderTarget](/windows/win32/api/d2d1/nn-d2d1-id2d1rendertarget) | Introduced in 10.0.10240. |
| [ID2D1Resource](/windows/win32/api/d2d1/nn-d2d1-id2d1resource) | Introduced in 10.0.10240. |
| [ID2D1ResourceTexture](/windows/win32/api/d2d1effectauthor/nn-d2d1effectauthor-id2d1resourcetexture) | Introduced in 10.0.10240. |
| [ID2D1RoundedRectangleGeometry](/windows/win32/api/d2d1/nn-d2d1-id2d1roundedrectanglegeometry) | Introduced in 10.0.10240. |
| [ID2D1SimplifiedGeometrySink](/windows/win32/api/d2d1/nn-d2d1-id2d1simplifiedgeometrysink) | Introduced in 10.0.10240. |
| [ID2D1SolidColorBrush](/windows/win32/api/d2d1/nn-d2d1-id2d1solidcolorbrush) | Introduced in 10.0.10240. |
| [ID2D1SourceTransform](/windows/win32/api/d2d1effectauthor/nn-d2d1effectauthor-id2d1sourcetransform) | Introduced in 10.0.10240. |
| [ID2D1StrokeStyle](/windows/win32/api/d2d1/nn-d2d1-id2d1strokestyle) | Introduced in 10.0.10240. |
| [ID2D1StrokeStyle1](/windows/win32/api/d2d1_1/nn-d2d1_1-id2d1strokestyle1) | Introduced in 10.0.10240. |
| [ID2D1TessellationSink](/windows/win32/api/d2d1/nn-d2d1-id2d1tessellationsink) | Introduced in 10.0.10240. |
| [ID2D1Transform](/windows/win32/api/d2d1effectauthor/nn-d2d1effectauthor-id2d1transform) | Introduced in 10.0.10240. |
| [ID2D1TransformedGeometry](/windows/win32/api/d2d1/nn-d2d1-id2d1transformedgeometry) | Introduced in 10.0.10240. |
| [ID2D1TransformedImageSource](/windows/win32/api/d2d1_3/nn-d2d1_3-id2d1transformedimagesource) | Introduced in 10.0.10240. |
| [ID2D1TransformGraph](/windows/win32/api/d2d1effectauthor/nn-d2d1effectauthor-id2d1transformgraph) | Introduced in 10.0.10240. |
| [ID2D1TransformNode](/windows/win32/api/d2d1effectauthor/nn-d2d1effectauthor-id2d1transformnode) | Introduced in 10.0.10240. |
| [ID2D1VertexBuffer](/windows/win32/api/d2d1effectauthor/nn-d2d1effectauthor-id2d1vertexbuffer) | Introduced in 10.0.10240. |
| [ID3D10Blob](/windows/win32/api/d3dcommon/nn-d3dcommon-id3d10blob) | Introduced in 10.0.10240. |
| [ID3D10Multithread](/windows/win32/api/d3d10/nn-d3d10-id3d10multithread) | Introduced in 10.0.10240. |
| [ID3D11Asynchronous](/windows/win32/api/d3d11/nn-d3d11-id3d11asynchronous) | Introduced in 10.0.10240. |
| [ID3D11AuthenticatedChannel](/windows/win32/api/d3d11/nn-d3d11-id3d11authenticatedchannel) | Introduced in 10.0.10240. |
| [ID3D11BlendState](/windows/win32/api/d3d11/nn-d3d11-id3d11blendstate) | Introduced in 10.0.10240. |
| [ID3D11BlendState1](/windows/win32/api/d3d11_1/nn-d3d11_1-id3d11blendstate1) | Introduced in 10.0.10240. |
| [ID3D11Buffer](/windows/win32/api/d3d11/nn-d3d11-id3d11buffer) | Introduced in 10.0.10240. |
| [ID3D11ClassInstance](/windows/win32/api/d3d11/nn-d3d11-id3d11classinstance) | Introduced in 10.0.10240. |
| [ID3D11ClassLinkage](/windows/win32/api/d3d11/nn-d3d11-id3d11classlinkage) | Introduced in 10.0.10240. |
| [ID3D11CommandList](/windows/win32/api/d3d11/nn-d3d11-id3d11commandlist) | Introduced in 10.0.10240. |
| [ID3D11ComputeShader](/windows/win32/api/d3d11/nn-d3d11-id3d11computeshader) | Introduced in 10.0.10240. |
| [ID3D11Counter](/windows/win32/api/d3d11/nn-d3d11-id3d11counter) | Introduced in 10.0.10240. |
| [ID3D11CryptoSession](/windows/win32/api/d3d11/nn-d3d11-id3d11cryptosession) | Introduced in 10.0.10240. |
| [ID3D11Debug](/windows/win32/api/d3d11sdklayers/nn-d3d11sdklayers-id3d11debug) | Introduced in 10.0.10240. |
| [ID3D11DepthStencilState](/windows/win32/api/d3d11/nn-d3d11-id3d11depthstencilstate) | Introduced in 10.0.10240. |
| [ID3D11DepthStencilView](/windows/win32/api/d3d11/nn-d3d11-id3d11depthstencilview) | Introduced in 10.0.10240. |
| [ID3D11Device](/windows/win32/api/d3d11/nn-d3d11-id3d11device) | Introduced in 10.0.10240. |
| [ID3D11Device1](/windows/win32/api/d3d11_1/nn-d3d11_1-id3d11device1) | Introduced in 10.0.10240. |
| [ID3D11Device2](/windows/win32/api/d3d11_2/nn-d3d11_2-id3d11device2) | Introduced in 10.0.10240. |
| [ID3D11DeviceChild](/windows/win32/api/d3d11/nn-d3d11-id3d11devicechild) | Introduced in 10.0.10240. |
| [ID3D11DeviceContext](/windows/win32/api/d3d11/nn-d3d11-id3d11devicecontext) | Introduced in 10.0.10240. |
| [ID3D11DeviceContext1](/windows/win32/api/d3d11_1/nn-d3d11_1-id3d11devicecontext1) | Introduced in 10.0.10240. |
| [ID3D11DeviceContext2](/windows/win32/api/d3d11_2/nn-d3d11_2-id3d11devicecontext2) | Introduced in 10.0.10240. |
| [ID3D11DeviceContext3](/windows/win32/api/d3d11_3/nn-d3d11_3-id3d11devicecontext3) | Introduced in 10.0.10240. |
| [ID3D11Device3](/windows/win32/api/d3d11_3/nn-d3d11_3-id3d11device3) | Introduced in 10.0.10240. |
| [ID3D11Texture2D1](/windows/win32/api/d3d11_3/nn-d3d11_3-id3d11texture2d1) | Introduced in 10.0.10240. |
| [ID3D11Texture3D1](/windows/win32/api/d3d11_3/nn-d3d11_3-id3d11texture3d1) | Introduced in 10.0.10240. |
| [ID3D11DomainShader](/windows/win32/api/d3d11/nn-d3d11-id3d11domainshader) | Introduced in 10.0.10240. |
| [ID3D11FunctionLinkingGraph](/windows/win32/api/d3d11shader/nn-d3d11shader-id3d11functionlinkinggraph) | Introduced in 10.0.10240. |
| [ID3D11GeometryShader](/windows/win32/api/d3d11/nn-d3d11-id3d11geometryshader) | Introduced in 10.0.10240. |
| [ID3D11HullShader](/windows/win32/api/d3d11/nn-d3d11-id3d11hullshader) | Introduced in 10.0.10240. |
| [ID3D11InfoQueue](/windows/win32/api/d3d11sdklayers/nn-d3d11sdklayers-id3d11infoqueue) | Introduced in 10.0.10240. |
| [ID3D11InputLayout](/windows/win32/api/d3d11/nn-d3d11-id3d11inputlayout) | Introduced in 10.0.10240. |
| [ID3D11LibraryReflection](/windows/win32/api/d3d11shader/nn-d3d11shader-id3d11libraryreflection) | Introduced in 10.0.10240. |
| [ID3D11Linker](/windows/win32/api/d3d11shader/nn-d3d11shader-id3d11linker) | Introduced in 10.0.10240. |
| [ID3D11LinkingNode](/windows/win32/api/d3d11shader/nn-d3d11shader-id3d11linkingnode) | Introduced in 10.0.10240. |
| [ID3D11Module](/windows/win32/api/d3d11shader/nn-d3d11shader-id3d11module) | Introduced in 10.0.10240. |
| [ID3D11ModuleInstance](/windows/win32/api/d3d11shader/nn-d3d11shader-id3d11moduleinstance) | Introduced in 10.0.10240. |
| [ID3D11On12Device](/windows/win32/api/d3d11on12/nn-d3d11on12-id3d11on12device) | Introduced in 10.0.10240. |
| [ID3D11PixelShader](/windows/win32/api/d3d11/nn-d3d11-id3d11pixelshader) | Introduced in 10.0.10240. |
| [ID3D11Predicate](/windows/win32/api/d3d11/nn-d3d11-id3d11predicate) | Introduced in 10.0.10240. |
| [ID3D11Query](/windows/win32/api/d3d11/nn-d3d11-id3d11query) | Introduced in 10.0.10240. |
| [ID3D11Query1](/windows/win32/api/d3d11_3/nn-d3d11_3-id3d11query1) | Introduced in 10.0.10240. |
| [ID3D11RasterizerState](/windows/win32/api/d3d11/nn-d3d11-id3d11rasterizerstate) | Introduced in 10.0.10240. |
| [ID3D11RasterizerState1](/windows/win32/api/d3d11_1/nn-d3d11_1-id3d11rasterizerstate1) | Introduced in 10.0.10240. |
| [ID3D11RasterizerState2](/windows/win32/api/d3d11_3/nn-d3d11_3-id3d11rasterizerstate2) | Introduced in 10.0.10240. |
| [ID3D11RefDefaultTrackingOptions](/windows/win32/api/d3d11sdklayers/nn-d3d11sdklayers-id3d11refdefaulttrackingoptions) | Introduced in 10.0.10240. |
| [ID3D11RefTrackingOptions](/windows/win32/api/d3d11sdklayers/nn-d3d11sdklayers-id3d11reftrackingoptions) | Introduced in 10.0.10240. |
| [ID3D11RenderTargetView](/windows/win32/api/d3d11/nn-d3d11-id3d11rendertargetview) | Introduced in 10.0.10240. |
| [ID3D11RenderTargetView1](/windows/win32/api/d3d11_3/nn-d3d11_3-id3d11rendertargetview1) | Introduced in 10.0.10240. |
| [ID3D11Resource](/windows/win32/api/d3d11/nn-d3d11-id3d11resource) | Introduced in 10.0.10240. |
| [ID3D11SamplerState](/windows/win32/api/d3d11/nn-d3d11-id3d11samplerstate) | Introduced in 10.0.10240. |
| [ID3D11ShaderReflection](/windows/win32/api/d3d11shader/nn-d3d11shader-id3d11shaderreflection) | Introduced in 10.0.10240. |
| [ID3D11ShaderReflectionConstantBuffer](/windows/win32/api/d3d11shader/nn-d3d11shader-id3d11shaderreflectionconstantbuffer) | Introduced in 10.0.10240. |
| [ID3D11ShaderReflectionType](/windows/win32/api/d3d11shader/nn-d3d11shader-id3d11shaderreflectiontype) | Introduced in 10.0.10240. |
| [ID3D11ShaderReflectionVariable](/windows/win32/api/d3d11shader/nn-d3d11shader-id3d11shaderreflectionvariable) | Introduced in 10.0.10240. |
| [ID3D11ShaderResourceView](/windows/win32/api/d3d11/nn-d3d11-id3d11shaderresourceview) | Introduced in 10.0.10240. |
| [ID3D11ShaderResourceView1](/windows/win32/api/d3d11_3/nn-d3d11_3-id3d11shaderresourceview1) | Introduced in 10.0.10240. |
| [ID3D11ShaderTrace](/windows/win32/api/d3d11shadertracing/nn-d3d11shadertracing-id3d11shadertrace) | Introduced in 10.0.10240. |
| [ID3D11ShaderTraceFactory](/windows/win32/api/d3d11shadertracing/nn-d3d11shadertracing-id3d11shadertracefactory) | Introduced in 10.0.10240. |
| [ID3D11Texture1D](/windows/win32/api/d3d11/nn-d3d11-id3d11texture1d) | Introduced in 10.0.10240. |
| [ID3D11Texture2D](/windows/win32/api/d3d11/nn-d3d11-id3d11texture2d) | Introduced in 10.0.10240. |
| [ID3D11Texture3D](/windows/win32/api/d3d11/nn-d3d11-id3d11texture3d) | Introduced in 10.0.10240. |
| [ID3D11TracingDevice](/windows/win32/api/d3d11sdklayers/nn-d3d11sdklayers-id3d11tracingdevice) | Introduced in 10.0.10240. |
| [ID3D11UnorderedAccessView](/windows/win32/api/d3d11/nn-d3d11-id3d11unorderedaccessview) | Introduced in 10.0.10240. |
| [ID3D11UnorderedAccessView1](/windows/win32/api/d3d11_3/nn-d3d11_3-id3d11unorderedaccessview1) | Introduced in 10.0.10240. |
| [ID3D11VertexShader](/windows/win32/api/d3d11/nn-d3d11-id3d11vertexshader) | Introduced in 10.0.10240. |
| [ID3D11VideoContext](/windows/win32/api/d3d11/nn-d3d11-id3d11videocontext) | Introduced in 10.0.10240. |
| [ID3D11VideoContext1](/windows/win32/api/d3d11_1/nn-d3d11_1-id3d11videocontext1) | Introduced in 10.0.10240. |
| [ID3D11VideoDecoder](/windows/win32/api/d3d11/nn-d3d11-id3d11videodecoder) | Introduced in 10.0.10240. |
| [ID3D11VideoDecoderOutputView](/windows/win32/api/d3d11/nn-d3d11-id3d11videodecoderoutputview) | Introduced in 10.0.10240. |
| [ID3D11VideoDevice](/windows/win32/api/d3d11/nn-d3d11-id3d11videodevice) | Introduced in 10.0.10240. |
| [ID3D11VideoDevice1](/windows/win32/api/d3d11_1/nn-d3d11_1-id3d11videodevice1) | Introduced in 10.0.10240. |
| [ID3D11VideoProcessor](/windows/win32/api/d3d11/nn-d3d11-id3d11videoprocessor) | Introduced in 10.0.10240. |
| [ID3D11VideoProcessorEnumerator](/windows/win32/api/d3d11/nn-d3d11-id3d11videoprocessorenumerator) | Introduced in 10.0.10240. |
| [ID3D11VideoProcessorEnumerator1](/windows/win32/api/d3d11_1/nn-d3d11_1-id3d11videoprocessorenumerator1) | Introduced in 10.0.10240. |
| [ID3D11VideoProcessorInputView](/windows/win32/api/d3d11/nn-d3d11-id3d11videoprocessorinputview) | Introduced in 10.0.10240. |
| [ID3D11VideoProcessorOutputView](/windows/win32/api/d3d11/nn-d3d11-id3d11videoprocessoroutputview) | Introduced in 10.0.10240. |
| [ID3D11View](/windows/win32/api/d3d11/nn-d3d11-id3d11view) | Introduced in 10.0.10240. |
| [ID3D12CommandAllocator](/windows/win32/api/d3d12/nn-d3d12-id3d12commandallocator) | Introduced in 10.0.10240. |
| [ID3D12CommandList](/windows/win32/api/d3d12/nn-d3d12-id3d12commandlist) | Introduced in 10.0.10240. |
| [ID3D12CommandQueue](/windows/win32/api/d3d12/nn-d3d12-id3d12commandqueue) | Introduced in 10.0.10240. |
| [ID3D12CommandSignature](/windows/win32/api/d3d12/nn-d3d12-id3d12commandsignature) | Introduced in 10.0.10240. |
| [ID3D12Debug](/windows/win32/api/d3d12sdklayers/nn-d3d12sdklayers-id3d12debug) | Introduced in 10.0.10240. |
| [ID3D12DebugCommandList](/windows/win32/api/d3d12sdklayers/nn-d3d12sdklayers-id3d12debugcommandlist) | Introduced in 10.0.10240. |
| [ID3D12DebugCommandQueue](/windows/win32/api/d3d12sdklayers/nn-d3d12sdklayers-id3d12debugcommandqueue) | Introduced in 10.0.10240. |
| [ID3D12DebugDevice](/windows/win32/api/d3d12sdklayers/nn-d3d12sdklayers-id3d12debugdevice) | Introduced in 10.0.10240. |
| [ID3D12DescriptorHeap](/windows/win32/api/d3d12/nn-d3d12-id3d12descriptorheap) | Introduced in 10.0.10240. |
| [ID3D12Device](/windows/win32/api/d3d12/nn-d3d12-id3d12device) | Introduced in 10.0.10240. |
| [ID3D12DeviceChild](/windows/win32/api/d3d12/nn-d3d12-id3d12devicechild) | Introduced in 10.0.10240. |
| [ID3D12Fence](/windows/win32/api/d3d12/nn-d3d12-id3d12fence) | Introduced in 10.0.10240. |
| [ID3D12GraphicsCommandList](/windows/win32/api/d3d12/nn-d3d12-id3d12graphicscommandlist) | Introduced in 10.0.10240. |
| [ID3D12Heap](/windows/win32/api/d3d12/nn-d3d12-id3d12heap) | Introduced in 10.0.10240. |
| [ID3D12InfoQueue](/windows/win32/api/d3d12sdklayers/nn-d3d12sdklayers-id3d12infoqueue) | Introduced in 10.0.10240. |
| [ID3D12LibraryReflection](/windows/win32/api/d3d12shader/nn-d3d12shader-id3d12libraryreflection) | Introduced in 10.0.10240. |
| [ID3D12Object](/windows/win32/api/d3d12/nn-d3d12-id3d12object) | Introduced in 10.0.10240. |
| [ID3D12Pageable](/windows/win32/api/d3d12/nn-d3d12-id3d12pageable) | Introduced in 10.0.10240. |
| [ID3D12PipelineState](/windows/win32/api/d3d12/nn-d3d12-id3d12pipelinestate) | Introduced in 10.0.10240. |
| [ID3D12QueryHeap](/windows/win32/api/d3d12/nn-d3d12-id3d12queryheap) | Introduced in 10.0.10240. |
| [ID3D12Resource](/windows/win32/api/d3d12/nn-d3d12-id3d12resource) | Introduced in 10.0.10240. |
| [ID3D12RootSignature](/windows/win32/api/d3d12/nn-d3d12-id3d12rootsignature) | Introduced in 10.0.10240. |
| [ID3D12RootSignatureDeserializer](/windows/win32/api/d3d12/nn-d3d12-id3d12rootsignaturedeserializer) | Introduced in 10.0.10240. |
| [ID3D12ShaderReflection](/windows/win32/api/d3d12shader/nn-d3d12shader-id3d12shaderreflection) | Introduced in 10.0.10240. |
| [ID3DDeviceContextState](/windows/win32/api/d3d11_1/nn-d3d11_1-id3ddevicecontextstate) | Introduced in 10.0.10240. |
| [ID3DUserDefinedAnnotation](/windows/win32/api/d3d11_1/nn-d3d11_1-id3duserdefinedannotation) | Introduced in 10.0.10240. |
| [IDeviceIoControl](/windows/win32/api/deviceaccess/nn-deviceaccess-ideviceiocontrol) | Introduced in 10.0.10240. |
| [IDeviceRequestCompletionCallback](/windows/win32/api/deviceaccess/nn-deviceaccess-idevicerequestcompletioncallback) | Introduced in 10.0.10240. |
| IDirect3DDxgiInterfaceAccess | Introduced in 10.0.10240. |
| [IDirectWriterLock](/windows/win32/api/objidl/nn-objidl-idirectwriterlock) | Introduced in 10.0.10240. |
| [IDispatch](/windows/win32/api/oaidl/nn-oaidl-idispatch) | Introduced in 10.0.10240. |
| [IDockProvider](/windows/win32/api/uiautomationcore/nn-uiautomationcore-idockprovider) | Introduced in 10.0.10240. |
| [IDragProvider](/windows/win32/api/uiautomationcore/nn-uiautomationcore-idragprovider) | Introduced in 10.0.10240. |
| [IDropTargetProvider](/windows/win32/api/uiautomationcore/nn-uiautomationcore-idroptargetprovider) | Introduced in 10.0.10240. |
| [IDvdControl2](/windows/win32/api/strmif/nn-strmif-idvdcontrol2) | Introduced in 10.0.10240. |
| [IDvdInfo2](/windows/win32/api/strmif/nn-strmif-idvdinfo2) | Introduced in 10.0.10240. |
| [IDWriteBitmapRenderTarget](/windows/win32/api/dwrite/nn-dwrite-idwritebitmaprendertarget) | Introduced in 10.0.10240. |
| [IDWriteBitmapRenderTarget1](/windows/win32/api/dwrite_1/nn-dwrite_1-idwritebitmaprendertarget1) | Introduced in 10.0.10240. |
| [IDWriteColorGlyphRunEnumerator](/windows/win32/api/dwrite_2/nn-dwrite_2-idwritecolorglyphrunenumerator) | Introduced in 10.0.10240. |
| [IDWriteFactory](/windows/win32/api/dwrite/nn-dwrite-idwritefactory) | Introduced in 10.0.10240. |
| [IDWriteFactory1](/windows/win32/api/dwrite_1/nn-dwrite_1-idwritefactory1) | Introduced in 10.0.10240. |
| [IDWriteFactory2](/windows/win32/api/dwrite_2/nn-dwrite_2-idwritefactory2) | Introduced in 10.0.10240. |
| [IDWriteFactory3](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefactory3) | Introduced in 10.0.10240. |
| [IDWriteFont](/windows/win32/api/dwrite/nn-dwrite-idwritefont) | Introduced in 10.0.10240. |
| [IDWriteFont1](/windows/win32/api/dwrite_1/nn-dwrite_1-idwritefont1) | Introduced in 10.0.10240. |
| [IDWriteFont2](/windows/win32/api/dwrite_2/nn-dwrite_2-idwritefont2) | Introduced in 10.0.10240. |
| [IDWriteFont3](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefont3) | Introduced in 10.0.10240. |
| [IDWriteFontCollection](/windows/win32/api/dwrite/nn-dwrite-idwritefontcollection) | Introduced in 10.0.10240. |
| [IDWriteFontCollection1](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontcollection1) | Introduced in 10.0.10240. |
| [IDWriteFontCollectionLoader](/windows/win32/api/dwrite/nn-dwrite-idwritefontcollectionloader) | Introduced in 10.0.10240. |
| [IDWriteFontDownloadListener](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontdownloadlistener) | Introduced in 10.0.10240. |
| [IDWriteFontDownloadQueue](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontdownloadqueue) | Introduced in 10.0.10240. |
| [IDWriteFontFace](/windows/win32/api/dwrite/nn-dwrite-idwritefontface) | Introduced in 10.0.10240. |
| [IDWriteFontFace1](/windows/win32/api/dwrite_1/nn-dwrite_1-idwritefontface1) | Introduced in 10.0.10240. |
| [IDWriteFontFace2](/windows/win32/api/dwrite_2/nn-dwrite_2-idwritefontface2) | Introduced in 10.0.10240. |
| [IDWriteFontFace3](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontface3) | Introduced in 10.0.10240. |
| [IDWriteFontFaceReference](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontfacereference) | Introduced in 10.0.10240. |
| [IDWriteFontFallback](/windows/win32/api/dwrite_2/nn-dwrite_2-idwritefontfallback) | Introduced in 10.0.10240. |
| [IDWriteFontFallbackBuilder](/windows/win32/api/dwrite_2/nn-dwrite_2-idwritefontfallbackbuilder) | Introduced in 10.0.10240. |
| [IDWriteFontFamily](/windows/win32/api/dwrite/nn-dwrite-idwritefontfamily) | Introduced in 10.0.10240. |
| [IDWriteFontFamily1](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontfamily1) | Introduced in 10.0.10240. |
| [IDWriteFontFile](/windows/win32/api/dwrite/nn-dwrite-idwritefontfile) | Introduced in 10.0.10240. |
| [IDWriteFontFileEnumerator](/windows/win32/api/dwrite/nn-dwrite-idwritefontfileenumerator) | Introduced in 10.0.10240. |
| [IDWriteFontFileLoader](/windows/win32/api/dwrite/nn-dwrite-idwritefontfileloader) | Introduced in 10.0.10240. |
| [IDWriteFontFileStream](/windows/win32/api/dwrite/nn-dwrite-idwritefontfilestream) | Introduced in 10.0.10240. |
| [IDWriteFontList](/windows/win32/api/dwrite/nn-dwrite-idwritefontlist) | Introduced in 10.0.10240. |
| [IDWriteFontList1](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontlist1) | Introduced in 10.0.10240. |
| [IDWriteFontSet](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontset) | Introduced in 10.0.10240. |
| [IDWriteFontSetBuilder](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritefontsetbuilder) | Introduced in 10.0.10240. |
| [IDWriteGdiInterop](/windows/win32/api/dwrite/nn-dwrite-idwritegdiinterop) | Introduced in 10.0.10240. |
| [IDWriteGdiInterop1](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritegdiinterop1) | Introduced in 10.0.10240. |
| [IDWriteGlyphRunAnalysis](/windows/win32/api/dwrite/nn-dwrite-idwriteglyphrunanalysis) | Introduced in 10.0.10240. |
| [IDWriteInlineObject](/windows/win32/api/dwrite/nn-dwrite-idwriteinlineobject) | Introduced in 10.0.10240. |
| [IDWriteLocalFontFileLoader](/windows/win32/api/dwrite/nn-dwrite-idwritelocalfontfileloader) | Introduced in 10.0.10240. |
| [IDWriteLocalizedStrings](/windows/win32/api/dwrite/nn-dwrite-idwritelocalizedstrings) | Introduced in 10.0.10240. |
| [IDWriteNumberSubstitution](/windows/win32/api/dwrite/nn-dwrite-idwritenumbersubstitution) | Introduced in 10.0.10240. |
| [IDWritePixelSnapping](/windows/win32/api/dwrite/nn-dwrite-idwritepixelsnapping) | Introduced in 10.0.10240. |
| [IDWriteRenderingParams](/windows/win32/api/dwrite/nn-dwrite-idwriterenderingparams) | Introduced in 10.0.10240. |
| [IDWriteRenderingParams1](/windows/win32/api/dwrite_1/nn-dwrite_1-idwriterenderingparams1) | Introduced in 10.0.10240. |
| [IDWriteRenderingParams2](/windows/win32/api/dwrite_2/nn-dwrite_2-idwriterenderingparams2) | Introduced in 10.0.10240. |
| [IDWriteRenderingParams3](/windows/win32/api/dwrite_3/nn-dwrite_3-idwriterenderingparams3) | Introduced in 10.0.10240. |
| [IDWriteStringList](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritestringlist) | Introduced in 10.0.10240. |
| [IDWriteTextAnalysisSink](/windows/win32/api/dwrite/nn-dwrite-idwritetextanalysissink) | Introduced in 10.0.10240. |
| [IDWriteTextAnalysisSink1](/windows/win32/api/dwrite_1/nn-dwrite_1-idwritetextanalysissink1) | Introduced in 10.0.10240. |
| [IDWriteTextAnalysisSource](/windows/win32/api/dwrite/nn-dwrite-idwritetextanalysissource) | Introduced in 10.0.10240. |
| [IDWriteTextAnalysisSource1](/windows/win32/api/dwrite_1/nn-dwrite_1-idwritetextanalysissource1) | Introduced in 10.0.10240. |
| [IDWriteTextAnalyzer](/windows/win32/api/dwrite/nn-dwrite-idwritetextanalyzer) | Introduced in 10.0.10240. |
| [IDWriteTextAnalyzer1](/windows/win32/api/dwrite_1/nn-dwrite_1-idwritetextanalyzer1) | Introduced in 10.0.10240. |
| [IDWriteTextAnalyzer2](/windows/win32/api/dwrite_2/nn-dwrite_2-idwritetextanalyzer2) | Introduced in 10.0.10240. |
| [IDWriteTextFormat](/windows/win32/api/dwrite/nn-dwrite-idwritetextformat) | Introduced in 10.0.10240. |
| [IDWriteTextFormat1](/windows/win32/api/dwrite_2/nn-dwrite_2-idwritetextformat1) | Introduced in 10.0.10240. |
| [IDWriteTextFormat2](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritetextformat2) | Introduced in 10.0.10240. |
| [IDWriteTextLayout](/windows/win32/api/dwrite/nn-dwrite-idwritetextlayout) | Introduced in 10.0.10240. |
| [IDWriteTextLayout1](/windows/win32/api/dwrite_1/nn-dwrite_1-idwritetextlayout1) | Introduced in 10.0.10240. |
| [IDWriteTextLayout2](/windows/win32/api/dwrite_2/nn-dwrite_2-idwritetextlayout2) | Introduced in 10.0.10240. |
| [IDWriteTextLayout3](/windows/win32/api/dwrite_3/nn-dwrite_3-idwritetextlayout3) | Introduced in 10.0.10240. |
| [IDWriteTextRenderer](/windows/win32/api/dwrite/nn-dwrite-idwritetextrenderer) | Introduced in 10.0.10240. |
| [IDWriteTextRenderer1](/windows/win32/api/dwrite_2/nn-dwrite_2-idwritetextrenderer1) | Introduced in 10.0.10240. |
| [IDWriteTypography](/windows/win32/api/dwrite/nn-dwrite-idwritetypography) | Introduced in 10.0.10240. |
| [IDXGIAdapter](/windows/win32/api/dxgi/nn-dxgi-idxgiadapter) | Introduced in 10.0.10240. |
| [IDXGIAdapter1](/windows/win32/api/dxgi/nn-dxgi-idxgiadapter1) | Introduced in 10.0.10240. |
| [IDXGIAdapter2](/windows/win32/api/dxgi1_2/nn-dxgi1_2-idxgiadapter2) | Introduced in 10.0.10240. |
| [IDXGIAdapter3](/windows/win32/api/dxgi1_4/nn-dxgi1_4-idxgiadapter3) | Introduced in 10.0.10240. |
| [IDXGIDebug](/windows/win32/api/dxgidebug/nn-dxgidebug-idxgidebug) | Introduced in 10.0.10240. |
| [IDXGIDebug1](/windows/win32/api/dxgidebug/nn-dxgidebug-idxgidebug1) | Introduced in 10.0.10240. |
| [IDXGIDevice](/windows/win32/api/dxgi/nn-dxgi-idxgidevice) | Introduced in 10.0.10240. |
| [IDXGIDevice1](/windows/win32/api/dxgi/nn-dxgi-idxgidevice1) | Introduced in 10.0.10240. |
| [IDXGIDevice2](/windows/win32/api/dxgi1_2/nn-dxgi1_2-idxgidevice2) | Introduced in 10.0.10240. |
| [IDXGIDevice3](/windows/win32/api/dxgi1_3/nn-dxgi1_3-idxgidevice3) | Introduced in 10.0.10240. |
| [IDXGIDeviceSubObject](/windows/win32/api/dxgi/nn-dxgi-idxgidevicesubobject) | Introduced in 10.0.10240. |
| [IDXGIFactory](/windows/win32/api/dxgi/nn-dxgi-idxgifactory) | Introduced in 10.0.10240. |
| [IDXGIFactory1](/windows/win32/api/dxgi/nn-dxgi-idxgifactory1) | Introduced in 10.0.10240. |
| [IDXGIFactory2](/windows/win32/api/dxgi1_2/nn-dxgi1_2-idxgifactory2) | Introduced in 10.0.10240. |
| [IDXGIFactory3](/windows/win32/api/dxgi1_3/nn-dxgi1_3-idxgifactory3) | Introduced in 10.0.10240. |
| [IDXGIFactory4](/windows/win32/api/dxgi1_4/nn-dxgi1_4-idxgifactory4) | Introduced in 10.0.10240. |
| [IDXGIInfoQueue](/windows/win32/api/dxgidebug/nn-dxgidebug-idxgiinfoqueue) | Introduced in 10.0.10240. |
| [IDXGIKeyedMutex](/windows/win32/api/dxgi/nn-dxgi-idxgikeyedmutex) | Introduced in 10.0.10240. |
| [IDXGIObject](/windows/win32/api/dxgi/nn-dxgi-idxgiobject) | Introduced in 10.0.10240. |
| [IDXGIOutput](/windows/win32/api/dxgi/nn-dxgi-idxgioutput) | Introduced in 10.0.10240. |
| [IDXGIOutput1](/windows/win32/api/dxgi1_2/nn-dxgi1_2-idxgioutput1) | Introduced in 10.0.10240. |
| [IDXGIOutput2](/windows/win32/api/dxgi1_3/nn-dxgi1_3-idxgioutput2) | Introduced in 10.0.10240. |
| [IDXGIOutput3](/windows/win32/api/dxgi1_3/nn-dxgi1_3-idxgioutput3) | Introduced in 10.0.10240. |
| [IDXGIOutput4](/windows/win32/api/dxgi1_4/nn-dxgi1_4-idxgioutput4) | Introduced in 10.0.10240. |
| [IDXGIResource](/windows/win32/api/dxgi/nn-dxgi-idxgiresource) | Introduced in 10.0.10240. |
| [IDXGIResource1](/windows/win32/api/dxgi1_2/nn-dxgi1_2-idxgiresource1) | Introduced in 10.0.10240. |
| [IDXGISurface](/windows/win32/api/dxgi/nn-dxgi-idxgisurface) | Introduced in 10.0.10240. |
| [IDXGISurface1](/windows/win32/api/dxgi/nn-dxgi-idxgisurface1) | Introduced in 10.0.10240. |
| [IDXGISurface2](/windows/win32/api/dxgi1_2/nn-dxgi1_2-idxgisurface2) | Introduced in 10.0.10240. |
| [IDXGISwapChain](/windows/win32/api/dxgi/nn-dxgi-idxgiswapchain) | Introduced in 10.0.10240. |
| [IDXGISwapChain1](/windows/win32/api/dxgi1_2/nn-dxgi1_2-idxgiswapchain1) | Introduced in 10.0.10240. |
| [IDXGISwapChain2](/windows/win32/api/dxgi1_3/nn-dxgi1_3-idxgiswapchain2) | Introduced in 10.0.10240. |
| [IDXGISwapChain3](/windows/win32/api/dxgi1_4/nn-dxgi1_4-idxgiswapchain3) | Introduced in 10.0.10240. |
| [IEditionUpgradeHelper](/windows/win32/api/editionupgradehelper/nn-editionupgradehelper-ieditionupgradehelper) | Introduced in 10.0.10240. |
| [IEnumCodePage](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa741101(v=vs.85)) | Introduced in 10.0.10240. |
| [IEnumConnectionPoints](/windows/win32/api/ocidl/nn-ocidl-ienumconnectionpoints) | Introduced in 10.0.10240. |
| [IEnumConnections](/windows/win32/api/ocidl/nn-ocidl-ienumconnections) | Introduced in 10.0.10240. |
| [IEnumGUID](/windows/win32/api/comcat/nn-comcat-ienumguid) | Introduced in 10.0.10240. |
| [IEnumITfCompositionView](/windows/win32/api/msctf/nn-msctf-ienumitfcompositionview) | Introduced in 10.0.10240. |
| [IEnumMoniker](/windows/win32/api/objidl/nn-objidl-ienummoniker) | Introduced in 10.0.10240. |
| [IEnumPortableDeviceObjectIDs](/windows/win32/api/portabledeviceapi/nn-portabledeviceapi-ienumportabledeviceobjectids) | Introduced in 10.0.10240. |
| [IEnumRfc1766](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa741095(v=vs.85)) | Introduced in 10.0.10240. |
| [IEnumScript](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa741082(v=vs.85)) | Introduced in 10.0.10240. |
| [IEnumSpellingError](/windows/win32/api/spellcheck/nn-spellcheck-ienumspellingerror) | Introduced in 10.0.10240. |
| [IEnumSTATDATA](/windows/win32/api/objidl/nn-objidl-ienumstatdata) | Introduced in 10.0.10240. |
| [IEnumSTATPROPSETSTG](/windows/win32/api/propidlbase/nn-propidlbase-ienumstatpropsetstg) | Introduced in 10.0.10240. |
| [IEnumSTATPROPSTG](/windows/win32/api/propidlbase/nn-propidlbase-ienumstatpropstg) | Introduced in 10.0.10240. |
| [IEnumSTATSTG](/windows/win32/api/objidl/nn-objidl-ienumstatstg) | Introduced in 10.0.10240. |
| [IEnumString](/windows/win32/api/objidlbase/nn-objidlbase-ienumstring) | Introduced in 10.0.10240. |
| [IEnumTfCandidates](/windows/win32/api/ctffunc/nn-ctffunc-ienumtfcandidates) | Introduced in 10.0.10240. |
| [IEnumTfContexts](/windows/win32/api/msctf/nn-msctf-ienumtfcontexts) | Introduced in 10.0.10240. |
| [IEnumTfContextViews](/windows/win32/api/msctf/nn-msctf-ienumtfcontextviews) | Introduced in 10.0.10240. |
| [IEnumTfDisplayAttributeInfo](/windows/win32/api/msctf/nn-msctf-ienumtfdisplayattributeinfo) | Introduced in 10.0.10240. |
| [IEnumTfDocumentMgrs](/windows/win32/api/msctf/nn-msctf-ienumtfdocumentmgrs) | Introduced in 10.0.10240. |
| [IEnumTfFunctionProviders](/windows/win32/api/msctf/nn-msctf-ienumtffunctionproviders) | Introduced in 10.0.10240. |
| [IEnumTfInputProcessorProfiles](/windows/win32/api/msctf/nn-msctf-ienumtfinputprocessorprofiles) | Introduced in 10.0.10240. |
| [IEnumTfProperties](/windows/win32/api/msctf/nn-msctf-ienumtfproperties) | Introduced in 10.0.10240. |
| [IEnumTfPropertyValue](/windows/win32/api/msctf/nn-msctf-ienumtfpropertyvalue) | Introduced in 10.0.10240. |
| [IEnumTfRanges](/windows/win32/api/msctf/nn-msctf-ienumtfranges) | Introduced in 10.0.10240. |
| [IEnumTfUIElements](/windows/win32/api/msctf/nn-msctf-ienumtfuielements) | Introduced in 10.0.10240. |
| [IEnumUnknown](/windows/win32/api/objidlbase/nn-objidlbase-ienumunknown) | Introduced in 10.0.10240. |
| [IEnumVARIANT](/windows/win32/api/oaidl/nn-oaidl-ienumvariant) | Introduced in 10.0.10240. |
| [IExpandCollapseProvider](/windows/win32/api/uiautomationcore/nn-uiautomationcore-iexpandcollapseprovider) | Introduced in 10.0.10240. |
| [IFillLockBytes](/windows/win32/api/objidl/nn-objidl-ifilllockbytes) | Introduced in 10.0.10240. |
| [IFindReferenceTargetsCallback](/windows/win32/api/windows.ui.xaml.hosting.referencetracker/nn-windows-ui-xaml-hosting-referencetracker-ifindreferencetargetscallback) | Introduced in 10.0.10240. |
| [IGlobalInterfaceTable](/windows/win32/api/objidl/nn-objidl-iglobalinterfacetable) | Introduced in 10.0.10240. |
| [IGlobalOptions](/windows/win32/api/objidlbase/nn-objidlbase-iglobaloptions) | Introduced in 10.0.10240. |
| [IGridItemProvider](/windows/win32/api/uiautomationcore/nn-uiautomationcore-igriditemprovider) | Introduced in 10.0.10240. |
| [IGridProvider](/windows/win32/api/uiautomationcore/nn-uiautomationcore-igridprovider) | Introduced in 10.0.10240. |
| [IInkD2DRenderer](/windows/win32/api/inkrenderer/nn-inkrenderer-iinkd2drenderer) | Introduced in 10.0.10240. |
| [IInspectable](/windows/win32/api/inspectable/nn-inspectable-iinspectable) | Introduced in 10.0.10240. |
| [IInvokeProvider](/windows/win32/api/uiautomationcore/nn-uiautomationcore-iinvokeprovider) | Introduced in 10.0.10240. |
| [IItemContainerProvider](/windows/win32/api/uiautomationcore/nn-uiautomationcore-iitemcontainerprovider) | Introduced in 10.0.10240. |
| [ILanguageExceptionErrorInfo](/windows/win32/api/restrictederrorinfo/nn-restrictederrorinfo-ilanguageexceptionerrorinfo) | Introduced in 10.0.10240. |
| [ILayoutStorage](/windows/win32/api/objidl/nn-objidl-ilayoutstorage) | Introduced in 10.0.10240. |
| [ILegacyIAccessibleProvider](/windows/win32/api/uiautomationcore/nn-uiautomationcore-ilegacyiaccessibleprovider) | Introduced in 10.0.10240. |
| [ILockBytes](/windows/win32/api/objidl/nn-objidl-ilockbytes) | Introduced in 10.0.10240. |
| [IMarshal](/previous-versions//ms688712(v=vs.85)) | Introduced in 10.0.10240. |
| [IMbnConnection](/windows/win32/api/mbnapi/nn-mbnapi-imbnconnection) | Introduced in 10.0.10240. |
| [IMbnConnectionEvents](/windows/win32/api/mbnapi/nn-mbnapi-imbnconnectionevents) | Introduced in 10.0.10240. |
| [IMbnConnectionManager](/windows/win32/api/mbnapi/nn-mbnapi-imbnconnectionmanager) | Introduced in 10.0.10240. |
| [IMbnConnectionManagerEvents](/windows/win32/api/mbnapi/nn-mbnapi-imbnconnectionmanagerevents) | Introduced in 10.0.10240. |
| [IMbnDeviceService](/windows/win32/api/mbnapi/nn-mbnapi-imbndeviceservice) | Introduced in 10.0.10240. |
| [IMbnDeviceServicesContext](/windows/win32/api/mbnapi/nn-mbnapi-imbndeviceservicescontext) | Introduced in 10.0.10240. |
| [IMbnDeviceServicesEvents](/windows/win32/api/mbnapi/nn-mbnapi-imbndeviceservicesevents) | Introduced in 10.0.10240. |
| [IMbnDeviceServicesManager](/windows/win32/api/mbnapi/nn-mbnapi-imbndeviceservicesmanager) | Introduced in 10.0.10240. |
| [IMbnInterface](/windows/win32/api/mbnapi/nn-mbnapi-imbninterface) | Introduced in 10.0.10240. |
| [IMbnInterfaceEvents](/windows/win32/api/mbnapi/nn-mbnapi-imbninterfaceevents) | Introduced in 10.0.10240. |
| [IMbnInterfaceManager](/windows/win32/api/mbnapi/nn-mbnapi-imbninterfacemanager) | Introduced in 10.0.10240. |
| [IMbnInterfaceManagerEvents](/windows/win32/api/mbnapi/nn-mbnapi-imbninterfacemanagerevents) | Introduced in 10.0.10240. |
| [IMbnPin](/windows/win32/api/mbnapi/nn-mbnapi-imbnpin) | Introduced in 10.0.10240. |
| [IMbnPinEvents](/windows/win32/api/mbnapi/nn-mbnapi-imbnpinevents) | Introduced in 10.0.10240. |
| [IMbnPinManager](/windows/win32/api/mbnapi/nn-mbnapi-imbnpinmanager) | Introduced in 10.0.10240. |
| [IMbnPinManagerEvents](/windows/win32/api/mbnapi/nn-mbnapi-imbnpinmanagerevents) | Introduced in 10.0.10240. |
| [IMbnRegistration](/windows/win32/api/mbnapi/nn-mbnapi-imbnregistration) | Introduced in 10.0.10240. |
| [IMbnRegistrationEvents](/windows/win32/api/mbnapi/nn-mbnapi-imbnregistrationevents) | Introduced in 10.0.10240. |
| [IMetaDataAssemblyImport](/windows/win32/api/rometadataapi/nn-rometadataapi-imetadataassemblyimport) | Introduced in 10.0.10240. |
| [IMetaDataDispenser](/windows/win32/api/rometadataapi/nn-rometadataapi-imetadatadispenser) | Introduced in 10.0.10240. |
| [IMetaDataDispenserEx](/windows/win32/api/rometadataapi/nn-rometadataapi-imetadatadispenserex) | Introduced in 10.0.10240. |
| [IMetaDataImport](/windows/win32/api/rometadataapi/nn-rometadataapi-imetadataimport) | Introduced in 10.0.10240. |
| [IMetaDataImport2](/windows/win32/api/rometadataapi/nn-rometadataapi-imetadataimport2) | Introduced in 10.0.10240. |
| [IMetaDataTables](/windows/win32/api/rometadataapi/nn-rometadataapi-imetadatatables) | Introduced in 10.0.10240. |
| [IMetaDataTables2](/windows/win32/api/rometadataapi/nn-rometadataapi-imetadatatables2) | Introduced in 10.0.10240. |
| [IMF2DBuffer](/windows/win32/api/mfobjects/nn-mfobjects-imf2dbuffer) | Introduced in 10.0.10240. |
| [IMF2DBuffer2](/windows/win32/api/mfobjects/nn-mfobjects-imf2dbuffer2) | Introduced in 10.0.10240. |
| [IMFActivate](/windows/win32/api/mfobjects/nn-mfobjects-imfactivate) | Introduced in 10.0.10240. |
| [IMFAsyncCallback](/windows/win32/api/mfobjects/nn-mfobjects-imfasynccallback) | Introduced in 10.0.10240. |
| [IMFAsyncResult](/windows/win32/api/mfobjects/nn-mfobjects-imfasyncresult) | Introduced in 10.0.10240. |
| [IMFAttributes](/windows/win32/api/mfobjects/nn-mfobjects-imfattributes) | Introduced in 10.0.10240. |
| [IMFByteStream](/windows/win32/api/mfobjects/nn-mfobjects-imfbytestream) | Introduced in 10.0.10240. |
| [IMFByteStreamBuffering](/windows/win32/api/mfidl/nn-mfidl-imfbytestreambuffering) | Introduced in 10.0.10240. |
| [IMFByteStreamCacheControl](/windows/win32/api/mfidl/nn-mfidl-imfbytestreamcachecontrol) | Introduced in 10.0.10240. |
| [IMFByteStreamCacheControl2](/windows/win32/api/mfidl/nn-mfidl-imfbytestreamcachecontrol2) | Introduced in 10.0.10240. |
| [IMFByteStreamTimeSeek](/windows/win32/api/mfidl/nn-mfidl-imfbytestreamtimeseek) | Introduced in 10.0.10240. |
| [IMFClock](/windows/win32/api/mfidl/nn-mfidl-imfclock) | Introduced in 10.0.10240. |
| [IMFClockStateSink](/windows/win32/api/mfidl/nn-mfidl-imfclockstatesink) | Introduced in 10.0.10240. |
| [IMFCollection](/windows/win32/api/mfobjects/nn-mfobjects-imfcollection) | Introduced in 10.0.10240. |
| [IMFContentDecryptorContext](/windows/win32/api/mfidl/nn-mfidl-imfcontentdecryptorcontext) | Introduced in 10.0.10240. |
| [IMFContentProtectionDevice](/windows/win32/api/mfidl/nn-mfidl-imfcontentprotectiondevice) | Introduced in 10.0.10240. |
| [IMFDXGIBuffer](/windows/win32/api/mfobjects/nn-mfobjects-imfdxgibuffer) | Introduced in 10.0.10240. |
| [IMFDXGIDeviceManager](/windows/win32/api/mfobjects/nn-mfobjects-imfdxgidevicemanager) | Introduced in 10.0.10240. |
| [IMFDXGIDeviceManagerSource](/windows/win32/api/mfidl/nn-mfidl-imfdxgidevicemanagersource) | Introduced in 10.0.10240. |
| [IMFGetService](/windows/win32/api/mfidl/nn-mfidl-imfgetservice) | Introduced in 10.0.10240. |
| [IMFInputTrustAuthority](/windows/win32/api/mfidl/nn-mfidl-imfinputtrustauthority) | Introduced in 10.0.10240. |
| [IMFMediaBuffer](/windows/win32/api/mfobjects/nn-mfobjects-imfmediabuffer) | Introduced in 10.0.10240. |
| [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine) | Introduced in 10.0.10240. |
| [IMFMediaEngineClassFactory](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengineclassfactory) | Introduced in 10.0.10240. |
| [IMFMediaEngineEx](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengineex) | Introduced in 10.0.10240. |
| [IMFMediaEngineExtension](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengineextension) | Introduced in 10.0.10240. |
| [IMFMediaEngineNotify](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaenginenotify) | Introduced in 10.0.10240. |
| [IMFMediaEngineProtectedContent](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengineprotectedcontent) | Introduced in 10.0.10240. |
| [IMFMediaEngineSrcElements](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaenginesrcelements) | Introduced in 10.0.10240. |
| [IMFMediaError](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaerror) | Introduced in 10.0.10240. |
| [IMFMediaEvent](/windows/win32/api/mfobjects/nn-mfobjects-imfmediaevent) | Introduced in 10.0.10240. |
| [IMFMediaEventGenerator](/windows/win32/api/mfobjects/nn-mfobjects-imfmediaeventgenerator) | Introduced in 10.0.10240. |
| [IMFMediaEventQueue](/windows/win32/api/mfobjects/nn-mfobjects-imfmediaeventqueue) | Introduced in 10.0.10240. |
| [IMFMediaSink](/windows/win32/api/mfidl/nn-mfidl-imfmediasink) | Introduced in 10.0.10240. |
| [IMFMediaSinkPreroll](/windows/win32/api/mfidl/nn-mfidl-imfmediasinkpreroll) | Introduced in 10.0.10240. |
| [IMFMediaSource](/windows/win32/api/mfidl/nn-mfidl-imfmediasource) | Introduced in 10.0.10240. |
| [IMFMediaSourceEx](/windows/win32/api/mfidl/nn-mfidl-imfmediasourceex) | Introduced in 10.0.10240. |
| [IMFMediaStream](/windows/win32/api/mfidl/nn-mfidl-imfmediastream) | Introduced in 10.0.10240. |
| [IMFMediaStreamSourceSampleRequest](/windows/win32/api/mfidl/nn-mfidl-imfmediastreamsourcesamplerequest) | Introduced in 10.0.10240. |
| [IMFMediaTimeRange](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediatimerange) | Introduced in 10.0.10240. |
| [IMFMediaType](/windows/win32/api/mfobjects/nn-mfobjects-imfmediatype) | Introduced in 10.0.10240. |
| [IMFMediaTypeHandler](/windows/win32/api/mfidl/nn-mfidl-imfmediatypehandler) | Introduced in 10.0.10240. |
| [IMFMetadata](/windows/win32/api/mfidl/nn-mfidl-imfmetadata) | Introduced in 10.0.10240. |
| [IMFMetadataProvider](/windows/win32/api/mfidl/nn-mfidl-imfmetadataprovider) | Introduced in 10.0.10240. |
| [IMFOutputPolicy](/windows/win32/api/mfidl/nn-mfidl-imfoutputpolicy) | Introduced in 10.0.10240. |
| [IMFOutputSchema](/windows/win32/api/mfidl/nn-mfidl-imfoutputschema) | Introduced in 10.0.10240. |
| [IMFOutputTrustAuthority](/windows/win32/api/mfidl/nn-mfidl-imfoutputtrustauthority) | Introduced in 10.0.10240. |
| [IMFPMPClientApp](/windows/win32/api/mfidl/nn-mfidl-imfpmpclientapp) | Introduced in 10.0.10240. |
| [IMFPMPHostApp](/windows/win32/api/mfidl/nn-mfidl-imfpmphostapp) | Introduced in 10.0.10240. |
| [IMFPresentationClock](/windows/win32/api/mfidl/nn-mfidl-imfpresentationclock) | Introduced in 10.0.10240. |
| [IMFPresentationDescriptor](/windows/win32/api/mfidl/nn-mfidl-imfpresentationdescriptor) | Introduced in 10.0.10240. |
| [IMFPresentationTimeSource](/windows/win32/api/mfidl/nn-mfidl-imfpresentationtimesource) | Introduced in 10.0.10240. |
| [IMFProtectedEnvironmentAccess](/windows/win32/api/mfidl/nn-mfidl-imfprotectedenvironmentaccess) | Introduced in 10.0.10240. |
| [IMFQualityAdvise](/windows/win32/api/mfidl/nn-mfidl-imfqualityadvise) | Introduced in 10.0.10240. |
| [IMFQualityAdvise2](/windows/win32/api/mfidl/nn-mfidl-imfqualityadvise2) | Introduced in 10.0.10240. |
| [IMFQualityAdviseLimits](/windows/win32/api/mfidl/nn-mfidl-imfqualityadviselimits) | Introduced in 10.0.10240. |
| [IMFRateControl](/windows/win32/api/mfidl/nn-mfidl-imfratecontrol) | Introduced in 10.0.10240. |
| [IMFRateSupport](/windows/win32/api/mfidl/nn-mfidl-imfratesupport) | Introduced in 10.0.10240. |
| [IMFReadWriteClassFactory](/windows/win32/api/mfreadwrite/nn-mfreadwrite-imfreadwriteclassfactory) | Introduced in 10.0.10240. |
| [IMFRealTimeClientEx](/windows/win32/api/mfidl/nn-mfidl-imfrealtimeclientex) | Introduced in 10.0.10240. |
| [IMFSample](/windows/win32/api/mfobjects/nn-mfobjects-imfsample) | Introduced in 10.0.10240. |
| [IMFSampleOutputStream](/windows/win32/api/mfobjects/nn-mfobjects-imfsampleoutputstream) | Introduced in 10.0.10240. |
| [IMFSampleProtection](/windows/win32/api/mfidl/nn-mfidl-imfsampleprotection) | Introduced in 10.0.10240. |
| [IMFSchemeHandler](/windows/win32/api/mfidl/nn-mfidl-imfschemehandler) | Introduced in 10.0.10240. |
| [IMFSeekInfo](/windows/win32/api/mfidl/nn-mfidl-imfseekinfo) | Introduced in 10.0.10240. |
| [IMFShutdown](/windows/win32/api/mfidl/nn-mfidl-imfshutdown) | Introduced in 10.0.10240. |
| [IMFSignedLibrary](/windows/win32/api/mfidl/nn-mfidl-imfsignedlibrary) | Introduced in 10.0.10240. |
| [IMFSinkWriter](/windows/win32/api/mfreadwrite/nn-mfreadwrite-imfsinkwriter) | Introduced in 10.0.10240. |
| [IMFSinkWriterCallback](/windows/win32/api/mfreadwrite/nn-mfreadwrite-imfsinkwritercallback) | Introduced in 10.0.10240. |
| [IMFSinkWriterCallback2](/windows/win32/api/mfreadwrite/nn-mfreadwrite-imfsinkwritercallback2) | Introduced in 10.0.10240. |
| [IMFSinkWriterEx](/windows/win32/api/mfreadwrite/nn-mfreadwrite-imfsinkwriterex) | Introduced in 10.0.10240. |
| [IMFSinkWriterEncoderConfig](/windows/win32/api/mfreadwrite/nn-mfreadwrite-imfsinkwriterencoderconfig) | Introduced in 10.0.10240. |
| [IMFSourceReader](/windows/win32/api/mfreadwrite/nn-mfreadwrite-imfsourcereader) | Introduced in 10.0.10240. |
| [IMFSourceReaderCallback](/windows/win32/api/mfreadwrite/nn-mfreadwrite-imfsourcereadercallback) | Introduced in 10.0.10240. |
| [IMFSourceReaderCallback2](/windows/win32/api/mfreadwrite/nn-mfreadwrite-imfsourcereadercallback2) | Introduced in 10.0.10240. |
| [IMFSourceReaderEx](/windows/win32/api/mfreadwrite/nn-mfreadwrite-imfsourcereaderex) | Introduced in 10.0.10240. |
| [IMFSourceResolver](/windows/win32/api/mfidl/nn-mfidl-imfsourceresolver) | Introduced in 10.0.10240. |
| [IMFStreamDescriptor](/windows/win32/api/mfidl/nn-mfidl-imfstreamdescriptor) | Introduced in 10.0.10240. |
| [IMFStreamingSinkConfig](/windows/win32/api/mfidl/nn-mfidl-imfstreamingsinkconfig) | Introduced in 10.0.10240. |
| [IMFStreamSink](/windows/win32/api/mfidl/nn-mfidl-imfstreamsink) | Introduced in 10.0.10240. |
| [IMFSystemId](/windows/win32/api/mfidl/nn-mfidl-imfsystemid) | Introduced in 10.0.10240. |
| [IMFTrackedSample](/windows/win32/api/mfidl/nn-mfidl-imftrackedsample) | Introduced in 10.0.10240. |
| [IMFTransform](/windows/win32/api/mftransform/nn-mftransform-imftransform) | Introduced in 10.0.10240. |
| [IMFTrustedInput](/windows/win32/api/mfidl/nn-mfidl-imftrustedinput) | Introduced in 10.0.10240. |
| [IMFTrustedOutput](/windows/win32/api/mfidl/nn-mfidl-imftrustedoutput) | Introduced in 10.0.10240. |
| [IMFVideoSampleAllocator](/windows/win32/api/mfidl/nn-mfidl-imfvideosampleallocator) | Introduced in 10.0.10240. |
| [IMFVideoSampleAllocatorCallback](/windows/win32/api/mfidl/nn-mfidl-imfvideosampleallocatorcallback) | Introduced in 10.0.10240. |
| [IMFVideoSampleAllocatorEx](/windows/win32/api/mfidl/nn-mfidl-imfvideosampleallocatorex) | Introduced in 10.0.10240. |
| [IMFVideoSampleAllocatorNotify](/windows/win32/api/mfidl/nn-mfidl-imfvideosampleallocatornotify) | Introduced in 10.0.10240. |
| [IMFVideoSampleAllocatorNotifyEx](/windows/win32/api/mfidl/nn-mfidl-imfvideosampleallocatornotifyex) | Introduced in 10.0.10240. |
| [IMFVideoProcessorControl](/windows/win32/api/mfidl/nn-mfidl-imfvideoprocessorcontrol) | Introduced in 10.0.10240. |
| [IMFVideoProcessorControl2](/windows/win32/api/mfidl/nn-mfidl-imfvideoprocessorcontrol2) | Introduced in 10.0.10240. |
| [IMLangConvertCharset](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa741058(v=vs.85)) | Introduced in 10.0.10240. |
| [IMultiLanguage](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa741022(v=vs.85)) | Introduced in 10.0.10240. |
| [IMultiLanguage2](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa741001(v=vs.85)) | Introduced in 10.0.10240. |
| [IMultipleViewProvider](/windows/win32/api/uiautomationcore/nn-uiautomationcore-imultipleviewprovider) | Introduced in 10.0.10240. |
| [IMultiQI](/windows/win32/api/objidlbase/nn-objidlbase-imultiqi) | Introduced in 10.0.10240. |
| [INoMarshal](/windows/win32/api/objidlbase/nn-objidlbase-inomarshal) | Introduced in 10.0.10240. |
| [IObjectModelProvider](/windows/win32/api/uiautomationcore/nn-uiautomationcore-iobjectmodelprovider) | Introduced in 10.0.10240. |
| [IOpcCertificateEnumerator](/windows/win32/api/msopc/nn-msopc-iopccertificateenumerator) | Introduced in 10.0.10240. |
| [IOpcCertificateSet](/windows/win32/api/msopc/nn-msopc-iopccertificateset) | Introduced in 10.0.10240. |
| [IOpcDigitalSignature](/windows/win32/api/msopc/nn-msopc-iopcdigitalsignature) | Introduced in 10.0.10240. |
| [IOpcDigitalSignatureEnumerator](/windows/win32/api/msopc/nn-msopc-iopcdigitalsignatureenumerator) | Introduced in 10.0.10240. |
| [IOpcDigitalSignatureManager](/windows/win32/api/msopc/nn-msopc-iopcdigitalsignaturemanager) | Introduced in 10.0.10240. |
| [IOpcFactory](/windows/win32/api/msopc/nn-msopc-iopcfactory) | Introduced in 10.0.10240. |
| [IOpcPackage](/windows/win32/api/msopc/nn-msopc-iopcpackage) | Introduced in 10.0.10240. |
| [IOpcPart](/windows/win32/api/msopc/nn-msopc-iopcpart) | Introduced in 10.0.10240. |
| [IOpcPartEnumerator](/windows/win32/api/msopc/nn-msopc-iopcpartenumerator) | Introduced in 10.0.10240. |
| [IOpcPartSet](/windows/win32/api/msopc/nn-msopc-iopcpartset) | Introduced in 10.0.10240. |
| [IOpcPartUri](/windows/win32/api/msopc/nn-msopc-iopcparturi) | Introduced in 10.0.10240. |
| [IOpcRelationship](/windows/win32/api/msopc/nn-msopc-iopcrelationship) | Introduced in 10.0.10240. |
| [IOpcRelationshipEnumerator](/windows/win32/api/msopc/nn-msopc-iopcrelationshipenumerator) | Introduced in 10.0.10240. |
| [IOpcRelationshipSelector](/windows/win32/api/msopc/nn-msopc-iopcrelationshipselector) | Introduced in 10.0.10240. |
| [IOpcRelationshipSelectorEnumerator](/windows/win32/api/msopc/nn-msopc-iopcrelationshipselectorenumerator) | Introduced in 10.0.10240. |
| [IOpcRelationshipSelectorSet](/windows/win32/api/msopc/nn-msopc-iopcrelationshipselectorset) | Introduced in 10.0.10240. |
| [IOpcRelationshipSet](/windows/win32/api/msopc/nn-msopc-iopcrelationshipset) | Introduced in 10.0.10240. |
| [IOpcSignatureCustomObject](/windows/win32/api/msopc/nn-msopc-iopcsignaturecustomobject) | Introduced in 10.0.10240. |
| [IOpcSignatureCustomObjectEnumerator](/windows/win32/api/msopc/nn-msopc-iopcsignaturecustomobjectenumerator) | Introduced in 10.0.10240. |
| [IOpcSignatureCustomObjectSet](/windows/win32/api/msopc/nn-msopc-iopcsignaturecustomobjectset) | Introduced in 10.0.10240. |
| [IOpcSignaturePartReference](/windows/win32/api/msopc/nn-msopc-iopcsignaturepartreference) | Introduced in 10.0.10240. |
| [IOpcSignaturePartReferenceEnumerator](/windows/win32/api/msopc/nn-msopc-iopcsignaturepartreferenceenumerator) | Introduced in 10.0.10240. |
| [IOpcSignaturePartReferenceSet](/windows/win32/api/msopc/nn-msopc-iopcsignaturepartreferenceset) | Introduced in 10.0.10240. |
| [IOpcSignatureReference](/windows/win32/api/msopc/nn-msopc-iopcsignaturereference) | Introduced in 10.0.10240. |
| [IOpcSignatureReferenceEnumerator](/windows/win32/api/msopc/nn-msopc-iopcsignaturereferenceenumerator) | Introduced in 10.0.10240. |
| [IOpcSignatureReferenceSet](/windows/win32/api/msopc/nn-msopc-iopcsignaturereferenceset) | Introduced in 10.0.10240. |
| [IOpcSignatureRelationshipReference](/windows/win32/api/msopc/nn-msopc-iopcsignaturerelationshipreference) | Introduced in 10.0.10240. |
| [IOpcSignatureRelationshipReferenceEnumerator](/windows/win32/api/msopc/nn-msopc-iopcsignaturerelationshipreferenceenumerator) | Introduced in 10.0.10240. |
| [IOpcSignatureRelationshipReferenceSet](/windows/win32/api/msopc/nn-msopc-iopcsignaturerelationshipreferenceset) | Introduced in 10.0.10240. |
| [IOpcSigningOptions](/windows/win32/api/msopc/nn-msopc-iopcsigningoptions) | Introduced in 10.0.10240. |
| [IOpcUri](/windows/win32/api/msopc/nn-msopc-iopcuri) | Introduced in 10.0.10240. |
| [IOptionDescription](/windows/win32/api/spellcheck/nn-spellcheck-ioptiondescription) | Introduced in 10.0.10240. |
| [IPdfRendererNative](/windows/win32/api/windows.data.pdf.interop/nn-windows-data-pdf-interop-ipdfrenderernative) | Introduced in 10.0.10240. |
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
| [IPortableDevice](/windows/win32/api/portabledeviceapi/nn-portabledeviceapi-iportabledevice) | Introduced in 10.0.10240. |
| [IPortableDeviceCapabilities](/windows/win32/api/portabledeviceapi/nn-portabledeviceapi-iportabledevicecapabilities) | Introduced in 10.0.10240. |
| [IPortableDeviceContent](/windows/win32/api/portabledeviceapi/nn-portabledeviceapi-iportabledevicecontent) | Introduced in 10.0.10240. |
| [IPortableDeviceContent2](/windows/win32/api/portabledeviceapi/nn-portabledeviceapi-iportabledevicecontent2) | Introduced in 10.0.10240. |
| [IPortableDeviceDataStream](/windows/win32/api/portabledeviceapi/nn-portabledeviceapi-iportabledevicedatastream) | Introduced in 10.0.10240. |
| [IPortableDeviceDispatchFactory](/windows/win32/api/portabledeviceapi/nn-portabledeviceapi-iportabledevicedispatchfactory) | Introduced in 10.0.10240. |
| [IPortableDeviceEventCallback](/windows/win32/api/portabledeviceapi/nn-portabledeviceapi-iportabledeviceeventcallback) | Introduced in 10.0.10240. |
| [IPortableDeviceKeyCollection](/windows/win32/wpd_sdk/iportabledevicekeycollection) | Introduced in 10.0.10240. |
| [IPortableDeviceManager](/windows/win32/api/portabledeviceapi/nn-portabledeviceapi-iportabledevicemanager) | Introduced in 10.0.10240. |
| [IPortableDeviceProperties](/windows/win32/api/portabledeviceapi/nn-portabledeviceapi-iportabledeviceproperties) | Introduced in 10.0.10240. |
| [IPortableDevicePropertiesBulk](/windows/win32/api/portabledeviceapi/nn-portabledeviceapi-iportabledevicepropertiesbulk) | Introduced in 10.0.10240. |
| [IPortableDevicePropertiesBulkCallback](/windows/win32/api/portabledeviceapi/nn-portabledeviceapi-iportabledevicepropertiesbulkcallback) | Introduced in 10.0.10240. |
| [IPortableDevicePropVariantCollection](/windows/win32/wpd_sdk/iportabledevicepropvariantcollection) | Introduced in 10.0.10240. |
| [IPortableDeviceResources](/windows/win32/api/portabledeviceapi/nn-portabledeviceapi-iportabledeviceresources) | Introduced in 10.0.10240. |
| [IPortableDeviceService](/windows/win32/api/portabledeviceapi/nn-portabledeviceapi-iportabledeviceservice) | Introduced in 10.0.10240. |
| IPortableDeviceServiceActivation | Introduced in 10.0.10240. |
| [IPortableDeviceServiceCapabilities](/windows/win32/api/portabledeviceapi/nn-portabledeviceapi-iportabledeviceservicecapabilities) | Introduced in 10.0.10240. |
| [IPortableDeviceServiceManager](/windows/win32/api/portabledeviceapi/nn-portabledeviceapi-iportabledeviceservicemanager) | Introduced in 10.0.10240. |
| [IPortableDeviceServiceMethodCallback](/windows/win32/api/portabledeviceapi/nn-portabledeviceapi-iportabledeviceservicemethodcallback) | Introduced in 10.0.10240. |
| [IPortableDeviceServiceMethods](/windows/win32/api/portabledeviceapi/nn-portabledeviceapi-iportabledeviceservicemethods) | Introduced in 10.0.10240. |
| IPortableDeviceServiceOpenCallback | Introduced in 10.0.10240. |
| [IPortableDeviceUnitsStream](/windows/win32/api/portabledeviceapi/nn-portabledeviceapi-iportabledeviceunitsstream) | Introduced in 10.0.10240. |
| [IPortableDeviceValues](/windows/win32/wpd_sdk/iportabledevicevalues) | Introduced in 10.0.10240. |
| [IPortableDeviceValuesCollection](/windows/win32/wpd_sdk/iportabledevicevaluescollection) | Introduced in 10.0.10240. |
| [IPrintDocumentPackageTarget](/windows/win32/api/documenttarget/nn-documenttarget-iprintdocumentpackagetarget) | Introduced in 10.0.10240. |
| [IPrintDocumentPageSource](/previous-versions//jj710015(v=vs.85)) | Introduced in 10.0.10240. |
| [IPrinterBidiSetRequestCallback](/windows-hardware/drivers/ddi/printerextension/nn-printerextension-iprinterbidisetrequestcallback) | Introduced in 10.0.10240. |
| [IPrinterExtensionAsyncOperation](/windows-hardware/drivers/ddi/printerextension/nn-printerextension-iprinterextensionasyncoperation) | Introduced in 10.0.10240. |
| [IPrinterExtensionContext](/windows-hardware/drivers/ddi/printerextension/nn-printerextension-iprinterextensioncontext) | Introduced in 10.0.10240. |
| [IPrinterPropertyBag](/windows-hardware/drivers/ddi/printerextension/nn-printerextension-iprinterpropertybag) | Introduced in 10.0.10240. |
| [IPrinterQueue](/windows-hardware/drivers/ddi/printerextension/nn-printerextension-iprinterqueue) | Introduced in 10.0.10240. |
| [IPrinterQueue2](/windows-hardware/drivers/ddi/printerextension/nn-printerextension-iprinterqueue2) | Introduced in 10.0.10240. |
| [IPrinterQueueEvent](/windows-hardware/drivers/ddi/printerextension/nn-printerextension-iprinterqueueevent) | Introduced in 10.0.10240. |
| [IPrinterQueueView](/windows-hardware/drivers/ddi/printerextension/nn-printerextension-iprinterqueueview) | Introduced in 10.0.10240. |
| [IPrinterQueueViewEvent](/windows-hardware/drivers/ddi/printerextension/nn-printerextension-iprinterqueueviewevent) | Introduced in 10.0.10240. |
| [IPrintJob](/windows-hardware/drivers/ddi/printerextension/nn-printerextension-iprintjob) | Introduced in 10.0.10240. |
| [IPrintJobCollection](/windows-hardware/drivers/ddi/printerextension/nn-printerextension-iprintjobcollection) | Introduced in 10.0.10240. |
| [IPrintPreviewDxgiPackageTarget](/previous-versions//jj553554(v=vs.85)) | Introduced in 10.0.10240. |
| [IPrintPreviewPageCollection](/previous-versions//jj710018(v=vs.85)) | Introduced in 10.0.10240. |
| [IPrintSchemaAsyncOperation](/windows-hardware/drivers/ddi/printerextension/nn-printerextension-iprintschemaasyncoperation) | Introduced in 10.0.10240. |
| [IPrintSchemaAsyncOperationEvent](/windows-hardware/drivers/ddi/printerextension/nn-printerextension-iprintschemaasyncoperationevent) | Introduced in 10.0.10240. |
| [IPrintSchemaCapabilities](/windows-hardware/drivers/ddi/printerextension/nn-printerextension-iprintschemacapabilities) | Introduced in 10.0.10240. |
| [IPrintSchemaCapabilities2](/windows-hardware/drivers/ddi/printerextension/nn-printerextension-iprintschemacapabilities2) | Introduced in 10.0.10240. |
| [IPrintSchemaDisplayableElement](/windows-hardware/drivers/ddi/printerextension/nn-printerextension-iprintschemadisplayableelement) | Introduced in 10.0.10240. |
| [IPrintSchemaElement](/windows-hardware/drivers/ddi/printerextension/nn-printerextension-iprintschemaelement) | Introduced in 10.0.10240. |
| [IPrintSchemaFeature](/windows-hardware/drivers/ddi/printerextension/nn-printerextension-iprintschemafeature) | Introduced in 10.0.10240. |
| [IPrintSchemaNUpOption](/windows-hardware/drivers/ddi/printerextension/nn-printerextension-iprintschemanupoption) | Introduced in 10.0.10240. |
| [IPrintSchemaOption](/windows-hardware/drivers/ddi/printerextension/nn-printerextension-iprintschemaoption) | Introduced in 10.0.10240. |
| [IPrintSchemaOptionCollection](/windows-hardware/drivers/ddi/printerextension/nn-printerextension-iprintschemaoptioncollection) | Introduced in 10.0.10240. |
| [IPrintSchemaPageImageableSize](/windows-hardware/drivers/ddi/printerextension/nn-printerextension-iprintschemapageimageablesize) | Introduced in 10.0.10240. |
| [IPrintSchemaPageMediaSizeOption](/windows-hardware/drivers/ddi/printerextension/nn-printerextension-iprintschemapagemediasizeoption) | Introduced in 10.0.10240. |
| [IPrintSchemaParameterDefinition](/windows-hardware/drivers/ddi/printerextension/nn-printerextension-iprintschemaparameterdefinition) | Introduced in 10.0.10240. |
| [IPrintSchemaParameterInitializer](/windows-hardware/drivers/ddi/printerextension/nn-printerextension-iprintschemaparameterinitializer) | Introduced in 10.0.10240. |
| [IPrintSchemaTicket](/windows-hardware/drivers/ddi/printerextension/nn-printerextension-iprintschematicket) | Introduced in 10.0.10240. |
| [IPrintSchemaTicket2](/windows-hardware/drivers/ddi/printerextension/nn-printerextension-iprintschematicket2) | Introduced in 10.0.10240. |
| [IPropertyBag2](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa768192(v=vs.85)) | Introduced in 10.0.10240. |
| [IPropertySetStorage](/windows/win32/api/propidl/nn-propidl-ipropertysetstorage) | Introduced in 10.0.10240. |
| [IPropertyStorage](/windows/win32/api/propidlbase/nn-propidlbase-ipropertystorage) | Introduced in 10.0.10240. |
| [IPropertyStore](/windows/win32/api/propsys/nn-propsys-ipropertystore) | Introduced in 10.0.10240. |
| [IProxyProviderWinEventHandler](/windows/win32/api/uiautomationcore/nn-uiautomationcore-iproxyproviderwineventhandler) | Introduced in 10.0.10240. |
| [IProxyProviderWinEventSink](/windows/win32/api/uiautomationcore/nn-uiautomationcore-iproxyproviderwineventsink) | Introduced in 10.0.10240. |
| [IPSFactoryBuffer](/windows/win32/api/objidlbase/nn-objidlbase-ipsfactorybuffer) | Introduced in 10.0.10240. |
| [IQuickActivate](/windows/win32/api/ocidl/nn-ocidl-iquickactivate) | Introduced in 10.0.10240. |
| [IRangeValueProvider](/windows/win32/api/uiautomationcore/nn-uiautomationcore-irangevalueprovider) | Introduced in 10.0.10240. |
| [IRawElementProviderAdviseEvents](/windows/win32/api/uiautomationcore/nn-uiautomationcore-irawelementprovideradviseevents) | Introduced in 10.0.10240. |
| [IRawElementProviderFragment](/windows/win32/api/uiautomationcore/nn-uiautomationcore-irawelementproviderfragment) | Introduced in 10.0.10240. |
| [IRawElementProviderFragmentRoot](/windows/win32/api/uiautomationcore/nn-uiautomationcore-irawelementproviderfragmentroot) | Introduced in 10.0.10240. |
| [IRawElementProviderHostingAccessibles](/windows/win32/api/uiautomationcore/nn-uiautomationcore-irawelementproviderhostingaccessibles) | Introduced in 10.0.10240. |
| [IRawElementProviderHwndOverride](/windows/win32/api/uiautomationcore/nn-uiautomationcore-irawelementproviderhwndoverride) | Introduced in 10.0.10240. |
| [IRawElementProviderSimple](/windows/win32/api/uiautomationcore/nn-uiautomationcore-irawelementprovidersimple) | Introduced in 10.0.10240. |
| [IRawElementProviderSimple2](/windows/win32/api/uiautomationcore/nn-uiautomationcore-irawelementprovidersimple2) | Introduced in 10.0.10240. |
| [IRawElementProviderWindowlessSite](/windows/win32/api/uiautomationcore/nn-uiautomationcore-irawelementproviderwindowlesssite) | Introduced in 10.0.10240. |
| [IRDPSRAPIApplication](/windows/win32/api/rdpencomapi/nn-rdpencomapi-irdpsrapiapplication) | Introduced in 10.0.10240. |
| [IRDPSRAPIApplicationFilter](/windows/win32/api/rdpencomapi/nn-rdpencomapi-irdpsrapiapplicationfilter) | Introduced in 10.0.10240. |
| [IRDPSRAPIApplicationList](/windows/win32/api/rdpencomapi/nn-rdpencomapi-irdpsrapiapplicationlist) | Introduced in 10.0.10240. |
| [IRDPSRAPIAttendee](/windows/win32/api/rdpencomapi/nn-rdpencomapi-irdpsrapiattendee) | Introduced in 10.0.10240. |
| [IRDPSRAPIAttendeeDisconnectInfo](/windows/win32/api/rdpencomapi/nn-rdpencomapi-irdpsrapiattendeedisconnectinfo) | Introduced in 10.0.10240. |
| [IRDPSRAPIAttendeeManager](/windows/win32/api/rdpencomapi/nn-rdpencomapi-irdpsrapiattendeemanager) | Introduced in 10.0.10240. |
| [IRDPSRAPIAudioStream](/windows/win32/api/rdpencomapi/nn-rdpencomapi-irdpsrapiaudiostream) | Introduced in 10.0.10240. |
| IRDPSRAPIDebug | Introduced in 10.0.10240. |
| [IRDPSRAPIFrameBuffer](/windows/win32/api/rdpencomapi/nn-rdpencomapi-irdpsrapiframebuffer) | Introduced in 10.0.10240. |
| [IRDPSRAPIInvitation](/windows/win32/api/rdpencomapi/nn-rdpencomapi-irdpsrapiinvitation) | Introduced in 10.0.10240. |
| [IRDPSRAPIInvitationManager](/windows/win32/api/rdpencomapi/nn-rdpencomapi-irdpsrapiinvitationmanager) | Introduced in 10.0.10240. |
| [IRDPSRAPIPerfCounterLogger](/windows/win32/api/rdpencomapi/nn-rdpencomapi-irdpsrapiperfcounterlogger) | Introduced in 10.0.10240. |
| [IRDPSRAPIPerfCounterLoggingManager](/windows/win32/api/rdpencomapi/nn-rdpencomapi-irdpsrapiperfcounterloggingmanager) | Introduced in 10.0.10240. |
| [IRDPSRAPISessionProperties](/windows/win32/api/rdpencomapi/nn-rdpencomapi-irdpsrapisessionproperties) | Introduced in 10.0.10240. |
| [IRDPSRAPISharingSession](/windows/win32/api/rdpencomapi/nn-rdpencomapi-irdpsrapisharingsession) | Introduced in 10.0.10240. |
| [IRDPSRAPISharingSession2](/windows/win32/api/rdpencomapi/nn-rdpencomapi-irdpsrapisharingsession2) | Introduced in 10.0.10240. |
| [IRDPSRAPITcpConnectionInfo](/windows/win32/api/rdpencomapi/nn-rdpencomapi-irdpsrapitcpconnectioninfo) | Introduced in 10.0.10240. |
| [IRDPSRAPITransportStream](/windows/win32/api/rdpencomapi/nn-rdpencomapi-irdpsrapitransportstream) | Introduced in 10.0.10240. |
| [IRDPSRAPITransportStreamBuffer](/windows/win32/api/rdpencomapi/nn-rdpencomapi-irdpsrapitransportstreambuffer) | Introduced in 10.0.10240. |
| [IRDPSRAPITransportStreamEvents](/windows/win32/api/rdpencomapi/nn-rdpencomapi-irdpsrapitransportstreamevents) | Introduced in 10.0.10240. |
| [IRDPSRAPIViewer](/windows/win32/api/rdpencomapi/nn-rdpencomapi-irdpsrapiviewer) | Introduced in 10.0.10240. |
| [IRDPSRAPIVirtualChannel](/windows/win32/api/rdpencomapi/nn-rdpencomapi-irdpsrapivirtualchannel) | Introduced in 10.0.10240. |
| [IRDPSRAPIVirtualChannelManager](/windows/win32/api/rdpencomapi/nn-rdpencomapi-irdpsrapivirtualchannelmanager) | Introduced in 10.0.10240. |
| [IRDPSRAPIWindow](/windows/win32/api/rdpencomapi/nn-rdpencomapi-irdpsrapiwindow) | Introduced in 10.0.10240. |
| [IRDPSRAPIWindowList](/windows/win32/api/rdpencomapi/nn-rdpencomapi-irdpsrapiwindowlist) | Introduced in 10.0.10240. |
| [IRDPViewerInputSink](/windows/win32/api/rdpencomapi/nn-rdpencomapi-irdpviewerinputsink) | Introduced in 10.0.10240. |
| [IRDPViewerRenderingSurface](/windows/win32/api/rdpencomapi/nn-rdpencomapi-irdpviewerrenderingsurface) | Introduced in 10.0.10240. |
| [IReferenceTracker](/windows/win32/api/windows.ui.xaml.hosting.referencetracker/nn-windows-ui-xaml-hosting-referencetracker-ireferencetracker) | Introduced in 10.0.10240. |
| [IReferenceTrackerHost](/windows/win32/api/windows.ui.xaml.hosting.referencetracker/nn-windows-ui-xaml-hosting-referencetracker-ireferencetrackerhost) | Introduced in 10.0.10240. |
| [IReferenceTrackerManager](/windows/win32/api/windows.ui.xaml.hosting.referencetracker/nn-windows-ui-xaml-hosting-referencetracker-ireferencetrackermanager) | Introduced in 10.0.10240. |
| [IReferenceTrackerTarget](/windows/win32/api/windows.ui.xaml.hosting.referencetracker/nn-windows-ui-xaml-hosting-referencetracker-ireferencetrackertarget) | Introduced in 10.0.10240. |
| [IRemoteDesktopClient](/previous-versions//hh448564(v=vs.85)) | Introduced in 10.0.10240. |
| [IRemoteDesktopClientActions](/previous-versions//hh448581(v=vs.85)) | Introduced in 10.0.10240. |
| [IRemoteDesktopClientEvents](/previous-versions//hh448568(v=vs.85)) | Introduced in 10.0.10240. |
| [IRemoteDesktopClientSettings](/previous-versions//hh448590(v=vs.85)) | Introduced in 10.0.10240. |
| [IRestrictedErrorInfo](/windows/win32/api/restrictederrorinfo/nn-restrictederrorinfo-irestrictederrorinfo) | Introduced in 10.0.10240. |
| [IRootStorage](/windows/win32/api/objidl/nn-objidl-irootstorage) | Introduced in 10.0.10240. |
| [IRpcChannelBuffer](/windows/win32/api/objidlbase/nn-objidlbase-irpcchannelbuffer) | Introduced in 10.0.10240. |
| [IRpcStubBuffer](/windows/win32/api/objidlbase/nn-objidlbase-irpcstubbuffer) | Introduced in 10.0.10240. |
| [IScrollItemProvider](/windows/win32/api/uiautomationcore/nn-uiautomationcore-iscrollitemprovider) | Introduced in 10.0.10240. |
| [IScrollProvider](/windows/win32/api/uiautomationcore/nn-uiautomationcore-iscrollprovider) | Introduced in 10.0.10240. |
| [ISelectionItemProvider](/windows/win32/api/uiautomationcore/nn-uiautomationcore-iselectionitemprovider) | Introduced in 10.0.10240. |
| [ISelectionProvider](/windows/win32/api/uiautomationcore/nn-uiautomationcore-iselectionprovider) | Introduced in 10.0.10240. |
| [ISequentialStream](/windows/win32/api/objidl/nn-objidl-isequentialstream) | Introduced in 10.0.10240. |
| ISignalableNotifier | Introduced in 10.0.10240. |
| [ISimpleAudioVolume](/windows/win32/api/audioclient/nn-audioclient-isimpleaudiovolume) | Introduced in 10.0.10240. |
| [ISoftwareBitmapNative](/windows/win32/api/windows.graphics.imaging.interop/nn-windows-graphics-imaging-interop-isoftwarebitmapnative) | Introduced in 10.0.10240. |
| [ISoftwareBitmapNativeFactory](/windows/win32/api/windows.graphics.imaging.interop/nn-windows-graphics-imaging-interop-isoftwarebitmapnativefactory) | Introduced in 10.0.10240. |
| [ISpellChecker](/windows/win32/api/spellcheck/nn-spellcheck-ispellchecker) | Introduced in 10.0.10240. |
| [ISpellChecker2](/windows/win32/api/spellcheck/nn-spellcheck-ispellchecker2) | Introduced in 10.0.10240. |
| [ISpellCheckerChangedEventHandler](/windows/win32/api/spellcheck/nn-spellcheck-ispellcheckerchangedeventhandler) | Introduced in 10.0.10240. |
| [ISpellCheckerFactory](/windows/win32/api/spellcheck/nn-spellcheck-ispellcheckerfactory) | Introduced in 10.0.10240. |
| [ISpellingError](/windows/win32/api/spellcheck/nn-spellcheck-ispellingerror) | Introduced in 10.0.10240. |
| [ISpreadsheetItemProvider](/windows/win32/api/uiautomationcore/nn-uiautomationcore-ispreadsheetitemprovider) | Introduced in 10.0.10240. |
| [ISpreadsheetProvider](/windows/win32/api/uiautomationcore/nn-uiautomationcore-ispreadsheetprovider) | Introduced in 10.0.10240. |
| [IStorage](/windows/win32/api/objidl/nn-objidl-istorage) | Introduced in 10.0.10240. |
| [IStream](/windows/win32/api/objidl/nn-objidl-istream) | Introduced in 10.0.10240. |
| [IStylesProvider](/windows/win32/api/uiautomationcore/nn-uiautomationcore-istylesprovider) | Introduced in 10.0.10240. |
| [ISurfaceImageSourceManagerNative](/windows/win32/api/windows.ui.xaml.media.dxinterop/nn-windows-ui-xaml-media-dxinterop-isurfaceimagesourcemanagernative) | Introduced in 10.0.10240. |
| [ISurfaceImageSourceNative](/windows/win32/api/windows.ui.xaml.media.dxinterop/nn-windows-ui-xaml-media-dxinterop-isurfaceimagesourcenative) | Introduced in 10.0.10240. |
| [ISurfaceImageSourceNativeWithD2D](/windows/win32/api/windows.ui.xaml.media.dxinterop/nn-windows-ui-xaml-media-dxinterop-isurfaceimagesourcenativewithd2d) | Introduced in 10.0.10240. |
| [ISurrogate](/windows/win32/api/objidlbase/nn-objidlbase-isurrogate) | Introduced in 10.0.10240. |
| [ISwapChainBackgroundPanelNative](/windows/win32/api/windows.ui.xaml.media.dxinterop/nn-windows-ui-xaml-media-dxinterop-iswapchainbackgroundpanelnative) | Introduced in 10.0.10240. |
| [ISwapChainPanelNative](/windows/win32/api/windows.ui.xaml.media.dxinterop/nn-windows-ui-xaml-media-dxinterop-iswapchainpanelnative) | Introduced in 10.0.10240. |
| [ISwapChainPanelNative2](/windows/win32/api/windows.ui.xaml.media.dxinterop/nn-windows-ui-xaml-media-dxinterop-iswapchainpanelnative2) | Introduced in 10.0.10240. |
| [ISynchronizedInputProvider](/windows/win32/api/uiautomationcore/nn-uiautomationcore-isynchronizedinputprovider) | Introduced in 10.0.10240. |
| [ITableItemProvider](/windows/win32/api/uiautomationcore/nn-uiautomationcore-itableitemprovider) | Introduced in 10.0.10240. |
| [ITableProvider](/windows/win32/api/uiautomationcore/nn-uiautomationcore-itableprovider) | Introduced in 10.0.10240. |
| [ITextChildProvider](/windows/win32/api/uiautomationcore/nn-uiautomationcore-itextchildprovider) | Introduced in 10.0.10240. |
| [ITextEditProvider](/windows/win32/api/uiautomationcore/nn-uiautomationcore-itexteditprovider) | Introduced in 10.0.10240. |
| [ITextProvider](/windows/win32/api/uiautomationcore/nn-uiautomationcore-itextprovider) | Introduced in 10.0.10240. |
| [ITextProvider2](/windows/win32/api/uiautomationcore/nn-uiautomationcore-itextprovider2) | Introduced in 10.0.10240. |
| [ITextRangeProvider](/windows/win32/api/uiautomationcore/nn-uiautomationcore-itextrangeprovider) | Introduced in 10.0.10240. |
| [ITextRangeProvider2](/windows/win32/api/uiautomationcore/nn-uiautomationcore-itextrangeprovider2) | Introduced in 10.0.10240. |
| [ITextStoreACP2](/windows/win32/api/textstor/nn-textstor-itextstoreacp2) | Introduced in 10.0.10240. |
| [ITextStoreACPServices](/windows/win32/api/msctf/nn-msctf-itextstoreacpservices) | Introduced in 10.0.10240. |
| [ITextStoreACPSink](/windows/win32/api/textstor/nn-textstor-itextstoreacpsink) | Introduced in 10.0.10240. |
| [ITextStoreAnchor](/windows/win32/api/textstor/nn-textstor-itextstoreanchor) | Introduced in 10.0.10240. |
| [ITextStoreAnchorSink](/windows/win32/api/textstor/nn-textstor-itextstoreanchorsink) | Introduced in 10.0.10240. |
| [ITfCandidateList](/windows/win32/api/ctffunc/nn-ctffunc-itfcandidatelist) | Introduced in 10.0.10240. |
| [ITfCandidateListUIElement](/windows/win32/api/msctf/nn-msctf-itfcandidatelistuielement) | Introduced in 10.0.10240. |
| [ITfCandidateListUIElementBehavior](/windows/win32/api/msctf/nn-msctf-itfcandidatelistuielementbehavior) | Introduced in 10.0.10240. |
| [ITfCandidateString](/windows/win32/api/ctffunc/nn-ctffunc-itfcandidatestring) | Introduced in 10.0.10240. |
| [ITfCategoryMgr](/windows/win32/api/msctf/nn-msctf-itfcategorymgr) | Introduced in 10.0.10240. |
| [ITfCompartment](/windows/win32/api/msctf/nn-msctf-itfcompartment) | Introduced in 10.0.10240. |
| [ITfCompartmentEventSink](/windows/win32/api/msctf/nn-msctf-itfcompartmenteventsink) | Introduced in 10.0.10240. |
| [ITfCompartmentMgr](/windows/win32/api/msctf/nn-msctf-itfcompartmentmgr) | Introduced in 10.0.10240. |
| [ITfComposition](/windows/win32/api/msctf/nn-msctf-itfcomposition) | Introduced in 10.0.10240. |
| [ITfCompositionSink](/windows/win32/api/msctf/nn-msctf-itfcompositionsink) | Introduced in 10.0.10240. |
| [ITfCompositionView](/windows/win32/api/msctf/nn-msctf-itfcompositionview) | Introduced in 10.0.10240. |
| [ITfConfigureSystemKeystrokeFeed](/windows/win32/api/msctf/nn-msctf-itfconfiguresystemkeystrokefeed) | Introduced in 10.0.10240. |
| [ITfContext](/windows/win32/api/msctf/nn-msctf-itfcontext) | Introduced in 10.0.10240. |
| [ITfContextComposition](/windows/win32/api/msctf/nn-msctf-itfcontextcomposition) | Introduced in 10.0.10240. |
| [ITfContextOwnerCompositionServices](/windows/win32/api/msctf/nn-msctf-itfcontextownercompositionservices) | Introduced in 10.0.10240. |
| [ITfContextOwnerCompositionSink](/windows/win32/api/msctf/nn-msctf-itfcontextownercompositionsink) | Introduced in 10.0.10240. |
| [ITfContextOwnerServices](/windows/win32/api/msctf/nn-msctf-itfcontextownerservices) | Introduced in 10.0.10240. |
| [ITfContextView](/windows/win32/api/msctf/nn-msctf-itfcontextview) | Introduced in 10.0.10240. |
| [ITfDisplayAttributeInfo](/windows/win32/api/msctf/nn-msctf-itfdisplayattributeinfo) | Introduced in 10.0.10240. |
| [ITfDisplayAttributeMgr](/windows/win32/api/msctf/nn-msctf-itfdisplayattributemgr) | Introduced in 10.0.10240. |
| [ITfDisplayAttributeNotifySink](/windows/win32/api/msctf/nn-msctf-itfdisplayattributenotifysink) | Introduced in 10.0.10240. |
| [ITfDisplayAttributeProvider](/windows/win32/api/msctf/nn-msctf-itfdisplayattributeprovider) | Introduced in 10.0.10240. |
| [ITfDocumentMgr](/windows/win32/api/msctf/nn-msctf-itfdocumentmgr) | Introduced in 10.0.10240. |
| [ITfEditRecord](/windows/win32/api/msctf/nn-msctf-itfeditrecord) | Introduced in 10.0.10240. |
| [ITfEditSession](/windows/win32/api/msctf/nn-msctf-itfeditsession) | Introduced in 10.0.10240. |
| [ITfFnGetSAPIObject](/windows/win32/api/ctffunc/nn-ctffunc-itffngetsapiobject) | Introduced in 10.0.10240. |
| [ITfFnReconversion](/windows/win32/api/ctffunc/nn-ctffunc-itffnreconversion) | Introduced in 10.0.10240. |
| [ITfFunction](/windows/win32/api/msctf/nn-msctf-itffunction) | Introduced in 10.0.10240. |
| [ITfFunctionProvider](/windows/win32/api/msctf/nn-msctf-itffunctionprovider) | Introduced in 10.0.10240. |
| [ITfInputProcessorProfileActivationSink](/windows/win32/api/msctf/nn-msctf-itfinputprocessorprofileactivationsink) | Introduced in 10.0.10240. |
| [ITfInputProcessorProfileMgr](/windows/win32/api/msctf/nn-msctf-itfinputprocessorprofilemgr) | Introduced in 10.0.10240. |
| [ITfInputScope](/windows/win32/api/inputscope/nn-inputscope-itfinputscope) | Introduced in 10.0.10240. |
| [ITfInputScope2](/windows/win32/api/inputscope/nn-inputscope-itfinputscope2) | Introduced in 10.0.10240. |
| [ITfKeyEventSink](/windows/win32/api/msctf/nn-msctf-itfkeyeventsink) | Introduced in 10.0.10240. |
| [ITfKeystrokeMgr](/windows/win32/api/msctf/nn-msctf-itfkeystrokemgr) | Introduced in 10.0.10240. |
| [ITfKeyTraceEventSink](/windows/win32/api/msctf/nn-msctf-itfkeytraceeventsink) | Introduced in 10.0.10240. |
| [ITfLanguageProfileNotifySink](/windows/win32/api/msctf/nn-msctf-itflanguageprofilenotifysink) | Introduced in 10.0.10240. |
| [ITfPersistentPropertyLoaderACP](/windows/win32/api/msctf/nn-msctf-itfpersistentpropertyloaderacp) | Introduced in 10.0.10240. |
| [ITfPreservedKeyNotifySink](/windows/win32/api/msctf/nn-msctf-itfpreservedkeynotifysink) | Introduced in 10.0.10240. |
| [ITfProperty](/windows/win32/api/msctf/nn-msctf-itfproperty) | Introduced in 10.0.10240. |
| [ITfPropertyStore](/windows/win32/api/msctf/nn-msctf-itfpropertystore) | Introduced in 10.0.10240. |
| [ITfRange](/windows/win32/api/msctf/nn-msctf-itfrange) | Introduced in 10.0.10240. |
| [ITfRangeACP](/windows/win32/api/msctf/nn-msctf-itfrangeacp) | Introduced in 10.0.10240. |
| [ITfRangeBackup](/windows/win32/api/msctf/nn-msctf-itfrangebackup) | Introduced in 10.0.10240. |
| [ITfReadingInformationUIElement](/windows/win32/api/msctf/nn-msctf-itfreadinginformationuielement) | Introduced in 10.0.10240. |
| [ITfReadOnlyProperty](/windows/win32/api/msctf/nn-msctf-itfreadonlyproperty) | Introduced in 10.0.10240. |
| [ITfSource](/windows/win32/api/msctf/nn-msctf-itfsource) | Introduced in 10.0.10240. |
| [ITfSourceSingle](/windows/win32/api/msctf/nn-msctf-itfsourcesingle) | Introduced in 10.0.10240. |
| [ITfTextEditSink](/windows/win32/api/msctf/nn-msctf-itftexteditsink) | Introduced in 10.0.10240. |
| [ITfThreadMgr2](/windows/win32/api/msctf/nn-msctf-itfthreadmgr2) | Introduced in 10.0.10240. |
| [ITfUIElement](/windows/win32/api/msctf/nn-msctf-itfuielement) | Introduced in 10.0.10240. |
| [ITfUIElementMgr](/windows/win32/api/msctf/nn-msctf-itfuielementmgr) | Introduced in 10.0.10240. |
| [ITfUIElementSink](/windows/win32/api/msctf/nn-msctf-itfuielementsink) | Introduced in 10.0.10240. |
| [IThumbnailStreamCache](/windows/win32/api/thumbnailstreamcache/nn-thumbnailstreamcache-ithumbnailstreamcache) | Introduced in 10.0.10240. |
| [IToggleProvider](/windows/win32/api/uiautomationcore/nn-uiautomationcore-itoggleprovider) | Introduced in 10.0.10240. |
| [ITransformProvider](/windows/win32/api/uiautomationcore/nn-uiautomationcore-itransformprovider) | Introduced in 10.0.10240. |
| [ITransformProvider2](/windows/win32/api/uiautomationcore/nn-uiautomationcore-itransformprovider2) | Introduced in 10.0.10240. |
| [IUIAnimationInterpolator](/windows/win32/api/uianimation/nn-uianimation-iuianimationinterpolator) | Introduced in 10.0.10240. |
| [IUIAnimationInterpolator2](/windows/win32/api/uianimation/nn-uianimation-iuianimationinterpolator2) | Introduced in 10.0.10240. |
| [IUIAnimationLoopIterationChangeHandler2](/windows/win32/api/uianimation/nn-uianimation-iuianimationloopiterationchangehandler2) | Introduced in 10.0.10240. |
| [IUIAnimationManager](/windows/win32/api/uianimation/nn-uianimation-iuianimationmanager) | Introduced in 10.0.10240. |
| [IUIAnimationManager2](/windows/win32/api/uianimation/nn-uianimation-iuianimationmanager2) | Introduced in 10.0.10240. |
| [IUIAnimationManagerEventHandler](/windows/win32/api/uianimation/nn-uianimation-iuianimationmanagereventhandler) | Introduced in 10.0.10240. |
| [IUIAnimationManagerEventHandler2](/windows/win32/api/uianimation/nn-uianimation-iuianimationmanagereventhandler2) | Introduced in 10.0.10240. |
| [IUIAnimationPrimitiveInterpolation](/windows/win32/api/uianimation/nn-uianimation-iuianimationprimitiveinterpolation) | Introduced in 10.0.10240. |
| [IUIAnimationPriorityComparison](/windows/win32/api/uianimation/nn-uianimation-iuianimationprioritycomparison) | Introduced in 10.0.10240. |
| [IUIAnimationPriorityComparison2](/windows/win32/api/uianimation/nn-uianimation-iuianimationprioritycomparison2) | Introduced in 10.0.10240. |
| [IUIAnimationStoryboard](/windows/win32/api/uianimation/nn-uianimation-iuianimationstoryboard) | Introduced in 10.0.10240. |
| [IUIAnimationStoryboard2](/windows/win32/api/uianimation/nn-uianimation-iuianimationstoryboard2) | Introduced in 10.0.10240. |
| [IUIAnimationStoryboardEventHandler](/windows/win32/api/uianimation/nn-uianimation-iuianimationstoryboardeventhandler) | Introduced in 10.0.10240. |
| [IUIAnimationStoryboardEventHandler2](/windows/win32/api/uianimation/nn-uianimation-iuianimationstoryboardeventhandler2) | Introduced in 10.0.10240. |
| [IUIAnimationTimer](/windows/win32/api/uianimation/nn-uianimation-iuianimationtimer) | Introduced in 10.0.10240. |
| [IUIAnimationTimerClientEventHandler](/windows/win32/api/uianimation/nn-uianimation-iuianimationtimerclienteventhandler) | Introduced in 10.0.10240. |
| [IUIAnimationTimerEventHandler](/windows/win32/api/uianimation/nn-uianimation-iuianimationtimereventhandler) | Introduced in 10.0.10240. |
| [IUIAnimationTimerUpdateHandler](/windows/win32/api/uianimation/nn-uianimation-iuianimationtimerupdatehandler) | Introduced in 10.0.10240. |
| [IUIAnimationTransition](/windows/win32/api/uianimation/nn-uianimation-iuianimationtransition) | Introduced in 10.0.10240. |
| [IUIAnimationTransition2](/windows/win32/api/uianimation/nn-uianimation-iuianimationtransition2) | Introduced in 10.0.10240. |
| [IUIAnimationTransitionFactory](/windows/win32/api/uianimation/nn-uianimation-iuianimationtransitionfactory) | Introduced in 10.0.10240. |
| [IUIAnimationTransitionFactory2](/windows/win32/api/uianimation/nn-uianimation-iuianimationtransitionfactory2) | Introduced in 10.0.10240. |
| [IUIAnimationTransitionLibrary](/windows/win32/api/uianimation/nn-uianimation-iuianimationtransitionlibrary) | Introduced in 10.0.10240. |
| [IUIAnimationTransitionLibrary2](/windows/win32/api/uianimation/nn-uianimation-iuianimationtransitionlibrary2) | Introduced in 10.0.10240. |
| [IUIAnimationVariable](/windows/win32/api/uianimation/nn-uianimation-iuianimationvariable) | Introduced in 10.0.10240. |
| [IUIAnimationVariable2](/windows/win32/api/uianimation/nn-uianimation-iuianimationvariable2) | Introduced in 10.0.10240. |
| [IUIAnimationVariableChangeHandler](/windows/win32/api/uianimation/nn-uianimation-iuianimationvariablechangehandler) | Introduced in 10.0.10240. |
| [IUIAnimationVariableChangeHandler2](/windows/win32/api/uianimation/nn-uianimation-iuianimationvariablechangehandler2) | Introduced in 10.0.10240. |
| [IUIAnimationVariableCurveChangeHandler2](/windows/win32/api/uianimation/nn-uianimation-iuianimationvariablecurvechangehandler2) | Introduced in 10.0.10240. |
| [IUIAnimationVariableIntegerChangeHandler](/windows/win32/api/uianimation/nn-uianimation-iuianimationvariableintegerchangehandler) | Introduced in 10.0.10240. |
| [IUIAnimationVariableIntegerChangeHandler2](/windows/win32/api/uianimation/nn-uianimation-iuianimationvariableintegerchangehandler2) | Introduced in 10.0.10240. |
| [IUIAutomationPatternHandler](/windows/win32/api/uiautomationcore/nn-uiautomationcore-iuiautomationpatternhandler) | Introduced in 10.0.10240. |
| [IUIAutomationPatternInstance](/windows/win32/api/uiautomationcore/nn-uiautomationcore-iuiautomationpatterninstance) | Introduced in 10.0.10240. |
| [IUIAutomationRegistrar](/windows/win32/api/uiautomationcore/nn-uiautomationcore-iuiautomationregistrar) | Introduced in 10.0.10240. |
| [IUnknown](/windows/win32/api/unknwn/nn-unknwn-iunknown) | Introduced in 10.0.10240. |
| [IValueProvider](/windows/win32/api/uiautomationcore/nn-uiautomationcore-ivalueprovider) | Introduced in 10.0.10240. |
| [IVideoFrameNative](/windows/win32/api/windows.media.core.interop/nn-windows-media-core-interop-ivideoframenative) | Introduced in 10.0.10240. |
| [IVideoFrameNativeFactory](/windows/win32/api/windows.media.core.interop/nn-windows-media-core-interop-ivideoframenativefactory) | Introduced in 10.0.10240. |
| [IVirtualizedItemProvider](/windows/win32/api/uiautomationcore/nn-uiautomationcore-ivirtualizeditemprovider) | Introduced in 10.0.10240. |
| [IVirtualSurfaceImageSourceNative](/windows/win32/api/windows.ui.xaml.media.dxinterop/nn-windows-ui-xaml-media-dxinterop-ivirtualsurfaceimagesourcenative) | Introduced in 10.0.10240. |
| [IVirtualSurfaceUpdatesCallbackNative](/windows/win32/api/windows.ui.xaml.media.dxinterop/nn-windows-ui-xaml-media-dxinterop-ivirtualsurfaceupdatescallbacknative) | Introduced in 10.0.10240. |
| [IWeakReference](/windows/win32/api/weakreference/nn-weakreference-iweakreference) | Introduced in 10.0.10240. |
| [IWeakReferenceSource](/windows/win32/api/weakreference/nn-weakreference-iweakreferencesource) | Introduced in 10.0.10240. |
| [IWICBitmap](/windows/win32/api/wincodec/nn-wincodec-iwicbitmap) | Introduced in 10.0.10240. |
| [IWICBitmapClipper](/windows/win32/api/wincodec/nn-wincodec-iwicbitmapclipper) | Introduced in 10.0.10240. |
| [IWICBitmapCodecInfo](/windows/win32/api/wincodec/nn-wincodec-iwicbitmapcodecinfo) | Introduced in 10.0.10240. |
| [IWICBitmapCodecProgressNotification](/windows/win32/api/wincodec/nn-wincodec-iwicbitmapcodecprogressnotification) | Introduced in 10.0.10240. |
| [IWICBitmapDecoder](/windows/win32/api/wincodec/nn-wincodec-iwicbitmapdecoder) | Introduced in 10.0.10240. |
| [IWICBitmapDecoderInfo](/windows/win32/api/wincodec/nn-wincodec-iwicbitmapdecoderinfo) | Introduced in 10.0.10240. |
| [IWICBitmapEncoder](/windows/win32/api/wincodec/nn-wincodec-iwicbitmapencoder) | Introduced in 10.0.10240. |
| [IWICBitmapEncoderInfo](/windows/win32/api/wincodec/nn-wincodec-iwicbitmapencoderinfo) | Introduced in 10.0.10240. |
| [IWICBitmapFlipRotator](/windows/win32/api/wincodec/nn-wincodec-iwicbitmapfliprotator) | Introduced in 10.0.10240. |
| [IWICBitmapFrameDecode](/windows/win32/api/wincodec/nn-wincodec-iwicbitmapframedecode) | Introduced in 10.0.10240. |
| [IWICBitmapFrameEncode](/windows/win32/api/wincodec/nn-wincodec-iwicbitmapframeencode) | Introduced in 10.0.10240. |
| [IWICBitmapLock](/windows/win32/api/wincodec/nn-wincodec-iwicbitmaplock) | Introduced in 10.0.10240. |
| [IWICBitmapScaler](/windows/win32/api/wincodec/nn-wincodec-iwicbitmapscaler) | Introduced in 10.0.10240. |
| [IWICBitmapSource](/windows/win32/api/wincodec/nn-wincodec-iwicbitmapsource) | Introduced in 10.0.10240. |
| [IWICBitmapSourceTransform](/windows/win32/api/wincodec/nn-wincodec-iwicbitmapsourcetransform) | Introduced in 10.0.10240. |
| [IWICColorContext](/windows/win32/api/wincodec/nn-wincodec-iwiccolorcontext) | Introduced in 10.0.10240. |
| [IWICColorTransform](/windows/win32/api/wincodec/nn-wincodec-iwiccolortransform) | Introduced in 10.0.10240. |
| [IWICComponentFactory](/windows/win32/api/wincodecsdk/nn-wincodecsdk-iwiccomponentfactory) | Introduced in 10.0.10240. |
| [IWICComponentInfo](/windows/win32/api/wincodec/nn-wincodec-iwiccomponentinfo) | Introduced in 10.0.10240. |
| [IWICDevelopRaw](/windows/win32/api/wincodec/nn-wincodec-iwicdevelopraw) | Introduced in 10.0.10240. |
| [IWICDevelopRawNotificationCallback](/windows/win32/api/wincodec/nn-wincodec-iwicdeveloprawnotificationcallback) | Introduced in 10.0.10240. |
| [IWICEnumMetadataItem](/windows/win32/api/wincodec/nn-wincodec-iwicenummetadataitem) | Introduced in 10.0.10240. |
| [IWICFastMetadataEncoder](/windows/win32/api/wincodec/nn-wincodec-iwicfastmetadataencoder) | Introduced in 10.0.10240. |
| [IWICFormatConverter](/windows/win32/api/wincodec/nn-wincodec-iwicformatconverter) | Introduced in 10.0.10240. |
| [IWICFormatConverterInfo](/windows/win32/api/wincodec/nn-wincodec-iwicformatconverterinfo) | Introduced in 10.0.10240. |
| [IWICImageEncoder](/windows/win32/api/wincodec/nn-wincodec-iwicimageencoder) | Introduced in 10.0.10240. |
| [IWICImagingFactory](/windows/win32/api/wincodec/nn-wincodec-iwicimagingfactory) | Introduced in 10.0.10240. |
| [IWICImagingFactory2](/windows/win32/api/wincodec/nn-wincodec-iwicimagingfactory2) | Introduced in 10.0.10240. |
| [IWICMetadataBlockReader](/windows/win32/api/wincodecsdk/nn-wincodecsdk-iwicmetadatablockreader) | Introduced in 10.0.10240. |
| [IWICMetadataBlockWriter](/windows/win32/api/wincodecsdk/nn-wincodecsdk-iwicmetadatablockwriter) | Introduced in 10.0.10240. |
| [IWICMetadataHandlerInfo](/windows/win32/api/wincodecsdk/nn-wincodecsdk-iwicmetadatahandlerinfo) | Introduced in 10.0.10240. |
| [IWICMetadataQueryReader](/windows/win32/api/wincodec/nn-wincodec-iwicmetadataqueryreader) | Introduced in 10.0.10240. |
| [IWICMetadataQueryWriter](/windows/win32/api/wincodec/nn-wincodec-iwicmetadataquerywriter) | Introduced in 10.0.10240. |
| [IWICMetadataReader](/windows/win32/api/wincodecsdk/nn-wincodecsdk-iwicmetadatareader) | Introduced in 10.0.10240. |
| [IWICMetadataReaderInfo](/windows/win32/api/wincodecsdk/nn-wincodecsdk-iwicmetadatareaderinfo) | Introduced in 10.0.10240. |
| [IWICMetadataWriter](/windows/win32/api/wincodecsdk/nn-wincodecsdk-iwicmetadatawriter) | Introduced in 10.0.10240. |
| [IWICMetadataWriterInfo](/windows/win32/api/wincodecsdk/nn-wincodecsdk-iwicmetadatawriterinfo) | Introduced in 10.0.10240. |
| [IWICPalette](/windows/win32/api/wincodec/nn-wincodec-iwicpalette) | Introduced in 10.0.10240. |
| [IWICPersistStream](/windows/win32/api/wincodecsdk/nn-wincodecsdk-iwicpersiststream) | Introduced in 10.0.10240. |
| [IWICPixelFormatInfo](/windows/win32/api/wincodec/nn-wincodec-iwicpixelformatinfo) | Introduced in 10.0.10240. |
| [IWICPixelFormatInfo2](/windows/win32/api/wincodec/nn-wincodec-iwicpixelformatinfo2) | Introduced in 10.0.10240. |
| [IWICProgressCallback](/windows/win32/api/wincodec/nn-wincodec-iwicprogresscallback) | Introduced in 10.0.10240. |
| [IWICProgressiveLevelControl](/windows/win32/api/wincodec/nn-wincodec-iwicprogressivelevelcontrol) | Introduced in 10.0.10240. |
| [IWICStream](/windows/win32/api/wincodec/nn-wincodec-iwicstream) | Introduced in 10.0.10240. |
| [IWICStreamProvider](/windows/win32/api/wincodecsdk/nn-wincodecsdk-iwicstreamprovider) | Introduced in 10.0.10240. |
| [IWICDdsDecoder](/windows/win32/api/wincodec/nn-wincodec-iwicddsdecoder) | Introduced in 10.0.10240. |
| [IWICDdsEncoder](/windows/win32/api/wincodec/nn-wincodec-iwicddsencoder) | Introduced in 10.0.10240. |
| [IWICDdsFrameDecode](/windows/win32/api/wincodec/nn-wincodec-iwicddsframedecode) | Introduced in 10.0.10240. |
| [IWICPlanarBitmapFrameEncode](/windows/win32/api/wincodec/nn-wincodec-iwicplanarbitmapframeencode) | Introduced in 10.0.10240. |
| [IWICPlanarBitmapSourceTransform](/windows/win32/api/wincodec/nn-wincodec-iwicplanarbitmapsourcetransform) | Introduced in 10.0.10240. |
| [IWICPlanarFormatConverter](/windows/win32/api/wincodec/nn-wincodec-iwicplanarformatconverter) | Introduced in 10.0.10240. |
| [IWICJpegFrameDecode](/windows/win32/api/wincodec/nn-wincodec-iwicjpegframedecode) | Introduced in 10.0.10240. |
| [IWICJpegFrameEncode](/windows/win32/api/wincodec/nn-wincodec-iwicjpegframeencode) | Introduced in 10.0.10240. |
| [IWindowProvider](/windows/win32/api/uiautomationcore/nn-uiautomationcore-iwindowprovider) | Introduced in 10.0.10240. |
| [IWindowsDevicesAllJoynBusAttachmentFactoryInterop](/windows/win32/api/windows.devices.alljoyn.interop/nn-windows-devices-alljoyn-interop-iwindowsdevicesalljoynbusattachmentfactoryinterop) | Introduced in 10.0.10240. |
| [IWindowsDevicesAllJoynBusAttachmentInterop](/windows/win32/api/windows.devices.alljoyn.interop/nn-windows-devices-alljoyn-interop-iwindowsdevicesalljoynbusattachmentinterop) | Introduced in 10.0.10240. |
| IWorkspaceBrokerAx | Introduced in 10.0.10240. |
| IWorkspaceBrokerAx2 | Introduced in 10.0.10240. |
| [IXAPO](/windows/win32/api/xapo/nn-xapo-ixapo) | Introduced in 10.0.10240. |
| [IXAPOHrtfParameters](/windows/win32/api/hrtfapoapi/nn-hrtfapoapi-ixapohrtfparameters) | Introduced in 10.0.10240. |
| [IXAPOParameters](/windows/win32/api/xapo/nn-xapo-ixapoparameters) | Introduced in 10.0.10240. |
| [IXAudio2](/windows/win32/api/xaudio2/nn-xaudio2-ixaudio2) | Introduced in 10.0.10240. |
| [IXAudio2EngineCallback](/windows/win32/api/xaudio2/nn-xaudio2-ixaudio2enginecallback) | Introduced in 10.0.10240. |
| [IXAudio2MasteringVoice](/windows/win32/api/xaudio2/nn-xaudio2-ixaudio2masteringvoice) | Introduced in 10.0.10240. |
| [IXAudio2SourceVoice](/windows/win32/api/xaudio2/nn-xaudio2-ixaudio2sourcevoice) | Introduced in 10.0.10240. |
| [IXAudio2SubmixVoice](/windows/win32/api/xaudio2/nn-xaudio2-ixaudio2submixvoice) | Introduced in 10.0.10240. |
| [IXAudio2Voice](/windows/win32/api/xaudio2/nn-xaudio2-ixaudio2voice) | Introduced in 10.0.10240. |
| [IXAudio2VoiceCallback](/windows/win32/api/xaudio2/nn-xaudio2-ixaudio2voicecallback) | Introduced in 10.0.10240. |
| [IXMLHTTPRequest2](/windows/win32/api/msxml6/nn-msxml6-ixmlhttprequest2) | Introduced in 10.0.10240. |
| [IXMLHTTPRequest2Callback](/windows/win32/api/msxml6/nn-msxml6-ixmlhttprequest2callback) | Introduced in 10.0.10240. |
| [IXMLHTTPRequest3](/windows/win32/api/msxml6/nn-msxml6-ixmlhttprequest3) | Introduced in 10.0.10240. |
| [IXMLHTTPRequest3Callback](/windows/win32/api/msxml6/nn-msxml6-ixmlhttprequest3callback) | Introduced in 10.0.10240. |
| [IXmlReader](/previous-versions/windows/desktop/ms752743(v=vs.85)) | Introduced in 10.0.10240. |
| [IXmlReaderInput](/previous-versions/windows/desktop/ms752817(v=vs.85)) | Introduced in 10.0.10240. |
| [IXmlResolver](/previous-versions/windows/desktop/ms752841(v=vs.85)) | Introduced in 10.0.10240. |
| [IXmlWriter](/previous-versions/windows/desktop/ms752860(v=vs.85)) | Introduced in 10.0.10240. |
| [IXmlWriterLite](/previous-versions/windows/desktop/mt143569(v=vs.85)) | Introduced in 10.0.10240. |
| [IXmlWriterOutput](/previous-versions/windows/desktop/ms752843(v=vs.85)) | Introduced in 10.0.10240. |
| [IXpsDocumentPackageTarget](/windows/win32/api/xpsobjectmodel_1/nn-xpsobjectmodel_1-ixpsdocumentpackagetarget) | Introduced in 10.0.10240. |
| [IXpsDocumentPackageTarget3D](/windows/win32/api/xpsobjectmodel_2/nn-xpsobjectmodel_2-ixpsdocumentpackagetarget3d) | Introduced in 10.0.10240. |
| [IXpsOMBrush](/windows/win32/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsombrush) | Introduced in 10.0.10240. |
| [IXpsOMCanvas](/windows/win32/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomcanvas) | Introduced in 10.0.10240. |
| [IXpsOMColorProfileResource](/windows/win32/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomcolorprofileresource) | Introduced in 10.0.10240. |
| [IXpsOMColorProfileResourceCollection](/windows/win32/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomcolorprofileresourcecollection) | Introduced in 10.0.10240. |
| [IXpsOMCoreProperties](/windows/win32/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomcoreproperties) | Introduced in 10.0.10240. |
| [IXpsOMDashCollection](/windows/win32/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomdashcollection) | Introduced in 10.0.10240. |
| [IXpsOMDictionary](/windows/win32/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomdictionary) | Introduced in 10.0.10240. |
| [IXpsOMDocument](/windows/win32/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomdocument) | Introduced in 10.0.10240. |
| [IXpsOMDocumentCollection](/windows/win32/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomdocumentcollection) | Introduced in 10.0.10240. |
| [IXpsOMDocumentSequence](/windows/win32/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomdocumentsequence) | Introduced in 10.0.10240. |
| [IXpsOMDocumentStructureResource](/windows/win32/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomdocumentstructureresource) | Introduced in 10.0.10240. |
| [IXpsOMFontResource](/windows/win32/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomfontresource) | Introduced in 10.0.10240. |
| [IXpsOMFontResourceCollection](/windows/win32/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomfontresourcecollection) | Introduced in 10.0.10240. |
| [IXpsOMGeometry](/windows/win32/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomgeometry) | Introduced in 10.0.10240. |
| [IXpsOMGeometryFigure](/windows/win32/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomgeometryfigure) | Introduced in 10.0.10240. |
| [IXpsOMGeometryFigureCollection](/windows/win32/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomgeometryfigurecollection) | Introduced in 10.0.10240. |
| [IXpsOMGlyphs](/windows/win32/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomglyphs) | Introduced in 10.0.10240. |
| [IXpsOMGlyphsEditor](/windows/win32/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomglyphseditor) | Introduced in 10.0.10240. |
| [IXpsOMGradientBrush](/windows/win32/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomgradientbrush) | Introduced in 10.0.10240. |
| [IXpsOMGradientStop](/windows/win32/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomgradientstop) | Introduced in 10.0.10240. |
| [IXpsOMGradientStopCollection](/windows/win32/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomgradientstopcollection) | Introduced in 10.0.10240. |
| [IXpsOMImageBrush](/windows/win32/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomimagebrush) | Introduced in 10.0.10240. |
| [IXpsOMImageResource](/windows/win32/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomimageresource) | Introduced in 10.0.10240. |
| [IXpsOMImageResourceCollection](/windows/win32/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomimageresourcecollection) | Introduced in 10.0.10240. |
| [IXpsOMLinearGradientBrush](/windows/win32/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomlineargradientbrush) | Introduced in 10.0.10240. |
| [IXpsOMMatrixTransform](/windows/win32/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsommatrixtransform) | Introduced in 10.0.10240. |
| [IXpsOMNameCollection](/windows/win32/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomnamecollection) | Introduced in 10.0.10240. |
| [IXpsOMObjectFactory](/windows/win32/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomobjectfactory) | Introduced in 10.0.10240. |
| [IXpsOMObjectFactory1](/windows/win32/api/xpsobjectmodel_1/nn-xpsobjectmodel_1-ixpsomobjectfactory1) | Introduced in 10.0.10240. |
| [IXpsOMPackage](/windows/win32/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsompackage) | Introduced in 10.0.10240. |
| [IXpsOMPackage1](/windows/win32/api/xpsobjectmodel_1/nn-xpsobjectmodel_1-ixpsompackage1) | Introduced in 10.0.10240. |
| [IXpsOMPackageTarget](/windows/win32/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsompackagetarget) | Introduced in 10.0.10240. |
| [IXpsOMPackageWriter](/windows/win32/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsompackagewriter) | Introduced in 10.0.10240. |
| [IXpsOMPackageWriter3D](/windows/win32/api/xpsobjectmodel_2/nn-xpsobjectmodel_2-ixpsompackagewriter3d) | Introduced in 10.0.10240. |
| [IXpsOMPage](/windows/win32/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsompage) | Introduced in 10.0.10240. |
| [IXpsOMPage1](/windows/win32/api/xpsobjectmodel_1/nn-xpsobjectmodel_1-ixpsompage1) | Introduced in 10.0.10240. |
| [IXpsOMPageReference](/windows/win32/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsompagereference) | Introduced in 10.0.10240. |
| [IXpsOMPageReferenceCollection](/windows/win32/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsompagereferencecollection) | Introduced in 10.0.10240. |
| [IXpsOMPart](/windows/win32/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsompart) | Introduced in 10.0.10240. |
| [IXpsOMPartResources](/windows/win32/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsompartresources) | Introduced in 10.0.10240. |
| [IXpsOMPartUriCollection](/windows/win32/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomparturicollection) | Introduced in 10.0.10240. |
| [IXpsOMPath](/windows/win32/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsompath) | Introduced in 10.0.10240. |
| [IXpsOMPrintTicketResource](/windows/win32/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomprintticketresource) | Introduced in 10.0.10240. |
| [IXpsOMRadialGradientBrush](/windows/win32/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomradialgradientbrush) | Introduced in 10.0.10240. |
| [IXpsOMRemoteDictionaryResource](/windows/win32/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomremotedictionaryresource) | Introduced in 10.0.10240. |
| [IXpsOMRemoteDictionaryResource1](/windows/win32/api/xpsobjectmodel_1/nn-xpsobjectmodel_1-ixpsomremotedictionaryresource1) | Introduced in 10.0.10240. |
| [IXpsOMRemoteDictionaryResourceCollection](/windows/win32/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomremotedictionaryresourcecollection) | Introduced in 10.0.10240. |
| [IXpsOMResource](/windows/win32/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomresource) | Introduced in 10.0.10240. |
| [IXpsOMShareable](/windows/win32/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomshareable) | Introduced in 10.0.10240. |
| [IXpsOMSignatureBlockResource](/windows/win32/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomsignatureblockresource) | Introduced in 10.0.10240. |
| [IXpsOMSignatureBlockResourceCollection](/windows/win32/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomsignatureblockresourcecollection) | Introduced in 10.0.10240. |
| [IXpsOMSolidColorBrush](/windows/win32/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomsolidcolorbrush) | Introduced in 10.0.10240. |
| [IXpsOMStoryFragmentsResource](/windows/win32/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomstoryfragmentsresource) | Introduced in 10.0.10240. |
| [IXpsOMTileBrush](/windows/win32/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomtilebrush) | Introduced in 10.0.10240. |
| [IXpsOMVisual](/windows/win32/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomvisual) | Introduced in 10.0.10240. |
| [IXpsOMVisualBrush](/windows/win32/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomvisualbrush) | Introduced in 10.0.10240. |
| [IXpsOMVisualCollection](/windows/win32/api/xpsobjectmodel/nn-xpsobjectmodel-ixpsomvisualcollection) | Introduced in 10.0.10240. |
| IBtRadioController | Introduced in 10.0.10586. |
| IBtCommandCallback | Introduced in 10.0.10586. |
| IBtConnectionObserver | Introduced in 10.0.10586. |
| IBtConnectionObserverCallback | Introduced in 10.0.10586. |
| IBtConnectionObserverCallback2 | Introduced in 10.0.10586. |
| IBtPairingRequest | Introduced in 10.0.10586. |
| IBtPairingRequestCallback | Introduced in 10.0.10586. |
| IBtIncomingPairingCallback | Introduced in 10.0.10586. |
| [ID3D11Device4](/windows/win32/api/d3d11_4/nn-d3d11_4-id3d11device4) | Introduced in 10.0.10586. |
| [IAppxBlockMapBlock](/windows/win32/api/appxpackaging/nn-appxpackaging-iappxblockmapblock) | Introduced in 10.0.14393. |
| [IAppxBlockMapBlocksEnumerator](/windows/win32/api/appxpackaging/nn-appxpackaging-iappxblockmapblocksenumerator) | Introduced in 10.0.14393. |
| [IAppxBlockMapFile](/windows/win32/api/appxpackaging/nn-appxpackaging-iappxblockmapfile) | Introduced in 10.0.14393. |
| [IAppxBlockMapFilesEnumerator](/windows/win32/api/appxpackaging/nn-appxpackaging-iappxblockmapfilesenumerator) | Introduced in 10.0.14393. |
| [IAppxBlockMapReader](/windows/win32/api/appxpackaging/nn-appxpackaging-iappxblockmapreader) | Introduced in 10.0.14393. |
| [IAppxBundleFactory](/windows/win32/api/appxpackaging/nn-appxpackaging-iappxbundlefactory) | Introduced in 10.0.14393. |
| [IAppxBundleWriter](/windows/win32/api/appxpackaging/nn-appxpackaging-iappxbundlewriter) | Introduced in 10.0.14393. |
| [IAppxBundleReader](/windows/win32/api/appxpackaging/nn-appxpackaging-iappxbundlereader) | Introduced in 10.0.14393. |
| [IAppxBundleManifestReader](/windows/win32/api/appxpackaging/nn-appxpackaging-iappxbundlemanifestreader) | Introduced in 10.0.14393. |
| [IAppxBundleManifestPackageInfoEnumerator](/windows/win32/api/appxpackaging/nn-appxpackaging-iappxbundlemanifestpackageinfoenumerator) | Introduced in 10.0.14393. |
| [IAppxBundleManifestPackageInfo](/windows/win32/api/appxpackaging/nn-appxpackaging-iappxbundlemanifestpackageinfo) | Introduced in 10.0.14393. |
| [IAppxFactory](/windows/win32/api/appxpackaging/nn-appxpackaging-iappxfactory) | Introduced in 10.0.14393. |
| [IAppxFile](/windows/win32/api/appxpackaging/nn-appxpackaging-iappxfile) | Introduced in 10.0.14393. |
| [IAppxFilesEnumerator](/windows/win32/api/appxpackaging/nn-appxpackaging-iappxfilesenumerator) | Introduced in 10.0.14393. |
| [IAppxManifestApplication](/windows/win32/api/appxpackaging/nn-appxpackaging-iappxmanifestapplication) | Introduced in 10.0.14393. |
| [IAppxManifestApplicationsEnumerator](/windows/win32/api/appxpackaging/nn-appxpackaging-iappxmanifestapplicationsenumerator) | Introduced in 10.0.14393. |
| [IAppxManifestQualifiedResource](/previous-versions//dn280305(v=vs.85)) | Introduced in 10.0.14393. |
| [IAppxManifestQualifiedResourcesEnumerator](/previous-versions//dn280306(v=vs.85)) | Introduced in 10.0.14393. |
| [IAppxPackageReader](/windows/win32/api/appxpackaging/nn-appxpackaging-iappxpackagereader) | Introduced in 10.0.14393. |
| [IAppxPackageWriter](/windows/win32/api/appxpackaging/nn-appxpackaging-iappxpackagewriter) | Introduced in 10.0.14393. |
| [IAppxManifestDeviceCapabilitiesEnumerator](/windows/win32/api/appxpackaging/nn-appxpackaging-iappxmanifestdevicecapabilitiesenumerator) | Introduced in 10.0.14393. |
| [IAppxManifestPackageId](/windows/win32/api/appxpackaging/nn-appxpackaging-iappxmanifestpackageid) | Introduced in 10.0.14393. |
| [IAppxManifestPackageDependency](/windows/win32/api/appxpackaging/nn-appxpackaging-iappxmanifestpackagedependency) | Introduced in 10.0.14393. |
| [IAppxManifestPackageDependenciesEnumerator](/windows/win32/api/appxpackaging/nn-appxpackaging-iappxmanifestpackagedependenciesenumerator) | Introduced in 10.0.14393. |
| [IAppxManifestProperties](/windows/win32/api/appxpackaging/nn-appxpackaging-iappxmanifestproperties) | Introduced in 10.0.14393. |
| [IAppxManifestReader](/windows/win32/api/appxpackaging/nn-appxpackaging-iappxmanifestreader) | Introduced in 10.0.14393. |
| [IAppxManifestReader2](/windows/win32/api/appxpackaging/nn-appxpackaging-iappxmanifestreader2) | Introduced in 10.0.14393. |
| [IAppxManifestReader3](/previous-versions//mt796945(v=vs.85)) | Introduced in 10.0.14393. |
| [IAppxManifestCapabilitiesEnumerator](/previous-versions//mt796938(v=vs.85)) | Introduced in 10.0.14393. |
| [IAppxManifestTargetDeviceFamiliesEnumerator](/previous-versions//mt796950(v=vs.85)) | Introduced in 10.0.14393. |
| [IAppxManifestTargetDeviceFamily](/windows/win32/api/appxpackaging/nn-appxpackaging-iappxmanifesttargetdevicefamily) | Introduced in 10.0.14393. |
| [IAppxManifestPackageDependency2](/windows/win32/api/appxpackaging/nn-appxpackaging-iappxmanifestpackagedependency2) | Introduced in 10.0.14393. |
| [IAppxManifestResourcesEnumerator](/windows/win32/api/appxpackaging/nn-appxpackaging-iappxmanifestresourcesenumerator) | Introduced in 10.0.14393. |
| [IAppxManifestReader4](/previous-versions//mt796948(v=vs.85)) | Introduced in 10.0.14393. |
| [IAppxManifestOptionalPackageInfo](/windows/win32/api/appxpackaging/nn-appxpackaging-iappxmanifestoptionalpackageinfo) | Introduced in 10.0.14393. |
| [IXblIdpAuthManager](/windows/win32/api/xblidpauthmanager/nn-xblidpauthmanager-ixblidpauthmanager) | Introduced in 10.0.14393. |
| [IXblIdpAuthTokenResult](/windows/win32/api/xblidpauthmanager/nn-xblidpauthmanager-ixblidpauthtokenresult) | Introduced in 10.0.14393. |
| [IAudioFormatEnumerator](/windows/win32/api/spatialaudioclient/nn-spatialaudioclient-iaudioformatenumerator) | Introduced in 10.0.16299. |
| [ID2D1CommandSink3](/windows/win32/api/d2d1_3/nn-d2d1_3-id2d1commandsink3) | Introduced in 10.0.16299. |
| [ID2D1CommandSink4](/windows/win32/api/d2d1_3/nn-d2d1_3-id2d1commandsink4) | Introduced in 10.0.16299. |
| [ID2D1Device3](/windows/win32/api/d2d1_3/nn-d2d1_3-id2d1device3) | Introduced in 10.0.16299. |
| [ID2D1Device4](/windows/win32/api/d2d1_3/nn-d2d1_3-id2d1device4) | Introduced in 10.0.16299. |
| [ID2D1Device5](/windows/win32/api/d2d1_3/nn-d2d1_3-id2d1device5) | Introduced in 10.0.16299. |
| [ID2D1DeviceContext3](/windows/win32/api/d2d1_3/nn-d2d1_3-id2d1devicecontext3) | Introduced in 10.0.16299. |
| [ID2D1DeviceContext4](/windows/win32/api/d2d1_3/nn-d2d1_3-id2d1devicecontext4) | Introduced in 10.0.16299. |
| [ID2D1DeviceContext5](/windows/win32/api/d2d1_3/nn-d2d1_3-id2d1devicecontext5) | Introduced in 10.0.16299. |
| [ID2D1Factory4](/windows/win32/api/d2d1_3/nn-d2d1_3-id2d1factory4) | Introduced in 10.0.16299. |
| [ID2D1Factory5](/windows/win32/api/d2d1_3/nn-d2d1_3-id2d1factory5) | Introduced in 10.0.16299. |
| [ID2D1Factory6](/windows/win32/api/d2d1_3/nn-d2d1_3-id2d1factory6) | Introduced in 10.0.16299. |
| [ID2D1SpriteBatch](/windows/win32/api/d2d1_3/nn-d2d1_3-id2d1spritebatch) | Introduced in 10.0.16299. |
| [ID2D1SvgAttribute](/windows/win32/api/d2d1svg/nn-d2d1svg-id2d1svgattribute) | Introduced in 10.0.16299. |
| [ID2D1SvgDocument](/windows/win32/api/d2d1svg/nn-d2d1svg-id2d1svgdocument) | Introduced in 10.0.16299. |
| [ID2D1SvgElement](/windows/win32/api/d2d1svg/nn-d2d1svg-id2d1svgelement) | Introduced in 10.0.16299. |
| [ID2D1SvgGlyphStyle](/windows/win32/api/d2d1_3/nn-d2d1_3-id2d1svgglyphstyle) | Introduced in 10.0.16299. |
| [ID2D1SvgPaint](/windows/win32/api/d2d1svg/nn-d2d1svg-id2d1svgpaint) | Introduced in 10.0.16299. |
| [ID2D1SvgPathData](/windows/win32/api/d2d1svg/nn-d2d1svg-id2d1svgpathdata) | Introduced in 10.0.16299. |
| [ID2D1SvgPointCollection](/windows/win32/api/d2d1svg/nn-d2d1svg-id2d1svgpointcollection) | Introduced in 10.0.16299. |
| [ID2D1SvgStrokeDashArray](/windows/win32/api/d2d1svg/nn-d2d1svg-id2d1svgstrokedasharray) | Introduced in 10.0.16299. |
| [IDXGIAdapter4](/windows/win32/api/dxgi1_6/nn-dxgi1_6-idxgiadapter4) | Introduced in 10.0.16299. |
| [IMFSpatialAudioObjectBuffer](/windows/win32/api/mfspatialaudio/nn-mfspatialaudio-imfspatialaudioobjectbuffer) | Introduced in 10.0.16299. |
| [IMFSpatialAudioSample](/windows/win32/api/mfspatialaudio/nn-mfspatialaudio-imfspatialaudiosample) | Introduced in 10.0.16299. |
| [IOplockBreakingHandler](/windows/win32/api/windowsstoragecom/nn-windowsstoragecom-ioplockbreakinghandler) | Introduced in 10.0.16299. |
| [ISpatialAudioObject](/windows/win32/api/spatialaudioclient/nn-spatialaudioclient-ispatialaudioobject) | Introduced in 10.0.16299. |
| [ISpatialAudioObjectRenderStream](/windows/win32/api/spatialaudioclient/nn-spatialaudioclient-ispatialaudioobjectrenderstream) | Introduced in 10.0.16299. |
| [ISpatialAudioObjectRenderStreamNotify](/windows/win32/api/spatialaudioclient/nn-spatialaudioclient-ispatialaudioobjectrenderstreamnotify) | Introduced in 10.0.16299. |
| [ISpatialAudioClient](/windows/win32/api/spatialaudioclient/nn-spatialaudioclient-ispatialaudioclient) | Introduced in 10.0.16299. |
| [IStorageItemHandleAccess](/windows/win32/api/windowsstoragecom/nn-windowsstoragecom-istorageitemhandleaccess) | Introduced in 10.0.16299. |
| [IStorageFolderHandleAccess](/windows/win32/api/windowsstoragecom/nn-windowsstoragecom-istoragefolderhandleaccess) | Introduced in 10.0.16299. |
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
| [RDPSession](/previous-versions/windows/desktop/rdp/rdpsession) | Introduced in 10.0.10240. |
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