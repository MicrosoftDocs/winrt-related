---
description: This topic lists the Win32 APIs that are part of the Universal Windows Platform (UWP) and that are implemented by all Windows 10 devices.
title: APIs present on all Windows 10 devices (grouped by module)
ms.topic: article
keywords: windows 10, uwp, win32, COM
ms.date: 10/10/2018
ms.assetid: 9763fa67-0f32-4128-b901-013b1d7ea73c
---

# APIs present on all Windows 10 devices
This topic lists the Win32 APIs that are part of the Universal Windows Platform (UWP) and that are implemented by all Windows 10 devices. For convenience, an umbrella library named WindowsApp.lib is provided in the Microsoft Windows Software Development Kit (SDK), which provides the exports for this set of Win32 APIs. Link your app with WindowsApp.lib (and no other libraries) to access these APIs.

This topic lists all the APIs in WindowsApp.lib, grouped by module (where the module is either an [API set](/windows/win32/apiindex/windows-umbrella-libraries#api_sets) or a dll). Linking to WindowsApp.lib will add to your app dependencies on dlls that are present on all Windows 10 devices. For delay load, use the module name. Note that an umbrella lib can contain some, but not necessarily all, APIs from a given module.

## APIs from api-ms-win-core-com-l1-1-1.dll

| API | Requirements |
| -----| --------------|
| [CLSIDFromString](/windows/win32/api/combaseapi/nf-combaseapi-clsidfromstring) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-com-l1-1-0.dll in 10.0.16299. |
| [CoCreateFreeThreadedMarshaler](/windows/win32/api/combaseapi/nf-combaseapi-cocreatefreethreadedmarshaler) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-com-l1-1-0.dll in 10.0.16299. |
| [CoCreateGuid](/windows/win32/api/combaseapi/nf-combaseapi-cocreateguid) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-com-l1-1-0.dll in 10.0.16299. |
| [CoCreateInstanceFromApp](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstancefromapp) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-com-l1-1-0.dll in 10.0.16299. |
| [CoDisconnectObject](/windows/win32/api/combaseapi/nf-combaseapi-codisconnectobject) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-com-l1-1-0.dll in 10.0.16299. |
| [CoFreeUnusedLibraries](/windows/win32/api/combaseapi/nf-combaseapi-cofreeunusedlibraries) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-com-l1-1-0.dll in 10.0.16299. |
| [CoFreeUnusedLibrariesEx](/windows/win32/api/combaseapi/nf-combaseapi-cofreeunusedlibrariesex) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-com-l1-1-0.dll in 10.0.16299. |
| [CoGetApartmentType](/windows/win32/api/combaseapi/nf-combaseapi-cogetapartmenttype) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-com-l1-1-0.dll in 10.0.16299. |
| [CoGetContextToken](/windows/win32/api/combaseapi/nf-combaseapi-cogetcontexttoken) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-com-l1-1-0.dll in 10.0.16299. |
| [CoGetCurrentLogicalThreadId](/windows/win32/api/combaseapi/nf-combaseapi-cogetcurrentlogicalthreadid) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-com-l1-1-0.dll in 10.0.16299. |
| [CoGetInterfaceAndReleaseStream](/windows/win32/api/combaseapi/nf-combaseapi-cogetinterfaceandreleasestream) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-com-l1-1-0.dll in 10.0.16299. |
| [CoGetMarshalSizeMax](/windows/win32/api/combaseapi/nf-combaseapi-cogetmarshalsizemax) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-com-l1-1-0.dll in 10.0.16299. |
| [CoGetObjectContext](/windows/win32/api/combaseapi/nf-combaseapi-cogetobjectcontext) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-com-l1-1-0.dll in 10.0.16299. |
| [CoGetStandardMarshal](/windows/win32/api/combaseapi/nf-combaseapi-cogetstandardmarshal) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-com-l1-1-0.dll in 10.0.16299. |
| [CoInitializeEx](/windows/win32/api/combaseapi/nf-combaseapi-coinitializeex) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-com-l1-1-0.dll in 10.0.16299. |
| [CoInitializeSecurity](/windows/win32/api/combaseapi/nf-combaseapi-coinitializesecurity) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-com-l1-1-0.dll in 10.0.16299. |
| [CoMarshalInterface](/windows/win32/api/combaseapi/nf-combaseapi-comarshalinterface) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-com-l1-1-0.dll in 10.0.16299. |
| [CoMarshalInterThreadInterfaceInStream](/windows/win32/api/combaseapi/nf-combaseapi-comarshalinterthreadinterfaceinstream) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-com-l1-1-0.dll in 10.0.16299. |
| [CoRegisterClassObject](/windows/win32/api/combaseapi/nf-combaseapi-coregisterclassobject) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-com-l1-1-0.dll in 10.0.16299. |
| [CoReleaseMarshalData](/windows/win32/api/combaseapi/nf-combaseapi-coreleasemarshaldata) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-com-l1-1-0.dll in 10.0.16299. |
| [CoResumeClassObjects](/windows/win32/api/combaseapi/nf-combaseapi-coresumeclassobjects) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-com-l1-1-0.dll in 10.0.16299. |
| [CoRevokeClassObject](/windows/win32/api/combaseapi/nf-combaseapi-corevokeclassobject) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-com-l1-1-0.dll in 10.0.16299. |
| [CoSuspendClassObjects](/windows/win32/api/combaseapi/nf-combaseapi-cosuspendclassobjects) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-com-l1-1-0.dll in 10.0.16299. |
| [CoSwitchCallContext](/windows/win32/api/combaseapi/nf-combaseapi-coswitchcallcontext) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-com-l1-1-0.dll in 10.0.16299. |
| [CoTaskMemAlloc](/windows/win32/api/combaseapi/nf-combaseapi-cotaskmemalloc) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-com-l1-1-0.dll in 10.0.16299. |
| [CoTaskMemFree](/windows/win32/api/combaseapi/nf-combaseapi-cotaskmemfree) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-com-l1-1-0.dll in 10.0.16299. |
| [CoTaskMemRealloc](/windows/win32/api/combaseapi/nf-combaseapi-cotaskmemrealloc) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-com-l1-1-0.dll in 10.0.16299. |
| [CoUninitialize](/windows/win32/api/combaseapi/nf-combaseapi-couninitialize) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-com-l1-1-0.dll in 10.0.16299. |
| [CoUnmarshalInterface](/windows/win32/api/combaseapi/nf-combaseapi-counmarshalinterface) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-com-l1-1-0.dll in 10.0.16299. |
| [CreateStreamOnHGlobal](/windows/win32/api/combaseapi/nf-combaseapi-createstreamonhglobal) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-com-l1-1-0.dll in 10.0.16299. |
| [FreePropVariantArray](/windows/win32/api/propidl/nf-propidl-freepropvariantarray) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-com-l1-1-0.dll in 10.0.16299. |
| [GetHGlobalFromStream](/windows/win32/api/combaseapi/nf-combaseapi-gethglobalfromstream) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-com-l1-1-0.dll in 10.0.16299. |
| [IIDFromString](/windows/win32/api/combaseapi/nf-combaseapi-iidfromstring) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-com-l1-1-0.dll in 10.0.16299. |
| [PropVariantClear](/windows/win32/api/propidl/nf-propidl-propvariantclear) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-com-l1-1-0.dll in 10.0.16299. |
| [PropVariantCopy](/windows/win32/api/propidl/nf-propidl-propvariantcopy) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-com-l1-1-0.dll in 10.0.16299. |
| [RoGetAgileReference](/windows/win32/api/combaseapi/nf-combaseapi-rogetagilereference) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. |
| [StringFromCLSID](/windows/win32/api/combaseapi/nf-combaseapi-stringfromclsid) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-com-l1-1-0.dll in 10.0.16299. |
| [StringFromGUID2](/windows/win32/api/combaseapi/nf-combaseapi-stringfromguid2) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-com-l1-1-0.dll in 10.0.16299. |
| [StringFromIID](/windows/win32/api/combaseapi/nf-combaseapi-stringfromiid) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-com-l1-1-0.dll in 10.0.16299. |


## APIs from api-ms-win-core-com-l2-1-1.dll

| API | Requirements |
| -----| --------------|
| [CreateILockBytesOnHGlobal](/windows/win32/api/coml2api/nf-coml2api-createilockbytesonhglobal) | Introduced into api-ms-win-core-com-l2-1-1.dll in 10.0.10240. |
| [FmtIdToPropStgName](/windows/win32/api/coml2api/nf-coml2api-fmtidtopropstgname) | Introduced into api-ms-win-core-com-l2-1-1.dll in 10.0.10240. |
| [GetConvertStg](/windows/win32/api/coml2api/nf-coml2api-getconvertstg) | Introduced into api-ms-win-core-com-l2-1-1.dll in 10.0.10240. |
| [GetHGlobalFromILockBytes](/windows/win32/api/coml2api/nf-coml2api-gethglobalfromilockbytes) | Introduced into api-ms-win-core-com-l2-1-1.dll in 10.0.10240. |
| [PropStgNameToFmtId](/windows/win32/api/coml2api/nf-coml2api-propstgnametofmtid) | Introduced into api-ms-win-core-com-l2-1-1.dll in 10.0.10240. |
| [ReadClassStg](/windows/win32/api/coml2api/nf-coml2api-readclassstg) | Introduced into api-ms-win-core-com-l2-1-1.dll in 10.0.10240. |
| [ReadClassStm](/windows/win32/api/coml2api/nf-coml2api-readclassstm) | Introduced into api-ms-win-core-com-l2-1-1.dll in 10.0.10240. |
| [StgCreateDocfile](/windows/win32/api/coml2api/nf-coml2api-stgcreatedocfile) | Introduced into api-ms-win-core-com-l2-1-1.dll in 10.0.10240. |
| [StgCreateDocfileOnILockBytes](/windows/win32/api/coml2api/nf-coml2api-stgcreatedocfileonilockbytes) | Introduced into api-ms-win-core-com-l2-1-1.dll in 10.0.10240. |
| [StgCreatePropSetStg](/windows/win32/api/coml2api/nf-coml2api-stgcreatepropsetstg) | Introduced into api-ms-win-core-com-l2-1-1.dll in 10.0.10240. |
| [StgCreatePropStg](/windows/win32/api/coml2api/nf-coml2api-stgcreatepropstg) | Introduced into api-ms-win-core-com-l2-1-1.dll in 10.0.10240. |
| [StgCreateStorageEx](/windows/win32/api/coml2api/nf-coml2api-stgcreatestorageex) | Introduced into api-ms-win-core-com-l2-1-1.dll in 10.0.10240. |
| [StgIsStorageFile](/windows/win32/api/coml2api/nf-coml2api-stgisstoragefile) | Introduced into api-ms-win-core-com-l2-1-1.dll in 10.0.10240. |
| [StgIsStorageILockBytes](/windows/win32/api/coml2api/nf-coml2api-stgisstorageilockbytes) | Introduced into api-ms-win-core-com-l2-1-1.dll in 10.0.10240. |
| [StgOpenPropStg](/windows/win32/api/coml2api/nf-coml2api-stgopenpropstg) | Introduced into api-ms-win-core-com-l2-1-1.dll in 10.0.10240. |
| [StgOpenStorage](/windows/win32/api/coml2api/nf-coml2api-stgopenstorage) | Introduced into api-ms-win-core-com-l2-1-1.dll in 10.0.10240. |
| [StgOpenStorageEx](/windows/win32/api/coml2api/nf-coml2api-stgopenstorageex) | Introduced into api-ms-win-core-com-l2-1-1.dll in 10.0.10240. |
| [StgOpenStorageOnILockBytes](/windows/win32/api/coml2api/nf-coml2api-stgopenstorageonilockbytes) | Introduced into api-ms-win-core-com-l2-1-1.dll in 10.0.10240. |
| [StgSetTimes](/windows/win32/api/coml2api/nf-coml2api-stgsettimes) | Introduced into api-ms-win-core-com-l2-1-1.dll in 10.0.10240. |
| [WriteClassStg](/windows/win32/api/coml2api/nf-coml2api-writeclassstg) | Introduced into api-ms-win-core-com-l2-1-1.dll in 10.0.10240. |
| [WriteClassStm](/windows/win32/api/coml2api/nf-coml2api-writeclassstm) | Introduced into api-ms-win-core-com-l2-1-1.dll in 10.0.10240. |


## APIs from api-ms-win-core-com-midlproxystub-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [CStdAsyncStubBuffer_AddRef](/windows/win32/api/rpcproxy/nf-rpcproxy-cstdasyncstubbuffer_addref) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [CStdAsyncStubBuffer_Connect](/windows/win32/api/rpcproxy/nf-rpcproxy-cstdasyncstubbuffer_connect) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [CStdAsyncStubBuffer_Disconnect](/windows/win32/api/rpcproxy/nf-rpcproxy-cstdasyncstubbuffer_disconnect) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [CStdAsyncStubBuffer_Invoke](/windows/win32/api/rpcproxy/nf-rpcproxy-cstdasyncstubbuffer_invoke) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [CStdAsyncStubBuffer_QueryInterface](/windows/win32/api/rpcproxy/nf-rpcproxy-cstdasyncstubbuffer_queryinterface) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [CStdAsyncStubBuffer_Release](/windows/win32/api/rpcproxy/nf-rpcproxy-cstdasyncstubbuffer_release) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [CStdAsyncStubBuffer2_Connect](/windows/win32/api/rpcproxy/nf-rpcproxy-cstdasyncstubbuffer2_connect) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [CStdAsyncStubBuffer2_Disconnect](/windows/win32/api/rpcproxy/nf-rpcproxy-cstdasyncstubbuffer2_disconnect) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [CStdAsyncStubBuffer2_Release](/windows/win32/api/rpcproxy/nf-rpcproxy-cstdasyncstubbuffer2_release) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [CStdStubBuffer2_Connect](/windows/win32/api/rpcproxy/nf-rpcproxy-cstdstubbuffer2_connect) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [CStdStubBuffer2_CountRefs](/windows/win32/api/rpcproxy/nf-rpcproxy-cstdstubbuffer2_countrefs) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [CStdStubBuffer2_Disconnect](/windows/win32/api/rpcproxy/nf-rpcproxy-cstdstubbuffer2_disconnect) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [CStdStubBuffer2_QueryInterface](/windows/win32/api/rpcproxy/nf-rpcproxy-cstdstubbuffer2_queryinterface) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [NdrProxyForwardingFunction10](/windows/win32/api/rpcproxy/nf-rpcproxy-ndrproxyforwardingfunction10) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [NdrProxyForwardingFunction11](/windows/win32/api/rpcproxy/nf-rpcproxy-ndrproxyforwardingfunction11) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [NdrProxyForwardingFunction12](/windows/win32/api/rpcproxy/nf-rpcproxy-ndrproxyforwardingfunction12) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [NdrProxyForwardingFunction13](/windows/win32/api/rpcproxy/nf-rpcproxy-ndrproxyforwardingfunction13) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [NdrProxyForwardingFunction14](/windows/win32/api/rpcproxy/nf-rpcproxy-ndrproxyforwardingfunction14) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [NdrProxyForwardingFunction15](/windows/win32/api/rpcproxy/nf-rpcproxy-ndrproxyforwardingfunction15) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [NdrProxyForwardingFunction16](/windows/win32/api/rpcproxy/nf-rpcproxy-ndrproxyforwardingfunction16) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [NdrProxyForwardingFunction17](/windows/win32/api/rpcproxy/nf-rpcproxy-ndrproxyforwardingfunction17) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [NdrProxyForwardingFunction18](/windows/win32/api/rpcproxy/nf-rpcproxy-ndrproxyforwardingfunction18) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [NdrProxyForwardingFunction19](/windows/win32/api/rpcproxy/nf-rpcproxy-ndrproxyforwardingfunction19) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [NdrProxyForwardingFunction20](/windows/win32/api/rpcproxy/nf-rpcproxy-ndrproxyforwardingfunction20) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [NdrProxyForwardingFunction21](/windows/win32/api/rpcproxy/nf-rpcproxy-ndrproxyforwardingfunction21) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [NdrProxyForwardingFunction22](/windows/win32/api/rpcproxy/nf-rpcproxy-ndrproxyforwardingfunction22) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [NdrProxyForwardingFunction23](/windows/win32/api/rpcproxy/nf-rpcproxy-ndrproxyforwardingfunction23) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [NdrProxyForwardingFunction24](/windows/win32/api/rpcproxy/nf-rpcproxy-ndrproxyforwardingfunction24) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [NdrProxyForwardingFunction25](/windows/win32/api/rpcproxy/nf-rpcproxy-ndrproxyforwardingfunction25) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [NdrProxyForwardingFunction26](/windows/win32/api/rpcproxy/nf-rpcproxy-ndrproxyforwardingfunction26) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [NdrProxyForwardingFunction27](/windows/win32/api/rpcproxy/nf-rpcproxy-ndrproxyforwardingfunction27) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [NdrProxyForwardingFunction28](/windows/win32/api/rpcproxy/nf-rpcproxy-ndrproxyforwardingfunction28) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [NdrProxyForwardingFunction29](/windows/win32/api/rpcproxy/nf-rpcproxy-ndrproxyforwardingfunction29) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [NdrProxyForwardingFunction3](/windows/win32/api/rpcproxy/nf-rpcproxy-ndrproxyforwardingfunction3) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [NdrProxyForwardingFunction30](/windows/win32/api/rpcproxy/nf-rpcproxy-ndrproxyforwardingfunction30) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [NdrProxyForwardingFunction31](/windows/win32/api/rpcproxy/nf-rpcproxy-ndrproxyforwardingfunction31) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [NdrProxyForwardingFunction32](/windows/win32/api/rpcproxy/nf-rpcproxy-ndrproxyforwardingfunction32) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [NdrProxyForwardingFunction4](/windows/win32/api/rpcproxy/nf-rpcproxy-ndrproxyforwardingfunction4) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [NdrProxyForwardingFunction5](/windows/win32/api/rpcproxy/nf-rpcproxy-ndrproxyforwardingfunction5) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [NdrProxyForwardingFunction6](/windows/win32/api/rpcproxy/nf-rpcproxy-ndrproxyforwardingfunction6) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [NdrProxyForwardingFunction7](/windows/win32/api/rpcproxy/nf-rpcproxy-ndrproxyforwardingfunction7) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [NdrProxyForwardingFunction8](/windows/win32/api/rpcproxy/nf-rpcproxy-ndrproxyforwardingfunction8) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [NdrProxyForwardingFunction9](/windows/win32/api/rpcproxy/nf-rpcproxy-ndrproxyforwardingfunction9) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [ObjectStublessClient10](/windows/win32/api/rpcproxy/nf-rpcproxy-objectstublessclient10) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [ObjectStublessClient11](/windows/win32/api/rpcproxy/nf-rpcproxy-objectstublessclient11) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [ObjectStublessClient12](/windows/win32/api/rpcproxy/nf-rpcproxy-objectstublessclient12) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [ObjectStublessClient13](/windows/win32/api/rpcproxy/nf-rpcproxy-objectstublessclient13) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [ObjectStublessClient14](/windows/win32/api/rpcproxy/nf-rpcproxy-objectstublessclient14) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [ObjectStublessClient15](/windows/win32/api/rpcproxy/nf-rpcproxy-objectstublessclient15) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [ObjectStublessClient16](/windows/win32/api/rpcproxy/nf-rpcproxy-objectstublessclient16) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [ObjectStublessClient17](/windows/win32/api/rpcproxy/nf-rpcproxy-objectstublessclient17) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [ObjectStublessClient18](/windows/win32/api/rpcproxy/nf-rpcproxy-objectstublessclient18) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [ObjectStublessClient19](/windows/win32/api/rpcproxy/nf-rpcproxy-objectstublessclient19) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [ObjectStublessClient20](/windows/win32/api/rpcproxy/nf-rpcproxy-objectstublessclient20) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [ObjectStublessClient21](/windows/win32/api/rpcproxy/nf-rpcproxy-objectstublessclient21) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [ObjectStublessClient22](/windows/win32/api/rpcproxy/nf-rpcproxy-objectstublessclient22) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [ObjectStublessClient23](/windows/win32/api/rpcproxy/nf-rpcproxy-objectstublessclient23) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [ObjectStublessClient24](/windows/win32/api/rpcproxy/nf-rpcproxy-objectstublessclient24) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [ObjectStublessClient25](/windows/win32/api/rpcproxy/nf-rpcproxy-objectstublessclient25) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [ObjectStublessClient26](/windows/win32/api/rpcproxy/nf-rpcproxy-objectstublessclient26) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [ObjectStublessClient27](/windows/win32/api/rpcproxy/nf-rpcproxy-objectstublessclient27) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [ObjectStublessClient28](/windows/win32/api/rpcproxy/nf-rpcproxy-objectstublessclient28) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [ObjectStublessClient29](/windows/win32/api/rpcproxy/nf-rpcproxy-objectstublessclient29) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [ObjectStublessClient3](/windows/win32/api/rpcproxy/nf-rpcproxy-objectstublessclient3) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [ObjectStublessClient30](/windows/win32/api/rpcproxy/nf-rpcproxy-objectstublessclient30) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [ObjectStublessClient31](/windows/win32/api/rpcproxy/nf-rpcproxy-objectstublessclient31) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [ObjectStublessClient32](/windows/win32/api/rpcproxy/nf-rpcproxy-objectstublessclient32) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [ObjectStublessClient4](/windows/win32/api/rpcproxy/nf-rpcproxy-objectstublessclient4) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [ObjectStublessClient5](/windows/win32/api/rpcproxy/nf-rpcproxy-objectstublessclient5) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [ObjectStublessClient6](/windows/win32/api/rpcproxy/nf-rpcproxy-objectstublessclient6) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [ObjectStublessClient7](/windows/win32/api/rpcproxy/nf-rpcproxy-objectstublessclient7) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [ObjectStublessClient8](/windows/win32/api/rpcproxy/nf-rpcproxy-objectstublessclient8) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [ObjectStublessClient9](/windows/win32/api/rpcproxy/nf-rpcproxy-objectstublessclient9) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |


## APIs from api-ms-win-core-datetime-l1-1-1.dll

| API | Requirements |
| -----| --------------|
| [GetDateFormatEx](/windows/win32/api/datetimeapi/nf-datetimeapi-getdateformatex) | Introduced into api-ms-win-core-datetime-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-datetime-l1-1-2.dll in 10.0.10586. Moved into api-ms-win-core-datetime-l1-1-1.dll in 10.0.14393. |
| [GetTimeFormatEx](/windows/win32/api/datetimeapi/nf-datetimeapi-gettimeformatex) | Introduced into api-ms-win-core-datetime-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-datetime-l1-1-2.dll in 10.0.10586. Moved into api-ms-win-core-datetime-l1-1-1.dll in 10.0.14393. |


## APIs from api-ms-win-core-datetime-l1-1-2.dll

| API | Requirements |
| -----| --------------|
| [GetDurationFormatEx](/windows/win32/api/winnls/nf-winnls-getdurationformatex) | Introduced into api-ms-win-core-datetime-l1-1-2.dll in 10.0.10240. |


## APIs from api-ms-win-core-debug-l1-1-1.dll

| API | Requirements |
| -----| --------------|
| [IsDebuggerPresent](/windows/win32/api/debugapi/nf-debugapi-isdebuggerpresent) | Introduced into api-ms-win-core-debug-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-debug-l1-1-2.dll in 10.0.10586. Moved into api-ms-win-core-debug-l1-1-1.dll in 10.0.14393. Moved into api-ms-win-core-debug-l1-1-0.dll in 10.0.16299. |
| [OutputDebugStringA](/windows/win32/api/debugapi/nf-debugapi-outputdebugstringa) | Introduced into api-ms-win-core-debug-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-debug-l1-1-2.dll in 10.0.10586. Moved into api-ms-win-core-debug-l1-1-1.dll in 10.0.14393. Moved into api-ms-win-core-debug-l1-1-0.dll in 10.0.16299. |
| [OutputDebugStringW](/windows/win32/api/debugapi/nf-debugapi-outputdebugstringa) | Introduced into api-ms-win-core-debug-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-debug-l1-1-2.dll in 10.0.10586. Moved into api-ms-win-core-debug-l1-1-1.dll in 10.0.14393. Moved into api-ms-win-core-debug-l1-1-0.dll in 10.0.16299. |


## APIs from api-ms-win-core-delayload-l1-1-1.dll

| API | Requirements |
| -----| --------------|
| [DelayLoadFailureHook](/windows/win32/devnotes/delayloadfailurehook) | Introduced into api-ms-win-core-delayload-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-delayload-l1-1-0.dll in 10.0.16299. |
| [ResolveDelayLoadedAPI](/windows/win32/devnotes/resolvedelayloadedapi) | Introduced into api-ms-win-core-delayload-l1-1-1.dll in 10.0.10240. |
| [ResolveDelayLoadsFromDll](/windows/win32/devnotes/resolvedelayloadsfromdll) | Introduced into api-ms-win-core-delayload-l1-1-1.dll in 10.0.10240. |


## APIs from api-ms-win-core-errorhandling-l1-1-1.dll

| API | Requirements |
| -----| --------------|
| [GetLastError](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getlasterror) | Introduced into api-ms-win-core-errorhandling-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-errorhandling-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-errorhandling-l1-1-1.dll in 10.0.14393. Moved into api-ms-win-core-errorhandling-l1-1-0.dll in 10.0.16299. |
| [RaiseException](/windows/win32/api/errhandlingapi/nf-errhandlingapi-raiseexception) | Introduced into api-ms-win-core-errorhandling-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-errorhandling-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-errorhandling-l1-1-1.dll in 10.0.14393. Moved into api-ms-win-core-errorhandling-l1-1-0.dll in 10.0.16299. |
| [SetLastError](/windows/win32/api/errhandlingapi/nf-errhandlingapi-setlasterror) | Introduced into api-ms-win-core-errorhandling-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-errorhandling-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-errorhandling-l1-1-1.dll in 10.0.14393. Moved into api-ms-win-core-errorhandling-l1-1-0.dll in 10.0.16299. |


## APIs from api-ms-win-core-errorhandling-l1-1-3.dll

| API | Requirements |
| -----| --------------|
| [RaiseFailFastException](/windows/win32/api/errhandlingapi/nf-errhandlingapi-raisefailfastexception) | Introduced into api-ms-win-core-errorhandling-l1-1-3.dll in 10.0.10240. Moved into api-ms-win-core-errorhandling-l1-1-2.dll in 10.0.16299. |
| [SetUnhandledExceptionFilter](/windows/win32/api/errhandlingapi/nf-errhandlingapi-setunhandledexceptionfilter) | Introduced into api-ms-win-core-errorhandling-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-errorhandling-l1-1-1.dll in 10.0.14393. Moved into api-ms-win-core-errorhandling-l1-1-0.dll in 10.0.16299. |
| [GetThreadErrorMode](/windows/win32/api/errhandlingapi/nf-errhandlingapi-getthreaderrormode) | Introduced into api-ms-win-core-errorhandling-l1-1-3.dll in 10.0.16299. |
| [SetThreadErrorMode](/windows/win32/api/errhandlingapi/nf-errhandlingapi-setthreaderrormode) | Introduced into api-ms-win-core-errorhandling-l1-1-3.dll in 10.0.16299. |


## APIs from api-ms-win-core-fibers-l1-1-1.dll

| API | Requirements |
| -----| --------------|
| [FlsAlloc](/windows/win32/api/fibersapi/nf-fibersapi-flsalloc) | Introduced into api-ms-win-core-fibers-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-fibers-l1-1-0.dll in 10.0.16299. |
| [FlsFree](/windows/win32/api/fibersapi/nf-fibersapi-flsfree) | Introduced into api-ms-win-core-fibers-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-fibers-l1-1-0.dll in 10.0.16299. |
| [FlsGetValue](/windows/win32/api/fibersapi/nf-fibersapi-flsgetvalue) | Introduced into api-ms-win-core-fibers-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-fibers-l1-1-0.dll in 10.0.16299. |
| [FlsSetValue](/windows/win32/api/fibersapi/nf-fibersapi-flssetvalue) | Introduced into api-ms-win-core-fibers-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-fibers-l1-1-0.dll in 10.0.16299. |
| [IsThreadAFiber](/windows/win32/api/fibersapi/nf-fibersapi-isthreadafiber) | Introduced into api-ms-win-core-fibers-l1-1-1.dll in 10.0.10240. |


## APIs from api-ms-win-core-fibers-l2-1-1.dll

| API | Requirements |
| -----| --------------|
| CalloutOnFiberStack | Introduced into api-ms-win-core-fibers-l2-1-1.dll in 10.0.10240. Removed in 10.0.10586. |
| [ConvertFiberToThread](/windows/win32/api/winbase/nf-winbase-convertfibertothread) | Introduced into api-ms-win-core-fibers-l2-1-1.dll in 10.0.10240. Moved into api-ms-win-core-fibers-l2-1-0.dll in 10.0.16299. |
| [ConvertThreadToFiberEx](/windows/win32/api/winbase/nf-winbase-convertthreadtofiberex) | Introduced into api-ms-win-core-fibers-l2-1-1.dll in 10.0.10240. |
| [CreateFiberEx](/windows/win32/api/winbase/nf-winbase-createfiberex) | Introduced into api-ms-win-core-fibers-l2-1-1.dll in 10.0.10240. |
| [DeleteFiber](/windows/win32/api/winbase/nf-winbase-deletefiber) | Introduced into api-ms-win-core-fibers-l2-1-1.dll in 10.0.10240. Moved into api-ms-win-core-fibers-l2-1-0.dll in 10.0.16299. |
| [SwitchToFiber](/windows/win32/api/winbase/nf-winbase-switchtofiber) | Introduced into api-ms-win-core-fibers-l2-1-1.dll in 10.0.10240. Moved into api-ms-win-core-fibers-l2-1-0.dll in 10.0.16299. |


## APIs from api-ms-win-core-file-ansi-l2-1-0.dll

| API | Requirements |
| -----| --------------|
| [ReplaceFileA](/windows/win32/api/winbase/nf-winbase-replacefilea) | Introduced into api-ms-win-core-file-ansi-l2-1-0.dll in 10.0.10240. |
| [CopyFileExA](/windows/win32/api/winbase/nf-winbase-copyfileexa) | Introduced into api-ms-win-core-file-ansi-l2-1-0.dll in 10.0.16299. |


## APIs from api-ms-win-core-file-l1-2-1.dll

| API | Requirements |
| -----| --------------|
| [CreateDirectoryA](/windows/win32/api/fileapi/nf-fileapi-createdirectorya) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. |
| [CreateDirectoryW](/windows/win32/api/fileapi/nf-fileapi-createdirectorya) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. |
| [CreateFile2](/windows/win32/api/fileapi/nf-fileapi-createfile2) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-file-l1-2-0.dll in 10.0.16299. |
| [DeleteFileA](/windows/win32/api/fileapi/nf-fileapi-deletefilea) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. |
| [DeleteFileW](/windows/win32/api/fileapi/nf-fileapi-deletefilea) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. |
| [FindClose](/windows/win32/api/fileapi/nf-fileapi-findclose) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. |
| [FindFirstFileExA](/windows/win32/api/fileapi/nf-fileapi-findfirstfileexa) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. |
| [FindFirstFileExW](/windows/win32/api/fileapi/nf-fileapi-findfirstfileexa) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. |
| [FindNextFileA](/windows/win32/api/fileapi/nf-fileapi-findnextfilea) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. |
| [FindNextFileW](/windows/win32/api/fileapi/nf-fileapi-findnextfilea) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. |
| [FlushFileBuffers](/windows/win32/api/fileapi/nf-fileapi-flushfilebuffers) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. |
| [GetDiskFreeSpaceExA](/windows/win32/api/fileapi/nf-fileapi-getdiskfreespaceexa) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. |
| [GetDiskFreeSpaceExW](/windows/win32/api/fileapi/nf-fileapi-getdiskfreespaceexa) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. |
| [GetFileAttributesExA](/windows/win32/api/fileapi/nf-fileapi-getfileattributesexa) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. |
| [GetFileAttributesExW](/windows/win32/api/fileapi/nf-fileapi-getfileattributesexa) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. |
| [GetFileSizeEx](/windows/win32/api/fileapi/nf-fileapi-getfilesizeex) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. |
| [GetFileTime](/windows/win32/api/fileapi/nf-fileapi-getfiletime) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. |
| [GetFileType](/windows/win32/api/fileapi/nf-fileapi-getfiletype) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. |
| [GetFullPathNameW](/windows/win32/api/fileapi/nf-fileapi-getfullpathnamea) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. |
| [GetLongPathNameW](/windows/win32/api/fileapi/nf-fileapi-getlongpathnamea) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. |
| [GetTempFileNameW](/windows/win32/api/fileapi/nf-fileapi-gettempfilenamea) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. |
| [GetTempPathW](/windows/win32/api/fileapi/nf-fileapi-gettemppatha) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-file-l1-2-0.dll in 10.0.16299. |
| [LockFileEx](/windows/win32/api/fileapi/nf-fileapi-lockfileex) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. |
| [ReadFile](/windows/win32/api/fileapi/nf-fileapi-readfile) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. |
| [RemoveDirectoryA](/windows/win32/api/fileapi/nf-fileapi-removedirectorya) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. |
| [RemoveDirectoryW](/windows/win32/api/fileapi/nf-fileapi-removedirectorya) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. |
| [SetEndOfFile](/windows/win32/api/fileapi/nf-fileapi-setendoffile) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. |
| [SetFileAttributesA](/windows/win32/api/fileapi/nf-fileapi-setfileattributesa) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. |
| [SetFileAttributesW](/windows/win32/api/fileapi/nf-fileapi-setfileattributesa) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. |
| [SetFileInformationByHandle](/windows/win32/api/fileapi/nf-fileapi-setfileinformationbyhandle) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. |
| [SetFilePointerEx](/windows/win32/api/fileapi/nf-fileapi-setfilepointerex) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. |
| [SetFileTime](/windows/win32/api/fileapi/nf-fileapi-setfiletime) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. |
| [UnlockFileEx](/windows/win32/api/fileapi/nf-fileapi-unlockfileex) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. |
| [WriteFile](/windows/win32/api/fileapi/nf-fileapi-writefile) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. |
| [FileTimeToLocalFileTime](/windows/win32/api/fileapi/nf-fileapi-filetimetolocalfiletime) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. |
| [FindFirstFileA](/windows/win32/api/fileapi/nf-fileapi-findfirstfilea) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. |
| [FindFirstFileW](/windows/win32/api/fileapi/nf-fileapi-findfirstfilea) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. |
| [GetDiskFreeSpaceA](/windows/win32/api/fileapi/nf-fileapi-getdiskfreespacea) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. |
| [GetDiskFreeSpaceW](/windows/win32/api/fileapi/nf-fileapi-getdiskfreespacea) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. |
| [GetFileAttributesA](/windows/win32/api/fileapi/nf-fileapi-getfileattributesa) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. |
| [GetFileAttributesW](/windows/win32/api/fileapi/nf-fileapi-getfileattributesa) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. |
| [GetFinalPathNameByHandleA](/windows/win32/api/fileapi/nf-fileapi-getfinalpathnamebyhandlea) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. |
| [GetFinalPathNameByHandleW](/windows/win32/api/fileapi/nf-fileapi-getfinalpathnamebyhandlea) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. |
| [LocalFileTimeToFileTime](/windows/win32/api/fileapi/nf-fileapi-localfiletimetofiletime) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. |
| [ReadFileEx](/windows/win32/api/fileapi/nf-fileapi-readfileex) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. |
| [SetFilePointer](/windows/win32/api/fileapi/nf-fileapi-setfilepointer) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. |
| [WriteFileEx](/windows/win32/api/fileapi/nf-fileapi-writefileex) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. |


## APIs from api-ms-win-core-file-l2-1-1.dll

| API | Requirements |
| -----| --------------|
| [CopyFile2](/windows/win32/api/winbase/nf-winbase-copyfile2) | Introduced into api-ms-win-core-file-l2-1-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l2-1-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l2-1-1.dll in 10.0.14393. Moved into api-ms-win-core-file-l2-1-0.dll in 10.0.16299. |
| [GetFileInformationByHandleEx](/windows/win32/api/winbase/nf-winbase-getfileinformationbyhandleex) | Introduced into api-ms-win-core-file-l2-1-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l2-1-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l2-1-1.dll in 10.0.14393. Moved into api-ms-win-core-file-l2-1-0.dll in 10.0.16299. |
| [MoveFileExW](/windows/win32/api/winbase/nf-winbase-movefileexa) | Introduced into api-ms-win-core-file-l2-1-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l2-1-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l2-1-1.dll in 10.0.14393. Moved into api-ms-win-core-file-l2-1-0.dll in 10.0.16299. |
| [ReplaceFileW](/windows/win32/api/winbase/nf-winbase-replacefilea) | Introduced into api-ms-win-core-file-l2-1-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l2-1-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l2-1-1.dll in 10.0.14393. Moved into api-ms-win-core-file-l2-1-0.dll in 10.0.16299. |


## APIs from api-ms-win-core-handle-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [CloseHandle](/windows/win32/api/handleapi/nf-handleapi-closehandle) | Introduced into api-ms-win-core-handle-l1-1-0.dll in 10.0.10240. |
| [CompareObjectHandles](/windows/win32/api/handleapi/nf-handleapi-compareobjecthandles) | Introduced into api-ms-win-core-handle-l1-1-0.dll in 10.0.10240. |
| [DuplicateHandle](/windows/win32/api/ntsecpkg/nc-ntsecpkg-lsa_duplicate_handle) | Introduced into api-ms-win-core-handle-l1-1-0.dll in 10.0.10240. |


## APIs from api-ms-win-core-heap-l1-2-0.dll

| API | Requirements |
| -----| --------------|
| [GetProcessHeap](/windows/win32/api/heapapi/nf-heapapi-getprocessheap) | Introduced into api-ms-win-core-heap-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-heap-l1-1-0.dll in 10.0.16299. |
| [HeapAlloc](/windows/win32/api/heapapi/nf-heapapi-heapalloc) | Introduced into api-ms-win-core-heap-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-heap-l1-1-0.dll in 10.0.16299. |
| [HeapCompact](/windows/win32/api/heapapi/nf-heapapi-heapcompact) | Introduced into api-ms-win-core-heap-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-heap-l1-1-0.dll in 10.0.16299. |
| [HeapCreate](/windows/win32/api/heapapi/nf-heapapi-heapcreate) | Introduced into api-ms-win-core-heap-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-heap-l1-1-0.dll in 10.0.16299. |
| [HeapDestroy](/windows/win32/api/heapapi/nf-heapapi-heapdestroy) | Introduced into api-ms-win-core-heap-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-heap-l1-1-0.dll in 10.0.16299. |
| [HeapFree](/windows/win32/api/heapapi/nf-heapapi-heapfree) | Introduced into api-ms-win-core-heap-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-heap-l1-1-0.dll in 10.0.16299. |
| [HeapReAlloc](/windows/win32/api/heapapi/nf-heapapi-heaprealloc) | Introduced into api-ms-win-core-heap-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-heap-l1-1-0.dll in 10.0.16299. |
| [HeapSetInformation](/windows/win32/api/heapapi/nf-heapapi-heapsetinformation) | Introduced into api-ms-win-core-heap-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-heap-l1-1-0.dll in 10.0.16299. |
| [HeapSize](/windows/win32/api/heapapi/nf-heapapi-heapsize) | Introduced into api-ms-win-core-heap-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-heap-l1-1-0.dll in 10.0.16299. |


## APIs from api-ms-win-core-interlocked-l1-2-0.dll

| API | Requirements |
| -----| --------------|
| [InitializeSListHead](/windows/win32/api/interlockedapi/nf-interlockedapi-initializeslisthead) | Introduced into api-ms-win-core-interlocked-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-interlocked-l1-1-0.dll in 10.0.16299. |
| [InterlockedFlushSList](/windows/win32/api/interlockedapi/nf-interlockedapi-interlockedflushslist) | Introduced into api-ms-win-core-interlocked-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-interlocked-l1-1-0.dll in 10.0.16299. |
| [InterlockedPopEntrySList](/windows/win32/api/interlockedapi/nf-interlockedapi-interlockedpopentryslist) | Introduced into api-ms-win-core-interlocked-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-interlocked-l1-1-0.dll in 10.0.16299. |
| [InterlockedPushEntrySList](/windows/win32/api/interlockedapi/nf-interlockedapi-interlockedpushentryslist) | Introduced into api-ms-win-core-interlocked-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-interlocked-l1-1-0.dll in 10.0.16299. |
| [InterlockedPushListSListEx](/windows/win32/api/interlockedapi/nf-interlockedapi-interlockedpushlistslistex) | Introduced into api-ms-win-core-interlocked-l1-2-0.dll in 10.0.10240. |
| [QueryDepthSList](/windows/win32/api/interlockedapi/nf-interlockedapi-querydepthslist) | Introduced into api-ms-win-core-interlocked-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-interlocked-l1-1-0.dll in 10.0.16299. |


## APIs from api-ms-win-core-io-l1-1-1.dll

| API | Requirements |
| -----| --------------|
| [CancelIoEx](/windows/win32/api/ioapiset/nf-ioapiset-cancelioex) | Introduced into api-ms-win-core-io-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-io-l1-1-0.dll in 10.0.16299. |
| [GetOverlappedResultEx](/windows/win32/api/ioapiset/nf-ioapiset-getoverlappedresultex) | Introduced into api-ms-win-core-io-l1-1-1.dll in 10.0.10240. |
| [CancelIo](/windows/win32/api/ioapiset/nf-ioapiset-cancelio) | Introduced into api-ms-win-core-io-l1-1-1.dll in 10.0.14393. |
| [CreateIoCompletionPort](/windows/win32/api/ioapiset/nf-ioapiset-createiocompletionport) | Introduced into api-ms-win-core-io-l1-1-1.dll in 10.0.14393. Moved into api-ms-win-core-io-l1-1-0.dll in 10.0.16299. |
| [GetOverlappedResult](/windows/win32/api/ioapiset/nf-ioapiset-getoverlappedresult) | Introduced into api-ms-win-core-io-l1-1-1.dll in 10.0.14393. Moved into api-ms-win-core-io-l1-1-0.dll in 10.0.16299. |
| [GetQueuedCompletionStatus](/windows/win32/api/ioapiset/nf-ioapiset-getqueuedcompletionstatus) | Introduced into api-ms-win-core-io-l1-1-1.dll in 10.0.14393. Moved into api-ms-win-core-io-l1-1-0.dll in 10.0.16299. |
| [GetQueuedCompletionStatusEx](/windows/win32/api/ioapiset/nf-ioapiset-getqueuedcompletionstatusex) | Introduced into api-ms-win-core-io-l1-1-1.dll in 10.0.14393. Moved into api-ms-win-core-io-l1-1-0.dll in 10.0.16299. |
| [PostQueuedCompletionStatus](/windows/win32/api/ioapiset/nf-ioapiset-postqueuedcompletionstatus) | Introduced into api-ms-win-core-io-l1-1-1.dll in 10.0.14393. Moved into api-ms-win-core-io-l1-1-0.dll in 10.0.16299. |


## APIs from api-ms-win-core-kernel32-legacy-l1-1-1.dll

| API | Requirements |
| -----| --------------|
| [MoveFileExA](/windows/win32/api/winbase/nf-winbase-movefileexa) | Introduced into api-ms-win-core-kernel32-legacy-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-kernel32-legacy-l1-1-4.dll in 10.0.10586. Moved into api-ms-win-core-kernel32-legacy-l1-1-1.dll in 10.0.14393. Moved into api-ms-win-core-kernel32-legacy-l1-1-0.dll in 10.0.16299. |


## APIs from api-ms-win-core-largeinteger-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [MulDiv](/windows/win32/api/winbase/nf-winbase-muldiv) | Introduced into api-ms-win-core-largeinteger-l1-1-0.dll in 10.0.10240. |


## APIs from api-ms-win-core-libraryloader-l1-2-0.dll

| API | Requirements |
| -----| --------------|
| [DisableThreadLibraryCalls](/windows/win32/api/libloaderapi/nf-libloaderapi-disablethreadlibrarycalls) | Introduced into api-ms-win-core-libraryloader-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-libraryloader-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-libraryloader-l1-2-0.dll in 10.0.14393. |
| [FindStringOrdinal](/windows/win32/api/libloaderapi/nf-libloaderapi-findstringordinal) | Introduced into api-ms-win-core-libraryloader-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-libraryloader-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-libraryloader-l1-2-0.dll in 10.0.14393. |
| [FreeLibrary](/windows/win32/api/libloaderapi/nf-libloaderapi-freelibrary) | Introduced into api-ms-win-core-libraryloader-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-libraryloader-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-libraryloader-l1-2-0.dll in 10.0.14393. |
| [GetModuleFileNameA](/windows/win32/api/libloaderapi/nf-libloaderapi-getmodulefilenamea) | Introduced into api-ms-win-core-libraryloader-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-libraryloader-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-libraryloader-l1-2-0.dll in 10.0.14393. |
| [GetModuleFileNameW](/windows/win32/api/libloaderapi/nf-libloaderapi-getmodulefilenamea) | Introduced into api-ms-win-core-libraryloader-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-libraryloader-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-libraryloader-l1-2-0.dll in 10.0.14393. |
| [GetProcAddress](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) | Introduced into api-ms-win-core-libraryloader-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-libraryloader-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-libraryloader-l1-2-0.dll in 10.0.14393. |


## APIs from api-ms-win-core-libraryloader-l2-1-0.dll

| API | Requirements |
| -----| --------------|
| [LoadPackagedLibrary](/windows/win32/api/winbase/nf-winbase-loadpackagedlibrary) | Introduced into api-ms-win-core-libraryloader-l2-1-0.dll in 10.0.10240. |
| [QueryOptionalDelayLoadedAPI](/windows/win32/api/libloaderapi2/nf-libloaderapi2-queryoptionaldelayloadedapi) | Introduced into api-ms-win-core-libraryloader-l2-1-0.dll in 10.0.10240. |


## APIs from api-ms-win-core-localization-ansi-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [GetStringTypeExA](/windows/win32/api/stringapiset/nf-stringapiset-getstringtypeexw) | Introduced into api-ms-win-core-localization-ansi-l1-1-0.dll in 10.0.10240. |
| [EnumUILanguagesA](/windows/win32/api/winnls/nf-winnls-enumuilanguagesa) | Introduced into api-ms-win-core-localization-ansi-l1-1-0.dll in 10.0.16299. |


## APIs from api-ms-win-core-localization-l1-2-1.dll

| API | Requirements |
| -----| --------------|
| [EnumSystemGeoID](/windows/win32/api/winnls/nf-winnls-enumsystemgeoid) | Introduced into api-ms-win-core-localization-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-localization-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-localization-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-localization-l1-2-0.dll in 10.0.16299. |
| [EnumSystemLocalesEx](/windows/win32/api/winnls/nf-winnls-enumsystemlocalesex) | Introduced into api-ms-win-core-localization-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-localization-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-localization-l1-2-1.dll in 10.0.14393. |
| [FindNLSStringEx](/windows/win32/api/winnls/nf-winnls-findnlsstringex) | Introduced into api-ms-win-core-localization-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-localization-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-localization-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-localization-l1-2-0.dll in 10.0.16299. |
| [FormatMessageA](/windows/win32/api/winbase/nf-winbase-formatmessage) | Introduced into api-ms-win-core-localization-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-localization-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-localization-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-localization-l1-2-0.dll in 10.0.16299. |
| [FormatMessageW](/windows/win32/api/winbase/nf-winbase-formatmessage) | Introduced into api-ms-win-core-localization-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-localization-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-localization-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-localization-l1-2-0.dll in 10.0.16299. |
| [GetCalendarInfoEx](/windows/win32/api/winnls/nf-winnls-getcalendarinfoex) | Introduced into api-ms-win-core-localization-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-localization-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-localization-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-localization-l1-2-0.dll in 10.0.16299. |
| [GetCPInfo](/windows/win32/api/winnls/nf-winnls-getcpinfo) | Introduced into api-ms-win-core-localization-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-localization-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-localization-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-localization-l1-2-0.dll in 10.0.16299. |
| [GetCPInfoExW](/windows/win32/api/winnls/nf-winnls-getcpinfoexa) | Introduced into api-ms-win-core-localization-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-localization-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-localization-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-localization-l1-2-0.dll in 10.0.16299. |
| [GetGeoInfoW](/windows/win32/api/winnls/nf-winnls-getgeoinfoa) | Introduced into api-ms-win-core-localization-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-localization-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-localization-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-localization-l1-2-0.dll in 10.0.16299. |
| [GetLocaleInfoEx](/windows/win32/api/winnls/nf-winnls-getlocaleinfoex) | Introduced into api-ms-win-core-localization-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-localization-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-localization-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-localization-l1-2-0.dll in 10.0.16299. |
| [GetNLSVersionEx](/windows/win32/api/winnls/nf-winnls-getnlsversionex) | Introduced into api-ms-win-core-localization-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-localization-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-localization-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-localization-l1-2-0.dll in 10.0.16299. |
| [GetUserDefaultLocaleName](/windows/win32/api/winnls/nf-winnls-getuserdefaultlocalename) | Introduced into api-ms-win-core-localization-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-localization-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-localization-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-localization-l1-2-0.dll in 10.0.16299. |
| [GetUserGeoID](/windows/win32/api/winnls/nf-winnls-getusergeoid) | Introduced into api-ms-win-core-localization-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-localization-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-localization-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-localization-l1-2-0.dll in 10.0.16299. |
| [IdnToAscii](/windows/win32/api/winnls/nf-winnls-idntoascii) | Introduced into api-ms-win-core-localization-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-localization-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-localization-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-localization-l1-2-0.dll in 10.0.16299. |
| [IdnToUnicode](/windows/win32/api/winnls/nf-winnls-idntounicode) | Introduced into api-ms-win-core-localization-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-localization-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-localization-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-localization-l1-2-0.dll in 10.0.16299. |
| [IsValidCodePage](/windows/win32/api/winnls/nf-winnls-isvalidcodepage) | Introduced into api-ms-win-core-localization-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-localization-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-localization-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-localization-l1-2-0.dll in 10.0.16299. |
| [IsValidLocaleName](/windows/win32/api/winnls/nf-winnls-isvalidlocalename) | Introduced into api-ms-win-core-localization-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-localization-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-localization-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-localization-l1-2-0.dll in 10.0.16299. |
| [IsValidNLSVersion](/windows/win32/api/winnls/nf-winnls-isvalidnlsversion) | Introduced into api-ms-win-core-localization-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-localization-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-localization-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-localization-l1-2-0.dll in 10.0.16299. |
| [LCMapStringEx](/windows/win32/api/winnls/nf-winnls-lcmapstringex) | Introduced into api-ms-win-core-localization-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-localization-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-localization-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-localization-l1-2-0.dll in 10.0.16299. |
| [LocaleNameToLCID](/windows/win32/api/winnls/nf-winnls-localenametolcid) | Introduced into api-ms-win-core-localization-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-localization-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-localization-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-localization-l1-2-0.dll in 10.0.16299. |
| [ResolveLocaleName](/windows/win32/api/winnls/nf-winnls-resolvelocalename) | Introduced into api-ms-win-core-localization-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-localization-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-localization-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-localization-l1-2-0.dll in 10.0.16299. |


## APIs from api-ms-win-core-localization-l1-2-2.dll

| API | Requirements |
| -----| --------------|
| [GetSystemDefaultLocaleName](/windows/win32/api/winnls/nf-winnls-getsystemdefaultlocalename) | Introduced into api-ms-win-core-localization-l1-2-2.dll in 10.0.10240. |
| [LCIDToLocaleName](/windows/win32/api/winnls/nf-winnls-lcidtolocalename) | Introduced into api-ms-win-core-localization-l1-2-2.dll in 10.0.10240. |


## APIs from api-ms-win-core-localization-l2-1-0.dll

| API | Requirements |
| -----| --------------|
| [EnumCalendarInfoExEx](/windows/win32/api/winnls/nf-winnls-enumcalendarinfoexex) | Introduced into api-ms-win-core-localization-l2-1-0.dll in 10.0.10240. |
| [EnumDateFormatsExEx](/windows/win32/api/winnls/nf-winnls-enumdateformatsexex) | Introduced into api-ms-win-core-localization-l2-1-0.dll in 10.0.10240. |
| [EnumSystemCodePagesW](/windows/win32/api/winnls/nf-winnls-enumsystemcodepagesa) | Introduced into api-ms-win-core-localization-l2-1-0.dll in 10.0.10240. |
| [EnumTimeFormatsEx](/windows/win32/api/winnls/nf-winnls-enumtimeformatsex) | Introduced into api-ms-win-core-localization-l2-1-0.dll in 10.0.10240. |
| [GetCurrencyFormatEx](/windows/win32/api/winnls/nf-winnls-getcurrencyformatex) | Introduced into api-ms-win-core-localization-l2-1-0.dll in 10.0.10240. |
| [GetNumberFormatEx](/windows/win32/api/winnls/nf-winnls-getnumberformatex) | Introduced into api-ms-win-core-localization-l2-1-0.dll in 10.0.10240. |


## APIs from api-ms-win-core-memory-l1-1-2.dll

| API | Requirements |
| -----| --------------|
| [CreateFileMappingFromApp](/windows/win32/api/memoryapi/nf-memoryapi-createfilemappingfromapp) | Introduced into api-ms-win-core-memory-l1-1-2.dll in 10.0.10240. Moved into api-ms-win-core-memory-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-memory-l1-1-2.dll in 10.0.14393. Moved into api-ms-win-core-memory-l1-1-1.dll in 10.0.16299. |
| [DiscardVirtualMemory](/windows/win32/api/memoryapi/nf-memoryapi-discardvirtualmemory) | Introduced into api-ms-win-core-memory-l1-1-2.dll in 10.0.10240. Moved into api-ms-win-core-memory-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-memory-l1-1-2.dll in 10.0.14393. |
| [FlushViewOfFile](/windows/win32/api/memoryapi/nf-memoryapi-flushviewoffile) | Introduced into api-ms-win-core-memory-l1-1-2.dll in 10.0.10240. Moved into api-ms-win-core-memory-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-memory-l1-1-2.dll in 10.0.14393. Moved into api-ms-win-core-memory-l1-1-0.dll in 10.0.16299. |
| [GetWriteWatch](/windows/win32/api/memoryapi/nf-memoryapi-getwritewatch) | Introduced into api-ms-win-core-memory-l1-1-2.dll in 10.0.10240. Moved into api-ms-win-core-memory-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-memory-l1-1-2.dll in 10.0.14393. Moved into api-ms-win-core-memory-l1-1-1.dll in 10.0.16299. |
| [MapViewOfFileFromApp](/windows/win32/api/memoryapi/nf-memoryapi-mapviewoffilefromapp) | Introduced into api-ms-win-core-memory-l1-1-2.dll in 10.0.10240. Moved into api-ms-win-core-memory-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-memory-l1-1-2.dll in 10.0.14393. Moved into api-ms-win-core-memory-l1-1-1.dll in 10.0.16299. |
| [OfferVirtualMemory](/windows/win32/api/memoryapi/nf-memoryapi-offervirtualmemory) | Introduced into api-ms-win-core-memory-l1-1-2.dll in 10.0.10240. Moved into api-ms-win-core-memory-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-memory-l1-1-2.dll in 10.0.14393. |
| [ReclaimVirtualMemory](/windows/win32/api/memoryapi/nf-memoryapi-reclaimvirtualmemory) | Introduced into api-ms-win-core-memory-l1-1-2.dll in 10.0.10240. Moved into api-ms-win-core-memory-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-memory-l1-1-2.dll in 10.0.14393. |
| [ResetWriteWatch](/windows/win32/api/memoryapi/nf-memoryapi-resetwritewatch) | Introduced into api-ms-win-core-memory-l1-1-2.dll in 10.0.10240. Moved into api-ms-win-core-memory-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-memory-l1-1-2.dll in 10.0.14393. Moved into api-ms-win-core-memory-l1-1-1.dll in 10.0.16299. |
| [UnmapViewOfFile](/windows/win32/api/memoryapi/nf-memoryapi-unmapviewoffile) | Introduced into api-ms-win-core-memory-l1-1-2.dll in 10.0.10240. Moved into api-ms-win-core-memory-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-memory-l1-1-2.dll in 10.0.14393. Moved into api-ms-win-core-memory-l1-1-0.dll in 10.0.16299. |
| [VirtualFree](/windows/win32/api/memoryapi/nf-memoryapi-virtualfree) | Introduced into api-ms-win-core-memory-l1-1-2.dll in 10.0.10240. Moved into api-ms-win-core-memory-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-memory-l1-1-2.dll in 10.0.14393. Moved into api-ms-win-core-memory-l1-1-0.dll in 10.0.16299. |
| [VirtualQuery](/windows/win32/api/memoryapi/nf-memoryapi-virtualquery) | Introduced into api-ms-win-core-memory-l1-1-2.dll in 10.0.10240. Moved into api-ms-win-core-memory-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-memory-l1-1-2.dll in 10.0.14393. Moved into api-ms-win-core-memory-l1-1-0.dll in 10.0.16299. |
| [UnmapViewOfFileEx](/windows/win32/api/memoryapi/nf-memoryapi-unmapviewoffileex) | Introduced into api-ms-win-core-memory-l1-1-2.dll in 10.0.14393. Moved into api-ms-win-core-memory-l1-1-1.dll in 10.0.16299. |


## APIs from api-ms-win-core-memory-l1-1-3.dll

| API | Requirements |
| -----| --------------|
| [OpenFileMappingFromApp](/windows/win32/api/memoryapi/nf-memoryapi-openfilemappingfromapp) | Introduced into api-ms-win-core-memory-l1-1-3.dll in 10.0.10240. Moved into api-ms-win-core-memory-l1-1-4.dll in 10.0.14393. Moved into api-ms-win-core-memory-l1-1-3.dll in 10.0.16299. |
| [VirtualAllocFromApp](/windows/win32/api/memoryapi/nf-memoryapi-virtualallocfromapp) | Introduced into api-ms-win-core-memory-l1-1-3.dll in 10.0.10240. Moved into api-ms-win-core-memory-l1-1-4.dll in 10.0.14393. Moved into api-ms-win-core-memory-l1-1-3.dll in 10.0.16299. |
| [VirtualProtectFromApp](/windows/win32/api/memoryapi/nf-memoryapi-virtualprotectfromapp) | Introduced into api-ms-win-core-memory-l1-1-3.dll in 10.0.10240. Moved into api-ms-win-core-memory-l1-1-4.dll in 10.0.14393. Moved into api-ms-win-core-memory-l1-1-3.dll in 10.0.16299. |
| [SetProcessValidCallTargets](/windows/win32/api/memoryapi/nf-memoryapi-setprocessvalidcalltargets) | Introduced into api-ms-win-core-memory-l1-1-3.dll in 10.0.16299. |


## APIs from api-ms-win-core-normalization-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [GetStringScripts](/windows/win32/api/winnls/nf-winnls-getstringscripts) | Introduced into api-ms-win-core-normalization-l1-1-0.dll in 10.0.10240. |
| [IdnToNameprepUnicode](/windows/win32/api/winnls/nf-winnls-idntonameprepunicode) | Introduced into api-ms-win-core-normalization-l1-1-0.dll in 10.0.10240. |
| [IsNormalizedString](/windows/win32/api/winnls/nf-winnls-isnormalizedstring) | Introduced into api-ms-win-core-normalization-l1-1-0.dll in 10.0.10240. |
| [NormalizeString](/windows/win32/api/winnls/nf-winnls-normalizestring) | Introduced into api-ms-win-core-normalization-l1-1-0.dll in 10.0.10240. |
| [VerifyScripts](/windows/win32/api/winnls/nf-winnls-verifyscripts) | Introduced into api-ms-win-core-normalization-l1-1-0.dll in 10.0.10240. |


## APIs from api-ms-win-core-processenvironment-l1-2-0.dll

| API | Requirements |
| -----| --------------|
| [GetCommandLineA](/windows/win32/api/processenv/nf-processenv-getcommandlinea) | Introduced into api-ms-win-core-processenvironment-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-processenvironment-l1-1-0.dll in 10.0.16299. |
| [GetCommandLineW](/windows/win32/api/processenv/nf-processenv-getcommandlinea) | Introduced into api-ms-win-core-processenvironment-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-processenvironment-l1-1-0.dll in 10.0.16299. |
| [GetCurrentDirectoryW](/windows/win32/api/winbase/nf-winbase-getcurrentdirectory) | Introduced into api-ms-win-core-processenvironment-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-processenvironment-l1-1-0.dll in 10.0.16299. |
| [SetCurrentDirectoryW](/windows/win32/api/winbase/nf-winbase-setcurrentdirectory) | Introduced into api-ms-win-core-processenvironment-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-processenvironment-l1-1-0.dll in 10.0.16299. |


## APIs from api-ms-win-core-processthreads-l1-1-2.dll

| API | Requirements |
| -----| --------------|
| [CreateThread](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createthread) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.10240. Moved into api-ms-win-core-processthreads-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.14393. Moved into api-ms-win-core-processthreads-l1-1-0.dll in 10.0.16299. |
| [ExitThread](/windows/win32/api/processthreadsapi/nf-processthreadsapi-exitthread) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.10240. Moved into api-ms-win-core-processthreads-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.14393. Moved into api-ms-win-core-processthreads-l1-1-0.dll in 10.0.16299. |
| [FlushProcessWriteBuffers](/windows/win32/api/processthreadsapi/nf-processthreadsapi-flushprocesswritebuffers) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.10240. Moved into api-ms-win-core-processthreads-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.14393. Moved into api-ms-win-core-processthreads-l1-1-0.dll in 10.0.16299. |
| [GetCurrentProcess](/windows/win32/api/processthreadsapi/nf-processthreadsapi-getcurrentprocess) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.10240. Moved into api-ms-win-core-processthreads-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.14393. Moved into api-ms-win-core-processthreads-l1-1-0.dll in 10.0.16299. |
| [GetCurrentProcessId](/windows/win32/api/processthreadsapi/nf-processthreadsapi-getcurrentprocessid) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.10240. Moved into api-ms-win-core-processthreads-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.14393. Moved into api-ms-win-core-processthreads-l1-1-0.dll in 10.0.16299. |
| [GetCurrentThread](/windows/win32/api/processthreadsapi/nf-processthreadsapi-getcurrentthread) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.10240. Moved into api-ms-win-core-processthreads-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.14393. Moved into api-ms-win-core-processthreads-l1-1-0.dll in 10.0.16299. |
| [GetCurrentThreadId](/windows/win32/api/processthreadsapi/nf-processthreadsapi-getcurrentthreadid) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.10240. Moved into api-ms-win-core-processthreads-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.14393. Moved into api-ms-win-core-processthreads-l1-1-0.dll in 10.0.16299. |
| [GetExitCodeThread](/windows/win32/api/processthreadsapi/nf-processthreadsapi-getexitcodethread) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.10240. Moved into api-ms-win-core-processthreads-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.14393. Moved into api-ms-win-core-processthreads-l1-1-0.dll in 10.0.16299. |
| [GetThreadContext](/windows/win32/api/processthreadsapi/nf-processthreadsapi-getthreadcontext) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.10240. Moved into api-ms-win-core-processthreads-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.14393. Moved into api-ms-win-core-processthreads-l1-1-1.dll in 10.0.16299. |
| [GetThreadId](/windows/win32/api/processthreadsapi/nf-processthreadsapi-getthreadid) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.10240. Moved into api-ms-win-core-processthreads-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.14393. Moved into api-ms-win-core-processthreads-l1-1-0.dll in 10.0.16299. |
| [GetThreadPriority](/windows/win32/api/processthreadsapi/nf-processthreadsapi-getthreadpriority) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.10240. Moved into api-ms-win-core-processthreads-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.14393. Moved into api-ms-win-core-processthreads-l1-1-0.dll in 10.0.16299. |
| [IsProcessorFeaturePresent](/windows/win32/api/processthreadsapi/nf-processthreadsapi-isprocessorfeaturepresent) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.10240. Moved into api-ms-win-core-processthreads-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.14393. Moved into api-ms-win-core-processthreads-l1-1-1.dll in 10.0.16299. |
| [OpenProcess](/windows/win32/api/processthreadsapi/nf-processthreadsapi-openprocess) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.10240. Moved into api-ms-win-core-processthreads-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.14393. Moved into api-ms-win-core-processthreads-l1-1-1.dll in 10.0.16299. |
| [QueueUserAPC](/windows/win32/api/processthreadsapi/nf-processthreadsapi-queueuserapc) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.10240. Moved into api-ms-win-core-processthreads-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.14393. Moved into api-ms-win-core-processthreads-l1-1-0.dll in 10.0.16299. |
| [ResumeThread](/windows/win32/api/processthreadsapi/nf-processthreadsapi-resumethread) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.10240. Moved into api-ms-win-core-processthreads-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.14393. Moved into api-ms-win-core-processthreads-l1-1-0.dll in 10.0.16299. |
| [SetThreadIdealProcessorEx](/windows/win32/api/processthreadsapi/nf-processthreadsapi-setthreadidealprocessorex) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.10240. Moved into api-ms-win-core-processthreads-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.14393. Moved into api-ms-win-core-processthreads-l1-1-1.dll in 10.0.16299. |
| [SetThreadPriority](/windows/win32/api/processthreadsapi/nf-processthreadsapi-setthreadpriority) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.10240. Moved into api-ms-win-core-processthreads-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.14393. Moved into api-ms-win-core-processthreads-l1-1-0.dll in 10.0.16299. |
| [SuspendThread](/windows/win32/api/processthreadsapi/nf-processthreadsapi-suspendthread) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.10240. Moved into api-ms-win-core-processthreads-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.14393. Moved into api-ms-win-core-processthreads-l1-1-0.dll in 10.0.16299. |
| [SwitchToThread](/windows/win32/api/processthreadsapi/nf-processthreadsapi-switchtothread) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.10240. Moved into api-ms-win-core-processthreads-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.14393. Moved into api-ms-win-core-processthreads-l1-1-0.dll in 10.0.16299. |
| [TerminateProcess](/windows/win32/api/processthreadsapi/nf-processthreadsapi-terminateprocess) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.10240. Moved into api-ms-win-core-processthreads-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.14393. Moved into api-ms-win-core-processthreads-l1-1-0.dll in 10.0.16299. |
| [TlsAlloc](/windows/win32/api/processthreadsapi/nf-processthreadsapi-tlsalloc) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.14393. Moved into api-ms-win-core-processthreads-l1-1-0.dll in 10.0.16299. |
| [TlsFree](/windows/win32/api/processthreadsapi/nf-processthreadsapi-tlsfree) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.14393. Moved into api-ms-win-core-processthreads-l1-1-0.dll in 10.0.16299. |
| [TlsGetValue](/windows/win32/api/processthreadsapi/nf-processthreadsapi-tlsgetvalue) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.14393. Moved into api-ms-win-core-processthreads-l1-1-0.dll in 10.0.16299. |
| [TlsSetValue](/windows/win32/api/processthreadsapi/nf-processthreadsapi-tlssetvalue) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.14393. Moved into api-ms-win-core-processthreads-l1-1-0.dll in 10.0.16299. |
| [GetProcessPriorityBoost](/windows/win32/api/processthreadsapi/nf-processthreadsapi-getprocesspriorityboost) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.16299. |
| [SetProcessPriorityBoost](/windows/win32/api/processthreadsapi/nf-processthreadsapi-setprocesspriorityboost) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.16299. |
| [SetThreadInformation](/windows/win32/api/processthreadsapi/nf-processthreadsapi-setthreadinformation) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.17134. |
| [GetSystemTimes](/windows/win32/api/processthreadsapi/nf-processthreadsapi-getsystemtimes) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.17763. |


## APIs from api-ms-win-core-processthreads-l1-1-3.dll

| API | Requirements |
| -----| --------------|
| [GetProcessDefaultCpuSets](/windows/win32/procthread/getprocessdefaultcpusets) | Introduced into api-ms-win-core-processthreads-l1-1-3.dll in 10.0.10240. |
| [GetProcessInformation](/windows/win32/api/processthreadsapi/nf-processthreadsapi-getprocessinformation) | Introduced into api-ms-win-core-processthreads-l1-1-3.dll in 10.0.10240. |
| [GetSystemCpuSetInformation](/windows/win32/procthread/getsystemcpusetinformation) | Introduced into api-ms-win-core-processthreads-l1-1-3.dll in 10.0.10240. |
| [GetThreadSelectedCpuSets](/windows/win32/procthread/getthreadselectedcpusets) | Introduced into api-ms-win-core-processthreads-l1-1-3.dll in 10.0.10240. |
| [SetProcessDefaultCpuSets](/windows/win32/procthread/setprocessdefaultcpusets) | Introduced into api-ms-win-core-processthreads-l1-1-3.dll in 10.0.10240. |
| [SetProcessInformation](/windows/win32/api/processthreadsapi/nf-processthreadsapi-setprocessinformation) | Introduced into api-ms-win-core-processthreads-l1-1-3.dll in 10.0.10240. |
| [SetThreadIdealProcessor](/windows/win32/api/processthreadsapi/nf-processthreadsapi-setthreadidealprocessor) | Introduced into api-ms-win-core-processthreads-l1-1-3.dll in 10.0.10240. |
| [SetThreadSelectedCpuSets](/windows/win32/procthread/setthreadselectedcpusets) | Introduced into api-ms-win-core-processthreads-l1-1-3.dll in 10.0.10240. |
| [GetThreadDescription](/windows/win32/api/processthreadsapi/nf-processthreadsapi-getthreaddescription) | Introduced into api-ms-win-core-processthreads-l1-1-3.dll in 10.0.16299. |
| [SetThreadDescription](/windows/win32/api/processthreadsapi/nf-processthreadsapi-setthreaddescription) | Introduced into api-ms-win-core-processthreads-l1-1-3.dll in 10.0.16299. |


## APIs from api-ms-win-core-profile-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [QueryPerformanceCounter](/windows/win32/api/profileapi/nf-profileapi-queryperformancecounter) | Introduced into api-ms-win-core-profile-l1-1-0.dll in 10.0.10240. |
| [QueryPerformanceFrequency](/windows/win32/api/profileapi/nf-profileapi-queryperformancefrequency) | Introduced into api-ms-win-core-profile-l1-1-0.dll in 10.0.10240. |


## APIs from api-ms-win-core-realtime-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [QueryUnbiasedInterruptTime](/windows/win32/api/realtimeapiset/nf-realtimeapiset-queryunbiasedinterrupttime) | Introduced into api-ms-win-core-realtime-l1-1-0.dll in 10.0.10240. Moved into api-ms-win-core-realtime-l1-1-1.dll in 10.0.10586. Moved into api-ms-win-core-realtime-l1-1-0.dll in 10.0.14393. |


## APIs from api-ms-win-core-realtime-l1-1-1.dll

| API | Requirements |
| -----| --------------|
| [QueryInterruptTime](/windows/win32/api/realtimeapiset/nf-realtimeapiset-queryinterrupttime) | Introduced into api-ms-win-core-realtime-l1-1-1.dll in 10.0.10240. |
| [QueryInterruptTimePrecise](/windows/win32/api/realtimeapiset/nf-realtimeapiset-queryinterrupttimeprecise) | Introduced into api-ms-win-core-realtime-l1-1-1.dll in 10.0.10240. |
| [QueryUnbiasedInterruptTimePrecise](/windows/win32/api/realtimeapiset/nf-realtimeapiset-queryunbiasedinterrupttimeprecise) | Introduced into api-ms-win-core-realtime-l1-1-1.dll in 10.0.10240. |


## APIs from api-ms-win-core-rtlsupport-l1-2-0.dll

| API | Requirements |
| -----| --------------|
| [RtlCaptureStackBackTrace](/previous-versions//aa813366(v=vs.85)) | Introduced into api-ms-win-core-rtlsupport-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-rtlsupport-l1-1-0.dll in 10.0.16299. |
| [RtlLookupFunctionEntry](/windows/win32/api/winnt/nf-winnt-rtllookupfunctionentry) | Introduced into api-ms-win-core-rtlsupport-l1-2-0.dll in 10.0.10240. Removed in 10.0.16299. |
| [RtlPcToFileHeader](/windows/win32/api/winnt/nf-winnt-rtlpctofileheader) | Introduced into api-ms-win-core-rtlsupport-l1-2-0.dll in 10.0.10240. |
| [RtlUnwind](/windows/win32/api/winnt/nf-winnt-rtlunwind) | Introduced into api-ms-win-core-rtlsupport-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-rtlsupport-l1-1-0.dll in 10.0.16299. |
| [RtlUnwindEx](/windows/win32/api/winnt/nf-winnt-rtlunwindex) | Introduced into api-ms-win-core-rtlsupport-l1-2-0.dll in 10.0.10240. Removed in 10.0.16299. |


## APIs from api-ms-win-core-string-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [CompareStringEx](/windows/win32/api/stringapiset/nf-stringapiset-comparestringex) | Introduced into api-ms-win-core-string-l1-1-0.dll in 10.0.10240. |
| [CompareStringOrdinal](/windows/win32/api/stringapiset/nf-stringapiset-comparestringordinal) | Introduced into api-ms-win-core-string-l1-1-0.dll in 10.0.10240. |
| [GetStringTypeExW](/windows/win32/api/stringapiset/nf-stringapiset-getstringtypeexw) | Introduced into api-ms-win-core-string-l1-1-0.dll in 10.0.10240. |
| [GetStringTypeW](/windows/win32/api/stringapiset/nf-stringapiset-getstringtypew) | Introduced into api-ms-win-core-string-l1-1-0.dll in 10.0.10240. |
| [MultiByteToWideChar](/windows/win32/api/stringapiset/nf-stringapiset-multibytetowidechar) | Introduced into api-ms-win-core-string-l1-1-0.dll in 10.0.10240. |
| [WideCharToMultiByte](/windows/win32/api/stringapiset/nf-stringapiset-widechartomultibyte) | Introduced into api-ms-win-core-string-l1-1-0.dll in 10.0.10240. |


## APIs from api-ms-win-core-synch-ansi-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [CreateSemaphoreA](/windows/win32/api/synchapi/nf-synchapi-createsemaphorew) | Introduced into api-ms-win-core-synch-ansi-l1-1-0.dll in 10.0.10240. |
| [CreateSemaphoreExA](/windows/win32/api/synchapi/nf-synchapi-createsemaphoreexw) | Introduced into api-ms-win-core-synch-ansi-l1-1-0.dll in 10.0.10240. |
| [OpenMutexA](/windows/win32/api/synchapi/nf-synchapi-openmutexw) | Introduced into api-ms-win-core-synch-ansi-l1-1-0.dll in 10.0.10240. |
| [CreateWaitableTimerA](/windows/win32/api/synchapi/nf-synchapi-createwaitabletimerw) | Introduced into api-ms-win-core-synch-ansi-l1-1-0.dll in 10.0.16299. |
| [CreateWaitableTimerExA](/windows/win32/api/synchapi/nf-synchapi-createwaitabletimerexw) | Introduced into api-ms-win-core-synch-ansi-l1-1-0.dll in 10.0.16299. |
| [OpenWaitableTimerA](/windows/win32/api/synchapi/nf-synchapi-openwaitabletimerw) | Introduced into api-ms-win-core-synch-ansi-l1-1-0.dll in 10.0.16299. |


## APIs from api-ms-win-core-synch-l1-2-0.dll

| API | Requirements |
| -----| --------------|
| [AcquireSRWLockExclusive](/windows/win32/api/synchapi/nf-synchapi-acquiresrwlockexclusive) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. Moved into api-ms-win-core-synch-l1-1-0.dll in 10.0.16299. |
| [AcquireSRWLockShared](/windows/win32/api/synchapi/nf-synchapi-acquiresrwlockshared) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. Moved into api-ms-win-core-synch-l1-1-0.dll in 10.0.16299. |
| [CreateEventA](/windows/win32/api/synchapi/nf-synchapi-createeventa) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. Moved into api-ms-win-core-synch-l1-1-0.dll in 10.0.16299. |
| [CreateEventExA](/windows/win32/api/synchapi/nf-synchapi-createeventexa) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. Moved into api-ms-win-core-synch-l1-1-0.dll in 10.0.16299. |
| [CreateEventExW](/windows/win32/api/synchapi/nf-synchapi-createeventexa) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. Moved into api-ms-win-core-synch-l1-1-0.dll in 10.0.16299. |
| [CreateEventW](/windows/win32/api/synchapi/nf-synchapi-createeventa) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. Moved into api-ms-win-core-synch-l1-1-0.dll in 10.0.16299. |
| [CreateMutexA](/windows/win32/api/synchapi/nf-synchapi-createmutexa) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. Moved into api-ms-win-core-synch-l1-1-0.dll in 10.0.16299. |
| [CreateMutexExA](/windows/win32/api/synchapi/nf-synchapi-createmutexexa) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. Moved into api-ms-win-core-synch-l1-1-0.dll in 10.0.16299. |
| [CreateMutexExW](/windows/win32/api/synchapi/nf-synchapi-createmutexexa) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. Moved into api-ms-win-core-synch-l1-1-0.dll in 10.0.16299. |
| [CreateMutexW](/windows/win32/api/synchapi/nf-synchapi-createmutexa) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. Moved into api-ms-win-core-synch-l1-1-0.dll in 10.0.16299. |
| [CreateSemaphoreExW](/windows/win32/api/synchapi/nf-synchapi-createsemaphoreexw) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. Moved into api-ms-win-core-synch-l1-1-0.dll in 10.0.16299. |
| [DeleteCriticalSection](/windows/win32/api/synchapi/nf-synchapi-deletecriticalsection) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. Moved into api-ms-win-core-synch-l1-1-0.dll in 10.0.16299. |
| [EnterCriticalSection](/windows/win32/api/synchapi/nf-synchapi-entercriticalsection) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. Moved into api-ms-win-core-synch-l1-1-0.dll in 10.0.16299. |
| [InitializeConditionVariable](/windows/win32/api/synchapi/nf-synchapi-initializeconditionvariable) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. |
| [InitializeCriticalSection](/windows/win32/api/synchapi/nf-synchapi-initializecriticalsection) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. Moved into api-ms-win-core-synch-l1-1-0.dll in 10.0.16299. |
| [InitializeCriticalSectionAndSpinCount](/windows/win32/api/synchapi/nf-synchapi-initializecriticalsectionandspincount) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. Moved into api-ms-win-core-synch-l1-1-0.dll in 10.0.16299. |
| [InitializeCriticalSectionEx](/windows/win32/api/synchapi/nf-synchapi-initializecriticalsectionex) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. Moved into api-ms-win-core-synch-l1-1-0.dll in 10.0.16299. |
| [InitializeSRWLock](/windows/win32/api/synchapi/nf-synchapi-initializesrwlock) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. Moved into api-ms-win-core-synch-l1-1-0.dll in 10.0.16299. |
| [InitOnceBeginInitialize](/windows/win32/api/synchapi/nf-synchapi-initoncebegininitialize) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. |
| [InitOnceComplete](/windows/win32/api/synchapi/nf-synchapi-initoncecomplete) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. |
| [InitOnceExecuteOnce](/windows/win32/api/synchapi/nf-synchapi-initonceexecuteonce) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. |
| [InitOnceInitialize](/windows/win32/api/synchapi/nf-synchapi-initonceinitialize) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. |
| [LeaveCriticalSection](/windows/win32/api/synchapi/nf-synchapi-leavecriticalsection) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. Moved into api-ms-win-core-synch-l1-1-0.dll in 10.0.16299. |
| [OpenEventA](/windows/win32/api/synchapi/nf-synchapi-openeventa) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. Moved into api-ms-win-core-synch-l1-1-0.dll in 10.0.16299. |
| [OpenEventW](/windows/win32/api/synchapi/nf-synchapi-openeventa) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. Moved into api-ms-win-core-synch-l1-1-0.dll in 10.0.16299. |
| [OpenMutexW](/windows/win32/api/synchapi/nf-synchapi-openmutexw) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. Moved into api-ms-win-core-synch-l1-1-0.dll in 10.0.16299. |
| [OpenSemaphoreW](/windows/win32/api/synchapi/nf-synchapi-opensemaphorew) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. Moved into api-ms-win-core-synch-l1-1-0.dll in 10.0.16299. |
| [ReleaseMutex](/windows/win32/api/synchapi/nf-synchapi-releasemutex) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. Moved into api-ms-win-core-synch-l1-1-0.dll in 10.0.16299. |
| [ReleaseSemaphore](/windows/win32/api/synchapi/nf-synchapi-releasesemaphore) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. Moved into api-ms-win-core-synch-l1-1-0.dll in 10.0.16299. |
| [ReleaseSRWLockExclusive](/windows/win32/api/synchapi/nf-synchapi-releasesrwlockexclusive) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. Moved into api-ms-win-core-synch-l1-1-0.dll in 10.0.16299. |
| [ReleaseSRWLockShared](/windows/win32/api/synchapi/nf-synchapi-releasesrwlockshared) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. Moved into api-ms-win-core-synch-l1-1-0.dll in 10.0.16299. |
| [ResetEvent](/windows/win32/api/synchapi/nf-synchapi-resetevent) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. Moved into api-ms-win-core-synch-l1-1-0.dll in 10.0.16299. |
| [SetCriticalSectionSpinCount](/windows/win32/api/synchapi/nf-synchapi-setcriticalsectionspincount) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. Moved into api-ms-win-core-synch-l1-1-0.dll in 10.0.16299. |
| [SetEvent](/windows/win32/api/synchapi/nf-synchapi-setevent) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. Moved into api-ms-win-core-synch-l1-1-0.dll in 10.0.16299. |
| [Sleep](/windows/win32/api/synchapi/nf-synchapi-sleep) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. |
| [SleepConditionVariableCS](/windows/win32/api/synchapi/nf-synchapi-sleepconditionvariablecs) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. |
| [SleepConditionVariableSRW](/windows/win32/api/synchapi/nf-synchapi-sleepconditionvariablesrw) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. |
| [SleepEx](/windows/win32/api/synchapi/nf-synchapi-sleepex) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. Moved into api-ms-win-core-synch-l1-1-0.dll in 10.0.16299. |
| [TryAcquireSRWLockExclusive](/windows/win32/api/synchapi/nf-synchapi-tryacquiresrwlockexclusive) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. Moved into api-ms-win-core-synch-l1-1-0.dll in 10.0.16299. |
| [TryAcquireSRWLockShared](/windows/win32/api/synchapi/nf-synchapi-tryacquiresrwlockshared) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. Moved into api-ms-win-core-synch-l1-1-0.dll in 10.0.16299. |
| [TryEnterCriticalSection](/windows/win32/api/synchapi/nf-synchapi-tryentercriticalsection) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. Moved into api-ms-win-core-synch-l1-1-0.dll in 10.0.16299. |
| [WaitForMultipleObjectsEx](/windows/win32/api/synchapi/nf-synchapi-waitformultipleobjectsex) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. Moved into api-ms-win-core-synch-l1-1-0.dll in 10.0.16299. |
| [WaitForSingleObject](/windows/win32/api/synchapi/nf-synchapi-waitforsingleobject) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. Moved into api-ms-win-core-synch-l1-1-0.dll in 10.0.16299. |
| [WaitForSingleObjectEx](/windows/win32/api/synchapi/nf-synchapi-waitforsingleobjectex) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. Moved into api-ms-win-core-synch-l1-1-0.dll in 10.0.16299. |
| [WaitOnAddress](/windows/win32/api/synchapi/nf-synchapi-waitonaddress) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. |
| [WakeAllConditionVariable](/windows/win32/api/synchapi/nf-synchapi-wakeallconditionvariable) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. |
| [WakeByAddressAll](/windows/win32/api/synchapi/nf-synchapi-wakebyaddressall) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. |
| [WakeByAddressSingle](/windows/win32/api/synchapi/nf-synchapi-wakebyaddresssingle) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. |
| [WakeConditionVariable](/windows/win32/api/synchapi/nf-synchapi-wakeconditionvariable) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. |
| [SignalObjectAndWait](/windows/win32/api/synchapi/nf-synchapi-signalobjectandwait) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.16299. |


## APIs from api-ms-win-core-synch-l1-2-1.dll

| API | Requirements |
| -----| --------------|
| [CreateSemaphoreW](/windows/win32/api/synchapi/nf-synchapi-createsemaphorew) | Introduced into api-ms-win-core-synch-l1-2-1.dll in 10.0.10240. |
| [WaitForMultipleObjects](/windows/win32/api/synchapi/nf-synchapi-waitformultipleobjects) | Introduced into api-ms-win-core-synch-l1-2-1.dll in 10.0.10240. |
| [CreateWaitableTimerW](/windows/win32/api/synchapi/nf-synchapi-createwaitabletimerw) | Introduced into api-ms-win-core-synch-l1-2-1.dll in 10.0.16299. |


## APIs from api-ms-win-core-sysinfo-l1-2-1.dll

| API | Requirements |
| -----| --------------|
| [GetLocalTime](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getlocaltime) | Introduced into api-ms-win-core-sysinfo-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-sysinfo-l1-2-3.dll in 10.0.10586. Moved into api-ms-win-core-sysinfo-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-sysinfo-l1-1-0.dll in 10.0.16299. |
| [GetNativeSystemInfo](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getnativesysteminfo) | Introduced into api-ms-win-core-sysinfo-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-sysinfo-l1-2-3.dll in 10.0.10586. Moved into api-ms-win-core-sysinfo-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-sysinfo-l1-2-0.dll in 10.0.16299. |
| [GetSystemInfo](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getsysteminfo) | Introduced into api-ms-win-core-sysinfo-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-sysinfo-l1-2-3.dll in 10.0.10586. Moved into api-ms-win-core-sysinfo-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-sysinfo-l1-1-0.dll in 10.0.16299. |
| [GetSystemTime](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getsystemtime) | Introduced into api-ms-win-core-sysinfo-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-sysinfo-l1-2-3.dll in 10.0.10586. Moved into api-ms-win-core-sysinfo-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-sysinfo-l1-1-0.dll in 10.0.16299. |
| [GetSystemTimeAsFileTime](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getsystemtimeasfiletime) | Introduced into api-ms-win-core-sysinfo-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-sysinfo-l1-2-3.dll in 10.0.10586. Moved into api-ms-win-core-sysinfo-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-sysinfo-l1-1-0.dll in 10.0.16299. |
| [GetSystemTimePreciseAsFileTime](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getsystemtimepreciseasfiletime) | Introduced into api-ms-win-core-sysinfo-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-sysinfo-l1-2-3.dll in 10.0.10586. Moved into api-ms-win-core-sysinfo-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-sysinfo-l1-2-0.dll in 10.0.16299. |
| [GetTickCount64](/windows/win32/api/sysinfoapi/nf-sysinfoapi-gettickcount64) | Introduced into api-ms-win-core-sysinfo-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-sysinfo-l1-2-3.dll in 10.0.10586. Moved into api-ms-win-core-sysinfo-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-sysinfo-l1-1-0.dll in 10.0.16299. |
| [GetLogicalProcessorInformation](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getlogicalprocessorinformation) | Introduced into api-ms-win-core-sysinfo-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-sysinfo-l1-1-0.dll in 10.0.16299. |
| [GetLogicalProcessorInformationEx](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getlogicalprocessorinformationex) | Introduced into api-ms-win-core-sysinfo-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-sysinfo-l1-1-0.dll in 10.0.16299. |
| [GlobalMemoryStatusEx](/windows/win32/api/sysinfoapi/nf-sysinfoapi-globalmemorystatusex) | Introduced into api-ms-win-core-sysinfo-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-sysinfo-l1-1-0.dll in 10.0.16299. |


## APIs from api-ms-win-core-sysinfo-l1-2-3.dll

| API | Requirements |
| -----| --------------|
| [GetIntegratedDisplaySize](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getintegrateddisplaysize) | Introduced into api-ms-win-core-sysinfo-l1-2-3.dll in 10.0.10240. |


## APIs from api-ms-win-core-threadpool-l1-2-0.dll

| API | Requirements |
| -----| --------------|
| [CallbackMayRunLong](/windows/win32/api/threadpoolapiset/nf-threadpoolapiset-callbackmayrunlong) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [CancelThreadpoolIo](/windows/win32/api/threadpoolapiset/nf-threadpoolapiset-cancelthreadpoolio) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [CloseThreadpool](/windows/win32/api/threadpoolapiset/nf-threadpoolapiset-closethreadpool) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [CloseThreadpoolCleanupGroup](/windows/win32/api/threadpoolapiset/nf-threadpoolapiset-closethreadpoolcleanupgroup) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [CloseThreadpoolCleanupGroupMembers](/windows/win32/api/threadpoolapiset/nf-threadpoolapiset-closethreadpoolcleanupgroupmembers) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [CloseThreadpoolIo](/windows/win32/api/threadpoolapiset/nf-threadpoolapiset-closethreadpoolio) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [CloseThreadpoolTimer](/windows/win32/api/threadpoolapiset/nf-threadpoolapiset-closethreadpooltimer) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [CloseThreadpoolWait](/windows/win32/api/threadpoolapiset/nf-threadpoolapiset-closethreadpoolwait) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [CloseThreadpoolWork](/windows/win32/api/threadpoolapiset/nf-threadpoolapiset-closethreadpoolwork) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [CreateThreadpool](/windows/win32/api/threadpoolapiset/nf-threadpoolapiset-createthreadpool) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [CreateThreadpoolCleanupGroup](/windows/win32/api/threadpoolapiset/nf-threadpoolapiset-createthreadpoolcleanupgroup) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [CreateThreadpoolIo](/windows/win32/api/threadpoolapiset/nf-threadpoolapiset-createthreadpoolio) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [CreateThreadpoolTimer](/windows/win32/api/threadpoolapiset/nf-threadpoolapiset-createthreadpooltimer) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [CreateThreadpoolWait](/windows/win32/api/threadpoolapiset/nf-threadpoolapiset-createthreadpoolwait) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [CreateThreadpoolWork](/windows/win32/api/threadpoolapiset/nf-threadpoolapiset-createthreadpoolwork) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [DisassociateCurrentThreadFromCallback](/windows/win32/api/threadpoolapiset/nf-threadpoolapiset-disassociatecurrentthreadfromcallback) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [FreeLibraryWhenCallbackReturns](/windows/win32/api/threadpoolapiset/nf-threadpoolapiset-freelibrarywhencallbackreturns) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [IsThreadpoolTimerSet](/windows/win32/api/threadpoolapiset/nf-threadpoolapiset-isthreadpooltimerset) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [LeaveCriticalSectionWhenCallbackReturns](/windows/win32/api/threadpoolapiset/nf-threadpoolapiset-leavecriticalsectionwhencallbackreturns) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [QueryThreadpoolStackInformation](/windows/win32/api/threadpoolapiset/nf-threadpoolapiset-querythreadpoolstackinformation) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [ReleaseMutexWhenCallbackReturns](/windows/win32/api/threadpoolapiset/nf-threadpoolapiset-releasemutexwhencallbackreturns) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [ReleaseSemaphoreWhenCallbackReturns](/windows/win32/api/threadpoolapiset/nf-threadpoolapiset-releasesemaphorewhencallbackreturns) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [SetEventWhenCallbackReturns](/windows/win32/api/threadpoolapiset/nf-threadpoolapiset-seteventwhencallbackreturns) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [SetThreadpoolStackInformation](/windows/win32/api/threadpoolapiset/nf-threadpoolapiset-setthreadpoolstackinformation) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [SetThreadpoolThreadMaximum](/windows/win32/api/threadpoolapiset/nf-threadpoolapiset-setthreadpoolthreadmaximum) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [SetThreadpoolThreadMinimum](/windows/win32/api/threadpoolapiset/nf-threadpoolapiset-setthreadpoolthreadminimum) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [SetThreadpoolTimer](/windows/win32/api/threadpoolapiset/nf-threadpoolapiset-setthreadpooltimer) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [SetThreadpoolTimerEx](/windows/win32/api/threadpoolapiset/nf-threadpoolapiset-setthreadpooltimerex) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [SetThreadpoolWait](/windows/win32/api/threadpoolapiset/nf-threadpoolapiset-setthreadpoolwait) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [SetThreadpoolWaitEx](/windows/win32/api/threadpoolapiset/nf-threadpoolapiset-setthreadpoolwaitex) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [StartThreadpoolIo](/windows/win32/api/threadpoolapiset/nf-threadpoolapiset-startthreadpoolio) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [SubmitThreadpoolWork](/windows/win32/api/threadpoolapiset/nf-threadpoolapiset-submitthreadpoolwork) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [TrySubmitThreadpoolCallback](/windows/win32/api/threadpoolapiset/nf-threadpoolapiset-trysubmitthreadpoolcallback) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [WaitForThreadpoolIoCallbacks](/windows/win32/api/threadpoolapiset/nf-threadpoolapiset-waitforthreadpooliocallbacks) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [WaitForThreadpoolTimerCallbacks](/windows/win32/api/threadpoolapiset/nf-threadpoolapiset-waitforthreadpooltimercallbacks) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [WaitForThreadpoolWaitCallbacks](/windows/win32/api/threadpoolapiset/nf-threadpoolapiset-waitforthreadpoolwaitcallbacks) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [WaitForThreadpoolWorkCallbacks](/windows/win32/api/threadpoolapiset/nf-threadpoolapiset-waitforthreadpoolworkcallbacks) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |


## APIs from api-ms-win-core-timezone-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [EnumDynamicTimeZoneInformation](/windows/win32/api/timezoneapi/nf-timezoneapi-enumdynamictimezoneinformation) | Introduced into api-ms-win-core-timezone-l1-1-0.dll in 10.0.10240. |
| [FileTimeToSystemTime](/windows/win32/api/timezoneapi/nf-timezoneapi-filetimetosystemtime) | Introduced into api-ms-win-core-timezone-l1-1-0.dll in 10.0.10240. |
| [GetDynamicTimeZoneInformation](/windows/win32/api/timezoneapi/nf-timezoneapi-getdynamictimezoneinformation) | Introduced into api-ms-win-core-timezone-l1-1-0.dll in 10.0.10240. |
| [GetDynamicTimeZoneInformationEffectiveYears](/windows/win32/api/timezoneapi/nf-timezoneapi-getdynamictimezoneinformationeffectiveyears) | Introduced into api-ms-win-core-timezone-l1-1-0.dll in 10.0.10240. |
| [GetTimeZoneInformation](/windows/win32/api/timezoneapi/nf-timezoneapi-gettimezoneinformation) | Introduced into api-ms-win-core-timezone-l1-1-0.dll in 10.0.10240. |
| [GetTimeZoneInformationForYear](/windows/win32/api/timezoneapi/nf-timezoneapi-gettimezoneinformationforyear) | Introduced into api-ms-win-core-timezone-l1-1-0.dll in 10.0.10240. |
| [SystemTimeToFileTime](/windows/win32/api/timezoneapi/nf-timezoneapi-systemtimetofiletime) | Introduced into api-ms-win-core-timezone-l1-1-0.dll in 10.0.10240. |
| [SystemTimeToTzSpecificLocalTime](/windows/win32/api/timezoneapi/nf-timezoneapi-systemtimetotzspecificlocaltime) | Introduced into api-ms-win-core-timezone-l1-1-0.dll in 10.0.10240. |
| [SystemTimeToTzSpecificLocalTimeEx](/windows/win32/api/timezoneapi/nf-timezoneapi-systemtimetotzspecificlocaltimeex) | Introduced into api-ms-win-core-timezone-l1-1-0.dll in 10.0.10240. |
| [TzSpecificLocalTimeToSystemTime](/windows/win32/api/timezoneapi/nf-timezoneapi-tzspecificlocaltimetosystemtime) | Introduced into api-ms-win-core-timezone-l1-1-0.dll in 10.0.10240. |
| [TzSpecificLocalTimeToSystemTimeEx](/windows/win32/api/timezoneapi/nf-timezoneapi-tzspecificlocaltimetosystemtimeex) | Introduced into api-ms-win-core-timezone-l1-1-0.dll in 10.0.10240. |


## APIs from api-ms-win-core-util-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [DecodePointer](/previous-versions//bb432242(v=vs.85)) | Introduced into api-ms-win-core-util-l1-1-0.dll in 10.0.10240. Moved into api-ms-win-core-util-l1-1-1.dll in 10.0.10586. Moved into api-ms-win-core-util-l1-1-0.dll in 10.0.14393. |
| [EncodePointer](/previous-versions//bb432254(v=vs.85)) | Introduced into api-ms-win-core-util-l1-1-0.dll in 10.0.10240. Moved into api-ms-win-core-util-l1-1-1.dll in 10.0.10586. Moved into api-ms-win-core-util-l1-1-0.dll in 10.0.14393. |
| [Beep](/windows/win32/api/utilapiset/nf-utilapiset-beep) | Introduced into api-ms-win-core-util-l1-1-0.dll in 10.0.16299. |


## APIs from api-ms-win-core-windowsceip-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [CeipIsOptedIn](/windows/win32/api/windowsceip/nf-windowsceip-ceipisoptedin) | Introduced into api-ms-win-core-windowsceip-l1-1-0.dll in 10.0.10240. |


## APIs from api-ms-win-core-windowserrorreporting-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [WerRegisterFile](/windows/win32/api/werapi/nf-werapi-werregisterfile) | Introduced into api-ms-win-core-windowserrorreporting-l1-1-0.dll in 10.0.10240. |
| [WerRegisterMemoryBlock](/windows/win32/api/werapi/nf-werapi-werregistermemoryblock) | Introduced into api-ms-win-core-windowserrorreporting-l1-1-0.dll in 10.0.10240. |
| [WerUnregisterFile](/windows/win32/api/werapi/nf-werapi-werunregisterfile) | Introduced into api-ms-win-core-windowserrorreporting-l1-1-0.dll in 10.0.10240. |
| [WerUnregisterMemoryBlock](/windows/win32/api/werapi/nf-werapi-werunregistermemoryblock) | Introduced into api-ms-win-core-windowserrorreporting-l1-1-0.dll in 10.0.10240. |


## APIs from api-ms-win-core-winrt-error-l1-1-1.dll

| API | Requirements |
| -----| --------------|
| [GetRestrictedErrorInfo](/windows/win32/api/roerrorapi/nf-roerrorapi-getrestrictederrorinfo) | Introduced into api-ms-win-core-winrt-error-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-winrt-error-l1-1-0.dll in 10.0.16299. |
| [RoCaptureErrorContext](/windows/win32/api/roerrorapi/nf-roerrorapi-rocaptureerrorcontext) | Introduced into api-ms-win-core-winrt-error-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-winrt-error-l1-1-0.dll in 10.0.16299. |
| [RoFailFastWithErrorContext](/windows/win32/api/roerrorapi/nf-roerrorapi-rofailfastwitherrorcontext) | Introduced into api-ms-win-core-winrt-error-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-winrt-error-l1-1-0.dll in 10.0.16299. |
| [RoGetErrorReportingFlags](/windows/win32/api/roerrorapi/nf-roerrorapi-rogeterrorreportingflags) | Introduced into api-ms-win-core-winrt-error-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-winrt-error-l1-1-0.dll in 10.0.16299. |
| [RoOriginateError](/windows/win32/api/roerrorapi/nf-roerrorapi-rooriginateerror) | Introduced into api-ms-win-core-winrt-error-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-winrt-error-l1-1-0.dll in 10.0.16299. |
| [RoOriginateErrorW](/windows/win32/api/roerrorapi/nf-roerrorapi-rooriginateerrorw) | Introduced into api-ms-win-core-winrt-error-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-winrt-error-l1-1-0.dll in 10.0.16299. |
| [RoOriginateLanguageException](/windows/win32/api/roerrorapi/nf-roerrorapi-rooriginatelanguageexception) | Introduced into api-ms-win-core-winrt-error-l1-1-1.dll in 10.0.10240. |
| [RoReportUnhandledError](/windows/win32/api/roerrorapi/nf-roerrorapi-roreportunhandlederror) | Introduced into api-ms-win-core-winrt-error-l1-1-1.dll in 10.0.10240. |
| [RoSetErrorReportingFlags](/windows/win32/api/roerrorapi/nf-roerrorapi-roseterrorreportingflags) | Introduced into api-ms-win-core-winrt-error-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-winrt-error-l1-1-0.dll in 10.0.16299. |
| [RoTransformError](/windows/win32/api/roerrorapi/nf-roerrorapi-rotransformerror) | Introduced into api-ms-win-core-winrt-error-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-winrt-error-l1-1-0.dll in 10.0.16299. |
| [RoTransformErrorW](/windows/win32/api/roerrorapi/nf-roerrorapi-rotransformerrorw) | Introduced into api-ms-win-core-winrt-error-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-winrt-error-l1-1-0.dll in 10.0.16299. |
| [SetRestrictedErrorInfo](/windows/win32/api/roerrorapi/nf-roerrorapi-setrestrictederrorinfo) | Introduced into api-ms-win-core-winrt-error-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-winrt-error-l1-1-0.dll in 10.0.16299. |


## APIs from api-ms-win-core-winrt-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [RoActivateInstance](/windows/win32/api/roapi/nf-roapi-roactivateinstance) | Introduced into api-ms-win-core-winrt-l1-1-0.dll in 10.0.10240. |
| [RoGetActivationFactory](/windows/win32/api/roapi/nf-roapi-rogetactivationfactory) | Introduced into api-ms-win-core-winrt-l1-1-0.dll in 10.0.10240. |
| [RoGetApartmentIdentifier](/windows/win32/api/roapi/nf-roapi-rogetapartmentidentifier) | Introduced into api-ms-win-core-winrt-l1-1-0.dll in 10.0.10240. |
| [RoInitialize](/windows/win32/api/roapi/nf-roapi-roinitialize) | Introduced into api-ms-win-core-winrt-l1-1-0.dll in 10.0.10240. |
| [RoRegisterActivationFactories](/windows/win32/api/roapi/nf-roapi-roregisteractivationfactories) | Introduced into api-ms-win-core-winrt-l1-1-0.dll in 10.0.10240. |
| [RoRegisterForApartmentShutdown](/windows/win32/api/roapi/nf-roapi-roregisterforapartmentshutdown) | Introduced into api-ms-win-core-winrt-l1-1-0.dll in 10.0.10240. |
| [RoRevokeActivationFactories](/windows/win32/api/roapi/nf-roapi-rorevokeactivationfactories) | Introduced into api-ms-win-core-winrt-l1-1-0.dll in 10.0.10240. |
| [RoUninitialize](/windows/win32/api/roapi/nf-roapi-rouninitialize) | Introduced into api-ms-win-core-winrt-l1-1-0.dll in 10.0.10240. |
| [RoUnregisterForApartmentShutdown](/windows/win32/api/roapi/nf-roapi-rounregisterforapartmentshutdown) | Introduced into api-ms-win-core-winrt-l1-1-0.dll in 10.0.10240. |


## APIs from api-ms-win-core-winrt-registration-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [RoGetActivatableClassRegistration](/windows/win32/api/roregistrationapi/nf-roregistrationapi-rogetactivatableclassregistration) | Introduced into api-ms-win-core-winrt-registration-l1-1-0.dll in 10.0.10240. |
| [RoGetServerActivatableClasses](/windows/win32/api/roregistrationapi/nf-roregistrationapi-rogetserveractivatableclasses) | Introduced into api-ms-win-core-winrt-registration-l1-1-0.dll in 10.0.10240. |


## APIs from api-ms-win-core-winrt-robuffer-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [RoGetBufferMarshaler](/windows/win32/api/robuffer/nf-robuffer-rogetbuffermarshaler) | Introduced into api-ms-win-core-winrt-robuffer-l1-1-0.dll in 10.0.10240. |


## APIs from api-ms-win-core-winrt-roparameterizediid-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [RoFreeParameterizedTypeExtra](/windows/win32/api/roparameterizediid/nf-roparameterizediid-rofreeparameterizedtypeextra) | Introduced into api-ms-win-core-winrt-roparameterizediid-l1-1-0.dll in 10.0.10240. |
| [RoGetParameterizedTypeInstanceIID](/windows/win32/api/roparameterizediid/nf-roparameterizediid-rogetparameterizedtypeinstanceiid) | Introduced into api-ms-win-core-winrt-roparameterizediid-l1-1-0.dll in 10.0.10240. |
| [RoParameterizedTypeExtraGetTypeSignature](/windows/win32/api/roparameterizediid/nf-roparameterizediid-roparameterizedtypeextragettypesignature) | Introduced into api-ms-win-core-winrt-roparameterizediid-l1-1-0.dll in 10.0.10240. |


## APIs from api-ms-win-core-winrt-string-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [HSTRING_UserFree](/windows/win32/api/inspectable/nf-inspectable-hstring_userfree) | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.10240. Moved into api-ms-win-core-winrt-string-l1-1-1.dll in 10.0.10586. Moved into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.14393. |
| [HSTRING_UserFree64](/windows/win32/api/inspectable/nf-inspectable-hstring_userfree64) | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.10240. Moved into api-ms-win-core-winrt-string-l1-1-1.dll in 10.0.10586. Moved into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.14393. Removed in 10.0.16299. |
| [HSTRING_UserMarshal](/windows/win32/api/inspectable/nf-inspectable-hstring_usermarshal) | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.10240. Moved into api-ms-win-core-winrt-string-l1-1-1.dll in 10.0.10586. Moved into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.14393. |
| [HSTRING_UserMarshal64](/windows/win32/api/inspectable/nf-inspectable-hstring_usermarshal64) | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.10240. Moved into api-ms-win-core-winrt-string-l1-1-1.dll in 10.0.10586. Moved into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.14393. Removed in 10.0.16299. |
| [HSTRING_UserSize](/windows/win32/api/inspectable/nf-inspectable-hstring_usersize) | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.10240. Moved into api-ms-win-core-winrt-string-l1-1-1.dll in 10.0.10586. Moved into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.14393. |
| [HSTRING_UserSize64](/windows/win32/api/inspectable/nf-inspectable-hstring_usersize64) | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.10240. Moved into api-ms-win-core-winrt-string-l1-1-1.dll in 10.0.10586. Moved into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.14393. Removed in 10.0.16299. |
| [HSTRING_UserUnmarshal](/windows/win32/api/inspectable/nf-inspectable-hstring_userunmarshal) | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.10240. Moved into api-ms-win-core-winrt-string-l1-1-1.dll in 10.0.10586. Moved into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.14393. |
| [HSTRING_UserUnmarshal64](/windows/win32/api/inspectable/nf-inspectable-hstring_userunmarshal64) | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.10240. Moved into api-ms-win-core-winrt-string-l1-1-1.dll in 10.0.10586. Moved into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.14393. Removed in 10.0.16299. |
| [WindowsCompareStringOrdinal](/windows/win32/api/winstring/nf-winstring-windowscomparestringordinal) | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.10240. Moved into api-ms-win-core-winrt-string-l1-1-1.dll in 10.0.10586. Moved into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.14393. |
| [WindowsConcatString](/windows/win32/api/winstring/nf-winstring-windowsconcatstring) | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.10240. Moved into api-ms-win-core-winrt-string-l1-1-1.dll in 10.0.10586. Moved into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.14393. |
| [WindowsCreateString](/windows/win32/api/winstring/nf-winstring-windowscreatestring) | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.10240. Moved into api-ms-win-core-winrt-string-l1-1-1.dll in 10.0.10586. Moved into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.14393. |
| [WindowsCreateStringReference](/windows/win32/api/winstring/nf-winstring-windowscreatestringreference) | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.10240. Moved into api-ms-win-core-winrt-string-l1-1-1.dll in 10.0.10586. Moved into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.14393. |
| [WindowsDeleteString](/windows/win32/api/winstring/nf-winstring-windowsdeletestring) | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.10240. Moved into api-ms-win-core-winrt-string-l1-1-1.dll in 10.0.10586. Moved into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.14393. |
| [WindowsDeleteStringBuffer](/windows/win32/api/winstring/nf-winstring-windowsdeletestringbuffer) | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.10240. Moved into api-ms-win-core-winrt-string-l1-1-1.dll in 10.0.10586. Moved into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.14393. |
| [WindowsDuplicateString](/windows/win32/api/winstring/nf-winstring-windowsduplicatestring) | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.10240. Moved into api-ms-win-core-winrt-string-l1-1-1.dll in 10.0.10586. Moved into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.14393. |
| [WindowsGetStringLen](/windows/win32/api/winstring/nf-winstring-windowsgetstringlen) | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.10240. Moved into api-ms-win-core-winrt-string-l1-1-1.dll in 10.0.10586. Moved into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.14393. |
| [WindowsGetStringRawBuffer](/windows/win32/api/winstring/nf-winstring-windowsgetstringrawbuffer) | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.10240. Moved into api-ms-win-core-winrt-string-l1-1-1.dll in 10.0.10586. Moved into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.14393. |
| [WindowsIsStringEmpty](/windows/win32/api/winstring/nf-winstring-windowsisstringempty) | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.10240. Moved into api-ms-win-core-winrt-string-l1-1-1.dll in 10.0.10586. Moved into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.14393. |
| [WindowsPreallocateStringBuffer](/windows/win32/api/winstring/nf-winstring-windowspreallocatestringbuffer) | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.10240. Moved into api-ms-win-core-winrt-string-l1-1-1.dll in 10.0.10586. Moved into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.14393. |
| [WindowsPromoteStringBuffer](/windows/win32/api/winstring/nf-winstring-windowspromotestringbuffer) | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.10240. Moved into api-ms-win-core-winrt-string-l1-1-1.dll in 10.0.10586. Moved into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.14393. |
| [WindowsReplaceString](/windows/win32/api/winstring/nf-winstring-windowsreplacestring) | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.10240. Moved into api-ms-win-core-winrt-string-l1-1-1.dll in 10.0.10586. Moved into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.14393. |
| [WindowsStringHasEmbeddedNull](/windows/win32/api/winstring/nf-winstring-windowsstringhasembeddednull) | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.10240. Moved into api-ms-win-core-winrt-string-l1-1-1.dll in 10.0.10586. Moved into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.14393. |
| [WindowsSubstring](/windows/win32/api/winstring/nf-winstring-windowssubstring) | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.10240. Moved into api-ms-win-core-winrt-string-l1-1-1.dll in 10.0.10586. Moved into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.14393. |
| [WindowsSubstringWithSpecifiedLength](/windows/win32/api/winstring/nf-winstring-windowssubstringwithspecifiedlength) | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.10240. Moved into api-ms-win-core-winrt-string-l1-1-1.dll in 10.0.10586. Moved into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.14393. |
| [WindowsTrimStringEnd](/windows/win32/api/winstring/nf-winstring-windowstrimstringend) | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.10240. Moved into api-ms-win-core-winrt-string-l1-1-1.dll in 10.0.10586. Moved into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.14393. |
| [WindowsTrimStringStart](/windows/win32/api/winstring/nf-winstring-windowstrimstringstart) | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.10240. Moved into api-ms-win-core-winrt-string-l1-1-1.dll in 10.0.10586. Moved into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.14393. |


## APIs from api-ms-win-core-xstate-l2-1-0.dll

| API | Requirements |
| -----| --------------|
| [GetEnabledXStateFeatures](/windows/win32/api/winbase/nf-winbase-getenabledxstatefeatures) | Introduced into api-ms-win-core-xstate-l2-1-0.dll in 10.0.10240. Removed in 10.0.10586. Moved into api-ms-win-core-xstate-l2-1-0.dll in 10.0.14393. |
| [GetXStateFeaturesMask](/windows/win32/api/winbase/nf-winbase-getxstatefeaturesmask) | Introduced into api-ms-win-core-xstate-l2-1-0.dll in 10.0.10240. Removed in 10.0.10586. Moved into api-ms-win-core-xstate-l2-1-0.dll in 10.0.14393. |
| [InitializeContext](/windows/win32/api/winbase/nf-winbase-initializecontext) | Introduced into api-ms-win-core-xstate-l2-1-0.dll in 10.0.10240. |
| [LocateXStateFeature](/windows/win32/api/winbase/nf-winbase-locatexstatefeature) | Introduced into api-ms-win-core-xstate-l2-1-0.dll in 10.0.10240. Removed in 10.0.10586. Moved into api-ms-win-core-xstate-l2-1-0.dll in 10.0.14393. |


## APIs from api-ms-win-eventing-classicprovider-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [GetTraceEnableFlags](/windows/win32/api/evntrace/nf-evntrace-gettraceenableflags) | Introduced into api-ms-win-eventing-classicprovider-l1-1-0.dll in 10.0.10240. |
| [GetTraceEnableLevel](/windows/win32/api/evntrace/nf-evntrace-gettraceenablelevel) | Introduced into api-ms-win-eventing-classicprovider-l1-1-0.dll in 10.0.10240. |
| [GetTraceLoggerHandle](/windows/win32/api/evntrace/nf-evntrace-gettraceloggerhandle) | Introduced into api-ms-win-eventing-classicprovider-l1-1-0.dll in 10.0.10240. |
| [RegisterTraceGuidsW](/windows/win32/api/evntrace/nf-evntrace-registertraceguidsa) | Introduced into api-ms-win-eventing-classicprovider-l1-1-0.dll in 10.0.10240. |
| [TraceMessage](/windows/win32/api/evntrace/nf-evntrace-tracemessage) | Introduced into api-ms-win-eventing-classicprovider-l1-1-0.dll in 10.0.10240. |
| [UnregisterTraceGuids](/windows/win32/api/evntrace/nf-evntrace-unregistertraceguids) | Introduced into api-ms-win-eventing-classicprovider-l1-1-0.dll in 10.0.10240. |


## APIs from api-ms-win-eventing-consumer-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [CloseTrace](/windows/win32/api/evntrace/nf-evntrace-closetrace) | Introduced into api-ms-win-eventing-consumer-l1-1-0.dll in 10.0.10240. |
| [OpenTraceW](/windows/win32/api/evntrace/nf-evntrace-opentracea) | Introduced into api-ms-win-eventing-consumer-l1-1-0.dll in 10.0.10240. |
| [ProcessTrace](/windows/win32/api/evntrace/nf-evntrace-processtrace) | Introduced into api-ms-win-eventing-consumer-l1-1-0.dll in 10.0.10240. |


## APIs from api-ms-win-eventing-controller-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [ControlTraceW](/windows/win32/api/evntrace/nf-evntrace-controltracea) | Introduced into api-ms-win-eventing-controller-l1-1-0.dll in 10.0.10240. |
| [EnableTraceEx2](/windows/win32/api/evntrace/nf-evntrace-enabletraceex2) | Introduced into api-ms-win-eventing-controller-l1-1-0.dll in 10.0.10240. |
| [StartTraceW](/windows/win32/api/evntrace/nf-evntrace-starttracea) | Introduced into api-ms-win-eventing-controller-l1-1-0.dll in 10.0.10240. |
| [StopTraceW](/windows/win32/api/evntrace/nf-evntrace-stoptrace) | Introduced into api-ms-win-eventing-controller-l1-1-0.dll in 10.0.10240. |
| [EnumerateTraceGuidsEx](/windows/win32/api/evntrace/nf-evntrace-enumeratetraceguidsex) | Introduced into api-ms-win-eventing-controller-l1-1-0.dll in 10.0.16299. |


## APIs from api-ms-win-eventing-legacy-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [EnableTrace](/windows/win32/api/evntrace/nf-evntrace-enabletrace) | Introduced into api-ms-win-eventing-legacy-l1-1-0.dll in 10.0.10240. |
| [EnableTraceEx](/windows/win32/api/evntrace/nf-evntrace-enabletraceex) | Introduced into api-ms-win-eventing-legacy-l1-1-0.dll in 10.0.10240. |
| [FlushTraceW](/windows/win32/api/evntrace/nf-evntrace-flushtracea) | Introduced into api-ms-win-eventing-legacy-l1-1-0.dll in 10.0.10240. |
| [QueryTraceW](/windows/win32/api/evntrace/nf-evntrace-querytrace) | Introduced into api-ms-win-eventing-legacy-l1-1-0.dll in 10.0.10240. |


## APIs from api-ms-win-eventing-provider-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [EventActivityIdControl](/windows/win32/api/evntprov/nf-evntprov-eventactivityidcontrol) | Introduced into api-ms-win-eventing-provider-l1-1-0.dll in 10.0.10240. |
| [EventRegister](/windows/win32/api/evntprov/nf-evntprov-eventregister) | Introduced into api-ms-win-eventing-provider-l1-1-0.dll in 10.0.10240. |
| [EventSetInformation](/windows/win32/api/evntprov/nf-evntprov-eventsetinformation) | Introduced into api-ms-win-eventing-provider-l1-1-0.dll in 10.0.10240. |
| [EventUnregister](/windows/win32/api/evntprov/nf-evntprov-eventunregister) | Introduced into api-ms-win-eventing-provider-l1-1-0.dll in 10.0.10240. |
| [EventWrite](/windows/win32/api/evntprov/nf-evntprov-eventwrite) | Introduced into api-ms-win-eventing-provider-l1-1-0.dll in 10.0.10240. |
| [EventWriteEx](/windows/win32/api/evntprov/nf-evntprov-eventwriteex) | Introduced into api-ms-win-eventing-provider-l1-1-0.dll in 10.0.10240. |
| [EventWriteString](/windows/win32/api/evntprov/nf-evntprov-eventwritestring) | Introduced into api-ms-win-eventing-provider-l1-1-0.dll in 10.0.10240. |
| [EventWriteTransfer](/windows/win32/api/evntprov/nf-evntprov-eventwritetransfer) | Introduced into api-ms-win-eventing-provider-l1-1-0.dll in 10.0.10240. |
| [EventEnabled](/windows/win32/api/evntprov/nf-evntprov-eventenabled) | Introduced into api-ms-win-eventing-provider-l1-1-0.dll in 10.0.17763. |
| [EventProviderEnabled](/windows/win32/api/evntprov/nf-evntprov-eventproviderenabled) | Introduced into api-ms-win-eventing-provider-l1-1-0.dll in 10.0.17763. |


## APIs from api-ms-win-gaming-tcui-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [ProcessPendingGameUI](/windows/win32/api/gamingtcui/nf-gamingtcui-processpendinggameui) | Introduced into api-ms-win-gaming-tcui-l1-1-0.dll in 10.0.10240. Removed in 10.0.10586. Moved into api-ms-win-gaming-tcui-l1-1-2.dll in 10.0.14393. Moved into api-ms-win-gaming-tcui-l1-1-0.dll in 10.0.16299. |
| [ShowChangeFriendRelationshipUI](/windows/win32/api/gamingtcui/nf-gamingtcui-showchangefriendrelationshipui) | Introduced into api-ms-win-gaming-tcui-l1-1-0.dll in 10.0.10240. Removed in 10.0.10586. Moved into api-ms-win-gaming-tcui-l1-1-2.dll in 10.0.14393. Moved into api-ms-win-gaming-tcui-l1-1-0.dll in 10.0.16299. |
| [ShowGameInviteUI](/windows/win32/api/gamingtcui/nf-gamingtcui-showgameinviteui) | Introduced into api-ms-win-gaming-tcui-l1-1-0.dll in 10.0.10240. Removed in 10.0.10586. Moved into api-ms-win-gaming-tcui-l1-1-2.dll in 10.0.14393. Moved into api-ms-win-gaming-tcui-l1-1-0.dll in 10.0.16299. |
| [ShowPlayerPickerUI](/windows/win32/api/gamingtcui/nf-gamingtcui-showplayerpickerui) | Introduced into api-ms-win-gaming-tcui-l1-1-0.dll in 10.0.10240. Removed in 10.0.10586. Moved into api-ms-win-gaming-tcui-l1-1-2.dll in 10.0.14393. Moved into api-ms-win-gaming-tcui-l1-1-0.dll in 10.0.16299. |
| [ShowProfileCardUI](/windows/win32/api/gamingtcui/nf-gamingtcui-showprofilecardui) | Introduced into api-ms-win-gaming-tcui-l1-1-0.dll in 10.0.10240. Removed in 10.0.10586. Moved into api-ms-win-gaming-tcui-l1-1-2.dll in 10.0.14393. Moved into api-ms-win-gaming-tcui-l1-1-0.dll in 10.0.16299. |
| [ShowTitleAchievementsUI](/windows/win32/api/gamingtcui/nf-gamingtcui-showtitleachievementsui) | Introduced into api-ms-win-gaming-tcui-l1-1-0.dll in 10.0.10240. Removed in 10.0.10586. Moved into api-ms-win-gaming-tcui-l1-1-2.dll in 10.0.14393. Moved into api-ms-win-gaming-tcui-l1-1-0.dll in 10.0.16299. |
| [TryCancelPendingGameUI](/windows/win32/api/gamingtcui/nf-gamingtcui-trycancelpendinggameui) | Introduced into api-ms-win-gaming-tcui-l1-1-0.dll in 10.0.10240. Removed in 10.0.10586. Moved into api-ms-win-gaming-tcui-l1-1-2.dll in 10.0.14393. Moved into api-ms-win-gaming-tcui-l1-1-0.dll in 10.0.16299. |


## APIs from api-ms-win-ro-typeresolution-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [RoGetMetaDataFile](/windows/win32/api/rometadataresolution/nf-rometadataresolution-rogetmetadatafile) | Introduced into api-ms-win-ro-typeresolution-l1-1-0.dll in 10.0.10240. |
| [RoParseTypeName](/windows/win32/api/rometadataresolution/nf-rometadataresolution-roparsetypename) | Introduced into api-ms-win-ro-typeresolution-l1-1-0.dll in 10.0.10240. |
| [RoResolveNamespace](/windows/win32/api/rometadataresolution/nf-rometadataresolution-roresolvenamespace) | Introduced into api-ms-win-ro-typeresolution-l1-1-0.dll in 10.0.10240. |


## APIs from api-ms-win-security-cryptoapi-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [CryptReleaseContext](/windows/win32/api/wincrypt/nf-wincrypt-cryptreleasecontext) | Introduced into api-ms-win-security-cryptoapi-l1-1-0.dll in 10.0.10240. |


## APIs from api-ms-win-shcore-stream-winrt-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [CreateRandomAccessStreamOnFile](/windows/win32/api/shcore/nf-shcore-createrandomaccessstreamonfile) | Introduced into api-ms-win-shcore-stream-winrt-l1-1-0.dll in 10.0.10240. |
| [CreateRandomAccessStreamOverStream](/windows/win32/api/shcore/nf-shcore-createrandomaccessstreamoverstream) | Introduced into api-ms-win-shcore-stream-winrt-l1-1-0.dll in 10.0.10240. |
| [CreateStreamOverRandomAccessStream](/windows/win32/api/shcore/nf-shcore-createstreamoverrandomaccessstream) | Introduced into api-ms-win-shcore-stream-winrt-l1-1-0.dll in 10.0.10240. |


## APIs from cabinet.dll

| API | Requirements |
| -----| --------------|
| [CloseCompressor](/windows/win32/api/compressapi/nf-compressapi-closecompressor) | Introduced into cabinet.dll in 10.0.10240. |
| [CloseDecompressor](/windows/win32/api/compressapi/nf-compressapi-closedecompressor) | Introduced into cabinet.dll in 10.0.10240. |
| [Compress](/windows/win32/api/compressapi/nf-compressapi-compress) | Introduced into cabinet.dll in 10.0.10240. |
| [CreateCompressor](/windows/win32/api/compressapi/nf-compressapi-createcompressor) | Introduced into cabinet.dll in 10.0.10240. |
| [CreateDecompressor](/windows/win32/api/compressapi/nf-compressapi-createdecompressor) | Introduced into cabinet.dll in 10.0.10240. |
| [Decompress](/windows/win32/api/compressapi/nf-compressapi-decompress) | Introduced into cabinet.dll in 10.0.10240. |
| [FDICopy](/windows/win32/api/fdi/nf-fdi-fdicopy) | Introduced into cabinet.dll in 10.0.10240. |
| [FDICreate](/windows/win32/api/fdi/nf-fdi-fdicreate) | Introduced into cabinet.dll in 10.0.10240. |
| [FDIDestroy](/windows/win32/api/fdi/nf-fdi-fdidestroy) | Introduced into cabinet.dll in 10.0.10240. |
| [FDIIsCabinet](/windows/win32/api/fdi/nf-fdi-fdiiscabinet) | Introduced into cabinet.dll in 10.0.10240. |
| [QueryCompressorInformation](/windows/win32/api/compressapi/nf-compressapi-querycompressorinformation) | Introduced into cabinet.dll in 10.0.10240. |
| [QueryDecompressorInformation](/windows/win32/api/compressapi/nf-compressapi-querydecompressorinformation) | Introduced into cabinet.dll in 10.0.10240. |
| [ResetCompressor](/windows/win32/api/compressapi/nf-compressapi-resetcompressor) | Introduced into cabinet.dll in 10.0.10240. |
| [ResetDecompressor](/windows/win32/api/compressapi/nf-compressapi-resetdecompressor) | Introduced into cabinet.dll in 10.0.10240. |
| [SetCompressorInformation](/windows/win32/api/compressapi/nf-compressapi-setcompressorinformation) | Introduced into cabinet.dll in 10.0.10240. |
| [SetDecompressorInformation](/windows/win32/api/compressapi/nf-compressapi-setdecompressorinformation) | Introduced into cabinet.dll in 10.0.10240. |


## APIs from chakra.dll

| API | Requirements |
| -----| --------------|
| JsAddRef | Introduced into chakra.dll in 10.0.10240. |
| JsBooleanToBool | Introduced into chakra.dll in 10.0.10240. |
| JsBoolToBoolean | Introduced into chakra.dll in 10.0.10240. |
| JsCallFunction | Introduced into chakra.dll in 10.0.10240. |
| JsCollectGarbage | Introduced into chakra.dll in 10.0.10240. |
| JsConstructObject | Introduced into chakra.dll in 10.0.10240. |
| JsConvertValueToBoolean | Introduced into chakra.dll in 10.0.10240. |
| JsConvertValueToNumber | Introduced into chakra.dll in 10.0.10240. |
| JsConvertValueToObject | Introduced into chakra.dll in 10.0.10240. |
| JsConvertValueToString | Introduced into chakra.dll in 10.0.10240. |
| JsCreateArray | Introduced into chakra.dll in 10.0.10240. |
| JsCreateArrayBuffer | Introduced into chakra.dll in 10.0.10240. |
| JsCreateContext | Introduced into chakra.dll in 10.0.10240. |
| JsCreateDataView | Introduced into chakra.dll in 10.0.10240. |
| JsCreateError | Introduced into chakra.dll in 10.0.10240. |
| JsCreateExternalObject | Introduced into chakra.dll in 10.0.10240. |
| JsCreateFunction | Introduced into chakra.dll in 10.0.10240. |
| JsCreateNamedFunction | Introduced into chakra.dll in 10.0.10240. |
| JsCreateObject | Introduced into chakra.dll in 10.0.10240. |
| JsCreateRangeError | Introduced into chakra.dll in 10.0.10240. |
| JsCreateReferenceError | Introduced into chakra.dll in 10.0.10240. |
| JsCreateRuntime | Introduced into chakra.dll in 10.0.10240. |
| JsCreateSymbol | Introduced into chakra.dll in 10.0.10240. |
| JsCreateSyntaxError | Introduced into chakra.dll in 10.0.10240. |
| JsCreateTypedArray | Introduced into chakra.dll in 10.0.10240. |
| JsCreateTypeError | Introduced into chakra.dll in 10.0.10240. |
| JsCreateURIError | Introduced into chakra.dll in 10.0.10240. |
| JsDefineProperty | Introduced into chakra.dll in 10.0.10240. |
| JsDeleteIndexedProperty | Introduced into chakra.dll in 10.0.10240. |
| JsDeleteProperty | Introduced into chakra.dll in 10.0.10240. |
| JsDisableRuntimeExecution | Introduced into chakra.dll in 10.0.10240. |
| JsDisposeRuntime | Introduced into chakra.dll in 10.0.10240. |
| JsDoubleToNumber | Introduced into chakra.dll in 10.0.10240. |
| JsEnableRuntimeExecution | Introduced into chakra.dll in 10.0.10240. |
| JsEquals | Introduced into chakra.dll in 10.0.10240. |
| JsGetAndClearException | Introduced into chakra.dll in 10.0.10240. |
| JsGetArrayBufferStorage | Introduced into chakra.dll in 10.0.10240. |
| JsGetCurrentContext | Introduced into chakra.dll in 10.0.10240. |
| JsGetDataViewStorage | Introduced into chakra.dll in 10.0.10240. |
| JsGetExtensionAllowed | Introduced into chakra.dll in 10.0.10240. |
| JsGetExternalData | Introduced into chakra.dll in 10.0.10240. |
| JsGetFalseValue | Introduced into chakra.dll in 10.0.10240. |
| JsGetGlobalObject | Introduced into chakra.dll in 10.0.10240. |
| JsGetIndexedPropertiesExternalData | Introduced into chakra.dll in 10.0.10240. |
| JsGetIndexedProperty | Introduced into chakra.dll in 10.0.10240. |
| JsGetNullValue | Introduced into chakra.dll in 10.0.10240. |
| JsGetOwnPropertyDescriptor | Introduced into chakra.dll in 10.0.10240. |
| JsGetOwnPropertyNames | Introduced into chakra.dll in 10.0.10240. |
| JsGetOwnPropertySymbols | Introduced into chakra.dll in 10.0.10240. |
| JsGetProperty | Introduced into chakra.dll in 10.0.10240. |
| JsGetPropertyIdFromName | Introduced into chakra.dll in 10.0.10240. |
| JsGetPropertyIdFromSymbol | Introduced into chakra.dll in 10.0.10240. |
| JsGetPropertyIdType | Introduced into chakra.dll in 10.0.10240. |
| JsGetPropertyNameFromId | Introduced into chakra.dll in 10.0.10240. |
| JsGetPrototype | Introduced into chakra.dll in 10.0.10240. |
| JsGetRuntime | Introduced into chakra.dll in 10.0.10240. |
| JsGetRuntimeMemoryLimit | Introduced into chakra.dll in 10.0.10240. |
| JsGetRuntimeMemoryUsage | Introduced into chakra.dll in 10.0.10240. |
| JsGetStringLength | Introduced into chakra.dll in 10.0.10240. |
| JsGetSymbolFromPropertyId | Introduced into chakra.dll in 10.0.10240. |
| JsGetTrueValue | Introduced into chakra.dll in 10.0.10240. |
| JsGetTypedArrayStorage | Introduced into chakra.dll in 10.0.10240. |
| JsGetUndefinedValue | Introduced into chakra.dll in 10.0.10240. |
| JsGetValueType | Introduced into chakra.dll in 10.0.10240. |
| JsHasException | Introduced into chakra.dll in 10.0.10240. |
| JsHasExternalData | Introduced into chakra.dll in 10.0.10240. |
| JsHasIndexedPropertiesExternalData | Introduced into chakra.dll in 10.0.10240. |
| JsHasIndexedProperty | Introduced into chakra.dll in 10.0.10240. |
| JsHasProperty | Introduced into chakra.dll in 10.0.10240. |
| JsIdle | Introduced into chakra.dll in 10.0.10240. |
| JsInspectableToObject | Introduced into chakra.dll in 10.0.10240. |
| JsIntToNumber | Introduced into chakra.dll in 10.0.10240. |
| JsIsRuntimeExecutionDisabled | Introduced into chakra.dll in 10.0.10240. |
| JsNumberToDouble | Introduced into chakra.dll in 10.0.10240. |
| JsNumberToInt | Introduced into chakra.dll in 10.0.10240. |
| JsObjectToInspectable | Introduced into chakra.dll in 10.0.10240. |
| JsParseScript | Introduced into chakra.dll in 10.0.10240. |
| JsParseSerializedScript | Introduced into chakra.dll in 10.0.10240. |
| JsPointerToString | Introduced into chakra.dll in 10.0.10240. |
| JsPreventExtension | Introduced into chakra.dll in 10.0.10240. |
| JsProjectWinRTNamespace | Introduced into chakra.dll in 10.0.10240. |
| JsRelease | Introduced into chakra.dll in 10.0.10240. |
| JsRunScript | Introduced into chakra.dll in 10.0.10240. |
| JsRunSerializedScript | Introduced into chakra.dll in 10.0.10240. |
| JsSerializeScript | Introduced into chakra.dll in 10.0.10240. |
| JsSetCurrentContext | Introduced into chakra.dll in 10.0.10240. |
| JsSetException | Introduced into chakra.dll in 10.0.10240. |
| JsSetExternalData | Introduced into chakra.dll in 10.0.10240. |
| JsSetIndexedPropertiesToExternalData | Introduced into chakra.dll in 10.0.10240. |
| JsSetIndexedProperty | Introduced into chakra.dll in 10.0.10240. |
| JsSetObjectBeforeCollectCallback | Introduced into chakra.dll in 10.0.10240. |
| JsSetProjectionEnqueueCallback | Introduced into chakra.dll in 10.0.10240. |
| JsSetPromiseContinuationCallback | Introduced into chakra.dll in 10.0.10240. |
| JsSetProperty | Introduced into chakra.dll in 10.0.10240. |
| JsSetPrototype | Introduced into chakra.dll in 10.0.10240. |
| JsSetRuntimeBeforeCollectCallback | Introduced into chakra.dll in 10.0.10240. |
| JsSetRuntimeMemoryAllocationCallback | Introduced into chakra.dll in 10.0.10240. |
| JsSetRuntimeMemoryLimit | Introduced into chakra.dll in 10.0.10240. |
| JsStartDebugging | Introduced into chakra.dll in 10.0.10240. |
| JsStrictEquals | Introduced into chakra.dll in 10.0.10240. |
| JsStringToPointer | Introduced into chakra.dll in 10.0.10240. |
| JsValueToVariant | Introduced into chakra.dll in 10.0.10240. |
| JsVariantToValue | Introduced into chakra.dll in 10.0.10240. |
| JsGetContextData | Introduced into chakra.dll in 10.0.10586. |
| JsGetContextOfObject | Introduced into chakra.dll in 10.0.10586. |
| JsGetTypedArrayInfo | Introduced into chakra.dll in 10.0.10586. |
| JsInstanceOf | Introduced into chakra.dll in 10.0.10586. |
| JsParseSerializedScriptWithCallback | Introduced into chakra.dll in 10.0.10586. |
| JsRunSerializedScriptWithCallback | Introduced into chakra.dll in 10.0.10586. |
| JsSetContextData | Introduced into chakra.dll in 10.0.10586. |
| JsCreateExternalArrayBuffer | Introduced into chakra.dll in 10.0.14393. |


## APIs from crypt32.dll

| API | Requirements |
| -----| --------------|
| [CertAddCertificateContextToStore](/windows/win32/api/wincrypt/nf-wincrypt-certaddcertificatecontexttostore) | Introduced into crypt32.dll in 10.0.10240. |
| [CertAddCertificateLinkToStore](/windows/win32/api/wincrypt/nf-wincrypt-certaddcertificatelinktostore) | Introduced into crypt32.dll in 10.0.10240. |
| [CertAddCRLContextToStore](/windows/win32/api/wincrypt/nf-wincrypt-certaddcrlcontexttostore) | Introduced into crypt32.dll in 10.0.10240. |
| [CertAddCRLLinkToStore](/windows/win32/api/wincrypt/nf-wincrypt-certaddcrllinktostore) | Introduced into crypt32.dll in 10.0.10240. |
| [CertAddCTLContextToStore](/windows/win32/api/wincrypt/nf-wincrypt-certaddctlcontexttostore) | Introduced into crypt32.dll in 10.0.10240. |
| [CertAddCTLLinkToStore](/windows/win32/api/wincrypt/nf-wincrypt-certaddctllinktostore) | Introduced into crypt32.dll in 10.0.10240. |
| [CertAddEncodedCertificateToStore](/windows/win32/api/wincrypt/nf-wincrypt-certaddencodedcertificatetostore) | Introduced into crypt32.dll in 10.0.10240. |
| [CertAddEncodedCRLToStore](/windows/win32/api/wincrypt/nf-wincrypt-certaddencodedcrltostore) | Introduced into crypt32.dll in 10.0.10240. |
| [CertAddEncodedCTLToStore](/windows/win32/api/wincrypt/nf-wincrypt-certaddencodedctltostore) | Introduced into crypt32.dll in 10.0.10240. |
| [CertAddSerializedElementToStore](/windows/win32/api/wincrypt/nf-wincrypt-certaddserializedelementtostore) | Introduced into crypt32.dll in 10.0.10240. |
| [CertAddStoreToCollection](/windows/win32/api/wincrypt/nf-wincrypt-certaddstoretocollection) | Introduced into crypt32.dll in 10.0.10240. |
| [CertCloseStore](/windows/win32/api/wincrypt/nf-wincrypt-certclosestore) | Introduced into crypt32.dll in 10.0.10240. |
| [CertCompareCertificate](/windows/win32/api/wincrypt/nf-wincrypt-certcomparecertificate) | Introduced into crypt32.dll in 10.0.10240. |
| [CertCompareCertificateName](/windows/win32/api/wincrypt/nf-wincrypt-certcomparecertificatename) | Introduced into crypt32.dll in 10.0.10240. |
| [CertCompareIntegerBlob](/windows/win32/api/wincrypt/nf-wincrypt-certcompareintegerblob) | Introduced into crypt32.dll in 10.0.10240. |
| [CertControlStore](/windows/win32/api/wincrypt/nf-wincrypt-certcontrolstore) | Introduced into crypt32.dll in 10.0.10240. |
| [CertCreateCertificateChainEngine](/windows/win32/api/wincrypt/nf-wincrypt-certcreatecertificatechainengine) | Introduced into crypt32.dll in 10.0.10240. |
| [CertCreateCertificateContext](/windows/win32/api/wincrypt/nf-wincrypt-certcreatecertificatecontext) | Introduced into crypt32.dll in 10.0.10240. |
| [CertCreateContext](/windows/win32/api/wincrypt/nf-wincrypt-certcreatecontext) | Introduced into crypt32.dll in 10.0.10240. |
| [CertCreateCRLContext](/windows/win32/api/wincrypt/nf-wincrypt-certcreatecrlcontext) | Introduced into crypt32.dll in 10.0.10240. |
| [CertCreateCTLContext](/windows/win32/api/wincrypt/nf-wincrypt-certcreatectlcontext) | Introduced into crypt32.dll in 10.0.10240. |
| [CertCreateSelfSignCertificate](/windows/win32/api/wincrypt/nf-wincrypt-certcreateselfsigncertificate) | Introduced into crypt32.dll in 10.0.10240. |
| [CertDeleteCertificateFromStore](/windows/win32/api/wincrypt/nf-wincrypt-certdeletecertificatefromstore) | Introduced into crypt32.dll in 10.0.10240. |
| [CertDeleteCRLFromStore](/windows/win32/api/wincrypt/nf-wincrypt-certdeletecrlfromstore) | Introduced into crypt32.dll in 10.0.10240. |
| [CertDeleteCTLFromStore](/windows/win32/api/wincrypt/nf-wincrypt-certdeletectlfromstore) | Introduced into crypt32.dll in 10.0.10240. |
| [CertDuplicateCertificateChain](/windows/win32/api/wincrypt/nf-wincrypt-certduplicatecertificatechain) | Introduced into crypt32.dll in 10.0.10240. |
| [CertDuplicateCertificateContext](/windows/win32/api/wincrypt/nf-wincrypt-certduplicatecertificatecontext) | Introduced into crypt32.dll in 10.0.10240. |
| [CertDuplicateCRLContext](/windows/win32/api/wincrypt/nf-wincrypt-certduplicatecrlcontext) | Introduced into crypt32.dll in 10.0.10240. |
| [CertDuplicateCTLContext](/windows/win32/api/wincrypt/nf-wincrypt-certduplicatectlcontext) | Introduced into crypt32.dll in 10.0.10240. |
| [CertDuplicateStore](/windows/win32/api/wincrypt/nf-wincrypt-certduplicatestore) | Introduced into crypt32.dll in 10.0.10240. |
| [CertEnumCertificateContextProperties](/windows/win32/api/wincrypt/nf-wincrypt-certenumcertificatecontextproperties) | Introduced into crypt32.dll in 10.0.10240. |
| [CertEnumCertificatesInStore](/windows/win32/api/wincrypt/nf-wincrypt-certenumcertificatesinstore) | Introduced into crypt32.dll in 10.0.10240. |
| [CertEnumCRLContextProperties](/windows/win32/api/wincrypt/nf-wincrypt-certenumcrlcontextproperties) | Introduced into crypt32.dll in 10.0.10240. |
| [CertEnumCRLsInStore](/windows/win32/api/wincrypt/nf-wincrypt-certenumcrlsinstore) | Introduced into crypt32.dll in 10.0.10240. |
| [CertEnumCTLContextProperties](/windows/win32/api/wincrypt/nf-wincrypt-certenumctlcontextproperties) | Introduced into crypt32.dll in 10.0.10240. |
| [CertEnumCTLsInStore](/windows/win32/api/wincrypt/nf-wincrypt-certenumctlsinstore) | Introduced into crypt32.dll in 10.0.10240. |
| [CertEnumPhysicalStore](/windows/win32/api/wincrypt/nf-wincrypt-certenumphysicalstore) | Introduced into crypt32.dll in 10.0.10240. |
| [CertEnumSystemStore](/windows/win32/api/wincrypt/nf-wincrypt-certenumsystemstore) | Introduced into crypt32.dll in 10.0.10240. |
| [CertEnumSystemStoreLocation](/windows/win32/api/wincrypt/nf-wincrypt-certenumsystemstorelocation) | Introduced into crypt32.dll in 10.0.10240. |
| [CertFindAttribute](/windows/win32/api/wincrypt/nf-wincrypt-certfindattribute) | Introduced into crypt32.dll in 10.0.10240. |
| [CertFindCertificateInCRL](/windows/win32/api/wincrypt/nf-wincrypt-certfindcertificateincrl) | Introduced into crypt32.dll in 10.0.10240. |
| [CertFindCertificateInStore](/windows/win32/api/wincrypt/nf-wincrypt-certfindcertificateinstore) | Introduced into crypt32.dll in 10.0.10240. |
| [CertFindCRLInStore](/windows/win32/api/wincrypt/nf-wincrypt-certfindcrlinstore) | Introduced into crypt32.dll in 10.0.10240. |
| [CertFindCTLInStore](/windows/win32/api/wincrypt/nf-wincrypt-certfindctlinstore) | Introduced into crypt32.dll in 10.0.10240. |
| [CertFindExtension](/windows/win32/api/wincrypt/nf-wincrypt-certfindextension) | Introduced into crypt32.dll in 10.0.10240. |
| [CertFindRDNAttr](/windows/win32/api/wincrypt/nf-wincrypt-certfindrdnattr) | Introduced into crypt32.dll in 10.0.10240. |
| [CertFindSubjectInCTL](/windows/win32/api/wincrypt/nf-wincrypt-certfindsubjectinctl) | Introduced into crypt32.dll in 10.0.10240. |
| [CertFreeCertificateChain](/windows/win32/api/wincrypt/nf-wincrypt-certfreecertificatechain) | Introduced into crypt32.dll in 10.0.10240. |
| [CertFreeCertificateChainEngine](/windows/win32/api/wincrypt/nf-wincrypt-certfreecertificatechainengine) | Introduced into crypt32.dll in 10.0.10240. |
| [CertFreeCertificateChainList](/windows/win32/api/wincrypt/nf-wincrypt-certfreecertificatechainlist) | Introduced into crypt32.dll in 10.0.10240. |
| [CertFreeCertificateContext](/windows/win32/api/wincrypt/nf-wincrypt-certfreecertificatecontext) | Introduced into crypt32.dll in 10.0.10240. |
| [CertFreeCRLContext](/windows/win32/api/wincrypt/nf-wincrypt-certfreecrlcontext) | Introduced into crypt32.dll in 10.0.10240. |
| [CertFreeCTLContext](/windows/win32/api/wincrypt/nf-wincrypt-certfreectlcontext) | Introduced into crypt32.dll in 10.0.10240. |
| [CertGetCertificateChain](/windows/win32/api/wincrypt/nf-wincrypt-certgetcertificatechain) | Introduced into crypt32.dll in 10.0.10240. |
| [CertGetCertificateContextProperty](/windows/win32/api/wincrypt/nf-wincrypt-certgetcertificatecontextproperty) | Introduced into crypt32.dll in 10.0.10240. |
| [CertGetCRLContextProperty](/windows/win32/api/wincrypt/nf-wincrypt-certgetcrlcontextproperty) | Introduced into crypt32.dll in 10.0.10240. |
| [CertGetCRLFromStore](/windows/win32/api/wincrypt/nf-wincrypt-certgetcrlfromstore) | Introduced into crypt32.dll in 10.0.10240. |
| [CertGetCTLContextProperty](/windows/win32/api/wincrypt/nf-wincrypt-certgetctlcontextproperty) | Introduced into crypt32.dll in 10.0.10240. |
| [CertGetEnhancedKeyUsage](/windows/win32/api/wincrypt/nf-wincrypt-certgetenhancedkeyusage) | Introduced into crypt32.dll in 10.0.10240. |
| [CertGetIntendedKeyUsage](/windows/win32/api/wincrypt/nf-wincrypt-certgetintendedkeyusage) | Introduced into crypt32.dll in 10.0.10240. |
| [CertGetIssuerCertificateFromStore](/windows/win32/api/wincrypt/nf-wincrypt-certgetissuercertificatefromstore) | Introduced into crypt32.dll in 10.0.10240. |
| [CertGetNameStringA](/windows/win32/api/wincrypt/nf-wincrypt-certgetnamestringa) | Introduced into crypt32.dll in 10.0.10240. |
| [CertGetNameStringW](/windows/win32/api/wincrypt/nf-wincrypt-certgetnamestringa) | Introduced into crypt32.dll in 10.0.10240. |
| [CertGetPublicKeyLength](/windows/win32/api/wincrypt/nf-wincrypt-certgetpublickeylength) | Introduced into crypt32.dll in 10.0.10240. |
| [CertGetStoreProperty](/windows/win32/api/wincrypt/nf-wincrypt-certgetstoreproperty) | Introduced into crypt32.dll in 10.0.10240. |
| [CertGetSubjectCertificateFromStore](/windows/win32/api/wincrypt/nf-wincrypt-certgetsubjectcertificatefromstore) | Introduced into crypt32.dll in 10.0.10240. |
| [CertGetValidUsages](/windows/win32/api/wincrypt/nf-wincrypt-certgetvalidusages) | Introduced into crypt32.dll in 10.0.10240. |
| [CertIsValidCRLForCertificate](/windows/win32/api/wincrypt/nf-wincrypt-certisvalidcrlforcertificate) | Introduced into crypt32.dll in 10.0.10240. |
| [CertNameToStrA](/windows/win32/api/wincrypt/nf-wincrypt-certnametostra) | Introduced into crypt32.dll in 10.0.10240. |
| [CertNameToStrW](/windows/win32/api/wincrypt/nf-wincrypt-certnametostra) | Introduced into crypt32.dll in 10.0.10240. |
| [CertOpenStore](/windows/win32/api/wincrypt/nf-wincrypt-certopenstore) | Introduced into crypt32.dll in 10.0.10240. |
| [CertRDNValueToStrA](/windows/win32/api/wincrypt/nf-wincrypt-certrdnvaluetostra) | Introduced into crypt32.dll in 10.0.10240. |
| [CertRDNValueToStrW](/windows/win32/api/wincrypt/nf-wincrypt-certrdnvaluetostra) | Introduced into crypt32.dll in 10.0.10240. |
| [CertRemoveStoreFromCollection](/windows/win32/api/wincrypt/nf-wincrypt-certremovestorefromcollection) | Introduced into crypt32.dll in 10.0.10240. |
| [CertResyncCertificateChainEngine](/windows/win32/api/wincrypt/nf-wincrypt-certresynccertificatechainengine) | Introduced into crypt32.dll in 10.0.10240. |
| [CertSaveStore](/windows/win32/api/wincrypt/nf-wincrypt-certsavestore) | Introduced into crypt32.dll in 10.0.10240. |
| [CertSelectCertificateChains](/windows/win32/api/wincrypt/nf-wincrypt-certselectcertificatechains) | Introduced into crypt32.dll in 10.0.10240. |
| [CertSerializeCertificateStoreElement](/windows/win32/api/wincrypt/nf-wincrypt-certserializecertificatestoreelement) | Introduced into crypt32.dll in 10.0.10240. |
| [CertSerializeCRLStoreElement](/windows/win32/api/wincrypt/nf-wincrypt-certserializecrlstoreelement) | Introduced into crypt32.dll in 10.0.10240. |
| [CertSerializeCTLStoreElement](/windows/win32/api/wincrypt/nf-wincrypt-certserializectlstoreelement) | Introduced into crypt32.dll in 10.0.10240. |
| [CertSetCertificateContextProperty](/windows/win32/api/wincrypt/nf-wincrypt-certsetcertificatecontextproperty) | Introduced into crypt32.dll in 10.0.10240. |
| [CertSetCRLContextProperty](/windows/win32/api/wincrypt/nf-wincrypt-certsetcrlcontextproperty) | Introduced into crypt32.dll in 10.0.10240. |
| [CertSetCTLContextProperty](/windows/win32/api/wincrypt/nf-wincrypt-certsetctlcontextproperty) | Introduced into crypt32.dll in 10.0.10240. |
| [CertSetStoreProperty](/windows/win32/api/wincrypt/nf-wincrypt-certsetstoreproperty) | Introduced into crypt32.dll in 10.0.10240. |
| [CertStrToNameA](/windows/win32/api/wincrypt/nf-wincrypt-certstrtonamea) | Introduced into crypt32.dll in 10.0.10240. |
| [CertStrToNameW](/windows/win32/api/wincrypt/nf-wincrypt-certstrtonamea) | Introduced into crypt32.dll in 10.0.10240. |
| [CertVerifyCertificateChainPolicy](/windows/win32/api/wincrypt/nf-wincrypt-certverifycertificatechainpolicy) | Introduced into crypt32.dll in 10.0.10240. |
| [CertVerifySubjectCertificateContext](/windows/win32/api/wincrypt/nf-wincrypt-certverifysubjectcertificatecontext) | Introduced into crypt32.dll in 10.0.10240. |
| [CertVerifyTimeValidity](/windows/win32/api/wincrypt/nf-wincrypt-certverifytimevalidity) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptAcquireCertificatePrivateKey](/windows/win32/api/wincrypt/nf-wincrypt-cryptacquirecertificateprivatekey) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptDecodeObject](/windows/win32/api/wincrypt/nf-wincrypt-cryptdecodeobject) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptDecodeObjectEx](/windows/win32/api/wincrypt/nf-wincrypt-cryptdecodeobjectex) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptEncodeObject](/windows/win32/api/wincrypt/nf-wincrypt-cryptencodeobject) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptEncodeObjectEx](/windows/win32/api/wincrypt/nf-wincrypt-cryptencodeobjectex) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptEnumOIDFunction](/windows/win32/api/wincrypt/nf-wincrypt-cryptenumoidfunction) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptEnumOIDInfo](/windows/win32/api/wincrypt/nf-wincrypt-cryptenumoidinfo) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptFindLocalizedName](/windows/win32/api/wincrypt/nf-wincrypt-cryptfindlocalizedname) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptFindOIDInfo](/windows/win32/api/wincrypt/nf-wincrypt-cryptfindoidinfo) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptFormatObject](/windows/win32/api/wincrypt/nf-wincrypt-cryptformatobject) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptFreeOIDFunctionAddress](/windows/win32/api/wincrypt/nf-wincrypt-cryptfreeoidfunctionaddress) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptGetDefaultOIDDllList](/windows/win32/api/wincrypt/nf-wincrypt-cryptgetdefaultoiddlllist) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptGetDefaultOIDFunctionAddress](/windows/win32/api/wincrypt/nf-wincrypt-cryptgetdefaultoidfunctionaddress) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptGetOIDFunctionAddress](/windows/win32/api/wincrypt/nf-wincrypt-cryptgetoidfunctionaddress) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptGetOIDFunctionValue](/windows/win32/api/wincrypt/nf-wincrypt-cryptgetoidfunctionvalue) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptHashPublicKeyInfo](/windows/win32/api/wincrypt/nf-wincrypt-crypthashpublickeyinfo) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptInitOIDFunctionSet](/windows/win32/api/wincrypt/nf-wincrypt-cryptinitoidfunctionset) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptInstallOIDFunctionAddress](/windows/win32/api/wincrypt/nf-wincrypt-cryptinstalloidfunctionaddress) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptMsgCalculateEncodedLength](/windows/win32/api/wincrypt/nf-wincrypt-cryptmsgcalculateencodedlength) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptMsgClose](/windows/win32/api/wincrypt/nf-wincrypt-cryptmsgclose) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptMsgControl](/windows/win32/api/wincrypt/nf-wincrypt-cryptmsgcontrol) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptMsgCountersign](/windows/win32/api/wincrypt/nf-wincrypt-cryptmsgcountersign) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptMsgCountersignEncoded](/windows/win32/api/wincrypt/nf-wincrypt-cryptmsgcountersignencoded) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptMsgDuplicate](/windows/win32/api/wincrypt/nf-wincrypt-cryptmsgduplicate) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptMsgGetAndVerifySigner](/windows/win32/api/wincrypt/nf-wincrypt-cryptmsggetandverifysigner) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptMsgGetParam](/windows/win32/api/wincrypt/nf-wincrypt-cryptmsggetparam) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptMsgOpenToDecode](/windows/win32/api/wincrypt/nf-wincrypt-cryptmsgopentodecode) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptMsgOpenToEncode](/windows/win32/api/wincrypt/nf-wincrypt-cryptmsgopentoencode) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptMsgUpdate](/windows/win32/api/wincrypt/nf-wincrypt-cryptmsgupdate) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptMsgVerifyCountersignatureEncoded](/windows/win32/api/wincrypt/nf-wincrypt-cryptmsgverifycountersignatureencoded) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptMsgVerifyCountersignatureEncodedEx](/windows/win32/api/wincrypt/nf-wincrypt-cryptmsgverifycountersignatureencodedex) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptProtectData](/windows/win32/api/dpapi/nf-dpapi-cryptprotectdata) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptQueryObject](/windows/win32/api/wincrypt/nf-wincrypt-cryptqueryobject) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptRetrieveTimeStamp](/windows/win32/api/wincrypt/nf-wincrypt-cryptretrievetimestamp) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptUnprotectData](/windows/win32/api/dpapi/nf-dpapi-cryptunprotectdata) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptVerifyTimeStampSignature](/windows/win32/api/wincrypt/nf-wincrypt-cryptverifytimestampsignature) | Introduced into crypt32.dll in 10.0.10240. |
| [PFXExportCertStore](/windows/win32/api/wincrypt/nf-wincrypt-pfxexportcertstore) | Introduced into crypt32.dll in 10.0.10240. |
| [PFXExportCertStoreEx](/windows/win32/api/wincrypt/nf-wincrypt-pfxexportcertstoreex) | Introduced into crypt32.dll in 10.0.10240. |
| [PFXImportCertStore](/windows/win32/api/wincrypt/nf-wincrypt-pfximportcertstore) | Introduced into crypt32.dll in 10.0.10240. |
| [PFXIsPFXBlob](/windows/win32/api/wincrypt/nf-wincrypt-pfxispfxblob) | Introduced into crypt32.dll in 10.0.10240. |
| [PFXVerifyPassword](/windows/win32/api/wincrypt/nf-wincrypt-pfxverifypassword) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptBinaryToStringW](/windows/win32/api/wincrypt/nf-wincrypt-cryptbinarytostringa) | Introduced into crypt32.dll in 10.0.16299. |
| [CryptHashCertificate2](/windows/win32/api/wincrypt/nf-wincrypt-crypthashcertificate2) | Introduced into crypt32.dll in 10.0.16299. |
| [CryptImportPublicKeyInfoEx2](/windows/win32/api/wincrypt/nf-wincrypt-cryptimportpublickeyinfoex2) | Introduced into crypt32.dll in 10.0.16299. |
| [CryptProtectMemory](/windows/win32/api/dpapi/nf-dpapi-cryptprotectmemory) | Introduced into crypt32.dll in 10.0.16299. |
| [CryptStringToBinaryA](/windows/win32/api/wincrypt/nf-wincrypt-cryptstringtobinarya) | Introduced into crypt32.dll in 10.0.16299. |
| [CryptUnprotectMemory](/windows/win32/api/dpapi/nf-dpapi-cryptunprotectmemory) | Introduced into crypt32.dll in 10.0.16299. |


## APIs from d2d1.dll

| API | Requirements |
| -----| --------------|
| [D2D1ComputeMaximumScaleFactor](/windows/win32/api/d2d1_2/nf-d2d1_2-d2d1computemaximumscalefactor) | Introduced into d2d1.dll in 10.0.10240. |
| [D2D1ConvertColorSpace](/windows/win32/api/d2d1_1/nf-d2d1_1-d2d1convertcolorspace) | Introduced into d2d1.dll in 10.0.10240. |
| [D2D1CreateDevice](/windows/win32/api/d2d1_1/nf-d2d1_1-d2d1createdevice) | Introduced into d2d1.dll in 10.0.10240. |
| [D2D1CreateDeviceContext](/windows/win32/api/d2d1_1/nf-d2d1_1-d2d1createdevicecontext) | Introduced into d2d1.dll in 10.0.10240. |
| [D2D1CreateFactory](/windows/win32/api/d2d1/nf-d2d1-d2d1createfactory) | Introduced into d2d1.dll in 10.0.10240. |
| [D2D1GetGradientMeshInteriorPointsFromCoonsPatch](/windows/win32/api/d2d1_3/nf-d2d1_3-d2d1getgradientmeshinteriorpointsfromcoonspatch) | Introduced into d2d1.dll in 10.0.10240. |
| [D2D1InvertMatrix](/windows/win32/api/d2d1/nf-d2d1-d2d1invertmatrix) | Introduced into d2d1.dll in 10.0.10240. |
| [D2D1IsMatrixInvertible](/windows/win32/api/d2d1/nf-d2d1-d2d1ismatrixinvertible) | Introduced into d2d1.dll in 10.0.10240. |
| [D2D1MakeRotateMatrix](/windows/win32/api/d2d1/nf-d2d1-d2d1makerotatematrix) | Introduced into d2d1.dll in 10.0.10240. |
| [D2D1MakeSkewMatrix](/windows/win32/api/d2d1/nf-d2d1-d2d1makeskewmatrix) | Introduced into d2d1.dll in 10.0.10240. |
| [D2D1SinCos](/windows/win32/api/d2d1_1/nf-d2d1_1-d2d1sincos) | Introduced into d2d1.dll in 10.0.10240. |
| [D2D1Tan](/windows/win32/api/d2d1_1/nf-d2d1_1-d2d1tan) | Introduced into d2d1.dll in 10.0.10240. |
| [D2D1Vec3Length](/windows/win32/api/d2d1_1/nf-d2d1_1-d2d1vec3length) | Introduced into d2d1.dll in 10.0.10240. |


## APIs from d3d11.dll

| API | Requirements |
| -----| --------------|
| CreateDirect3D11DeviceFromDXGIDevice | Introduced into d3d11.dll in 10.0.10240. |
| CreateDirect3D11SurfaceFromDXGISurface | Introduced into d3d11.dll in 10.0.10240. |
| [D3D11CreateDevice](/windows/win32/api/d3d11/nf-d3d11-d3d11createdevice) | Introduced into d3d11.dll in 10.0.10240. |
| [D3D11On12CreateDevice](/windows/win32/api/d3d11on12/nf-d3d11on12-d3d11on12createdevice) | Introduced into d3d11.dll in 10.0.10240. |


## APIs from d3d12.dll

| API | Requirements |
| -----| --------------|
| [D3D12CreateDevice](/windows/win32/api/d3d12/nf-d3d12-d3d12createdevice) | Introduced into d3d12.dll in 10.0.10240. |
| [D3D12CreateRootSignatureDeserializer](/windows/win32/api/d3d12/nf-d3d12-d3d12createrootsignaturedeserializer) | Introduced into d3d12.dll in 10.0.10240. |
| [D3D12SerializeRootSignature](/windows/win32/api/d3d12/nf-d3d12-d3d12serializerootsignature) | Introduced into d3d12.dll in 10.0.10240. |
| [D3D12CreateVersionedRootSignatureDeserializer](/windows/win32/api/d3d12/nf-d3d12-d3d12createversionedrootsignaturedeserializer) | Introduced into d3d12.dll in 10.0.16299. |
| [D3D12EnableExperimentalFeatures](/windows/win32/api/d3d12/nf-d3d12-d3d12enableexperimentalfeatures) | Introduced into d3d12.dll in 10.0.16299. |
| [D3D12SerializeVersionedRootSignature](/windows/win32/api/d3d12/nf-d3d12-d3d12serializeversionedrootsignature) | Introduced into d3d12.dll in 10.0.16299. |


## APIs from d3dcompiler_47.dll

| API | Requirements |
| -----| --------------|
| [D3DCompile](/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dcompile) | Introduced into d3dcompiler_47.dll in 10.0.10240. |
| [D3DCompile2](/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dcompile2) | Introduced into d3dcompiler_47.dll in 10.0.10240. |
| [D3DCompileFromFile](/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dcompilefromfile) | Introduced into d3dcompiler_47.dll in 10.0.10240. |
| [D3DCompressShaders](/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dcompressshaders) | Introduced into d3dcompiler_47.dll in 10.0.10240. |
| [D3DCreateBlob](/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dcreateblob) | Introduced into d3dcompiler_47.dll in 10.0.10240. |
| [D3DCreateFunctionLinkingGraph](/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dcreatefunctionlinkinggraph) | Introduced into d3dcompiler_47.dll in 10.0.10240. |
| [D3DCreateLinker](/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dcreatelinker) | Introduced into d3dcompiler_47.dll in 10.0.10240. |
| [D3DDecompressShaders](/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3ddecompressshaders) | Introduced into d3dcompiler_47.dll in 10.0.10240. |
| [D3DDisassemble](/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3ddisassemble) | Introduced into d3dcompiler_47.dll in 10.0.10240. |
| [D3DDisassemble11Trace](/windows/win32/api/d3d11shadertracing/nf-d3d11shadertracing-d3ddisassemble11trace) | Introduced into d3dcompiler_47.dll in 10.0.10240. |
| [D3DDisassembleRegion](/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3ddisassembleregion) | Introduced into d3dcompiler_47.dll in 10.0.10240. |
| [D3DGetBlobPart](/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dgetblobpart) | Introduced into d3dcompiler_47.dll in 10.0.10240. |
| [D3DGetDebugInfo](/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dgetdebuginfo) | Introduced into d3dcompiler_47.dll in 10.0.10240. |
| [D3DGetInputAndOutputSignatureBlob](/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dgetinputandoutputsignatureblob) | Introduced into d3dcompiler_47.dll in 10.0.10240. |
| [D3DGetInputSignatureBlob](/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dgetinputsignatureblob) | Introduced into d3dcompiler_47.dll in 10.0.10240. |
| [D3DGetOutputSignatureBlob](/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dgetoutputsignatureblob) | Introduced into d3dcompiler_47.dll in 10.0.10240. |
| [D3DGetTraceInstructionOffsets](/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dgettraceinstructionoffsets) | Introduced into d3dcompiler_47.dll in 10.0.10240. |
| [D3DLoadModule](/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dloadmodule) | Introduced into d3dcompiler_47.dll in 10.0.10240. |
| [D3DPreprocess](/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dpreprocess) | Introduced into d3dcompiler_47.dll in 10.0.10240. |
| [D3DReadFileToBlob](/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dreadfiletoblob) | Introduced into d3dcompiler_47.dll in 10.0.10240. |
| [D3DReflect](/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dreflect) | Introduced into d3dcompiler_47.dll in 10.0.10240. |
| [D3DReflectLibrary](/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dreflectlibrary) | Introduced into d3dcompiler_47.dll in 10.0.10240. |
| [D3DSetBlobPart](/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dsetblobpart) | Introduced into d3dcompiler_47.dll in 10.0.10240. |
| [D3DStripShader](/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dstripshader) | Introduced into d3dcompiler_47.dll in 10.0.10240. |
| [D3DWriteBlobToFile](/windows/win32/api/d3dcompiler/nf-d3dcompiler-d3dwriteblobtofile) | Introduced into d3dcompiler_47.dll in 10.0.10240. |


## APIs from deviceaccess.dll

| API | Requirements |
| -----| --------------|
| [CreateDeviceAccessInstance](/windows/win32/api/deviceaccess/nf-deviceaccess-createdeviceaccessinstance) | Introduced into deviceaccess.dll in 10.0.10240. |


## APIs from dhcpcsvc.dll

| API | Requirements |
| -----| --------------|
| [DhcpCApiCleanup](/windows/win32/api/dhcpcsdk/nf-dhcpcsdk-dhcpcapicleanup) | Introduced into dhcpcsvc.dll in 10.0.10240. |
| [DhcpCApiInitialize](/windows/win32/api/dhcpcsdk/nf-dhcpcsdk-dhcpcapiinitialize) | Introduced into dhcpcsvc.dll in 10.0.10240. |
| [DhcpRequestParams](/windows/win32/api/dhcpcsdk/nf-dhcpcsdk-dhcprequestparams) | Introduced into dhcpcsvc.dll in 10.0.10240. |


## APIs from dhcpcsvc6.dll

| API | Requirements |
| -----| --------------|
| [Dhcpv6CApiCleanup](/windows/win32/api/dhcpv6csdk/nf-dhcpv6csdk-dhcpv6capicleanup) | Introduced into dhcpcsvc6.dll in 10.0.10240. |
| [Dhcpv6CApiInitialize](/windows/win32/api/dhcpv6csdk/nf-dhcpv6csdk-dhcpv6capiinitialize) | Introduced into dhcpcsvc6.dll in 10.0.10240. |
| [Dhcpv6RequestParams](/windows/win32/api/dhcpv6csdk/nf-dhcpv6csdk-dhcpv6requestparams) | Introduced into dhcpcsvc6.dll in 10.0.10240. |


## APIs from dwrite.dll

| API | Requirements |
| -----| --------------|
| [DWriteCreateFactory](/windows/win32/api/dwrite/nf-dwrite-dwritecreatefactory) | Introduced into dwrite.dll in 10.0.10240. |


## APIs from dxgi.dll

| API | Requirements |
| -----| --------------|
| [CreateDXGIFactory1](/windows/win32/api/dxgi/nf-dxgi-createdxgifactory1) | Introduced into dxgi.dll in 10.0.10240. |
| [CreateDXGIFactory2](/windows/win32/api/dxgi1_3/nf-dxgi1_3-createdxgifactory2) | Introduced into dxgi.dll in 10.0.10240. |


## APIs from esent.dll

| API | Requirements |
| -----| --------------|
| [JetAddColumnW](/windows/win32/extensible-storage-engine/jetaddcolumn-function) | Introduced into esent.dll in 10.0.10240. |
| [JetAttachDatabase2W](/windows/win32/extensible-storage-engine/jetattachdatabase2-function) | Introduced into esent.dll in 10.0.10240. |
| [JetBackupInstanceW](/windows/win32/extensible-storage-engine/jetbackupinstance-function) | Introduced into esent.dll in 10.0.10240. |
| [JetBeginSessionW](/windows/win32/extensible-storage-engine/jetbeginsession-function) | Introduced into esent.dll in 10.0.10240. |
| [JetBeginTransaction3](/windows/win32/extensible-storage-engine/jetbegintransaction3-function) | Introduced into esent.dll in 10.0.10240. |
| [JetCloseDatabase](/windows/win32/extensible-storage-engine/jetclosedatabase-function) | Introduced into esent.dll in 10.0.10240. |
| [JetCloseTable](/windows/win32/extensible-storage-engine/jetclosetable-function) | Introduced into esent.dll in 10.0.10240. |
| [JetCommitTransaction](/windows/win32/extensible-storage-engine/jetcommittransaction-function) | Introduced into esent.dll in 10.0.10240. |
| [JetCommitTransaction2](/windows/win32/extensible-storage-engine/jetcommittransaction2-function) | Introduced into esent.dll in 10.0.10240. |
| [JetCreateDatabase2W](/windows/win32/extensible-storage-engine/jetcreatedatabase2-function) | Introduced into esent.dll in 10.0.10240. |
| [JetCreateIndex4W](/windows/win32/extensible-storage-engine/jetcreateindex4w-function) | Introduced into esent.dll in 10.0.10240. |
| [JetCreateInstance2W](/windows/win32/extensible-storage-engine/jetcreateinstance2-function) | Introduced into esent.dll in 10.0.10240. |
| [JetCreateTableColumnIndex4W](/windows/win32/extensible-storage-engine/jetcreatetablecolumnindex4w-function) | Introduced into esent.dll in 10.0.10240. |
| [JetDefragment2W](/windows/win32/extensible-storage-engine/jetdefragment2-function) | Introduced into esent.dll in 10.0.10240. |
| [JetDelete](/windows/win32/extensible-storage-engine/jetdelete-function) | Introduced into esent.dll in 10.0.10240. |
| [JetDeleteColumn2W](/windows/win32/extensible-storage-engine/jetdeletecolumn2-function) | Introduced into esent.dll in 10.0.10240. |
| [JetDeleteIndexW](/windows/win32/extensible-storage-engine/jetdeleteindex-function) | Introduced into esent.dll in 10.0.10240. |
| [JetDeleteTableW](/windows/win32/extensible-storage-engine/jetdeletetable-function) | Introduced into esent.dll in 10.0.10240. |
| [JetDetachDatabase2W](/windows/win32/extensible-storage-engine/jetdetachdatabase2-function) | Introduced into esent.dll in 10.0.10240. |
| [JetEndSession](/windows/win32/extensible-storage-engine/jetendsession-function) | Introduced into esent.dll in 10.0.10240. |
| [JetEnumerateColumns](/windows/win32/extensible-storage-engine/jetenumeratecolumns-function) | Introduced into esent.dll in 10.0.10240. |
| [JetEscrowUpdate](/windows/win32/extensible-storage-engine/jetescrowupdate-function) | Introduced into esent.dll in 10.0.10240. |
| [JetGetBookmark](/windows/win32/extensible-storage-engine/jetgetbookmark-function) | Introduced into esent.dll in 10.0.10240. |
| [JetGetColumnInfoW](/windows/win32/extensible-storage-engine/jetgetcolumninfo-function) | Introduced into esent.dll in 10.0.10240. |
| [JetGetCurrentIndexW](/windows/win32/extensible-storage-engine/jetgetcurrentindex-function) | Introduced into esent.dll in 10.0.10240. |
| [JetGetDatabaseFileInfoW](/windows/win32/extensible-storage-engine/jetgetdatabasefileinfo-function) | Introduced into esent.dll in 10.0.10240. |
| [JetGetDatabaseInfoW](/windows/win32/extensible-storage-engine/jetgetdatabaseinfo-function) | Introduced into esent.dll in 10.0.10240. |
| [JetGetErrorInfoW](/windows/win32/extensible-storage-engine/jetgeterrorinfow-function) | Introduced into esent.dll in 10.0.10240. |
| [JetGetIndexInfoW](/windows/win32/extensible-storage-engine/jetgetindexinfo-function) | Introduced into esent.dll in 10.0.10240. |
| [JetGetObjectInfoW](/windows/win32/extensible-storage-engine/jetgetobjectinfo-function) | Introduced into esent.dll in 10.0.10240. |
| [JetGetRecordPosition](/windows/win32/extensible-storage-engine/jetgetrecordposition-function) | Introduced into esent.dll in 10.0.10240. |
| [JetGetSecondaryIndexBookmark](/windows/win32/extensible-storage-engine/jetgetsecondaryindexbookmark-function) | Introduced into esent.dll in 10.0.10240. |
| [JetGetSessionParameter](/windows/win32/extensible-storage-engine/jetgetsessionparameter-function) | Introduced into esent.dll in 10.0.10240. |
| [JetGetSystemParameterW](/windows/win32/extensible-storage-engine/jetgetsystemparameter-function) | Introduced into esent.dll in 10.0.10240. |
| [JetGetTableColumnInfoW](/windows/win32/extensible-storage-engine/jetgettablecolumninfo-function) | Introduced into esent.dll in 10.0.10240. |
| [JetGetTableIndexInfoW](/windows/win32/extensible-storage-engine/jetgettableindexinfo-function) | Introduced into esent.dll in 10.0.10240. |
| [JetGetTableInfoW](/windows/win32/extensible-storage-engine/jetgettableinfo-function) | Introduced into esent.dll in 10.0.10240. |
| [JetGetThreadStats](/windows/win32/extensible-storage-engine/jetgetthreadstats-function) | Introduced into esent.dll in 10.0.10240. |
| [JetGotoBookmark](/windows/win32/extensible-storage-engine/jetgotobookmark-function) | Introduced into esent.dll in 10.0.10240. |
| [JetGotoPosition](/windows/win32/extensible-storage-engine/jetgotoposition-function) | Introduced into esent.dll in 10.0.10240. |
| [JetGotoSecondaryIndexBookmark](/windows/win32/extensible-storage-engine/jetgotosecondaryindexbookmark-function) | Introduced into esent.dll in 10.0.10240. |
| [JetIndexRecordCount](/windows/win32/extensible-storage-engine/jetindexrecordcount-function) | Introduced into esent.dll in 10.0.10240. |
| [JetInit3W](/windows/win32/extensible-storage-engine/jetinit3-function) | Introduced into esent.dll in 10.0.10240. |
| [JetIntersectIndexes](/windows/win32/extensible-storage-engine/jetintersectindexes-function) | Introduced into esent.dll in 10.0.10240. |
| [JetMakeKey](/windows/win32/extensible-storage-engine/jetmakekey-function) | Introduced into esent.dll in 10.0.10240. |
| [JetMove](/windows/win32/extensible-storage-engine/jetmove-function) | Introduced into esent.dll in 10.0.10240. |
| [JetOpenDatabaseW](/windows/win32/extensible-storage-engine/jetopendatabase-function) | Introduced into esent.dll in 10.0.10240. |
| [JetOpenTableW](/windows/win32/extensible-storage-engine/jetopentable-function) | Introduced into esent.dll in 10.0.10240. |
| [JetOpenTemporaryTable2](/windows/win32/extensible-storage-engine/jetopentemptable2-function) | Introduced into esent.dll in 10.0.10240. |
| [JetOpenTempTable3](/windows/win32/extensible-storage-engine/jetopentemptable3-function) | Introduced into esent.dll in 10.0.10240. |
| [JetPrepareUpdate](/windows/win32/extensible-storage-engine/jetprepareupdate-function) | Introduced into esent.dll in 10.0.10240. |
| [JetPrereadIndexRanges](/windows/win32/extensible-storage-engine/jetprereadindexranges-function) | Introduced into esent.dll in 10.0.10240. |
| [JetPrereadKeys](/windows/win32/extensible-storage-engine/jetprereadkeys-function) | Introduced into esent.dll in 10.0.10240. |
| [JetRegisterCallback](/windows/win32/extensible-storage-engine/jetregistercallback-function) | Introduced into esent.dll in 10.0.10240. |
| [JetRenameColumnW](/windows/win32/extensible-storage-engine/jetrenamecolumn-function) | Introduced into esent.dll in 10.0.10240. |
| [JetRenameTableW](/windows/win32/extensible-storage-engine/jetrenametable-function) | Introduced into esent.dll in 10.0.10240. |
| [JetResetSessionContext](/windows/win32/extensible-storage-engine/jetresetsessioncontext-function) | Introduced into esent.dll in 10.0.10240. |
| [JetResetTableSequential](/windows/win32/extensible-storage-engine/jetresettablesequential-function) | Introduced into esent.dll in 10.0.10240. |
| [JetResizeDatabase](/windows/win32/extensible-storage-engine/jetresizedatabase-function) | Introduced into esent.dll in 10.0.10240. |
| [JetRestoreInstanceW](/windows/win32/extensible-storage-engine/jetrestoreinstance-function) | Introduced into esent.dll in 10.0.10240. |
| [JetRetrieveColumn](/windows/win32/extensible-storage-engine/jetretrievecolumn-function) | Introduced into esent.dll in 10.0.10240. |
| [JetRetrieveColumns](/windows/win32/extensible-storage-engine/jetretrievecolumns-function) | Introduced into esent.dll in 10.0.10240. |
| [JetRetrieveKey](/windows/win32/extensible-storage-engine/jetretrievekey-function) | Introduced into esent.dll in 10.0.10240. |
| [JetRollback](/windows/win32/extensible-storage-engine/jetrollback-function) | Introduced into esent.dll in 10.0.10240. |
| [JetSeek](/windows/win32/extensible-storage-engine/jetseek-function) | Introduced into esent.dll in 10.0.10240. |
| [JetSetColumn](/windows/win32/extensible-storage-engine/jetsetcolumn-function) | Introduced into esent.dll in 10.0.10240. |
| [JetSetColumns](/windows/win32/extensible-storage-engine/jetsetcolumns-function) | Introduced into esent.dll in 10.0.10240. |
| [JetSetCurrentIndex4W](/windows/win32/extensible-storage-engine/jetsetcurrentindex4-function) | Introduced into esent.dll in 10.0.10240. |
| [JetSetCursorFilter](/windows/win32/extensible-storage-engine/jetsetcursorfilter-function) | Introduced into esent.dll in 10.0.10240. |
| [JetSetIndexRange](/windows/win32/extensible-storage-engine/jetsetindexrange-function) | Introduced into esent.dll in 10.0.10240. |
| [JetSetSessionContext](/windows/win32/extensible-storage-engine/jetsetsessioncontext-function) | Introduced into esent.dll in 10.0.10240. |
| [JetSetSessionParameter](/windows/win32/extensible-storage-engine/jetsetsessionparameter-function) | Introduced into esent.dll in 10.0.10240. |
| [JetSetSystemParameterW](/windows/win32/extensible-storage-engine/jetsetsystemparameter-function) | Introduced into esent.dll in 10.0.10240. |
| [JetSetTableSequential](/windows/win32/extensible-storage-engine/jetsettablesequential-function) | Introduced into esent.dll in 10.0.10240. |
| [JetStopBackupInstance](/windows/win32/extensible-storage-engine/jetstopbackupinstance-function) | Introduced into esent.dll in 10.0.10240. |
| JetStopServiceInstance2 | Introduced into esent.dll in 10.0.10240. |
| [JetTerm2](/windows/win32/extensible-storage-engine/jetterm2-function) | Introduced into esent.dll in 10.0.10240. |
| [JetUnregisterCallback](/windows/win32/extensible-storage-engine/jetunregistercallback-function) | Introduced into esent.dll in 10.0.10240. |
| [JetUpdate2](/windows/win32/extensible-storage-engine/jetupdate2-function) | Introduced into esent.dll in 10.0.10240. |
| JetAddColumn | Introduced into esent.dll in 10.0.16299. Removed in 10.0.17134. |
| JetAttachDatabase2 | Introduced into esent.dll in 10.0.16299. Removed in 10.0.17134. |
| JetBackupInstance | Introduced into esent.dll in 10.0.16299. Removed in 10.0.17134. |
| JetBeginSession | Introduced into esent.dll in 10.0.16299. Removed in 10.0.17134. |
| JetCreateDatabase2 | Introduced into esent.dll in 10.0.16299. Removed in 10.0.17134. |
| JetCreateInstance2 | Introduced into esent.dll in 10.0.16299. Removed in 10.0.17134. |
| JetDefragment2 | Introduced into esent.dll in 10.0.16299. Removed in 10.0.17134. |
| JetDeleteColumn2 | Introduced into esent.dll in 10.0.16299. Removed in 10.0.17134. |
| JetDeleteIndex | Introduced into esent.dll in 10.0.16299. Removed in 10.0.17134. |
| JetDeleteTable | Introduced into esent.dll in 10.0.16299. Removed in 10.0.17134. |
| JetDetachDatabase2 | Introduced into esent.dll in 10.0.16299. Removed in 10.0.17134. |
| JetGetColumnInfo | Introduced into esent.dll in 10.0.16299. Removed in 10.0.17134. |
| JetGetCurrentIndex | Introduced into esent.dll in 10.0.16299. Removed in 10.0.17134. |
| JetGetDatabaseFileInfo | Introduced into esent.dll in 10.0.16299. Removed in 10.0.17134. |
| JetGetDatabaseInfo | Introduced into esent.dll in 10.0.16299. Removed in 10.0.17134. |
| JetGetIndexInfo | Introduced into esent.dll in 10.0.16299. Removed in 10.0.17134. |
| JetGetObjectInfo | Introduced into esent.dll in 10.0.16299. Removed in 10.0.17134. |
| JetGetSystemParameter | Introduced into esent.dll in 10.0.16299. Removed in 10.0.17134. |
| JetGetTableColumnInfo | Introduced into esent.dll in 10.0.16299. Removed in 10.0.17134. |
| JetGetTableIndexInfo | Introduced into esent.dll in 10.0.16299. Removed in 10.0.17134. |
| JetGetTableInfo | Introduced into esent.dll in 10.0.16299. Removed in 10.0.17134. |
| JetInit3 | Introduced into esent.dll in 10.0.16299. Removed in 10.0.17134. |
| JetOpenDatabase | Introduced into esent.dll in 10.0.16299. Removed in 10.0.17134. |
| JetOpenTable | Introduced into esent.dll in 10.0.16299. Removed in 10.0.17134. |
| JetRenameColumn | Introduced into esent.dll in 10.0.16299. Removed in 10.0.17134. |
| JetRenameTable | Introduced into esent.dll in 10.0.16299. Removed in 10.0.17134. |
| JetRestoreInstance | Introduced into esent.dll in 10.0.16299. Removed in 10.0.17134. |
| JetSetCurrentIndex4 | Introduced into esent.dll in 10.0.16299. Removed in 10.0.17134. |
| JetSetSystemParameter | Introduced into esent.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from hrtfapo.dll

| API | Requirements |
| -----| --------------|
| [CreateHrtfApo](/windows/win32/api/hrtfapoapi/nf-hrtfapoapi-createhrtfapo) | Introduced into hrtfapo.dll in 10.0.10240. |


## APIs from mf.dll

| API | Requirements |
| -----| --------------|
| [MFCreateAggregateSource](/windows/win32/api/mfidl/nf-mfidl-mfcreateaggregatesource) | Introduced into mf.dll in 10.0.10240. |
| [MFCreateProtectedEnvironmentAccess](/windows/win32/api/mfidl/nf-mfidl-mfcreateprotectedenvironmentaccess) | Introduced into mf.dll in 10.0.10240. |
| [MFGetLocalId](/windows/win32/api/mfidl/nf-mfidl-mfgetlocalid) | Introduced into mf.dll in 10.0.10240. |
| [MFGetService](/windows/win32/api/mfidl/nf-mfidl-mfgetservice) | Introduced into mf.dll in 10.0.10240. |
| [MFGetSystemId](/windows/win32/api/mfidl/nf-mfidl-mfgetsystemid) | Introduced into mf.dll in 10.0.10240. |
| [MFLoadSignedLibrary](/windows/win32/api/mfidl/nf-mfidl-mfloadsignedlibrary) | Introduced into mf.dll in 10.0.10240. |
| [MFCreateASFContentInfo](/windows/win32/api/wmcontainer/nf-wmcontainer-mfcreateasfcontentinfo) | Introduced into mf.dll in 10.0.16299. |
| [MFCreateASFIndexer](/windows/win32/api/wmcontainer/nf-wmcontainer-mfcreateasfindexer) | Introduced into mf.dll in 10.0.16299. |
| [MFCreateASFIndexerByteStream](/windows/win32/api/wmcontainer/nf-wmcontainer-mfcreateasfindexerbytestream) | Introduced into mf.dll in 10.0.16299. |
| [MFCreateASFSplitter](/windows/win32/api/wmcontainer/nf-wmcontainer-mfcreateasfsplitter) | Introduced into mf.dll in 10.0.16299. |
| [MFCreateAudioRendererActivate](/windows/win32/api/mfidl/nf-mfidl-mfcreateaudiorendereractivate) | Introduced into mf.dll in 10.0.16299. |
| [MFCreatePMPMediaSession](/windows/win32/api/mfidl/nf-mfidl-mfcreatepmpmediasession) | Introduced into mf.dll in 10.0.16299. |
| [MFCreatePresentationClock](/windows/win32/api/mfidl/nf-mfidl-mfcreatepresentationclock) | Introduced into mf.dll in 10.0.16299. |
| [MFCreateTopology](/windows/win32/api/mfidl/nf-mfidl-mfcreatetopology) | Introduced into mf.dll in 10.0.16299. |
| [MFCreateTopologyNode](/windows/win32/api/mfidl/nf-mfidl-mfcreatetopologynode) | Introduced into mf.dll in 10.0.16299. |


## APIs from mfplat.dll

| API | Requirements |
| -----| --------------|
| [MFAllocateSerialWorkQueue](/windows/win32/api/mfapi/nf-mfapi-mfallocateserialworkqueue) | Introduced into mfplat.dll in 10.0.10240. |
| [MFCancelWorkItem](/windows/win32/api/mfapi/nf-mfapi-mfcancelworkitem) | Introduced into mfplat.dll in 10.0.10240. |
| [MFCopyImage](/windows/win32/api/mfapi/nf-mfapi-mfcopyimage) | Introduced into mfplat.dll in 10.0.10240. |
| [MFCreate2DMediaBuffer](/windows/win32/api/mfapi/nf-mfapi-mfcreate2dmediabuffer) | Introduced into mfplat.dll in 10.0.10240. |
| [MFCreateAlignedMemoryBuffer](/windows/win32/api/mfapi/nf-mfapi-mfcreatealignedmemorybuffer) | Introduced into mfplat.dll in 10.0.10240. |
| [MFCreateAsyncResult](/windows/win32/api/mfapi/nf-mfapi-mfcreateasyncresult) | Introduced into mfplat.dll in 10.0.10240. |
| [MFCreateAttributes](/windows/win32/api/mfapi/nf-mfapi-mfcreateattributes) | Introduced into mfplat.dll in 10.0.10240. |
| [MFCreateCollection](/windows/win32/api/mfapi/nf-mfapi-mfcreatecollection) | Introduced into mfplat.dll in 10.0.10240. |
| [MFCreateContentDecryptorContext](/windows/win32/api/mfidl/nf-mfidl-mfcreatecontentdecryptorcontext) | Introduced into mfplat.dll in 10.0.10240. |
| [MFCreateContentProtectionDevice](/windows/win32/api/mfidl/nf-mfidl-mfcreatecontentprotectiondevice) | Introduced into mfplat.dll in 10.0.10240. |
| [MFCreateDXGIDeviceManager](/windows/win32/api/mfapi/nf-mfapi-mfcreatedxgidevicemanager) | Introduced into mfplat.dll in 10.0.10240. |
| [MFCreateDXGISurfaceBuffer](/windows/win32/api/mfapi/nf-mfapi-mfcreatedxgisurfacebuffer) | Introduced into mfplat.dll in 10.0.10240. |
| [MFCreateEventQueue](/windows/win32/api/mfapi/nf-mfapi-mfcreateeventqueue) | Introduced into mfplat.dll in 10.0.10240. |
| [MFCreateMediaBufferFromMediaType](/windows/win32/api/mfapi/nf-mfapi-mfcreatemediabufferfrommediatype) | Introduced into mfplat.dll in 10.0.10240. |
| [MFCreateMediaBufferWrapper](/windows/win32/api/mfapi/nf-mfapi-mfcreatemediabufferwrapper) | Introduced into mfplat.dll in 10.0.10240. |
| [MFCreateMediaEvent](/windows/win32/api/mfapi/nf-mfapi-mfcreatemediaevent) | Introduced into mfplat.dll in 10.0.10240. |
| [MFCreateMediaExtensionActivate](/windows/win32/api/mfapi/nf-mfapi-mfcreatemediaextensionactivate) | Introduced into mfplat.dll in 10.0.10240. |
| [MFCreateMediaType](/windows/win32/api/mfapi/nf-mfapi-mfcreatemediatype) | Introduced into mfplat.dll in 10.0.10240. |
| [MFCreateMediaTypeFromProperties](/windows/win32/api/mfidl/nf-mfidl-mfcreatemediatypefromproperties) | Introduced into mfplat.dll in 10.0.10240. |
| [MFCreateMemoryBuffer](/windows/win32/api/mfapi/nf-mfapi-mfcreatememorybuffer) | Introduced into mfplat.dll in 10.0.10240. |
| [MFCreateMFByteStreamOnStreamEx](/windows/win32/api/mfidl/nf-mfidl-mfcreatemfbytestreamonstreamex) | Introduced into mfplat.dll in 10.0.10240. |
| [MFCreatePresentationDescriptor](/windows/win32/api/mfidl/nf-mfidl-mfcreatepresentationdescriptor) | Introduced into mfplat.dll in 10.0.10240. |
| [MFCreatePropertiesFromMediaType](/windows/win32/api/mfidl/nf-mfidl-mfcreatepropertiesfrommediatype) | Introduced into mfplat.dll in 10.0.10240. |
| [MFCreateSample](/windows/win32/api/mfapi/nf-mfapi-mfcreatesample) | Introduced into mfplat.dll in 10.0.10240. |
| [MFCreateSourceResolver](/windows/win32/api/mfidl/nf-mfidl-mfcreatesourceresolver) | Introduced into mfplat.dll in 10.0.10240. |
| [MFCreateStreamDescriptor](/windows/win32/api/mfidl/nf-mfidl-mfcreatestreamdescriptor) | Introduced into mfplat.dll in 10.0.10240. |
| [MFCreateStreamOnMFByteStreamEx](/windows/win32/api/mfidl/nf-mfidl-mfcreatestreamonmfbytestreamex) | Introduced into mfplat.dll in 10.0.10240. |
| [MFCreateTrackedSample](/windows/win32/api/mfidl/nf-mfidl-mfcreatetrackedsample) | Introduced into mfplat.dll in 10.0.10240. |
| [MFCreateVideoSampleAllocatorEx](/windows/win32/api/mfapi/nf-mfapi-mfcreatevideosampleallocatorex) | Introduced into mfplat.dll in 10.0.10240. |
| [MFCreateWaveFormatExFromMFMediaType](/windows/win32/api/mfapi/nf-mfapi-mfcreatewaveformatexfrommfmediatype) | Introduced into mfplat.dll in 10.0.10240. |
| [MFDeserializeAttributesFromStream](/windows/win32/api/mfobjects/nf-mfobjects-mfdeserializeattributesfromstream) | Introduced into mfplat.dll in 10.0.10240. |
| [MFGetAttributesAsBlob](/windows/win32/api/mfapi/nf-mfapi-mfgetattributesasblob) | Introduced into mfplat.dll in 10.0.10240. |
| [MFGetAttributesAsBlobSize](/windows/win32/api/mfapi/nf-mfapi-mfgetattributesasblobsize) | Introduced into mfplat.dll in 10.0.10240. |
| [MFGetSystemTime](/windows/win32/api/mfidl/nf-mfidl-mfgetsystemtime) | Introduced into mfplat.dll in 10.0.10240. |
| [MFInitAttributesFromBlob](/windows/win32/api/mfapi/nf-mfapi-mfinitattributesfromblob) | Introduced into mfplat.dll in 10.0.10240. |
| [MFInitMediaTypeFromWaveFormatEx](/windows/win32/api/mfapi/nf-mfapi-mfinitmediatypefromwaveformatex) | Introduced into mfplat.dll in 10.0.10240. |
| [MFInvokeCallback](/windows/win32/api/mfapi/nf-mfapi-mfinvokecallback) | Introduced into mfplat.dll in 10.0.10240. |
| [MFIsContentProtectionDeviceSupported](/windows/win32/api/mfidl/nf-mfidl-mfiscontentprotectiondevicesupported) | Introduced into mfplat.dll in 10.0.10240. |
| [MFllMulDiv](/windows/win32/api/mfapi/nf-mfapi-mfllmuldiv) | Introduced into mfplat.dll in 10.0.10240. |
| [MFLockDXGIDeviceManager](/windows/win32/api/mfapi/nf-mfapi-mflockdxgidevicemanager) | Introduced into mfplat.dll in 10.0.10240. |
| [MFLockPlatform](/windows/win32/api/mfapi/nf-mfapi-mflockplatform) | Introduced into mfplat.dll in 10.0.10240. |
| [MFLockSharedWorkQueue](/windows/win32/api/mfapi/nf-mfapi-mflocksharedworkqueue) | Introduced into mfplat.dll in 10.0.10240. |
| [MFLockWorkQueue](/windows/win32/api/mfapi/nf-mfapi-mflockworkqueue) | Introduced into mfplat.dll in 10.0.10240. |
| [MFPutWaitingWorkItem](/windows/win32/api/mfapi/nf-mfapi-mfputwaitingworkitem) | Introduced into mfplat.dll in 10.0.10240. |
| [MFPutWorkItem2](/windows/win32/api/mfapi/nf-mfapi-mfputworkitem2) | Introduced into mfplat.dll in 10.0.10240. |
| [MFPutWorkItemEx2](/windows/win32/api/mfapi/nf-mfapi-mfputworkitemex2) | Introduced into mfplat.dll in 10.0.10240. |
| [MFSerializeAttributesToStream](/windows/win32/api/mfobjects/nf-mfobjects-mfserializeattributestostream) | Introduced into mfplat.dll in 10.0.10240. |
| [MFShutdown](/windows/win32/api/mfapi/nf-mfapi-mfshutdown) | Introduced into mfplat.dll in 10.0.10240. |
| [MFStartup](/windows/win32/api/mfapi/nf-mfapi-mfstartup) | Introduced into mfplat.dll in 10.0.10240. |
| [MFUnlockDXGIDeviceManager](/windows/win32/api/mfapi/nf-mfapi-mfunlockdxgidevicemanager) | Introduced into mfplat.dll in 10.0.10240. |
| [MFUnlockPlatform](/windows/win32/api/mfapi/nf-mfapi-mfunlockplatform) | Introduced into mfplat.dll in 10.0.10240. |
| [MFUnlockWorkQueue](/windows/win32/api/mfapi/nf-mfapi-mfunlockworkqueue) | Introduced into mfplat.dll in 10.0.10240. |
| [MFUnwrapMediaType](/windows/win32/api/mfapi/nf-mfapi-mfunwrapmediatype) | Introduced into mfplat.dll in 10.0.10240. |
| [MFWrapMediaType](/windows/win32/api/mfapi/nf-mfapi-mfwrapmediatype) | Introduced into mfplat.dll in 10.0.10240. |
| [MFCreateSystemTimeSource](/windows/win32/api/mfidl/nf-mfidl-mfcreatesystemtimesource) | Introduced into mfplat.dll in 10.0.16299. |
| [MFScheduleWorkItemEx](/windows/win32/api/mfapi/nf-mfapi-mfscheduleworkitemex) | Introduced into mfplat.dll in 10.0.16299. |
| [MFTEnumEx](/windows/win32/api/mfapi/nf-mfapi-mftenumex) | Introduced into mfplat.dll in 10.0.16299. |


## APIs from mfreadwrite.dll

| API | Requirements |
| -----| --------------|
| [MFCreateSinkWriterFromMediaSink](/windows/win32/api/mfreadwrite/nf-mfreadwrite-mfcreatesinkwriterfrommediasink) | Introduced into mfreadwrite.dll in 10.0.10240. |
| [MFCreateSinkWriterFromURL](/windows/win32/api/mfreadwrite/nf-mfreadwrite-mfcreatesinkwriterfromurl) | Introduced into mfreadwrite.dll in 10.0.10240. |
| [MFCreateSourceReaderFromByteStream](/windows/win32/api/mfreadwrite/nf-mfreadwrite-mfcreatesourcereaderfrombytestream) | Introduced into mfreadwrite.dll in 10.0.10240. |
| [MFCreateSourceReaderFromMediaSource](/windows/win32/api/mfreadwrite/nf-mfreadwrite-mfcreatesourcereaderfrommediasource) | Introduced into mfreadwrite.dll in 10.0.10240. |
| [MFCreateSourceReaderFromURL](/windows/win32/api/mfreadwrite/nf-mfreadwrite-mfcreatesourcereaderfromurl) | Introduced into mfreadwrite.dll in 10.0.10240. |


## APIs from mmdevapi.dll

| API | Requirements |
| -----| --------------|
| [ActivateAudioInterfaceAsync](/windows/win32/api/mmdeviceapi/nf-mmdeviceapi-activateaudiointerfaceasync) | Introduced into mmdevapi.dll in 10.0.10240. |


## APIs from MSAJApi.dll

| API | Requirements |
| -----| --------------|
| alljoyn_aboutdata_create | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutdata_create_empty | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutdata_create_full | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutdata_createfrommsgarg | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutdata_destroy | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutdata_getaboutdata | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutdata_getajsoftwareversion | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutdata_getannouncedaboutdata | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutdata_getappid | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutdata_getappname | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutdata_getdateofmanufacture | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutdata_getdefaultlanguage | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutdata_getdescription | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutdata_getdeviceid | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutdata_getdevicename | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutdata_getfield | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutdata_getfields | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutdata_getfieldsignature | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutdata_gethardwareversion | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutdata_getmanufacturer | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutdata_getmodelnumber | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutdata_getsoftwareversion | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutdata_getsupportedlanguages | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutdata_getsupporturl | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutdata_isfieldannounced | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutdata_isfieldlocalized | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutdata_isfieldrequired | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutdata_isvalid | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutdata_setappid | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutdata_setappid_fromstring | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutdata_setappname | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutdata_setdateofmanufacture | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutdata_setdefaultlanguage | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutdata_setdescription | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutdata_setdeviceid | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutdata_setdevicename | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutdata_setfield | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutdata_sethardwareversion | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutdata_setmanufacturer | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutdata_setmodelnumber | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutdata_setsoftwareversion | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutdata_setsupportedlanguage | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutdata_setsupporturl | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutdatalistener_create | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutdatalistener_destroy | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_abouticon_clear | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_abouticon_create | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_abouticon_destroy | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_abouticon_setcontent | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_abouticon_setcontent_frommsgarg | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_abouticon_seturl | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_abouticonobj_create | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_abouticonobj_destroy | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_abouticonproxy_create | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_abouticonproxy_destroy | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_abouticonproxy_geticon | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_abouticonproxy_getversion | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutlistener_create | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutlistener_destroy | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutobj_announce | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutobj_announce_using_datalistener | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutobj_create | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutobj_destroy | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutobj_unannounce | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutobjectdescription_clear | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutobjectdescription_create | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutobjectdescription_create_full | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutobjectdescription_createfrommsgarg | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutobjectdescription_destroy | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutobjectdescription_getinterfacepaths | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutobjectdescription_getinterfaces | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutobjectdescription_getmsgarg | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutobjectdescription_getpaths | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutobjectdescription_hasinterface | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutobjectdescription_hasinterfaceatpath | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutobjectdescription_haspath | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutproxy_create | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutproxy_destroy | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutproxy_getaboutdata | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutproxy_getobjectdescription | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_aboutproxy_getversion | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_authlistener_create | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_authlistener_destroy | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_authlistener_requestcredentialsresponse | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_authlistener_verifycredentialsresponse | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_authlistenerasync_create | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_authlistenerasync_destroy | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_addlogonentry | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_addmatch | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_advertisename | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_bindsessionport | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_canceladvertisename | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_cancelfindadvertisedname | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_cancelfindadvertisednamebytransport | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_cancelwhoimplements_interface | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_cancelwhoimplements_interfaces | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_clearkeys | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_clearkeystore | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_connect | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_create | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_create_concurrency | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_createinterface | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_createinterface_secure | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_createinterfacesfromxml | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_deleteinterface | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_destroy | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_disconnect | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_enableconcurrentcallbacks | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_enablepeersecurity | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_findadvertisedname | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_findadvertisednamebytransport | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_getalljoyndebugobj | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_getalljoynproxyobj | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_getconcurrency | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_getconnectspec | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_getdbusproxyobj | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_getglobalguidstring | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_getinterface | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_getinterfaces | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_getkeyexpiration | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_getpeerguid | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_gettimestamp | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_getuniquename | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_isconnected | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_ispeersecurityenabled | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_isstarted | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_isstopping | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_join | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_joinsession | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_joinsessionasync | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_leavesession | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_namehasowner | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_ping | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_registeraboutlistener | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_registerbuslistener | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_registerbusobject | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_registerbusobject_secure | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_registerkeystorelistener | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_registersignalhandler | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_registersignalhandlerwithrule | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_releasename | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_reloadkeystore | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_removematch | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_removesessionmember | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_requestname | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_setdaemondebug | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_setkeyexpiration | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_setlinktimeout | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_setlinktimeoutasync | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_setsessionlistener | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_start | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_stop | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_unbindsessionport | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_unregisteraboutlistener | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_unregisterallaboutlisteners | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_unregisterallhandlers | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_unregisterbuslistener | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_unregisterbusobject | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_unregistersignalhandler | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_unregistersignalhandlerwithrule | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_whoimplements_interface | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_whoimplements_interfaces | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_buslistener_create | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_buslistener_destroy | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busobject_addinterface | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busobject_addinterface_announced | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busobject_addmethodhandler | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busobject_addmethodhandlers | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busobject_cancelsessionlessmessage | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busobject_cancelsessionlessmessage_serial | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busobject_create | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busobject_destroy | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busobject_emitpropertieschanged | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busobject_emitpropertychanged | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busobject_getannouncedinterfacenames | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busobject_getbusattachment | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busobject_getname | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busobject_getpath | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busobject_issecure | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busobject_methodreply_args | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busobject_methodreply_err | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busobject_methodreply_status | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busobject_setannounceflag | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busobject_signal | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_credentials_clear | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_credentials_create | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_credentials_destroy | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_credentials_getcertchain | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_credentials_getexpiration | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_credentials_getlogonentry | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_credentials_getpassword | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_credentials_getprivateKey | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_credentials_getusername | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_credentials_isset | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_credentials_setcertchain | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_credentials_setexpiration | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_credentials_setlogonentry | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_credentials_setpassword | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_credentials_setprivatekey | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_credentials_setusername | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_getbuildinfo | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_getnumericversion | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_getversion | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_init | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_interfacedescription_activate | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_interfacedescription_addannotation | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_interfacedescription_addmember | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_interfacedescription_addmemberannotation | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_interfacedescription_addmethod | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_interfacedescription_addproperty | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_interfacedescription_addpropertyannotation | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_interfacedescription_addsignal | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_interfacedescription_eql | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_interfacedescription_getannotation | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_interfacedescription_getannotationatindex | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_interfacedescription_getannotationscount | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_interfacedescription_getmember | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_interfacedescription_getmemberannotation | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_interfacedescription_getmembers | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_interfacedescription_getmethod | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_interfacedescription_getname | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_interfacedescription_getproperties | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_interfacedescription_getproperty | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_interfacedescription_getpropertyannotation | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_interfacedescription_getsecuritypolicy | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_interfacedescription_getsignal | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_interfacedescription_hasmember | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_interfacedescription_hasproperties | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_interfacedescription_hasproperty | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_interfacedescription_introspect | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_interfacedescription_issecure | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_interfacedescription_member_eql | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_interfacedescription_member_getannotation | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_interfacedescription_member_getannotationatindex | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_interfacedescription_member_getannotationscount | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_interfacedescription_property_eql | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_interfacedescription_property_getannotation | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_interfacedescription_property_getannotationatindex | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_interfacedescription_property_getannotationscount | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_keystorelistener_create | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_keystorelistener_destroy | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_keystorelistener_getkeys | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_keystorelistener_putkeys | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_message_create | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_message_description | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_message_destroy | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_message_eql | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_message_getarg | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_message_getargs | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_message_getauthmechanism | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_message_getcallserial | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_message_getcompressiontoken | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_message_getdestination | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_message_geterrorname | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_message_getflags | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_message_getinterface | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_message_getmembername | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_message_getobjectpath | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_message_getreceiveendpointname | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_message_getreplyserial | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_message_getsender | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_message_getsessionid | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_message_getsignature | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_message_gettimestamp | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_message_gettype | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_message_isbroadcastsignal | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_message_isencrypted | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_message_isexpired | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_message_isglobalbroadcast | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_message_issessionless | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_message_isunreliable | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_message_parseargs | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_message_setendianess | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_message_tostring | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_array_create | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_array_element | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_array_get | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_array_set | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_array_set_offset | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_array_signature | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_array_tostring | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_clear | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_clone | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_copy | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_create | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_create_and_set | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_destroy | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_equal | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_get | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_get_array_element | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_get_array_elementsignature | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_get_array_numberofelements | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_get_bool | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_get_bool_array | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_get_double | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_get_double_array | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_get_int16 | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_get_int16_array | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_get_int32 | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_get_int32_array | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_get_int64 | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_get_int64_array | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_get_objectpath | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_get_signature | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_get_string | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_get_uint16 | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_get_uint16_array | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_get_uint32 | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_get_uint32_array | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_get_uint64 | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_get_uint64_array | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_get_uint8 | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_get_uint8_array | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_get_variant | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_get_variant_array | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_getdictelement | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_getkey | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_getmember | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_getnummembers | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_gettype | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_getvalue | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_hassignature | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_set | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_set_and_stabilize | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_set_bool | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_set_bool_array | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_set_double | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_set_double_array | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_set_int16 | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_set_int16_array | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_set_int32 | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_set_int32_array | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_set_int64 | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_set_int64_array | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_set_objectpath | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_set_objectpath_array | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_set_signature | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_set_signature_array | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_set_string | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_set_string_array | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_set_uint16 | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_set_uint16_array | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_set_uint32 | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_set_uint32_array | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_set_uint64 | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_set_uint64_array | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_set_uint8 | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_set_uint8_array | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_setdictentry | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_setstruct | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_signature | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_stabilize | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_msgarg_tostring | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_observer_create | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_observer_destroy | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_observer_get | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_observer_getfirst | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_observer_getnext | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_observer_registerlistener | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_observer_unregisteralllisteners | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_observer_unregisterlistener | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_observerlistener_create | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_observerlistener_destroy | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_passwordmanager_setcredentials | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_proxybusobject_addchild | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_proxybusobject_addinterface | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_proxybusobject_addinterface_by_name | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_proxybusobject_copy | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_proxybusobject_create | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_proxybusobject_create_secure | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_proxybusobject_destroy | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_proxybusobject_enablepropertycaching | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_proxybusobject_getallproperties | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_proxybusobject_getallpropertiesasync | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_proxybusobject_getchild | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_proxybusobject_getchildren | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_proxybusobject_getinterface | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_proxybusobject_getinterfaces | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_proxybusobject_getpath | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_proxybusobject_getproperty | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_proxybusobject_getpropertyasync | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_proxybusobject_getservicename | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_proxybusobject_getsessionid | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_proxybusobject_getuniquename | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_proxybusobject_implementsinterface | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_proxybusobject_introspectremoteobject | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_proxybusobject_introspectremoteobjectasync | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_proxybusobject_issecure | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_proxybusobject_isvalid | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_proxybusobject_methodcall | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_proxybusobject_methodcall_member | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_proxybusobject_methodcall_member_noreply | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_proxybusobject_methodcall_noreply | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_proxybusobject_methodcallasync | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_proxybusobject_methodcallasync_member | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_proxybusobject_parsexml | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_proxybusobject_ref_create | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_proxybusobject_ref_decref | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_proxybusobject_ref_get | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_proxybusobject_ref_incref | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_proxybusobject_registerpropertieschangedlistener | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_proxybusobject_removechild | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_proxybusobject_secureconnection | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_proxybusobject_secureconnectionasync | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_proxybusobject_setproperty | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_proxybusobject_setpropertyasync | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_proxybusobject_unregisterpropertieschangedlistener | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_sessionlistener_create | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_sessionlistener_destroy | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_sessionopts_cmp | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_sessionopts_create | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_sessionopts_destroy | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_sessionopts_get_multipoint | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_sessionopts_get_proximity | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_sessionopts_get_traffic | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_sessionopts_get_transports | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_sessionopts_iscompatible | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_sessionopts_set_multipoint | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_sessionopts_set_proximity | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_sessionopts_set_traffic | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_sessionopts_set_transports | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_sessionportlistener_create | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_sessionportlistener_destroy | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_shutdown | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_unity_deferred_callbacks_process | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_unity_set_deferred_callback_mainthread_only | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [AllJoynCloseBusHandle](/windows/win32/api/msajtransport/nf-msajtransport-alljoynclosebushandle) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [AllJoynConnectToBus](/windows/win32/api/msajtransport/nf-msajtransport-alljoynconnecttobus) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [AllJoynEnumEvents](/windows/win32/api/msajtransport/nf-msajtransport-alljoynenumevents) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [AllJoynEventSelect](/windows/win32/api/msajtransport/nf-msajtransport-alljoyneventselect) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [AllJoynReceiveFromBus](/windows/win32/api/msajtransport/nf-msajtransport-alljoynreceivefrombus) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [AllJoynSendToBus](/windows/win32/api/msajtransport/nf-msajtransport-alljoynsendtobus) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [QCC_StatusText](/previous-versions/windows/desktop/alljoyn/qcc-statustext) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_autopinger_adddestination | Introduced into MSAJApi.dll in 10.0.10586. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_autopinger_addpinggroup | Introduced into MSAJApi.dll in 10.0.10586. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_autopinger_create | Introduced into MSAJApi.dll in 10.0.10586. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_autopinger_destroy | Introduced into MSAJApi.dll in 10.0.10586. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_autopinger_pause | Introduced into MSAJApi.dll in 10.0.10586. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_autopinger_removedestination | Introduced into MSAJApi.dll in 10.0.10586. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_autopinger_removepinggroup | Introduced into MSAJApi.dll in 10.0.10586. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_autopinger_resume | Introduced into MSAJApi.dll in 10.0.10586. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_autopinger_setpinginterval | Introduced into MSAJApi.dll in 10.0.10586. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_enablepeersecuritywithpermissionconfigurationlistener | Introduced into MSAJApi.dll in 10.0.10586. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_secureconnection | Introduced into MSAJApi.dll in 10.0.10586. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_secureconnectionasync | Introduced into MSAJApi.dll in 10.0.10586. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_permissionconfigurationlistener_create | Introduced into MSAJApi.dll in 10.0.10586. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_permissionconfigurationlistener_destroy | Introduced into MSAJApi.dll in 10.0.10586. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_pinglistener_create | Introduced into MSAJApi.dll in 10.0.10586. Moved into msajapi.dll in 10.0.14393. |
| alljoyn_pinglistener_destroy | Introduced into MSAJApi.dll in 10.0.10586. Moved into msajapi.dll in 10.0.14393. |


## APIs from mscoree.dll

| API | Requirements |
| -----| --------------|
| [_CorDllMain](/previous-versions/dotnet/netframework-3.0/9yk0t8cf(v=vs.85)) | Introduced into mscoree.dll in 10.0.10240. Removed in 10.0.16299. |
| [_CorExeMain](/previous-versions/dotnet/netframework-3.0/xh0859k0(v=vs.85)) | Introduced into mscoree.dll in 10.0.10240. Removed in 10.0.16299. |
| [MetaDataGetDispenser](/windows/win32/api/rometadata/nf-rometadata-metadatagetdispenser) | Introduced into mscoree.dll in 10.0.10240. Moved into rometadata.dll in 10.0.10586. |


## APIs from mswsock.dll

| API | Requirements |
| -----| --------------|
| [AcceptEx](/windows/win32/api/mswsock/nf-mswsock-acceptex) | Introduced into mswsock.dll in 10.0.10240. |
| [GetAcceptExSockaddrs](/windows/win32/api/mswsock/nf-mswsock-getacceptexsockaddrs) | Introduced into mswsock.dll in 10.0.10240. |
| [TransmitFile](/windows/win32/api/mswsock/nf-mswsock-transmitfile) | Introduced into mswsock.dll in 10.0.10240. |


## APIs from ncrypt.dll

| API | Requirements |
| -----| --------------|
| [BCryptCloseAlgorithmProvider](/windows/win32/api/bcrypt/nf-bcrypt-bcryptclosealgorithmprovider) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptCreateHash](/windows/win32/api/bcrypt/nf-bcrypt-bcryptcreatehash) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptDecrypt](/windows/win32/api/bcrypt/nf-bcrypt-bcryptdecrypt) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptDeriveKey](/windows/win32/api/bcrypt/nf-bcrypt-bcryptderivekey) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptDeriveKeyCapi](/windows/win32/api/bcrypt/nf-bcrypt-bcryptderivekeycapi) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptDeriveKeyPBKDF2](/windows/win32/api/bcrypt/nf-bcrypt-bcryptderivekeypbkdf2) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptDestroyHash](/windows/win32/api/bcrypt/nf-bcrypt-bcryptdestroyhash) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptDestroyKey](/windows/win32/api/bcrypt/nf-bcrypt-bcryptdestroykey) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptDestroySecret](/windows/win32/api/bcrypt/nf-bcrypt-bcryptdestroysecret) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptDuplicateHash](/windows/win32/api/bcrypt/nf-bcrypt-bcryptduplicatehash) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptDuplicateKey](/windows/win32/api/bcrypt/nf-bcrypt-bcryptduplicatekey) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptEncrypt](/windows/win32/api/bcrypt/nf-bcrypt-bcryptencrypt) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptEnumAlgorithms](/windows/win32/api/bcrypt/nf-bcrypt-bcryptenumalgorithms) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptEnumProviders](/windows/win32/api/bcrypt/nf-bcrypt-bcryptenumproviders) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptExportKey](/windows/win32/api/bcrypt/nf-bcrypt-bcryptexportkey) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptFinalizeKeyPair](/windows/win32/api/bcrypt/nf-bcrypt-bcryptfinalizekeypair) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptFinishHash](/windows/win32/api/bcrypt/nf-bcrypt-bcryptfinishhash) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptFreeBuffer](/windows/win32/api/bcrypt/nf-bcrypt-bcryptfreebuffer) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptGenerateKeyPair](/windows/win32/api/bcrypt/nf-bcrypt-bcryptgeneratekeypair) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptGenerateSymmetricKey](/windows/win32/api/bcrypt/nf-bcrypt-bcryptgeneratesymmetrickey) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptGenRandom](/windows/win32/api/bcrypt/nf-bcrypt-bcryptgenrandom) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptGetProperty](/windows/win32/api/bcrypt/nf-bcrypt-bcryptgetproperty) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptHash](/windows/win32/api/bcrypt/nf-bcrypt-bcrypthash) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptHashData](/windows/win32/api/bcrypt/nf-bcrypt-bcrypthashdata) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptImportKey](/windows/win32/api/bcrypt/nf-bcrypt-bcryptimportkey) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptImportKeyPair](/windows/win32/api/bcrypt/nf-bcrypt-bcryptimportkeypair) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptKeyDerivation](/windows/win32/api/bcrypt/nf-bcrypt-bcryptkeyderivation) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptOpenAlgorithmProvider](/windows/win32/api/bcrypt/nf-bcrypt-bcryptopenalgorithmprovider) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptSecretAgreement](/windows/win32/api/bcrypt/nf-bcrypt-bcryptsecretagreement) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptSetProperty](/windows/win32/api/bcrypt/nf-bcrypt-bcryptsetproperty) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptSignHash](/windows/win32/api/bcrypt/nf-bcrypt-bcryptsignhash) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptVerifySignature](/windows/win32/api/bcrypt/nf-bcrypt-bcryptverifysignature) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [NCryptCreateClaim](/windows/win32/api/ncrypt/nf-ncrypt-ncryptcreateclaim) | Introduced into ncrypt.dll in 10.0.10240. |
| [NCryptCreatePersistedKey](/windows/win32/api/ncrypt/nf-ncrypt-ncryptcreatepersistedkey) | Introduced into ncrypt.dll in 10.0.10240. |
| [NCryptDecrypt](/windows/win32/api/ncrypt/nf-ncrypt-ncryptdecrypt) | Introduced into ncrypt.dll in 10.0.10240. |
| [NCryptDeleteKey](/windows/win32/api/ncrypt/nf-ncrypt-ncryptdeletekey) | Introduced into ncrypt.dll in 10.0.10240. |
| [NCryptDeriveKey](/windows/win32/api/ncrypt/nf-ncrypt-ncryptderivekey) | Introduced into ncrypt.dll in 10.0.10240. |
| [NCryptEncrypt](/windows/win32/api/ncrypt/nf-ncrypt-ncryptencrypt) | Introduced into ncrypt.dll in 10.0.10240. |
| [NCryptEnumAlgorithms](/windows/win32/api/ncrypt/nf-ncrypt-ncryptenumalgorithms) | Introduced into ncrypt.dll in 10.0.10240. |
| [NCryptEnumKeys](/windows/win32/api/ncrypt/nf-ncrypt-ncryptenumkeys) | Introduced into ncrypt.dll in 10.0.10240. |
| [NCryptExportKey](/windows/win32/api/ncrypt/nf-ncrypt-ncryptexportkey) | Introduced into ncrypt.dll in 10.0.10240. |
| [NCryptFinalizeKey](/windows/win32/api/ncrypt/nf-ncrypt-ncryptfinalizekey) | Introduced into ncrypt.dll in 10.0.10240. |
| [NCryptFreeBuffer](/windows/win32/api/ncrypt/nf-ncrypt-ncryptfreebuffer) | Introduced into ncrypt.dll in 10.0.10240. |
| [NCryptFreeObject](/windows/win32/api/ncrypt/nf-ncrypt-ncryptfreeobject) | Introduced into ncrypt.dll in 10.0.10240. |
| [NCryptGetProperty](/windows/win32/api/ncrypt/nf-ncrypt-ncryptgetproperty) | Introduced into ncrypt.dll in 10.0.10240. |
| [NCryptImportKey](/windows/win32/api/ncrypt/nf-ncrypt-ncryptimportkey) | Introduced into ncrypt.dll in 10.0.10240. |
| [NCryptIsAlgSupported](/windows/win32/api/ncrypt/nf-ncrypt-ncryptisalgsupported) | Introduced into ncrypt.dll in 10.0.10240. |
| [NCryptKeyDerivation](/windows/win32/api/ncrypt/nf-ncrypt-ncryptkeyderivation) | Introduced into ncrypt.dll in 10.0.10240. |
| [NCryptOpenKey](/windows/win32/api/ncrypt/nf-ncrypt-ncryptopenkey) | Introduced into ncrypt.dll in 10.0.10240. |
| [NCryptOpenStorageProvider](/windows/win32/api/ncrypt/nf-ncrypt-ncryptopenstorageprovider) | Introduced into ncrypt.dll in 10.0.10240. |
| [NCryptSecretAgreement](/windows/win32/api/ncrypt/nf-ncrypt-ncryptsecretagreement) | Introduced into ncrypt.dll in 10.0.10240. |
| [NCryptSetProperty](/windows/win32/api/ncrypt/nf-ncrypt-ncryptsetproperty) | Introduced into ncrypt.dll in 10.0.10240. |
| [NCryptSignHash](/windows/win32/api/ncrypt/nf-ncrypt-ncryptsignhash) | Introduced into ncrypt.dll in 10.0.10240. |
| [NCryptVerifyClaim](/windows/win32/api/ncrypt/nf-ncrypt-ncryptverifyclaim) | Introduced into ncrypt.dll in 10.0.10240. |
| [NCryptVerifySignature](/windows/win32/api/ncrypt/nf-ncrypt-ncryptverifysignature) | Introduced into ncrypt.dll in 10.0.10240. |


## APIs from ntdll.dll

| API | Requirements |
| -----| --------------|
| [RtlEthernetAddressToStringA](/windows/win32/api/ip2string/nf-ip2string-rtlethernetaddresstostringa) | Introduced into ntdll.dll in 10.0.10240. |
| [RtlEthernetAddressToStringW](/windows/win32/api/ip2string/nf-ip2string-rtlethernetaddresstostringa) | Introduced into ntdll.dll in 10.0.10240. |
| [RtlEthernetStringToAddressA](/windows/win32/api/ip2string/nf-ip2string-rtlethernetstringtoaddressa) | Introduced into ntdll.dll in 10.0.10240. |
| [RtlEthernetStringToAddressW](/windows/win32/api/ip2string/nf-ip2string-rtlethernetstringtoaddressa) | Introduced into ntdll.dll in 10.0.10240. |
| [RtlIpv4AddressToStringA](/windows/win32/api/ip2string/nf-ip2string-rtlipv4addresstostringa) | Introduced into ntdll.dll in 10.0.10240. |
| [RtlIpv4AddressToStringExA](/windows/win32/api/ip2string/nf-ip2string-rtlipv4addresstostringexw) | Introduced into ntdll.dll in 10.0.10240. |
| [RtlIpv4AddressToStringExW](/windows/win32/api/ip2string/nf-ip2string-rtlipv4addresstostringexw) | Introduced into ntdll.dll in 10.0.10240. |
| [RtlIpv4AddressToStringW](/windows/win32/api/ip2string/nf-ip2string-rtlipv4addresstostringa) | Introduced into ntdll.dll in 10.0.10240. |
| [RtlIpv4StringToAddressA](/windows/win32/api/ip2string/nf-ip2string-rtlipv4stringtoaddressa) | Introduced into ntdll.dll in 10.0.10240. |
| [RtlIpv4StringToAddressExA](/windows/win32/api/ip2string/nf-ip2string-rtlipv4stringtoaddressexw) | Introduced into ntdll.dll in 10.0.10240. |
| [RtlIpv4StringToAddressExW](/windows/win32/api/ip2string/nf-ip2string-rtlipv4stringtoaddressexw) | Introduced into ntdll.dll in 10.0.10240. |
| [RtlIpv4StringToAddressW](/windows/win32/api/ip2string/nf-ip2string-rtlipv4stringtoaddressa) | Introduced into ntdll.dll in 10.0.10240. |
| [RtlIpv6AddressToStringA](/windows/win32/api/ip2string/nf-ip2string-rtlipv6addresstostringa) | Introduced into ntdll.dll in 10.0.10240. |
| [RtlIpv6AddressToStringExA](/windows/win32/api/ip2string/nf-ip2string-rtlipv6addresstostringexw) | Introduced into ntdll.dll in 10.0.10240. |
| [RtlIpv6AddressToStringExW](/windows/win32/api/ip2string/nf-ip2string-rtlipv6addresstostringexw) | Introduced into ntdll.dll in 10.0.10240. |
| [RtlIpv6AddressToStringW](/windows/win32/api/ip2string/nf-ip2string-rtlipv6addresstostringa) | Introduced into ntdll.dll in 10.0.10240. |
| [RtlIpv6StringToAddressA](/windows/win32/api/ip2string/nf-ip2string-rtlipv6stringtoaddressa) | Introduced into ntdll.dll in 10.0.10240. |
| [RtlIpv6StringToAddressExA](/windows/win32/api/ip2string/nf-ip2string-rtlipv6stringtoaddressexw) | Introduced into ntdll.dll in 10.0.10240. |
| [RtlIpv6StringToAddressExW](/windows/win32/api/ip2string/nf-ip2string-rtlipv6stringtoaddressexw) | Introduced into ntdll.dll in 10.0.10240. |
| [RtlIpv6StringToAddressW](/windows/win32/api/ip2string/nf-ip2string-rtlipv6stringtoaddressa) | Introduced into ntdll.dll in 10.0.10240. |


## APIs from oleaut32.dll

| API | Requirements |
| -----| --------------|
| [BSTR_UserFree](/windows/win32/api/oaidl/nf-oaidl-bstr_userfree) | Introduced into oleaut32.dll in 10.0.10240. |
| [BSTR_UserFree64](/windows/win32/api/oaidl/nf-oaidl-bstr_userfree64) | Introduced into oleaut32.dll in 10.0.10240. Removed in 10.0.16299. |
| [BSTR_UserMarshal](/windows/win32/api/oaidl/nf-oaidl-bstr_usermarshal) | Introduced into oleaut32.dll in 10.0.10240. |
| [BSTR_UserMarshal64](/windows/win32/api/oaidl/nf-oaidl-bstr_usermarshal64) | Introduced into oleaut32.dll in 10.0.10240. Removed in 10.0.16299. |
| [BSTR_UserSize](/windows/win32/api/oaidl/nf-oaidl-bstr_usersize) | Introduced into oleaut32.dll in 10.0.10240. |
| [BSTR_UserSize64](/windows/win32/api/oaidl/nf-oaidl-bstr_usersize64) | Introduced into oleaut32.dll in 10.0.10240. Removed in 10.0.16299. |
| [BSTR_UserUnmarshal](/windows/win32/api/oaidl/nf-oaidl-bstr_userunmarshal) | Introduced into oleaut32.dll in 10.0.10240. |
| [BSTR_UserUnmarshal64](/windows/win32/api/oaidl/nf-oaidl-bstr_userunmarshal64) | Introduced into oleaut32.dll in 10.0.10240. Removed in 10.0.16299. |
| [DispInvoke](/windows/win32/api/oleauto/nf-oleauto-dispinvoke) | Introduced into oleaut32.dll in 10.0.10240. |
| [LPSAFEARRAY_Marshal](/previous-versions/windows/desktop/automat/lpsafearray-marshal) | Introduced into oleaut32.dll in 10.0.10240. |
| [LPSAFEARRAY_Size](/previous-versions/windows/desktop/automat/lpsafearray-size) | Introduced into oleaut32.dll in 10.0.10240. |
| [LPSAFEARRAY_Unmarshal](/previous-versions/windows/desktop/automat/lpsafearray-unmarshal) | Introduced into oleaut32.dll in 10.0.10240. |
| [LPSAFEARRAY_UserFree](/windows/win32/api/wia_xp/nf-wia_xp-lpsafearray_userfree) | Introduced into oleaut32.dll in 10.0.10240. |
| [LPSAFEARRAY_UserFree64](/windows/win32/api/wia_xp/nf-wia_xp-lpsafearray_userfree64) | Introduced into oleaut32.dll in 10.0.10240. Removed in 10.0.16299. |
| [LPSAFEARRAY_UserMarshal](/windows/win32/api/wia_xp/nf-wia_xp-lpsafearray_usermarshal) | Introduced into oleaut32.dll in 10.0.10240. |
| [LPSAFEARRAY_UserMarshal64](/windows/win32/api/wia_xp/nf-wia_xp-lpsafearray_usermarshal64) | Introduced into oleaut32.dll in 10.0.10240. Removed in 10.0.16299. |
| [LPSAFEARRAY_UserSize](/windows/win32/api/wia_xp/nf-wia_xp-lpsafearray_usersize) | Introduced into oleaut32.dll in 10.0.10240. |
| [LPSAFEARRAY_UserSize64](/windows/win32/api/wia_xp/nf-wia_xp-lpsafearray_usersize64) | Introduced into oleaut32.dll in 10.0.10240. Removed in 10.0.16299. |
| [LPSAFEARRAY_UserUnmarshal](/windows/win32/api/wia_xp/nf-wia_xp-lpsafearray_userunmarshal) | Introduced into oleaut32.dll in 10.0.10240. |
| [LPSAFEARRAY_UserUnmarshal64](/windows/win32/api/wia_xp/nf-wia_xp-lpsafearray_userunmarshal64) | Introduced into oleaut32.dll in 10.0.10240. Removed in 10.0.16299. |
| [SafeArrayAccessData](/windows/win32/api/oleauto/nf-oleauto-safearrayaccessdata) | Introduced into oleaut32.dll in 10.0.10240. |
| [SafeArrayAllocData](/windows/win32/api/oleauto/nf-oleauto-safearrayallocdata) | Introduced into oleaut32.dll in 10.0.10240. |
| [SafeArrayAllocDescriptor](/windows/win32/api/oleauto/nf-oleauto-safearrayallocdescriptor) | Introduced into oleaut32.dll in 10.0.10240. |
| [SafeArrayAllocDescriptorEx](/windows/win32/api/oleauto/nf-oleauto-safearrayallocdescriptorex) | Introduced into oleaut32.dll in 10.0.10240. |
| [SafeArrayCopy](/windows/win32/api/oleauto/nf-oleauto-safearraycopy) | Introduced into oleaut32.dll in 10.0.10240. |
| [SafeArrayCopyData](/windows/win32/api/oleauto/nf-oleauto-safearraycopydata) | Introduced into oleaut32.dll in 10.0.10240. |
| [SafeArrayCreate](/windows/win32/api/oleauto/nf-oleauto-safearraycreate) | Introduced into oleaut32.dll in 10.0.10240. |
| [SafeArrayCreateEx](/windows/win32/api/oleauto/nf-oleauto-safearraycreateex) | Introduced into oleaut32.dll in 10.0.10240. |
| [SafeArrayCreateVector](/windows/win32/api/oleauto/nf-oleauto-safearraycreatevector) | Introduced into oleaut32.dll in 10.0.10240. |
| [SafeArrayCreateVectorEx](/windows/win32/api/oleauto/nf-oleauto-safearraycreatevectorex) | Introduced into oleaut32.dll in 10.0.10240. |
| [SafeArrayDestroy](/windows/win32/api/oleauto/nf-oleauto-safearraydestroy) | Introduced into oleaut32.dll in 10.0.10240. |
| [SafeArrayDestroyData](/windows/win32/api/oleauto/nf-oleauto-safearraydestroydata) | Introduced into oleaut32.dll in 10.0.10240. |
| [SafeArrayDestroyDescriptor](/windows/win32/api/oleauto/nf-oleauto-safearraydestroydescriptor) | Introduced into oleaut32.dll in 10.0.10240. |
| [SafeArrayGetDim](/windows/win32/api/oleauto/nf-oleauto-safearraygetdim) | Introduced into oleaut32.dll in 10.0.10240. |
| [SafeArrayGetElement](/windows/win32/api/oleauto/nf-oleauto-safearraygetelement) | Introduced into oleaut32.dll in 10.0.10240. |
| [SafeArrayGetElemsize](/windows/win32/api/oleauto/nf-oleauto-safearraygetelemsize) | Introduced into oleaut32.dll in 10.0.10240. |
| [SafeArrayGetIID](/windows/win32/api/oleauto/nf-oleauto-safearraygetiid) | Introduced into oleaut32.dll in 10.0.10240. |
| [SafeArrayGetLBound](/windows/win32/api/oleauto/nf-oleauto-safearraygetlbound) | Introduced into oleaut32.dll in 10.0.10240. |
| [SafeArrayGetRecordInfo](/windows/win32/api/oleauto/nf-oleauto-safearraygetrecordinfo) | Introduced into oleaut32.dll in 10.0.10240. |
| [SafeArrayGetUBound](/windows/win32/api/oleauto/nf-oleauto-safearraygetubound) | Introduced into oleaut32.dll in 10.0.10240. |
| [SafeArrayGetVartype](/windows/win32/api/oleauto/nf-oleauto-safearraygetvartype) | Introduced into oleaut32.dll in 10.0.10240. |
| [SafeArrayLock](/windows/win32/api/oleauto/nf-oleauto-safearraylock) | Introduced into oleaut32.dll in 10.0.10240. |
| [SafeArrayPtrOfIndex](/windows/win32/api/oleauto/nf-oleauto-safearrayptrofindex) | Introduced into oleaut32.dll in 10.0.10240. |
| [SafeArrayPutElement](/windows/win32/api/oleauto/nf-oleauto-safearrayputelement) | Introduced into oleaut32.dll in 10.0.10240. |
| [SafeArrayRedim](/windows/win32/api/oleauto/nf-oleauto-safearrayredim) | Introduced into oleaut32.dll in 10.0.10240. |
| [SafeArraySetIID](/windows/win32/api/oleauto/nf-oleauto-safearraysetiid) | Introduced into oleaut32.dll in 10.0.10240. |
| [SafeArraySetRecordInfo](/windows/win32/api/oleauto/nf-oleauto-safearraysetrecordinfo) | Introduced into oleaut32.dll in 10.0.10240. |
| [SafeArrayUnaccessData](/windows/win32/api/oleauto/nf-oleauto-safearrayunaccessdata) | Introduced into oleaut32.dll in 10.0.10240. |
| [SafeArrayUnlock](/windows/win32/api/oleauto/nf-oleauto-safearrayunlock) | Introduced into oleaut32.dll in 10.0.10240. |
| [SysAllocString](/windows/win32/api/oleauto/nf-oleauto-sysallocstring) | Introduced into oleaut32.dll in 10.0.10240. |
| [SysAllocStringByteLen](/windows/win32/api/oleauto/nf-oleauto-sysallocstringbytelen) | Introduced into oleaut32.dll in 10.0.10240. |
| [SysAllocStringLen](/windows/win32/api/oleauto/nf-oleauto-sysallocstringlen) | Introduced into oleaut32.dll in 10.0.10240. |
| [SysFreeString](/windows/win32/api/oleauto/nf-oleauto-sysfreestring) | Introduced into oleaut32.dll in 10.0.10240. |
| [SysReAllocString](/windows/win32/api/oleauto/nf-oleauto-sysreallocstring) | Introduced into oleaut32.dll in 10.0.10240. |
| [SysReAllocStringLen](/windows/win32/api/oleauto/nf-oleauto-sysreallocstringlen) | Introduced into oleaut32.dll in 10.0.10240. |
| [SysStringByteLen](/windows/win32/api/oleauto/nf-oleauto-sysstringbytelen) | Introduced into oleaut32.dll in 10.0.10240. |
| [SysStringLen](/windows/win32/api/oleauto/nf-oleauto-sysstringlen) | Introduced into oleaut32.dll in 10.0.10240. |
| [SystemTimeToVariantTime](/windows/win32/api/oleauto/nf-oleauto-systemtimetovarianttime) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarAbs](/windows/win32/api/oleauto/nf-oleauto-varabs) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarAdd](/windows/win32/api/oleauto/nf-oleauto-varadd) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarAnd](/windows/win32/api/oleauto/nf-oleauto-varand) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBoolFromCy](/windows/win32/api/oleauto/nf-oleauto-varboolfromcy) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBoolFromDate](/windows/win32/api/oleauto/nf-oleauto-varboolfromdate) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBoolFromDec](/windows/win32/api/oleauto/nf-oleauto-varboolfromdec) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBoolFromDisp](/windows/win32/api/oleauto/nf-oleauto-varboolfromdisp) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBoolFromI1](/windows/win32/api/oleauto/nf-oleauto-varboolfromi1) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBoolFromI2](/windows/win32/api/oleauto/nf-oleauto-varboolfromi2) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBoolFromI4](/windows/win32/api/oleauto/nf-oleauto-varboolfromi4) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBoolFromI8](/windows/win32/api/oleauto/nf-oleauto-varboolfromi8) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBoolFromR4](/windows/win32/api/oleauto/nf-oleauto-varboolfromr4) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBoolFromR8](/windows/win32/api/oleauto/nf-oleauto-varboolfromr8) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBoolFromStr](/windows/win32/api/oleauto/nf-oleauto-varboolfromstr) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBoolFromUI1](/windows/win32/api/oleauto/nf-oleauto-varboolfromui1) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBoolFromUI2](/windows/win32/api/oleauto/nf-oleauto-varboolfromui2) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBoolFromUI4](/windows/win32/api/oleauto/nf-oleauto-varboolfromui4) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBoolFromUI8](/windows/win32/api/oleauto/nf-oleauto-varboolfromui8) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBstrCat](/windows/win32/api/oleauto/nf-oleauto-varbstrcat) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBstrCmp](/windows/win32/api/oleauto/nf-oleauto-varbstrcmp) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBstrFromBool](/windows/win32/api/oleauto/nf-oleauto-varbstrfrombool) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBstrFromCy](/windows/win32/api/oleauto/nf-oleauto-varbstrfromcy) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBstrFromDate](/windows/win32/api/oleauto/nf-oleauto-varbstrfromdate) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBstrFromDec](/windows/win32/api/oleauto/nf-oleauto-varbstrfromdec) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBstrFromDisp](/windows/win32/api/oleauto/nf-oleauto-varbstrfromdisp) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBstrFromI1](/windows/win32/api/oleauto/nf-oleauto-varbstrfromi1) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBstrFromI2](/windows/win32/api/oleauto/nf-oleauto-varbstrfromi2) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBstrFromI4](/windows/win32/api/oleauto/nf-oleauto-varbstrfromi4) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBstrFromI8](/windows/win32/api/oleauto/nf-oleauto-varbstrfromi8) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBstrFromR4](/windows/win32/api/oleauto/nf-oleauto-varbstrfromr4) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBstrFromR8](/windows/win32/api/oleauto/nf-oleauto-varbstrfromr8) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBstrFromUI1](/windows/win32/api/oleauto/nf-oleauto-varbstrfromui1) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBstrFromUI2](/windows/win32/api/oleauto/nf-oleauto-varbstrfromui2) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBstrFromUI4](/windows/win32/api/oleauto/nf-oleauto-varbstrfromui4) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBstrFromUI8](/windows/win32/api/oleauto/nf-oleauto-varbstrfromui8) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarCat](/windows/win32/api/oleauto/nf-oleauto-varcat) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarCmp](/windows/win32/api/oleauto/nf-oleauto-varcmp) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarCyAbs](/windows/win32/api/oleauto/nf-oleauto-varcyabs) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarCyAdd](/windows/win32/api/oleauto/nf-oleauto-varcyadd) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarCyCmp](/windows/win32/api/oleauto/nf-oleauto-varcycmp) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarCyCmpR8](/windows/win32/api/oleauto/nf-oleauto-varcycmpr8) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarCyFix](/windows/win32/api/oleauto/nf-oleauto-varcyfix) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarCyFromBool](/windows/win32/api/oleauto/nf-oleauto-varcyfrombool) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarCyFromDate](/windows/win32/api/oleauto/nf-oleauto-varcyfromdate) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarCyFromDec](/windows/win32/api/oleauto/nf-oleauto-varcyfromdec) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarCyFromDisp](/windows/win32/api/oleauto/nf-oleauto-varcyfromdisp) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarCyFromI1](/windows/win32/api/oleauto/nf-oleauto-varcyfromi1) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarCyFromI2](/windows/win32/api/oleauto/nf-oleauto-varcyfromi2) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarCyFromI4](/windows/win32/api/oleauto/nf-oleauto-varcyfromi4) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarCyFromI8](/windows/win32/api/oleauto/nf-oleauto-varcyfromi8) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarCyFromR4](/windows/win32/api/oleauto/nf-oleauto-varcyfromr4) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarCyFromR8](/windows/win32/api/oleauto/nf-oleauto-varcyfromr8) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarCyFromStr](/windows/win32/api/oleauto/nf-oleauto-varcyfromstr) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarCyFromUI1](/windows/win32/api/oleauto/nf-oleauto-varcyfromui1) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarCyFromUI2](/windows/win32/api/oleauto/nf-oleauto-varcyfromui2) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarCyFromUI4](/windows/win32/api/oleauto/nf-oleauto-varcyfromui4) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarCyFromUI8](/windows/win32/api/oleauto/nf-oleauto-varcyfromui8) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarCyInt](/windows/win32/api/oleauto/nf-oleauto-varcyint) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarCyMul](/windows/win32/api/oleauto/nf-oleauto-varcymul) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarCyMulI4](/windows/win32/api/oleauto/nf-oleauto-varcymuli4) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarCyMulI8](/windows/win32/api/oleauto/nf-oleauto-varcymuli8) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarCyNeg](/windows/win32/api/oleauto/nf-oleauto-varcyneg) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarCyRound](/windows/win32/api/oleauto/nf-oleauto-varcyround) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarCySub](/windows/win32/api/oleauto/nf-oleauto-varcysub) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDateFromBool](/windows/win32/api/oleauto/nf-oleauto-vardatefrombool) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDateFromCy](/windows/win32/api/oleauto/nf-oleauto-vardatefromcy) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDateFromDec](/windows/win32/api/oleauto/nf-oleauto-vardatefromdec) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDateFromDisp](/windows/win32/api/oleauto/nf-oleauto-vardatefromdisp) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDateFromI1](/windows/win32/api/oleauto/nf-oleauto-vardatefromi1) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDateFromI2](/windows/win32/api/oleauto/nf-oleauto-vardatefromi2) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDateFromI4](/windows/win32/api/oleauto/nf-oleauto-vardatefromi4) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDateFromI8](/windows/win32/api/oleauto/nf-oleauto-vardatefromi8) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDateFromR4](/windows/win32/api/oleauto/nf-oleauto-vardatefromr4) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDateFromR8](/windows/win32/api/oleauto/nf-oleauto-vardatefromr8) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDateFromStr](/windows/win32/api/oleauto/nf-oleauto-vardatefromstr) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDateFromUdate](/windows/win32/api/oleauto/nf-oleauto-vardatefromudate) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDateFromUdateEx](/windows/win32/api/oleauto/nf-oleauto-vardatefromudateex) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDateFromUI1](/windows/win32/api/oleauto/nf-oleauto-vardatefromui1) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDateFromUI2](/windows/win32/api/oleauto/nf-oleauto-vardatefromui2) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDateFromUI4](/windows/win32/api/oleauto/nf-oleauto-vardatefromui4) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDateFromUI8](/windows/win32/api/oleauto/nf-oleauto-vardatefromui8) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDecAbs](/windows/win32/api/oleauto/nf-oleauto-vardecabs) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDecAdd](/windows/win32/api/oleauto/nf-oleauto-vardecadd) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDecCmp](/windows/win32/api/oleauto/nf-oleauto-vardeccmp) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDecCmpR8](/windows/win32/api/oleauto/nf-oleauto-vardeccmpr8) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDecDiv](/windows/win32/api/oleauto/nf-oleauto-vardecdiv) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDecFix](/windows/win32/api/oleauto/nf-oleauto-vardecfix) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDecFromBool](/windows/win32/api/oleauto/nf-oleauto-vardecfrombool) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDecFromCy](/windows/win32/api/oleauto/nf-oleauto-vardecfromcy) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDecFromDate](/windows/win32/api/oleauto/nf-oleauto-vardecfromdate) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDecFromDisp](/windows/win32/api/oleauto/nf-oleauto-vardecfromdisp) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDecFromI1](/windows/win32/api/oleauto/nf-oleauto-vardecfromi1) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDecFromI2](/windows/win32/api/oleauto/nf-oleauto-vardecfromi2) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDecFromI4](/windows/win32/api/oleauto/nf-oleauto-vardecfromi4) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDecFromI8](/windows/win32/api/oleauto/nf-oleauto-vardecfromi8) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDecFromR4](/windows/win32/api/oleauto/nf-oleauto-vardecfromr4) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDecFromR8](/windows/win32/api/oleauto/nf-oleauto-vardecfromr8) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDecFromStr](/windows/win32/api/oleauto/nf-oleauto-vardecfromstr) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDecFromUI1](/windows/win32/api/oleauto/nf-oleauto-vardecfromui1) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDecFromUI2](/windows/win32/api/oleauto/nf-oleauto-vardecfromui2) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDecFromUI4](/windows/win32/api/oleauto/nf-oleauto-vardecfromui4) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDecFromUI8](/windows/win32/api/oleauto/nf-oleauto-vardecfromui8) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDecInt](/windows/win32/api/oleauto/nf-oleauto-vardecint) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDecMul](/windows/win32/api/oleauto/nf-oleauto-vardecmul) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDecNeg](/windows/win32/api/oleauto/nf-oleauto-vardecneg) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDecRound](/windows/win32/api/oleauto/nf-oleauto-vardecround) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDecSub](/windows/win32/api/oleauto/nf-oleauto-vardecsub) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDiv](/windows/win32/api/oleauto/nf-oleauto-vardiv) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarEqv](/windows/win32/api/oleauto/nf-oleauto-vareqv) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarFix](/windows/win32/api/oleauto/nf-oleauto-varfix) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarFormat](/windows/win32/api/oleauto/nf-oleauto-varformat) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarFormatCurrency](/windows/win32/api/oleauto/nf-oleauto-varformatcurrency) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarFormatDateTime](/windows/win32/api/oleauto/nf-oleauto-varformatdatetime) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarFormatFromTokens](/windows/win32/api/oleauto/nf-oleauto-varformatfromtokens) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarFormatNumber](/windows/win32/api/oleauto/nf-oleauto-varformatnumber) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarFormatPercent](/windows/win32/api/oleauto/nf-oleauto-varformatpercent) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI1FromBool](/windows/win32/api/oleauto/nf-oleauto-vari1frombool) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI1FromCy](/windows/win32/api/oleauto/nf-oleauto-vari1fromcy) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI1FromDate](/windows/win32/api/oleauto/nf-oleauto-vari1fromdate) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI1FromDec](/windows/win32/api/oleauto/nf-oleauto-vari1fromdec) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI1FromDisp](/windows/win32/api/oleauto/nf-oleauto-vari1fromdisp) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI1FromI2](/windows/win32/api/oleauto/nf-oleauto-vari1fromi2) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI1FromI4](/windows/win32/api/oleauto/nf-oleauto-vari1fromi4) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI1FromI8](/windows/win32/api/oleauto/nf-oleauto-vari1fromi8) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI1FromR4](/windows/win32/api/oleauto/nf-oleauto-vari1fromr4) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI1FromR8](/windows/win32/api/oleauto/nf-oleauto-vari1fromr8) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI1FromStr](/windows/win32/api/oleauto/nf-oleauto-vari1fromstr) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI1FromUI1](/windows/win32/api/oleauto/nf-oleauto-vari1fromui1) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI1FromUI2](/windows/win32/api/oleauto/nf-oleauto-vari1fromui2) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI1FromUI4](/windows/win32/api/oleauto/nf-oleauto-vari1fromui4) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI1FromUI8](/windows/win32/api/oleauto/nf-oleauto-vari1fromui8) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI2FromBool](/windows/win32/api/oleauto/nf-oleauto-vari2frombool) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI2FromCy](/windows/win32/api/oleauto/nf-oleauto-vari2fromcy) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI2FromDate](/windows/win32/api/oleauto/nf-oleauto-vari2fromdate) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI2FromDec](/windows/win32/api/oleauto/nf-oleauto-vari2fromdec) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI2FromDisp](/windows/win32/api/oleauto/nf-oleauto-vari2fromdisp) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI2FromI1](/windows/win32/api/oleauto/nf-oleauto-vari2fromi1) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI2FromI4](/windows/win32/api/oleauto/nf-oleauto-vari2fromi4) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI2FromI8](/windows/win32/api/oleauto/nf-oleauto-vari2fromi8) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI2FromR4](/windows/win32/api/oleauto/nf-oleauto-vari2fromr4) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI2FromR8](/windows/win32/api/oleauto/nf-oleauto-vari2fromr8) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI2FromStr](/windows/win32/api/oleauto/nf-oleauto-vari2fromstr) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI2FromUI1](/windows/win32/api/oleauto/nf-oleauto-vari2fromui1) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI2FromUI2](/windows/win32/api/oleauto/nf-oleauto-vari2fromui2) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI2FromUI4](/windows/win32/api/oleauto/nf-oleauto-vari2fromui4) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI2FromUI8](/windows/win32/api/oleauto/nf-oleauto-vari2fromui8) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI4FromBool](/windows/win32/api/oleauto/nf-oleauto-vari4frombool) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI4FromCy](/windows/win32/api/oleauto/nf-oleauto-vari4fromcy) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI4FromDate](/windows/win32/api/oleauto/nf-oleauto-vari4fromdate) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI4FromDec](/windows/win32/api/oleauto/nf-oleauto-vari4fromdec) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI4FromDisp](/windows/win32/api/oleauto/nf-oleauto-vari4fromdisp) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI4FromI1](/windows/win32/api/oleauto/nf-oleauto-vari4fromi1) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI4FromI2](/windows/win32/api/oleauto/nf-oleauto-vari4fromi2) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI4FromI8](/windows/win32/api/oleauto/nf-oleauto-vari4fromi8) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI4FromR4](/windows/win32/api/oleauto/nf-oleauto-vari4fromr4) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI4FromR8](/windows/win32/api/oleauto/nf-oleauto-vari4fromr8) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI4FromStr](/windows/win32/api/oleauto/nf-oleauto-vari4fromstr) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI4FromUI1](/windows/win32/api/oleauto/nf-oleauto-vari4fromui1) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI4FromUI2](/windows/win32/api/oleauto/nf-oleauto-vari4fromui2) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI4FromUI4](/windows/win32/api/oleauto/nf-oleauto-vari4fromui4) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI4FromUI8](/windows/win32/api/oleauto/nf-oleauto-vari4fromui8) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI8FromBool](/windows/win32/api/oleauto/nf-oleauto-vari8frombool) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI8FromCy](/windows/win32/api/oleauto/nf-oleauto-vari8fromcy) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI8FromDate](/windows/win32/api/oleauto/nf-oleauto-vari8fromdate) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI8FromDec](/windows/win32/api/oleauto/nf-oleauto-vari8fromdec) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI8FromDisp](/windows/win32/api/oleauto/nf-oleauto-vari8fromdisp) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI8FromI1](/windows/win32/api/oleauto/nf-oleauto-vari8fromi1) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI8FromI2](/windows/win32/api/oleauto/nf-oleauto-vari8fromi2) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI8FromR4](/windows/win32/api/oleauto/nf-oleauto-vari8fromr4) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI8FromR8](/windows/win32/api/oleauto/nf-oleauto-vari8fromr8) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI8FromStr](/windows/win32/api/oleauto/nf-oleauto-vari8fromstr) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI8FromUI1](/windows/win32/api/oleauto/nf-oleauto-vari8fromui1) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI8FromUI2](/windows/win32/api/oleauto/nf-oleauto-vari8fromui2) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI8FromUI4](/windows/win32/api/oleauto/nf-oleauto-vari8fromui4) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI8FromUI8](/windows/win32/api/oleauto/nf-oleauto-vari8fromui8) | Introduced into oleaut32.dll in 10.0.10240. |
| [VARIANT_UserFree](/windows/win32/api/oaidl/nf-oaidl-variant_userfree) | Introduced into oleaut32.dll in 10.0.10240. |
| [VARIANT_UserFree64](/windows/win32/api/oaidl/nf-oaidl-variant_userfree64) | Introduced into oleaut32.dll in 10.0.10240. Removed in 10.0.16299. |
| [VARIANT_UserMarshal](/windows/win32/api/oaidl/nf-oaidl-variant_usermarshal) | Introduced into oleaut32.dll in 10.0.10240. |
| [VARIANT_UserMarshal64](/windows/win32/api/oaidl/nf-oaidl-variant_usermarshal64) | Introduced into oleaut32.dll in 10.0.10240. Removed in 10.0.16299. |
| [VARIANT_UserSize](/windows/win32/api/oaidl/nf-oaidl-variant_usersize) | Introduced into oleaut32.dll in 10.0.10240. |
| [VARIANT_UserSize64](/windows/win32/api/oaidl/nf-oaidl-variant_usersize64) | Introduced into oleaut32.dll in 10.0.10240. Removed in 10.0.16299. |
| [VARIANT_UserUnmarshal](/windows/win32/api/oaidl/nf-oaidl-variant_userunmarshal) | Introduced into oleaut32.dll in 10.0.10240. |
| [VARIANT_UserUnmarshal64](/windows/win32/api/oaidl/nf-oaidl-variant_userunmarshal64) | Introduced into oleaut32.dll in 10.0.10240. Removed in 10.0.16299. |
| [VariantChangeType](/windows/win32/api/oleauto/nf-oleauto-variantchangetype) | Introduced into oleaut32.dll in 10.0.10240. |
| [VariantChangeTypeEx](/windows/win32/api/oleauto/nf-oleauto-variantchangetypeex) | Introduced into oleaut32.dll in 10.0.10240. |
| [VariantClear](/windows/win32/api/oleauto/nf-oleauto-variantclear) | Introduced into oleaut32.dll in 10.0.10240. |
| [VariantCopy](/windows/win32/api/oleauto/nf-oleauto-variantcopy) | Introduced into oleaut32.dll in 10.0.10240. |
| [VariantCopyInd](/windows/win32/api/oleauto/nf-oleauto-variantcopyind) | Introduced into oleaut32.dll in 10.0.10240. |
| [VariantInit](/windows/win32/api/oleauto/nf-oleauto-variantinit) | Introduced into oleaut32.dll in 10.0.10240. |
| [VariantTimeToSystemTime](/windows/win32/api/oleauto/nf-oleauto-varianttimetosystemtime) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarIdiv](/windows/win32/api/oleauto/nf-oleauto-varidiv) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarImp](/windows/win32/api/oleauto/nf-oleauto-varimp) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarInt](/windows/win32/api/oleauto/nf-oleauto-varint) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarMod](/windows/win32/api/oleauto/nf-oleauto-varmod) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarMonthName](/windows/win32/api/oleauto/nf-oleauto-varmonthname) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarMul](/windows/win32/api/oleauto/nf-oleauto-varmul) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarNeg](/windows/win32/api/oleauto/nf-oleauto-varneg) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarNot](/windows/win32/api/oleauto/nf-oleauto-varnot) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarNumFromParseNum](/windows/win32/api/oleauto/nf-oleauto-varnumfromparsenum) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarOr](/windows/win32/api/oleauto/nf-oleauto-varor) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarParseNumFromStr](/windows/win32/api/oleauto/nf-oleauto-varparsenumfromstr) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarPow](/windows/win32/api/oleauto/nf-oleauto-varpow) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR4CmpR8](/windows/win32/api/oleauto/nf-oleauto-varr4cmpr8) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR4FromBool](/windows/win32/api/oleauto/nf-oleauto-varr4frombool) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR4FromCy](/windows/win32/api/oleauto/nf-oleauto-varr4fromcy) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR4FromDate](/windows/win32/api/oleauto/nf-oleauto-varr4fromdate) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR4FromDec](/windows/win32/api/oleauto/nf-oleauto-varr4fromdec) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR4FromDisp](/windows/win32/api/oleauto/nf-oleauto-varr4fromdisp) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR4FromI1](/windows/win32/api/oleauto/nf-oleauto-varr4fromi1) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR4FromI2](/windows/win32/api/oleauto/nf-oleauto-varr4fromi2) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR4FromI4](/windows/win32/api/oleauto/nf-oleauto-varr4fromi4) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR4FromI8](/windows/win32/api/oleauto/nf-oleauto-varr4fromi8) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR4FromR8](/windows/win32/api/oleauto/nf-oleauto-varr4fromr8) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR4FromStr](/windows/win32/api/oleauto/nf-oleauto-varr4fromstr) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR4FromUI1](/windows/win32/api/oleauto/nf-oleauto-varr4fromui1) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR4FromUI2](/windows/win32/api/oleauto/nf-oleauto-varr4fromui2) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR4FromUI4](/windows/win32/api/oleauto/nf-oleauto-varr4fromui4) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR4FromUI8](/windows/win32/api/oleauto/nf-oleauto-varr4fromui8) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR8FromBool](/windows/win32/api/oleauto/nf-oleauto-varr8frombool) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR8FromCy](/windows/win32/api/oleauto/nf-oleauto-varr8fromcy) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR8FromDate](/windows/win32/api/oleauto/nf-oleauto-varr8fromdate) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR8FromDec](/windows/win32/api/oleauto/nf-oleauto-varr8fromdec) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR8FromDisp](/windows/win32/api/oleauto/nf-oleauto-varr8fromdisp) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR8FromI1](/windows/win32/api/oleauto/nf-oleauto-varr8fromi1) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR8FromI2](/windows/win32/api/oleauto/nf-oleauto-varr8fromi2) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR8FromI4](/windows/win32/api/oleauto/nf-oleauto-varr8fromi4) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR8FromI8](/windows/win32/api/oleauto/nf-oleauto-varr8fromi8) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR8FromR4](/windows/win32/api/oleauto/nf-oleauto-varr8fromr4) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR8FromStr](/windows/win32/api/oleauto/nf-oleauto-varr8fromstr) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR8FromUI1](/windows/win32/api/oleauto/nf-oleauto-varr8fromui1) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR8FromUI2](/windows/win32/api/oleauto/nf-oleauto-varr8fromui2) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR8FromUI4](/windows/win32/api/oleauto/nf-oleauto-varr8fromui4) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR8FromUI8](/windows/win32/api/oleauto/nf-oleauto-varr8fromui8) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR8Pow](/windows/win32/api/oleauto/nf-oleauto-varr8pow) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR8Round](/windows/win32/api/oleauto/nf-oleauto-varr8round) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarRound](/windows/win32/api/oleauto/nf-oleauto-varround) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarSub](/windows/win32/api/oleauto/nf-oleauto-varsub) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarTokenizeFormatString](/windows/win32/api/oleauto/nf-oleauto-vartokenizeformatstring) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUdateFromDate](/windows/win32/api/oleauto/nf-oleauto-varudatefromdate) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI1FromBool](/windows/win32/api/oleauto/nf-oleauto-varui1frombool) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI1FromCy](/windows/win32/api/oleauto/nf-oleauto-varui1fromcy) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI1FromDate](/windows/win32/api/oleauto/nf-oleauto-varui1fromdate) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI1FromDec](/windows/win32/api/oleauto/nf-oleauto-varui1fromdec) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI1FromDisp](/windows/win32/api/oleauto/nf-oleauto-varui1fromdisp) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI1FromI1](/windows/win32/api/oleauto/nf-oleauto-varui1fromi1) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI1FromI2](/windows/win32/api/oleauto/nf-oleauto-varui1fromi2) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI1FromI4](/windows/win32/api/oleauto/nf-oleauto-varui1fromi4) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI1FromI8](/windows/win32/api/oleauto/nf-oleauto-varui1fromi8) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI1FromR4](/windows/win32/api/oleauto/nf-oleauto-varui1fromr4) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI1FromR8](/windows/win32/api/oleauto/nf-oleauto-varui1fromr8) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI1FromStr](/windows/win32/api/oleauto/nf-oleauto-varui1fromstr) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI1FromUI2](/windows/win32/api/oleauto/nf-oleauto-varui1fromui2) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI1FromUI4](/windows/win32/api/oleauto/nf-oleauto-varui1fromui4) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI1FromUI8](/windows/win32/api/oleauto/nf-oleauto-varui1fromui8) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI2FromBool](/windows/win32/api/oleauto/nf-oleauto-varui2frombool) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI2FromCy](/windows/win32/api/oleauto/nf-oleauto-varui2fromcy) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI2FromDate](/windows/win32/api/oleauto/nf-oleauto-varui2fromdate) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI2FromDec](/windows/win32/api/oleauto/nf-oleauto-varui2fromdec) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI2FromDisp](/windows/win32/api/oleauto/nf-oleauto-varui2fromdisp) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI2FromI1](/windows/win32/api/oleauto/nf-oleauto-varui2fromi1) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI2FromI2](/windows/win32/api/oleauto/nf-oleauto-varui2fromi2) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI2FromI4](/windows/win32/api/oleauto/nf-oleauto-varui2fromi4) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI2FromI8](/windows/win32/api/oleauto/nf-oleauto-varui2fromi8) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI2FromR4](/windows/win32/api/oleauto/nf-oleauto-varui2fromr4) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI2FromR8](/windows/win32/api/oleauto/nf-oleauto-varui2fromr8) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI2FromStr](/windows/win32/api/oleauto/nf-oleauto-varui2fromstr) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI2FromUI1](/windows/win32/api/oleauto/nf-oleauto-varui2fromui1) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI2FromUI4](/windows/win32/api/oleauto/nf-oleauto-varui2fromui4) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI2FromUI8](/windows/win32/api/oleauto/nf-oleauto-varui2fromui8) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI4FromBool](/windows/win32/api/oleauto/nf-oleauto-varui4frombool) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI4FromCy](/windows/win32/api/oleauto/nf-oleauto-varui4fromcy) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI4FromDate](/windows/win32/api/oleauto/nf-oleauto-varui4fromdate) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI4FromDec](/windows/win32/api/oleauto/nf-oleauto-varui4fromdec) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI4FromDisp](/windows/win32/api/oleauto/nf-oleauto-varui4fromdisp) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI4FromI1](/windows/win32/api/oleauto/nf-oleauto-varui4fromi1) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI4FromI2](/windows/win32/api/oleauto/nf-oleauto-varui4fromi2) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI4FromI4](/windows/win32/api/oleauto/nf-oleauto-varui4fromi4) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI4FromI8](/windows/win32/api/oleauto/nf-oleauto-varui4fromi8) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI4FromR4](/windows/win32/api/oleauto/nf-oleauto-varui4fromr4) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI4FromR8](/windows/win32/api/oleauto/nf-oleauto-varui4fromr8) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI4FromStr](/windows/win32/api/oleauto/nf-oleauto-varui4fromstr) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI4FromUI1](/windows/win32/api/oleauto/nf-oleauto-varui4fromui1) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI4FromUI2](/windows/win32/api/oleauto/nf-oleauto-varui4fromui2) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI4FromUI8](/windows/win32/api/oleauto/nf-oleauto-varui4fromui8) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI8FromBool](/windows/win32/api/oleauto/nf-oleauto-varui8frombool) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI8FromCy](/windows/win32/api/oleauto/nf-oleauto-varui8fromcy) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI8FromDate](/windows/win32/api/oleauto/nf-oleauto-varui8fromdate) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI8FromDec](/windows/win32/api/oleauto/nf-oleauto-varui8fromdec) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI8FromDisp](/windows/win32/api/oleauto/nf-oleauto-varui8fromdisp) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI8FromI1](/windows/win32/api/oleauto/nf-oleauto-varui8fromi1) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI8FromI2](/windows/win32/api/oleauto/nf-oleauto-varui8fromi2) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI8FromI8](/windows/win32/api/oleauto/nf-oleauto-varui8fromi8) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI8FromR4](/windows/win32/api/oleauto/nf-oleauto-varui8fromr4) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI8FromR8](/windows/win32/api/oleauto/nf-oleauto-varui8fromr8) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI8FromStr](/windows/win32/api/oleauto/nf-oleauto-varui8fromstr) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI8FromUI1](/windows/win32/api/oleauto/nf-oleauto-varui8fromui1) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI8FromUI2](/windows/win32/api/oleauto/nf-oleauto-varui8fromui2) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI8FromUI4](/windows/win32/api/oleauto/nf-oleauto-varui8fromui4) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarWeekdayName](/windows/win32/api/oleauto/nf-oleauto-varweekdayname) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarXor](/windows/win32/api/oleauto/nf-oleauto-varxor) | Introduced into oleaut32.dll in 10.0.10240. |


## APIs from propsys.dll

| API | Requirements |
| -----| --------------|
| [PropVariantCompareEx](/windows/win32/api/propvarutil/nf-propvarutil-propvariantcompareex) | Introduced into propsys.dll in 10.0.10240. |
| [PropVariantToWinRTPropertyValue](/previous-versions//dn313197(v=vs.85)) | Introduced into propsys.dll in 10.0.10240. |
| [WinRTPropertyValueToPropVariant](/windows/win32/api/propsys/nf-propsys-winrtpropertyvaluetopropvariant) | Introduced into propsys.dll in 10.0.10240. |
| [InitPropVariantFromCLSID](/windows/win32/api/propvarutil/nf-propvarutil-initpropvariantfromclsid) | Introduced into propsys.dll in 10.0.16299. |
| [InitPropVariantFromFileTime](/windows/win32/api/propvarutil/nf-propvarutil-initpropvariantfromfiletime) | Introduced into propsys.dll in 10.0.16299. |
| [InitVariantFromBuffer](/windows/win32/api/propvarutil/nf-propvarutil-initvariantfrombuffer) | Introduced into propsys.dll in 10.0.16299. |
| [PropVariantChangeType](/windows/win32/api/propvarutil/nf-propvarutil-propvariantchangetype) | Introduced into propsys.dll in 10.0.16299. |
| [PropVariantToBoolean](/windows/win32/api/propvarutil/nf-propvarutil-propvarianttoboolean) | Introduced into propsys.dll in 10.0.16299. |
| [PropVariantToBSTR](/windows/win32/api/propvarutil/nf-propvarutil-propvarianttobstr) | Introduced into propsys.dll in 10.0.16299. |
| [PropVariantToGUID](/windows/win32/api/propvarutil/nf-propvarutil-propvarianttoguid) | Introduced into propsys.dll in 10.0.16299. |
| [PropVariantToStringAlloc](/windows/win32/api/propvarutil/nf-propvarutil-propvarianttostringalloc) | Introduced into propsys.dll in 10.0.16299. |
| [PropVariantToStringWithDefault](/windows/win32/api/propvarutil/nf-propvarutil-propvarianttostringwithdefault) | Introduced into propsys.dll in 10.0.16299. |
| [PropVariantToVariant](/windows/win32/api/propvarutil/nf-propvarutil-propvarianttovariant) | Introduced into propsys.dll in 10.0.16299. |
| [PSCreateAdapterFromPropertyStore](/windows/win32/api/propsys/nf-propsys-pscreateadapterfrompropertystore) | Introduced into propsys.dll in 10.0.16299. |
| [PSCreateMemoryPropertyStore](/windows/win32/api/propsys/nf-propsys-pscreatememorypropertystore) | Introduced into propsys.dll in 10.0.16299. |
| [PSCreatePropertyStoreFromObject](/windows/win32/api/propsys/nf-propsys-pscreatepropertystorefromobject) | Introduced into propsys.dll in 10.0.16299. |
| [VariantToGUID](/windows/win32/api/propvarutil/nf-propvarutil-varianttoguid) | Introduced into propsys.dll in 10.0.16299. |
| [VariantToPropVariant](/windows/win32/api/propvarutil/nf-propvarutil-varianttopropvariant) | Introduced into propsys.dll in 10.0.16299. |


## APIs from rpcrt4.dll

| API | Requirements |
| -----| --------------|
| CreateProxyFromTypeInfo | Introduced into rpcrt4.dll in 10.0.10240. |
| CreateStubFromTypeInfo | Introduced into rpcrt4.dll in 10.0.10240. |
| [CStdStubBuffer_AddRef](/windows/win32/api/rpcproxy/nf-rpcproxy-cstdstubbuffer_addref) | Introduced into rpcrt4.dll in 10.0.10240. |
| [CStdStubBuffer_Connect](/windows/win32/api/rpcproxy/nf-rpcproxy-cstdstubbuffer_connect) | Introduced into rpcrt4.dll in 10.0.10240. |
| [CStdStubBuffer_CountRefs](/windows/win32/api/rpcproxy/nf-rpcproxy-cstdstubbuffer_countrefs) | Introduced into rpcrt4.dll in 10.0.10240. |
| [CStdStubBuffer_DebugServerQueryInterface](/windows/win32/api/rpcproxy/nf-rpcproxy-cstdstubbuffer_debugserverqueryinterface) | Introduced into rpcrt4.dll in 10.0.10240. |
| [CStdStubBuffer_DebugServerRelease](/windows/win32/api/rpcproxy/nf-rpcproxy-cstdstubbuffer_debugserverrelease) | Introduced into rpcrt4.dll in 10.0.10240. |
| [CStdStubBuffer_Disconnect](/windows/win32/api/rpcproxy/nf-rpcproxy-cstdstubbuffer_disconnect) | Introduced into rpcrt4.dll in 10.0.10240. |
| [CStdStubBuffer_Invoke](/windows/win32/api/rpcproxy/nf-rpcproxy-cstdstubbuffer_invoke) | Introduced into rpcrt4.dll in 10.0.10240. |
| [CStdStubBuffer_IsIIDSupported](/windows/win32/api/rpcproxy/nf-rpcproxy-cstdstubbuffer_isiidsupported) | Introduced into rpcrt4.dll in 10.0.10240. |
| [CStdStubBuffer_QueryInterface](/windows/win32/api/rpcproxy/nf-rpcproxy-cstdstubbuffer_queryinterface) | Introduced into rpcrt4.dll in 10.0.10240. |
| [IUnknown_AddRef_Proxy](/windows/win32/api/unknwnbase/nf-unknwnbase-iunknown_addref_proxy) | Introduced into rpcrt4.dll in 10.0.10240. |
| [IUnknown_QueryInterface_Proxy](/windows/win32/api/unknwnbase/nf-unknwnbase-iunknown_queryinterface_proxy) | Introduced into rpcrt4.dll in 10.0.10240. |
| [IUnknown_Release_Proxy](/windows/win32/api/unknwnbase/nf-unknwnbase-iunknown_release_proxy) | Introduced into rpcrt4.dll in 10.0.10240. |
| [Ndr64AsyncClientCall](/windows/win32/api/rpcndr/nf-rpcndr-ndr64asyncclientcall) | Introduced into rpcrt4.dll in 10.0.10240. Removed in 10.0.16299. |
| Ndr64AsyncServerCall64 | Introduced into rpcrt4.dll in 10.0.10240. Removed in 10.0.16299. |
| [Ndr64AsyncServerCallAll](/windows/win32/api/rpcndr/nf-rpcndr-ndr64asyncservercallall) | Introduced into rpcrt4.dll in 10.0.10240. Removed in 10.0.16299. |
| NdrAllocate | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrAsyncClientCall](/windows/win32/api/rpcndr/nf-rpcndr-ndrasyncclientcall) | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrAsyncServerCall](/windows/win32/api/rpcndr/nf-rpcndr-ndrasyncservercall) | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrByteCountPointerBufferSize | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrByteCountPointerFree | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrByteCountPointerMarshall | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrByteCountPointerUnmarshall | Introduced into rpcrt4.dll in 10.0.10240. |
| NDRCContextBinding | Introduced into rpcrt4.dll in 10.0.10240. |
| NDRCContextMarshall | Introduced into rpcrt4.dll in 10.0.10240. |
| NDRCContextUnmarshall | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrClearOutParameters](/windows/win32/api/rpcndr/nf-rpcndr-ndrclearoutparameters) | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrClientCall2](/windows/win32/api/rpcndr/nf-rpcndr-ndrclientcall2) | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrClientCall3](/windows/win32/api/rpcndr/nf-rpcndr-ndrclientcall3) | Introduced into rpcrt4.dll in 10.0.10240. Removed in 10.0.16299. |
| NdrClientContextMarshall | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrClientContextUnmarshall | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrClientInitialize | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrClientInitializeNew | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrComplexArrayBufferSize](/windows/win32/api/rpcndr/nf-rpcndr-ndrcomplexarraybuffersize) | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrComplexArrayFree | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrComplexArrayMarshall](/windows/win32/api/rpcndr/nf-rpcndr-ndrcomplexarraymarshall) | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrComplexArrayMemorySize | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrComplexArrayUnmarshall](/windows/win32/api/rpcndr/nf-rpcndr-ndrcomplexarrayunmarshall) | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrComplexStructBufferSize](/windows/win32/api/rpcndr/nf-rpcndr-ndrcomplexstructbuffersize) | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrComplexStructFree | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrComplexStructMarshall](/windows/win32/api/rpcndr/nf-rpcndr-ndrcomplexstructmarshall) | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrComplexStructMemorySize | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrComplexStructUnmarshall](/windows/win32/api/rpcndr/nf-rpcndr-ndrcomplexstructunmarshall) | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrConformantArrayBufferSize](/windows/win32/api/rpcndr/nf-rpcndr-ndrconformantarraybuffersize) | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrConformantArrayFree | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrConformantArrayMarshall](/windows/win32/api/rpcndr/nf-rpcndr-ndrconformantarraymarshall) | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrConformantArrayMemorySize | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrConformantArrayUnmarshall](/windows/win32/api/rpcndr/nf-rpcndr-ndrconformantarrayunmarshall) | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrConformantStringBufferSize](/windows/win32/api/rpcndr/nf-rpcndr-ndrconformantstringbuffersize) | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrConformantStringMarshall](/windows/win32/api/rpcndr/nf-rpcndr-ndrconformantstringmarshall) | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrConformantStringMemorySize | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrConformantStringUnmarshall](/windows/win32/api/rpcndr/nf-rpcndr-ndrconformantstringunmarshall) | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrConformantStructBufferSize | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrConformantStructFree | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrConformantStructMarshall | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrConformantStructMemorySize | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrConformantStructUnmarshall | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrConformantVaryingArrayBufferSize | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrConformantVaryingArrayFree | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrConformantVaryingArrayMarshall | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrConformantVaryingArrayMemorySize | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrConformantVaryingArrayUnmarshall | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrConformantVaryingStructBufferSize | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrConformantVaryingStructFree | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrConformantVaryingStructMarshall | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrConformantVaryingStructMemorySize | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrConformantVaryingStructUnmarshall | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrContextHandleInitialize](/windows/win32/api/rpcndr/nf-rpcndr-ndrcontexthandleinitialize) | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrContextHandleSize](/windows/win32/api/rpcndr/nf-rpcndr-ndrcontexthandlesize) | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrConvert](/windows/win32/api/rpcndr/nf-rpcndr-ndrconvert) | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrConvert2 | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrCorrelationFree | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrCorrelationInitialize | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrCorrelationPass | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrCreateServerInterfaceFromStub | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrCStdStubBuffer_Release](/windows/win32/api/rpcproxy/nf-rpcproxy-ndrcstdstubbuffer_release) | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrCStdStubBuffer2_Release](/windows/win32/api/rpcproxy/nf-rpcproxy-ndrcstdstubbuffer2_release) | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrDllCanUnloadNow](/windows/win32/api/rpcproxy/nf-rpcproxy-ndrdllcanunloadnow) | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrDllGetClassObject](/windows/win32/api/rpcproxy/nf-rpcproxy-ndrdllgetclassobject) | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrDllRegisterProxy](/windows/win32/api/rpcproxy/nf-rpcproxy-ndrdllregisterproxy) | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrDllUnregisterProxy](/windows/win32/api/rpcproxy/nf-rpcproxy-ndrdllunregisterproxy) | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrEncapsulatedUnionBufferSize | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrEncapsulatedUnionFree | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrEncapsulatedUnionMarshall | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrEncapsulatedUnionMemorySize | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrEncapsulatedUnionUnmarshall | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrFixedArrayBufferSize | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrFixedArrayFree | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrFixedArrayMarshall | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrFixedArrayMemorySize | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrFixedArrayUnmarshall | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrFreeBuffer | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrFullPointerXlatFree | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrFullPointerXlatInit | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrGetBuffer | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrGetDcomProtocolVersion | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrGetUserMarshalInfo](/windows/win32/api/rpcndr/nf-rpcndr-ndrgetusermarshalinfo) | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrInterfacePointerBufferSize](/windows/win32/api/rpcndr/nf-rpcndr-ndrinterfacepointerbuffersize) | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrInterfacePointerFree](/windows/win32/api/rpcndr/nf-rpcndr-ndrinterfacepointerfree) | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrInterfacePointerMarshall](/windows/win32/api/rpcndr/nf-rpcndr-ndrinterfacepointermarshall) | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrInterfacePointerMemorySize | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrInterfacePointerUnmarshall](/windows/win32/api/rpcndr/nf-rpcndr-ndrinterfacepointerunmarshall) | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrMapCommAndFaultStatus | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrNonConformantStringBufferSize | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrNonConformantStringMarshall | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrNonConformantStringMemorySize | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrNonConformantStringUnmarshall | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrNonEncapsulatedUnionBufferSize | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrNonEncapsulatedUnionFree | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrNonEncapsulatedUnionMarshall | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrNonEncapsulatedUnionMemorySize | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrNonEncapsulatedUnionUnmarshall | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrNsGetBuffer | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrNsSendReceive | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrOleAllocate](/windows/win32/api/rpcndr/nf-rpcndr-ndroleallocate) | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrOleFree](/windows/win32/api/rpcndr/nf-rpcndr-ndrolefree) | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrPartialIgnoreClientBufferSize | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrPartialIgnoreClientMarshall | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrPartialIgnoreServerInitialize | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrPartialIgnoreServerUnmarshall | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrPointerBufferSize](/windows/win32/api/rpcndr/nf-rpcndr-ndrpointerbuffersize) | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrPointerFree](/windows/win32/api/rpcndr/nf-rpcndr-ndrpointerfree) | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrPointerMarshall](/windows/win32/api/rpcndr/nf-rpcndr-ndrpointermarshall) | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrPointerMemorySize | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrPointerUnmarshall](/windows/win32/api/rpcndr/nf-rpcndr-ndrpointerunmarshall) | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrProxyErrorHandler](/windows/win32/api/rpcproxy/nf-rpcproxy-ndrproxyerrorhandler) | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrRangeUnmarshall | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrRpcSmClientAllocate | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrRpcSmClientFree | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrRpcSmSetClientToOsf | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrRpcSsDefaultAllocate | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrRpcSsDefaultFree | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrRpcSsDisableAllocate | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrRpcSsEnableAllocate | Introduced into rpcrt4.dll in 10.0.10240. |
| NDRSContextMarshall | Introduced into rpcrt4.dll in 10.0.10240. |
| NDRSContextMarshall2 | Introduced into rpcrt4.dll in 10.0.10240. |
| NDRSContextMarshallEx | Introduced into rpcrt4.dll in 10.0.10240. |
| NDRSContextUnmarshall | Introduced into rpcrt4.dll in 10.0.10240. |
| NDRSContextUnmarshall2 | Introduced into rpcrt4.dll in 10.0.10240. |
| NDRSContextUnmarshallEx | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrSendReceive | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrServerCall2](/windows/win32/api/rpcndr/nf-rpcndr-ndrservercall2) | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrServerCallAll](/windows/win32/api/rpcndr/nf-rpcndr-ndrservercallall) | Introduced into rpcrt4.dll in 10.0.10240. Removed in 10.0.16299. |
| NdrServerCallNdr64 | Introduced into rpcrt4.dll in 10.0.10240. Removed in 10.0.16299. |
| NdrServerContextMarshall | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrServerContextNewMarshall | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrServerContextNewUnmarshall | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrServerContextUnmarshall | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrServerInitialize | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrServerInitializeMarshall | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrServerInitializeNew | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrServerInitializePartial | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrServerInitializeUnmarshall | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrSimpleStructBufferSize](/windows/win32/api/rpcndr/nf-rpcndr-ndrsimplestructbuffersize) | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrSimpleStructFree | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrSimpleStructMarshall](/windows/win32/api/rpcndr/nf-rpcndr-ndrsimplestructmarshall) | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrSimpleStructMemorySize | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrSimpleStructUnmarshall](/windows/win32/api/rpcndr/nf-rpcndr-ndrsimplestructunmarshall) | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrSimpleTypeMarshall](/windows/win32/api/rpcndr/nf-rpcndr-ndrsimpletypemarshall) | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrSimpleTypeUnmarshall](/windows/win32/api/rpcndr/nf-rpcndr-ndrsimpletypeunmarshall) | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrStubCall2](/windows/win32/api/rpcndr/nf-rpcndr-ndrstubcall2) | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrStubCall3](/windows/win32/api/rpcndr/nf-rpcndr-ndrstubcall3) | Introduced into rpcrt4.dll in 10.0.10240. Removed in 10.0.16299. |
| [NdrStubForwardingFunction](/windows/win32/api/rpcproxy/nf-rpcproxy-ndrstubforwardingfunction) | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrUserMarshalBufferSize](/windows/win32/api/rpcndr/nf-rpcndr-ndrusermarshalbuffersize) | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrUserMarshalFree](/windows/win32/api/rpcndr/nf-rpcndr-ndrusermarshalfree) | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrUserMarshalMarshall](/windows/win32/api/rpcndr/nf-rpcndr-ndrusermarshalmarshall) | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrUserMarshalMemorySize | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrUserMarshalSimpleTypeConvert | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrUserMarshalUnmarshall](/windows/win32/api/rpcndr/nf-rpcndr-ndrusermarshalunmarshall) | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrVaryingArrayBufferSize | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrVaryingArrayFree | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrVaryingArrayMarshall | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrVaryingArrayMemorySize | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrVaryingArrayUnmarshall | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrXmitOrRepAsBufferSize | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrXmitOrRepAsFree | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrXmitOrRepAsMarshall | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrXmitOrRepAsMemorySize | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrXmitOrRepAsUnmarshall | Introduced into rpcrt4.dll in 10.0.10240. |
| [RpcSmAllocate](/windows/win32/api/rpcndr/nf-rpcndr-rpcsmallocate) | Introduced into rpcrt4.dll in 10.0.10240. |
| [RpcSmClientFree](/windows/win32/api/rpcndr/nf-rpcndr-rpcsmclientfree) | Introduced into rpcrt4.dll in 10.0.10240. |
| [RpcSmDestroyClientContext](/windows/win32/api/rpcndr/nf-rpcndr-rpcsmdestroyclientcontext) | Introduced into rpcrt4.dll in 10.0.10240. |
| [RpcSmDisableAllocate](/windows/win32/api/rpcndr/nf-rpcndr-rpcsmdisableallocate) | Introduced into rpcrt4.dll in 10.0.10240. |
| [RpcSmEnableAllocate](/windows/win32/api/rpcndr/nf-rpcndr-rpcsmenableallocate) | Introduced into rpcrt4.dll in 10.0.10240. |
| [RpcSmFree](/windows/win32/api/rpcndr/nf-rpcndr-rpcsmfree) | Introduced into rpcrt4.dll in 10.0.10240. |
| [RpcSmGetThreadHandle](/windows/win32/api/rpcndr/nf-rpcndr-rpcsmgetthreadhandle) | Introduced into rpcrt4.dll in 10.0.10240. |
| [RpcSmSetClientAllocFree](/windows/win32/api/rpcndr/nf-rpcndr-rpcsmsetclientallocfree) | Introduced into rpcrt4.dll in 10.0.10240. |
| [RpcSmSetThreadHandle](/windows/win32/api/rpcndr/nf-rpcndr-rpcsmsetthreadhandle) | Introduced into rpcrt4.dll in 10.0.10240. |
| [RpcSmSwapClientAllocFree](/windows/win32/api/rpcndr/nf-rpcndr-rpcsmswapclientallocfree) | Introduced into rpcrt4.dll in 10.0.10240. |
| [RpcSsAllocate](/windows/win32/api/rpcndr/nf-rpcndr-rpcssallocate) | Introduced into rpcrt4.dll in 10.0.10240. |
| [RpcSsDestroyClientContext](/windows/win32/api/rpcndr/nf-rpcndr-rpcssdestroyclientcontext) | Introduced into rpcrt4.dll in 10.0.10240. |
| [RpcSsDisableAllocate](/windows/win32/api/rpcndr/nf-rpcndr-rpcssdisableallocate) | Introduced into rpcrt4.dll in 10.0.10240. |
| [RpcSsEnableAllocate](/windows/win32/api/rpcndr/nf-rpcndr-rpcssenableallocate) | Introduced into rpcrt4.dll in 10.0.10240. |
| [RpcSsFree](/windows/win32/api/rpcndr/nf-rpcndr-rpcssfree) | Introduced into rpcrt4.dll in 10.0.10240. |
| [RpcSsGetThreadHandle](/windows/win32/api/rpcndr/nf-rpcndr-rpcssgetthreadhandle) | Introduced into rpcrt4.dll in 10.0.10240. |
| [RpcSsSetClientAllocFree](/windows/win32/api/rpcndr/nf-rpcndr-rpcsssetclientallocfree) | Introduced into rpcrt4.dll in 10.0.10240. |
| [RpcSsSetThreadHandle](/windows/win32/api/rpcndr/nf-rpcndr-rpcsssetthreadhandle) | Introduced into rpcrt4.dll in 10.0.10240. |
| [RpcSsSwapClientAllocFree](/windows/win32/api/rpcndr/nf-rpcndr-rpcssswapclientallocfree) | Introduced into rpcrt4.dll in 10.0.10240. |
| [RpcUserFree](/windows/win32/api/rpcndr/nf-rpcndr-rpcuserfree) | Introduced into rpcrt4.dll in 10.0.10240. |
| [UuidToStringW](/windows/win32/api/rpcdce/nf-rpcdce-uuidtostring) | Introduced into rpcrt4.dll in 10.0.16299. |
| [UuidToStringA](/windows/win32/api/rpcdce/nf-rpcdce-uuidtostring) | Introduced into rpcrt4.dll in 10.0.16299. |
| [UuidIsNil](/windows/win32/api/rpcdce/nf-rpcdce-uuidisnil) | Introduced into rpcrt4.dll in 10.0.16299. |
| [UuidHash](/windows/win32/api/rpcdce/nf-rpcdce-uuidhash) | Introduced into rpcrt4.dll in 10.0.16299. |
| [UuidFromStringW](/windows/win32/api/rpcdce/nf-rpcdce-uuidfromstring) | Introduced into rpcrt4.dll in 10.0.16299. |
| [UuidFromStringA](/windows/win32/api/rpcdce/nf-rpcdce-uuidfromstring) | Introduced into rpcrt4.dll in 10.0.16299. |
| [UuidEqual](/windows/win32/api/rpcdce/nf-rpcdce-uuidequal) | Introduced into rpcrt4.dll in 10.0.16299. |
| [UuidCreateSequential](/windows/win32/api/rpcdce/nf-rpcdce-uuidcreatesequential) | Introduced into rpcrt4.dll in 10.0.16299. |
| [UuidCreateNil](/windows/win32/api/rpcdce/nf-rpcdce-uuidcreatenil) | Introduced into rpcrt4.dll in 10.0.16299. |
| [UuidCreate](/windows/win32/api/rpcdce/nf-rpcdce-uuidcreate) | Introduced into rpcrt4.dll in 10.0.16299. |
| [UuidCompare](/windows/win32/api/rpcdce/nf-rpcdce-uuidcompare) | Introduced into rpcrt4.dll in 10.0.16299. |
| [RpcTestCancel](/windows/win32/api/rpcdce/nf-rpcdce-rpctestcancel) | Introduced into rpcrt4.dll in 10.0.16299. |
| [RpcStringFreeW](/windows/win32/api/rpcdce/nf-rpcdce-rpcstringfree) | Introduced into rpcrt4.dll in 10.0.16299. |
| [RpcStringFreeA](/windows/win32/api/rpcdce/nf-rpcdce-rpcstringfree) | Introduced into rpcrt4.dll in 10.0.16299. |
| [RpcStringBindingParseW](/windows/win32/api/rpcdce/nf-rpcdce-rpcstringbindingparse) | Introduced into rpcrt4.dll in 10.0.16299. |
| [RpcStringBindingParseA](/windows/win32/api/rpcdce/nf-rpcdce-rpcstringbindingparse) | Introduced into rpcrt4.dll in 10.0.16299. |
| [RpcStringBindingComposeW](/windows/win32/api/rpcdce/nf-rpcdce-rpcstringbindingcompose) | Introduced into rpcrt4.dll in 10.0.16299. |
| [RpcStringBindingComposeA](/windows/win32/api/rpcdce/nf-rpcdce-rpcstringbindingcompose) | Introduced into rpcrt4.dll in 10.0.16299. |
| [RpcRaiseException](/windows/win32/api/rpcdce/nf-rpcdce-rpcraiseexception) | Introduced into rpcrt4.dll in 10.0.16299. |
| [RpcNetworkIsProtseqValidW](/windows/win32/api/rpcdce/nf-rpcdce-rpcnetworkisprotseqvalid) | Introduced into rpcrt4.dll in 10.0.16299. |
| [RpcNetworkIsProtseqValidA](/windows/win32/api/rpcdce/nf-rpcdce-rpcnetworkisprotseqvalid) | Introduced into rpcrt4.dll in 10.0.16299. |
| [RpcMgmtSetComTimeout](/windows/win32/api/rpcdce/nf-rpcdce-rpcmgmtsetcomtimeout) | Introduced into rpcrt4.dll in 10.0.16299. |
| [RpcMgmtSetCancelTimeout](/windows/win32/api/rpcdce/nf-rpcdce-rpcmgmtsetcanceltimeout) | Introduced into rpcrt4.dll in 10.0.16299. |
| [RpcMgmtIsServerListening](/windows/win32/api/rpcdce/nf-rpcdce-rpcmgmtisserverlistening) | Introduced into rpcrt4.dll in 10.0.16299. |
| [RpcMgmtInqStats](/windows/win32/api/rpcdce/nf-rpcdce-rpcmgmtinqstats) | Introduced into rpcrt4.dll in 10.0.16299. |
| [RpcMgmtInqServerPrincNameW](/windows/win32/api/rpcdce/nf-rpcdce-rpcmgmtinqserverprincname) | Introduced into rpcrt4.dll in 10.0.16299. |
| [RpcMgmtInqServerPrincNameA](/windows/win32/api/rpcdce/nf-rpcdce-rpcmgmtinqserverprincname) | Introduced into rpcrt4.dll in 10.0.16299. |
| [RpcExceptionFilter](/windows/win32/api/rpcdce/nf-rpcdce-rpcexceptionfilter) | Introduced into rpcrt4.dll in 10.0.16299. |
| [RpcErrorStartEnumeration](/windows/win32/api/rpcasync/nf-rpcasync-rpcerrorstartenumeration) | Introduced into rpcrt4.dll in 10.0.16299. |
| [RpcErrorSaveErrorInfo](/windows/win32/api/rpcasync/nf-rpcasync-rpcerrorsaveerrorinfo) | Introduced into rpcrt4.dll in 10.0.16299. |
| [RpcErrorResetEnumeration](/windows/win32/api/rpcasync/nf-rpcasync-rpcerrorresetenumeration) | Introduced into rpcrt4.dll in 10.0.16299. |
| [RpcErrorLoadErrorInfo](/windows/win32/api/rpcasync/nf-rpcasync-rpcerrorloaderrorinfo) | Introduced into rpcrt4.dll in 10.0.16299. |
| [RpcErrorGetNumberOfRecords](/windows/win32/api/rpcasync/nf-rpcasync-rpcerrorgetnumberofrecords) | Introduced into rpcrt4.dll in 10.0.16299. |
| [RpcErrorGetNextRecord](/windows/win32/api/rpcasync/nf-rpcasync-rpcerrorgetnextrecord) | Introduced into rpcrt4.dll in 10.0.16299. |
| [RpcErrorEndEnumeration](/windows/win32/api/rpcasync/nf-rpcasync-rpcerrorendenumeration) | Introduced into rpcrt4.dll in 10.0.16299. |
| [RpcErrorClearInformation](/windows/win32/api/rpcasync/nf-rpcasync-rpcerrorclearinformation) | Introduced into rpcrt4.dll in 10.0.16299. |
| [RpcErrorAddRecord](/windows/win32/api/rpcasync/nf-rpcasync-rpcerroraddrecord) | Introduced into rpcrt4.dll in 10.0.16299. |
| [RpcEpResolveBinding](/windows/win32/api/rpcdce/nf-rpcdce-rpcepresolvebinding) | Introduced into rpcrt4.dll in 10.0.16299. |
| [RpcBindingUnbind](/windows/win32/api/rpcasync/nf-rpcasync-rpcbindingunbind) | Introduced into rpcrt4.dll in 10.0.16299. |
| [RpcBindingToStringBindingW](/windows/win32/api/rpcdce/nf-rpcdce-rpcbindingtostringbinding) | Introduced into rpcrt4.dll in 10.0.16299. |
| [RpcBindingToStringBindingA](/windows/win32/api/rpcdce/nf-rpcdce-rpcbindingtostringbinding) | Introduced into rpcrt4.dll in 10.0.16299. |
| [RpcBindingSetOption](/windows/win32/api/rpcdce/nf-rpcdce-rpcbindingsetoption) | Introduced into rpcrt4.dll in 10.0.16299. |
| [RpcBindingSetObject](/windows/win32/api/rpcdce/nf-rpcdce-rpcbindingsetobject) | Introduced into rpcrt4.dll in 10.0.16299. |
| [RpcBindingSetAuthInfoW](/windows/win32/api/rpcdce/nf-rpcdce-rpcbindingsetauthinfo) | Introduced into rpcrt4.dll in 10.0.16299. |
| [RpcBindingSetAuthInfoExW](/windows/win32/api/rpcdce/nf-rpcdce-rpcbindingsetauthinfoexa) | Introduced into rpcrt4.dll in 10.0.16299. |
| [RpcBindingSetAuthInfoExA](/windows/win32/api/rpcdce/nf-rpcdce-rpcbindingsetauthinfoexa) | Introduced into rpcrt4.dll in 10.0.16299. |
| [RpcBindingSetAuthInfoA](/windows/win32/api/rpcdce/nf-rpcdce-rpcbindingsetauthinfo) | Introduced into rpcrt4.dll in 10.0.16299. |
| [RpcBindingReset](/windows/win32/api/rpcdce/nf-rpcdce-rpcbindingreset) | Introduced into rpcrt4.dll in 10.0.16299. |
| [RpcBindingInqOption](/windows/win32/api/rpcdce/nf-rpcdce-rpcbindinginqoption) | Introduced into rpcrt4.dll in 10.0.16299. |
| [RpcBindingInqObject](/windows/win32/api/rpcdce/nf-rpcdce-rpcbindinginqobject) | Introduced into rpcrt4.dll in 10.0.16299. |
| [RpcBindingInqAuthInfoW](/windows/win32/api/rpcdce/nf-rpcdce-rpcbindinginqauthinfo) | Introduced into rpcrt4.dll in 10.0.16299. |
| [RpcBindingInqAuthInfoExW](/windows/win32/api/rpcdce/nf-rpcdce-rpcbindinginqauthinfoexa) | Introduced into rpcrt4.dll in 10.0.16299. |
| [RpcBindingInqAuthInfoExA](/windows/win32/api/rpcdce/nf-rpcdce-rpcbindinginqauthinfoexa) | Introduced into rpcrt4.dll in 10.0.16299. |
| [RpcBindingInqAuthInfoA](/windows/win32/api/rpcdce/nf-rpcdce-rpcbindinginqauthinfo) | Introduced into rpcrt4.dll in 10.0.16299. |
| [RpcBindingFromStringBindingW](/windows/win32/api/rpcdce/nf-rpcdce-rpcbindingfromstringbinding) | Introduced into rpcrt4.dll in 10.0.16299. |
| [RpcBindingFromStringBindingA](/windows/win32/api/rpcdce/nf-rpcdce-rpcbindingfromstringbinding) | Introduced into rpcrt4.dll in 10.0.16299. |
| [RpcBindingFree](/windows/win32/api/rpcdce/nf-rpcdce-rpcbindingfree) | Introduced into rpcrt4.dll in 10.0.16299. |
| [RpcBindingCreateW](/windows/win32/api/rpcdce/nf-rpcdce-rpcbindingcreatea) | Introduced into rpcrt4.dll in 10.0.16299. |
| [RpcBindingCreateA](/windows/win32/api/rpcdce/nf-rpcdce-rpcbindingcreatea) | Introduced into rpcrt4.dll in 10.0.16299. |
| [RpcBindingCopy](/windows/win32/api/rpcdce/nf-rpcdce-rpcbindingcopy) | Introduced into rpcrt4.dll in 10.0.16299. |
| [RpcBindingBind](/windows/win32/api/rpcasync/nf-rpcasync-rpcbindingbind) | Introduced into rpcrt4.dll in 10.0.16299. |
| [RpcAsyncInitializeHandle](/windows/win32/api/rpcasync/nf-rpcasync-rpcasyncinitializehandle) | Introduced into rpcrt4.dll in 10.0.16299. |
| [RpcAsyncGetCallStatus](/windows/win32/api/rpcasync/nf-rpcasync-rpcasyncgetcallstatus) | Introduced into rpcrt4.dll in 10.0.16299. |
| [RpcAsyncCompleteCall](/windows/win32/api/rpcasync/nf-rpcasync-rpcasynccompletecall) | Introduced into rpcrt4.dll in 10.0.16299. |
| [RpcAsyncCancelCall](/windows/win32/api/rpcasync/nf-rpcasync-rpcasynccancelcall) | Introduced into rpcrt4.dll in 10.0.16299. |
| [RpcAsyncAbortCall](/windows/win32/api/rpcasync/nf-rpcasync-rpcasyncabortcall) | Introduced into rpcrt4.dll in 10.0.16299. |
| [NdrClientCall4](/windows/win32/api/rpcndr/nf-rpcndr-ndrclientcall4) | Introduced into rpcrt4.dll in 10.0.16299. |
| [NdrAsyncClientCall2](/windows/win32/api/rpcndr/nf-rpcndr-ndrasyncclientcall2) | Introduced into rpcrt4.dll in 10.0.16299. |
| [DceErrorInqTextW](/windows/win32/api/rpcdce/nf-rpcdce-dceerrorinqtext) | Introduced into rpcrt4.dll in 10.0.16299. |
| [DceErrorInqTextA](/windows/win32/api/rpcdce/nf-rpcdce-dceerrorinqtext) | Introduced into rpcrt4.dll in 10.0.16299. |


## APIs from uiautomationcore.dll

| API | Requirements |
| -----| --------------|
| [UiaClientsAreListening](/windows/win32/api/uiautomationcoreapi/nf-uiautomationcoreapi-uiaclientsarelistening) | Introduced into uiautomationcore.dll in 10.0.10240. Moved into ext-ms-win-uiacore-l1-1-1.dll in 10.0.16299. |
| [UiaDisconnectAllProviders](/windows/win32/api/uiautomationcoreapi/nf-uiautomationcoreapi-uiadisconnectallproviders) | Introduced into uiautomationcore.dll in 10.0.10240. Moved into ext-ms-win-uiacore-l1-1-2.dll in 10.0.16299. |
| [UiaDisconnectProvider](/windows/win32/api/uiautomationcoreapi/nf-uiautomationcoreapi-uiadisconnectprovider) | Introduced into uiautomationcore.dll in 10.0.10240. Moved into ext-ms-win-uiacore-l1-1-1.dll in 10.0.16299. |
| [UiaGetReservedMixedAttributeValue](/windows/win32/api/uiautomationcoreapi/nf-uiautomationcoreapi-uiagetreservedmixedattributevalue) | Introduced into uiautomationcore.dll in 10.0.10240. Moved into ext-ms-win-uiacore-l1-1-1.dll in 10.0.16299. |
| [UiaGetReservedNotSupportedValue](/windows/win32/api/uiautomationcoreapi/nf-uiautomationcoreapi-uiagetreservednotsupportedvalue) | Introduced into uiautomationcore.dll in 10.0.10240. Moved into ext-ms-win-uiacore-l1-1-1.dll in 10.0.16299. |
| [UiaHostProviderFromHwnd](/windows/win32/api/uiautomationcoreapi/nf-uiautomationcoreapi-uiahostproviderfromhwnd) | Introduced into uiautomationcore.dll in 10.0.10240. Moved into ext-ms-win-uiacore-l1-1-0.dll in 10.0.16299. |
| [UiaProviderForNonClient](/windows/win32/api/uiautomationcoreapi/nf-uiautomationcoreapi-uiaproviderfornonclient) | Introduced into uiautomationcore.dll in 10.0.10240. |
| [UiaProviderFromIAccessible](/windows/win32/api/uiautomationcoreapi/nf-uiautomationcoreapi-uiaproviderfromiaccessible) | Introduced into uiautomationcore.dll in 10.0.10240. |
| [UiaRaiseAsyncContentLoadedEvent](/windows/win32/api/uiautomationcoreapi/nf-uiautomationcoreapi-uiaraiseasynccontentloadedevent) | Introduced into uiautomationcore.dll in 10.0.10240. |
| [UiaRaiseAutomationEvent](/windows/win32/api/uiautomationcoreapi/nf-uiautomationcoreapi-uiaraiseautomationevent) | Introduced into uiautomationcore.dll in 10.0.10240. Moved into ext-ms-win-uiacore-l1-1-1.dll in 10.0.16299. |
| [UiaRaiseAutomationPropertyChangedEvent](/windows/win32/api/uiautomationcoreapi/nf-uiautomationcoreapi-uiaraiseautomationpropertychangedevent) | Introduced into uiautomationcore.dll in 10.0.10240. Moved into ext-ms-win-uiacore-l1-1-1.dll in 10.0.16299. |
| [UiaRaiseStructureChangedEvent](/windows/win32/api/uiautomationcoreapi/nf-uiautomationcoreapi-uiaraisestructurechangedevent) | Introduced into uiautomationcore.dll in 10.0.10240. Moved into ext-ms-win-uiacore-l1-1-1.dll in 10.0.16299. |
| [UiaRaiseTextEditTextChangedEvent](/windows/win32/api/uiautomationcoreapi/nf-uiautomationcoreapi-uiaraisetextedittextchangedevent) | Introduced into uiautomationcore.dll in 10.0.10240. Moved into ext-ms-win-uiacore-l1-1-2.dll in 10.0.16299. |
| [UiaReturnRawElementProvider](/windows/win32/api/uiautomationcoreapi/nf-uiautomationcoreapi-uiareturnrawelementprovider) | Introduced into uiautomationcore.dll in 10.0.10240. Moved into ext-ms-win-uiacore-l1-1-0.dll in 10.0.16299. |
| [UiaRaiseChangesEvent](/windows/win32/api/uiautomationcoreapi/nf-uiautomationcoreapi-uiaraisechangesevent) | Introduced into uiautomationcore.dll in 10.0.14393. Moved into ext-ms-win-uiacore-l1-1-3.dll in 10.0.16299. |


## APIs from urlmon.dll

| API | Requirements |
| -----| --------------|
| [CreateUri](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms775098(v=vs.85)) | Introduced into urlmon.dll in 10.0.10240. Moved into ext-ms-win-core-iuri-l1-1-0.dll in 10.0.16299. |
| [CreateUriWithFragment](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms775100(v=vs.85)) | Introduced into urlmon.dll in 10.0.10240. Moved into ext-ms-win-core-iuri-l1-1-0.dll in 10.0.16299. |
| [UrlMkGetSessionOption](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms775124(v=vs.85)) | Introduced into urlmon.dll in 10.0.16299. |
| [UrlMkSetSessionOption](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/ms775125(v=vs.85)) | Introduced into urlmon.dll in 10.0.16299. |


## APIs from webservices.dll

| API | Requirements |
| -----| --------------|
| [WsAbandonCall](/windows/win32/api/webservices/nf-webservices-wsabandoncall) | Introduced into webservices.dll in 10.0.10240. |
| [WsAbandonMessage](/windows/win32/api/webservices/nf-webservices-wsabandonmessage) | Introduced into webservices.dll in 10.0.10240. |
| [WsAbortChannel](/windows/win32/api/webservices/nf-webservices-wsabortchannel) | Introduced into webservices.dll in 10.0.10240. |
| [WsAbortServiceProxy](/windows/win32/api/webservices/nf-webservices-wsabortserviceproxy) | Introduced into webservices.dll in 10.0.10240. |
| [WsAddCustomHeader](/windows/win32/api/webservices/nf-webservices-wsaddcustomheader) | Introduced into webservices.dll in 10.0.10240. |
| [WsAddErrorString](/windows/win32/api/webservices/nf-webservices-wsadderrorstring) | Introduced into webservices.dll in 10.0.10240. |
| [WsAddMappedHeader](/windows/win32/api/webservices/nf-webservices-wsaddmappedheader) | Introduced into webservices.dll in 10.0.10240. |
| [WsAddressMessage](/windows/win32/api/webservices/nf-webservices-wsaddressmessage) | Introduced into webservices.dll in 10.0.10240. |
| [WsAlloc](/windows/win32/api/webservices/nf-webservices-wsalloc) | Introduced into webservices.dll in 10.0.10240. |
| [WsAsyncExecute](/windows/win32/api/webservices/nf-webservices-wsasyncexecute) | Introduced into webservices.dll in 10.0.10240. |
| [WsCall](/windows/win32/api/webservices/nf-webservices-wscall) | Introduced into webservices.dll in 10.0.10240. |
| [WsCheckMustUnderstandHeaders](/windows/win32/api/webservices/nf-webservices-wscheckmustunderstandheaders) | Introduced into webservices.dll in 10.0.10240. |
| [WsCloseChannel](/windows/win32/api/webservices/nf-webservices-wsclosechannel) | Introduced into webservices.dll in 10.0.10240. |
| [WsCloseServiceProxy](/windows/win32/api/webservices/nf-webservices-wscloseserviceproxy) | Introduced into webservices.dll in 10.0.10240. |
| [WsCombineUrl](/windows/win32/api/webservices/nf-webservices-wscombineurl) | Introduced into webservices.dll in 10.0.10240. |
| [WsCopyError](/windows/win32/api/webservices/nf-webservices-wscopyerror) | Introduced into webservices.dll in 10.0.10240. |
| [WsCopyNode](/windows/win32/api/webservices/nf-webservices-wscopynode) | Introduced into webservices.dll in 10.0.10240. |
| [WsCreateChannel](/windows/win32/api/webservices/nf-webservices-wscreatechannel) | Introduced into webservices.dll in 10.0.10240. |
| [WsCreateError](/windows/win32/api/webservices/nf-webservices-wscreateerror) | Introduced into webservices.dll in 10.0.10240. |
| [WsCreateFaultFromError](/windows/win32/api/webservices/nf-webservices-wscreatefaultfromerror) | Introduced into webservices.dll in 10.0.10240. |
| [WsCreateHeap](/windows/win32/api/webservices/nf-webservices-wscreateheap) | Introduced into webservices.dll in 10.0.10240. |
| [WsCreateMessage](/windows/win32/api/webservices/nf-webservices-wscreatemessage) | Introduced into webservices.dll in 10.0.10240. |
| [WsCreateMessageForChannel](/windows/win32/api/webservices/nf-webservices-wscreatemessageforchannel) | Introduced into webservices.dll in 10.0.10240. |
| [WsCreateMetadata](/windows/win32/api/webservices/nf-webservices-wscreatemetadata) | Introduced into webservices.dll in 10.0.10240. |
| [WsCreateReader](/windows/win32/api/webservices/nf-webservices-wscreatereader) | Introduced into webservices.dll in 10.0.10240. |
| [WsCreateServiceProxy](/windows/win32/api/webservices/nf-webservices-wscreateserviceproxy) | Introduced into webservices.dll in 10.0.10240. |
| [WsCreateServiceProxyFromTemplate](/windows/win32/api/webservices/nf-webservices-wscreateserviceproxyfromtemplate) | Introduced into webservices.dll in 10.0.10240. |
| [WsCreateWriter](/windows/win32/api/webservices/nf-webservices-wscreatewriter) | Introduced into webservices.dll in 10.0.10240. |
| [WsCreateXmlBuffer](/windows/win32/api/webservices/nf-webservices-wscreatexmlbuffer) | Introduced into webservices.dll in 10.0.10240. |
| [WsCreateXmlSecurityToken](/windows/win32/api/webservices/nf-webservices-wscreatexmlsecuritytoken) | Introduced into webservices.dll in 10.0.10240. |
| [WsDateTimeToFileTime](/windows/win32/api/webservices/nf-webservices-wsdatetimetofiletime) | Introduced into webservices.dll in 10.0.10240. |
| [WsDecodeUrl](/windows/win32/api/webservices/nf-webservices-wsdecodeurl) | Introduced into webservices.dll in 10.0.10240. |
| [WsEncodeUrl](/windows/win32/api/webservices/nf-webservices-wsencodeurl) | Introduced into webservices.dll in 10.0.10240. |
| [WsEndReaderCanonicalization](/windows/win32/api/webservices/nf-webservices-wsendreadercanonicalization) | Introduced into webservices.dll in 10.0.10240. |
| [WsEndWriterCanonicalization](/windows/win32/api/webservices/nf-webservices-wsendwritercanonicalization) | Introduced into webservices.dll in 10.0.10240. |
| [WsFileTimeToDateTime](/windows/win32/api/webservices/nf-webservices-wsfiletimetodatetime) | Introduced into webservices.dll in 10.0.10240. |
| [WsFillBody](/windows/win32/api/webservices/nf-webservices-wsfillbody) | Introduced into webservices.dll in 10.0.10240. |
| [WsFillReader](/windows/win32/api/webservices/nf-webservices-wsfillreader) | Introduced into webservices.dll in 10.0.10240. |
| [WsFindAttribute](/windows/win32/api/webservices/nf-webservices-wsfindattribute) | Introduced into webservices.dll in 10.0.10240. |
| [WsFlushBody](/windows/win32/api/webservices/nf-webservices-wsflushbody) | Introduced into webservices.dll in 10.0.10240. |
| [WsFlushWriter](/windows/win32/api/webservices/nf-webservices-wsflushwriter) | Introduced into webservices.dll in 10.0.10240. |
| [WsFreeChannel](/windows/win32/api/webservices/nf-webservices-wsfreechannel) | Introduced into webservices.dll in 10.0.10240. |
| [WsFreeError](/windows/win32/api/webservices/nf-webservices-wsfreeerror) | Introduced into webservices.dll in 10.0.10240. |
| [WsFreeHeap](/windows/win32/api/webservices/nf-webservices-wsfreeheap) | Introduced into webservices.dll in 10.0.10240. |
| [WsFreeMessage](/windows/win32/api/webservices/nf-webservices-wsfreemessage) | Introduced into webservices.dll in 10.0.10240. |
| [WsFreeMetadata](/windows/win32/api/webservices/nf-webservices-wsfreemetadata) | Introduced into webservices.dll in 10.0.10240. |
| [WsFreeReader](/windows/win32/api/webservices/nf-webservices-wsfreereader) | Introduced into webservices.dll in 10.0.10240. |
| [WsFreeSecurityToken](/windows/win32/api/webservices/nf-webservices-wsfreesecuritytoken) | Introduced into webservices.dll in 10.0.10240. |
| [WsFreeServiceProxy](/windows/win32/api/webservices/nf-webservices-wsfreeserviceproxy) | Introduced into webservices.dll in 10.0.10240. |
| [WsFreeWriter](/windows/win32/api/webservices/nf-webservices-wsfreewriter) | Introduced into webservices.dll in 10.0.10240. |
| [WsGetChannelProperty](/windows/win32/api/webservices/nf-webservices-wsgetchannelproperty) | Introduced into webservices.dll in 10.0.10240. |
| [WsGetCustomHeader](/windows/win32/api/webservices/nf-webservices-wsgetcustomheader) | Introduced into webservices.dll in 10.0.10240. |
| [WsGetDictionary](/windows/win32/api/webservices/nf-webservices-wsgetdictionary) | Introduced into webservices.dll in 10.0.10240. |
| [WsGetErrorProperty](/windows/win32/api/webservices/nf-webservices-wsgeterrorproperty) | Introduced into webservices.dll in 10.0.10240. |
| [WsGetErrorString](/windows/win32/api/webservices/nf-webservices-wsgeterrorstring) | Introduced into webservices.dll in 10.0.10240. |
| [WsGetFaultErrorDetail](/windows/win32/api/webservices/nf-webservices-wsgetfaulterrordetail) | Introduced into webservices.dll in 10.0.10240. |
| [WsGetFaultErrorProperty](/windows/win32/api/webservices/nf-webservices-wsgetfaulterrorproperty) | Introduced into webservices.dll in 10.0.10240. |
| [WsGetHeader](/windows/win32/api/webservices/nf-webservices-wsgetheader) | Introduced into webservices.dll in 10.0.10240. |
| [WsGetHeaderAttributes](/windows/win32/api/webservices/nf-webservices-wsgetheaderattributes) | Introduced into webservices.dll in 10.0.10240. |
| [WsGetHeapProperty](/windows/win32/api/webservices/nf-webservices-wsgetheapproperty) | Introduced into webservices.dll in 10.0.10240. |
| [WsGetMappedHeader](/windows/win32/api/webservices/nf-webservices-wsgetmappedheader) | Introduced into webservices.dll in 10.0.10240. |
| [WsGetMessageProperty](/windows/win32/api/webservices/nf-webservices-wsgetmessageproperty) | Introduced into webservices.dll in 10.0.10240. |
| [WsGetMetadataEndpoints](/windows/win32/api/webservices/nf-webservices-wsgetmetadataendpoints) | Introduced into webservices.dll in 10.0.10240. |
| [WsGetMetadataProperty](/windows/win32/api/webservices/nf-webservices-wsgetmetadataproperty) | Introduced into webservices.dll in 10.0.10240. |
| [WsGetMissingMetadataDocumentAddress](/windows/win32/api/webservices/nf-webservices-wsgetmissingmetadatadocumentaddress) | Introduced into webservices.dll in 10.0.10240. |
| [WsGetNamespaceFromPrefix](/windows/win32/api/webservices/nf-webservices-wsgetnamespacefromprefix) | Introduced into webservices.dll in 10.0.10240. |
| [WsGetPolicyAlternativeCount](/windows/win32/api/webservices/nf-webservices-wsgetpolicyalternativecount) | Introduced into webservices.dll in 10.0.10240. |
| [WsGetPolicyProperty](/windows/win32/api/webservices/nf-webservices-wsgetpolicyproperty) | Introduced into webservices.dll in 10.0.10240. |
| [WsGetPrefixFromNamespace](/windows/win32/api/webservices/nf-webservices-wsgetprefixfromnamespace) | Introduced into webservices.dll in 10.0.10240. |
| [WsGetReaderNode](/windows/win32/api/webservices/nf-webservices-wsgetreadernode) | Introduced into webservices.dll in 10.0.10240. |
| [WsGetReaderPosition](/windows/win32/api/webservices/nf-webservices-wsgetreaderposition) | Introduced into webservices.dll in 10.0.10240. |
| [WsGetReaderProperty](/windows/win32/api/webservices/nf-webservices-wsgetreaderproperty) | Introduced into webservices.dll in 10.0.10240. |
| [WsGetSecurityContextProperty](/windows/win32/api/webservices/nf-webservices-wsgetsecuritycontextproperty) | Introduced into webservices.dll in 10.0.10240. |
| [WsGetSecurityTokenProperty](/windows/win32/api/webservices/nf-webservices-wsgetsecuritytokenproperty) | Introduced into webservices.dll in 10.0.10240. |
| [WsGetServiceProxyProperty](/windows/win32/api/webservices/nf-webservices-wsgetserviceproxyproperty) | Introduced into webservices.dll in 10.0.10240. |
| [WsGetWriterPosition](/windows/win32/api/webservices/nf-webservices-wsgetwriterposition) | Introduced into webservices.dll in 10.0.10240. |
| [WsGetWriterProperty](/windows/win32/api/webservices/nf-webservices-wsgetwriterproperty) | Introduced into webservices.dll in 10.0.10240. |
| [WsGetXmlAttribute](/windows/win32/api/webservices/nf-webservices-wsgetxmlattribute) | Introduced into webservices.dll in 10.0.10240. |
| [WsInitializeMessage](/windows/win32/api/webservices/nf-webservices-wsinitializemessage) | Introduced into webservices.dll in 10.0.10240. |
| [WsMarkHeaderAsUnderstood](/windows/win32/api/webservices/nf-webservices-wsmarkheaderasunderstood) | Introduced into webservices.dll in 10.0.10240. |
| [WsMatchPolicyAlternative](/windows/win32/api/webservices/nf-webservices-wsmatchpolicyalternative) | Introduced into webservices.dll in 10.0.10240. |
| [WsMoveReader](/windows/win32/api/webservices/nf-webservices-wsmovereader) | Introduced into webservices.dll in 10.0.10240. |
| [WsMoveWriter](/windows/win32/api/webservices/nf-webservices-wsmovewriter) | Introduced into webservices.dll in 10.0.10240. |
| [WsOpenChannel](/windows/win32/api/webservices/nf-webservices-wsopenchannel) | Introduced into webservices.dll in 10.0.10240. |
| [WsOpenServiceProxy](/windows/win32/api/webservices/nf-webservices-wsopenserviceproxy) | Introduced into webservices.dll in 10.0.10240. |
| [WsPullBytes](/windows/win32/api/webservices/nf-webservices-wspullbytes) | Introduced into webservices.dll in 10.0.10240. |
| [WsPushBytes](/windows/win32/api/webservices/nf-webservices-wspushbytes) | Introduced into webservices.dll in 10.0.10240. |
| [WsReadArray](/windows/win32/api/webservices/nf-webservices-wsreadarray) | Introduced into webservices.dll in 10.0.10240. |
| [WsReadAttribute](/windows/win32/api/webservices/nf-webservices-wsreadattribute) | Introduced into webservices.dll in 10.0.10240. |
| [WsReadBody](/windows/win32/api/webservices/nf-webservices-wsreadbody) | Introduced into webservices.dll in 10.0.10240. |
| [WsReadBytes](/windows/win32/api/webservices/nf-webservices-wsreadbytes) | Introduced into webservices.dll in 10.0.10240. |
| [WsReadChars](/windows/win32/api/webservices/nf-webservices-wsreadchars) | Introduced into webservices.dll in 10.0.10240. |
| [WsReadCharsUtf8](/windows/win32/api/webservices/nf-webservices-wsreadcharsutf8) | Introduced into webservices.dll in 10.0.10240. |
| [WsReadElement](/windows/win32/api/webservices/nf-webservices-wsreadelement) | Introduced into webservices.dll in 10.0.10240. |
| [WsReadEndAttribute](/windows/win32/api/webservices/nf-webservices-wsreadendattribute) | Introduced into webservices.dll in 10.0.10240. |
| [WsReadEndElement](/windows/win32/api/webservices/nf-webservices-wsreadendelement) | Introduced into webservices.dll in 10.0.10240. |
| [WsReadEndpointAddressExtension](/windows/win32/api/webservices/nf-webservices-wsreadendpointaddressextension) | Introduced into webservices.dll in 10.0.10240. |
| [WsReadEnvelopeEnd](/windows/win32/api/webservices/nf-webservices-wsreadenvelopeend) | Introduced into webservices.dll in 10.0.10240. |
| [WsReadEnvelopeStart](/windows/win32/api/webservices/nf-webservices-wsreadenvelopestart) | Introduced into webservices.dll in 10.0.10240. |
| [WsReadMessageEnd](/windows/win32/api/webservices/nf-webservices-wsreadmessageend) | Introduced into webservices.dll in 10.0.10240. |
| [WsReadMessageStart](/windows/win32/api/webservices/nf-webservices-wsreadmessagestart) | Introduced into webservices.dll in 10.0.10240. |
| [WsReadMetadata](/windows/win32/api/webservices/nf-webservices-wsreadmetadata) | Introduced into webservices.dll in 10.0.10240. |
| [WsReadNode](/windows/win32/api/webservices/nf-webservices-wsreadnode) | Introduced into webservices.dll in 10.0.10240. |
| [WsReadQualifiedName](/windows/win32/api/webservices/nf-webservices-wsreadqualifiedname) | Introduced into webservices.dll in 10.0.10240. |
| [WsReadStartAttribute](/windows/win32/api/webservices/nf-webservices-wsreadstartattribute) | Introduced into webservices.dll in 10.0.10240. |
| [WsReadStartElement](/windows/win32/api/webservices/nf-webservices-wsreadstartelement) | Introduced into webservices.dll in 10.0.10240. |
| [WsReadToStartElement](/windows/win32/api/webservices/nf-webservices-wsreadtostartelement) | Introduced into webservices.dll in 10.0.10240. |
| [WsReadType](/windows/win32/api/webservices/nf-webservices-wsreadtype) | Introduced into webservices.dll in 10.0.10240. |
| [WsReadValue](/windows/win32/api/webservices/nf-webservices-wsreadvalue) | Introduced into webservices.dll in 10.0.10240. |
| [WsReadXmlBuffer](/windows/win32/api/webservices/nf-webservices-wsreadxmlbuffer) | Introduced into webservices.dll in 10.0.10240. |
| [WsReadXmlBufferFromBytes](/windows/win32/api/webservices/nf-webservices-wsreadxmlbufferfrombytes) | Introduced into webservices.dll in 10.0.10240. |
| [WsReceiveMessage](/windows/win32/api/webservices/nf-webservices-wsreceivemessage) | Introduced into webservices.dll in 10.0.10240. |
| [WsRemoveCustomHeader](/windows/win32/api/webservices/nf-webservices-wsremovecustomheader) | Introduced into webservices.dll in 10.0.10240. |
| [WsRemoveHeader](/windows/win32/api/webservices/nf-webservices-wsremoveheader) | Introduced into webservices.dll in 10.0.10240. |
| [WsRemoveMappedHeader](/windows/win32/api/webservices/nf-webservices-wsremovemappedheader) | Introduced into webservices.dll in 10.0.10240. |
| [WsRemoveNode](/windows/win32/api/webservices/nf-webservices-wsremovenode) | Introduced into webservices.dll in 10.0.10240. |
| [WsRequestReply](/windows/win32/api/webservices/nf-webservices-wsrequestreply) | Introduced into webservices.dll in 10.0.10240. |
| [WsRequestSecurityToken](/windows/win32/api/webservices/nf-webservices-wsrequestsecuritytoken) | Introduced into webservices.dll in 10.0.10240. |
| [WsResetChannel](/windows/win32/api/webservices/nf-webservices-wsresetchannel) | Introduced into webservices.dll in 10.0.10240. |
| [WsResetError](/windows/win32/api/webservices/nf-webservices-wsreseterror) | Introduced into webservices.dll in 10.0.10240. |
| [WsResetHeap](/windows/win32/api/webservices/nf-webservices-wsresetheap) | Introduced into webservices.dll in 10.0.10240. |
| [WsResetMessage](/windows/win32/api/webservices/nf-webservices-wsresetmessage) | Introduced into webservices.dll in 10.0.10240. |
| [WsResetMetadata](/windows/win32/api/webservices/nf-webservices-wsresetmetadata) | Introduced into webservices.dll in 10.0.10240. |
| [WsResetServiceProxy](/windows/win32/api/webservices/nf-webservices-wsresetserviceproxy) | Introduced into webservices.dll in 10.0.10240. |
| [WsRevokeSecurityContext](/windows/win32/api/webservices/nf-webservices-wsrevokesecuritycontext) | Introduced into webservices.dll in 10.0.10240. |
| [WsSendFaultMessageForError](/windows/win32/api/webservices/nf-webservices-wssendfaultmessageforerror) | Introduced into webservices.dll in 10.0.10240. |
| [WsSendMessage](/windows/win32/api/webservices/nf-webservices-wssendmessage) | Introduced into webservices.dll in 10.0.10240. |
| [WsSendReplyMessage](/windows/win32/api/webservices/nf-webservices-wssendreplymessage) | Introduced into webservices.dll in 10.0.10240. |
| [WsSetChannelProperty](/windows/win32/api/webservices/nf-webservices-wssetchannelproperty) | Introduced into webservices.dll in 10.0.10240. |
| [WsSetErrorProperty](/windows/win32/api/webservices/nf-webservices-wsseterrorproperty) | Introduced into webservices.dll in 10.0.10240. |
| [WsSetFaultErrorDetail](/windows/win32/api/webservices/nf-webservices-wssetfaulterrordetail) | Introduced into webservices.dll in 10.0.10240. |
| [WsSetFaultErrorProperty](/windows/win32/api/webservices/nf-webservices-wssetfaulterrorproperty) | Introduced into webservices.dll in 10.0.10240. |
| [WsSetHeader](/windows/win32/api/webservices/nf-webservices-wssetheader) | Introduced into webservices.dll in 10.0.10240. |
| [WsSetInput](/windows/win32/api/webservices/nf-webservices-wssetinput) | Introduced into webservices.dll in 10.0.10240. |
| [WsSetInputToBuffer](/windows/win32/api/webservices/nf-webservices-wssetinputtobuffer) | Introduced into webservices.dll in 10.0.10240. |
| [WsSetMessageProperty](/windows/win32/api/webservices/nf-webservices-wssetmessageproperty) | Introduced into webservices.dll in 10.0.10240. |
| [WsSetOutput](/windows/win32/api/webservices/nf-webservices-wssetoutput) | Introduced into webservices.dll in 10.0.10240. |
| [WsSetOutputToBuffer](/windows/win32/api/webservices/nf-webservices-wssetoutputtobuffer) | Introduced into webservices.dll in 10.0.10240. |
| [WsSetReaderPosition](/windows/win32/api/webservices/nf-webservices-wssetreaderposition) | Introduced into webservices.dll in 10.0.10240. |
| [WsSetWriterPosition](/windows/win32/api/webservices/nf-webservices-wssetwriterposition) | Introduced into webservices.dll in 10.0.10240. |
| [WsShutdownSessionChannel](/windows/win32/api/webservices/nf-webservices-wsshutdownsessionchannel) | Introduced into webservices.dll in 10.0.10240. |
| [WsSkipNode](/windows/win32/api/webservices/nf-webservices-wsskipnode) | Introduced into webservices.dll in 10.0.10240. |
| [WsStartReaderCanonicalization](/windows/win32/api/webservices/nf-webservices-wsstartreadercanonicalization) | Introduced into webservices.dll in 10.0.10240. |
| [WsStartWriterCanonicalization](/windows/win32/api/webservices/nf-webservices-wsstartwritercanonicalization) | Introduced into webservices.dll in 10.0.10240. |
| [WsTrimXmlWhitespace](/windows/win32/api/webservices/nf-webservices-wstrimxmlwhitespace) | Introduced into webservices.dll in 10.0.10240. |
| [WsVerifyXmlNCName](/windows/win32/api/webservices/nf-webservices-wsverifyxmlncname) | Introduced into webservices.dll in 10.0.10240. |
| [WsWriteArray](/windows/win32/api/webservices/nf-webservices-wswritearray) | Introduced into webservices.dll in 10.0.10240. |
| [WsWriteAttribute](/windows/win32/api/webservices/nf-webservices-wswriteattribute) | Introduced into webservices.dll in 10.0.10240. |
| [WsWriteBody](/windows/win32/api/webservices/nf-webservices-wswritebody) | Introduced into webservices.dll in 10.0.10240. |
| [WsWriteBytes](/windows/win32/api/webservices/nf-webservices-wswritebytes) | Introduced into webservices.dll in 10.0.10240. |
| [WsWriteChars](/windows/win32/api/webservices/nf-webservices-wswritechars) | Introduced into webservices.dll in 10.0.10240. |
| [WsWriteCharsUtf8](/windows/win32/api/webservices/nf-webservices-wswritecharsutf8) | Introduced into webservices.dll in 10.0.10240. |
| [WsWriteElement](/windows/win32/api/webservices/nf-webservices-wswriteelement) | Introduced into webservices.dll in 10.0.10240. |
| [WsWriteEndAttribute](/windows/win32/api/webservices/nf-webservices-wswriteendattribute) | Introduced into webservices.dll in 10.0.10240. |
| [WsWriteEndCData](/windows/win32/api/webservices/nf-webservices-wswriteendcdata) | Introduced into webservices.dll in 10.0.10240. |
| [WsWriteEndElement](/windows/win32/api/webservices/nf-webservices-wswriteendelement) | Introduced into webservices.dll in 10.0.10240. |
| [WsWriteEndStartElement](/windows/win32/api/webservices/nf-webservices-wswriteendstartelement) | Introduced into webservices.dll in 10.0.10240. |
| [WsWriteEnvelopeEnd](/windows/win32/api/webservices/nf-webservices-wswriteenvelopeend) | Introduced into webservices.dll in 10.0.10240. |
| [WsWriteEnvelopeStart](/windows/win32/api/webservices/nf-webservices-wswriteenvelopestart) | Introduced into webservices.dll in 10.0.10240. |
| [WsWriteMessageEnd](/windows/win32/api/webservices/nf-webservices-wswritemessageend) | Introduced into webservices.dll in 10.0.10240. |
| [WsWriteMessageStart](/windows/win32/api/webservices/nf-webservices-wswritemessagestart) | Introduced into webservices.dll in 10.0.10240. |
| [WsWriteNode](/windows/win32/api/webservices/nf-webservices-wswritenode) | Introduced into webservices.dll in 10.0.10240. |
| [WsWriteQualifiedName](/windows/win32/api/webservices/nf-webservices-wswritequalifiedname) | Introduced into webservices.dll in 10.0.10240. |
| [WsWriteStartAttribute](/windows/win32/api/webservices/nf-webservices-wswritestartattribute) | Introduced into webservices.dll in 10.0.10240. |
| [WsWriteStartCData](/windows/win32/api/webservices/nf-webservices-wswritestartcdata) | Introduced into webservices.dll in 10.0.10240. |
| [WsWriteStartElement](/windows/win32/api/webservices/nf-webservices-wswritestartelement) | Introduced into webservices.dll in 10.0.10240. |
| [WsWriteText](/windows/win32/api/webservices/nf-webservices-wswritetext) | Introduced into webservices.dll in 10.0.10240. |
| [WsWriteType](/windows/win32/api/webservices/nf-webservices-wswritetype) | Introduced into webservices.dll in 10.0.10240. |
| [WsWriteValue](/windows/win32/api/webservices/nf-webservices-wswritevalue) | Introduced into webservices.dll in 10.0.10240. |
| [WsWriteXmlBuffer](/windows/win32/api/webservices/nf-webservices-wswritexmlbuffer) | Introduced into webservices.dll in 10.0.10240. |
| [WsWriteXmlBufferToBytes](/windows/win32/api/webservices/nf-webservices-wswritexmlbuffertobytes) | Introduced into webservices.dll in 10.0.10240. |
| [WsWriteXmlnsAttribute](/windows/win32/api/webservices/nf-webservices-wswritexmlnsattribute) | Introduced into webservices.dll in 10.0.10240. |
| [WsXmlStringEquals](/windows/win32/api/webservices/nf-webservices-wsxmlstringequals) | Introduced into webservices.dll in 10.0.10240. |


## APIs from windows.data.pdf.dll

| API | Requirements |
| -----| --------------|
| [PdfCreateRenderer](/windows/win32/api/windows.data.pdf.interop/nf-windows-data-pdf-interop-pdfcreaterenderer) | Introduced into windows.data.pdf.dll in 10.0.10240. |


## APIs from windows.networking.dll

| API | Requirements |
| -----| --------------|
| [SetSocketMediaStreamingMode](/windows/win32/api/socketapi/nf-socketapi-setsocketmediastreamingmode) | Introduced into windows.networking.dll in 10.0.10240. |


## APIs from windowscodecs.dll

| API | Requirements |
| -----| --------------|
| [WICConvertBitmapSource](/windows/win32/api/wincodec/nf-wincodec-wicconvertbitmapsource) | Introduced into windowscodecs.dll in 10.0.10240. |
| [WICCreateBitmapFromSection](/windows/win32/api/wincodec/nf-wincodec-wiccreatebitmapfromsection) | Introduced into windowscodecs.dll in 10.0.10240. |
| [WICCreateBitmapFromSectionEx](/windows/win32/api/wincodec/nf-wincodec-wiccreatebitmapfromsectionex) | Introduced into windowscodecs.dll in 10.0.10240. |
| [WICGetMetadataContentSize](/windows/win32/api/wincodecsdk/nf-wincodecsdk-wicgetmetadatacontentsize) | Introduced into windowscodecs.dll in 10.0.10240. |
| [WICMapGuidToShortName](/windows/win32/api/wincodec/nf-wincodec-wicmapguidtoshortname) | Introduced into windowscodecs.dll in 10.0.10240. |
| [WICMapSchemaToName](/windows/win32/api/wincodec/nf-wincodec-wicmapschematoname) | Introduced into windowscodecs.dll in 10.0.10240. |
| [WICMapShortNameToGuid](/windows/win32/api/wincodec/nf-wincodec-wicmapshortnametoguid) | Introduced into windowscodecs.dll in 10.0.10240. |
| [WICMatchMetadataContent](/windows/win32/api/wincodecsdk/nf-wincodecsdk-wicmatchmetadatacontent) | Introduced into windowscodecs.dll in 10.0.10240. |
| [WICSerializeMetadataContent](/windows/win32/api/wincodecsdk/nf-wincodecsdk-wicserializemetadatacontent) | Introduced into windowscodecs.dll in 10.0.10240. |


## APIs from ws2_32.dll

| API | Requirements |
| -----| --------------|
| [__WSAFDIsSet](/windows/win32/api/winsock/nf-winsock-__wsafdisset) | Introduced into ws2_32.dll in 10.0.10240. |
| [accept](/windows/win32/api/winsock2/nf-winsock2-accept) | Introduced into ws2_32.dll in 10.0.10240. |
| [bind](/windows/win32/api/winsock/nf-winsock-bind) | Introduced into ws2_32.dll in 10.0.10240. |
| [closesocket](/windows/win32/api/winsock/nf-winsock-closesocket) | Introduced into ws2_32.dll in 10.0.10240. |
| [connect](/windows/win32/api/winsock2/nf-winsock2-connect) | Introduced into ws2_32.dll in 10.0.10240. |
| [freeaddrinfo](/windows/win32/api/ws2tcpip/nf-ws2tcpip-freeaddrinfo) | Introduced into ws2_32.dll in 10.0.10240. |
| [FreeAddrInfoExW](/windows/win32/api/ws2tcpip/nf-ws2tcpip-freeaddrinfoex) | Introduced into ws2_32.dll in 10.0.10240. |
| [FreeAddrInfoW](/windows/win32/api/ws2tcpip/nf-ws2tcpip-freeaddrinfow) | Introduced into ws2_32.dll in 10.0.10240. |
| [getaddrinfo](/windows/win32/api/ws2tcpip/nf-ws2tcpip-getaddrinfo) | Introduced into ws2_32.dll in 10.0.10240. |
| [GetAddrInfoExCancel](/windows/win32/api/ws2tcpip/nf-ws2tcpip-getaddrinfoexcancel) | Introduced into ws2_32.dll in 10.0.10240. |
| [GetAddrInfoExOverlappedResult](/windows/win32/api/ws2tcpip/nf-ws2tcpip-getaddrinfoexoverlappedresult) | Introduced into ws2_32.dll in 10.0.10240. |
| [GetAddrInfoExW](/windows/win32/api/ws2tcpip/nf-ws2tcpip-getaddrinfoexa) | Introduced into ws2_32.dll in 10.0.10240. |
| [GetAddrInfoW](/windows/win32/api/ws2tcpip/nf-ws2tcpip-getaddrinfow) | Introduced into ws2_32.dll in 10.0.10240. |
| [gethostbyaddr](/windows/win32/api/wsipv6ok/nf-wsipv6ok-gethostbyaddr) | Introduced into ws2_32.dll in 10.0.10240. |
| [gethostbyname](/windows/win32/api/wsipv6ok/nf-wsipv6ok-gethostbyname) | Introduced into ws2_32.dll in 10.0.10240. |
| [gethostname](/windows/win32/api/winsock/nf-winsock-gethostname) | Introduced into ws2_32.dll in 10.0.10240. |
| [GetHostNameW](/windows/win32/api/winsock2/nf-winsock2-gethostnamew) | Introduced into ws2_32.dll in 10.0.10240. |
| [getnameinfo](/windows/win32/api/ws2tcpip/nf-ws2tcpip-getnameinfo) | Introduced into ws2_32.dll in 10.0.10240. |
| [GetNameInfoW](/windows/win32/api/ws2tcpip/nf-ws2tcpip-getnameinfow) | Introduced into ws2_32.dll in 10.0.10240. |
| [getpeername](/windows/win32/api/winsock/nf-winsock-getpeername) | Introduced into ws2_32.dll in 10.0.10240. |
| [getprotobyname](/windows/win32/api/winsock/nf-winsock-getprotobyname) | Introduced into ws2_32.dll in 10.0.10240. |
| [getprotobynumber](/windows/win32/api/winsock/nf-winsock-getprotobynumber) | Introduced into ws2_32.dll in 10.0.10240. |
| [getservbyname](/windows/win32/api/winsock/nf-winsock-getservbyname) | Introduced into ws2_32.dll in 10.0.10240. |
| [getservbyport](/windows/win32/api/winsock/nf-winsock-getservbyport) | Introduced into ws2_32.dll in 10.0.10240. |
| [getsockname](/windows/win32/api/winsock/nf-winsock-getsockname) | Introduced into ws2_32.dll in 10.0.10240. |
| [getsockopt](/windows/win32/api/winsock/nf-winsock-getsockopt) | Introduced into ws2_32.dll in 10.0.10240. |
| [htonl](/windows/win32/api/winsock/nf-winsock-htonl) | Introduced into ws2_32.dll in 10.0.10240. |
| [htons](/windows/win32/api/winsock/nf-winsock-htons) | Introduced into ws2_32.dll in 10.0.10240. |
| [inet_addr](/windows/win32/api/winsock2/nf-winsock2-inet_addr) | Introduced into ws2_32.dll in 10.0.10240. |
| [inet_ntoa](/windows/win32/api/winsock2/nf-winsock2-inet_ntoa) | Introduced into ws2_32.dll in 10.0.10240. |
| inet_ntop | Introduced into ws2_32.dll in 10.0.10240. |
| [inet_pton](/windows/win32/api/ws2tcpip/nf-ws2tcpip-inetptonw) | Introduced into ws2_32.dll in 10.0.10240. |
| [InetNtopW](/windows/win32/api/ws2tcpip/nf-ws2tcpip-inetntopw) | Introduced into ws2_32.dll in 10.0.10240. |
| [InetPtonW](/windows/win32/api/ws2tcpip/nf-ws2tcpip-inetptonw) | Introduced into ws2_32.dll in 10.0.10240. |
| [ioctlsocket](/windows/win32/api/winsock/nf-winsock-ioctlsocket) | Introduced into ws2_32.dll in 10.0.10240. |
| [listen](/windows/win32/api/winsock2/nf-winsock2-listen) | Introduced into ws2_32.dll in 10.0.10240. |
| [ntohl](/windows/win32/api/winsock/nf-winsock-ntohl) | Introduced into ws2_32.dll in 10.0.10240. |
| [ntohs](/windows/win32/api/winsock/nf-winsock-ntohs) | Introduced into ws2_32.dll in 10.0.10240. |
| [recv](/windows/win32/api/winsock/nf-winsock-recv) | Introduced into ws2_32.dll in 10.0.10240. |
| [recvfrom](/windows/win32/api/winsock/nf-winsock-recvfrom) | Introduced into ws2_32.dll in 10.0.10240. |
| [select](/windows/win32/api/winsock2/nf-winsock2-select) | Introduced into ws2_32.dll in 10.0.10240. |
| [send](/windows/win32/api/winsock2/nf-winsock2-send) | Introduced into ws2_32.dll in 10.0.10240. |
| [sendto](/windows/win32/api/winsock/nf-winsock-sendto) | Introduced into ws2_32.dll in 10.0.10240. |
| [SetAddrInfoExW](/windows/win32/api/ws2tcpip/nf-ws2tcpip-setaddrinfoexa) | Introduced into ws2_32.dll in 10.0.10240. |
| [setsockopt](/windows/win32/api/winsock/nf-winsock-setsockopt) | Introduced into ws2_32.dll in 10.0.10240. |
| [shutdown](/windows/win32/api/winsock/nf-winsock-shutdown) | Introduced into ws2_32.dll in 10.0.10240. |
| [socket](/windows/win32/api/winsock2/nf-winsock2-socket) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSAAccept](/windows/win32/api/winsock2/nf-winsock2-wsaaccept) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSAAddressToStringA](/windows/win32/api/winsock2/nf-winsock2-wsaaddresstostringa) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSAAddressToStringW](/windows/win32/api/winsock2/nf-winsock2-wsaaddresstostringa) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSACleanup](/windows/win32/api/winsock/nf-winsock-wsacleanup) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSACloseEvent](/windows/win32/api/winsock2/nf-winsock2-wsacloseevent) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSAConnect](/windows/win32/api/winsock2/nf-winsock2-wsaconnect) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSAConnectByList](/windows/win32/api/winsock2/nf-winsock2-wsaconnectbylist) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSAConnectByNameA](/windows/win32/api/winsock2/nf-winsock2-wsaconnectbynamea) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSAConnectByNameW](/windows/win32/api/winsock2/nf-winsock2-wsaconnectbynamea) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSACreateEvent](/windows/win32/api/winsock2/nf-winsock2-wsacreateevent) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSADuplicateSocketA](/windows/win32/api/winsock2/nf-winsock2-wsaduplicatesocketa) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSADuplicateSocketW](/windows/win32/api/winsock2/nf-winsock2-wsaduplicatesocketa) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSAEnumNameSpaceProvidersA](/windows/win32/api/winsock2/nf-winsock2-wsaenumnamespaceprovidersa) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSAEnumNameSpaceProvidersExA](/windows/win32/api/winsock2/nf-winsock2-wsaenumnamespaceprovidersexa) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSAEnumNameSpaceProvidersExW](/windows/win32/api/winsock2/nf-winsock2-wsaenumnamespaceprovidersexa) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSAEnumNameSpaceProvidersW](/windows/win32/api/winsock2/nf-winsock2-wsaenumnamespaceprovidersa) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSAEnumNetworkEvents](/windows/win32/api/winsock2/nf-winsock2-wsaenumnetworkevents) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSAEnumProtocolsA](/windows/win32/api/winsock2/nf-winsock2-wsaenumprotocolsa) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSAEnumProtocolsW](/windows/win32/api/winsock2/nf-winsock2-wsaenumprotocolsa) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSAEventSelect](/windows/win32/api/winsock2/nf-winsock2-wsaeventselect) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSAGetLastError](/windows/win32/api/winsock/nf-winsock-wsagetlasterror) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSAGetOverlappedResult](/windows/win32/api/winsock2/nf-winsock2-wsagetoverlappedresult) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSAGetServiceClassInfoW](/windows/win32/api/winsock2/nf-winsock2-wsagetserviceclassinfoa) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSAGetServiceClassNameByClassIdW](/windows/win32/api/winsock2/nf-winsock2-wsagetserviceclassnamebyclassida) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSAHtonl](/windows/win32/api/winsock2/nf-winsock2-wsahtonl) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSAHtons](/windows/win32/api/winsock2/nf-winsock2-wsahtons) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSAIoctl](/windows/win32/api/winsock2/nf-winsock2-wsaioctl) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSAJoinLeaf](/windows/win32/api/winsock2/nf-winsock2-wsajoinleaf) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSALookupServiceBeginA](/windows/win32/api/winsock2/nf-winsock2-wsalookupservicebegina) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSALookupServiceBeginW](/windows/win32/api/winsock2/nf-winsock2-wsalookupservicebegina) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSALookupServiceEnd](/windows/win32/api/winsock2/nf-winsock2-wsalookupserviceend) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSALookupServiceNextA](/windows/win32/api/winsock2/nf-winsock2-wsalookupservicenexta) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSALookupServiceNextW](/windows/win32/api/winsock2/nf-winsock2-wsalookupservicenexta) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSANSPIoctl](/windows/win32/api/winsock2/nf-winsock2-wsanspioctl) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSANtohl](/windows/win32/api/winsock2/nf-winsock2-wsantohl) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSANtohs](/windows/win32/api/winsock2/nf-winsock2-wsantohs) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSAPoll](/windows/win32/api/winsock2/nf-winsock2-wsapoll) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSAProviderConfigChange](/windows/win32/api/winsock2/nf-winsock2-wsaproviderconfigchange) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSARecv](/windows/win32/api/winsock2/nf-winsock2-wsarecv) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSARecvFrom](/windows/win32/api/winsock2/nf-winsock2-wsarecvfrom) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSAResetEvent](/windows/win32/api/winsock2/nf-winsock2-wsaresetevent) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSASend](/windows/win32/api/winsock2/nf-winsock2-wsasend) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSASendMsg](/windows/win32/api/winsock2/nf-winsock2-wsasendmsg) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSASendTo](/windows/win32/api/winsock2/nf-winsock2-wsasendto) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSASetEvent](/windows/win32/api/winsock2/nf-winsock2-wsasetevent) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSASetLastError](/windows/win32/api/winsock/nf-winsock-wsasetlasterror) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSASetServiceA](/windows/win32/api/winsock2/nf-winsock2-wsasetservicea) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSASetServiceW](/windows/win32/api/winsock2/nf-winsock2-wsasetservicea) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSASocketA](/windows/win32/api/winsock2/nf-winsock2-wsasocketa) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSASocketW](/windows/win32/api/winsock2/nf-winsock2-wsasocketa) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSAStartup](/windows/win32/api/winsock/nf-winsock-wsastartup) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSAStringToAddressA](/windows/win32/api/winsock2/nf-winsock2-wsastringtoaddressa) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSAStringToAddressW](/windows/win32/api/winsock2/nf-winsock2-wsastringtoaddressa) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSAWaitForMultipleEvents](/windows/win32/api/winsock2/nf-winsock2-wsawaitformultipleevents) | Introduced into ws2_32.dll in 10.0.10240. |
| [FreeAddrInfoEx](/windows/win32/api/ws2tcpip/nf-ws2tcpip-freeaddrinfoex) | Introduced into ws2_32.dll in 10.0.16299. Removed in 10.0.17134. |


## APIs from xaudio2_9.dll

| API | Requirements |
| -----| --------------|
| CreateAudioReverb | Introduced into xaudio2_9.dll in 10.0.10240. |
| CreateAudioVolumeMeter | Introduced into xaudio2_9.dll in 10.0.10240. |
| [CreateFX](/windows/win32/api/xapofx/nf-xapofx-createfx) | Introduced into xaudio2_9.dll in 10.0.10240. |
| [X3DAudioCalculate](/windows/win32/api/x3daudio/nf-x3daudio-x3daudiocalculate) | Introduced into xaudio2_9.dll in 10.0.10240. |
| [X3DAudioInitialize](/windows/win32/api/x3daudio/nf-x3daudio-x3daudioinitialize) | Introduced into xaudio2_9.dll in 10.0.10240. |
| [XAudio2Create](/windows/win32/api/xaudio2/nf-xaudio2-xaudio2create) | Introduced into xaudio2_9.dll in 10.0.10240. |


## APIs from xinputuap.dll

| API | Requirements |
| -----| --------------|
| [XInputEnable](/windows/win32/api/xinput/nf-xinput-xinputenable) | Introduced into xinputuap.dll in 10.0.10240. Moved into ext-ms-win-gaming-xinput-l1-1-0.dll in 10.0.16299. Moved into xinputuap.dll in 10.0.17134. |
| [XInputGetAudioDeviceIds](/windows/win32/api/xinput/nf-xinput-xinputgetaudiodeviceids) | Introduced into xinputuap.dll in 10.0.10240. Moved into ext-ms-win-gaming-xinput-l1-1-0.dll in 10.0.16299. Moved into xinputuap.dll in 10.0.17134. |
| [XInputGetBatteryInformation](/windows/win32/api/xinput/nf-xinput-xinputgetbatteryinformation) | Introduced into xinputuap.dll in 10.0.10240. Moved into ext-ms-win-gaming-xinput-l1-1-0.dll in 10.0.16299. Moved into xinputuap.dll in 10.0.17134. |
| [XInputGetCapabilities](/windows/win32/api/xinput/nf-xinput-xinputgetcapabilities) | Introduced into xinputuap.dll in 10.0.10240. Moved into ext-ms-win-gaming-xinput-l1-1-0.dll in 10.0.16299. Moved into xinputuap.dll in 10.0.17134. |
| [XInputGetKeystroke](/windows/win32/api/xinput/nf-xinput-xinputgetkeystroke) | Introduced into xinputuap.dll in 10.0.10240. Moved into ext-ms-win-gaming-xinput-l1-1-0.dll in 10.0.16299. Moved into xinputuap.dll in 10.0.17134. |
| [XInputGetState](/windows/win32/api/xinput/nf-xinput-xinputgetstate) | Introduced into xinputuap.dll in 10.0.10240. Moved into ext-ms-win-gaming-xinput-l1-1-0.dll in 10.0.16299. Moved into xinputuap.dll in 10.0.17134. |
| [XInputSetState](/windows/win32/api/xinput/nf-xinput-xinputsetstate) | Introduced into xinputuap.dll in 10.0.10240. Moved into ext-ms-win-gaming-xinput-l1-1-0.dll in 10.0.16299. Moved into xinputuap.dll in 10.0.17134. |


## APIs from xmllite.dll

| API | Requirements |
| -----| --------------|
| [CreateXmlReader](/previous-versions/windows/desktop/ms752822(v=vs.85)) | Introduced into xmllite.dll in 10.0.10240. |
| [CreateXmlReaderInputWithEncodingCodePage](/previous-versions/windows/desktop/ms752859(v=vs.85)) | Introduced into xmllite.dll in 10.0.10240. |
| [CreateXmlReaderInputWithEncodingName](/previous-versions/windows/desktop/ms752899(v=vs.85)) | Introduced into xmllite.dll in 10.0.10240. |
| [CreateXmlWriter](/previous-versions/windows/desktop/ms752911(v=vs.85)) | Introduced into xmllite.dll in 10.0.10240. |
| [CreateXmlWriterOutputWithEncodingCodePage](/previous-versions/windows/desktop/ms753133(v=vs.85)) | Introduced into xmllite.dll in 10.0.10240. |
| [CreateXmlWriterOutputWithEncodingName](/previous-versions/windows/desktop/ms752894(v=vs.85)) | Introduced into xmllite.dll in 10.0.10240. |


## APIs from api-ms-win-core-file-l1-2-2.dll

| API | Requirements |
| -----| --------------|
| [CompareFileTime](/windows/win32/api/fileapi/nf-fileapi-comparefiletime) | Introduced into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. |
| [GetTempFileNameA](/windows/win32/api/fileapi/nf-fileapi-gettempfilenamea) | Introduced into api-ms-win-core-file-l1-2-2.dll in 10.0.16299. |
| [GetTempPathA](/windows/win32/api/fileapi/nf-fileapi-gettemppatha) | Introduced into api-ms-win-core-file-l1-2-2.dll in 10.0.16299. |
| [GetVolumeInformationA](/windows/win32/api/fileapi/nf-fileapi-getvolumeinformationa) | Introduced into api-ms-win-core-file-l1-2-2.dll in 10.0.16299. |


## APIs from api-ms-win-core-libraryloader-l1-2-1.dll

| API | Requirements |
| -----| --------------|
| [FreeLibraryAndExitThread](/windows/win32/api/libloaderapi/nf-libloaderapi-freelibraryandexitthread) | Introduced into api-ms-win-core-libraryloader-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-libraryloader-l1-2-0.dll in 10.0.14393. |


## APIs from Bcrypt.dll

| API | Requirements |
| -----| --------------|
| [BCryptCreateMultiHash](/windows/win32/api/bcrypt/nf-bcrypt-bcryptcreatemultihash) | Introduced into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptProcessMultiOperations](/windows/win32/api/bcrypt/nf-bcrypt-bcryptprocessmultioperations) | Introduced into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |


## APIs from api-ms-win-core-featurestaging-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [GetFeatureEnabledState](/windows/win32/api/featurestagingapi/nf-featurestagingapi-getfeatureenabledstate) | Introduced into api-ms-win-core-featurestaging-l1-1-0.dll in 10.0.14393. |
| [RecordFeatureError](/windows/win32/api/featurestagingapi/nf-featurestagingapi-recordfeatureerror) | Introduced into api-ms-win-core-featurestaging-l1-1-0.dll in 10.0.14393. |
| [RecordFeatureUsage](/windows/win32/api/featurestagingapi/nf-featurestagingapi-recordfeatureusage) | Introduced into api-ms-win-core-featurestaging-l1-1-0.dll in 10.0.14393. |
| [SubscribeFeatureStateChangeNotification](/windows/win32/api/featurestagingapi/nf-featurestagingapi-subscribefeaturestatechangenotification) | Introduced into api-ms-win-core-featurestaging-l1-1-0.dll in 10.0.14393. |
| [UnsubscribeFeatureStateChangeNotification](/windows/win32/api/featurestagingapi/nf-featurestagingapi-unsubscribefeaturestatechangenotification) | Introduced into api-ms-win-core-featurestaging-l1-1-0.dll in 10.0.14393. |


## APIs from api-ms-win-core-heap-l2-1-0.dll

| API | Requirements |
| -----| --------------|
| [GlobalAlloc](/windows/win32/api/winbase/nf-winbase-globalalloc) | Introduced into api-ms-win-core-heap-l2-1-0.dll in 10.0.14393. |
| [GlobalFree](/windows/win32/api/winbase/nf-winbase-globalfree) | Introduced into api-ms-win-core-heap-l2-1-0.dll in 10.0.14393. |
| [LocalAlloc](/windows/win32/api/winbase/nf-winbase-localalloc) | Introduced into api-ms-win-core-heap-l2-1-0.dll in 10.0.14393. |
| [LocalFree](/windows/win32/api/winbase/nf-winbase-localfree) | Introduced into api-ms-win-core-heap-l2-1-0.dll in 10.0.14393. |
| [LocalReAlloc](/windows/win32/api/winbase/nf-winbase-localrealloc) | Introduced into api-ms-win-core-heap-l2-1-0.dll in 10.0.14393. |


## APIs from api-ms-win-core-heap-obsolete-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [GlobalReAlloc](/windows/win32/api/winbase/nf-winbase-globalrealloc) | Introduced into api-ms-win-core-heap-obsolete-l1-1-0.dll in 10.0.14393. |
| [GlobalLock](/windows/win32/api/winbase/nf-winbase-globallock) | Introduced into api-ms-win-core-heap-obsolete-l1-1-0.dll in 10.0.16299. |
| [GlobalSize](/windows/win32/api/winbase/nf-winbase-globalsize) | Introduced into api-ms-win-core-heap-obsolete-l1-1-0.dll in 10.0.16299. |
| [GlobalUnlock](/windows/win32/api/winbase/nf-winbase-globalunlock) | Introduced into api-ms-win-core-heap-obsolete-l1-1-0.dll in 10.0.16299. |


## APIs from api-ms-win-core-psapi-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [K32GetModuleInformation](/windows/win32/api/psapi/nf-psapi-getmoduleinformation) | Introduced into api-ms-win-core-psapi-l1-1-0.dll in 10.0.14393. |
| [K32GetProcessMemoryInfo](/windows/win32/api/psapi/nf-psapi-getprocessmemoryinfo) | Introduced into api-ms-win-core-psapi-l1-1-0.dll in 10.0.14393. |
| [K32EnumProcesses](/windows/win32/api/psapi/nf-psapi-enumprocesses) | Introduced into api-ms-win-core-psapi-l1-1-0.dll in 10.0.16299. |
| [K32GetModuleBaseNameW](/windows/win32/api/psapi/nf-psapi-getmodulebasenamea) | Introduced into api-ms-win-core-psapi-l1-1-0.dll in 10.0.16299. |
| [K32GetModuleFileNameExW](/windows/win32/api/psapi/nf-psapi-getmodulefilenameexa) | Introduced into api-ms-win-core-psapi-l1-1-0.dll in 10.0.16299. |


## APIs from api-ms-win-core-slapi-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [SLQueryLicenseValueFromApp](/windows/win32/api/slpublic/nf-slpublic-slquerylicensevaluefromapp) | Introduced into api-ms-win-core-slapi-l1-1-0.dll in 10.0.14393. |
| SLQueryLicenseValueFromApp2 | Introduced into api-ms-win-core-slapi-l1-1-0.dll in 10.0.14393. |


## APIs from api-ms-win-gaming-tcui-l1-1-2.dll

| API | Requirements |
| -----| --------------|
| CheckGamingPrivilegeSilently | Introduced into api-ms-win-gaming-tcui-l1-1-2.dll in 10.0.14393. Moved into api-ms-win-gaming-tcui-l1-1-1.dll in 10.0.16299. |
| CheckGamingPrivilegeSilentlyForUser | Introduced into api-ms-win-gaming-tcui-l1-1-2.dll in 10.0.14393. |
| [CheckGamingPrivilegeWithUI](/windows/win32/api/gamingtcui/nf-gamingtcui-checkgamingprivilegewithui) | Introduced into api-ms-win-gaming-tcui-l1-1-2.dll in 10.0.14393. Moved into api-ms-win-gaming-tcui-l1-1-1.dll in 10.0.16299. |
| CheckGamingPrivilegeWithUIForUser | Introduced into api-ms-win-gaming-tcui-l1-1-2.dll in 10.0.14393. |
| ShowChangeFriendRelationshipUIForUser | Introduced into api-ms-win-gaming-tcui-l1-1-2.dll in 10.0.14393. |
| ShowGameInviteUIForUser | Introduced into api-ms-win-gaming-tcui-l1-1-2.dll in 10.0.14393. |
| ShowPlayerPickerUIForUser | Introduced into api-ms-win-gaming-tcui-l1-1-2.dll in 10.0.14393. |
| ShowProfileCardUIForUser | Introduced into api-ms-win-gaming-tcui-l1-1-2.dll in 10.0.14393. |
| ShowTitleAchievementsUIForUser | Introduced into api-ms-win-gaming-tcui-l1-1-2.dll in 10.0.14393. |


## APIs from api-ms-win-security-base-l1-2-1.dll

| API | Requirements |
| -----| --------------|
| [CveEventWrite](/windows/win32/api/securitybaseapi/nf-securitybaseapi-cveeventwrite) | Introduced into api-ms-win-security-base-l1-2-1.dll in 10.0.14393. |


## APIs from inkobjcore.dll

| API | Requirements |
| -----| --------------|
| [AddStroke](/windows/win32/api/recapis/nf-recapis-addstroke) | Introduced into inkobjcore.dll in 10.0.14393. |
| [AddWordsToWordList](/windows/win32/api/recapis/nf-recapis-addwordstowordlist) | Introduced into inkobjcore.dll in 10.0.14393. |
| [AdviseInkChange](/windows/win32/api/recapis/nf-recapis-adviseinkchange) | Introduced into inkobjcore.dll in 10.0.14393. |
| [CreateContext](/windows/win32/api/recapis/nf-recapis-createcontext) | Introduced into inkobjcore.dll in 10.0.14393. |
| [CreateRecognizer](/windows/win32/api/recapis/nf-recapis-createrecognizer) | Introduced into inkobjcore.dll in 10.0.14393. |
| [DestroyContext](/windows/win32/api/recapis/nf-recapis-destroycontext) | Introduced into inkobjcore.dll in 10.0.14393. |
| [DestroyRecognizer](/windows/win32/api/recapis/nf-recapis-destroyrecognizer) | Introduced into inkobjcore.dll in 10.0.14393. |
| [DestroyWordList](/windows/win32/api/recapis/nf-recapis-destroywordlist) | Introduced into inkobjcore.dll in 10.0.14393. |
| [EndInkInput](/windows/win32/api/recapis/nf-recapis-endinkinput) | Introduced into inkobjcore.dll in 10.0.14393. |
| [GetAllRecognizers](/windows/win32/api/recapis/nf-recapis-getallrecognizers) | Introduced into inkobjcore.dll in 10.0.14393. |
| [GetBestResultString](/windows/win32/api/recapis/nf-recapis-getbestresultstring) | Introduced into inkobjcore.dll in 10.0.14393. |
| [GetLatticePtr](/windows/win32/api/recapis/nf-recapis-getlatticeptr) | Introduced into inkobjcore.dll in 10.0.14393. |
| [GetLeftSeparator](/windows/win32/api/recapis/nf-recapis-getleftseparator) | Introduced into inkobjcore.dll in 10.0.14393. |
| [GetRecoAttributes](/windows/win32/api/recapis/nf-recapis-getrecoattributes) | Introduced into inkobjcore.dll in 10.0.14393. |
| [GetResultPropertyList](/windows/win32/api/recapis/nf-recapis-getresultpropertylist) | Introduced into inkobjcore.dll in 10.0.14393. |
| [GetRightSeparator](/windows/win32/api/recapis/nf-recapis-getrightseparator) | Introduced into inkobjcore.dll in 10.0.14393. |
| [GetUnicodeRanges](/windows/win32/api/recapis/nf-recapis-getunicoderanges) | Introduced into inkobjcore.dll in 10.0.14393. |
| [IsStringSupported](/windows/win32/api/recapis/nf-recapis-isstringsupported) | Introduced into inkobjcore.dll in 10.0.14393. |
| [LoadCachedAttributes](/windows/win32/api/recapis/nf-recapis-loadcachedattributes) | Introduced into inkobjcore.dll in 10.0.14393. |
| [MakeWordList](/windows/win32/api/recapis/nf-recapis-makewordlist) | Introduced into inkobjcore.dll in 10.0.14393. |
| [Process](/windows/win32/etw/process) | Introduced into inkobjcore.dll in 10.0.14393. |
| [SetEnabledUnicodeRanges](/windows/win32/api/recapis/nf-recapis-setenabledunicoderanges) | Introduced into inkobjcore.dll in 10.0.14393. |
| [SetFactoid](/windows/win32/api/recapis/nf-recapis-setfactoid) | Introduced into inkobjcore.dll in 10.0.14393. |
| [SetFlags](/previous-versions//dd378283(v=vs.85)) | Introduced into inkobjcore.dll in 10.0.14393. |
| [SetGuide](/windows/win32/api/recapis/nf-recapis-setguide) | Introduced into inkobjcore.dll in 10.0.14393. |
| [SetTextContext](/windows/win32/api/recapis/nf-recapis-settextcontext) | Introduced into inkobjcore.dll in 10.0.14393. |
| [SetWordList](/windows/win32/api/recapis/nf-recapis-setwordlist) | Introduced into inkobjcore.dll in 10.0.14393. |


## APIs from iphlpapi.dll

| API | Requirements |
| -----| --------------|
| [FreeMibTable](/windows/win32/api/netioapi/nf-netioapi-freemibtable) | Introduced into iphlpapi.dll in 10.0.14393. |
| [GetAdaptersAddresses](/windows/win32/api/iphlpapi/nf-iphlpapi-getadaptersaddresses) | Introduced into iphlpapi.dll in 10.0.14393. |
| [GetBestRoute2](/windows/win32/api/netioapi/nf-netioapi-getbestroute2) | Introduced into iphlpapi.dll in 10.0.14393. |
| [GetUnicastIpAddressTable](/windows/win32/api/netioapi/nf-netioapi-getunicastipaddresstable) | Introduced into iphlpapi.dll in 10.0.14393. |
| [CancelMibChangeNotify2](/windows/win32/api/netioapi/nf-netioapi-cancelmibchangenotify2) | Introduced into iphlpapi.dll in 10.0.16299. |
| [GetBestInterfaceEx](/windows/win32/api/iphlpapi/nf-iphlpapi-getbestinterfaceex) | Introduced into iphlpapi.dll in 10.0.16299. |
| [GetExtendedTcpTable](/windows/win32/api/iphlpapi/nf-iphlpapi-getextendedtcptable) | Introduced into iphlpapi.dll in 10.0.16299. |
| [GetExtendedUdpTable](/windows/win32/api/iphlpapi/nf-iphlpapi-getextendedudptable) | Introduced into iphlpapi.dll in 10.0.16299. |
| [GetIcmpStatistics](/windows/win32/api/iphlpapi/nf-iphlpapi-geticmpstatistics) | Introduced into iphlpapi.dll in 10.0.16299. |
| [GetIcmpStatisticsEx](/windows/win32/api/iphlpapi/nf-iphlpapi-geticmpstatisticsex) | Introduced into iphlpapi.dll in 10.0.16299. |
| [GetIfEntry2](/windows/win32/api/netioapi/nf-netioapi-getifentry2) | Introduced into iphlpapi.dll in 10.0.16299. |
| [GetIpStatisticsEx](/windows/win32/api/iphlpapi/nf-iphlpapi-getipstatisticsex) | Introduced into iphlpapi.dll in 10.0.16299. |
| [GetNetworkParams](/windows/win32/api/iphlpapi/nf-iphlpapi-getnetworkparams) | Introduced into iphlpapi.dll in 10.0.16299. |
| [GetPerAdapterInfo](/windows/win32/api/iphlpapi/nf-iphlpapi-getperadapterinfo) | Introduced into iphlpapi.dll in 10.0.16299. |
| [GetTcpStatisticsEx](/windows/win32/api/iphlpapi/nf-iphlpapi-gettcpstatisticsex) | Introduced into iphlpapi.dll in 10.0.16299. |
| [GetTcpTable](/windows/win32/api/iphlpapi/nf-iphlpapi-gettcptable) | Introduced into iphlpapi.dll in 10.0.16299. |
| [GetUdpStatisticsEx](/windows/win32/api/iphlpapi/nf-iphlpapi-getudpstatisticsex) | Introduced into iphlpapi.dll in 10.0.16299. |
| [GetUdpTable](/windows/win32/api/iphlpapi/nf-iphlpapi-getudptable) | Introduced into iphlpapi.dll in 10.0.16299. |
| [Icmp6CreateFile](/windows/win32/api/icmpapi/nf-icmpapi-icmp6createfile) | Introduced into iphlpapi.dll in 10.0.16299. |
| [Icmp6SendEcho2](/windows/win32/api/icmpapi/nf-icmpapi-icmp6sendecho2) | Introduced into iphlpapi.dll in 10.0.16299. |
| [IcmpCloseHandle](/windows/win32/api/icmpapi/nf-icmpapi-icmpclosehandle) | Introduced into iphlpapi.dll in 10.0.16299. |
| [IcmpCreateFile](/windows/win32/api/icmpapi/nf-icmpapi-icmpcreatefile) | Introduced into iphlpapi.dll in 10.0.16299. |
| [IcmpSendEcho2](/windows/win32/api/icmpapi/nf-icmpapi-icmpsendecho2) | Introduced into iphlpapi.dll in 10.0.16299. |
| [NotifyStableUnicastIpAddressTable](/windows/win32/api/netioapi/nf-netioapi-notifystableunicastipaddresstable) | Introduced into iphlpapi.dll in 10.0.16299. |
| [NotifyUnicastIpAddressChange](/windows/win32/api/netioapi/nf-netioapi-notifyunicastipaddresschange) | Introduced into iphlpapi.dll in 10.0.16299. |


## APIs from msajapi.dll

| API | Requirements |
| -----| --------------|
| alljoyn_aboutdata_createfromxml | Introduced into msajapi.dll in 10.0.14393. |
| alljoyn_abouticon_getcontent | Introduced into msajapi.dll in 10.0.14393. |
| alljoyn_abouticon_geturl | Introduced into msajapi.dll in 10.0.14393. |
| alljoyn_applicationstatelistener_create | Introduced into msajapi.dll in 10.0.14393. |
| alljoyn_applicationstatelistener_destroy | Introduced into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_getpermissionconfigurator | Introduced into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_registerapplicationstatelistener | Introduced into msajapi.dll in 10.0.14393. |
| alljoyn_busattachment_unregisterapplicationstatelistener | Introduced into msajapi.dll in 10.0.14393. |
| alljoyn_interfacedescription_addargannotation | Introduced into msajapi.dll in 10.0.14393. |
| alljoyn_interfacedescription_getdescriptionlanguages | Introduced into msajapi.dll in 10.0.14393. |
| alljoyn_interfacedescription_getdescriptiontranslationcallback | Introduced into msajapi.dll in 10.0.14393. |
| alljoyn_interfacedescription_getmemberargannotation | Introduced into msajapi.dll in 10.0.14393. |
| alljoyn_interfacedescription_hasdescription | Introduced into msajapi.dll in 10.0.14393. |
| alljoyn_interfacedescription_member_getargannotation | Introduced into msajapi.dll in 10.0.14393. |
| alljoyn_interfacedescription_member_getargannotationatindex | Introduced into msajapi.dll in 10.0.14393. |
| alljoyn_interfacedescription_member_getargannotationscount | Introduced into msajapi.dll in 10.0.14393. |
| alljoyn_interfacedescription_setargdescription | Introduced into msajapi.dll in 10.0.14393. |
| alljoyn_interfacedescription_setdescription | Introduced into msajapi.dll in 10.0.14393. |
| alljoyn_interfacedescription_setdescriptionlanguage | Introduced into msajapi.dll in 10.0.14393. |
| alljoyn_interfacedescription_setdescriptiontranslationcallback | Introduced into msajapi.dll in 10.0.14393. |
| alljoyn_interfacedescription_setmemberdescription | Introduced into msajapi.dll in 10.0.14393. |
| alljoyn_interfacedescription_setpropertydescription | Introduced into msajapi.dll in 10.0.14393. |
| alljoyn_permissionconfigurator_getapplicationstate | Introduced into msajapi.dll in 10.0.14393. |
| alljoyn_permissionconfigurator_getclaimcapabilities | Introduced into msajapi.dll in 10.0.14393. |
| alljoyn_permissionconfigurator_getclaimcapabilitiesadditionalinfo | Introduced into msajapi.dll in 10.0.14393. |
| alljoyn_permissionconfigurator_reset | Introduced into msajapi.dll in 10.0.14393. |
| alljoyn_permissionconfigurator_setapplicationstate | Introduced into msajapi.dll in 10.0.14393. |
| alljoyn_permissionconfigurator_setclaimcapabilities | Introduced into msajapi.dll in 10.0.14393. |
| alljoyn_permissionconfigurator_setclaimcapabilitiesadditionalinfo | Introduced into msajapi.dll in 10.0.14393. |
| alljoyn_permissionconfigurator_setmanifestfromxml | Introduced into msajapi.dll in 10.0.14393. |
| alljoyn_securityapplicationproxy_claim | Introduced into msajapi.dll in 10.0.14393. |
| alljoyn_securityapplicationproxy_create | Introduced into msajapi.dll in 10.0.14393. |
| alljoyn_securityapplicationproxy_destroy | Introduced into msajapi.dll in 10.0.14393. |
| alljoyn_securityapplicationproxy_eccpublickey_destroy | Introduced into msajapi.dll in 10.0.14393. |
| alljoyn_securityapplicationproxy_endmanagement | Introduced into msajapi.dll in 10.0.14393. |
| alljoyn_securityapplicationproxy_getapplicationstate | Introduced into msajapi.dll in 10.0.14393. |
| alljoyn_securityapplicationproxy_getclaimcapabilities | Introduced into msajapi.dll in 10.0.14393. |
| alljoyn_securityapplicationproxy_getclaimcapabilitiesadditionalinfo | Introduced into msajapi.dll in 10.0.14393. |
| alljoyn_securityapplicationproxy_geteccpublickey | Introduced into msajapi.dll in 10.0.14393. |
| alljoyn_securityapplicationproxy_getmanifesttemplate | Introduced into msajapi.dll in 10.0.14393. |
| alljoyn_securityapplicationproxy_installmembership | Introduced into msajapi.dll in 10.0.14393. |
| alljoyn_securityapplicationproxy_manifest_destroy | Introduced into msajapi.dll in 10.0.14393. |
| alljoyn_securityapplicationproxy_manifesttemplate_destroy | Introduced into msajapi.dll in 10.0.14393. |
| alljoyn_securityapplicationproxy_reset | Introduced into msajapi.dll in 10.0.14393. |
| alljoyn_securityapplicationproxy_resetpolicy | Introduced into msajapi.dll in 10.0.14393. |
| alljoyn_securityapplicationproxy_signmanifest | Introduced into msajapi.dll in 10.0.14393. |
| alljoyn_securityapplicationproxy_startmanagement | Introduced into msajapi.dll in 10.0.14393. |
| alljoyn_securityapplicationproxy_updateidentity | Introduced into msajapi.dll in 10.0.14393. |
| alljoyn_securityapplicationproxy_updatepolicy | Introduced into msajapi.dll in 10.0.14393. |
| alljoyn_authlistener_setsharedsecret | Introduced into msajapi.dll in 10.0.16299. |
| alljoyn_busattachment_deletedefaultkeystore | Introduced into msajapi.dll in 10.0.16299. |
| alljoyn_interfacedescription_getargdescriptionforlanguage | Introduced into msajapi.dll in 10.0.16299. |
| alljoyn_interfacedescription_getdescriptionforlanguage | Introduced into msajapi.dll in 10.0.16299. |
| alljoyn_interfacedescription_getdescriptionlanguages2 | Introduced into msajapi.dll in 10.0.16299. |
| alljoyn_interfacedescription_getmemberdescriptionforlanguage | Introduced into msajapi.dll in 10.0.16299. |
| alljoyn_interfacedescription_getpropertydescriptionforlanguage | Introduced into msajapi.dll in 10.0.16299. |
| alljoyn_interfacedescription_setargdescriptionforlanguage | Introduced into msajapi.dll in 10.0.16299. |
| alljoyn_interfacedescription_setdescriptionforlanguage | Introduced into msajapi.dll in 10.0.16299. |
| alljoyn_interfacedescription_setmemberdescriptionforlanguage | Introduced into msajapi.dll in 10.0.16299. |
| alljoyn_interfacedescription_setpropertydescriptionforlanguage | Introduced into msajapi.dll in 10.0.16299. |
| alljoyn_keystorelistener_with_synchronization_create | Introduced into msajapi.dll in 10.0.16299. |
| alljoyn_permissionconfigurator_certificatechain_destroy | Introduced into msajapi.dll in 10.0.16299. |
| alljoyn_permissionconfigurator_certificateid_cleanup | Introduced into msajapi.dll in 10.0.16299. |
| alljoyn_permissionconfigurator_certificateidarray_cleanup | Introduced into msajapi.dll in 10.0.16299. |
| alljoyn_permissionconfigurator_claim | Introduced into msajapi.dll in 10.0.16299. |
| alljoyn_permissionconfigurator_endmanagement | Introduced into msajapi.dll in 10.0.16299. |
| alljoyn_permissionconfigurator_getdefaultclaimcapabilities | Introduced into msajapi.dll in 10.0.16299. |
| alljoyn_permissionconfigurator_getdefaultpolicy | Introduced into msajapi.dll in 10.0.16299. |
| alljoyn_permissionconfigurator_getidentity | Introduced into msajapi.dll in 10.0.16299. |
| alljoyn_permissionconfigurator_getidentitycertificateid | Introduced into msajapi.dll in 10.0.16299. |
| alljoyn_permissionconfigurator_getmanifests | Introduced into msajapi.dll in 10.0.16299. |
| alljoyn_permissionconfigurator_getmanifesttemplate | Introduced into msajapi.dll in 10.0.16299. |
| alljoyn_permissionconfigurator_getmembershipsummaries | Introduced into msajapi.dll in 10.0.16299. |
| alljoyn_permissionconfigurator_getpolicy | Introduced into msajapi.dll in 10.0.16299. |
| alljoyn_permissionconfigurator_getpublickey | Introduced into msajapi.dll in 10.0.16299. |
| alljoyn_permissionconfigurator_installmanifests | Introduced into msajapi.dll in 10.0.16299. |
| alljoyn_permissionconfigurator_installmembership | Introduced into msajapi.dll in 10.0.16299. |
| alljoyn_permissionconfigurator_manifestarray_cleanup | Introduced into msajapi.dll in 10.0.16299. |
| alljoyn_permissionconfigurator_manifesttemplate_destroy | Introduced into msajapi.dll in 10.0.16299. |
| alljoyn_permissionconfigurator_policy_destroy | Introduced into msajapi.dll in 10.0.16299. |
| alljoyn_permissionconfigurator_publickey_destroy | Introduced into msajapi.dll in 10.0.16299. |
| alljoyn_permissionconfigurator_removemembership | Introduced into msajapi.dll in 10.0.16299. |
| alljoyn_permissionconfigurator_resetpolicy | Introduced into msajapi.dll in 10.0.16299. |
| alljoyn_permissionconfigurator_setmanifesttemplatefromxml | Introduced into msajapi.dll in 10.0.16299. |
| alljoyn_permissionconfigurator_startmanagement | Introduced into msajapi.dll in 10.0.16299. |
| alljoyn_permissionconfigurator_updateidentity | Introduced into msajapi.dll in 10.0.16299. |
| alljoyn_permissionconfigurator_updatepolicy | Introduced into msajapi.dll in 10.0.16299. |
| alljoyn_routerinit | Introduced into msajapi.dll in 10.0.16299. |
| alljoyn_routerinitwithconfig | Introduced into msajapi.dll in 10.0.16299. |
| alljoyn_routershutdown | Introduced into msajapi.dll in 10.0.16299. |
| alljoyn_securityapplicationproxy_computemanifestdigest | Introduced into msajapi.dll in 10.0.16299. |
| alljoyn_securityapplicationproxy_digest_destroy | Introduced into msajapi.dll in 10.0.16299. |
| alljoyn_securityapplicationproxy_getdefaultpolicy | Introduced into msajapi.dll in 10.0.16299. |
| alljoyn_securityapplicationproxy_getpermissionmanagementsessionport | Introduced into msajapi.dll in 10.0.16299. |
| alljoyn_securityapplicationproxy_getpolicy | Introduced into msajapi.dll in 10.0.16299. |
| alljoyn_securityapplicationproxy_policy_destroy | Introduced into msajapi.dll in 10.0.16299. |
| alljoyn_securityapplicationproxy_setmanifestsignature | Introduced into msajapi.dll in 10.0.16299. |


## APIs from mfsensorgroup.dll

| API | Requirements |
| -----| --------------|
| [MFCreateSensorGroup](/windows/win32/api/mfidl/nf-mfidl-mfcreatesensorgroup) | Introduced into mfsensorgroup.dll in 10.0.16299. |
| [MFCreateSensorStream](/windows/win32/api/mfidl/nf-mfidl-mfcreatesensorstream) | Introduced into mfsensorgroup.dll in 10.0.16299. |


## APIs from api-ms-win-core-kernel32-legacy-ansi-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [SetVolumeLabelA](/windows/win32/api/winbase/nf-winbase-setvolumelabela) | Introduced into api-ms-win-core-kernel32-legacy-ansi-l1-1-0.dll in 10.0.16299. |


## APIs from api-ms-win-core-kernel32-legacy-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [CopyFileA](/windows/win32/api/winbase/nf-winbase-copyfile) | Introduced into api-ms-win-core-kernel32-legacy-l1-1-0.dll in 10.0.16299. |
| [CreateNamedPipeA](/windows/win32/api/winbase/nf-winbase-createnamedpipea) | Introduced into api-ms-win-core-kernel32-legacy-l1-1-0.dll in 10.0.16299. |
| [GetComputerNameA](/windows/win32/api/winbase/nf-winbase-getcomputernamea) | Introduced into api-ms-win-core-kernel32-legacy-l1-1-0.dll in 10.0.16299. |
| [GetComputerNameW](/windows/win32/api/winbase/nf-winbase-getcomputernamea) | Introduced into api-ms-win-core-kernel32-legacy-l1-1-0.dll in 10.0.16299. |
| [GetSystemPowerStatus](/windows/win32/api/winbase/nf-winbase-getsystempowerstatus) | Introduced into api-ms-win-core-kernel32-legacy-l1-1-0.dll in 10.0.16299. |
| [SetFileCompletionNotificationModes](/windows/win32/api/winbase/nf-winbase-setfilecompletionnotificationmodes) | Introduced into api-ms-win-core-kernel32-legacy-l1-1-0.dll in 10.0.16299. |
| [SetVolumeLabelW](/windows/win32/api/winbase/nf-winbase-setvolumelabela) | Introduced into api-ms-win-core-kernel32-legacy-l1-1-0.dll in 10.0.16299. |


## APIs from api-ms-win-core-namespace-ansi-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [CreateBoundaryDescriptorA](/windows/win32/api/winbase/nf-winbase-createboundarydescriptora) | Introduced into api-ms-win-core-namespace-ansi-l1-1-0.dll in 10.0.16299. |
| [CreatePrivateNamespaceA](/windows/win32/api/winbase/nf-winbase-createprivatenamespacea) | Introduced into api-ms-win-core-namespace-ansi-l1-1-0.dll in 10.0.16299. |
| [OpenPrivateNamespaceA](/windows/win32/api/winbase/nf-winbase-openprivatenamespacea) | Introduced into api-ms-win-core-namespace-ansi-l1-1-0.dll in 10.0.16299. |


## APIs from api-ms-win-core-processtopology-obsolete-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [GetProcessAffinityMask](/windows/win32/api/winbase/nf-winbase-getprocessaffinitymask) | Introduced into api-ms-win-core-processtopology-obsolete-l1-1-0.dll in 10.0.16299. |
| [SetProcessAffinityMask](/windows/win32/api/winbase/nf-winbase-setprocessaffinitymask) | Introduced into api-ms-win-core-processtopology-obsolete-l1-1-0.dll in 10.0.16299. |
| [SetThreadAffinityMask](/windows/win32/api/winbase/nf-winbase-setthreadaffinitymask) | Introduced into api-ms-win-core-processtopology-obsolete-l1-1-0.dll in 10.0.16299. |


## APIs from api-ms-win-core-psapi-ansi-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [K32GetModuleBaseNameA](/windows/win32/api/psapi/nf-psapi-getmodulebasenamea) | Introduced into api-ms-win-core-psapi-ansi-l1-1-0.dll in 10.0.16299. |
| [K32GetModuleFileNameExA](/windows/win32/api/psapi/nf-psapi-getmodulefilenameexa) | Introduced into api-ms-win-core-psapi-ansi-l1-1-0.dll in 10.0.16299. |


## APIs from api-ms-win-core-url-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [GetAcceptLanguagesA](/windows/win32/api/shlwapi/nf-shlwapi-getacceptlanguagesa) | Introduced into api-ms-win-core-url-l1-1-0.dll in 10.0.16299. |
| [GetAcceptLanguagesW](/windows/win32/api/shlwapi/nf-shlwapi-getacceptlanguagesa) | Introduced into api-ms-win-core-url-l1-1-0.dll in 10.0.16299. |


## APIs from api-ms-win-core-versionansi-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [GetFileVersionInfoExA](/windows/win32/api/winver/nf-winver-getfileversioninfoexa) | Introduced into api-ms-win-core-versionansi-l1-1-0.dll in 10.0.16299. |
| [GetFileVersionInfoSizeExA](/windows/win32/api/winver/nf-winver-getfileversioninfosizeexa) | Introduced into api-ms-win-core-versionansi-l1-1-0.dll in 10.0.16299. |
| [VerQueryValueA](/windows/win32/api/winver/nf-winver-verqueryvaluea) | Introduced into api-ms-win-core-versionansi-l1-1-0.dll in 10.0.16299. |


## APIs from api-ms-win-core-windowserrorreporting-l1-1-1.dll

| API | Requirements |
| -----| --------------|
| [WerRegisterAdditionalProcess](/windows/win32/api/werapi/nf-werapi-werregisteradditionalprocess) | Introduced into api-ms-win-core-windowserrorreporting-l1-1-1.dll in 10.0.16299. |
| [WerRegisterCustomMetadata](/windows/win32/api/werapi/nf-werapi-werregistercustommetadata) | Introduced into api-ms-win-core-windowserrorreporting-l1-1-1.dll in 10.0.16299. |
| [WerRegisterExcludedMemoryBlock](/windows/win32/api/werapi/nf-werapi-werregisterexcludedmemoryblock) | Introduced into api-ms-win-core-windowserrorreporting-l1-1-1.dll in 10.0.16299. |
| [WerUnregisterAdditionalProcess](/windows/win32/api/werapi/nf-werapi-werunregisteradditionalprocess) | Introduced into api-ms-win-core-windowserrorreporting-l1-1-1.dll in 10.0.16299. |
| [WerUnregisterCustomMetadata](/windows/win32/api/werapi/nf-werapi-werunregistercustommetadata) | Introduced into api-ms-win-core-windowserrorreporting-l1-1-1.dll in 10.0.16299. |
| [WerUnregisterExcludedMemoryBlock](/windows/win32/api/werapi/nf-werapi-werunregisterexcludedmemoryblock) | Introduced into api-ms-win-core-windowserrorreporting-l1-1-1.dll in 10.0.16299. |


## APIs from api-ms-win-core-windowserrorreporting-l1-1-2.dll

| API | Requirements |
| -----| --------------|
| [WerRegisterAppLocalDump](/windows/win32/api/werapi/nf-werapi-werregisterapplocaldump) | Introduced into api-ms-win-core-windowserrorreporting-l1-1-2.dll in 10.0.16299. |
| [WerUnregisterAppLocalDump](/windows/win32/api/werapi/nf-werapi-werunregisterapplocaldump) | Introduced into api-ms-win-core-windowserrorreporting-l1-1-2.dll in 10.0.16299. |


## APIs from api-ms-win-security-lsalookup-ansi-l2-1-0.dll

| API | Requirements |
| -----| --------------|
| [LookupAccountNameA](/windows/win32/api/winbase/nf-winbase-lookupaccountnamea) | Introduced into api-ms-win-security-lsalookup-ansi-l2-1-0.dll in 10.0.16299. |
| [LookupAccountSidA](/windows/win32/api/winbase/nf-winbase-lookupaccountsida) | Introduced into api-ms-win-security-lsalookup-ansi-l2-1-0.dll in 10.0.16299. |
| [LookupPrivilegeDisplayNameA](/windows/win32/api/winbase/nf-winbase-lookupprivilegedisplaynamea) | Introduced into api-ms-win-security-lsalookup-ansi-l2-1-0.dll in 10.0.16299. |
| [LookupPrivilegeNameA](/windows/win32/api/winbase/nf-winbase-lookupprivilegenamea) | Introduced into api-ms-win-security-lsalookup-ansi-l2-1-0.dll in 10.0.16299. |
| [LookupPrivilegeValueA](/windows/win32/api/winbase/nf-winbase-lookupprivilegevaluea) | Introduced into api-ms-win-security-lsalookup-ansi-l2-1-0.dll in 10.0.16299. |


## APIs from api-ms-win-security-lsalookup-l2-1-0.dll

| API | Requirements |
| -----| --------------|
| [LookupAccountNameW](/windows/win32/api/winbase/nf-winbase-lookupaccountnamea) | Introduced into api-ms-win-security-lsalookup-l2-1-0.dll in 10.0.16299. |
| [LookupAccountSidW](/windows/win32/api/winbase/nf-winbase-lookupaccountsida) | Introduced into api-ms-win-security-lsalookup-l2-1-0.dll in 10.0.16299. |
| [LookupPrivilegeDisplayNameW](/windows/win32/api/winbase/nf-winbase-lookupprivilegedisplaynamea) | Introduced into api-ms-win-security-lsalookup-l2-1-0.dll in 10.0.16299. |
| [LookupPrivilegeNameW](/windows/win32/api/winbase/nf-winbase-lookupprivilegenamea) | Introduced into api-ms-win-security-lsalookup-l2-1-0.dll in 10.0.16299. |
| [LookupPrivilegeValueW](/windows/win32/api/winbase/nf-winbase-lookupprivilegevaluea) | Introduced into api-ms-win-security-lsalookup-l2-1-0.dll in 10.0.16299. |


## APIs from api-ms-win-security-provider-ansi-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [GetExplicitEntriesFromAclA](/windows/win32/api/aclapi/nf-aclapi-getexplicitentriesfromacla) | Introduced into api-ms-win-security-provider-ansi-l1-1-0.dll in 10.0.16299. |
| [GetNamedSecurityInfoA](/windows/win32/api/aclapi/nf-aclapi-getnamedsecurityinfoa) | Introduced into api-ms-win-security-provider-ansi-l1-1-0.dll in 10.0.16299. |
| [SetEntriesInAclA](/windows/win32/api/aclapi/nf-aclapi-setentriesinacla) | Introduced into api-ms-win-security-provider-ansi-l1-1-0.dll in 10.0.16299. |
| [SetNamedSecurityInfoA](/windows/win32/api/aclapi/nf-aclapi-setnamedsecurityinfoa) | Introduced into api-ms-win-security-provider-ansi-l1-1-0.dll in 10.0.16299. |


## APIs from api-ms-win-security-provider-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [GetExplicitEntriesFromAclW](/windows/win32/api/aclapi/nf-aclapi-getexplicitentriesfromacla) | Introduced into api-ms-win-security-provider-l1-1-0.dll in 10.0.16299. |
| [GetNamedSecurityInfoW](/windows/win32/api/aclapi/nf-aclapi-getnamedsecurityinfoa) | Introduced into api-ms-win-security-provider-l1-1-0.dll in 10.0.16299. |
| [GetSecurityInfo](/windows/win32/api/aclapi/nf-aclapi-getsecurityinfo) | Introduced into api-ms-win-security-provider-l1-1-0.dll in 10.0.16299. |
| [SetEntriesInAclW](/windows/win32/api/aclapi/nf-aclapi-setentriesinacla) | Introduced into api-ms-win-security-provider-l1-1-0.dll in 10.0.16299. |
| [SetNamedSecurityInfoW](/windows/win32/api/aclapi/nf-aclapi-setnamedsecurityinfoa) | Introduced into api-ms-win-security-provider-l1-1-0.dll in 10.0.16299. |
| [SetSecurityInfo](/windows/win32/api/aclapi/nf-aclapi-setsecurityinfo) | Introduced into api-ms-win-security-provider-l1-1-0.dll in 10.0.16299. |


## APIs from api-ms-win-security-sddl-ansi-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [ConvertSidToStringSidA](/windows/win32/api/sddl/nf-sddl-convertsidtostringsida) | Introduced into api-ms-win-security-sddl-ansi-l1-1-0.dll in 10.0.16299. |
| [ConvertStringSidToSidA](/windows/win32/api/sddl/nf-sddl-convertstringsidtosida) | Introduced into api-ms-win-security-sddl-ansi-l1-1-0.dll in 10.0.16299. |


## APIs from coremessaging.dll

| API | Requirements |
| -----| --------------|
| [CreateDispatcherQueueController](/windows/win32/api/dispatcherqueue/nf-dispatcherqueue-createdispatcherqueuecontroller) | Introduced into coremessaging.dll in 10.0.16299. |


## APIs from api-ms-win-core-localization-obsolete-l1-2-0.dll

| API | Requirements |
| -----| --------------|
| [EnumUILanguagesW](/windows/win32/api/winnls/nf-winnls-enumuilanguagesa) | Introduced into api-ms-win-core-localization-obsolete-l1-2-0.dll in 10.0.16299. |
| [GetUserDefaultUILanguage](/windows/win32/api/winnls/nf-winnls-getuserdefaultuilanguage) | Introduced into api-ms-win-core-localization-obsolete-l1-2-0.dll in 10.0.16299. |


## APIs from api-ms-win-core-namedpipe-ansi-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [GetNamedPipeClientComputerNameA](/windows/win32/api/winbase/nf-winbase-getnamedpipeclientcomputernamea) | Introduced into api-ms-win-core-namedpipe-ansi-l1-1-0.dll in 10.0.16299. |
| [GetNamedPipeHandleStateA](/windows/win32/api/winbase/nf-winbase-getnamedpipehandlestatea) | Introduced into api-ms-win-core-namedpipe-ansi-l1-1-0.dll in 10.0.16299. |
| [WaitNamedPipeA](/windows/win32/api/winbase/nf-winbase-waitnamedpipea) | Introduced into api-ms-win-core-namedpipe-ansi-l1-1-0.dll in 10.0.16299. |


## APIs from api-ms-win-core-namedpipe-ansi-l1-1-1.dll

| API | Requirements |
| -----| --------------|
| [CallNamedPipeA](/windows/win32/api/winbase/nf-winbase-callnamedpipea) | Introduced into api-ms-win-core-namedpipe-ansi-l1-1-1.dll in 10.0.16299. |


## APIs from api-ms-win-core-console-l2-1-0.dll

| API | Requirements |
| -----| --------------|
| [FillConsoleOutputAttribute](/windows/console/fillconsoleoutputattribute) | Introduced into api-ms-win-core-console-l2-1-0.dll in 10.0.16299. |
| [FillConsoleOutputCharacterW](/windows/console/fillconsoleoutputcharacter) | Introduced into api-ms-win-core-console-l2-1-0.dll in 10.0.16299. |
| [GetConsoleCursorInfo](/windows/console/getconsolecursorinfo) | Introduced into api-ms-win-core-console-l2-1-0.dll in 10.0.16299. |
| [GetConsoleScreenBufferInfo](/windows/console/getconsolescreenbufferinfo) | Introduced into api-ms-win-core-console-l2-1-0.dll in 10.0.16299. |
| [GetConsoleTitleW](/windows/console/getconsoletitle) | Introduced into api-ms-win-core-console-l2-1-0.dll in 10.0.16299. Moved into api-ms-win-core-console-l2-2-0.dll in 10.0.17134. |
| [GetLargestConsoleWindowSize](/windows/console/getlargestconsolewindowsize) | Introduced into api-ms-win-core-console-l2-1-0.dll in 10.0.16299. |
| [PeekConsoleInputW](/windows/console/peekconsoleinput) | Introduced into api-ms-win-core-console-l2-1-0.dll in 10.0.16299. Moved into api-ms-win-core-console-l1-2-0.dll in 10.0.17134. |
| [ReadConsoleOutputW](/windows/console/readconsoleoutput) | Introduced into api-ms-win-core-console-l2-1-0.dll in 10.0.16299. |
| [SetConsoleCP](/windows/console/setconsolecp) | Introduced into api-ms-win-core-console-l2-1-0.dll in 10.0.16299. |
| [SetConsoleCursorInfo](/windows/console/setconsolecursorinfo) | Introduced into api-ms-win-core-console-l2-1-0.dll in 10.0.16299. |
| [SetConsoleCursorPosition](/windows/console/setconsolecursorposition) | Introduced into api-ms-win-core-console-l2-1-0.dll in 10.0.16299. |
| [SetConsoleOutputCP](/windows/console/setconsoleoutputcp) | Introduced into api-ms-win-core-console-l2-1-0.dll in 10.0.16299. |
| [SetConsoleScreenBufferSize](/windows/console/setconsolescreenbuffersize) | Introduced into api-ms-win-core-console-l2-1-0.dll in 10.0.16299. |
| [SetConsoleTextAttribute](/windows/console/setconsoletextattribute) | Introduced into api-ms-win-core-console-l2-1-0.dll in 10.0.16299. |
| [SetConsoleTitleW](/windows/console/setconsoletitle) | Introduced into api-ms-win-core-console-l2-1-0.dll in 10.0.16299. Moved into api-ms-win-core-console-l2-2-0.dll in 10.0.17134. |
| [SetConsoleWindowInfo](/windows/console/setconsolewindowinfo) | Introduced into api-ms-win-core-console-l2-1-0.dll in 10.0.16299. |
| [WriteConsoleOutputW](/windows/console/writeconsoleoutput) | Introduced into api-ms-win-core-console-l2-1-0.dll in 10.0.16299. |
| [CreateConsoleScreenBuffer](/windows/console/createconsolescreenbuffer) | Introduced into api-ms-win-core-console-l2-1-0.dll in 10.0.17134. |
| [FillConsoleOutputCharacterA](/windows/console/fillconsoleoutputcharacter) | Introduced into api-ms-win-core-console-l2-1-0.dll in 10.0.17134. |
| [FlushConsoleInputBuffer](/windows/console/flushconsoleinputbuffer) | Introduced into api-ms-win-core-console-l2-1-0.dll in 10.0.17134. |
| [GenerateConsoleCtrlEvent](/windows/console/generateconsolectrlevent) | Introduced into api-ms-win-core-console-l2-1-0.dll in 10.0.17134. |
| [GetConsoleScreenBufferInfoEx](/windows/console/getconsolescreenbufferinfoex) | Introduced into api-ms-win-core-console-l2-1-0.dll in 10.0.17134. |
| [ReadConsoleOutputA](/windows/console/readconsoleoutput) | Introduced into api-ms-win-core-console-l2-1-0.dll in 10.0.17134. |
| [ReadConsoleOutputAttribute](/windows/console/readconsoleoutputattribute) | Introduced into api-ms-win-core-console-l2-1-0.dll in 10.0.17134. |
| [ReadConsoleOutputCharacterA](/windows/console/readconsoleoutputcharacter) | Introduced into api-ms-win-core-console-l2-1-0.dll in 10.0.17134. |
| [ReadConsoleOutputCharacterW](/windows/console/readconsoleoutputcharacter) | Introduced into api-ms-win-core-console-l2-1-0.dll in 10.0.17134. |
| [ScrollConsoleScreenBufferA](/windows/console/scrollconsolescreenbuffer) | Introduced into api-ms-win-core-console-l2-1-0.dll in 10.0.17134. |
| [ScrollConsoleScreenBufferW](/windows/console/scrollconsolescreenbuffer) | Introduced into api-ms-win-core-console-l2-1-0.dll in 10.0.17134. |
| [SetConsoleActiveScreenBuffer](/windows/console/setconsoleactivescreenbuffer) | Introduced into api-ms-win-core-console-l2-1-0.dll in 10.0.17134. |
| [SetConsoleScreenBufferInfoEx](/windows/console/setconsolescreenbufferinfoex) | Introduced into api-ms-win-core-console-l2-1-0.dll in 10.0.17134. |
| [WriteConsoleInputA](/windows/console/writeconsoleinput) | Introduced into api-ms-win-core-console-l2-1-0.dll in 10.0.17134. |
| [WriteConsoleInputW](/windows/console/writeconsoleinput) | Introduced into api-ms-win-core-console-l2-1-0.dll in 10.0.17134. |
| [WriteConsoleOutputA](/windows/console/writeconsoleoutput) | Introduced into api-ms-win-core-console-l2-1-0.dll in 10.0.17134. |
| [WriteConsoleOutputAttribute](/windows/console/writeconsoleoutputattribute) | Introduced into api-ms-win-core-console-l2-1-0.dll in 10.0.17134. |
| [WriteConsoleOutputCharacterA](/windows/console/writeconsoleoutputcharacter) | Introduced into api-ms-win-core-console-l2-1-0.dll in 10.0.17134. |
| [WriteConsoleOutputCharacterW](/windows/console/writeconsoleoutputcharacter) | Introduced into api-ms-win-core-console-l2-1-0.dll in 10.0.17134. |


## APIs from api-ms-win-core-file-l2-1-0.dll

| API | Requirements |
| -----| --------------|
| [CopyFileExW](/windows/win32/api/winbase/nf-winbase-copyfileexa) | Introduced into api-ms-win-core-file-l2-1-0.dll in 10.0.16299. |
| [ReadDirectoryChangesW](/windows/win32/api/winbase/nf-winbase-readdirectorychangesw) | Introduced into api-ms-win-core-file-l2-1-0.dll in 10.0.16299. |


## APIs from api-ms-win-core-file-l2-1-2.dll

| API | Requirements |
| -----| --------------|
| [CopyFileW](/windows/win32/api/winbase/nf-winbase-copyfile) | Introduced into api-ms-win-core-file-l2-1-2.dll in 10.0.16299. |


## APIs from api-ms-win-core-version-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [GetFileVersionInfoExW](/windows/win32/api/winver/nf-winver-getfileversioninfoexa) | Introduced into api-ms-win-core-version-l1-1-0.dll in 10.0.16299. |
| [GetFileVersionInfoSizeExW](/windows/win32/api/winver/nf-winver-getfileversioninfosizeexa) | Introduced into api-ms-win-core-version-l1-1-0.dll in 10.0.16299. |
| [VerQueryValueW](/windows/win32/api/winver/nf-winver-verqueryvaluea) | Introduced into api-ms-win-core-version-l1-1-0.dll in 10.0.16299. |


## APIs from api-ms-win-core-file-ansi-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [DeleteVolumeMountPointA](/windows/win32/api/fileapi/nf-fileapi-deletevolumemountpointw) | Introduced into api-ms-win-core-file-ansi-l1-1-0.dll in 10.0.16299. |


## APIs from api-ms-win-core-errorhandling-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [SetErrorMode](/windows/win32/api/errhandlingapi/nf-errhandlingapi-seterrormode) | Introduced into api-ms-win-core-errorhandling-l1-1-0.dll in 10.0.16299. |


## APIs from api-ms-win-core-file-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [DeleteVolumeMountPointW](/windows/win32/api/fileapi/nf-fileapi-deletevolumemountpointw) | Introduced into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. |
| [GetDriveTypeA](/windows/win32/api/fileapi/nf-fileapi-getdrivetypea) | Introduced into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. |
| [GetDriveTypeW](/windows/win32/api/fileapi/nf-fileapi-getdrivetypea) | Introduced into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. |
| [GetFullPathNameA](/windows/win32/api/fileapi/nf-fileapi-getfullpathnamea) | Introduced into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. |
| [GetLogicalDrives](/windows/win32/api/fileapi/nf-fileapi-getlogicaldrives) | Introduced into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. |
| [GetVolumeInformationW](/windows/win32/api/fileapi/nf-fileapi-getvolumeinformationa) | Introduced into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. |
| [LockFile](/windows/win32/api/fileapi/nf-fileapi-lockfile) | Introduced into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. |
| [UnlockFile](/windows/win32/api/fileapi/nf-fileapi-unlockfile) | Introduced into api-ms-win-core-file-l1-1-0.dll in 10.0.16299. |


## APIs from api-ms-win-core-interlocked-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [InterlockedCompareExchange](/windows/win32/direct3dhlsl/interlockedcompareexchange) | Introduced into api-ms-win-core-interlocked-l1-1-0.dll in 10.0.16299. |
| [InterlockedCompareExchange64](/windows/win32/api/winnt/nf-winnt-interlockedcompareexchange64) | Introduced into api-ms-win-core-interlocked-l1-1-0.dll in 10.0.16299. |
| [InterlockedDecrement](/windows/win32/api/winnt/nf-winnt-interlockeddecrement) | Introduced into api-ms-win-core-interlocked-l1-1-0.dll in 10.0.16299. |
| [InterlockedExchange](/windows/win32/direct3dhlsl/interlockedexchange) | Introduced into api-ms-win-core-interlocked-l1-1-0.dll in 10.0.16299. |
| [InterlockedExchangeAdd](/windows/win32/api/winnt/nf-winnt-interlockedexchangeadd) | Introduced into api-ms-win-core-interlocked-l1-1-0.dll in 10.0.16299. |
| [InterlockedIncrement](/windows/win32/api/winnt/nf-winnt-interlockedincrement) | Introduced into api-ms-win-core-interlocked-l1-1-0.dll in 10.0.16299. |


## APIs from api-ms-win-core-localization-l1-2-0.dll

| API | Requirements |
| -----| --------------|
| [GetACP](/windows/win32/api/winnls/nf-winnls-getacp) | Introduced into api-ms-win-core-localization-l1-2-0.dll in 10.0.16299. |
| [GetLocaleInfoA](/windows/win32/api/winnls/nf-winnls-getlocaleinfoa) | Introduced into api-ms-win-core-localization-l1-2-0.dll in 10.0.16299. |
| [GetLocaleInfoW](/windows/win32/api/winnls/nf-winnls-getlocaleinfoa) | Introduced into api-ms-win-core-localization-l1-2-0.dll in 10.0.16299. |
| [GetUserDefaultLangID](/windows/win32/api/winnls/nf-winnls-getuserdefaultlangid) | Introduced into api-ms-win-core-localization-l1-2-0.dll in 10.0.16299. |
| [IsDBCSLeadByte](/windows/win32/api/winnls/nf-winnls-isdbcsleadbyte) | Introduced into api-ms-win-core-localization-l1-2-0.dll in 10.0.16299. |
| [IsDBCSLeadByteEx](/windows/win32/api/winnls/nf-winnls-isdbcsleadbyteex) | Introduced into api-ms-win-core-localization-l1-2-0.dll in 10.0.16299. |
| [IsNLSDefinedString](/windows/win32/api/winnls/nf-winnls-isnlsdefinedstring) | Introduced into api-ms-win-core-localization-l1-2-0.dll in 10.0.16299. |
| [VerLanguageNameA](/windows/win32/api/winver/nf-winver-verlanguagenamea) | Introduced into api-ms-win-core-localization-l1-2-0.dll in 10.0.16299. |
| [VerLanguageNameW](/windows/win32/api/winver/nf-winver-verlanguagenamea) | Introduced into api-ms-win-core-localization-l1-2-0.dll in 10.0.16299. |


## APIs from api-ms-win-core-wow64-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [IsWow64Process](/windows/win32/api/wow64apiset/nf-wow64apiset-iswow64process) | Introduced into api-ms-win-core-wow64-l1-1-0.dll in 10.0.16299. |


## APIs from api-ms-win-core-memory-l1-1-1.dll

| API | Requirements |
| -----| --------------|
| [GetLargePageMinimum](/windows/win32/api/memoryapi/nf-memoryapi-getlargepageminimum) | Introduced into api-ms-win-core-memory-l1-1-1.dll in 10.0.16299. |
| [GetProcessWorkingSetSizeEx](/windows/win32/api/memoryapi/nf-memoryapi-getprocessworkingsetsizeex) | Introduced into api-ms-win-core-memory-l1-1-1.dll in 10.0.16299. |
| [SetProcessWorkingSetSizeEx](/windows/win32/api/memoryapi/nf-memoryapi-setprocessworkingsetsizeex) | Introduced into api-ms-win-core-memory-l1-1-1.dll in 10.0.16299. |


## APIs from api-ms-win-core-namedpipe-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [ConnectNamedPipe](/windows/win32/api/namedpipeapi/nf-namedpipeapi-connectnamedpipe) | Introduced into api-ms-win-core-namedpipe-l1-1-0.dll in 10.0.16299. |
| [CreateNamedPipeW](/windows/win32/api/winbase/nf-winbase-createnamedpipea) | Introduced into api-ms-win-core-namedpipe-l1-1-0.dll in 10.0.16299. |
| [CreatePipe](/windows/win32/api/namedpipeapi/nf-namedpipeapi-createpipe) | Introduced into api-ms-win-core-namedpipe-l1-1-0.dll in 10.0.16299. |
| [DisconnectNamedPipe](/windows/win32/api/namedpipeapi/nf-namedpipeapi-disconnectnamedpipe) | Introduced into api-ms-win-core-namedpipe-l1-1-0.dll in 10.0.16299. |
| [GetNamedPipeClientComputerNameW](/windows/win32/api/winbase/nf-winbase-getnamedpipeclientcomputernamea) | Introduced into api-ms-win-core-namedpipe-l1-1-0.dll in 10.0.16299. |
| [PeekNamedPipe](/windows/win32/api/namedpipeapi/nf-namedpipeapi-peeknamedpipe) | Introduced into api-ms-win-core-namedpipe-l1-1-0.dll in 10.0.16299. |
| [SetNamedPipeHandleState](/windows/win32/api/namedpipeapi/nf-namedpipeapi-setnamedpipehandlestate) | Introduced into api-ms-win-core-namedpipe-l1-1-0.dll in 10.0.16299. |
| [TransactNamedPipe](/windows/win32/api/namedpipeapi/nf-namedpipeapi-transactnamedpipe) | Introduced into api-ms-win-core-namedpipe-l1-1-0.dll in 10.0.16299. |
| [WaitNamedPipeW](/windows/win32/api/winbase/nf-winbase-waitnamedpipea) | Introduced into api-ms-win-core-namedpipe-l1-1-0.dll in 10.0.16299. |


## APIs from api-ms-win-core-namedpipe-l1-2-1.dll

| API | Requirements |
| -----| --------------|
| [GetNamedPipeHandleStateW](/windows/win32/api/winbase/nf-winbase-getnamedpipehandlestatea) | Introduced into api-ms-win-core-namedpipe-l1-2-1.dll in 10.0.16299. |
| [GetNamedPipeInfo](/windows/win32/api/namedpipeapi/nf-namedpipeapi-getnamedpipeinfo) | Introduced into api-ms-win-core-namedpipe-l1-2-1.dll in 10.0.16299. |


## APIs from api-ms-win-core-processenvironment-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [ExpandEnvironmentStringsA](/windows/win32/api/processenv/nf-processenv-expandenvironmentstringsa) | Introduced into api-ms-win-core-processenvironment-l1-1-0.dll in 10.0.16299. |
| [ExpandEnvironmentStringsW](/windows/win32/api/processenv/nf-processenv-expandenvironmentstringsa) | Introduced into api-ms-win-core-processenvironment-l1-1-0.dll in 10.0.16299. |
| [FreeEnvironmentStringsA](/windows/win32/api/processenv/nf-processenv-freeenvironmentstringsa) | Introduced into api-ms-win-core-processenvironment-l1-1-0.dll in 10.0.16299. |
| [FreeEnvironmentStringsW](/windows/win32/api/processenv/nf-processenv-freeenvironmentstringsa) | Introduced into api-ms-win-core-processenvironment-l1-1-0.dll in 10.0.16299. |
| [GetEnvironmentStrings](/windows/win32/api/processenv/nf-processenv-getenvironmentstrings) | Introduced into api-ms-win-core-processenvironment-l1-1-0.dll in 10.0.16299. |
| [GetEnvironmentStringsW](/windows/win32/api/processenv/nf-processenv-getenvironmentstrings) | Introduced into api-ms-win-core-processenvironment-l1-1-0.dll in 10.0.16299. |
| [GetEnvironmentVariableA](/windows/win32/api/processenv/nf-processenv-getenvironmentvariablea) | Introduced into api-ms-win-core-processenvironment-l1-1-0.dll in 10.0.16299. |
| [GetEnvironmentVariableW](/windows/win32/api/processenv/nf-processenv-getenvironmentvariablea) | Introduced into api-ms-win-core-processenvironment-l1-1-0.dll in 10.0.16299. |
| [GetStdHandle](/windows/console/getstdhandle) | Introduced into api-ms-win-core-processenvironment-l1-1-0.dll in 10.0.16299. |
| [SetEnvironmentVariableA](/windows/win32/api/processenv/nf-processenv-setenvironmentvariablea) | Introduced into api-ms-win-core-processenvironment-l1-1-0.dll in 10.0.16299. |
| [SetEnvironmentVariableW](/windows/win32/api/processenv/nf-processenv-setenvironmentvariablea) | Introduced into api-ms-win-core-processenvironment-l1-1-0.dll in 10.0.16299. |
| [SetStdHandle](/windows/console/setstdhandle) | Introduced into api-ms-win-core-processenvironment-l1-1-0.dll in 10.0.16299. |
| SetStdHandleEx | Introduced into api-ms-win-core-processenvironment-l1-1-0.dll in 10.0.16299. |


## APIs from api-ms-win-core-processthreads-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [CreateProcessA](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa) | Introduced into api-ms-win-core-processthreads-l1-1-0.dll in 10.0.16299. |
| [CreateProcessW](/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessa) | Introduced into api-ms-win-core-processthreads-l1-1-0.dll in 10.0.16299. |
| [GetExitCodeProcess](/windows/win32/api/processthreadsapi/nf-processthreadsapi-getexitcodeprocess) | Introduced into api-ms-win-core-processthreads-l1-1-0.dll in 10.0.16299. |
| [GetPriorityClass](/windows/win32/api/processthreadsapi/nf-processthreadsapi-getpriorityclass) | Introduced into api-ms-win-core-processthreads-l1-1-0.dll in 10.0.16299. |
| [GetProcessId](/windows/win32/api/processthreadsapi/nf-processthreadsapi-getprocessid) | Introduced into api-ms-win-core-processthreads-l1-1-0.dll in 10.0.16299. |
| [GetProcessTimes](/windows/win32/api/processthreadsapi/nf-processthreadsapi-getprocesstimes) | Introduced into api-ms-win-core-processthreads-l1-1-0.dll in 10.0.16299. |
| [GetThreadPriorityBoost](/windows/win32/api/processthreadsapi/nf-processthreadsapi-getthreadpriorityboost) | Introduced into api-ms-win-core-processthreads-l1-1-0.dll in 10.0.16299. |
| [OpenProcessToken](/windows/win32/api/processthreadsapi/nf-processthreadsapi-openprocesstoken) | Introduced into api-ms-win-core-processthreads-l1-1-0.dll in 10.0.16299. |
| [OpenThread](/windows/win32/api/processthreadsapi/nf-processthreadsapi-openthread) | Introduced into api-ms-win-core-processthreads-l1-1-0.dll in 10.0.16299. |
| [OpenThreadToken](/windows/win32/api/processthreadsapi/nf-processthreadsapi-openthreadtoken) | Introduced into api-ms-win-core-processthreads-l1-1-0.dll in 10.0.16299. |
| [SetPriorityClass](/windows/win32/api/processthreadsapi/nf-processthreadsapi-setpriorityclass) | Introduced into api-ms-win-core-processthreads-l1-1-0.dll in 10.0.16299. |
| [SetThreadPriorityBoost](/windows/win32/api/processthreadsapi/nf-processthreadsapi-setthreadpriorityboost) | Introduced into api-ms-win-core-processthreads-l1-1-0.dll in 10.0.16299. |
| [SetThreadToken](/windows/win32/api/processthreadsapi/nf-processthreadsapi-setthreadtoken) | Introduced into api-ms-win-core-processthreads-l1-1-0.dll in 10.0.16299. |
| [ExitProcess](/windows/win32/api/processthreadsapi/nf-processthreadsapi-exitprocess) | Introduced into api-ms-win-core-processthreads-l1-1-0.dll in 10.0.17763. |


## APIs from api-ms-win-core-processthreads-l1-1-1.dll

| API | Requirements |
| -----| --------------|
| [FlushInstructionCache](/windows/win32/api/processthreadsapi/nf-processthreadsapi-flushinstructioncache) | Introduced into api-ms-win-core-processthreads-l1-1-1.dll in 10.0.16299. |
| [GetCurrentProcessorNumber](/windows/win32/api/processthreadsapi/nf-processthreadsapi-getcurrentprocessornumber) | Introduced into api-ms-win-core-processthreads-l1-1-1.dll in 10.0.16299. |
| [GetCurrentProcessorNumberEx](/windows/win32/api/processthreadsapi/nf-processthreadsapi-getcurrentprocessornumberex) | Introduced into api-ms-win-core-processthreads-l1-1-1.dll in 10.0.16299. |
| [GetCurrentThreadStackLimits](/windows/win32/api/processthreadsapi/nf-processthreadsapi-getcurrentthreadstacklimits) | Introduced into api-ms-win-core-processthreads-l1-1-1.dll in 10.0.16299. |
| [GetProcessMitigationPolicy](/windows/win32/api/processthreadsapi/nf-processthreadsapi-getprocessmitigationpolicy) | Introduced into api-ms-win-core-processthreads-l1-1-1.dll in 10.0.16299. |
| [GetThreadIdealProcessorEx](/windows/win32/api/processthreadsapi/nf-processthreadsapi-getthreadidealprocessorex) | Introduced into api-ms-win-core-processthreads-l1-1-1.dll in 10.0.16299. |
| [GetThreadTimes](/windows/win32/api/processthreadsapi/nf-processthreadsapi-getthreadtimes) | Introduced into api-ms-win-core-processthreads-l1-1-1.dll in 10.0.16299. |


## APIs from api-ms-win-security-base-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [AddAccessAllowedAce](/windows/win32/api/securitybaseapi/nf-securitybaseapi-addaccessallowedace) | Introduced into api-ms-win-security-base-l1-1-0.dll in 10.0.16299. |
| [AddAccessAllowedAceEx](/windows/win32/api/securitybaseapi/nf-securitybaseapi-addaccessallowedaceex) | Introduced into api-ms-win-security-base-l1-1-0.dll in 10.0.16299. |
| [AddAce](/windows/win32/api/securitybaseapi/nf-securitybaseapi-addace) | Introduced into api-ms-win-security-base-l1-1-0.dll in 10.0.16299. |
| [AddMandatoryAce](/windows/win32/api/securitybaseapi/nf-securitybaseapi-addmandatoryace) | Introduced into api-ms-win-security-base-l1-1-0.dll in 10.0.16299. |
| [AdjustTokenGroups](/windows/win32/api/securitybaseapi/nf-securitybaseapi-adjusttokengroups) | Introduced into api-ms-win-security-base-l1-1-0.dll in 10.0.16299. |
| [AdjustTokenPrivileges](/windows/win32/api/securitybaseapi/nf-securitybaseapi-adjusttokenprivileges) | Introduced into api-ms-win-security-base-l1-1-0.dll in 10.0.16299. |
| [AllocateAndInitializeSid](/windows/win32/api/securitybaseapi/nf-securitybaseapi-allocateandinitializesid) | Introduced into api-ms-win-security-base-l1-1-0.dll in 10.0.16299. |
| [AllocateLocallyUniqueId](/windows/win32/api/securitybaseapi/nf-securitybaseapi-allocatelocallyuniqueid) | Introduced into api-ms-win-security-base-l1-1-0.dll in 10.0.16299. |
| [CheckTokenMembership](/windows/win32/api/securitybaseapi/nf-securitybaseapi-checktokenmembership) | Introduced into api-ms-win-security-base-l1-1-0.dll in 10.0.16299. |
| [CopySid](/windows/win32/api/securitybaseapi/nf-securitybaseapi-copysid) | Introduced into api-ms-win-security-base-l1-1-0.dll in 10.0.16299. |
| [CreateWellKnownSid](/windows/win32/api/securitybaseapi/nf-securitybaseapi-createwellknownsid) | Introduced into api-ms-win-security-base-l1-1-0.dll in 10.0.16299. |
| [DeleteAce](/windows/win32/api/securitybaseapi/nf-securitybaseapi-deleteace) | Introduced into api-ms-win-security-base-l1-1-0.dll in 10.0.16299. |
| [DuplicateToken](/windows/win32/api/securitybaseapi/nf-securitybaseapi-duplicatetoken) | Introduced into api-ms-win-security-base-l1-1-0.dll in 10.0.16299. |
| [DuplicateTokenEx](/windows/win32/api/securitybaseapi/nf-securitybaseapi-duplicatetokenex) | Introduced into api-ms-win-security-base-l1-1-0.dll in 10.0.16299. |
| [EqualDomainSid](/windows/win32/api/securitybaseapi/nf-securitybaseapi-equaldomainsid) | Introduced into api-ms-win-security-base-l1-1-0.dll in 10.0.16299. |
| [FreeSid](/windows/win32/api/securitybaseapi/nf-securitybaseapi-freesid) | Introduced into api-ms-win-security-base-l1-1-0.dll in 10.0.16299. |
| [GetAce](/windows/win32/api/securitybaseapi/nf-securitybaseapi-getace) | Introduced into api-ms-win-security-base-l1-1-0.dll in 10.0.16299. |
| [GetAclInformation](/windows/win32/api/securitybaseapi/nf-securitybaseapi-getaclinformation) | Introduced into api-ms-win-security-base-l1-1-0.dll in 10.0.16299. |
| [GetKernelObjectSecurity](/windows/win32/api/securitybaseapi/nf-securitybaseapi-getkernelobjectsecurity) | Introduced into api-ms-win-security-base-l1-1-0.dll in 10.0.16299. |
| [GetLengthSid](/windows/win32/api/securitybaseapi/nf-securitybaseapi-getlengthsid) | Introduced into api-ms-win-security-base-l1-1-0.dll in 10.0.16299. |
| [GetSecurityDescriptorControl](/windows/win32/api/securitybaseapi/nf-securitybaseapi-getsecuritydescriptorcontrol) | Introduced into api-ms-win-security-base-l1-1-0.dll in 10.0.16299. |
| [GetSecurityDescriptorDacl](/windows/win32/api/securitybaseapi/nf-securitybaseapi-getsecuritydescriptordacl) | Introduced into api-ms-win-security-base-l1-1-0.dll in 10.0.16299. |
| [GetSecurityDescriptorGroup](/windows/win32/api/securitybaseapi/nf-securitybaseapi-getsecuritydescriptorgroup) | Introduced into api-ms-win-security-base-l1-1-0.dll in 10.0.16299. |
| [GetSecurityDescriptorLength](/windows/win32/api/securitybaseapi/nf-securitybaseapi-getsecuritydescriptorlength) | Introduced into api-ms-win-security-base-l1-1-0.dll in 10.0.16299. |
| [GetSecurityDescriptorOwner](/windows/win32/api/securitybaseapi/nf-securitybaseapi-getsecuritydescriptorowner) | Introduced into api-ms-win-security-base-l1-1-0.dll in 10.0.16299. |
| [GetSecurityDescriptorRMControl](/windows/win32/api/securitybaseapi/nf-securitybaseapi-getsecuritydescriptorrmcontrol) | Introduced into api-ms-win-security-base-l1-1-0.dll in 10.0.16299. |
| [GetSecurityDescriptorSacl](/windows/win32/api/securitybaseapi/nf-securitybaseapi-getsecuritydescriptorsacl) | Introduced into api-ms-win-security-base-l1-1-0.dll in 10.0.16299. |
| [GetSidIdentifierAuthority](/windows/win32/api/securitybaseapi/nf-securitybaseapi-getsididentifierauthority) | Introduced into api-ms-win-security-base-l1-1-0.dll in 10.0.16299. |
| [GetSidLengthRequired](/windows/win32/api/securitybaseapi/nf-securitybaseapi-getsidlengthrequired) | Introduced into api-ms-win-security-base-l1-1-0.dll in 10.0.16299. |
| [GetSidSubAuthority](/windows/win32/api/securitybaseapi/nf-securitybaseapi-getsidsubauthority) | Introduced into api-ms-win-security-base-l1-1-0.dll in 10.0.16299. |
| [GetSidSubAuthorityCount](/windows/win32/api/securitybaseapi/nf-securitybaseapi-getsidsubauthoritycount) | Introduced into api-ms-win-security-base-l1-1-0.dll in 10.0.16299. |
| [GetTokenInformation](/windows/win32/api/securitybaseapi/nf-securitybaseapi-gettokeninformation) | Introduced into api-ms-win-security-base-l1-1-0.dll in 10.0.16299. |
| [GetWindowsAccountDomainSid](/windows/win32/api/securitybaseapi/nf-securitybaseapi-getwindowsaccountdomainsid) | Introduced into api-ms-win-security-base-l1-1-0.dll in 10.0.16299. |
| [InitializeAcl](/windows/win32/api/securitybaseapi/nf-securitybaseapi-initializeacl) | Introduced into api-ms-win-security-base-l1-1-0.dll in 10.0.16299. |
| [InitializeSecurityDescriptor](/windows/win32/api/securitybaseapi/nf-securitybaseapi-initializesecuritydescriptor) | Introduced into api-ms-win-security-base-l1-1-0.dll in 10.0.16299. |
| [InitializeSid](/windows/win32/api/securitybaseapi/nf-securitybaseapi-initializesid) | Introduced into api-ms-win-security-base-l1-1-0.dll in 10.0.16299. |
| [IsValidAcl](/windows/win32/api/securitybaseapi/nf-securitybaseapi-isvalidacl) | Introduced into api-ms-win-security-base-l1-1-0.dll in 10.0.16299. |
| [IsValidSecurityDescriptor](/windows/win32/api/securitybaseapi/nf-securitybaseapi-isvalidsecuritydescriptor) | Introduced into api-ms-win-security-base-l1-1-0.dll in 10.0.16299. |
| [IsValidSid](/windows/win32/api/securitybaseapi/nf-securitybaseapi-isvalidsid) | Introduced into api-ms-win-security-base-l1-1-0.dll in 10.0.16299. |
| [IsWellKnownSid](/windows/win32/api/securitybaseapi/nf-securitybaseapi-iswellknownsid) | Introduced into api-ms-win-security-base-l1-1-0.dll in 10.0.16299. |
| [MakeAbsoluteSD](/windows/win32/api/securitybaseapi/nf-securitybaseapi-makeabsolutesd) | Introduced into api-ms-win-security-base-l1-1-0.dll in 10.0.16299. |
| [MakeSelfRelativeSD](/windows/win32/api/securitybaseapi/nf-securitybaseapi-makeselfrelativesd) | Introduced into api-ms-win-security-base-l1-1-0.dll in 10.0.16299. |
| [SetKernelObjectSecurity](/windows/win32/api/securitybaseapi/nf-securitybaseapi-setkernelobjectsecurity) | Introduced into api-ms-win-security-base-l1-1-0.dll in 10.0.16299. |
| [SetSecurityDescriptorControl](/windows/win32/api/securitybaseapi/nf-securitybaseapi-setsecuritydescriptorcontrol) | Introduced into api-ms-win-security-base-l1-1-0.dll in 10.0.16299. |
| [SetSecurityDescriptorDacl](/windows/win32/api/securitybaseapi/nf-securitybaseapi-setsecuritydescriptordacl) | Introduced into api-ms-win-security-base-l1-1-0.dll in 10.0.16299. |
| [SetSecurityDescriptorGroup](/windows/win32/api/securitybaseapi/nf-securitybaseapi-setsecuritydescriptorgroup) | Introduced into api-ms-win-security-base-l1-1-0.dll in 10.0.16299. |
| [SetSecurityDescriptorOwner](/windows/win32/api/securitybaseapi/nf-securitybaseapi-setsecuritydescriptorowner) | Introduced into api-ms-win-security-base-l1-1-0.dll in 10.0.16299. |
| [SetSecurityDescriptorRMControl](/windows/win32/api/securitybaseapi/nf-securitybaseapi-setsecuritydescriptorrmcontrol) | Introduced into api-ms-win-security-base-l1-1-0.dll in 10.0.16299. |
| [SetSecurityDescriptorSacl](/windows/win32/api/securitybaseapi/nf-securitybaseapi-setsecuritydescriptorsacl) | Introduced into api-ms-win-security-base-l1-1-0.dll in 10.0.16299. |
| [SetTokenInformation](/windows/win32/api/securitybaseapi/nf-securitybaseapi-settokeninformation) | Introduced into api-ms-win-security-base-l1-1-0.dll in 10.0.16299. |


## APIs from api-ms-win-security-sddl-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [ConvertSecurityDescriptorToStringSecurityDescriptorW](/windows/win32/api/sddl/nf-sddl-convertsecuritydescriptortostringsecuritydescriptora) | Introduced into api-ms-win-security-sddl-l1-1-0.dll in 10.0.16299. |
| [ConvertSidToStringSidW](/windows/win32/api/sddl/nf-sddl-convertsidtostringsida) | Introduced into api-ms-win-security-sddl-l1-1-0.dll in 10.0.16299. |
| [ConvertStringSecurityDescriptorToSecurityDescriptorW](/windows/win32/api/sddl/nf-sddl-convertstringsecuritydescriptortosecuritydescriptora) | Introduced into api-ms-win-security-sddl-l1-1-0.dll in 10.0.16299. |
| [ConvertStringSidToSidW](/windows/win32/api/sddl/nf-sddl-convertstringsidtosida) | Introduced into api-ms-win-security-sddl-l1-1-0.dll in 10.0.16299. |


## APIs from api-ms-win-core-synch-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [CancelWaitableTimer](/windows/win32/api/synchapi/nf-synchapi-cancelwaitabletimer) | Introduced into api-ms-win-core-synch-l1-1-0.dll in 10.0.16299. |
| [CreateWaitableTimerExW](/windows/win32/api/synchapi/nf-synchapi-createwaitabletimerexw) | Introduced into api-ms-win-core-synch-l1-1-0.dll in 10.0.16299. |
| [OpenWaitableTimerW](/windows/win32/api/synchapi/nf-synchapi-openwaitabletimerw) | Introduced into api-ms-win-core-synch-l1-1-0.dll in 10.0.16299. |
| [SetWaitableTimer](/windows/win32/api/synchapi/nf-synchapi-setwaitabletimer) | Introduced into api-ms-win-core-synch-l1-1-0.dll in 10.0.16299. |
| [SetWaitableTimerEx](/windows/win32/api/synchapi/nf-synchapi-setwaitabletimerex) | Introduced into api-ms-win-core-synch-l1-1-0.dll in 10.0.16299. |


## APIs from api-ms-win-core-sysinfo-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [GetSystemDirectoryA](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getsystemdirectorya) | Introduced into api-ms-win-core-sysinfo-l1-1-0.dll in 10.0.16299. |
| [GetSystemDirectoryW](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getsystemdirectorya) | Introduced into api-ms-win-core-sysinfo-l1-1-0.dll in 10.0.16299. |
| [GetTickCount](/windows/win32/api/sysinfoapi/nf-sysinfoapi-gettickcount) | Introduced into api-ms-win-core-sysinfo-l1-1-0.dll in 10.0.16299. |
| [GetVersionExA](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getversionexa) | Introduced into api-ms-win-core-sysinfo-l1-1-0.dll in 10.0.16299. |
| [GetVersionExW](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getversionexa) | Introduced into api-ms-win-core-sysinfo-l1-1-0.dll in 10.0.16299. |


## APIs from api-ms-win-core-comm-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [ClearCommBreak](/windows/win32/api/winbase/nf-winbase-clearcommbreak) | Introduced into api-ms-win-core-comm-l1-1-0.dll in 10.0.16299. |
| [ClearCommError](/windows/win32/api/winbase/nf-winbase-clearcommerror) | Introduced into api-ms-win-core-comm-l1-1-0.dll in 10.0.16299. |
| [EscapeCommFunction](/windows/win32/api/winbase/nf-winbase-escapecommfunction) | Introduced into api-ms-win-core-comm-l1-1-0.dll in 10.0.16299. |
| [GetCommConfig](/windows/win32/api/winbase/nf-winbase-getcommconfig) | Introduced into api-ms-win-core-comm-l1-1-0.dll in 10.0.16299. |
| [GetCommMask](/windows/win32/api/winbase/nf-winbase-getcommmask) | Introduced into api-ms-win-core-comm-l1-1-0.dll in 10.0.16299. |
| [GetCommModemStatus](/windows/win32/api/winbase/nf-winbase-getcommmodemstatus) | Introduced into api-ms-win-core-comm-l1-1-0.dll in 10.0.16299. |
| [GetCommProperties](/windows/win32/api/winbase/nf-winbase-getcommproperties) | Introduced into api-ms-win-core-comm-l1-1-0.dll in 10.0.16299. |
| [GetCommState](/windows/win32/api/winbase/nf-winbase-getcommstate) | Introduced into api-ms-win-core-comm-l1-1-0.dll in 10.0.16299. |
| [GetCommTimeouts](/windows/win32/api/winbase/nf-winbase-getcommtimeouts) | Introduced into api-ms-win-core-comm-l1-1-0.dll in 10.0.16299. |
| [PurgeComm](/windows/win32/api/winbase/nf-winbase-purgecomm) | Introduced into api-ms-win-core-comm-l1-1-0.dll in 10.0.16299. |
| [SetCommBreak](/windows/win32/api/winbase/nf-winbase-setcommbreak) | Introduced into api-ms-win-core-comm-l1-1-0.dll in 10.0.16299. |
| [SetCommConfig](/windows/win32/api/winbase/nf-winbase-setcommconfig) | Introduced into api-ms-win-core-comm-l1-1-0.dll in 10.0.16299. |
| [SetCommMask](/windows/win32/api/winbase/nf-winbase-setcommmask) | Introduced into api-ms-win-core-comm-l1-1-0.dll in 10.0.16299. |
| [SetCommState](/windows/win32/api/winbase/nf-winbase-setcommstate) | Introduced into api-ms-win-core-comm-l1-1-0.dll in 10.0.16299. |
| [SetCommTimeouts](/windows/win32/api/winbase/nf-winbase-setcommtimeouts) | Introduced into api-ms-win-core-comm-l1-1-0.dll in 10.0.16299. |
| [SetupComm](/windows/win32/api/winbase/nf-winbase-setupcomm) | Introduced into api-ms-win-core-comm-l1-1-0.dll in 10.0.16299. |
| [TransmitCommChar](/windows/win32/api/winbase/nf-winbase-transmitcommchar) | Introduced into api-ms-win-core-comm-l1-1-0.dll in 10.0.16299. |
| [WaitCommEvent](/windows/win32/api/winbase/nf-winbase-waitcommevent) | Introduced into api-ms-win-core-comm-l1-1-0.dll in 10.0.16299. |


## APIs from api-ms-win-core-console-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [GetConsoleCP](/windows/console/getconsolecp) | Introduced into api-ms-win-core-console-l1-1-0.dll in 10.0.16299. |
| [GetConsoleMode](/windows/console/getconsolemode) | Introduced into api-ms-win-core-console-l1-1-0.dll in 10.0.16299. |
| [GetConsoleOutputCP](/windows/console/getconsoleoutputcp) | Introduced into api-ms-win-core-console-l1-1-0.dll in 10.0.16299. |
| [ReadConsoleInputW](/windows/console/readconsoleinput) | Introduced into api-ms-win-core-console-l1-1-0.dll in 10.0.16299. |
| [ReadConsoleW](/windows/console/readconsole) | Introduced into api-ms-win-core-console-l1-1-0.dll in 10.0.16299. |
| [SetConsoleCtrlHandler](/windows/console/setconsolectrlhandler) | Introduced into api-ms-win-core-console-l1-1-0.dll in 10.0.16299. |
| [SetConsoleMode](/windows/console/setconsolemode) | Introduced into api-ms-win-core-console-l1-1-0.dll in 10.0.16299. |
| [WriteConsoleW](/windows/console/writeconsole) | Introduced into api-ms-win-core-console-l1-1-0.dll in 10.0.16299. |
| [AllocConsole](/windows/console/allocconsole) | Introduced into api-ms-win-core-console-l1-1-0.dll in 10.0.17134. |
| [GetNumberOfConsoleInputEvents](/windows/console/getnumberofconsoleinputevents) | Introduced into api-ms-win-core-console-l1-1-0.dll in 10.0.17134. |
| [ReadConsoleA](/windows/console/readconsole) | Introduced into api-ms-win-core-console-l1-1-0.dll in 10.0.17134. |
| [ReadConsoleInputA](/windows/console/readconsoleinput) | Introduced into api-ms-win-core-console-l1-1-0.dll in 10.0.17134. |
| [WriteConsoleA](/windows/console/writeconsole) | Introduced into api-ms-win-core-console-l1-1-0.dll in 10.0.17134. |


## APIs from api-ms-win-appmodel-runtime-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [PackageFamilyNameFromFullName](/windows/win32/api/appmodel/nf-appmodel-packagefamilynamefromfullname) | Introduced into api-ms-win-appmodel-runtime-l1-1-0.dll in 10.0.16299. |
| [PackageFamilyNameFromId](/windows/win32/api/appmodel/nf-appmodel-packagefamilynamefromid) | Introduced into api-ms-win-appmodel-runtime-l1-1-0.dll in 10.0.16299. |
| [PackageFullNameFromId](/windows/win32/api/appmodel/nf-appmodel-packagefullnamefromid) | Introduced into api-ms-win-appmodel-runtime-l1-1-0.dll in 10.0.16299. |
| [PackageIdFromFullName](/windows/win32/api/appmodel/nf-appmodel-packageidfromfullname) | Introduced into api-ms-win-appmodel-runtime-l1-1-0.dll in 10.0.16299. |
| [PackageNameAndPublisherIdFromFamilyName](/windows/win32/api/appmodel/nf-appmodel-packagenameandpublisheridfromfamilyname) | Introduced into api-ms-win-appmodel-runtime-l1-1-0.dll in 10.0.16299. |


## APIs from api-ms-win-appmodel-runtime-l1-1-1.dll

| API | Requirements |
| -----| --------------|
| [FormatApplicationUserModelId](/windows/win32/api/appmodel/nf-appmodel-formatapplicationusermodelid) | Introduced into api-ms-win-appmodel-runtime-l1-1-1.dll in 10.0.16299. |
| [ParseApplicationUserModelId](/windows/win32/api/appmodel/nf-appmodel-parseapplicationusermodelid) | Introduced into api-ms-win-appmodel-runtime-l1-1-1.dll in 10.0.16299. |
| VerifyApplicationUserModelId | Introduced into api-ms-win-appmodel-runtime-l1-1-1.dll in 10.0.16299. |
| VerifyPackageFamilyName | Introduced into api-ms-win-appmodel-runtime-l1-1-1.dll in 10.0.16299. |
| VerifyPackageFullName | Introduced into api-ms-win-appmodel-runtime-l1-1-1.dll in 10.0.16299. |
| VerifyPackageId | Introduced into api-ms-win-appmodel-runtime-l1-1-1.dll in 10.0.16299. |
| VerifyPackageRelativeApplicationId | Introduced into api-ms-win-appmodel-runtime-l1-1-1.dll in 10.0.16299. |


## APIs from api-ms-win-core-comm-l1-1-1.dll

| API | Requirements |
| -----| --------------|
| [OpenCommPort](https://msdn.microsoft.com/library/Mt829668(v=VS.85).aspx) | Introduced into api-ms-win-core-comm-l1-1-1.dll in 10.0.16299. |


## APIs from api-ms-win-core-enclave-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [CreateEnclave](/windows/win32/api/enclaveapi/nf-enclaveapi-createenclave) | Introduced into api-ms-win-core-enclave-l1-1-0.dll in 10.0.16299. |
| [InitializeEnclave](/windows/win32/api/enclaveapi/nf-enclaveapi-initializeenclave) | Introduced into api-ms-win-core-enclave-l1-1-0.dll in 10.0.16299. |
| [IsEnclaveTypeSupported](/windows/win32/api/enclaveapi/nf-enclaveapi-isenclavetypesupported) | Introduced into api-ms-win-core-enclave-l1-1-0.dll in 10.0.16299. |
| [LoadEnclaveData](/windows/win32/api/enclaveapi/nf-enclaveapi-loadenclavedata) | Introduced into api-ms-win-core-enclave-l1-1-0.dll in 10.0.16299. |


## APIs from api-ms-win-core-featurestaging-l1-1-1.dll

| API | Requirements |
| -----| --------------|
| [GetFeatureVariant](/windows/win32/api/featurestagingapi/nf-featurestagingapi-getfeaturevariant) | Introduced into api-ms-win-core-featurestaging-l1-1-1.dll in 10.0.16299. |


## APIs from api-ms-win-core-namedpipe-l1-2-2.dll

| API | Requirements |
| -----| --------------|
| [CallNamedPipeW](/windows/win32/api/winbase/nf-winbase-callnamedpipea) | Introduced into api-ms-win-core-namedpipe-l1-2-2.dll in 10.0.16299. |


## APIs from api-ms-win-core-namespace-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [AddSIDToBoundaryDescriptor](/windows/win32/api/namespaceapi/nf-namespaceapi-addsidtoboundarydescriptor) | Introduced into api-ms-win-core-namespace-l1-1-0.dll in 10.0.16299. |
| [ClosePrivateNamespace](/windows/win32/api/namespaceapi/nf-namespaceapi-closeprivatenamespace) | Introduced into api-ms-win-core-namespace-l1-1-0.dll in 10.0.16299. |
| [CreateBoundaryDescriptorW](/windows/win32/api/winbase/nf-winbase-createboundarydescriptora) | Introduced into api-ms-win-core-namespace-l1-1-0.dll in 10.0.16299. |
| [CreatePrivateNamespaceW](/windows/win32/api/winbase/nf-winbase-createprivatenamespacea) | Introduced into api-ms-win-core-namespace-l1-1-0.dll in 10.0.16299. |
| [DeleteBoundaryDescriptor](/windows/win32/api/namespaceapi/nf-namespaceapi-deleteboundarydescriptor) | Introduced into api-ms-win-core-namespace-l1-1-0.dll in 10.0.16299. |
| [OpenPrivateNamespaceW](/windows/win32/api/winbase/nf-winbase-openprivatenamespacea) | Introduced into api-ms-win-core-namespace-l1-1-0.dll in 10.0.16299. |


## APIs from api-ms-win-core-path-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [PathAllocCanonicalize](/windows/win32/api/pathcch/nf-pathcch-pathalloccanonicalize) | Introduced into api-ms-win-core-path-l1-1-0.dll in 10.0.16299. |
| [PathAllocCombine](/windows/win32/api/pathcch/nf-pathcch-pathalloccombine) | Introduced into api-ms-win-core-path-l1-1-0.dll in 10.0.16299. |
| [PathCchAddBackslash](/windows/win32/api/pathcch/nf-pathcch-pathcchaddbackslash) | Introduced into api-ms-win-core-path-l1-1-0.dll in 10.0.16299. |
| [PathCchAddBackslashEx](/windows/win32/api/pathcch/nf-pathcch-pathcchaddbackslashex) | Introduced into api-ms-win-core-path-l1-1-0.dll in 10.0.16299. |
| [PathCchAddExtension](/windows/win32/api/pathcch/nf-pathcch-pathcchaddextension) | Introduced into api-ms-win-core-path-l1-1-0.dll in 10.0.16299. |
| [PathCchAppend](/windows/win32/api/pathcch/nf-pathcch-pathcchappend) | Introduced into api-ms-win-core-path-l1-1-0.dll in 10.0.16299. |
| [PathCchAppendEx](/windows/win32/api/pathcch/nf-pathcch-pathcchappendex) | Introduced into api-ms-win-core-path-l1-1-0.dll in 10.0.16299. |
| [PathCchCanonicalize](/windows/win32/api/pathcch/nf-pathcch-pathcchcanonicalize) | Introduced into api-ms-win-core-path-l1-1-0.dll in 10.0.16299. |
| [PathCchCanonicalizeEx](/windows/win32/api/pathcch/nf-pathcch-pathcchcanonicalizeex) | Introduced into api-ms-win-core-path-l1-1-0.dll in 10.0.16299. |
| [PathCchCombine](/windows/win32/api/pathcch/nf-pathcch-pathcchcombine) | Introduced into api-ms-win-core-path-l1-1-0.dll in 10.0.16299. |
| [PathCchCombineEx](/windows/win32/api/pathcch/nf-pathcch-pathcchcombineex) | Introduced into api-ms-win-core-path-l1-1-0.dll in 10.0.16299. |
| [PathCchFindExtension](/windows/win32/api/pathcch/nf-pathcch-pathcchfindextension) | Introduced into api-ms-win-core-path-l1-1-0.dll in 10.0.16299. |
| [PathCchIsRoot](/windows/win32/api/pathcch/nf-pathcch-pathcchisroot) | Introduced into api-ms-win-core-path-l1-1-0.dll in 10.0.16299. |
| [PathCchRemoveBackslash](/windows/win32/api/pathcch/nf-pathcch-pathcchremovebackslash) | Introduced into api-ms-win-core-path-l1-1-0.dll in 10.0.16299. |
| [PathCchRemoveBackslashEx](/windows/win32/api/pathcch/nf-pathcch-pathcchremovebackslashex) | Introduced into api-ms-win-core-path-l1-1-0.dll in 10.0.16299. |
| [PathCchRemoveExtension](/windows/win32/api/pathcch/nf-pathcch-pathcchremoveextension) | Introduced into api-ms-win-core-path-l1-1-0.dll in 10.0.16299. |
| [PathCchRemoveFileSpec](/windows/win32/api/pathcch/nf-pathcch-pathcchremovefilespec) | Introduced into api-ms-win-core-path-l1-1-0.dll in 10.0.16299. |
| [PathCchRenameExtension](/windows/win32/api/pathcch/nf-pathcch-pathcchrenameextension) | Introduced into api-ms-win-core-path-l1-1-0.dll in 10.0.16299. |
| [PathCchSkipRoot](/windows/win32/api/pathcch/nf-pathcch-pathcchskiproot) | Introduced into api-ms-win-core-path-l1-1-0.dll in 10.0.16299. |
| [PathCchStripPrefix](/windows/win32/api/pathcch/nf-pathcch-pathcchstripprefix) | Introduced into api-ms-win-core-path-l1-1-0.dll in 10.0.16299. |
| [PathCchStripToRoot](/windows/win32/api/pathcch/nf-pathcch-pathcchstriptoroot) | Introduced into api-ms-win-core-path-l1-1-0.dll in 10.0.16299. |
| [PathIsUNCEx](/windows/win32/api/pathcch/nf-pathcch-pathisuncex) | Introduced into api-ms-win-core-path-l1-1-0.dll in 10.0.16299. |


## APIs from api-ms-win-core-psm-appnotify-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [RegisterAppStateChangeNotification](/windows/win32/api/appnotify/nf-appnotify-registerappstatechangenotification) | Introduced into api-ms-win-core-psm-appnotify-l1-1-0.dll in 10.0.16299. |
| [UnregisterAppStateChangeNotification](/windows/win32/api/appnotify/nf-appnotify-unregisterappstatechangenotification) | Introduced into api-ms-win-core-psm-appnotify-l1-1-0.dll in 10.0.16299. |


## APIs from api-ms-win-core-realtime-l1-1-2.dll

| API | Requirements |
| -----| --------------|
| [ConvertAuxiliaryCounterToPerformanceCounter](/windows/win32/api/realtimeapiset/nf-realtimeapiset-convertauxiliarycountertoperformancecounter) | Introduced into api-ms-win-core-realtime-l1-1-2.dll in 10.0.16299. |
| [ConvertPerformanceCounterToAuxiliaryCounter](/windows/win32/api/realtimeapiset/nf-realtimeapiset-convertperformancecountertoauxiliarycounter) | Introduced into api-ms-win-core-realtime-l1-1-2.dll in 10.0.16299. |
| [QueryAuxiliaryCounterFrequency](/windows/win32/api/realtimeapiset/nf-realtimeapiset-queryauxiliarycounterfrequency) | Introduced into api-ms-win-core-realtime-l1-1-2.dll in 10.0.16299. |


## APIs from api-ms-win-gaming-tcui-l1-1-3.dll

| API | Requirements |
| -----| --------------|
| ShowGameInviteUIWithContext | Introduced into api-ms-win-gaming-tcui-l1-1-3.dll in 10.0.16299. |
| ShowGameInviteUIWithContextForUser | Introduced into api-ms-win-gaming-tcui-l1-1-3.dll in 10.0.16299. |


## APIs from api-ms-win-gaming-tcui-l1-1-4.dll

| API | Requirements |
| -----| --------------|
| ShowCustomizeUserProfileUI | Introduced into api-ms-win-gaming-tcui-l1-1-4.dll in 10.0.16299. |
| ShowCustomizeUserProfileUIForUser | Introduced into api-ms-win-gaming-tcui-l1-1-4.dll in 10.0.16299. |
| ShowFindFriendsUI | Introduced into api-ms-win-gaming-tcui-l1-1-4.dll in 10.0.16299. |
| ShowFindFriendsUIForUser | Introduced into api-ms-win-gaming-tcui-l1-1-4.dll in 10.0.16299. |
| ShowGameInfoUI | Introduced into api-ms-win-gaming-tcui-l1-1-4.dll in 10.0.16299. |
| ShowGameInfoUIForUser | Introduced into api-ms-win-gaming-tcui-l1-1-4.dll in 10.0.16299. |
| ShowUserSettingsUI | Introduced into api-ms-win-gaming-tcui-l1-1-4.dll in 10.0.16299. |
| ShowUserSettingsUIForUser | Introduced into api-ms-win-gaming-tcui-l1-1-4.dll in 10.0.16299. |


## APIs from api-ms-win-gaming-deviceinformation-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [GetGamingDeviceModelInformation](/windows/win32/api/gamingdeviceinformation/nf-gamingdeviceinformation-getgamingdevicemodelinformation) | Introduced into api-ms-win-gaming-deviceinformation-l1-1-0.dll in 10.0.16299. |


## APIs from api-ms-win-gaming-expandedresources-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [GetExpandedResourceExclusiveCpuCount](/windows/win32/api/expandedresources/nf-expandedresources-getexpandedresourceexclusivecpucount) | Introduced into api-ms-win-gaming-expandedresources-l1-1-0.dll in 10.0.16299. |
| [HasExpandedResources](/windows/win32/api/expandedresources/nf-expandedresources-hasexpandedresources) | Introduced into api-ms-win-gaming-expandedresources-l1-1-0.dll in 10.0.16299. |
| [ReleaseExclusiveCpuSets](/windows/win32/api/expandedresources/nf-expandedresources-releaseexclusivecpusets) | Introduced into api-ms-win-gaming-expandedresources-l1-1-0.dll in 10.0.16299. |


## APIs from api-ms-win-gaming-gamemonitor-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [EnableActiveGameMonitoring](/previous-versions/visualstudio/) | Introduced into api-ms-win-gaming-gamemonitor-l1-1-0.dll in 10.0.16299. Removed in 10.0.17763. |
| [ReportGameActivity](/previous-versions/visualstudio/) | Introduced into api-ms-win-gaming-gamemonitor-l1-1-0.dll in 10.0.16299. Removed in 10.0.17763. |
| [SetGameActivityCorrelationId](/previous-versions//mt808784(v=vs.85)) | Introduced into api-ms-win-gaming-gamemonitor-l1-1-0.dll in 10.0.16299. Removed in 10.0.17763. |


## APIs from api-ms-win-gaming-gamemonitor-l1-1-1.dll

| API | Requirements |
| -----| --------------|
| [GetGameMonitoringPermissionState](/previous-versions//mt823413(v=vs.85)) | Introduced into api-ms-win-gaming-gamemonitor-l1-1-1.dll in 10.0.16299. Removed in 10.0.17763. |


## APIs from api-ms-win-security-base-l1-2-0.dll

| API | Requirements |
| -----| --------------|
| [CheckTokenMembershipEx](/windows/win32/api/securitybaseapi/nf-securitybaseapi-checktokenmembershipex) | Introduced into api-ms-win-security-base-l1-2-0.dll in 10.0.16299. |


## APIs from api-ms-win-security-isolatedcontainer-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| IsProcessInIsolatedContainer | Introduced into api-ms-win-security-isolatedcontainer-l1-1-0.dll in 10.0.16299. |


## APIs from bcrypt.dll

| API | Requirements |
| -----| --------------|
| [BCryptGetFipsAlgorithmMode](/windows/win32/api/bcrypt/nf-bcrypt-bcryptgetfipsalgorithmmode) | Introduced into bcrypt.dll in 10.0.16299. |


## APIs from api-ms-win-core-memory-l1-1-6.dll

| API | Requirements |
| -----| --------------|
| MapViewOfFile3FromApp | Introduced into api-ms-win-core-memory-l1-1-6.dll in 10.0.17134. |
| VirtualAlloc2FromApp | Introduced into api-ms-win-core-memory-l1-1-6.dll in 10.0.17134. |


## APIs from api-ms-win-core-memory-l1-1-5.dll

| API | Requirements |
| -----| --------------|
| [UnmapViewOfFile2](/windows/win32/api/memoryapi/nf-memoryapi-unmapviewoffile2) | Introduced into api-ms-win-core-memory-l1-1-5.dll in 10.0.17134. |
| VirtualUnlockEx | Introduced into api-ms-win-core-memory-l1-1-5.dll in 10.0.17134. |


## APIs from api-ms-win-core-console-l2-2-0.dll

| API | Requirements |
| -----| --------------|
| [GetConsoleOriginalTitleA](/windows/console/getconsoleoriginaltitle) | Introduced into api-ms-win-core-console-l2-2-0.dll in 10.0.17134. |
| [GetConsoleOriginalTitleW](/windows/console/getconsoleoriginaltitle) | Introduced into api-ms-win-core-console-l2-2-0.dll in 10.0.17134. |
| [GetConsoleTitleA](/windows/console/getconsoletitle) | Introduced into api-ms-win-core-console-l2-2-0.dll in 10.0.17134. |
| [SetConsoleTitleA](/windows/console/setconsoletitle) | Introduced into api-ms-win-core-console-l2-2-0.dll in 10.0.17134. |


## APIs from api-ms-win-core-console-l3-2-0.dll

| API | Requirements |
| -----| --------------|
| [AddConsoleAliasA](/windows/console/addconsolealias) | Introduced into api-ms-win-core-console-l3-2-0.dll in 10.0.17134. |
| [AddConsoleAliasW](/windows/console/addconsolealias) | Introduced into api-ms-win-core-console-l3-2-0.dll in 10.0.17134. |
| ExpungeConsoleCommandHistoryA | Introduced into api-ms-win-core-console-l3-2-0.dll in 10.0.17134. |
| ExpungeConsoleCommandHistoryW | Introduced into api-ms-win-core-console-l3-2-0.dll in 10.0.17134. |
| [GetConsoleAliasA](/windows/console/getconsolealias) | Introduced into api-ms-win-core-console-l3-2-0.dll in 10.0.17134. |
| [GetConsoleAliasExesA](/windows/console/getconsolealiasexes) | Introduced into api-ms-win-core-console-l3-2-0.dll in 10.0.17134. |
| [GetConsoleAliasExesLengthA](/windows/console/getconsolealiasexeslength) | Introduced into api-ms-win-core-console-l3-2-0.dll in 10.0.17134. |
| [GetConsoleAliasExesLengthW](/windows/console/getconsolealiasexeslength) | Introduced into api-ms-win-core-console-l3-2-0.dll in 10.0.17134. |
| [GetConsoleAliasExesW](/windows/console/getconsolealiasexes) | Introduced into api-ms-win-core-console-l3-2-0.dll in 10.0.17134. |
| [GetConsoleAliasW](/windows/console/getconsolealias) | Introduced into api-ms-win-core-console-l3-2-0.dll in 10.0.17134. |
| [GetConsoleAliasesA](/windows/console/getconsolealiases) | Introduced into api-ms-win-core-console-l3-2-0.dll in 10.0.17134. |
| [GetConsoleAliasesLengthA](/windows/console/getconsolealiaseslength) | Introduced into api-ms-win-core-console-l3-2-0.dll in 10.0.17134. |
| [GetConsoleAliasesLengthW](/windows/console/getconsolealiaseslength) | Introduced into api-ms-win-core-console-l3-2-0.dll in 10.0.17134. |
| [GetConsoleAliasesW](/windows/console/getconsolealiases) | Introduced into api-ms-win-core-console-l3-2-0.dll in 10.0.17134. |
| GetConsoleCommandHistoryA | Introduced into api-ms-win-core-console-l3-2-0.dll in 10.0.17134. |
| GetConsoleCommandHistoryLengthA | Introduced into api-ms-win-core-console-l3-2-0.dll in 10.0.17134. |
| GetConsoleCommandHistoryLengthW | Introduced into api-ms-win-core-console-l3-2-0.dll in 10.0.17134. |
| GetConsoleCommandHistoryW | Introduced into api-ms-win-core-console-l3-2-0.dll in 10.0.17134. |
| [GetConsoleDisplayMode](/windows/console/getconsoledisplaymode) | Introduced into api-ms-win-core-console-l3-2-0.dll in 10.0.17134. |
| [GetConsoleFontSize](/windows/console/getconsolefontsize) | Introduced into api-ms-win-core-console-l3-2-0.dll in 10.0.17134. |
| [GetConsoleHistoryInfo](/windows/console/getconsolehistoryinfo) | Introduced into api-ms-win-core-console-l3-2-0.dll in 10.0.17134. |
| [GetConsoleProcessList](/windows/console/getconsoleprocesslist) | Introduced into api-ms-win-core-console-l3-2-0.dll in 10.0.17134. |
| [GetConsoleSelectionInfo](/windows/console/getconsoleselectioninfo) | Introduced into api-ms-win-core-console-l3-2-0.dll in 10.0.17134. |
| [GetConsoleWindow](/windows/console/getconsolewindow) | Introduced into api-ms-win-core-console-l3-2-0.dll in 10.0.17134. |
| [GetCurrentConsoleFont](/windows/console/getcurrentconsolefont) | Introduced into api-ms-win-core-console-l3-2-0.dll in 10.0.17134. |
| [GetCurrentConsoleFontEx](/windows/console/getcurrentconsolefontex) | Introduced into api-ms-win-core-console-l3-2-0.dll in 10.0.17134. |
| [GetNumberOfConsoleMouseButtons](/windows/console/getnumberofconsolemousebuttons) | Introduced into api-ms-win-core-console-l3-2-0.dll in 10.0.17134. |
| [SetConsoleDisplayMode](/windows/console/setconsoledisplaymode) | Introduced into api-ms-win-core-console-l3-2-0.dll in 10.0.17134. |
| [SetConsoleHistoryInfo](/windows/console/setconsolehistoryinfo) | Introduced into api-ms-win-core-console-l3-2-0.dll in 10.0.17134. |
| SetConsoleNumberOfCommandsA | Introduced into api-ms-win-core-console-l3-2-0.dll in 10.0.17134. |
| SetConsoleNumberOfCommandsW | Introduced into api-ms-win-core-console-l3-2-0.dll in 10.0.17134. |
| [SetCurrentConsoleFontEx](/windows/console/setcurrentconsolefontex) | Introduced into api-ms-win-core-console-l3-2-0.dll in 10.0.17134. |


## APIs from api-ms-win-core-memory-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [VirtualFreeEx](/windows/win32/api/memoryapi/nf-memoryapi-virtualfreeex) | Introduced into api-ms-win-core-memory-l1-1-0.dll in 10.0.17134. |


## APIs from api-ms-win-core-sysinfo-l1-2-0.dll

| API | Requirements |
| -----| --------------|
| [EnumSystemFirmwareTables](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-_dxgk_firmware_table_interface) | Introduced into api-ms-win-core-sysinfo-l1-2-0.dll in 10.0.17134. |
| [GetSystemFirmwareTable](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getsystemfirmwaretable) | Introduced into api-ms-win-core-sysinfo-l1-2-0.dll in 10.0.17134. |
| [GetProductInfo](/windows/win32/api/sysinfoapi/nf-sysinfoapi-getproductinfo) | Introduced into api-ms-win-core-sysinfo-l1-2-0.dll in 10.0.17763. |


## APIs from api-ms-win-core-console-l1-2-0.dll

| API | Requirements |
| -----| --------------|
| [AttachConsole](/windows/console/attachconsole) | Introduced into api-ms-win-core-console-l1-2-0.dll in 10.0.17134. |
| [FreeConsole](/windows/console/freeconsole) | Introduced into api-ms-win-core-console-l1-2-0.dll in 10.0.17134. |
| [PeekConsoleInputA](/windows/console/peekconsoleinput) | Introduced into api-ms-win-core-console-l1-2-0.dll in 10.0.17134. |


## APIs from api-ms-win-core-debug-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [DebugBreak](/windows/win32/api/debugapi/nf-debugapi-debugbreak) | Introduced into api-ms-win-core-debug-l1-1-0.dll in 10.0.17134. |


## APIs from api-ms-win-core-wow64-l1-1-1.dll

| API | Requirements |
| -----| --------------|
| [IsWow64Process2](/windows/win32/api/wow64apiset/nf-wow64apiset-iswow64process2) | Introduced into api-ms-win-core-wow64-l1-1-1.dll in 10.0.17134. |


## APIs from api-ms-win-core-comm-l1-1-2.dll

| API | Requirements |
| -----| --------------|
| [GetCommPorts](https://msdn.microsoft.com/library/Mt829680(v=VS.85).aspx) | Introduced into api-ms-win-core-comm-l1-1-2.dll in 10.0.17134. |


## APIs from api-ms-win-core-file-fromapp-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [CopyFileFromAppW](/previous-versions/windows/desktop/legacy/mt846582(v=vs.85)) | Introduced into api-ms-win-core-file-fromapp-l1-1-0.dll in 10.0.17134. |
| [CreateDirectoryFromAppW](/previous-versions/windows/desktop/legacy/mt846583(v=vs.85)) | Introduced into api-ms-win-core-file-fromapp-l1-1-0.dll in 10.0.17134. |
| [CreateFile2FromAppW](/previous-versions/windows/desktop/legacy/mt846584(v=vs.85)) | Introduced into api-ms-win-core-file-fromapp-l1-1-0.dll in 10.0.17134. |
| [CreateFileFromAppW](/previous-versions/windows/desktop/legacy/mt846585(v=vs.85)) | Introduced into api-ms-win-core-file-fromapp-l1-1-0.dll in 10.0.17134. |
| [DeleteFileFromAppW](/previous-versions/windows/desktop/legacy/mt846586(v=vs.85)) | Introduced into api-ms-win-core-file-fromapp-l1-1-0.dll in 10.0.17134. |
| [FindFirstFileExFromAppW](/previous-versions/windows/desktop/legacy/mt846625(v=vs.85)) | Introduced into api-ms-win-core-file-fromapp-l1-1-0.dll in 10.0.17134. |
| GetFileAttributesExFromAppW | Introduced into api-ms-win-core-file-fromapp-l1-1-0.dll in 10.0.17134. |
| [MoveFileFromAppW](/previous-versions/windows/desktop/legacy/mt846627(v=vs.85)) | Introduced into api-ms-win-core-file-fromapp-l1-1-0.dll in 10.0.17134. |
| [RemoveDirectoryFromAppW](/previous-versions/windows/desktop/legacy/mt846628(v=vs.85)) | Introduced into api-ms-win-core-file-fromapp-l1-1-0.dll in 10.0.17134. |
| [ReplaceFileFromAppW](/previous-versions/windows/desktop/legacy/mt846629(v=vs.85)) | Introduced into api-ms-win-core-file-fromapp-l1-1-0.dll in 10.0.17134. |
| [SetFileAttributesFromAppW](/previous-versions/windows/desktop/legacy/mt846630(v=vs.85)) | Introduced into api-ms-win-core-file-fromapp-l1-1-0.dll in 10.0.17134. |


## APIs from api-ms-win-core-firmware-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [GetFirmwareEnvironmentVariableA](/windows/win32/api/winbase/nf-winbase-getfirmwareenvironmentvariablea) | Introduced into api-ms-win-core-firmware-l1-1-0.dll in 10.0.17134. |
| [GetFirmwareEnvironmentVariableExA](/windows/win32/api/winbase/nf-winbase-getfirmwareenvironmentvariableexa) | Introduced into api-ms-win-core-firmware-l1-1-0.dll in 10.0.17134. |
| [GetFirmwareEnvironmentVariableExW](/windows/win32/api/winbase/nf-winbase-getfirmwareenvironmentvariableexa) | Introduced into api-ms-win-core-firmware-l1-1-0.dll in 10.0.17134. |
| [GetFirmwareEnvironmentVariableW](/windows/win32/api/winbase/nf-winbase-getfirmwareenvironmentvariablea) | Introduced into api-ms-win-core-firmware-l1-1-0.dll in 10.0.17134. |
| [SetFirmwareEnvironmentVariableA](/windows/win32/api/winbase/nf-winbase-setfirmwareenvironmentvariablea) | Introduced into api-ms-win-core-firmware-l1-1-0.dll in 10.0.17134. |
| [SetFirmwareEnvironmentVariableExA](/windows/win32/api/winbase/nf-winbase-setfirmwareenvironmentvariableexa) | Introduced into api-ms-win-core-firmware-l1-1-0.dll in 10.0.17134. |
| [SetFirmwareEnvironmentVariableExW](/windows/win32/api/winbase/nf-winbase-setfirmwareenvironmentvariableexa) | Introduced into api-ms-win-core-firmware-l1-1-0.dll in 10.0.17134. |
| [SetFirmwareEnvironmentVariableW](/windows/win32/api/winbase/nf-winbase-setfirmwareenvironmentvariablea) | Introduced into api-ms-win-core-firmware-l1-1-0.dll in 10.0.17134. |


## APIs from api-ms-win-shcore-obsolete-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [CommandLineToArgvW](/windows/win32/api/shellapi/nf-shellapi-commandlinetoargvw) | Introduced into api-ms-win-shcore-obsolete-l1-1-0.dll in 10.0.17134. |


## APIs from windows.ai.machinelearning.dll

| API | Requirements |
| -----| --------------|
| MLCreateOperatorRegistry | Introduced into windows.ai.machinelearning.dll in 10.0.17763. |


## APIs from api-ms-win-ro-typeresolution-l1-1-1.dll

| API | Requirements |
| -----| --------------|
| [RoIsApiContractPresent](/windows/win32/api/rometadataresolution/nf-rometadataresolution-roisapicontractpresent) | Introduced into api-ms-win-ro-typeresolution-l1-1-1.dll in 10.0.17763. |
| [RoIsApiContractMajorVersionPresent](/windows/win32/api/rometadataresolution/nf-rometadataresolution-roisapicontractmajorversionpresent) | Introduced into api-ms-win-ro-typeresolution-l1-1-1.dll in 10.0.17763. |


## APIs from api-ms-win-core-memory-l1-1-7.dll

| API | Requirements |
| -----| --------------|
| SetProcessValidCallTargetsForMappedView | Introduced into api-ms-win-core-memory-l1-1-7.dll in 10.0.17763. |


## APIs from mscms.dll

| API | Requirements |
| -----| --------------|
| [InstallColorProfileA](/previous-versions/windows/desktop/wcs/installcolorprofile) | Introduced into mscms.dll in 10.0.17763. |
| [InstallColorProfileW](/previous-versions/windows/desktop/wcs/installcolorprofile) | Introduced into mscms.dll in 10.0.17763. |
| ColorAdapterGetSystemModifyWhitePointCaps | Introduced into mscms.dll in 10.0.17763. |
| ColorAdapterGetDisplayCurrentStateID | Introduced into mscms.dll in 10.0.17763. |
| ColorAdapterGetDisplayTransformData | Introduced into mscms.dll in 10.0.17763. |
| ColorAdapterGetDisplayTargetWhitePoint | Introduced into mscms.dll in 10.0.17763. |
| ColorAdapterGetDisplayProfile | Introduced into mscms.dll in 10.0.17763. |
| ColorAdapterGetCurrentProfileCalibration | Introduced into mscms.dll in 10.0.17763. |
| ColorAdapterRegisterOEMColorService | Introduced into mscms.dll in 10.0.17763. |
| ColorAdapterUnregisterOEMColorService | Introduced into mscms.dll in 10.0.17763. |
| ColorProfileAddDisplayAssociation | Introduced into mscms.dll in 10.0.17763. |
| ColorProfileRemoveDisplayAssociation | Introduced into mscms.dll in 10.0.17763. |
| ColorProfileSetDisplayDefaultAssociation | Introduced into mscms.dll in 10.0.17763. |
| ColorProfileGetDisplayList | Introduced into mscms.dll in 10.0.17763. |
| ColorProfileGetDisplayDefault | Introduced into mscms.dll in 10.0.17763. |
| ColorProfileGetDisplayUserScope | Introduced into mscms.dll in 10.0.17763. |


## APIs from api-ms-win-core-com-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [CoDecrementMTAUsage](/windows/win32/api/combaseapi/nf-combaseapi-codecrementmtausage) | Introduced into api-ms-win-core-com-l1-1-0.dll in 10.0.17763. |
| [CoIncrementMTAUsage](/windows/win32/api/combaseapi/nf-combaseapi-coincrementmtausage) | Introduced into api-ms-win-core-com-l1-1-0.dll in 10.0.17763. |


## APIs from api-ms-win-devices-config-l1-1-1.dll

| API | Requirements |
| -----| --------------|
| [CM_Get_Device_Interface_ListW](/previous-versions//aa363183(v=vs.85)) | Introduced into api-ms-win-devices-config-l1-1-1.dll in 10.0.17763. |
| [CM_Get_Device_Interface_List_SizeW](/previous-versions//aa363184(v=vs.85)) | Introduced into api-ms-win-devices-config-l1-1-1.dll in 10.0.17763. |
| [CM_MapCrToWin32Err](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_mapcrtowin32err) | Introduced into api-ms-win-devices-config-l1-1-1.dll in 10.0.17763. |
| [CM_Register_Notification](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_register_notification) | Introduced into api-ms-win-devices-config-l1-1-1.dll in 10.0.17763. |
| [CM_Unregister_Notification](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_unregister_notification) | Introduced into api-ms-win-devices-config-l1-1-1.dll in 10.0.17763. |


## APIs from api-ms-win-devices-config-l1-1-2.dll

| API | Requirements |
| -----| --------------|
| [CM_Get_Device_Interface_ListA](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_device_interface_lista) | Introduced into api-ms-win-devices-config-l1-1-2.dll in 10.0.17763. |
| [CM_Get_Device_Interface_List_SizeA](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_device_interface_list_sizea) | Introduced into api-ms-win-devices-config-l1-1-2.dll in 10.0.17763. |


## APIs from api-ms-win-core-io-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [DeviceIoControl](/windows/win32/api/ioapiset/nf-ioapiset-deviceiocontrol) | Introduced into api-ms-win-core-io-l1-1-0.dll in 10.0.17763. |


## APIs from api-ms-win-core-timezone-l1-1-1.dll

| API | Requirements |
| -----| --------------|
| LocalFileTimeToLocalSystemTime | Introduced into api-ms-win-core-timezone-l1-1-1.dll in 10.0.17763. |
| LocalSystemTimeToLocalFileTime | Introduced into api-ms-win-core-timezone-l1-1-1.dll in 10.0.17763. |