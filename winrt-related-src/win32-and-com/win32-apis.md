---
author: msatranjr
description: This topic lists the Win32 APIs that are part of the Universal Windows Platform (UWP) and that are implemented by all Windows 10 devices.
title: APIs present on all Windows 10 devices (grouped by module)
ms.author: misatran
ms.topic: article
ms.prod: windows
ms.technology: uwp
keywords: windows 10, uwp, win32, COM
ms.date: 04/05/2017
ms.assetid: 9763fa67-0f32-4128-b901-013b1d7ea73c
---

# APIs present on all Windows 10 devices
This topic lists the Win32 APIs that are part of the Universal Windows Platform (UWP) and that are implemented by all Windows 10 devices. For convenience, an umbrella library named WindowsApp.lib is provided in the Microsoft Windows Software Development Kit (SDK), which provides the exports for this set of Win32 APIs. Link your app with WindowsApp.lib (and no other libraries) to access these APIs.

This topic lists all the APIs in WindowsApp.lib, grouped by module (where the module is either an [API set](https://msdn.microsoft.com/en-us/library/windows/apps/mt683763.aspx#api_sets) or a dll). Linking to WindowsApp.lib will add to your app dependencies on dlls that are present on all Windows 10 devices. For delay load, use the module name. Note that an umbrella lib can contain some, but not necessarily all, APIs from a given module.


## <span id="_api-ms-win-core-com-l1-1-1.dll"></span><span id="_API-MS-WIN-CORE-COM-L1-1-1.DLL"></span>APIs from the API Set api-ms-win-core-com-l1-1-1.dll


| API                                                                                    | Requirements                                                           |
|----------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| [**CLSIDFromString**](https://msdn.microsoft.com/en-us/library/windows/apps/ms680589.aspx)                                             | Introduced into api-ms-win-core-com-l1-1-1.dll in Windows 10.0.10240.0 |
| [**CoCreateFreeThreadedMarshaler**](https://msdn.microsoft.com/en-us/library/windows/apps/ms694500.aspx)                 | Introduced into api-ms-win-core-com-l1-1-1.dll in Windows 10.0.10240.0 |
| [**CoCreateGuid**](https://msdn.microsoft.com/en-us/library/windows/apps/ms688568.aspx)                                                   | Introduced into api-ms-win-core-com-l1-1-1.dll in Windows 10.0.10240.0 |
| [**CoCreateInstanceFromApp**](https://msdn.microsoft.com/en-us/library/windows/apps/hh404137.aspx)                             | Introduced into api-ms-win-core-com-l1-1-1.dll in Windows 10.0.10240.0 |
| [**CoDisconnectObject**](https://msdn.microsoft.com/en-us/library/windows/apps/ms680756.aspx)                                       | Introduced into api-ms-win-core-com-l1-1-1.dll in Windows 10.0.10240.0 |
| [**CoFreeUnusedLibraries**](https://msdn.microsoft.com/en-us/library/windows/apps/ms679712.aspx)                                 | Introduced into api-ms-win-core-com-l1-1-1.dll in Windows 10.0.10240.0 |
| [**CoFreeUnusedLibrariesEx**](https://msdn.microsoft.com/en-us/library/windows/apps/ms678413.aspx)                             | Introduced into api-ms-win-core-com-l1-1-1.dll in Windows 10.0.10240.0 |
| [**CoGetApartmentType**](https://msdn.microsoft.com/en-us/library/windows/apps/dd542641.aspx)                                       | Introduced into api-ms-win-core-com-l1-1-1.dll in Windows 10.0.10240.0 |
| [**CoGetContextToken**](https://msdn.microsoft.com/en-us/library/windows/apps/ms679665.aspx)                                         | Introduced into api-ms-win-core-com-l1-1-1.dll in Windows 10.0.10240.0 |
| [**CoGetCurrentLogicalThreadId**](https://msdn.microsoft.com/en-us/library/windows/apps/ms693805.aspx)                     | Introduced into api-ms-win-core-com-l1-1-1.dll in Windows 10.0.10240.0 |
| [**CoGetInterfaceAndReleaseStream**](https://msdn.microsoft.com/en-us/library/windows/apps/ms691421.aspx)               | Introduced into api-ms-win-core-com-l1-1-1.dll in Windows 10.0.10240.0 |
| [**CoGetMarshalSizeMax**](https://msdn.microsoft.com/en-us/library/windows/apps/ms692640.aspx)                                     | Introduced into api-ms-win-core-com-l1-1-1.dll in Windows 10.0.10240.0 |
| [**CoGetObjectContext**](https://msdn.microsoft.com/en-us/library/windows/apps/ms690084.aspx)                                       | Introduced into api-ms-win-core-com-l1-1-1.dll in Windows 10.0.10240.0 |
| [**CoGetStandardMarshal**](https://msdn.microsoft.com/en-us/library/windows/apps/ms678527.aspx)                                   | Introduced into api-ms-win-core-com-l1-1-1.dll in Windows 10.0.10240.0 |
| [**CoInitializeEx**](https://msdn.microsoft.com/en-us/library/windows/apps/ms695279.aspx)                                               | Introduced into api-ms-win-core-com-l1-1-1.dll in Windows 10.0.10240.0 |
| [**CoInitializeSecurity**](https://msdn.microsoft.com/en-us/library/windows/apps/ms693736.aspx)                                   | Introduced into api-ms-win-core-com-l1-1-1.dll in Windows 10.0.10240.0 |
| [**CoMarshalInterface**](https://msdn.microsoft.com/en-us/library/windows/apps/ms678428.aspx)                                       | Introduced into api-ms-win-core-com-l1-1-1.dll in Windows 10.0.10240.0 |
| [**CoMarshalInterThreadInterfaceInStream**](https://msdn.microsoft.com/en-us/library/windows/apps/ms693316.aspx) | Introduced into api-ms-win-core-com-l1-1-1.dll in Windows 10.0.10240.0 |
| [**CoRegisterClassObject**](https://msdn.microsoft.com/en-us/library/windows/apps/ms693407.aspx)                                 | Introduced into api-ms-win-core-com-l1-1-1.dll in Windows 10.0.10240.0 |
| [**CoReleaseMarshalData**](https://msdn.microsoft.com/en-us/library/windows/apps/ms690490.aspx)                                   | Introduced into api-ms-win-core-com-l1-1-1.dll in Windows 10.0.10240.0 |
| [**CoResumeClassObjects**](https://msdn.microsoft.com/en-us/library/windows/apps/ms692686.aspx)                                   | Introduced into api-ms-win-core-com-l1-1-1.dll in Windows 10.0.10240.0 |
| [**CoRevokeClassObject**](https://msdn.microsoft.com/en-us/library/windows/apps/ms688650.aspx)                                     | Introduced into api-ms-win-core-com-l1-1-1.dll in Windows 10.0.10240.0 |
| [**CoSuspendClassObjects**](https://msdn.microsoft.com/en-us/library/windows/apps/ms691208.aspx)                                 | Introduced into api-ms-win-core-com-l1-1-1.dll in Windows 10.0.10240.0 |
| [**CoSwitchCallContext**](https://msdn.microsoft.com/en-us/library/windows/apps/ms679683.aspx)                                     | Introduced into api-ms-win-core-com-l1-1-1.dll in Windows 10.0.10240.0 |
| [**CoTaskMemAlloc**](https://msdn.microsoft.com/en-us/library/windows/apps/ms692727.aspx)                                               | Introduced into api-ms-win-core-com-l1-1-1.dll in Windows 10.0.10240.0 |
| [**CoTaskMemFree**](https://msdn.microsoft.com/en-us/library/windows/apps/ms680722.aspx)                                                 | Introduced into api-ms-win-core-com-l1-1-1.dll in Windows 10.0.10240.0 |
| [**CoTaskMemRealloc**](https://msdn.microsoft.com/en-us/library/windows/apps/ms687280.aspx)                                           | Introduced into api-ms-win-core-com-l1-1-1.dll in Windows 10.0.10240.0 |
| [**CoUninitialize**](https://msdn.microsoft.com/en-us/library/windows/apps/ms688715.aspx)                                               | Introduced into api-ms-win-core-com-l1-1-1.dll in Windows 10.0.10240.0 |
| [**CoUnmarshalInterface**](https://msdn.microsoft.com/en-us/library/windows/apps/ms693382.aspx)                                   | Introduced into api-ms-win-core-com-l1-1-1.dll in Windows 10.0.10240.0 |
| [**CreateStreamOnHGlobal**](https://msdn.microsoft.com/en-us/library/windows/apps/aa378980.aspx)                                 | Introduced into api-ms-win-core-com-l1-1-1.dll in Windows 10.0.10240.0 |
| [**FreePropVariantArray**](https://msdn.microsoft.com/en-us/library/windows/apps/bb762285.aspx)                            | Introduced into api-ms-win-core-com-l1-1-1.dll in Windows 10.0.10240.0 |
| [**GetHGlobalFromStream**](https://msdn.microsoft.com/en-us/library/windows/apps/aa379145.aspx)                                   | Introduced into api-ms-win-core-com-l1-1-1.dll in Windows 10.0.10240.0 |
| [**IIDFromString**](https://msdn.microsoft.com/en-us/library/windows/apps/ms687262.aspx)                                                 | Introduced into api-ms-win-core-com-l1-1-1.dll in Windows 10.0.10240.0 |
| [**PropVariantClear**](https://msdn.microsoft.com/en-us/library/windows/apps/bb776515.aspx)                                    | Introduced into api-ms-win-core-com-l1-1-1.dll in Windows 10.0.10240.0 |
| [**PropVariantCopy**](https://msdn.microsoft.com/en-us/library/windows/apps/bb776518.aspx)                                      | Introduced into api-ms-win-core-com-l1-1-1.dll in Windows 10.0.10240.0 |
| [**RoGetAgileReference**](https://msdn.microsoft.com/en-us/library/windows/apps/dn269839.aspx)                                   | Introduced into api-ms-win-core-com-l1-1-1.dll in Windows 10.0.10240.0 |
| [**StringFromCLSID**](https://msdn.microsoft.com/en-us/library/windows/apps/ms683917.aspx)                                             | Introduced into api-ms-win-core-com-l1-1-1.dll in Windows 10.0.10240.0 |
| [**StringFromGUID2**](https://msdn.microsoft.com/en-us/library/windows/apps/ms683893.aspx)                                             | Introduced into api-ms-win-core-com-l1-1-1.dll in Windows 10.0.10240.0 |
| [**StringFromIID**](https://msdn.microsoft.com/en-us/library/windows/apps/ms688692.aspx)                                                 | Introduced into api-ms-win-core-com-l1-1-1.dll in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-core-com-l2-1-1.dll"></span><span id="_API-MS-WIN-CORE-COM-L2-1-1.DLL"></span>APIs from the API Set api-ms-win-core-com-l2-1-1.dll


| API                                                                  | Requirements                                                           |
|----------------------------------------------------------------------|------------------------------------------------------------------------|
| [**CreateILockBytesOnHGlobal**](https://msdn.microsoft.com/en-us/library/windows/apps/aa378977.aspx)       | Introduced into api-ms-win-core-com-l2-1-1.dll in Windows 10.0.10240.0 |
| [**FmtIdToPropStgName**](https://msdn.microsoft.com/en-us/library/windows/apps/aa379108.aspx)                     | Introduced into api-ms-win-core-com-l2-1-1.dll in Windows 10.0.10240.0 |
| [**GetConvertStg**](https://msdn.microsoft.com/en-us/library/windows/apps/aa379138.aspx)                               | Introduced into api-ms-win-core-com-l2-1-1.dll in Windows 10.0.10240.0 |
| [**GetHGlobalFromILockBytes**](https://msdn.microsoft.com/en-us/library/windows/apps/aa379140.aspx)         | Introduced into api-ms-win-core-com-l2-1-1.dll in Windows 10.0.10240.0 |
| [**PropStgNameToFmtId**](https://msdn.microsoft.com/en-us/library/windows/apps/aa380071.aspx)                     | Introduced into api-ms-win-core-com-l2-1-1.dll in Windows 10.0.10240.0 |
| [**ReadClassStg**](https://msdn.microsoft.com/en-us/library/windows/apps/aa380302.aspx)                                 | Introduced into api-ms-win-core-com-l2-1-1.dll in Windows 10.0.10240.0 |
| [**ReadClassStm**](https://msdn.microsoft.com/en-us/library/windows/apps/aa380303.aspx)                                 | Introduced into api-ms-win-core-com-l2-1-1.dll in Windows 10.0.10240.0 |
| [**StgCreateDocfile**](https://msdn.microsoft.com/en-us/library/windows/apps/aa380323.aspx)                         | Introduced into api-ms-win-core-com-l2-1-1.dll in Windows 10.0.10240.0 |
| [**StgCreateDocfileOnILockBytes**](https://msdn.microsoft.com/en-us/library/windows/apps/aa380324.aspx) | Introduced into api-ms-win-core-com-l2-1-1.dll in Windows 10.0.10240.0 |
| [**StgCreatePropSetStg**](https://msdn.microsoft.com/en-us/library/windows/apps/aa380325.aspx)                   | Introduced into api-ms-win-core-com-l2-1-1.dll in Windows 10.0.10240.0 |
| [**StgCreatePropStg**](https://msdn.microsoft.com/en-us/library/windows/apps/aa380327.aspx)                         | Introduced into api-ms-win-core-com-l2-1-1.dll in Windows 10.0.10240.0 |
| [**StgCreateStorageEx**](https://msdn.microsoft.com/en-us/library/windows/apps/aa380328.aspx)                     | Introduced into api-ms-win-core-com-l2-1-1.dll in Windows 10.0.10240.0 |
| [**StgIsStorageFile**](https://msdn.microsoft.com/en-us/library/windows/apps/aa380334.aspx)                         | Introduced into api-ms-win-core-com-l2-1-1.dll in Windows 10.0.10240.0 |
| [**StgIsStorageILockBytes**](https://msdn.microsoft.com/en-us/library/windows/apps/aa380335.aspx)             | Introduced into api-ms-win-core-com-l2-1-1.dll in Windows 10.0.10240.0 |
| [**StgOpenPropStg**](https://msdn.microsoft.com/en-us/library/windows/apps/aa380340.aspx)                             | Introduced into api-ms-win-core-com-l2-1-1.dll in Windows 10.0.10240.0 |
| [**StgOpenStorage**](https://msdn.microsoft.com/en-us/library/windows/apps/aa380341.aspx)                             | Introduced into api-ms-win-core-com-l2-1-1.dll in Windows 10.0.10240.0 |
| [**StgOpenStorageEx**](https://msdn.microsoft.com/en-us/library/windows/apps/aa380342.aspx)                         | Introduced into api-ms-win-core-com-l2-1-1.dll in Windows 10.0.10240.0 |
| [**StgOpenStorageOnILockBytes**](https://msdn.microsoft.com/en-us/library/windows/apps/aa380343.aspx)     | Introduced into api-ms-win-core-com-l2-1-1.dll in Windows 10.0.10240.0 |
| [**StgSetTimes**](https://msdn.microsoft.com/en-us/library/windows/apps/aa380347.aspx)                                   | Introduced into api-ms-win-core-com-l2-1-1.dll in Windows 10.0.10240.0 |
| [**WriteClassStg**](https://msdn.microsoft.com/en-us/library/windows/apps/aa380384.aspx)                               | Introduced into api-ms-win-core-com-l2-1-1.dll in Windows 10.0.10240.0 |
| [**WriteClassStm**](https://msdn.microsoft.com/en-us/library/windows/apps/aa380385.aspx)                               | Introduced into api-ms-win-core-com-l2-1-1.dll in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-core-com-midlproxystub-l1-1-0.dll"></span><span id="_API-MS-WIN-CORE-COM-MIDLPROXYSTUB-L1-1-0.DLL"></span>APIs from the API Set api-ms-win-core-com-midlproxystub-l1-1-0.dll


| API                                                                                            | Requirements                                                                         |
|------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| [**CStdAsyncStubBuffer\_AddRef**](https://msdn.microsoft.com/en-us/library/windows/apps/mt243874.aspx)                              | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**CStdAsyncStubBuffer\_Connect**](https://msdn.microsoft.com/en-us/library/windows/apps/mt243875.aspx)                            | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**CStdAsyncStubBuffer\_Disconnect**](https://msdn.microsoft.com/en-us/library/windows/apps/mt243876.aspx)                      | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**CStdAsyncStubBuffer\_Invoke**](https://msdn.microsoft.com/en-us/library/windows/apps/mt243877.aspx)                              | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**CStdAsyncStubBuffer\_QueryInterface**](https://msdn.microsoft.com/en-us/library/windows/apps/mt243878.aspx)              | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**CStdAsyncStubBuffer\_Release**](https://msdn.microsoft.com/en-us/library/windows/apps/mt243879.aspx)                            | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**CStdAsyncStubBuffer2\_Connect**](https://msdn.microsoft.com/en-us/library/windows/apps/mt243871.aspx)                          | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**CStdAsyncStubBuffer2\_Disconnect**](https://msdn.microsoft.com/en-us/library/windows/apps/mt243872.aspx)                    | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**CStdAsyncStubBuffer2\_Release**](https://msdn.microsoft.com/en-us/library/windows/apps/mt243873.aspx)                          | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**CStdStubBuffer2\_Connect**](https://msdn.microsoft.com/en-us/library/windows/apps/mt243880.aspx)                                    | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**CStdStubBuffer2\_CountRefs**](https://msdn.microsoft.com/en-us/library/windows/apps/mt243881.aspx)                                | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**CStdStubBuffer2\_Disconnect**](https://msdn.microsoft.com/en-us/library/windows/apps/mt243882.aspx)                              | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**CStdStubBuffer2\_QueryInterface**](https://msdn.microsoft.com/en-us/library/windows/apps/mt243883.aspx)                      | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**NdrProxyForwardingFunction10**](https://www.bing.com/search?q=NdrProxyForwardingFunction10) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**NdrProxyForwardingFunction11**](https://www.bing.com/search?q=NdrProxyForwardingFunction11) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**NdrProxyForwardingFunction12**](https://www.bing.com/search?q=NdrProxyForwardingFunction12) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**NdrProxyForwardingFunction13**](https://www.bing.com/search?q=NdrProxyForwardingFunction13) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**NdrProxyForwardingFunction14**](https://www.bing.com/search?q=NdrProxyForwardingFunction14) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**NdrProxyForwardingFunction15**](https://www.bing.com/search?q=NdrProxyForwardingFunction15) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**NdrProxyForwardingFunction16**](https://www.bing.com/search?q=NdrProxyForwardingFunction16) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**NdrProxyForwardingFunction17**](https://www.bing.com/search?q=NdrProxyForwardingFunction17) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**NdrProxyForwardingFunction18**](https://www.bing.com/search?q=NdrProxyForwardingFunction18) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**NdrProxyForwardingFunction19**](https://www.bing.com/search?q=NdrProxyForwardingFunction19) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**NdrProxyForwardingFunction20**](https://www.bing.com/search?q=NdrProxyForwardingFunction20) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**NdrProxyForwardingFunction21**](https://www.bing.com/search?q=NdrProxyForwardingFunction21) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**NdrProxyForwardingFunction22**](https://www.bing.com/search?q=NdrProxyForwardingFunction22) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**NdrProxyForwardingFunction23**](https://www.bing.com/search?q=NdrProxyForwardingFunction23) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**NdrProxyForwardingFunction24**](https://www.bing.com/search?q=NdrProxyForwardingFunction24) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**NdrProxyForwardingFunction25**](https://www.bing.com/search?q=NdrProxyForwardingFunction25) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**NdrProxyForwardingFunction26**](https://www.bing.com/search?q=NdrProxyForwardingFunction26) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**NdrProxyForwardingFunction27**](https://www.bing.com/search?q=NdrProxyForwardingFunction27) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**NdrProxyForwardingFunction28**](https://www.bing.com/search?q=NdrProxyForwardingFunction28) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**NdrProxyForwardingFunction29**](https://www.bing.com/search?q=NdrProxyForwardingFunction29) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**NdrProxyForwardingFunction3**](https://www.bing.com/search?q=NdrProxyForwardingFunction3)   | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**NdrProxyForwardingFunction30**](https://www.bing.com/search?q=NdrProxyForwardingFunction30) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**NdrProxyForwardingFunction31**](https://www.bing.com/search?q=NdrProxyForwardingFunction31) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**NdrProxyForwardingFunction32**](https://www.bing.com/search?q=NdrProxyForwardingFunction32) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**NdrProxyForwardingFunction4**](https://www.bing.com/search?q=NdrProxyForwardingFunction4)   | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**NdrProxyForwardingFunction5**](https://www.bing.com/search?q=NdrProxyForwardingFunction5)   | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**NdrProxyForwardingFunction6**](https://www.bing.com/search?q=NdrProxyForwardingFunction6)   | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**NdrProxyForwardingFunction7**](https://www.bing.com/search?q=NdrProxyForwardingFunction7)   | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**NdrProxyForwardingFunction8**](https://www.bing.com/search?q=NdrProxyForwardingFunction8)   | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**NdrProxyForwardingFunction9**](https://www.bing.com/search?q=NdrProxyForwardingFunction9)   | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**ObjectStublessClient10**](https://www.bing.com/search?q=ObjectStublessClient10)             | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**ObjectStublessClient11**](https://www.bing.com/search?q=ObjectStublessClient11)             | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**ObjectStublessClient12**](https://www.bing.com/search?q=ObjectStublessClient12)             | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**ObjectStublessClient13**](https://www.bing.com/search?q=ObjectStublessClient13)             | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**ObjectStublessClient14**](https://www.bing.com/search?q=ObjectStublessClient14)             | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**ObjectStublessClient15**](https://www.bing.com/search?q=ObjectStublessClient15)             | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**ObjectStublessClient16**](https://www.bing.com/search?q=ObjectStublessClient16)             | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**ObjectStublessClient17**](https://www.bing.com/search?q=ObjectStublessClient17)             | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**ObjectStublessClient18**](https://www.bing.com/search?q=ObjectStublessClient18)             | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**ObjectStublessClient19**](https://www.bing.com/search?q=ObjectStublessClient19)             | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**ObjectStublessClient20**](https://www.bing.com/search?q=ObjectStublessClient20)             | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**ObjectStublessClient21**](https://www.bing.com/search?q=ObjectStublessClient21)             | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**ObjectStublessClient22**](https://www.bing.com/search?q=ObjectStublessClient22)             | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**ObjectStublessClient23**](https://www.bing.com/search?q=ObjectStublessClient23)             | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**ObjectStublessClient24**](https://www.bing.com/search?q=ObjectStublessClient24)             | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**ObjectStublessClient25**](https://www.bing.com/search?q=ObjectStublessClient25)             | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**ObjectStublessClient26**](https://www.bing.com/search?q=ObjectStublessClient26)             | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**ObjectStublessClient27**](https://www.bing.com/search?q=ObjectStublessClient27)             | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**ObjectStublessClient28**](https://www.bing.com/search?q=ObjectStublessClient28)             | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**ObjectStublessClient29**](https://www.bing.com/search?q=ObjectStublessClient29)             | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**ObjectStublessClient3**](https://www.bing.com/search?q=ObjectStublessClient3)               | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**ObjectStublessClient30**](https://www.bing.com/search?q=ObjectStublessClient30)             | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**ObjectStublessClient31**](https://www.bing.com/search?q=ObjectStublessClient31)             | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**ObjectStublessClient32**](https://www.bing.com/search?q=ObjectStublessClient32)             | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**ObjectStublessClient4**](https://www.bing.com/search?q=ObjectStublessClient4)               | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**ObjectStublessClient5**](https://www.bing.com/search?q=ObjectStublessClient5)               | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**ObjectStublessClient6**](https://www.bing.com/search?q=ObjectStublessClient6)               | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**ObjectStublessClient7**](https://www.bing.com/search?q=ObjectStublessClient7)               | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**ObjectStublessClient8**](https://www.bing.com/search?q=ObjectStublessClient8)               | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |
| [**ObjectStublessClient9**](https://www.bing.com/search?q=ObjectStublessClient9)               | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-core-datetime-l1-1-1.dll"></span><span id="_API-MS-WIN-CORE-DATETIME-L1-1-1.DLL"></span>APIs from the API Set api-ms-win-core-datetime-l1-1-1.dll


| API                                         | Requirements                                                                |
|---------------------------------------------|-----------------------------------------------------------------------------|
| [**GetDateFormatEx**](https://msdn.microsoft.com/en-us/library/windows/apps/dd318088.aspx) | Introduced into api-ms-win-core-datetime-l1-1-1.dll in Windows 10.0.10240.0 |
| [**GetTimeFormatEx**](https://msdn.microsoft.com/en-us/library/windows/apps/dd318131.aspx) | Introduced into api-ms-win-core-datetime-l1-1-1.dll in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-core-datetime-l1-1-2.dll"></span><span id="_API-MS-WIN-CORE-DATETIME-L1-1-2.DLL"></span>APIs from the API Set api-ms-win-core-datetime-l1-1-2.dll


| API                                                 | Requirements                                                                |
|-----------------------------------------------------|-----------------------------------------------------------------------------|
| [**GetDurationFormatEx**](https://msdn.microsoft.com/en-us/library/windows/apps/dd318092.aspx) | Introduced into api-ms-win-core-datetime-l1-1-2.dll in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-core-debug-l1-1-1.dll"></span><span id="_API-MS-WIN-CORE-DEBUG-L1-1-1.DLL"></span>APIs from the API Set api-ms-win-core-debug-l1-1-1.dll


| API                                              | Requirements                                                             |
|--------------------------------------------------|--------------------------------------------------------------------------|
| [**IsDebuggerPresent**](https://msdn.microsoft.com/en-us/library/windows/apps/ms680345.aspx)  | Introduced into api-ms-win-core-debug-l1-1-1.dll in Windows 10.0.10240.0 |
| [**OutputDebugStringA**](https://msdn.microsoft.com/en-us/library/windows/apps/aa363362.aspx) | Introduced into api-ms-win-core-debug-l1-1-1.dll in Windows 10.0.10240.0 |
| [**OutputDebugStringW**](https://msdn.microsoft.com/en-us/library/windows/apps/aa363362.aspx) | Introduced into api-ms-win-core-debug-l1-1-1.dll in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-core-delayload-l1-1-1.dll"></span><span id="_API-MS-WIN-CORE-DELAYLOAD-L1-1-1.DLL"></span>APIs from the API Set api-ms-win-core-delayload-l1-1-1.dll


| API                                                                                    | Requirements                                                                 |
|----------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| [**DelayLoadFailureHook**](https://www.bing.com/search?q=DelayLoadFailureHook)         | Introduced into api-ms-win-core-delayload-l1-1-1.dll in Windows 10.0.10240.0 |
| [**ResolveDelayLoadedAPI**](https://www.bing.com/search?q=ResolveDelayLoadedAPI)       | Introduced into api-ms-win-core-delayload-l1-1-1.dll in Windows 10.0.10240.0 |
| [**ResolveDelayLoadsFromDll**](https://www.bing.com/search?q=ResolveDelayLoadsFromDll) | Introduced into api-ms-win-core-delayload-l1-1-1.dll in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-core-errorhandling-l1-1-1.dll"></span><span id="_API-MS-WIN-CORE-ERRORHANDLING-L1-1-1.DLL"></span>APIs from the API Set api-ms-win-core-errorhandling-l1-1-1.dll


| API                                                                 | Requirements                                                                     |
|---------------------------------------------------------------------|----------------------------------------------------------------------------------|
| [**GetLastError**](https://msdn.microsoft.com/en-us/library/windows/apps/ms679360.aspx)                               | Introduced into api-ms-win-core-errorhandling-l1-1-1.dll in Windows 10.0.10240.0 |
| [**RaiseException**](https://msdn.microsoft.com/en-us/library/windows/apps/ms680552.aspx)                           | Introduced into api-ms-win-core-errorhandling-l1-1-1.dll in Windows 10.0.10240.0 |
| [**SetLastError**](https://msdn.microsoft.com/en-us/library/windows/apps/ms680627.aspx)                               | Introduced into api-ms-win-core-errorhandling-l1-1-1.dll in Windows 10.0.10240.0 |
| [**SetUnhandledExceptionFilter**](https://msdn.microsoft.com/en-us/library/windows/apps/ms680634.aspx) | Introduced into api-ms-win-core-errorhandling-l1-1-1.dll in Windows 10.0.10586.0 |

 

## <span id="_api-ms-win-core-errorhandling-l1-1-3.dll"></span><span id="_API-MS-WIN-CORE-ERRORHANDLING-L1-1-3.DLL"></span>APIs from the API Set api-ms-win-core-errorhandling-l1-1-3.dll


| API                                                       | Requirements                                                                     |
|-----------------------------------------------------------|----------------------------------------------------------------------------------|
| [**RaiseFailFastException**](https://msdn.microsoft.com/en-us/library/windows/apps/dd941688.aspx) | Introduced into api-ms-win-core-errorhandling-l1-1-3.dll in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-core-fibers-l1-1-1.dll"></span><span id="_API-MS-WIN-CORE-FIBERS-L1-1-1.DLL"></span>APIs from the API Set api-ms-win-core-fibers-l1-1-1.dll


| API                                       | Requirements                                                              |
|-------------------------------------------|---------------------------------------------------------------------------|
| [**FlsAlloc**](https://msdn.microsoft.com/en-us/library/windows/apps/ms682664.aspx)             | Introduced into api-ms-win-core-fibers-l1-1-1.dll in Windows 10.0.10240.0 |
| [**FlsFree**](https://msdn.microsoft.com/en-us/library/windows/apps/ms682667.aspx)               | Introduced into api-ms-win-core-fibers-l1-1-1.dll in Windows 10.0.10240.0 |
| [**FlsGetValue**](https://msdn.microsoft.com/en-us/library/windows/apps/ms683141.aspx)       | Introduced into api-ms-win-core-fibers-l1-1-1.dll in Windows 10.0.10240.0 |
| [**FlsSetValue**](https://msdn.microsoft.com/en-us/library/windows/apps/ms683146.aspx)       | Introduced into api-ms-win-core-fibers-l1-1-1.dll in Windows 10.0.10240.0 |
| [**IsThreadAFiber**](https://msdn.microsoft.com/en-us/library/windows/apps/ms684131.aspx) | Introduced into api-ms-win-core-fibers-l1-1-1.dll in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-core-fibers-l2-1-1.dll"></span><span id="_API-MS-WIN-CORE-FIBERS-L2-1-1.DLL"></span>APIs from the API Set api-ms-win-core-fibers-l2-1-1.dll


| API                                                                          | Requirements                                                                                               |
|------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| [**CalloutOnFiberStack**](https://www.bing.com/search?q=CalloutOnFiberStack) | Introduced into api-ms-win-core-fibers-l2-1-1.dll in Windows 10.0.10240.0. Removed in Windows 10.0.10586.0 |
| [**ConvertFiberToThread**](https://msdn.microsoft.com/en-us/library/windows/apps/ms682112.aspx)                        | Introduced into api-ms-win-core-fibers-l2-1-1.dll in Windows 10.0.10240.0                                  |
| [**ConvertThreadToFiberEx**](https://msdn.microsoft.com/en-us/library/windows/apps/ms682117.aspx)                    | Introduced into api-ms-win-core-fibers-l2-1-1.dll in Windows 10.0.10240.0                                  |
| [**CreateFiberEx**](https://msdn.microsoft.com/en-us/library/windows/apps/ms682406.aspx)                                      | Introduced into api-ms-win-core-fibers-l2-1-1.dll in Windows 10.0.10240.0                                  |
| [**DeleteFiber**](https://msdn.microsoft.com/en-us/library/windows/apps/ms682556.aspx)                                          | Introduced into api-ms-win-core-fibers-l2-1-1.dll in Windows 10.0.10240.0                                  |
| [**SwitchToFiber**](https://msdn.microsoft.com/en-us/library/windows/apps/ms686350.aspx)                                      | Introduced into api-ms-win-core-fibers-l2-1-1.dll in Windows 10.0.10240.0                                  |

 

## <span id="_api-ms-win-core-file-ansi-l2-1-0.dll"></span><span id="_API-MS-WIN-CORE-FILE-ANSI-L2-1-0.DLL"></span>APIs from the API Set api-ms-win-core-file-ansi-l2-1-0.dll


| API                                | Requirements                                                                 |
|------------------------------------|------------------------------------------------------------------------------|
| [**ReplaceFileA**](https://msdn.microsoft.com/en-us/library/windows/apps/aa365512.aspx) | Introduced into api-ms-win-core-file-ansi-l2-1-0.dll in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-core-file-l1-2-1.dll"></span><span id="_API-MS-WIN-CORE-FILE-L1-2-1.DLL"></span>APIs from the API Set api-ms-win-core-file-l1-2-1.dll


| API                                                             | Requirements                                                            |
|-----------------------------------------------------------------|-------------------------------------------------------------------------|
| [**CreateDirectoryA**](https://msdn.microsoft.com/en-us/library/windows/apps/aa363855.aspx)                      | Introduced into api-ms-win-core-file-l1-2-1.dll in Windows 10.0.10240.0 |
| [**CreateDirectoryW**](https://msdn.microsoft.com/en-us/library/windows/apps/aa363855.aspx)                      | Introduced into api-ms-win-core-file-l1-2-1.dll in Windows 10.0.10240.0 |
| [**CreateFile2**](https://msdn.microsoft.com/en-us/library/windows/apps/hh449422.aspx)                               | Introduced into api-ms-win-core-file-l1-2-1.dll in Windows 10.0.10240.0 |
| [**DeleteFileA**](https://msdn.microsoft.com/en-us/library/windows/apps/aa363915.aspx)                                | Introduced into api-ms-win-core-file-l1-2-1.dll in Windows 10.0.10240.0 |
| [**DeleteFileW**](https://msdn.microsoft.com/en-us/library/windows/apps/aa363915.aspx)                                | Introduced into api-ms-win-core-file-l1-2-1.dll in Windows 10.0.10240.0 |
| [**FindClose**](https://msdn.microsoft.com/en-us/library/windows/apps/aa364413.aspx)                                   | Introduced into api-ms-win-core-file-l1-2-1.dll in Windows 10.0.10240.0 |
| [**FindFirstFileExA**](https://msdn.microsoft.com/en-us/library/windows/apps/aa364419.aspx)                      | Introduced into api-ms-win-core-file-l1-2-1.dll in Windows 10.0.10240.0 |
| [**FindFirstFileExW**](https://msdn.microsoft.com/en-us/library/windows/apps/aa364419.aspx)                      | Introduced into api-ms-win-core-file-l1-2-1.dll in Windows 10.0.10240.0 |
| [**FindNextFileA**](https://msdn.microsoft.com/en-us/library/windows/apps/aa364428.aspx)                            | Introduced into api-ms-win-core-file-l1-2-1.dll in Windows 10.0.10240.0 |
| [**FindNextFileW**](https://msdn.microsoft.com/en-us/library/windows/apps/aa364428.aspx)                            | Introduced into api-ms-win-core-file-l1-2-1.dll in Windows 10.0.10240.0 |
| [**FlushFileBuffers**](https://msdn.microsoft.com/en-us/library/windows/apps/aa364439.aspx)                     | Introduced into api-ms-win-core-file-l1-2-1.dll in Windows 10.0.10240.0 |
| [**GetDiskFreeSpaceExA**](https://msdn.microsoft.com/en-us/library/windows/apps/aa364937.aspx)                | Introduced into api-ms-win-core-file-l1-2-1.dll in Windows 10.0.10240.0 |
| [**GetDiskFreeSpaceExW**](https://msdn.microsoft.com/en-us/library/windows/apps/aa364937.aspx)                | Introduced into api-ms-win-core-file-l1-2-1.dll in Windows 10.0.10240.0 |
| [**GetFileAttributesExA**](https://msdn.microsoft.com/en-us/library/windows/apps/aa364946.aspx)              | Introduced into api-ms-win-core-file-l1-2-1.dll in Windows 10.0.10240.0 |
| [**GetFileAttributesExW**](https://msdn.microsoft.com/en-us/library/windows/apps/aa364946.aspx)              | Introduced into api-ms-win-core-file-l1-2-1.dll in Windows 10.0.10240.0 |
| [**GetFileSizeEx**](https://msdn.microsoft.com/en-us/library/windows/apps/aa364957.aspx)                           | Introduced into api-ms-win-core-file-l1-2-1.dll in Windows 10.0.10240.0 |
| [**GetFileTime**](https://msdn.microsoft.com/en-us/library/windows/apps/ms724320.aspx)                             | Introduced into api-ms-win-core-file-l1-2-1.dll in Windows 10.0.10240.0 |
| [**GetFileType**](https://msdn.microsoft.com/en-us/library/windows/apps/aa364960.aspx)                               | Introduced into api-ms-win-core-file-l1-2-1.dll in Windows 10.0.10240.0 |
| [**GetFullPathNameW**](https://msdn.microsoft.com/en-us/library/windows/apps/aa364963.aspx)                      | Introduced into api-ms-win-core-file-l1-2-1.dll in Windows 10.0.10240.0 |
| [**GetLongPathNameW**](https://msdn.microsoft.com/en-us/library/windows/apps/aa364980.aspx)                      | Introduced into api-ms-win-core-file-l1-2-1.dll in Windows 10.0.10240.0 |
| [**GetTempFileNameW**](https://msdn.microsoft.com/en-us/library/windows/apps/aa364991.aspx)                      | Introduced into api-ms-win-core-file-l1-2-1.dll in Windows 10.0.10240.0 |
| [**GetTempPathW**](https://msdn.microsoft.com/en-us/library/windows/apps/aa364992.aspx)                              | Introduced into api-ms-win-core-file-l1-2-1.dll in Windows 10.0.10240.0 |
| [**LockFileEx**](https://msdn.microsoft.com/en-us/library/windows/apps/aa365203.aspx)                                 | Introduced into api-ms-win-core-file-l1-2-1.dll in Windows 10.0.10240.0 |
| [**ReadFile**](https://msdn.microsoft.com/en-us/library/windows/apps/aa365467.aspx)                                     | Introduced into api-ms-win-core-file-l1-2-1.dll in Windows 10.0.10240.0 |
| [**RemoveDirectoryA**](https://msdn.microsoft.com/en-us/library/windows/apps/aa365488.aspx)                      | Introduced into api-ms-win-core-file-l1-2-1.dll in Windows 10.0.10240.0 |
| [**RemoveDirectoryW**](https://msdn.microsoft.com/en-us/library/windows/apps/aa365488.aspx)                      | Introduced into api-ms-win-core-file-l1-2-1.dll in Windows 10.0.10240.0 |
| [**SetEndOfFile**](https://msdn.microsoft.com/en-us/library/windows/apps/aa365531.aspx)                             | Introduced into api-ms-win-core-file-l1-2-1.dll in Windows 10.0.10240.0 |
| [**SetFileAttributesA**](https://msdn.microsoft.com/en-us/library/windows/apps/aa365535.aspx)                  | Introduced into api-ms-win-core-file-l1-2-1.dll in Windows 10.0.10240.0 |
| [**SetFileAttributesW**](https://msdn.microsoft.com/en-us/library/windows/apps/aa365535.aspx)                  | Introduced into api-ms-win-core-file-l1-2-1.dll in Windows 10.0.10240.0 |
| [**SetFileInformationByHandle**](https://msdn.microsoft.com/en-us/library/windows/apps/aa365539.aspx) | Introduced into api-ms-win-core-file-l1-2-1.dll in Windows 10.0.10240.0 |
| [**SetFilePointerEx**](https://msdn.microsoft.com/en-us/library/windows/apps/aa365542.aspx)                     | Introduced into api-ms-win-core-file-l1-2-1.dll in Windows 10.0.10240.0 |
| [**SetFileTime**](https://msdn.microsoft.com/en-us/library/windows/apps/ms724933.aspx)                             | Introduced into api-ms-win-core-file-l1-2-1.dll in Windows 10.0.10240.0 |
| [**UnlockFileEx**](https://msdn.microsoft.com/en-us/library/windows/apps/aa365716.aspx)                             | Introduced into api-ms-win-core-file-l1-2-1.dll in Windows 10.0.10240.0 |
| [**WriteFile**](https://msdn.microsoft.com/en-us/library/windows/apps/aa365747.aspx)                                   | Introduced into api-ms-win-core-file-l1-2-1.dll in Windows 10.0.10240.0 |
| [**CompareFileTime**](https://msdn.microsoft.com/en-us/library/windows/apps/ms724214.aspx)                     | Introduced into api-ms-win-core-file-l1-2-1.dll in Windows 10.0.10586.0 |
| [**FileTimeToLocalFileTime**](https://msdn.microsoft.com/en-us/library/windows/apps/ms724277.aspx)     | Introduced into api-ms-win-core-file-l1-2-1.dll in Windows 10.0.14393.0 |
| [**FindFirstFileA**](https://msdn.microsoft.com/en-us/library/windows/apps/aa364418.aspx)                          | Introduced into api-ms-win-core-file-l1-2-1.dll in Windows 10.0.14393.0 |
| [**FindFirstFileW**](https://msdn.microsoft.com/en-us/library/windows/apps/aa364418.aspx)                          | Introduced into api-ms-win-core-file-l1-2-1.dll in Windows 10.0.14393.0 |
| [**GetDiskFreeSpaceA**](https://msdn.microsoft.com/en-us/library/windows/apps/aa364935.aspx)                    | Introduced into api-ms-win-core-file-l1-2-1.dll in Windows 10.0.14393.0 |
| [**GetDiskFreeSpaceW**](https://msdn.microsoft.com/en-us/library/windows/apps/aa364935.aspx)                    | Introduced into api-ms-win-core-file-l1-2-1.dll in Windows 10.0.14393.0 |
| [**GetFileAttributesA**](https://msdn.microsoft.com/en-us/library/windows/apps/aa364944.aspx)                  | Introduced into api-ms-win-core-file-l1-2-1.dll in Windows 10.0.14393.0 |
| [**GetFileAttributesW**](https://msdn.microsoft.com/en-us/library/windows/apps/aa364944.aspx)                  | Introduced into api-ms-win-core-file-l1-2-1.dll in Windows 10.0.14393.0 |
| [**GetFinalPathNameByHandleA**](https://msdn.microsoft.com/en-us/library/windows/apps/aa364962.aspx)    | Introduced into api-ms-win-core-file-l1-2-1.dll in Windows 10.0.14393.0 |
| [**GetFinalPathNameByHandleW**](https://msdn.microsoft.com/en-us/library/windows/apps/aa364962.aspx)    | Introduced into api-ms-win-core-file-l1-2-1.dll in Windows 10.0.14393.0 |
| [**LocalFileTimeToFileTime**](https://msdn.microsoft.com/en-us/library/windows/apps/ms724490.aspx)     | Introduced into api-ms-win-core-file-l1-2-1.dll in Windows 10.0.14393.0 |
| [**ReadFileEx**](https://msdn.microsoft.com/en-us/library/windows/apps/aa365468.aspx)                                 | Introduced into api-ms-win-core-file-l1-2-1.dll in Windows 10.0.14393.0 |
| [**SetFilePointer**](https://msdn.microsoft.com/en-us/library/windows/apps/aa365541.aspx)                         | Introduced into api-ms-win-core-file-l1-2-1.dll in Windows 10.0.14393.0 |
| [**WriteFileEx**](https://msdn.microsoft.com/en-us/library/windows/apps/aa365748.aspx)                               | Introduced into api-ms-win-core-file-l1-2-1.dll in Windows 10.0.14393.0 |

 

## <span id="_api-ms-win-core-file-l2-1-1.dll"></span><span id="_API-MS-WIN-CORE-FILE-L2-1-1.DLL"></span>APIs from the API Set api-ms-win-core-file-l2-1-1.dll


| API                                                                 | Requirements                                                            |
|---------------------------------------------------------------------|-------------------------------------------------------------------------|
| [**CopyFile2**](https://msdn.microsoft.com/en-us/library/windows/apps/hh449404.aspx)                                       | Introduced into api-ms-win-core-file-l2-1-1.dll in Windows 10.0.10240.0 |
| [**GetFileInformationByHandleEx**](https://msdn.microsoft.com/en-us/library/windows/apps/aa364953.aspx) | Introduced into api-ms-win-core-file-l2-1-1.dll in Windows 10.0.10240.0 |
| [**MoveFileExW**](https://msdn.microsoft.com/en-us/library/windows/apps/aa365240.aspx)                                    | Introduced into api-ms-win-core-file-l2-1-1.dll in Windows 10.0.10240.0 |
| [**ReplaceFileW**](https://msdn.microsoft.com/en-us/library/windows/apps/aa365512.aspx)                                  | Introduced into api-ms-win-core-file-l2-1-1.dll in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-core-handle-l1-1-0.dll"></span><span id="_API-MS-WIN-CORE-HANDLE-L1-1-0.DLL"></span>APIs from the API Set api-ms-win-core-handle-l1-1-0.dll


| API                                                   | Requirements                                                              |
|-------------------------------------------------------|---------------------------------------------------------------------------|
| [**CloseHandle**](https://msdn.microsoft.com/en-us/library/windows/apps/ms724211.aspx)                   | Introduced into api-ms-win-core-handle-l1-1-0.dll in Windows 10.0.10240.0 |
| [**CompareObjectHandles**](https://msdn.microsoft.com/en-us/library/windows/apps/mt438733.aspx) | Introduced into api-ms-win-core-handle-l1-1-0.dll in Windows 10.0.10240.0 |
| [**DuplicateHandle**](https://msdn.microsoft.com/en-us/library/windows/apps/ms724251.aspx)           | Introduced into api-ms-win-core-handle-l1-1-0.dll in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-core-heap-l1-2-0.dll"></span><span id="_API-MS-WIN-CORE-HEAP-L1-2-0.DLL"></span>APIs from the API Set api-ms-win-core-heap-l1-2-0.dll


| API                                               | Requirements                                                            |
|---------------------------------------------------|-------------------------------------------------------------------------|
| [**GetProcessHeap**](https://msdn.microsoft.com/en-us/library/windows/apps/aa366569.aspx)         | Introduced into api-ms-win-core-heap-l1-2-0.dll in Windows 10.0.10240.0 |
| [**HeapAlloc**](https://msdn.microsoft.com/en-us/library/windows/apps/aa366597.aspx)                   | Introduced into api-ms-win-core-heap-l1-2-0.dll in Windows 10.0.10240.0 |
| [**HeapCompact**](https://msdn.microsoft.com/en-us/library/windows/apps/aa366598.aspx)               | Introduced into api-ms-win-core-heap-l1-2-0.dll in Windows 10.0.10240.0 |
| [**HeapCreate**](https://msdn.microsoft.com/en-us/library/windows/apps/aa366599.aspx)                 | Introduced into api-ms-win-core-heap-l1-2-0.dll in Windows 10.0.10240.0 |
| [**HeapDestroy**](https://msdn.microsoft.com/en-us/library/windows/apps/aa366700.aspx)               | Introduced into api-ms-win-core-heap-l1-2-0.dll in Windows 10.0.10240.0 |
| [**HeapFree**](https://msdn.microsoft.com/en-us/library/windows/apps/aa366701.aspx)                     | Introduced into api-ms-win-core-heap-l1-2-0.dll in Windows 10.0.10240.0 |
| [**HeapReAlloc**](https://msdn.microsoft.com/en-us/library/windows/apps/aa366704.aspx)               | Introduced into api-ms-win-core-heap-l1-2-0.dll in Windows 10.0.10240.0 |
| [**HeapSetInformation**](https://msdn.microsoft.com/en-us/library/windows/apps/aa366705.aspx) | Introduced into api-ms-win-core-heap-l1-2-0.dll in Windows 10.0.10240.0 |
| [**HeapSize**](https://msdn.microsoft.com/en-us/library/windows/apps/aa366706.aspx)                     | Introduced into api-ms-win-core-heap-l1-2-0.dll in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-core-interlocked-l1-2-0.dll"></span><span id="_API-MS-WIN-CORE-INTERLOCKED-L1-2-0.DLL"></span>APIs from the API Set api-ms-win-core-interlocked-l1-2-0.dll


| API                                                               | Requirements                                                                   |
|-------------------------------------------------------------------|--------------------------------------------------------------------------------|
| [**InitializeSListHead**](https://msdn.microsoft.com/en-us/library/windows/apps/ms683482.aspx)               | Introduced into api-ms-win-core-interlocked-l1-2-0.dll in Windows 10.0.10240.0 |
| [**InterlockedFlushSList**](https://msdn.microsoft.com/en-us/library/windows/apps/ms683612.aspx)           | Introduced into api-ms-win-core-interlocked-l1-2-0.dll in Windows 10.0.10240.0 |
| [**InterlockedPopEntrySList**](https://msdn.microsoft.com/en-us/library/windows/apps/ms683648.aspx)     | Introduced into api-ms-win-core-interlocked-l1-2-0.dll in Windows 10.0.10240.0 |
| [**InterlockedPushEntrySList**](https://msdn.microsoft.com/en-us/library/windows/apps/ms684020.aspx)   | Introduced into api-ms-win-core-interlocked-l1-2-0.dll in Windows 10.0.10240.0 |
| [**InterlockedPushListSListEx**](https://msdn.microsoft.com/en-us/library/windows/apps/hh972673.aspx) | Introduced into api-ms-win-core-interlocked-l1-2-0.dll in Windows 10.0.10240.0 |
| [**QueryDepthSList**](https://msdn.microsoft.com/en-us/library/windows/apps/ms684916.aspx)                       | Introduced into api-ms-win-core-interlocked-l1-2-0.dll in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-core-io-l1-1-1.dll"></span><span id="_API-MS-WIN-CORE-IO-L1-1-1.DLL"></span>APIs from the API Set api-ms-win-core-io-l1-1-1.dll


| API                                                                    | Requirements                                                          |
|------------------------------------------------------------------------|-----------------------------------------------------------------------|
| [**CancelIoEx**](https://msdn.microsoft.com/en-us/library/windows/apps/aa363792.aspx)                                   | Introduced into api-ms-win-core-io-l1-1-1.dll in Windows 10.0.10240.0 |
| [**GetOverlappedResultEx**](https://msdn.microsoft.com/en-us/library/windows/apps/hh448542.aspx)                | Introduced into api-ms-win-core-io-l1-1-1.dll in Windows 10.0.10240.0 |
| [**CancelIo**](https://msdn.microsoft.com/en-us/library/windows/apps/aa363791.aspx)                                            | Introduced into api-ms-win-core-io-l1-1-1.dll in Windows 10.0.14393.0 |
| [**CreateIoCompletionPort**](https://msdn.microsoft.com/en-us/library/windows/apps/aa363862.aspx)                | Introduced into api-ms-win-core-io-l1-1-1.dll in Windows 10.0.14393.0 |
| [**GetOverlappedResult**](https://msdn.microsoft.com/en-us/library/windows/apps/ms683209.aspx)                    | Introduced into api-ms-win-core-io-l1-1-1.dll in Windows 10.0.14393.0 |
| [**GetQueuedCompletionStatus**](https://msdn.microsoft.com/en-us/library/windows/apps/aa364986.aspx)          | Introduced into api-ms-win-core-io-l1-1-1.dll in Windows 10.0.14393.0 |
| [**GetQueuedCompletionStatusEx**](https://msdn.microsoft.com/en-us/library/windows/apps/aa364988.aspx) | Introduced into api-ms-win-core-io-l1-1-1.dll in Windows 10.0.14393.0 |
| [**PostQueuedCompletionStatus**](https://msdn.microsoft.com/en-us/library/windows/apps/aa365458.aspx)        | Introduced into api-ms-win-core-io-l1-1-1.dll in Windows 10.0.14393.0 |

 

## <span id="_api-ms-win-core-kernel32-legacy-l1-1-1.dll"></span><span id="_API-MS-WIN-CORE-KERNEL32-LEGACY-L1-1-1.DLL"></span>APIs from the API Set api-ms-win-core-kernel32-legacy-l1-1-1.dll


| API                              | Requirements                                                                       |
|----------------------------------|------------------------------------------------------------------------------------|
| [**MoveFileExA**](https://msdn.microsoft.com/en-us/library/windows/apps/aa365240.aspx) | Introduced into api-ms-win-core-kernel32-legacy-l1-1-1.dll in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-core-largeinteger-l1-1-0.dll"></span><span id="_API-MS-WIN-CORE-LARGEINTEGER-L1-1-0.DLL"></span>APIs from the API Set api-ms-win-core-largeinteger-l1-1-0.dll


| API                          | Requirements                                                                    |
|------------------------------|---------------------------------------------------------------------------------|
| [**MulDiv**](https://msdn.microsoft.com/en-us/library/windows/apps/aa383718.aspx) | Introduced into api-ms-win-core-largeinteger-l1-1-0.dll in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-core-libraryloader-l1-2-0.dll"></span><span id="_API-MS-WIN-CORE-LIBRARYLOADER-L1-2-0.DLL"></span>APIs from the API Set api-ms-win-core-libraryloader-l1-2-0.dll


| API                                                             | Requirements                                                                     |
|-----------------------------------------------------------------|----------------------------------------------------------------------------------|
| [**DisableThreadLibraryCalls**](https://msdn.microsoft.com/en-us/library/windows/apps/ms682579.aspx) | Introduced into api-ms-win-core-libraryloader-l1-2-0.dll in Windows 10.0.10240.0 |
| [**FindStringOrdinal**](https://msdn.microsoft.com/en-us/library/windows/apps/dd318061.aspx)                 | Introduced into api-ms-win-core-libraryloader-l1-2-0.dll in Windows 10.0.10240.0 |
| [**FreeLibrary**](https://msdn.microsoft.com/en-us/library/windows/apps/ms683152.aspx)                             | Introduced into api-ms-win-core-libraryloader-l1-2-0.dll in Windows 10.0.10240.0 |
| [**GetModuleFileNameA**](https://msdn.microsoft.com/en-us/library/windows/apps/ms683197.aspx)                | Introduced into api-ms-win-core-libraryloader-l1-2-0.dll in Windows 10.0.10240.0 |
| [**GetModuleFileNameW**](https://msdn.microsoft.com/en-us/library/windows/apps/ms683197.aspx)                | Introduced into api-ms-win-core-libraryloader-l1-2-0.dll in Windows 10.0.10240.0 |
| [**GetProcAddress**](https://msdn.microsoft.com/en-us/library/windows/apps/ms683212.aspx)                       | Introduced into api-ms-win-core-libraryloader-l1-2-0.dll in Windows 10.0.10240.0 |
| [**FreeLibraryAndExitThread**](https://msdn.microsoft.com/en-us/library/windows/apps/ms683153.aspx)   | Introduced into api-ms-win-core-libraryloader-l1-2-0.dll in Windows 10.0.10586.0 |

 

## <span id="_api-ms-win-core-libraryloader-l2-1-0.dll"></span><span id="_API-MS-WIN-CORE-LIBRARYLOADER-L2-1-0.DLL"></span>APIs from the API Set api-ms-win-core-libraryloader-l2-1-0.dll


| API                                                                 | Requirements                                                                     |
|---------------------------------------------------------------------|----------------------------------------------------------------------------------|
| [**LoadPackagedLibrary**](https://msdn.microsoft.com/en-us/library/windows/apps/hh447159.aspx)                 | Introduced into api-ms-win-core-libraryloader-l2-1-0.dll in Windows 10.0.10240.0 |
| [**QueryOptionalDelayLoadedAPI**](https://msdn.microsoft.com/en-us/library/windows/apps/mt403328.aspx) | Introduced into api-ms-win-core-libraryloader-l2-1-0.dll in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-core-localization-ansi-l1-1-0.dll"></span><span id="_API-MS-WIN-CORE-LOCALIZATION-ANSI-L1-1-0.DLL"></span>APIs from the API Set api-ms-win-core-localization-ansi-l1-1-0.dll


| API                                          | Requirements                                                                         |
|----------------------------------------------|--------------------------------------------------------------------------------------|
| [**GetStringTypeExA**](https://msdn.microsoft.com/en-us/library/windows/apps/dd318118.aspx) | Introduced into api-ms-win-core-localization-ansi-l1-1-0.dll in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-core-localization-l1-2-1.dll"></span><span id="_API-MS-WIN-CORE-LOCALIZATION-L1-2-1.DLL"></span>APIs from the API Set api-ms-win-core-localization-l1-2-1.dll


| API                                                           | Requirements                                                                    |
|---------------------------------------------------------------|---------------------------------------------------------------------------------|
| [**EnumSystemGeoID**](https://msdn.microsoft.com/en-us/library/windows/apps/dd317826.aspx)                   | Introduced into api-ms-win-core-localization-l1-2-1.dll in Windows 10.0.10240.0 |
| [**EnumSystemLocalesEx**](https://msdn.microsoft.com/en-us/library/windows/apps/dd317829.aspx)           | Introduced into api-ms-win-core-localization-l1-2-1.dll in Windows 10.0.10240.0 |
| [**FindNLSStringEx**](https://msdn.microsoft.com/en-us/library/windows/apps/dd318059.aspx)                   | Introduced into api-ms-win-core-localization-l1-2-1.dll in Windows 10.0.10240.0 |
| [**FormatMessageA**](https://msdn.microsoft.com/en-us/library/windows/apps/ms679351.aspx)                      | Introduced into api-ms-win-core-localization-l1-2-1.dll in Windows 10.0.10240.0 |
| [**FormatMessageW**](https://msdn.microsoft.com/en-us/library/windows/apps/ms679351.aspx)                      | Introduced into api-ms-win-core-localization-l1-2-1.dll in Windows 10.0.10240.0 |
| [**GetCalendarInfoEx**](https://msdn.microsoft.com/en-us/library/windows/apps/dd318075.aspx)               | Introduced into api-ms-win-core-localization-l1-2-1.dll in Windows 10.0.10240.0 |
| [**GetCPInfo**](https://msdn.microsoft.com/en-us/library/windows/apps/dd318078.aspx)                               | Introduced into api-ms-win-core-localization-l1-2-1.dll in Windows 10.0.10240.0 |
| [**GetCPInfoExW**](https://msdn.microsoft.com/en-us/library/windows/apps/dd318081.aspx)                          | Introduced into api-ms-win-core-localization-l1-2-1.dll in Windows 10.0.10240.0 |
| [**GetGeoInfoW**](https://msdn.microsoft.com/en-us/library/windows/apps/dd318099.aspx)                            | Introduced into api-ms-win-core-localization-l1-2-1.dll in Windows 10.0.10240.0 |
| [**GetLocaleInfoEx**](https://msdn.microsoft.com/en-us/library/windows/apps/dd318103.aspx)                   | Introduced into api-ms-win-core-localization-l1-2-1.dll in Windows 10.0.10240.0 |
| [**GetNLSVersionEx**](https://msdn.microsoft.com/en-us/library/windows/apps/dd318107.aspx)                   | Introduced into api-ms-win-core-localization-l1-2-1.dll in Windows 10.0.10240.0 |
| [**GetUserDefaultLocaleName**](https://msdn.microsoft.com/en-us/library/windows/apps/dd318136.aspx) | Introduced into api-ms-win-core-localization-l1-2-1.dll in Windows 10.0.10240.0 |
| [**GetUserGeoID**](https://msdn.microsoft.com/en-us/library/windows/apps/dd318138.aspx)                         | Introduced into api-ms-win-core-localization-l1-2-1.dll in Windows 10.0.10240.0 |
| [**IdnToAscii**](https://msdn.microsoft.com/en-us/library/windows/apps/dd318149.aspx)                             | Introduced into api-ms-win-core-localization-l1-2-1.dll in Windows 10.0.10240.0 |
| [**IdnToUnicode**](https://msdn.microsoft.com/en-us/library/windows/apps/dd318151.aspx)                         | Introduced into api-ms-win-core-localization-l1-2-1.dll in Windows 10.0.10240.0 |
| [**IsValidCodePage**](https://msdn.microsoft.com/en-us/library/windows/apps/dd318674.aspx)                   | Introduced into api-ms-win-core-localization-l1-2-1.dll in Windows 10.0.10240.0 |
| [**IsValidLocaleName**](https://msdn.microsoft.com/en-us/library/windows/apps/dd318681.aspx)               | Introduced into api-ms-win-core-localization-l1-2-1.dll in Windows 10.0.10240.0 |
| [**IsValidNLSVersion**](https://msdn.microsoft.com/en-us/library/windows/apps/hh706739.aspx)               | Introduced into api-ms-win-core-localization-l1-2-1.dll in Windows 10.0.10240.0 |
| [**LCMapStringEx**](https://msdn.microsoft.com/en-us/library/windows/apps/dd318702.aspx)                       | Introduced into api-ms-win-core-localization-l1-2-1.dll in Windows 10.0.10240.0 |
| [**LocaleNameToLCID**](https://msdn.microsoft.com/en-us/library/windows/apps/dd318711.aspx)                 | Introduced into api-ms-win-core-localization-l1-2-1.dll in Windows 10.0.10240.0 |
| [**ResolveLocaleName**](https://msdn.microsoft.com/en-us/library/windows/apps/dd319112.aspx)               | Introduced into api-ms-win-core-localization-l1-2-1.dll in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-core-localization-l1-2-2.dll"></span><span id="_API-MS-WIN-CORE-LOCALIZATION-L1-2-2.DLL"></span>APIs from the API Set api-ms-win-core-localization-l1-2-2.dll


| API                                                               | Requirements                                                                    |
|-------------------------------------------------------------------|---------------------------------------------------------------------------------|
| [**GetSystemDefaultLocaleName**](https://msdn.microsoft.com/en-us/library/windows/apps/dd318122.aspx) | Introduced into api-ms-win-core-localization-l1-2-2.dll in Windows 10.0.10240.0 |
| [**LCIDToLocaleName**](https://msdn.microsoft.com/en-us/library/windows/apps/dd318698.aspx)                     | Introduced into api-ms-win-core-localization-l1-2-2.dll in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-core-localization-l2-1-0.dll"></span><span id="_API-MS-WIN-CORE-LOCALIZATION-L2-1-0.DLL"></span>APIs from the API Set api-ms-win-core-localization-l2-1-0.dll


| API                                                   | Requirements                                                                    |
|-------------------------------------------------------|---------------------------------------------------------------------------------|
| [**EnumCalendarInfoExEx**](https://msdn.microsoft.com/en-us/library/windows/apps/dd317805.aspx) | Introduced into api-ms-win-core-localization-l2-1-0.dll in Windows 10.0.10240.0 |
| [**EnumDateFormatsExEx**](https://msdn.microsoft.com/en-us/library/windows/apps/dd317812.aspx)   | Introduced into api-ms-win-core-localization-l2-1-0.dll in Windows 10.0.10240.0 |
| [**EnumSystemCodePagesW**](https://msdn.microsoft.com/en-us/library/windows/apps/dd317825.aspx)  | Introduced into api-ms-win-core-localization-l2-1-0.dll in Windows 10.0.10240.0 |
| [**EnumTimeFormatsEx**](https://msdn.microsoft.com/en-us/library/windows/apps/dd317831.aspx)       | Introduced into api-ms-win-core-localization-l2-1-0.dll in Windows 10.0.10240.0 |
| [**GetCurrencyFormatEx**](https://msdn.microsoft.com/en-us/library/windows/apps/dd318084.aspx)   | Introduced into api-ms-win-core-localization-l2-1-0.dll in Windows 10.0.10240.0 |
| [**GetNumberFormatEx**](https://msdn.microsoft.com/en-us/library/windows/apps/dd318113.aspx)       | Introduced into api-ms-win-core-localization-l2-1-0.dll in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-core-memory-l1-1-2.dll"></span><span id="_API-MS-WIN-CORE-MEMORY-L1-1-2.DLL"></span>APIs from the API Set api-ms-win-core-memory-l1-1-2.dll


| API                                                           | Requirements                                                              |
|---------------------------------------------------------------|---------------------------------------------------------------------------|
| [**CreateFileMappingFromApp**](https://msdn.microsoft.com/en-us/library/windows/apps/hh994453.aspx) | Introduced into api-ms-win-core-memory-l1-1-2.dll in Windows 10.0.10240.0 |
| [**DiscardVirtualMemory**](https://msdn.microsoft.com/en-us/library/windows/apps/dn781432.aspx)         | Introduced into api-ms-win-core-memory-l1-1-2.dll in Windows 10.0.10240.0 |
| [**FlushViewOfFile**](https://msdn.microsoft.com/en-us/library/windows/apps/aa366563.aspx)                   | Introduced into api-ms-win-core-memory-l1-1-2.dll in Windows 10.0.10240.0 |
| [**GetWriteWatch**](https://msdn.microsoft.com/en-us/library/windows/apps/aa366573.aspx)                       | Introduced into api-ms-win-core-memory-l1-1-2.dll in Windows 10.0.10240.0 |
| [**MapViewOfFileFromApp**](https://msdn.microsoft.com/en-us/library/windows/apps/hh994454.aspx)         | Introduced into api-ms-win-core-memory-l1-1-2.dll in Windows 10.0.10240.0 |
| [**OfferVirtualMemory**](https://msdn.microsoft.com/en-us/library/windows/apps/dn781436.aspx)             | Introduced into api-ms-win-core-memory-l1-1-2.dll in Windows 10.0.10240.0 |
| [**ReclaimVirtualMemory**](https://msdn.microsoft.com/en-us/library/windows/apps/dn781437.aspx)         | Introduced into api-ms-win-core-memory-l1-1-2.dll in Windows 10.0.10240.0 |
| [**ResetWriteWatch**](https://msdn.microsoft.com/en-us/library/windows/apps/aa366874.aspx)                   | Introduced into api-ms-win-core-memory-l1-1-2.dll in Windows 10.0.10240.0 |
| [**UnmapViewOfFile**](https://msdn.microsoft.com/en-us/library/windows/apps/aa366882.aspx)                   | Introduced into api-ms-win-core-memory-l1-1-2.dll in Windows 10.0.10240.0 |
| [**VirtualFree**](https://msdn.microsoft.com/en-us/library/windows/apps/aa366892.aspx)                           | Introduced into api-ms-win-core-memory-l1-1-2.dll in Windows 10.0.10240.0 |
| [**VirtualQuery**](https://msdn.microsoft.com/en-us/library/windows/apps/aa366902.aspx)                         | Introduced into api-ms-win-core-memory-l1-1-2.dll in Windows 10.0.10240.0 |
| [**UnmapViewOfFileEx**](https://msdn.microsoft.com/en-us/library/windows/apps/mt670639.aspx)               | Introduced into api-ms-win-core-memory-l1-1-2.dll in Windows 10.0.14393.0 |

 

## <span id="_api-ms-win-core-memory-l1-1-3.dll"></span><span id="_API-MS-WIN-CORE-MEMORY-L1-1-3.DLL"></span>APIs from the API Set api-ms-win-core-memory-l1-1-3.dll


| API                                                       | Requirements                                                              |
|-----------------------------------------------------------|---------------------------------------------------------------------------|
| [**OpenFileMappingFromApp**](https://msdn.microsoft.com/en-us/library/windows/apps/mt169844.aspx) | Introduced into api-ms-win-core-memory-l1-1-3.dll in Windows 10.0.10240.0 |
| [**VirtualAllocFromApp**](https://msdn.microsoft.com/en-us/library/windows/apps/mt169845.aspx)       | Introduced into api-ms-win-core-memory-l1-1-3.dll in Windows 10.0.10240.0 |
| [**VirtualProtectFromApp**](https://msdn.microsoft.com/en-us/library/windows/apps/mt169846.aspx)   | Introduced into api-ms-win-core-memory-l1-1-3.dll in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-core-normalization-l1-1-0.dll"></span><span id="_API-MS-WIN-CORE-NORMALIZATION-L1-1-0.DLL"></span>APIs from the API Set api-ms-win-core-normalization-l1-1-0.dll


| API                                                   | Requirements                                                                     |
|-------------------------------------------------------|----------------------------------------------------------------------------------|
| [**GetStringScripts**](https://msdn.microsoft.com/en-us/library/windows/apps/dd318116.aspx)         | Introduced into api-ms-win-core-normalization-l1-1-0.dll in Windows 10.0.10240.0 |
| [**IdnToNameprepUnicode**](https://msdn.microsoft.com/en-us/library/windows/apps/dd318150.aspx) | Introduced into api-ms-win-core-normalization-l1-1-0.dll in Windows 10.0.10240.0 |
| [**IsNormalizedString**](https://msdn.microsoft.com/en-us/library/windows/apps/dd318671.aspx)     | Introduced into api-ms-win-core-normalization-l1-1-0.dll in Windows 10.0.10240.0 |
| [**NormalizeString**](https://msdn.microsoft.com/en-us/library/windows/apps/dd319093.aspx)           | Introduced into api-ms-win-core-normalization-l1-1-0.dll in Windows 10.0.10240.0 |
| [**VerifyScripts**](https://msdn.microsoft.com/en-us/library/windows/apps/dd374129.aspx)               | Introduced into api-ms-win-core-normalization-l1-1-0.dll in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-core-processenvironment-l1-2-0.dll"></span><span id="_API-MS-WIN-CORE-PROCESSENVIRONMENT-L1-2-0.DLL"></span>APIs from the API Set api-ms-win-core-processenvironment-l1-2-0.dll


| API                                                | Requirements                                                                          |
|----------------------------------------------------|---------------------------------------------------------------------------------------|
| [**GetCommandLineA**](https://msdn.microsoft.com/en-us/library/windows/apps/ms683156.aspx)         | Introduced into api-ms-win-core-processenvironment-l1-2-0.dll in Windows 10.0.10240.0 |
| [**GetCommandLineW**](https://msdn.microsoft.com/en-us/library/windows/apps/ms683156.aspx)         | Introduced into api-ms-win-core-processenvironment-l1-2-0.dll in Windows 10.0.10240.0 |
| [**GetCurrentDirectoryW**](https://msdn.microsoft.com/en-us/library/windows/apps/aa364934.aspx) | Introduced into api-ms-win-core-processenvironment-l1-2-0.dll in Windows 10.0.10240.0 |
| [**SetCurrentDirectoryW**](https://msdn.microsoft.com/en-us/library/windows/apps/aa365530.aspx) | Introduced into api-ms-win-core-processenvironment-l1-2-0.dll in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-core-processthreads-l1-1-2.dll"></span><span id="_API-MS-WIN-CORE-PROCESSTHREADS-L1-1-2.DLL"></span>APIs from the API Set api-ms-win-core-processthreads-l1-1-2.dll


| API                                                             | Requirements                                                                      |
|-----------------------------------------------------------------|-----------------------------------------------------------------------------------|
| [**CreateThread**](https://msdn.microsoft.com/en-us/library/windows/apps/ms682453.aspx)                           | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in Windows 10.0.10240.0 |
| [**ExitThread**](https://msdn.microsoft.com/en-us/library/windows/apps/ms682659.aspx)                               | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in Windows 10.0.10240.0 |
| [**FlushProcessWriteBuffers**](https://msdn.microsoft.com/en-us/library/windows/apps/ms683148.aspx)   | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in Windows 10.0.10240.0 |
| [**GetCurrentProcess**](https://msdn.microsoft.com/en-us/library/windows/apps/ms683179.aspx)                 | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in Windows 10.0.10240.0 |
| [**GetCurrentProcessId**](https://msdn.microsoft.com/en-us/library/windows/apps/ms683180.aspx)             | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in Windows 10.0.10240.0 |
| [**GetCurrentThread**](https://msdn.microsoft.com/en-us/library/windows/apps/ms683182.aspx)                   | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in Windows 10.0.10240.0 |
| [**GetCurrentThreadId**](https://msdn.microsoft.com/en-us/library/windows/apps/ms683183.aspx)               | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in Windows 10.0.10240.0 |
| [**GetExitCodeThread**](https://msdn.microsoft.com/en-us/library/windows/apps/ms683190.aspx)                 | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in Windows 10.0.10240.0 |
| [**GetThreadContext**](https://msdn.microsoft.com/en-us/library/windows/apps/ms679362.aspx)                   | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in Windows 10.0.10240.0 |
| [**GetThreadId**](https://msdn.microsoft.com/en-us/library/windows/apps/ms683233.aspx)                             | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in Windows 10.0.10240.0 |
| [**GetThreadPriority**](https://msdn.microsoft.com/en-us/library/windows/apps/ms683235.aspx)                 | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in Windows 10.0.10240.0 |
| [**IsProcessorFeaturePresent**](https://msdn.microsoft.com/en-us/library/windows/apps/ms724482.aspx) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in Windows 10.0.10240.0 |
| [**OpenProcess**](https://msdn.microsoft.com/en-us/library/windows/apps/ms684320.aspx)                             | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in Windows 10.0.10240.0 |
| [**QueueUserAPC**](https://msdn.microsoft.com/en-us/library/windows/apps/ms684954.aspx)                           | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in Windows 10.0.10240.0 |
| [**ResumeThread**](https://msdn.microsoft.com/en-us/library/windows/apps/ms685086.aspx)                           | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in Windows 10.0.10240.0 |
| [**SetThreadIdealProcessorEx**](https://msdn.microsoft.com/en-us/library/windows/apps/dd405517.aspx) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in Windows 10.0.10240.0 |
| [**SetThreadPriority**](https://msdn.microsoft.com/en-us/library/windows/apps/ms686277.aspx)                 | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in Windows 10.0.10240.0 |
| [**SuspendThread**](https://msdn.microsoft.com/en-us/library/windows/apps/ms686345.aspx)                         | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in Windows 10.0.10240.0 |
| [**SwitchToThread**](https://msdn.microsoft.com/en-us/library/windows/apps/ms686352.aspx)                       | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in Windows 10.0.10240.0 |
| [**TerminateProcess**](https://msdn.microsoft.com/en-us/library/windows/apps/ms686714.aspx)                   | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in Windows 10.0.10240.0 |
| [**TlsAlloc**](https://msdn.microsoft.com/en-us/library/windows/apps/ms686801.aspx)                                   | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in Windows 10.0.14393.0 |
| [**TlsFree**](https://msdn.microsoft.com/en-us/library/windows/apps/ms686804.aspx)                                     | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in Windows 10.0.14393.0 |
| [**TlsGetValue**](https://msdn.microsoft.com/en-us/library/windows/apps/ms686812.aspx)                             | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in Windows 10.0.14393.0 |
| [**TlsSetValue**](https://msdn.microsoft.com/en-us/library/windows/apps/ms686818.aspx)                             | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in Windows 10.0.14393.0 |

 

## <span id="_api-ms-win-core-processthreads-l1-1-3.dll"></span><span id="_API-MS-WIN-CORE-PROCESSTHREADS-L1-1-3.DLL"></span>APIs from the API Set api-ms-win-core-processthreads-l1-1-3.dll


| API                                                               | Requirements                                                                      |
|-------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| [**GetProcessDefaultCpuSets**](https://msdn.microsoft.com/en-us/library/windows/apps/mt186424.aspx)     | Introduced into api-ms-win-core-processthreads-l1-1-3.dll in Windows 10.0.10240.0 |
| [**GetProcessInformation**](https://msdn.microsoft.com/en-us/library/windows/apps/hh448381.aspx)           | Introduced into api-ms-win-core-processthreads-l1-1-3.dll in Windows 10.0.10240.0 |
| [**GetSystemCpuSetInformation**](https://msdn.microsoft.com/en-us/library/windows/apps/mt186425.aspx) | Introduced into api-ms-win-core-processthreads-l1-1-3.dll in Windows 10.0.10240.0 |
| [**GetThreadSelectedCpuSets**](https://msdn.microsoft.com/en-us/library/windows/apps/mt186426.aspx)     | Introduced into api-ms-win-core-processthreads-l1-1-3.dll in Windows 10.0.10240.0 |
| [**SetProcessDefaultCpuSets**](https://msdn.microsoft.com/en-us/library/windows/apps/mt186427.aspx)     | Introduced into api-ms-win-core-processthreads-l1-1-3.dll in Windows 10.0.10240.0 |
| [**SetProcessInformation**](https://msdn.microsoft.com/en-us/library/windows/apps/hh448389.aspx)           | Introduced into api-ms-win-core-processthreads-l1-1-3.dll in Windows 10.0.10240.0 |
| [**SetThreadIdealProcessor**](https://msdn.microsoft.com/en-us/library/windows/apps/ms686253.aspx)       | Introduced into api-ms-win-core-processthreads-l1-1-3.dll in Windows 10.0.10240.0 |
| [**SetThreadSelectedCpuSets**](https://msdn.microsoft.com/en-us/library/windows/apps/mt186428.aspx)     | Introduced into api-ms-win-core-processthreads-l1-1-3.dll in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-core-profile-l1-1-0.dll"></span><span id="_API-MS-WIN-CORE-PROFILE-L1-1-0.DLL"></span>APIs from the API Set api-ms-win-core-profile-l1-1-0.dll


| API                                                             | Requirements                                                               |
|-----------------------------------------------------------------|----------------------------------------------------------------------------|
| [**QueryPerformanceCounter**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644904.aspx)     | Introduced into api-ms-win-core-profile-l1-1-0.dll in Windows 10.0.10240.0 |
| [**QueryPerformanceFrequency**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644905.aspx) | Introduced into api-ms-win-core-profile-l1-1-0.dll in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-core-realtime-l1-1-0.dll"></span><span id="_API-MS-WIN-CORE-REALTIME-L1-1-0.DLL"></span>APIs from the API Set api-ms-win-core-realtime-l1-1-0.dll


| API                                                               | Requirements                                                                |
|-------------------------------------------------------------------|-----------------------------------------------------------------------------|
| [**QueryUnbiasedInterruptTime**](https://msdn.microsoft.com/en-us/library/windows/apps/ee662307.aspx) | Introduced into api-ms-win-core-realtime-l1-1-0.dll in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-core-realtime-l1-1-1.dll"></span><span id="_API-MS-WIN-CORE-REALTIME-L1-1-1.DLL"></span>APIs from the API Set api-ms-win-core-realtime-l1-1-1.dll


| API                                                                             | Requirements                                                                |
|---------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| [**QueryInterruptTime**](https://msdn.microsoft.com/en-us/library/windows/apps/dn903659.aspx)                               | Introduced into api-ms-win-core-realtime-l1-1-1.dll in Windows 10.0.10240.0 |
| [**QueryInterruptTimePrecise**](https://msdn.microsoft.com/en-us/library/windows/apps/dn903660.aspx)                 | Introduced into api-ms-win-core-realtime-l1-1-1.dll in Windows 10.0.10240.0 |
| [**QueryUnbiasedInterruptTimePrecise**](https://msdn.microsoft.com/en-us/library/windows/apps/dn891448.aspx) | Introduced into api-ms-win-core-realtime-l1-1-1.dll in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-core-rtlsupport-l1-2-0.dll"></span><span id="_API-MS-WIN-CORE-RTLSUPPORT-L1-2-0.DLL"></span>APIs from the API Set api-ms-win-core-rtlsupport-l1-2-0.dll


| API                                                                                    | Requirements                                                                  |
|----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| [**RtlCaptureStackBackTrace**](https://www.bing.com/search?q=RtlCaptureStackBackTrace) | Introduced into api-ms-win-core-rtlsupport-l1-2-0.dll in Windows 10.0.10240.0 |
| [**RtlLookupFunctionEntry**](https://msdn.microsoft.com/en-us/library/windows/apps/ms680597.aspx)                              | Introduced into api-ms-win-core-rtlsupport-l1-2-0.dll in Windows 10.0.10240.0 |
| [**RtlPcToFileHeader**](https://msdn.microsoft.com/en-us/library/windows/apps/ms680603.aspx)                                        | Introduced into api-ms-win-core-rtlsupport-l1-2-0.dll in Windows 10.0.10240.0 |
| [**RtlUnwind**](https://msdn.microsoft.com/en-us/library/windows/apps/ms680609.aspx)                                                        | Introduced into api-ms-win-core-rtlsupport-l1-2-0.dll in Windows 10.0.10240.0 |
| [**RtlUnwindEx**](https://msdn.microsoft.com/en-us/library/windows/apps/ms680615.aspx)                                                    | Introduced into api-ms-win-core-rtlsupport-l1-2-0.dll in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-core-string-l1-1-0.dll"></span><span id="_API-MS-WIN-CORE-STRING-L1-1-0.DLL"></span>APIs from the API Set api-ms-win-core-string-l1-1-0.dll


| API                                                   | Requirements                                                              |
|-------------------------------------------------------|---------------------------------------------------------------------------|
| [**CompareStringEx**](https://msdn.microsoft.com/en-us/library/windows/apps/dd317761.aspx)           | Introduced into api-ms-win-core-string-l1-1-0.dll in Windows 10.0.10240.0 |
| [**CompareStringOrdinal**](https://msdn.microsoft.com/en-us/library/windows/apps/dd317762.aspx) | Introduced into api-ms-win-core-string-l1-1-0.dll in Windows 10.0.10240.0 |
| [**GetStringTypeExW**](https://msdn.microsoft.com/en-us/library/windows/apps/dd318118.aspx)          | Introduced into api-ms-win-core-string-l1-1-0.dll in Windows 10.0.10240.0 |
| [**GetStringTypeW**](https://msdn.microsoft.com/en-us/library/windows/apps/dd318119.aspx)             | Introduced into api-ms-win-core-string-l1-1-0.dll in Windows 10.0.10240.0 |
| [**MultiByteToWideChar**](https://msdn.microsoft.com/en-us/library/windows/apps/dd319072.aspx)   | Introduced into api-ms-win-core-string-l1-1-0.dll in Windows 10.0.10240.0 |
| [**WideCharToMultiByte**](https://msdn.microsoft.com/en-us/library/windows/apps/dd374130.aspx)   | Introduced into api-ms-win-core-string-l1-1-0.dll in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-core-synch-ansi-l1-1-0.dll"></span><span id="_API-MS-WIN-CORE-SYNCH-ANSI-L1-1-0.DLL"></span>APIs from the API Set api-ms-win-core-synch-ansi-l1-1-0.dll


| API                                              | Requirements                                                                  |
|--------------------------------------------------|-------------------------------------------------------------------------------|
| [**CreateSemaphoreA**](https://msdn.microsoft.com/en-us/library/windows/apps/ms682438.aspx)     | Introduced into api-ms-win-core-synch-ansi-l1-1-0.dll in Windows 10.0.10240.0 |
| [**CreateSemaphoreExA**](https://msdn.microsoft.com/en-us/library/windows/apps/ms682446.aspx) | Introduced into api-ms-win-core-synch-ansi-l1-1-0.dll in Windows 10.0.10240.0 |
| [**OpenMutexA**](https://msdn.microsoft.com/en-us/library/windows/apps/ms684315.aspx)                 | Introduced into api-ms-win-core-synch-ansi-l1-1-0.dll in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-core-synch-l1-2-0.dll"></span><span id="_API-MS-WIN-CORE-SYNCH-L1-2-0.DLL"></span>APIs from the API Set api-ms-win-core-synch-l1-2-0.dll


| API                                                                                     | Requirements                                                             |
|-----------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| [**AcquireSRWLockExclusive**](https://msdn.microsoft.com/en-us/library/windows/apps/ms681930.aspx)                             | Introduced into api-ms-win-core-synch-l1-2-0.dll in Windows 10.0.10240.0 |
| [**AcquireSRWLockShared**](https://msdn.microsoft.com/en-us/library/windows/apps/ms681934.aspx)                                   | Introduced into api-ms-win-core-synch-l1-2-0.dll in Windows 10.0.10240.0 |
| [**CreateEventA**](https://msdn.microsoft.com/en-us/library/windows/apps/ms682396.aspx)                                                    | Introduced into api-ms-win-core-synch-l1-2-0.dll in Windows 10.0.10240.0 |
| [**CreateEventExA**](https://msdn.microsoft.com/en-us/library/windows/apps/ms682400.aspx)                                                | Introduced into api-ms-win-core-synch-l1-2-0.dll in Windows 10.0.10240.0 |
| [**CreateEventExW**](https://msdn.microsoft.com/en-us/library/windows/apps/ms682400.aspx)                                                | Introduced into api-ms-win-core-synch-l1-2-0.dll in Windows 10.0.10240.0 |
| [**CreateEventW**](https://msdn.microsoft.com/en-us/library/windows/apps/ms682396.aspx)                                                    | Introduced into api-ms-win-core-synch-l1-2-0.dll in Windows 10.0.10240.0 |
| [**CreateMutexA**](https://msdn.microsoft.com/en-us/library/windows/apps/ms682411.aspx)                                                    | Introduced into api-ms-win-core-synch-l1-2-0.dll in Windows 10.0.10240.0 |
| [**CreateMutexExA**](https://msdn.microsoft.com/en-us/library/windows/apps/ms682418.aspx)                                                | Introduced into api-ms-win-core-synch-l1-2-0.dll in Windows 10.0.10240.0 |
| [**CreateMutexExW**](https://msdn.microsoft.com/en-us/library/windows/apps/ms682418.aspx)                                                | Introduced into api-ms-win-core-synch-l1-2-0.dll in Windows 10.0.10240.0 |
| [**CreateMutexW**](https://msdn.microsoft.com/en-us/library/windows/apps/ms682411.aspx)                                                    | Introduced into api-ms-win-core-synch-l1-2-0.dll in Windows 10.0.10240.0 |
| [**CreateSemaphoreExW**](https://msdn.microsoft.com/en-us/library/windows/apps/ms682446.aspx)                                        | Introduced into api-ms-win-core-synch-l1-2-0.dll in Windows 10.0.10240.0 |
| [**DeleteCriticalSection**](https://msdn.microsoft.com/en-us/library/windows/apps/ms682552.aspx)                                 | Introduced into api-ms-win-core-synch-l1-2-0.dll in Windows 10.0.10240.0 |
| [**EnterCriticalSection**](https://msdn.microsoft.com/en-us/library/windows/apps/ms682608.aspx)                                   | Introduced into api-ms-win-core-synch-l1-2-0.dll in Windows 10.0.10240.0 |
| [**InitializeConditionVariable**](https://msdn.microsoft.com/en-us/library/windows/apps/ms683469.aspx)                     | Introduced into api-ms-win-core-synch-l1-2-0.dll in Windows 10.0.10240.0 |
| [**InitializeCriticalSection**](https://msdn.microsoft.com/en-us/library/windows/apps/ms683472.aspx)                         | Introduced into api-ms-win-core-synch-l1-2-0.dll in Windows 10.0.10240.0 |
| [**InitializeCriticalSectionAndSpinCount**](https://msdn.microsoft.com/en-us/library/windows/apps/ms683476.aspx) | Introduced into api-ms-win-core-synch-l1-2-0.dll in Windows 10.0.10240.0 |
| [**InitializeCriticalSectionEx**](https://msdn.microsoft.com/en-us/library/windows/apps/ms683477.aspx)                     | Introduced into api-ms-win-core-synch-l1-2-0.dll in Windows 10.0.10240.0 |
| [**InitializeSRWLock**](https://msdn.microsoft.com/en-us/library/windows/apps/ms683483.aspx)                                         | Introduced into api-ms-win-core-synch-l1-2-0.dll in Windows 10.0.10240.0 |
| [**InitOnceBeginInitialize**](https://msdn.microsoft.com/en-us/library/windows/apps/ms683487.aspx)                             | Introduced into api-ms-win-core-synch-l1-2-0.dll in Windows 10.0.10240.0 |
| [**InitOnceComplete**](https://msdn.microsoft.com/en-us/library/windows/apps/ms683491.aspx)                                           | Introduced into api-ms-win-core-synch-l1-2-0.dll in Windows 10.0.10240.0 |
| [**InitOnceExecuteOnce**](https://msdn.microsoft.com/en-us/library/windows/apps/ms683493.aspx)                                     | Introduced into api-ms-win-core-synch-l1-2-0.dll in Windows 10.0.10240.0 |
| [**InitOnceInitialize**](https://msdn.microsoft.com/en-us/library/windows/apps/ms683495.aspx)                                       | Introduced into api-ms-win-core-synch-l1-2-0.dll in Windows 10.0.10240.0 |
| [**LeaveCriticalSection**](https://msdn.microsoft.com/en-us/library/windows/apps/ms684169.aspx)                                   | Introduced into api-ms-win-core-synch-l1-2-0.dll in Windows 10.0.10240.0 |
| [**OpenEventA**](https://msdn.microsoft.com/en-us/library/windows/apps/ms684305.aspx)                                                        | Introduced into api-ms-win-core-synch-l1-2-0.dll in Windows 10.0.10240.0 |
| [**OpenEventW**](https://msdn.microsoft.com/en-us/library/windows/apps/ms684305.aspx)                                                        | Introduced into api-ms-win-core-synch-l1-2-0.dll in Windows 10.0.10240.0 |
| [**OpenMutexW**](https://msdn.microsoft.com/en-us/library/windows/apps/ms684315.aspx)                                                        | Introduced into api-ms-win-core-synch-l1-2-0.dll in Windows 10.0.10240.0 |
| [**OpenSemaphoreW**](https://msdn.microsoft.com/en-us/library/windows/apps/ms684326.aspx)                                                | Introduced into api-ms-win-core-synch-l1-2-0.dll in Windows 10.0.10240.0 |
| [**ReleaseMutex**](https://msdn.microsoft.com/en-us/library/windows/apps/ms685066.aspx)                                                   | Introduced into api-ms-win-core-synch-l1-2-0.dll in Windows 10.0.10240.0 |
| [**ReleaseSemaphore**](https://msdn.microsoft.com/en-us/library/windows/apps/ms685071.aspx)                                           | Introduced into api-ms-win-core-synch-l1-2-0.dll in Windows 10.0.10240.0 |
| [**ReleaseSRWLockExclusive**](https://msdn.microsoft.com/en-us/library/windows/apps/ms685076.aspx)                             | Introduced into api-ms-win-core-synch-l1-2-0.dll in Windows 10.0.10240.0 |
| [**ReleaseSRWLockShared**](https://msdn.microsoft.com/en-us/library/windows/apps/ms685080.aspx)                                   | Introduced into api-ms-win-core-synch-l1-2-0.dll in Windows 10.0.10240.0 |
| [**ResetEvent**](https://msdn.microsoft.com/en-us/library/windows/apps/ms685081.aspx)                                                       | Introduced into api-ms-win-core-synch-l1-2-0.dll in Windows 10.0.10240.0 |
| [**SetCriticalSectionSpinCount**](https://msdn.microsoft.com/en-us/library/windows/apps/ms686197.aspx)                     | Introduced into api-ms-win-core-synch-l1-2-0.dll in Windows 10.0.10240.0 |
| [**SetEvent**](https://msdn.microsoft.com/en-us/library/windows/apps/ms686211.aspx)                                                           | Introduced into api-ms-win-core-synch-l1-2-0.dll in Windows 10.0.10240.0 |
| [**Sleep**](https://msdn.microsoft.com/en-us/library/windows/apps/ms686298.aspx)                                                                 | Introduced into api-ms-win-core-synch-l1-2-0.dll in Windows 10.0.10240.0 |
| [**SleepConditionVariableCS**](https://msdn.microsoft.com/en-us/library/windows/apps/ms686301.aspx)                           | Introduced into api-ms-win-core-synch-l1-2-0.dll in Windows 10.0.10240.0 |
| [**SleepConditionVariableSRW**](https://msdn.microsoft.com/en-us/library/windows/apps/ms686304.aspx)                         | Introduced into api-ms-win-core-synch-l1-2-0.dll in Windows 10.0.10240.0 |
| [**SleepEx**](https://msdn.microsoft.com/en-us/library/windows/apps/ms686307.aspx)                                                             | Introduced into api-ms-win-core-synch-l1-2-0.dll in Windows 10.0.10240.0 |
| [**TryAcquireSRWLockExclusive**](https://msdn.microsoft.com/en-us/library/windows/apps/dd405523.aspx)                       | Introduced into api-ms-win-core-synch-l1-2-0.dll in Windows 10.0.10240.0 |
| [**TryAcquireSRWLockShared**](https://msdn.microsoft.com/en-us/library/windows/apps/dd405524.aspx)                             | Introduced into api-ms-win-core-synch-l1-2-0.dll in Windows 10.0.10240.0 |
| [**TryEnterCriticalSection**](https://msdn.microsoft.com/en-us/library/windows/apps/ms686857.aspx)                             | Introduced into api-ms-win-core-synch-l1-2-0.dll in Windows 10.0.10240.0 |
| [**WaitForMultipleObjectsEx**](https://msdn.microsoft.com/en-us/library/windows/apps/ms687028.aspx)                           | Introduced into api-ms-win-core-synch-l1-2-0.dll in Windows 10.0.10240.0 |
| [**WaitForSingleObject**](https://msdn.microsoft.com/en-us/library/windows/apps/ms687032.aspx)                                     | Introduced into api-ms-win-core-synch-l1-2-0.dll in Windows 10.0.10240.0 |
| [**WaitForSingleObjectEx**](https://msdn.microsoft.com/en-us/library/windows/apps/ms687036.aspx)                                 | Introduced into api-ms-win-core-synch-l1-2-0.dll in Windows 10.0.10240.0 |
| [**WaitOnAddress**](https://msdn.microsoft.com/en-us/library/windows/apps/hh706898.aspx)                                                 | Introduced into api-ms-win-core-synch-l1-2-0.dll in Windows 10.0.10240.0 |
| [**WakeAllConditionVariable**](https://msdn.microsoft.com/en-us/library/windows/apps/ms687076.aspx)                           | Introduced into api-ms-win-core-synch-l1-2-0.dll in Windows 10.0.10240.0 |
| [**WakeByAddressAll**](https://msdn.microsoft.com/en-us/library/windows/apps/hh706899.aspx)                                           | Introduced into api-ms-win-core-synch-l1-2-0.dll in Windows 10.0.10240.0 |
| [**WakeByAddressSingle**](https://msdn.microsoft.com/en-us/library/windows/apps/hh706900.aspx)                                     | Introduced into api-ms-win-core-synch-l1-2-0.dll in Windows 10.0.10240.0 |
| [**WakeConditionVariable**](https://msdn.microsoft.com/en-us/library/windows/apps/ms687080.aspx)                                 | Introduced into api-ms-win-core-synch-l1-2-0.dll in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-core-synch-l1-2-1.dll"></span><span id="_API-MS-WIN-CORE-SYNCH-L1-2-1.DLL"></span>APIs from the API Set api-ms-win-core-synch-l1-2-1.dll


| API                                                       | Requirements                                                             |
|-----------------------------------------------------------|--------------------------------------------------------------------------|
| [**CreateSemaphoreW**](https://msdn.microsoft.com/en-us/library/windows/apps/ms682438.aspx)              | Introduced into api-ms-win-core-synch-l1-2-1.dll in Windows 10.0.10240.0 |
| [**WaitForMultipleObjects**](https://msdn.microsoft.com/en-us/library/windows/apps/ms687025.aspx) | Introduced into api-ms-win-core-synch-l1-2-1.dll in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-core-sysinfo-l1-2-1.dll"></span><span id="_API-MS-WIN-CORE-SYSINFO-L1-2-1.DLL"></span>APIs from the API Set api-ms-win-core-sysinfo-l1-2-1.dll


| API                                                                           | Requirements                                                               |
|-------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| [**GetLocalTime**](https://msdn.microsoft.com/en-us/library/windows/apps/ms724338.aspx)                                         | Introduced into api-ms-win-core-sysinfo-l1-2-1.dll in Windows 10.0.10240.0 |
| [**GetNativeSystemInfo**](https://msdn.microsoft.com/en-us/library/windows/apps/ms724340.aspx)                           | Introduced into api-ms-win-core-sysinfo-l1-2-1.dll in Windows 10.0.10240.0 |
| [**GetSystemInfo**](https://msdn.microsoft.com/en-us/library/windows/apps/ms724381.aspx)                                       | Introduced into api-ms-win-core-sysinfo-l1-2-1.dll in Windows 10.0.10240.0 |
| [**GetSystemTime**](https://msdn.microsoft.com/en-us/library/windows/apps/ms724390.aspx)                                       | Introduced into api-ms-win-core-sysinfo-l1-2-1.dll in Windows 10.0.10240.0 |
| [**GetSystemTimeAsFileTime**](https://msdn.microsoft.com/en-us/library/windows/apps/ms724397.aspx)                   | Introduced into api-ms-win-core-sysinfo-l1-2-1.dll in Windows 10.0.10240.0 |
| [**GetSystemTimePreciseAsFileTime**](https://msdn.microsoft.com/en-us/library/windows/apps/hh706895.aspx)     | Introduced into api-ms-win-core-sysinfo-l1-2-1.dll in Windows 10.0.10240.0 |
| [**GetTickCount64**](https://msdn.microsoft.com/en-us/library/windows/apps/ms724411.aspx)                                     | Introduced into api-ms-win-core-sysinfo-l1-2-1.dll in Windows 10.0.10240.0 |
| [**GetLogicalProcessorInformation**](https://msdn.microsoft.com/en-us/library/windows/apps/ms683194.aspx)     | Introduced into api-ms-win-core-sysinfo-l1-2-1.dll in Windows 10.0.14393.0 |
| [**GetLogicalProcessorInformationEx**](https://msdn.microsoft.com/en-us/library/windows/apps/dd405488.aspx) | Introduced into api-ms-win-core-sysinfo-l1-2-1.dll in Windows 10.0.14393.0 |
| [**GlobalMemoryStatusEx**](https://msdn.microsoft.com/en-us/library/windows/apps/aa366589.aspx)                         | Introduced into api-ms-win-core-sysinfo-l1-2-1.dll in Windows 10.0.14393.0 |

 

## <span id="_api-ms-win-core-sysinfo-l1-2-3.dll"></span><span id="_API-MS-WIN-CORE-SYSINFO-L1-2-3.DLL"></span>APIs from the API Set api-ms-win-core-sysinfo-l1-2-3.dll


| API                                                           | Requirements                                                               |
|---------------------------------------------------------------|----------------------------------------------------------------------------|
| [**GetIntegratedDisplaySize**](https://msdn.microsoft.com/en-us/library/windows/apps/dn904185.aspx) | Introduced into api-ms-win-core-sysinfo-l1-2-3.dll in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-core-threadpool-l1-2-0.dll"></span><span id="_API-MS-WIN-CORE-THREADPOOL-L1-2-0.DLL"></span>APIs from the API Set api-ms-win-core-threadpool-l1-2-0.dll


| API                                                                                         | Requirements                                                                  |
|---------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| [**CallbackMayRunLong**](https://msdn.microsoft.com/en-us/library/windows/apps/ms681981.aspx)                                           | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in Windows 10.0.10240.0 |
| [**CancelThreadpoolIo**](https://msdn.microsoft.com/en-us/library/windows/apps/ms681983.aspx)                                           | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in Windows 10.0.10240.0 |
| [**CloseThreadpool**](https://msdn.microsoft.com/en-us/library/windows/apps/ms682030.aspx)                                                 | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in Windows 10.0.10240.0 |
| [**CloseThreadpoolCleanupGroup**](https://msdn.microsoft.com/en-us/library/windows/apps/ms682033.aspx)                         | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in Windows 10.0.10240.0 |
| [**CloseThreadpoolCleanupGroupMembers**](https://msdn.microsoft.com/en-us/library/windows/apps/ms682036.aspx)           | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in Windows 10.0.10240.0 |
| [**CloseThreadpoolIo**](https://msdn.microsoft.com/en-us/library/windows/apps/ms682038.aspx)                                             | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in Windows 10.0.10240.0 |
| [**CloseThreadpoolTimer**](https://msdn.microsoft.com/en-us/library/windows/apps/ms682040.aspx)                                       | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in Windows 10.0.10240.0 |
| [**CloseThreadpoolWait**](https://msdn.microsoft.com/en-us/library/windows/apps/ms682042.aspx)                                         | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in Windows 10.0.10240.0 |
| [**CloseThreadpoolWork**](https://msdn.microsoft.com/en-us/library/windows/apps/ms682043.aspx)                                         | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in Windows 10.0.10240.0 |
| [**CreateThreadpool**](https://msdn.microsoft.com/en-us/library/windows/apps/ms682456.aspx)                                               | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in Windows 10.0.10240.0 |
| [**CreateThreadpoolCleanupGroup**](https://msdn.microsoft.com/en-us/library/windows/apps/ms682462.aspx)                       | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in Windows 10.0.10240.0 |
| [**CreateThreadpoolIo**](https://msdn.microsoft.com/en-us/library/windows/apps/ms682464.aspx)                                           | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in Windows 10.0.10240.0 |
| [**CreateThreadpoolTimer**](https://msdn.microsoft.com/en-us/library/windows/apps/ms682466.aspx)                                     | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in Windows 10.0.10240.0 |
| [**CreateThreadpoolWait**](https://msdn.microsoft.com/en-us/library/windows/apps/ms682474.aspx)                                       | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in Windows 10.0.10240.0 |
| [**CreateThreadpoolWork**](https://msdn.microsoft.com/en-us/library/windows/apps/ms682478.aspx)                                       | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in Windows 10.0.10240.0 |
| [**DisassociateCurrentThreadFromCallback**](https://msdn.microsoft.com/en-us/library/windows/apps/ms682581.aspx)     | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in Windows 10.0.10240.0 |
| [**FreeLibraryWhenCallbackReturns**](https://msdn.microsoft.com/en-us/library/windows/apps/ms683154.aspx)                   | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in Windows 10.0.10240.0 |
| [**IsThreadpoolTimerSet**](https://msdn.microsoft.com/en-us/library/windows/apps/ms684133.aspx)                                       | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in Windows 10.0.10240.0 |
| [**LeaveCriticalSectionWhenCallbackReturns**](https://msdn.microsoft.com/en-us/library/windows/apps/ms684171.aspx) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in Windows 10.0.10240.0 |
| [**QueryThreadpoolStackInformation**](https://msdn.microsoft.com/en-us/library/windows/apps/dd405508.aspx)                 | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in Windows 10.0.10240.0 |
| [**ReleaseMutexWhenCallbackReturns**](https://msdn.microsoft.com/en-us/library/windows/apps/ms685070.aspx)                 | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in Windows 10.0.10240.0 |
| [**ReleaseSemaphoreWhenCallbackReturns**](https://msdn.microsoft.com/en-us/library/windows/apps/ms685073.aspx)         | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in Windows 10.0.10240.0 |
| [**SetEventWhenCallbackReturns**](https://msdn.microsoft.com/en-us/library/windows/apps/ms686214.aspx)                         | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in Windows 10.0.10240.0 |
| [**SetThreadpoolStackInformation**](https://msdn.microsoft.com/en-us/library/windows/apps/dd405520.aspx)                     | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in Windows 10.0.10240.0 |
| [**SetThreadpoolThreadMaximum**](https://msdn.microsoft.com/en-us/library/windows/apps/ms686266.aspx)                           | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in Windows 10.0.10240.0 |
| [**SetThreadpoolThreadMinimum**](https://msdn.microsoft.com/en-us/library/windows/apps/ms686268.aspx)                           | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in Windows 10.0.10240.0 |
| [**SetThreadpoolTimer**](https://msdn.microsoft.com/en-us/library/windows/apps/ms686271.aspx)                                           | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in Windows 10.0.10240.0 |
| [**SetThreadpoolTimerEx**](https://msdn.microsoft.com/en-us/library/windows/apps/dn894018.aspx)                                       | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in Windows 10.0.10240.0 |
| [**SetThreadpoolWait**](https://msdn.microsoft.com/en-us/library/windows/apps/ms686273.aspx)                                             | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in Windows 10.0.10240.0 |
| [**SetThreadpoolWaitEx**](https://msdn.microsoft.com/en-us/library/windows/apps/mt186618.aspx)                                         | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in Windows 10.0.10240.0 |
| [**StartThreadpoolIo**](https://msdn.microsoft.com/en-us/library/windows/apps/ms686326.aspx)                                             | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in Windows 10.0.10240.0 |
| [**SubmitThreadpoolWork**](https://msdn.microsoft.com/en-us/library/windows/apps/ms686338.aspx)                                       | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in Windows 10.0.10240.0 |
| [**TrySubmitThreadpoolCallback**](https://msdn.microsoft.com/en-us/library/windows/apps/ms686862.aspx)                         | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in Windows 10.0.10240.0 |
| [**WaitForThreadpoolIoCallbacks**](https://msdn.microsoft.com/en-us/library/windows/apps/ms687038.aspx)                       | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in Windows 10.0.10240.0 |
| [**WaitForThreadpoolTimerCallbacks**](https://msdn.microsoft.com/en-us/library/windows/apps/ms687042.aspx)                 | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in Windows 10.0.10240.0 |
| [**WaitForThreadpoolWaitCallbacks**](https://msdn.microsoft.com/en-us/library/windows/apps/ms687047.aspx)                   | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in Windows 10.0.10240.0 |
| [**WaitForThreadpoolWorkCallbacks**](https://msdn.microsoft.com/en-us/library/windows/apps/ms687053.aspx)                   | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-core-timezone-l1-1-0.dll"></span><span id="_API-MS-WIN-CORE-TIMEZONE-L1-1-0.DLL"></span>APIs from the API Set api-ms-win-core-timezone-l1-1-0.dll


| API                                                                                                 | Requirements                                                                |
|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| [**EnumDynamicTimeZoneInformation**](https://msdn.microsoft.com/en-us/library/windows/apps/hh706893.aspx)                           | Introduced into api-ms-win-core-timezone-l1-1-0.dll in Windows 10.0.10240.0 |
| [**FileTimeToSystemTime**](https://msdn.microsoft.com/en-us/library/windows/apps/ms724280.aspx)                                               | Introduced into api-ms-win-core-timezone-l1-1-0.dll in Windows 10.0.10240.0 |
| [**GetDynamicTimeZoneInformation**](https://msdn.microsoft.com/en-us/library/windows/apps/ms724318.aspx)                             | Introduced into api-ms-win-core-timezone-l1-1-0.dll in Windows 10.0.10240.0 |
| [**GetDynamicTimeZoneInformationEffectiveYears**](https://msdn.microsoft.com/en-us/library/windows/apps/hh706894.aspx) | Introduced into api-ms-win-core-timezone-l1-1-0.dll in Windows 10.0.10240.0 |
| [**GetTimeZoneInformation**](https://msdn.microsoft.com/en-us/library/windows/apps/ms724421.aspx)                                           | Introduced into api-ms-win-core-timezone-l1-1-0.dll in Windows 10.0.10240.0 |
| [**GetTimeZoneInformationForYear**](https://msdn.microsoft.com/en-us/library/windows/apps/bb540851.aspx)                             | Introduced into api-ms-win-core-timezone-l1-1-0.dll in Windows 10.0.10240.0 |
| [**SystemTimeToFileTime**](https://msdn.microsoft.com/en-us/library/windows/apps/ms724948.aspx)                                               | Introduced into api-ms-win-core-timezone-l1-1-0.dll in Windows 10.0.10240.0 |
| [**SystemTimeToTzSpecificLocalTime**](https://msdn.microsoft.com/en-us/library/windows/apps/ms724949.aspx)                         | Introduced into api-ms-win-core-timezone-l1-1-0.dll in Windows 10.0.10240.0 |
| [**SystemTimeToTzSpecificLocalTimeEx**](https://msdn.microsoft.com/en-us/library/windows/apps/jj206642.aspx)                     | Introduced into api-ms-win-core-timezone-l1-1-0.dll in Windows 10.0.10240.0 |
| [**TzSpecificLocalTimeToSystemTime**](https://msdn.microsoft.com/en-us/library/windows/apps/ms725485.aspx)                         | Introduced into api-ms-win-core-timezone-l1-1-0.dll in Windows 10.0.10240.0 |
| [**TzSpecificLocalTimeToSystemTimeEx**](https://msdn.microsoft.com/en-us/library/windows/apps/jj206643.aspx)                     | Introduced into api-ms-win-core-timezone-l1-1-0.dll in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-core-util-l1-1-0.dll"></span><span id="_API-MS-WIN-CORE-UTIL-L1-1-0.DLL"></span>APIs from the API Set api-ms-win-core-util-l1-1-0.dll


| API                                                              | Requirements                                                            |
|------------------------------------------------------------------|-------------------------------------------------------------------------|
| [**DecodePointer**](https://www.bing.com/search?q=DecodePointer) | Introduced into api-ms-win-core-util-l1-1-0.dll in Windows 10.0.10240.0 |
| [**EncodePointer**](https://www.bing.com/search?q=EncodePointer) | Introduced into api-ms-win-core-util-l1-1-0.dll in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-core-windowsceip-l1-1-0.dll"></span><span id="_API-MS-WIN-CORE-WINDOWSCEIP-L1-1-0.DLL"></span>APIs from the API Set api-ms-win-core-windowsceip-l1-1-0.dll


| API                                     | Requirements                                                                   |
|-----------------------------------------|--------------------------------------------------------------------------------|
| [**CeipIsOptedIn**](https://msdn.microsoft.com/en-us/library/windows/apps/dn482415.aspx) | Introduced into api-ms-win-core-windowsceip-l1-1-0.dll in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-core-windowserrorreporting-l1-1-0.dll"></span><span id="_API-MS-WIN-CORE-WINDOWSERRORREPORTING-L1-1-0.DLL"></span>APIs from the API Set api-ms-win-core-windowserrorreporting-l1-1-0.dll


| API                                                          | Requirements                                                                             |
|--------------------------------------------------------------|------------------------------------------------------------------------------------------|
| [**WerRegisterFile**](https://msdn.microsoft.com/en-us/library/windows/apps/bb513619.aspx)                   | Introduced into api-ms-win-core-windowserrorreporting-l1-1-0.dll in Windows 10.0.10240.0 |
| [**WerRegisterMemoryBlock**](https://msdn.microsoft.com/en-us/library/windows/apps/bb513620.aspx)     | Introduced into api-ms-win-core-windowserrorreporting-l1-1-0.dll in Windows 10.0.10240.0 |
| [**WerUnregisterFile**](https://msdn.microsoft.com/en-us/library/windows/apps/bb513630.aspx)               | Introduced into api-ms-win-core-windowserrorreporting-l1-1-0.dll in Windows 10.0.10240.0 |
| [**WerUnregisterMemoryBlock**](https://msdn.microsoft.com/en-us/library/windows/apps/bb513631.aspx) | Introduced into api-ms-win-core-windowserrorreporting-l1-1-0.dll in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-core-winrt-error-l1-1-1.dll"></span><span id="_API-MS-WIN-CORE-WINRT-ERROR-L1-1-1.DLL"></span>APIs from the API Set api-ms-win-core-winrt-error-l1-1-1.dll


| API                                                                    | Requirements                                                                   |
|------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| [**GetRestrictedErrorInfo**](https://msdn.microsoft.com/en-us/library/windows/apps/jj219013.aspx)             | Introduced into api-ms-win-core-winrt-error-l1-1-1.dll in Windows 10.0.10240.0 |
| [**RoCaptureErrorContext**](https://msdn.microsoft.com/en-us/library/windows/apps/jj219014.aspx)               | Introduced into api-ms-win-core-winrt-error-l1-1-1.dll in Windows 10.0.10240.0 |
| [**RoFailFastWithErrorContext**](https://msdn.microsoft.com/en-us/library/windows/apps/jj219015.aspx)     | Introduced into api-ms-win-core-winrt-error-l1-1-1.dll in Windows 10.0.10240.0 |
| [**RoGetErrorReportingFlags**](https://msdn.microsoft.com/en-us/library/windows/apps/br224649.aspx)         | Introduced into api-ms-win-core-winrt-error-l1-1-1.dll in Windows 10.0.10240.0 |
| [**RoOriginateError**](https://msdn.microsoft.com/en-us/library/windows/apps/br224651.aspx)                         | Introduced into api-ms-win-core-winrt-error-l1-1-1.dll in Windows 10.0.10240.0 |
| [**RoOriginateErrorW**](https://msdn.microsoft.com/en-us/library/windows/apps/br224652.aspx)                       | Introduced into api-ms-win-core-winrt-error-l1-1-1.dll in Windows 10.0.10240.0 |
| [**RoOriginateLanguageException**](https://msdn.microsoft.com/en-us/library/windows/apps/dn302172.aspx) | Introduced into api-ms-win-core-winrt-error-l1-1-1.dll in Windows 10.0.10240.0 |
| [**RoReportUnhandledError**](https://msdn.microsoft.com/en-us/library/windows/apps/dn457328.aspx)             | Introduced into api-ms-win-core-winrt-error-l1-1-1.dll in Windows 10.0.10240.0 |
| [**RoSetErrorReportingFlags**](https://msdn.microsoft.com/en-us/library/windows/apps/br224657.aspx)         | Introduced into api-ms-win-core-winrt-error-l1-1-1.dll in Windows 10.0.10240.0 |
| [**RoTransformError**](https://msdn.microsoft.com/en-us/library/windows/apps/br224658.aspx)                         | Introduced into api-ms-win-core-winrt-error-l1-1-1.dll in Windows 10.0.10240.0 |
| [**RoTransformErrorW**](https://msdn.microsoft.com/en-us/library/windows/apps/br224659.aspx)                       | Introduced into api-ms-win-core-winrt-error-l1-1-1.dll in Windows 10.0.10240.0 |
| [**SetRestrictedErrorInfo**](https://msdn.microsoft.com/en-us/library/windows/apps/jj219016.aspx)             | Introduced into api-ms-win-core-winrt-error-l1-1-1.dll in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-core-winrt-l1-1-0.dll"></span><span id="_API-MS-WIN-CORE-WINRT-L1-1-0.DLL"></span>APIs from the API Set api-ms-win-core-winrt-l1-1-0.dll


| API                                                                            | Requirements                                                             |
|--------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| [**RoActivateInstance**](https://msdn.microsoft.com/en-us/library/windows/apps/br224646.aspx)                             | Introduced into api-ms-win-core-winrt-l1-1-0.dll in Windows 10.0.10240.0 |
| [**RoGetActivationFactory**](https://msdn.microsoft.com/en-us/library/windows/apps/br224648.aspx)                     | Introduced into api-ms-win-core-winrt-l1-1-0.dll in Windows 10.0.10240.0 |
| [**RoGetApartmentIdentifier**](https://msdn.microsoft.com/en-us/library/windows/apps/jj219266.aspx)                 | Introduced into api-ms-win-core-winrt-l1-1-0.dll in Windows 10.0.10240.0 |
| [**RoInitialize**](https://msdn.microsoft.com/en-us/library/windows/apps/br224650.aspx)                                         | Introduced into api-ms-win-core-winrt-l1-1-0.dll in Windows 10.0.10240.0 |
| [**RoRegisterActivationFactories**](https://msdn.microsoft.com/en-us/library/windows/apps/br224653.aspx)       | Introduced into api-ms-win-core-winrt-l1-1-0.dll in Windows 10.0.10240.0 |
| [**RoRegisterForApartmentShutdown**](https://msdn.microsoft.com/en-us/library/windows/apps/jj219267.aspx)     | Introduced into api-ms-win-core-winrt-l1-1-0.dll in Windows 10.0.10240.0 |
| [**RoRevokeActivationFactories**](https://msdn.microsoft.com/en-us/library/windows/apps/br224655.aspx)           | Introduced into api-ms-win-core-winrt-l1-1-0.dll in Windows 10.0.10240.0 |
| [**RoUninitialize**](https://msdn.microsoft.com/en-us/library/windows/apps/br224660.aspx)                                     | Introduced into api-ms-win-core-winrt-l1-1-0.dll in Windows 10.0.10240.0 |
| [**RoUnregisterForApartmentShutdown**](https://msdn.microsoft.com/en-us/library/windows/apps/jj219268.aspx) | Introduced into api-ms-win-core-winrt-l1-1-0.dll in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-core-winrt-registration-l1-1-0.dll"></span><span id="_API-MS-WIN-CORE-WINRT-REGISTRATION-L1-1-0.DLL"></span>APIs from the API Set api-ms-win-core-winrt-registration-l1-1-0.dll


| API                                                                              | Requirements                                                                          |
|----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| [**RoGetActivatableClassRegistration**](https://msdn.microsoft.com/en-us/library/windows/apps/br229855.aspx) | Introduced into api-ms-win-core-winrt-registration-l1-1-0.dll in Windows 10.0.10240.0 |
| [**RoGetServerActivatableClasses**](https://msdn.microsoft.com/en-us/library/windows/apps/br229858.aspx)         | Introduced into api-ms-win-core-winrt-registration-l1-1-0.dll in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-core-winrt-robuffer-l1-1-0.dll"></span><span id="_API-MS-WIN-CORE-WINRT-ROBUFFER-L1-1-0.DLL"></span>APIs from the API Set api-ms-win-core-winrt-robuffer-l1-1-0.dll


| API                                                    | Requirements                                                                      |
|--------------------------------------------------------|-----------------------------------------------------------------------------------|
| [**RoGetBufferMarshaler**](https://msdn.microsoft.com/en-us/library/windows/apps/hh438433.aspx) | Introduced into api-ms-win-core-winrt-robuffer-l1-1-0.dll in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-core-winrt-roparameterizediid-l1-1-0.dll"></span><span id="_API-MS-WIN-CORE-WINRT-ROPARAMETERIZEDIID-L1-1-0.DLL"></span>APIs from the API Set api-ms-win-core-winrt-roparameterizediid-l1-1-0.dll


| API                                                                                            | Requirements                                                                                |
|------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| [**RoFreeParameterizedTypeExtra**](https://msdn.microsoft.com/en-us/library/windows/apps/br229854.aspx)                         | Introduced into api-ms-win-core-winrt-roparameterizediid-l1-1-0.dll in Windows 10.0.10240.0 |
| [**RoGetParameterizedTypeInstanceIID**](https://msdn.microsoft.com/en-us/library/windows/apps/br229857.aspx)               | Introduced into api-ms-win-core-winrt-roparameterizediid-l1-1-0.dll in Windows 10.0.10240.0 |
| [**RoParameterizedTypeExtraGetTypeSignature**](https://msdn.microsoft.com/en-us/library/windows/apps/br229859.aspx) | Introduced into api-ms-win-core-winrt-roparameterizediid-l1-1-0.dll in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-core-winrt-string-l1-1-0.dll"></span><span id="_API-MS-WIN-CORE-WINRT-STRING-L1-1-0.DLL"></span>APIs from the API Set api-ms-win-core-winrt-string-l1-1-0.dll


| API                                                                                  | Requirements                                                                    |
|--------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| [**HSTRING\_UserFree**](https://msdn.microsoft.com/en-us/library/windows/apps/hh846259.aspx)                                      | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in Windows 10.0.10240.0 |
| [**HSTRING\_UserFree64**](https://msdn.microsoft.com/en-us/library/windows/apps/hh846260.aspx)                                  | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in Windows 10.0.10240.0 |
| [**HSTRING\_UserMarshal**](https://msdn.microsoft.com/en-us/library/windows/apps/hh846261.aspx)                                | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in Windows 10.0.10240.0 |
| [**HSTRING\_UserMarshal64**](https://msdn.microsoft.com/en-us/library/windows/apps/hh846262.aspx)                            | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in Windows 10.0.10240.0 |
| [**HSTRING\_UserSize**](https://msdn.microsoft.com/en-us/library/windows/apps/hh846263.aspx)                                      | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in Windows 10.0.10240.0 |
| [**HSTRING\_UserSize64**](https://msdn.microsoft.com/en-us/library/windows/apps/hh846264.aspx)                                  | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in Windows 10.0.10240.0 |
| [**HSTRING\_UserUnmarshal**](https://msdn.microsoft.com/en-us/library/windows/apps/hh846265.aspx)                            | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in Windows 10.0.10240.0 |
| [**HSTRING\_UserUnmarshal64**](https://msdn.microsoft.com/en-us/library/windows/apps/hh846266.aspx)                        | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in Windows 10.0.10240.0 |
| [**WindowsCompareStringOrdinal**](https://msdn.microsoft.com/en-us/library/windows/apps/br224628.aspx)                 | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in Windows 10.0.10240.0 |
| [**WindowsConcatString**](https://msdn.microsoft.com/en-us/library/windows/apps/br224629.aspx)                                 | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in Windows 10.0.10240.0 |
| [**WindowsCreateString**](https://msdn.microsoft.com/en-us/library/windows/apps/br224630.aspx)                                 | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in Windows 10.0.10240.0 |
| [**WindowsCreateStringReference**](https://msdn.microsoft.com/en-us/library/windows/apps/br224631.aspx)               | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in Windows 10.0.10240.0 |
| [**WindowsDeleteString**](https://msdn.microsoft.com/en-us/library/windows/apps/br224632.aspx)                                 | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in Windows 10.0.10240.0 |
| [**WindowsDeleteStringBuffer**](https://msdn.microsoft.com/en-us/library/windows/apps/br224633.aspx)                     | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in Windows 10.0.10240.0 |
| [**WindowsDuplicateString**](https://msdn.microsoft.com/en-us/library/windows/apps/br224634.aspx)                           | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in Windows 10.0.10240.0 |
| [**WindowsGetStringLen**](https://msdn.microsoft.com/en-us/library/windows/apps/br224635.aspx)                                 | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in Windows 10.0.10240.0 |
| [**WindowsGetStringRawBuffer**](https://msdn.microsoft.com/en-us/library/windows/apps/br224636.aspx)                     | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in Windows 10.0.10240.0 |
| [**WindowsIsStringEmpty**](https://msdn.microsoft.com/en-us/library/windows/apps/br224637.aspx)                               | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in Windows 10.0.10240.0 |
| [**WindowsPreallocateStringBuffer**](https://msdn.microsoft.com/en-us/library/windows/apps/br224638.aspx)           | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in Windows 10.0.10240.0 |
| [**WindowsPromoteStringBuffer**](https://msdn.microsoft.com/en-us/library/windows/apps/br224639.aspx)                   | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in Windows 10.0.10240.0 |
| [**WindowsReplaceString**](https://msdn.microsoft.com/en-us/library/windows/apps/br224640.aspx)                               | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in Windows 10.0.10240.0 |
| [**WindowsStringHasEmbeddedNull**](https://msdn.microsoft.com/en-us/library/windows/apps/br224641.aspx)               | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in Windows 10.0.10240.0 |
| [**WindowsSubstring**](https://msdn.microsoft.com/en-us/library/windows/apps/br224642.aspx)                                       | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in Windows 10.0.10240.0 |
| [**WindowsSubstringWithSpecifiedLength**](https://msdn.microsoft.com/en-us/library/windows/apps/br224643.aspx) | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in Windows 10.0.10240.0 |
| [**WindowsTrimStringEnd**](https://msdn.microsoft.com/en-us/library/windows/apps/br224644.aspx)                               | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in Windows 10.0.10240.0 |
| [**WindowsTrimStringStart**](https://msdn.microsoft.com/en-us/library/windows/apps/br224645.aspx)                           | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-core-xstate-l2-1-0.dll"></span><span id="_API-MS-WIN-CORE-XSTATE-L2-1-0.DLL"></span>APIs from the API Set api-ms-win-core-xstate-l2-1-0.dll


| API                                                           | Requirements                                                              |
|---------------------------------------------------------------|---------------------------------------------------------------------------|
| [**GetEnabledXStateFeatures**](https://msdn.microsoft.com/en-us/library/windows/apps/hh134235.aspx) | Introduced into api-ms-win-core-xstate-l2-1-0.dll in Windows 10.0.10240.0 |
| [**GetXStateFeaturesMask**](https://msdn.microsoft.com/en-us/library/windows/apps/hh134236.aspx)       | Introduced into api-ms-win-core-xstate-l2-1-0.dll in Windows 10.0.10240.0 |
| [**InitializeContext**](https://msdn.microsoft.com/en-us/library/windows/apps/hh134237.aspx)               | Introduced into api-ms-win-core-xstate-l2-1-0.dll in Windows 10.0.10240.0 |
| [**LocateXStateFeature**](https://msdn.microsoft.com/en-us/library/windows/apps/hh134238.aspx)           | Introduced into api-ms-win-core-xstate-l2-1-0.dll in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-eventing-classicprovider-l1-1-0.dll"></span><span id="_API-MS-WIN-EVENTING-CLASSICPROVIDER-L1-1-0.DLL"></span>APIs from the API Set api-ms-win-eventing-classicprovider-l1-1-0.dll


| API                                                  | Requirements                                                                           |
|------------------------------------------------------|----------------------------------------------------------------------------------------|
| [**GetTraceEnableFlags**](https://msdn.microsoft.com/en-us/library/windows/apps/aa363893.aspx)   | Introduced into api-ms-win-eventing-classicprovider-l1-1-0.dll in Windows 10.0.10240.0 |
| [**GetTraceEnableLevel**](https://msdn.microsoft.com/en-us/library/windows/apps/aa363894.aspx)   | Introduced into api-ms-win-eventing-classicprovider-l1-1-0.dll in Windows 10.0.10240.0 |
| [**GetTraceLoggerHandle**](https://msdn.microsoft.com/en-us/library/windows/apps/aa363897.aspx) | Introduced into api-ms-win-eventing-classicprovider-l1-1-0.dll in Windows 10.0.10240.0 |
| [**RegisterTraceGuidsW**](https://msdn.microsoft.com/en-us/library/windows/apps/aa364105.aspx)    | Introduced into api-ms-win-eventing-classicprovider-l1-1-0.dll in Windows 10.0.10240.0 |
| [**TraceMessage**](https://msdn.microsoft.com/en-us/library/windows/apps/aa364139.aspx)                 | Introduced into api-ms-win-eventing-classicprovider-l1-1-0.dll in Windows 10.0.10240.0 |
| [**UnregisterTraceGuids**](https://msdn.microsoft.com/en-us/library/windows/apps/aa364154.aspx) | Introduced into api-ms-win-eventing-classicprovider-l1-1-0.dll in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-eventing-consumer-l1-1-0.dll"></span><span id="_API-MS-WIN-EVENTING-CONSUMER-L1-1-0.DLL"></span>APIs from the API Set api-ms-win-eventing-consumer-l1-1-0.dll


| API                                  | Requirements                                                                    |
|--------------------------------------|---------------------------------------------------------------------------------|
| [**CloseTrace**](https://msdn.microsoft.com/en-us/library/windows/apps/aa363686.aspx)     | Introduced into api-ms-win-eventing-consumer-l1-1-0.dll in Windows 10.0.10240.0 |
| [**OpenTraceW**](https://msdn.microsoft.com/en-us/library/windows/apps/aa364089.aspx)      | Introduced into api-ms-win-eventing-consumer-l1-1-0.dll in Windows 10.0.10240.0 |
| [**ProcessTrace**](https://msdn.microsoft.com/en-us/library/windows/apps/aa364093.aspx) | Introduced into api-ms-win-eventing-consumer-l1-1-0.dll in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-eventing-controller-l1-1-0.dll"></span><span id="_API-MS-WIN-EVENTING-CONTROLLER-L1-1-0.DLL"></span>APIs from the API Set api-ms-win-eventing-controller-l1-1-0.dll


| API                                      | Requirements                                                                      |
|------------------------------------------|-----------------------------------------------------------------------------------|
| [**ControlTraceW**](https://msdn.microsoft.com/en-us/library/windows/apps/aa363696.aspx)    | Introduced into api-ms-win-eventing-controller-l1-1-0.dll in Windows 10.0.10240.0 |
| [**EnableTraceEx2**](https://msdn.microsoft.com/en-us/library/windows/apps/dd392305.aspx) | Introduced into api-ms-win-eventing-controller-l1-1-0.dll in Windows 10.0.10240.0 |
| [**StartTraceW**](https://msdn.microsoft.com/en-us/library/windows/apps/aa364117.aspx)        | Introduced into api-ms-win-eventing-controller-l1-1-0.dll in Windows 10.0.10240.0 |
| [**StopTraceW**](https://msdn.microsoft.com/en-us/library/windows/apps/aa364119.aspx)          | Introduced into api-ms-win-eventing-controller-l1-1-0.dll in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-eventing-legacy-l1-1-0.dll"></span><span id="_API-MS-WIN-EVENTING-LEGACY-L1-1-0.DLL"></span>APIs from the API Set api-ms-win-eventing-legacy-l1-1-0.dll


| API                                         | Requirements                                                                  |
|---------------------------------------------|-------------------------------------------------------------------------------|
| [**EnableTrace**](https://msdn.microsoft.com/en-us/library/windows/apps/aa363710.aspx)          | Introduced into api-ms-win-eventing-legacy-l1-1-0.dll in Windows 10.0.10240.0 |
| [**EnableTraceEx**](https://msdn.microsoft.com/en-us/library/windows/apps/aa363711.aspx) | Introduced into api-ms-win-eventing-legacy-l1-1-0.dll in Windows 10.0.10240.0 |
| [**FlushTraceW**](https://msdn.microsoft.com/en-us/library/windows/apps/aa363891.aspx)           | Introduced into api-ms-win-eventing-legacy-l1-1-0.dll in Windows 10.0.10240.0 |
| [**QueryTraceW**](https://msdn.microsoft.com/en-us/library/windows/apps/aa364103.aspx)           | Introduced into api-ms-win-eventing-legacy-l1-1-0.dll in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-eventing-provider-l1-1-0.dll"></span><span id="_API-MS-WIN-EVENTING-PROVIDER-L1-1-0.DLL"></span>APIs from the API Set api-ms-win-eventing-provider-l1-1-0.dll


| API                                                           | Requirements                                                                    |
|---------------------------------------------------------------|---------------------------------------------------------------------------------|
| [**EventActivityIdControl**](https://msdn.microsoft.com/en-us/library/windows/apps/aa363720.aspx) | Introduced into api-ms-win-eventing-provider-l1-1-0.dll in Windows 10.0.10240.0 |
| [**EventRegister**](https://msdn.microsoft.com/en-us/library/windows/apps/aa363744.aspx)                   | Introduced into api-ms-win-eventing-provider-l1-1-0.dll in Windows 10.0.10240.0 |
| [**EventSetInformation**](https://msdn.microsoft.com/en-us/library/windows/apps/hh447256.aspx)            | Introduced into api-ms-win-eventing-provider-l1-1-0.dll in Windows 10.0.10240.0 |
| [**EventUnregister**](https://msdn.microsoft.com/en-us/library/windows/apps/aa363749.aspx)               | Introduced into api-ms-win-eventing-provider-l1-1-0.dll in Windows 10.0.10240.0 |
| [**EventWrite**](https://msdn.microsoft.com/en-us/library/windows/apps/aa363752.aspx)                         | Introduced into api-ms-win-eventing-provider-l1-1-0.dll in Windows 10.0.10240.0 |
| [**EventWriteEx**](https://msdn.microsoft.com/en-us/library/windows/apps/dd392307.aspx)                          | Introduced into api-ms-win-eventing-provider-l1-1-0.dll in Windows 10.0.10240.0 |
| [**EventWriteString**](https://msdn.microsoft.com/en-us/library/windows/apps/aa363750.aspx)             | Introduced into api-ms-win-eventing-provider-l1-1-0.dll in Windows 10.0.10240.0 |
| [**EventWriteTransfer**](https://msdn.microsoft.com/en-us/library/windows/apps/aa363751.aspx)         | Introduced into api-ms-win-eventing-provider-l1-1-0.dll in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-gaming-tcui-l1-1-0.dll"></span><span id="_API-MS-WIN-GAMING-TCUI-L1-1-0.DLL"></span>APIs from the API Set api-ms-win-gaming-tcui-l1-1-0.dll


| API                                                                                                | Requirements                                                              |
|----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| [**ProcessPendingGameUI**](https://www.bing.com/search?q=ProcessPendingGameUI)                     | Introduced into api-ms-win-gaming-tcui-l1-1-0.dll in Windows 10.0.10240.0 |
| [**ShowChangeFriendRelationshipUI**](https://www.bing.com/search?q=ShowChangeFriendRelationshipUI) | Introduced into api-ms-win-gaming-tcui-l1-1-0.dll in Windows 10.0.10240.0 |
| [**ShowGameInviteUI**](https://www.bing.com/search?q=ShowGameInviteUI)                             | Introduced into api-ms-win-gaming-tcui-l1-1-0.dll in Windows 10.0.10240.0 |
| [**ShowPlayerPickerUI**](https://www.bing.com/search?q=ShowPlayerPickerUI)                         | Introduced into api-ms-win-gaming-tcui-l1-1-0.dll in Windows 10.0.10240.0 |
| [**ShowProfileCardUI**](https://www.bing.com/search?q=ShowProfileCardUI)                           | Introduced into api-ms-win-gaming-tcui-l1-1-0.dll in Windows 10.0.10240.0 |
| [**ShowTitleAchievementsUI**](https://www.bing.com/search?q=ShowTitleAchievementsUI)               | Introduced into api-ms-win-gaming-tcui-l1-1-0.dll in Windows 10.0.10240.0 |
| [**TryCancelPendingGameUI**](https://www.bing.com/search?q=TryCancelPendingGameUI)                 | Introduced into api-ms-win-gaming-tcui-l1-1-0.dll in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-ro-typeresolution-l1-1-0.dll"></span><span id="_API-MS-WIN-RO-TYPERESOLUTION-L1-1-0.DLL"></span>APIs from the API Set api-ms-win-ro-typeresolution-l1-1-0.dll


| API                                                | Requirements                                                                    |
|----------------------------------------------------|---------------------------------------------------------------------------------|
| [**RoGetMetaDataFile**](https://msdn.microsoft.com/en-us/library/windows/apps/br229856.aspx)   | Introduced into api-ms-win-ro-typeresolution-l1-1-0.dll in Windows 10.0.10240.0 |
| [**RoParseTypeName**](https://msdn.microsoft.com/en-us/library/windows/apps/hh438434.aspx)       | Introduced into api-ms-win-ro-typeresolution-l1-1-0.dll in Windows 10.0.10240.0 |
| [**RoResolveNamespace**](https://msdn.microsoft.com/en-us/library/windows/apps/br229860.aspx) | Introduced into api-ms-win-ro-typeresolution-l1-1-0.dll in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-security-cryptoapi-l1-1-0.dll"></span><span id="_API-MS-WIN-SECURITY-CRYPTOAPI-L1-1-0.DLL"></span>APIs from the API Set api-ms-win-security-cryptoapi-l1-1-0.dll


| API                                                     | Requirements                                                                     |
|---------------------------------------------------------|----------------------------------------------------------------------------------|
| [**CryptReleaseContext**](https://msdn.microsoft.com/en-us/library/windows/apps/aa380268.aspx) | Introduced into api-ms-win-security-cryptoapi-l1-1-0.dll in Windows 10.0.10240.0 |

 

## <span id="_api-ms-win-shcore-stream-winrt-l1-1-0.dll"></span><span id="_API-MS-WIN-SHCORE-STREAM-WINRT-L1-1-0.DLL"></span>APIs from the API Set api-ms-win-shcore-stream-winrt-l1-1-0.dll


| API                                                                                | Requirements                                                                      |
|------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| [**CreateRandomAccessStreamOnFile**](https://msdn.microsoft.com/en-us/library/windows/apps/hh846256.aspx)         | Introduced into api-ms-win-shcore-stream-winrt-l1-1-0.dll in Windows 10.0.10240.0 |
| [**CreateRandomAccessStreamOverStream**](https://msdn.microsoft.com/en-us/library/windows/apps/hh846257.aspx) | Introduced into api-ms-win-shcore-stream-winrt-l1-1-0.dll in Windows 10.0.10240.0 |
| [**CreateStreamOverRandomAccessStream**](https://msdn.microsoft.com/en-us/library/windows/apps/hh846258.aspx) | Introduced into api-ms-win-shcore-stream-winrt-l1-1-0.dll in Windows 10.0.10240.0 |

 

## <span id="_CABINET.DLL"></span>APIs from the dll cabinet.dll


| API                                                                     | Requirements                                        |
|-------------------------------------------------------------------------|-----------------------------------------------------|
| [**CloseCompressor**](https://msdn.microsoft.com/en-us/library/windows/apps/hh437542.aspx)                           | Introduced into cabinet.dll in Windows 10.0.10240.0 |
| [**CloseDecompressor**](https://msdn.microsoft.com/en-us/library/windows/apps/hh437545.aspx)                       | Introduced into cabinet.dll in Windows 10.0.10240.0 |
| [**Compress**](https://msdn.microsoft.com/en-us/library/windows/apps/hh437548.aspx)                                         | Introduced into cabinet.dll in Windows 10.0.10240.0 |
| [**CreateCompressor**](https://msdn.microsoft.com/en-us/library/windows/apps/hh437570.aspx)                         | Introduced into cabinet.dll in Windows 10.0.10240.0 |
| [**CreateDecompressor**](https://msdn.microsoft.com/en-us/library/windows/apps/hh437573.aspx)                     | Introduced into cabinet.dll in Windows 10.0.10240.0 |
| [**Decompress**](https://msdn.microsoft.com/en-us/library/windows/apps/hh437576.aspx)                                     | Introduced into cabinet.dll in Windows 10.0.10240.0 |
| [**FDICopy**](https://www.bing.com/search?q=FDICopy)                    | Introduced into cabinet.dll in Windows 10.0.10240.0 |
| [**FDICreate**](https://www.bing.com/search?q=FDICreate)                | Introduced into cabinet.dll in Windows 10.0.10240.0 |
| [**FDIDestroy**](https://www.bing.com/search?q=FDIDestroy)              | Introduced into cabinet.dll in Windows 10.0.10240.0 |
| [**FDIIsCabinet**](https://www.bing.com/search?q=FDIIsCabinet)          | Introduced into cabinet.dll in Windows 10.0.10240.0 |
| [**QueryCompressorInformation**](https://msdn.microsoft.com/en-us/library/windows/apps/hh437578.aspx)     | Introduced into cabinet.dll in Windows 10.0.10240.0 |
| [**QueryDecompressorInformation**](https://msdn.microsoft.com/en-us/library/windows/apps/hh437580.aspx) | Introduced into cabinet.dll in Windows 10.0.10240.0 |
| [**ResetCompressor**](https://msdn.microsoft.com/en-us/library/windows/apps/hh437583.aspx)                           | Introduced into cabinet.dll in Windows 10.0.10240.0 |
| [**ResetDecompressor**](https://msdn.microsoft.com/en-us/library/windows/apps/hh437586.aspx)                       | Introduced into cabinet.dll in Windows 10.0.10240.0 |
| [**SetCompressorInformation**](https://msdn.microsoft.com/en-us/library/windows/apps/hh437588.aspx)         | Introduced into cabinet.dll in Windows 10.0.10240.0 |
| [**SetDecompressorInformation**](https://msdn.microsoft.com/en-us/library/windows/apps/hh437592.aspx)     | Introduced into cabinet.dll in Windows 10.0.10240.0 |

 

## <span id="_CHAKRA.DLL"></span>APIs from the dll chakra.dll


| API                                                                                                            | Requirements                                       |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| [**JsAddRef**](https://www.bing.com/search?q=JsAddRef)                                                         | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsBooleanToBool**](https://www.bing.com/search?q=JsBooleanToBool)                                           | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsBoolToBoolean**](https://www.bing.com/search?q=JsBoolToBoolean)                                           | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsCallFunction**](https://www.bing.com/search?q=JsCallFunction)                                             | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsCollectGarbage**](https://www.bing.com/search?q=JsCollectGarbage)                                         | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsConstructObject**](https://www.bing.com/search?q=JsConstructObject)                                       | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsConvertValueToBoolean**](https://www.bing.com/search?q=JsConvertValueToBoolean)                           | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsConvertValueToNumber**](https://www.bing.com/search?q=JsConvertValueToNumber)                             | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsConvertValueToObject**](https://www.bing.com/search?q=JsConvertValueToObject)                             | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsConvertValueToString**](https://www.bing.com/search?q=JsConvertValueToString)                             | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsCreateArray**](https://www.bing.com/search?q=JsCreateArray)                                               | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsCreateArrayBuffer**](https://www.bing.com/search?q=JsCreateArrayBuffer)                                   | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsCreateContext**](https://www.bing.com/search?q=JsCreateContext)                                           | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsCreateDataView**](https://www.bing.com/search?q=JsCreateDataView)                                         | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsCreateError**](https://www.bing.com/search?q=JsCreateError)                                               | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsCreateExternalObject**](https://www.bing.com/search?q=JsCreateExternalObject)                             | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsCreateFunction**](https://www.bing.com/search?q=JsCreateFunction)                                         | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsCreateNamedFunction**](https://www.bing.com/search?q=JsCreateNamedFunction)                               | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsCreateObject**](https://www.bing.com/search?q=JsCreateObject)                                             | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsCreateRangeError**](https://www.bing.com/search?q=JsCreateRangeError)                                     | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsCreateReferenceError**](https://www.bing.com/search?q=JsCreateReferenceError)                             | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsCreateRuntime**](https://www.bing.com/search?q=JsCreateRuntime)                                           | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsCreateSymbol**](https://www.bing.com/search?q=JsCreateSymbol)                                             | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsCreateSyntaxError**](https://www.bing.com/search?q=JsCreateSyntaxError)                                   | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsCreateTypedArray**](https://www.bing.com/search?q=JsCreateTypedArray)                                     | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsCreateTypeError**](https://www.bing.com/search?q=JsCreateTypeError)                                       | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsCreateURIError**](https://www.bing.com/search?q=JsCreateURIError)                                         | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsDefineProperty**](https://www.bing.com/search?q=JsDefineProperty)                                         | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsDeleteIndexedProperty**](https://www.bing.com/search?q=JsDeleteIndexedProperty)                           | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsDeleteProperty**](https://www.bing.com/search?q=JsDeleteProperty)                                         | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsDisableRuntimeExecution**](https://www.bing.com/search?q=JsDisableRuntimeExecution)                       | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsDisposeRuntime**](https://www.bing.com/search?q=JsDisposeRuntime)                                         | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsDoubleToNumber**](https://www.bing.com/search?q=JsDoubleToNumber)                                         | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsEnableRuntimeExecution**](https://www.bing.com/search?q=JsEnableRuntimeExecution)                         | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsEquals**](https://www.bing.com/search?q=JsEquals)                                                         | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsGetAndClearException**](https://www.bing.com/search?q=JsGetAndClearException)                             | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsGetArrayBufferStorage**](https://www.bing.com/search?q=JsGetArrayBufferStorage)                           | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsGetCurrentContext**](https://www.bing.com/search?q=JsGetCurrentContext)                                   | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsGetDataViewStorage**](https://www.bing.com/search?q=JsGetDataViewStorage)                                 | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsGetExtensionAllowed**](https://www.bing.com/search?q=JsGetExtensionAllowed)                               | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsGetExternalData**](https://www.bing.com/search?q=JsGetExternalData)                                       | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsGetFalseValue**](https://www.bing.com/search?q=JsGetFalseValue)                                           | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsGetGlobalObject**](https://www.bing.com/search?q=JsGetGlobalObject)                                       | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsGetIndexedPropertiesExternalData**](https://www.bing.com/search?q=JsGetIndexedPropertiesExternalData)     | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsGetIndexedProperty**](https://www.bing.com/search?q=JsGetIndexedProperty)                                 | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsGetNullValue**](https://www.bing.com/search?q=JsGetNullValue)                                             | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsGetOwnPropertyDescriptor**](https://www.bing.com/search?q=JsGetOwnPropertyDescriptor)                     | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsGetOwnPropertyNames**](https://www.bing.com/search?q=JsGetOwnPropertyNames)                               | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsGetOwnPropertySymbols**](https://www.bing.com/search?q=JsGetOwnPropertySymbols)                           | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsGetProperty**](https://www.bing.com/search?q=JsGetProperty)                                               | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsGetPropertyIdFromName**](https://www.bing.com/search?q=JsGetPropertyIdFromName)                           | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsGetPropertyIdFromSymbol**](https://www.bing.com/search?q=JsGetPropertyIdFromSymbol)                       | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsGetPropertyIdType**](https://www.bing.com/search?q=JsGetPropertyIdType)                                   | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsGetPropertyNameFromId**](https://www.bing.com/search?q=JsGetPropertyNameFromId)                           | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsGetPrototype**](https://www.bing.com/search?q=JsGetPrototype)                                             | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsGetRuntime**](https://www.bing.com/search?q=JsGetRuntime)                                                 | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsGetRuntimeMemoryLimit**](https://www.bing.com/search?q=JsGetRuntimeMemoryLimit)                           | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsGetRuntimeMemoryUsage**](https://www.bing.com/search?q=JsGetRuntimeMemoryUsage)                           | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsGetStringLength**](https://www.bing.com/search?q=JsGetStringLength)                                       | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsGetSymbolFromPropertyId**](https://www.bing.com/search?q=JsGetSymbolFromPropertyId)                       | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsGetTrueValue**](https://www.bing.com/search?q=JsGetTrueValue)                                             | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsGetTypedArrayStorage**](https://www.bing.com/search?q=JsGetTypedArrayStorage)                             | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsGetUndefinedValue**](https://www.bing.com/search?q=JsGetUndefinedValue)                                   | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsGetValueType**](https://www.bing.com/search?q=JsGetValueType)                                             | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsHasException**](https://www.bing.com/search?q=JsHasException)                                             | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsHasExternalData**](https://www.bing.com/search?q=JsHasExternalData)                                       | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsHasIndexedPropertiesExternalData**](https://www.bing.com/search?q=JsHasIndexedPropertiesExternalData)     | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsHasIndexedProperty**](https://www.bing.com/search?q=JsHasIndexedProperty)                                 | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsHasProperty**](https://www.bing.com/search?q=JsHasProperty)                                               | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsIdle**](https://www.bing.com/search?q=JsIdle)                                                             | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsInspectableToObject**](https://www.bing.com/search?q=JsInspectableToObject)                               | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsIntToNumber**](https://www.bing.com/search?q=JsIntToNumber)                                               | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsIsRuntimeExecutionDisabled**](https://www.bing.com/search?q=JsIsRuntimeExecutionDisabled)                 | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsNumberToDouble**](https://www.bing.com/search?q=JsNumberToDouble)                                         | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsNumberToInt**](https://www.bing.com/search?q=JsNumberToInt)                                               | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsObjectToInspectable**](https://www.bing.com/search?q=JsObjectToInspectable)                               | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsParseScript**](https://www.bing.com/search?q=JsParseScript)                                               | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsParseSerializedScript**](https://www.bing.com/search?q=JsParseSerializedScript)                           | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsPointerToString**](https://www.bing.com/search?q=JsPointerToString)                                       | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsPreventExtension**](https://www.bing.com/search?q=JsPreventExtension)                                     | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsProjectWinRTNamespace**](https://www.bing.com/search?q=JsProjectWinRTNamespace)                           | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsRelease**](https://www.bing.com/search?q=JsRelease)                                                       | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsRunScript**](https://www.bing.com/search?q=JsRunScript)                                                   | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsRunSerializedScript**](https://www.bing.com/search?q=JsRunSerializedScript)                               | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsSerializeScript**](https://www.bing.com/search?q=JsSerializeScript)                                       | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsSetCurrentContext**](https://www.bing.com/search?q=JsSetCurrentContext)                                   | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsSetException**](https://www.bing.com/search?q=JsSetException)                                             | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsSetExternalData**](https://www.bing.com/search?q=JsSetExternalData)                                       | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsSetIndexedPropertiesToExternalData**](https://www.bing.com/search?q=JsSetIndexedPropertiesToExternalData) | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsSetIndexedProperty**](https://www.bing.com/search?q=JsSetIndexedProperty)                                 | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsSetObjectBeforeCollectCallback**](https://www.bing.com/search?q=JsSetObjectBeforeCollectCallback)         | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsSetProjectionEnqueueCallback**](https://www.bing.com/search?q=JsSetProjectionEnqueueCallback)             | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsSetPromiseContinuationCallback**](https://www.bing.com/search?q=JsSetPromiseContinuationCallback)         | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsSetProperty**](https://www.bing.com/search?q=JsSetProperty)                                               | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsSetPrototype**](https://www.bing.com/search?q=JsSetPrototype)                                             | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsSetRuntimeBeforeCollectCallback**](https://www.bing.com/search?q=JsSetRuntimeBeforeCollectCallback)       | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsSetRuntimeMemoryAllocationCallback**](https://www.bing.com/search?q=JsSetRuntimeMemoryAllocationCallback) | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsSetRuntimeMemoryLimit**](https://www.bing.com/search?q=JsSetRuntimeMemoryLimit)                           | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsStartDebugging**](https://www.bing.com/search?q=JsStartDebugging)                                         | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsStrictEquals**](https://www.bing.com/search?q=JsStrictEquals)                                             | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsStringToPointer**](https://www.bing.com/search?q=JsStringToPointer)                                       | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsValueToVariant**](https://www.bing.com/search?q=JsValueToVariant)                                         | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsVariantToValue**](https://www.bing.com/search?q=JsVariantToValue)                                         | Introduced into chakra.dll in Windows 10.0.10240.0 |
| [**JsGetContextData**](https://www.bing.com/search?q=JsGetContextData)                                         | Introduced into chakra.dll in Windows 10.0.10586.0 |
| [**JsGetContextOfObject**](https://www.bing.com/search?q=JsGetContextOfObject)                                 | Introduced into chakra.dll in Windows 10.0.10586.0 |
| [**JsGetTypedArrayInfo**](https://www.bing.com/search?q=JsGetTypedArrayInfo)                                   | Introduced into chakra.dll in Windows 10.0.10586.0 |
| [**JsInstanceOf**](https://www.bing.com/search?q=JsInstanceOf)                                                 | Introduced into chakra.dll in Windows 10.0.10586.0 |
| [**JsParseSerializedScriptWithCallback**](https://www.bing.com/search?q=JsParseSerializedScriptWithCallback)   | Introduced into chakra.dll in Windows 10.0.10586.0 |
| [**JsRunSerializedScriptWithCallback**](https://www.bing.com/search?q=JsRunSerializedScriptWithCallback)       | Introduced into chakra.dll in Windows 10.0.10586.0 |
| [**JsSetContextData**](https://www.bing.com/search?q=JsSetContextData)                                         | Introduced into chakra.dll in Windows 10.0.10586.0 |
| [**JsCreateExternalArrayBuffer**](https://www.bing.com/search?q=JsCreateExternalArrayBuffer)                   | Introduced into chakra.dll in Windows 10.0.14393.0 |

 

## <span id="_CRYPT32.DLL"></span>APIs from the dll crypt32.dll


| API                                                                                             | Requirements                                        |
|-------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| [**CertAddCertificateContextToStore**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376009.aspx)               | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertAddCertificateLinkToStore**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376010.aspx)                     | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertAddCRLContextToStore**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376011.aspx)                               | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertAddCRLLinkToStore**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376012.aspx)                                     | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertAddCTLContextToStore**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376013.aspx)                               | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertAddCTLLinkToStore**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376014.aspx)                                     | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertAddEncodedCertificateToStore**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376015.aspx)               | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertAddEncodedCRLToStore**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376016.aspx)                               | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertAddEncodedCTLToStore**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376017.aspx)                               | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertAddSerializedElementToStore**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376021.aspx)                 | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertAddStoreToCollection**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376022.aspx)                               | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertCloseStore**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376026.aspx)                                                   | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertCompareCertificate**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376027.aspx)                                   | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertCompareCertificateName**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376028.aspx)                           | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertCompareIntegerBlob**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376029.aspx)                                   | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertControlStore**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376031.aspx)                                               | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertCreateCertificateChainEngine**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376032.aspx)               | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertCreateCertificateContext**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376033.aspx)                       | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertCreateContext**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376035.aspx)                                             | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertCreateCRLContext**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376036.aspx)                                       | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertCreateCTLContext**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376037.aspx)                                       | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertCreateSelfSignCertificate**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376039.aspx)                     | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertDeleteCertificateFromStore**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376040.aspx)                   | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertDeleteCRLFromStore**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376041.aspx)                                   | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertDeleteCTLFromStore**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376042.aspx)                                   | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertDuplicateCertificateChain**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376044.aspx)                     | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertDuplicateCertificateContext**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376045.aspx)                 | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertDuplicateCRLContext**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376046.aspx)                                 | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertDuplicateCTLContext**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376047.aspx)                                 | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertDuplicateStore**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376048.aspx)                                           | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertEnumCertificateContextProperties**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376049.aspx)       | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertEnumCertificatesInStore**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376050.aspx)                         | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertEnumCRLContextProperties**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376051.aspx)                       | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertEnumCRLsInStore**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376052.aspx)                                         | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertEnumCTLContextProperties**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376053.aspx)                       | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertEnumCTLsInStore**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376054.aspx)                                         | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertEnumPhysicalStore**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376055.aspx)                                     | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertEnumSystemStore**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376058.aspx)                                         | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertEnumSystemStoreLocation**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376060.aspx)                         | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertFindAttribute**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376062.aspx)                                             | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertFindCertificateInCRL**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376063.aspx)                               | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertFindCertificateInStore**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376064.aspx)                           | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertFindCRLInStore**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376066.aspx)                                           | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertFindCTLInStore**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376067.aspx)                                           | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertFindExtension**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376068.aspx)                                             | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertFindRDNAttr**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376069.aspx)                                                 | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertFindSubjectInCTL**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376071.aspx)                                       | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertFreeCertificateChain**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376073.aspx)                               | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertFreeCertificateChainEngine**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376074.aspx)                   | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertFreeCertificateChainList**](https://msdn.microsoft.com/en-us/library/windows/apps/dd433796.aspx)                       | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertFreeCertificateContext**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376075.aspx)                           | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertFreeCRLContext**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376076.aspx)                                           | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertFreeCTLContext**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376077.aspx)                                           | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertGetCertificateChain**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376078.aspx)                                 | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertGetCertificateContextProperty**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376079.aspx)             | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertGetCRLContextProperty**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376080.aspx)                             | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertGetCRLFromStore**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376081.aspx)                                         | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertGetCTLContextProperty**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376082.aspx)                             | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertGetEnhancedKeyUsage**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376083.aspx)                                 | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertGetIntendedKeyUsage**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376084.aspx)                                 | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertGetIssuerCertificateFromStore**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376085.aspx)             | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertGetNameStringA**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376086.aspx)                                            | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertGetNameStringW**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376086.aspx)                                            | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertGetPublicKeyLength**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376087.aspx)                                   | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertGetStoreProperty**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376089.aspx)                                       | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertGetSubjectCertificateFromStore**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376090.aspx)           | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertGetValidUsages**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376091.aspx)                                           | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertIsValidCRLForCertificate**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376552.aspx)                       | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertNameToStrA**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376556.aspx)                                                    | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertNameToStrW**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376556.aspx)                                                    | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertOpenStore**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376559.aspx)                                                     | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertRDNValueToStrA**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376561.aspx)                                            | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertRDNValueToStrW**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376561.aspx)                                            | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertRemoveStoreFromCollection**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376565.aspx)                     | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertResyncCertificateChainEngine**](https://msdn.microsoft.com/en-us/library/windows/apps/mt270087.aspx)               | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertSaveStore**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376567.aspx)                                                     | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertSelectCertificateChains**](https://msdn.microsoft.com/en-us/library/windows/apps/dd433797.aspx)                         | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertSerializeCertificateStoreElement**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376569.aspx)       | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertSerializeCRLStoreElement**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376570.aspx)                       | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertSerializeCTLStoreElement**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376571.aspx)                       | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertSetCertificateContextProperty**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376573.aspx)             | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertSetCRLContextProperty**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376574.aspx)                             | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertSetCTLContextProperty**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376575.aspx)                             | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertSetStoreProperty**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376577.aspx)                                       | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertStrToNameA**](https://www.bing.com/search?q=CertStrToNameA)                              | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertStrToNameW**](https://www.bing.com/search?q=CertStrToNameW)                              | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertVerifyCertificateChainPolicy**](https://msdn.microsoft.com/en-us/library/windows/apps/aa377163.aspx)               | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertVerifySubjectCertificateContext**](https://msdn.microsoft.com/en-us/library/windows/apps/aa377168.aspx)         | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CertVerifyTimeValidity**](https://msdn.microsoft.com/en-us/library/windows/apps/aa377169.aspx)                                   | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CryptAcquireCertificatePrivateKey**](https://msdn.microsoft.com/en-us/library/windows/apps/aa379885.aspx)             | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CryptDecodeObject**](https://msdn.microsoft.com/en-us/library/windows/apps/aa379911.aspx)                                             | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CryptDecodeObjectEx**](https://msdn.microsoft.com/en-us/library/windows/apps/aa379912.aspx)                                         | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CryptEncodeObject**](https://msdn.microsoft.com/en-us/library/windows/apps/aa379921.aspx)                                             | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CryptEncodeObjectEx**](https://msdn.microsoft.com/en-us/library/windows/apps/aa379922.aspx)                                         | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CryptEnumOIDFunction**](https://msdn.microsoft.com/en-us/library/windows/apps/aa379927.aspx)                                       | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CryptEnumOIDInfo**](https://msdn.microsoft.com/en-us/library/windows/apps/aa379928.aspx)                                               | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CryptFindLocalizedName**](https://msdn.microsoft.com/en-us/library/windows/apps/aa379937.aspx)                                   | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CryptFindOIDInfo**](https://msdn.microsoft.com/en-us/library/windows/apps/aa379938.aspx)                                               | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CryptFormatObject**](https://msdn.microsoft.com/en-us/library/windows/apps/aa379939.aspx)                                             | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CryptFreeOIDFunctionAddress**](https://msdn.microsoft.com/en-us/library/windows/apps/aa379940.aspx)                         | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CryptGetDefaultOIDDllList**](https://msdn.microsoft.com/en-us/library/windows/apps/aa379943.aspx)                             | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CryptGetDefaultOIDFunctionAddress**](https://msdn.microsoft.com/en-us/library/windows/apps/aa379944.aspx)             | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CryptGetOIDFunctionAddress**](https://msdn.microsoft.com/en-us/library/windows/apps/aa380088.aspx)                           | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CryptGetOIDFunctionValue**](https://msdn.microsoft.com/en-us/library/windows/apps/aa380187.aspx)                               | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CryptHashPublicKeyInfo**](https://msdn.microsoft.com/en-us/library/windows/apps/aa380204.aspx)                                   | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CryptInitOIDFunctionSet**](https://msdn.microsoft.com/en-us/library/windows/apps/aa380212.aspx)                                 | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CryptInstallOIDFunctionAddress**](https://msdn.microsoft.com/en-us/library/windows/apps/aa380214.aspx)                   | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CryptMsgCalculateEncodedLength**](https://msdn.microsoft.com/en-us/library/windows/apps/aa380218.aspx)                   | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CryptMsgClose**](https://msdn.microsoft.com/en-us/library/windows/apps/aa380219.aspx)                                                     | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CryptMsgControl**](https://msdn.microsoft.com/en-us/library/windows/apps/aa380220.aspx)                                                 | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CryptMsgCountersign**](https://msdn.microsoft.com/en-us/library/windows/apps/aa380221.aspx)                                         | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CryptMsgCountersignEncoded**](https://msdn.microsoft.com/en-us/library/windows/apps/aa380223.aspx)                           | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CryptMsgDuplicate**](https://msdn.microsoft.com/en-us/library/windows/apps/aa380224.aspx)                                             | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CryptMsgGetAndVerifySigner**](https://msdn.microsoft.com/en-us/library/windows/apps/aa380226.aspx)                           | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CryptMsgGetParam**](https://msdn.microsoft.com/en-us/library/windows/apps/aa380227.aspx)                                               | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CryptMsgOpenToDecode**](https://msdn.microsoft.com/en-us/library/windows/apps/aa380228.aspx)                                       | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CryptMsgOpenToEncode**](https://msdn.microsoft.com/en-us/library/windows/apps/aa380229.aspx)                                       | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CryptMsgUpdate**](https://msdn.microsoft.com/en-us/library/windows/apps/aa380231.aspx)                                                   | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CryptMsgVerifyCountersignatureEncoded**](https://msdn.microsoft.com/en-us/library/windows/apps/aa380232.aspx)     | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CryptMsgVerifyCountersignatureEncodedEx**](https://msdn.microsoft.com/en-us/library/windows/apps/aa380233.aspx) | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CryptProtectData**](https://msdn.microsoft.com/en-us/library/windows/apps/aa380261.aspx)                                               | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CryptQueryObject**](https://msdn.microsoft.com/en-us/library/windows/apps/aa380264.aspx)                                               | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CryptRetrieveTimeStamp**](https://msdn.microsoft.com/en-us/library/windows/apps/dd433803.aspx)                                   | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CryptUnprotectData**](https://msdn.microsoft.com/en-us/library/windows/apps/aa380882.aspx)                                           | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**CryptVerifyTimeStampSignature**](https://msdn.microsoft.com/en-us/library/windows/apps/dd433804.aspx)                     | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**PFXExportCertStore**](https://msdn.microsoft.com/en-us/library/windows/apps/aa387311.aspx)                                           | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**PFXExportCertStoreEx**](https://msdn.microsoft.com/en-us/library/windows/apps/aa387313.aspx)                                       | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**PFXImportCertStore**](https://msdn.microsoft.com/en-us/library/windows/apps/aa387314.aspx)                                           | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**PFXIsPFXBlob**](https://msdn.microsoft.com/en-us/library/windows/apps/aa387316.aspx)                                                       | Introduced into crypt32.dll in Windows 10.0.10240.0 |
| [**PFXVerifyPassword**](https://msdn.microsoft.com/en-us/library/windows/apps/aa387319.aspx)                                             | Introduced into crypt32.dll in Windows 10.0.10240.0 |

 

## <span id="_D2D1.DLL"></span>APIs from the dll d2d1.dll


| API                                                                                                             | Requirements                                     |
|-----------------------------------------------------------------------------------------------------------------|--------------------------------------------------|
| [**D2D1ComputeMaximumScaleFactor**](https://msdn.microsoft.com/en-us/library/windows/apps/dn280381.aspx)                                     | Introduced into d2d1.dll in Windows 10.0.10240.0 |
| [**D2D1ConvertColorSpace**](https://msdn.microsoft.com/en-us/library/windows/apps/hh847939.aspx)                                                     | Introduced into d2d1.dll in Windows 10.0.10240.0 |
| [**D2D1CreateDevice**](https://msdn.microsoft.com/en-us/library/windows/apps/hh404272.aspx)                                                               | Introduced into d2d1.dll in Windows 10.0.10240.0 |
| [**D2D1CreateDeviceContext**](https://msdn.microsoft.com/en-us/library/windows/apps/hh404273.aspx)                                                 | Introduced into d2d1.dll in Windows 10.0.10240.0 |
| [**D2D1CreateFactory**](https://www.bing.com/search?q=D2D1CreateFactory)                                        | Introduced into d2d1.dll in Windows 10.0.10240.0 |
| [**D2D1GetGradientMeshInteriorPointsFromCoonsPatch**](https://msdn.microsoft.com/en-us/library/windows/apps/mt149083.aspx) | Introduced into d2d1.dll in Windows 10.0.10240.0 |
| [**D2D1InvertMatrix**](https://msdn.microsoft.com/en-us/library/windows/apps/dd368044.aspx)                                                               | Introduced into d2d1.dll in Windows 10.0.10240.0 |
| [**D2D1IsMatrixInvertible**](https://msdn.microsoft.com/en-us/library/windows/apps/dd368045.aspx)                                                   | Introduced into d2d1.dll in Windows 10.0.10240.0 |
| [**D2D1MakeRotateMatrix**](https://msdn.microsoft.com/en-us/library/windows/apps/dd368049.aspx)                                                       | Introduced into d2d1.dll in Windows 10.0.10240.0 |
| [**D2D1MakeSkewMatrix**](https://msdn.microsoft.com/en-us/library/windows/apps/dd368052.aspx)                                                           | Introduced into d2d1.dll in Windows 10.0.10240.0 |
| [**D2D1SinCos**](https://msdn.microsoft.com/en-us/library/windows/apps/hh847940.aspx)                                                                           | Introduced into d2d1.dll in Windows 10.0.10240.0 |
| [**D2D1Tan**](https://msdn.microsoft.com/en-us/library/windows/apps/hh847941.aspx)                                                                                 | Introduced into d2d1.dll in Windows 10.0.10240.0 |
| [**D2D1Vec3Length**](https://msdn.microsoft.com/en-us/library/windows/apps/hh847942.aspx)                                                                   | Introduced into d2d1.dll in Windows 10.0.10240.0 |

 

## <span id="_D3D11.DLL"></span>APIs from the dll d3d11.dll


| API                                                                                                                | Requirements                                      |
|--------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| [**CreateDirect3D11DeviceFromDXGIDevice**](https://www.bing.com/search?q=CreateDirect3D11DeviceFromDXGIDevice)     | Introduced into d3d11.dll in Windows 10.0.10240.0 |
| [**CreateDirect3D11SurfaceFromDXGISurface**](https://www.bing.com/search?q=CreateDirect3D11SurfaceFromDXGISurface) | Introduced into d3d11.dll in Windows 10.0.10240.0 |
| [**D3D11CreateDevice**](https://msdn.microsoft.com/en-us/library/windows/apps/ff476082.aspx)                                                              | Introduced into d3d11.dll in Windows 10.0.10240.0 |
| [**D3D11On12CreateDevice**](https://www.bing.com/search?q=D3D11On12CreateDevice)                                   | Introduced into d3d11.dll in Windows 10.0.10240.0 |

 

## <span id="_D3D12.DLL"></span>APIs from the dll d3d12.dll


| API                                                                                                            | Requirements                                      |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| [**D3D12CreateDevice**](https://www.bing.com/search?q=D3D12CreateDevice)                                       | Introduced into d3d12.dll in Windows 10.0.10240.0 |
| [**D3D12CreateRootSignatureDeserializer**](https://www.bing.com/search?q=D3D12CreateRootSignatureDeserializer) | Introduced into d3d12.dll in Windows 10.0.10240.0 |
| [**D3D12SerializeRootSignature**](https://www.bing.com/search?q=D3D12SerializeRootSignature)                   | Introduced into d3d12.dll in Windows 10.0.10240.0 |

 

## <span id="_D3DCOMPILER_47.DLL"></span>APIs from the dll d3dcompiler\_47.dll


| API                                                                                     | Requirements                                                |
|-----------------------------------------------------------------------------------------|-------------------------------------------------------------|
| [**D3DCompile**](https://msdn.microsoft.com/en-us/library/windows/apps/dd607324.aspx)                                               | Introduced into d3dcompiler\_47.dll in Windows 10.0.10240.0 |
| [**D3DCompile2**](https://msdn.microsoft.com/en-us/library/windows/apps/hh446869.aspx)                                             | Introduced into d3dcompiler\_47.dll in Windows 10.0.10240.0 |
| [**D3DCompileFromFile**](https://msdn.microsoft.com/en-us/library/windows/apps/hh446872.aspx)                               | Introduced into d3dcompiler\_47.dll in Windows 10.0.10240.0 |
| [**D3DCompressShaders**](https://msdn.microsoft.com/en-us/library/windows/apps/ff728671.aspx)                               | Introduced into d3dcompiler\_47.dll in Windows 10.0.10240.0 |
| [**D3DCreateBlob**](https://msdn.microsoft.com/en-us/library/windows/apps/ff728672.aspx)                                         | Introduced into d3dcompiler\_47.dll in Windows 10.0.10240.0 |
| [**D3DCreateFunctionLinkingGraph**](https://msdn.microsoft.com/en-us/library/windows/apps/dn280340.aspx)         | Introduced into d3dcompiler\_47.dll in Windows 10.0.10240.0 |
| [**D3DCreateLinker**](https://msdn.microsoft.com/en-us/library/windows/apps/dn280341.aspx)                                     | Introduced into d3dcompiler\_47.dll in Windows 10.0.10240.0 |
| [**D3DDecompressShaders**](https://msdn.microsoft.com/en-us/library/windows/apps/ff728673.aspx)                           | Introduced into d3dcompiler\_47.dll in Windows 10.0.10240.0 |
| [**D3DDisassemble**](https://msdn.microsoft.com/en-us/library/windows/apps/dd607326.aspx)                                       | Introduced into d3dcompiler\_47.dll in Windows 10.0.10240.0 |
| [**D3DDisassemble11Trace**](https://msdn.microsoft.com/en-us/library/windows/apps/dn933259.aspx)                           | Introduced into d3dcompiler\_47.dll in Windows 10.0.10240.0 |
| [**D3DDisassembleRegion**](https://msdn.microsoft.com/en-us/library/windows/apps/hh706344.aspx)                           | Introduced into d3dcompiler\_47.dll in Windows 10.0.10240.0 |
| [**D3DGetBlobPart**](https://msdn.microsoft.com/en-us/library/windows/apps/ff728674.aspx)                                       | Introduced into d3dcompiler\_47.dll in Windows 10.0.10240.0 |
| [**D3DGetDebugInfo**](https://msdn.microsoft.com/en-us/library/windows/apps/dd607328.aspx)                                     | Introduced into d3dcompiler\_47.dll in Windows 10.0.10240.0 |
| [**D3DGetInputAndOutputSignatureBlob**](https://msdn.microsoft.com/en-us/library/windows/apps/dd607329.aspx) | Introduced into d3dcompiler\_47.dll in Windows 10.0.10240.0 |
| [**D3DGetInputSignatureBlob**](https://msdn.microsoft.com/en-us/library/windows/apps/dd607330.aspx)                   | Introduced into d3dcompiler\_47.dll in Windows 10.0.10240.0 |
| [**D3DGetOutputSignatureBlob**](https://msdn.microsoft.com/en-us/library/windows/apps/dd607331.aspx)                 | Introduced into d3dcompiler\_47.dll in Windows 10.0.10240.0 |
| [**D3DGetTraceInstructionOffsets**](https://msdn.microsoft.com/en-us/library/windows/apps/hh446875.aspx)         | Introduced into d3dcompiler\_47.dll in Windows 10.0.10240.0 |
| [**D3DLoadModule**](https://msdn.microsoft.com/en-us/library/windows/apps/dn280342.aspx)                                         | Introduced into d3dcompiler\_47.dll in Windows 10.0.10240.0 |
| [**D3DPreprocess**](https://msdn.microsoft.com/en-us/library/windows/apps/dd607332.aspx)                                         | Introduced into d3dcompiler\_47.dll in Windows 10.0.10240.0 |
| [**D3DReadFileToBlob**](https://msdn.microsoft.com/en-us/library/windows/apps/hh446877.aspx)                                 | Introduced into d3dcompiler\_47.dll in Windows 10.0.10240.0 |
| [**D3DReflect**](https://msdn.microsoft.com/en-us/library/windows/apps/dd607334.aspx)                                               | Introduced into d3dcompiler\_47.dll in Windows 10.0.10240.0 |
| [**D3DReflectLibrary**](https://msdn.microsoft.com/en-us/library/windows/apps/dn280343.aspx)                                 | Introduced into d3dcompiler\_47.dll in Windows 10.0.10240.0 |
| [**D3DSetBlobPart**](https://msdn.microsoft.com/en-us/library/windows/apps/hh446880.aspx)                                       | Introduced into d3dcompiler\_47.dll in Windows 10.0.10240.0 |
| [**D3DStripShader**](https://msdn.microsoft.com/en-us/library/windows/apps/dd607335.aspx)                                       | Introduced into d3dcompiler\_47.dll in Windows 10.0.10240.0 |
| [**D3DWriteBlobToFile**](https://msdn.microsoft.com/en-us/library/windows/apps/hh446883.aspx)                               | Introduced into d3dcompiler\_47.dll in Windows 10.0.10240.0 |

 

## <span id="_DEVICEACCESS.DLL"></span>APIs from the dll deviceaccess.dll


| API                                                                       | Requirements                                             |
|---------------------------------------------------------------------------|----------------------------------------------------------|
| [**CreateDeviceAccessInstance**](https://msdn.microsoft.com/en-us/library/windows/apps/hh404237.aspx) | Introduced into deviceaccess.dll in Windows 10.0.10240.0 |

 

## <span id="_DHCPCSVC.DLL"></span>APIs from the dll dhcpcsvc.dll


| API                                               | Requirements                                         |
|---------------------------------------------------|------------------------------------------------------|
| [**DhcpCApiCleanup**](https://msdn.microsoft.com/en-us/library/windows/apps/aa363272.aspx)       | Introduced into dhcpcsvc.dll in Windows 10.0.10240.0 |
| [**DhcpCApiInitialize**](https://msdn.microsoft.com/en-us/library/windows/apps/aa363273.aspx) | Introduced into dhcpcsvc.dll in Windows 10.0.10240.0 |
| [**DhcpRequestParams**](https://msdn.microsoft.com/en-us/library/windows/apps/aa363298.aspx)   | Introduced into dhcpcsvc.dll in Windows 10.0.10240.0 |

 

## <span id="_DHCPCSVC6.DLL"></span>APIs from the dll dhcpcsvc6.dll


| API                                                   | Requirements                                          |
|-------------------------------------------------------|-------------------------------------------------------|
| [**Dhcpv6CApiCleanup**](https://msdn.microsoft.com/en-us/library/windows/apps/aa363305.aspx)       | Introduced into dhcpcsvc6.dll in Windows 10.0.10240.0 |
| [**Dhcpv6CApiInitialize**](https://msdn.microsoft.com/en-us/library/windows/apps/aa363306.aspx) | Introduced into dhcpcsvc6.dll in Windows 10.0.10240.0 |
| [**Dhcpv6RequestParams**](https://msdn.microsoft.com/en-us/library/windows/apps/aa363327.aspx)   | Introduced into dhcpcsvc6.dll in Windows 10.0.10240.0 |

 

## <span id="_DWRITE.DLL"></span>APIs from the dll dwrite.dll


| API                                                        | Requirements                                       |
|------------------------------------------------------------|----------------------------------------------------|
| [**DWriteCreateFactory**](https://msdn.microsoft.com/en-us/library/windows/apps/dd368040.aspx) | Introduced into dwrite.dll in Windows 10.0.10240.0 |

 

## <span id="_DXGI.DLL"></span>APIs from the dll dxgi.dll


| API                                                       | Requirements                                     |
|-----------------------------------------------------------|--------------------------------------------------|
| [**CreateDXGIFactory1**](https://msdn.microsoft.com/en-us/library/windows/apps/ff471318.aspx) | Introduced into dxgi.dll in Windows 10.0.10240.0 |
| [**CreateDXGIFactory2**](https://msdn.microsoft.com/en-us/library/windows/apps/dn268307.aspx) | Introduced into dxgi.dll in Windows 10.0.10240.0 |

 

## <span id="_ESENT.DLL"></span>APIs from the dll esent.dll


| API                                                                                              | Requirements                                      |
|--------------------------------------------------------------------------------------------------|---------------------------------------------------|
| [**JetAddColumnW**](https://www.bing.com/search?q=JetAddColumnW)                                 | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetAttachDatabase2W**](https://www.bing.com/search?q=JetAttachDatabase2W)                     | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetBackupInstanceW**](https://www.bing.com/search?q=JetBackupInstanceW)                       | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetBeginSessionW**](https://www.bing.com/search?q=JetBeginSessionW)                           | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetBeginTransaction3**](https://www.bing.com/search?q=JetBeginTransaction3)                   | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetCloseDatabase**](https://www.bing.com/search?q=JetCloseDatabase)                           | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetCloseTable**](https://www.bing.com/search?q=JetCloseTable)                                 | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetCommitTransaction**](https://www.bing.com/search?q=JetCommitTransaction)                   | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetCommitTransaction2**](https://www.bing.com/search?q=JetCommitTransaction2)                 | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetCreateDatabase2W**](https://www.bing.com/search?q=JetCreateDatabase2W)                     | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetCreateIndex4W**](https://www.bing.com/search?q=JetCreateIndex4W)                           | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetCreateInstance2W**](https://www.bing.com/search?q=JetCreateInstance2W)                     | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetCreateTableColumnIndex4W**](https://www.bing.com/search?q=JetCreateTableColumnIndex4W)     | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetDefragment2W**](https://www.bing.com/search?q=JetDefragment2W)                             | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetDelete**](https://www.bing.com/search?q=JetDelete)                                         | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetDeleteColumn2W**](https://www.bing.com/search?q=JetDeleteColumn2W)                         | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetDeleteIndexW**](https://www.bing.com/search?q=JetDeleteIndexW)                             | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetDeleteTableW**](https://www.bing.com/search?q=JetDeleteTableW)                             | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetDetachDatabase2W**](https://www.bing.com/search?q=JetDetachDatabase2W)                     | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetEndSession**](https://www.bing.com/search?q=JetEndSession)                                 | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetEnumerateColumns**](https://www.bing.com/search?q=JetEnumerateColumns)                     | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetEscrowUpdate**](https://www.bing.com/search?q=JetEscrowUpdate)                             | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetGetBookmark**](https://www.bing.com/search?q=JetGetBookmark)                               | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetGetColumnInfoW**](https://www.bing.com/search?q=JetGetColumnInfoW)                         | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetGetCurrentIndexW**](https://www.bing.com/search?q=JetGetCurrentIndexW)                     | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetGetDatabaseFileInfoW**](https://www.bing.com/search?q=JetGetDatabaseFileInfoW)             | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetGetDatabaseInfoW**](https://www.bing.com/search?q=JetGetDatabaseInfoW)                     | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetGetErrorInfoW**](https://www.bing.com/search?q=JetGetErrorInfoW)                           | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetGetIndexInfoW**](https://www.bing.com/search?q=JetGetIndexInfoW)                           | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetGetObjectInfoW**](https://www.bing.com/search?q=JetGetObjectInfoW)                         | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetGetRecordPosition**](https://www.bing.com/search?q=JetGetRecordPosition)                   | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetGetSecondaryIndexBookmark**](https://www.bing.com/search?q=JetGetSecondaryIndexBookmark)   | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetGetSessionParameter**](https://www.bing.com/search?q=JetGetSessionParameter)               | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetGetSystemParameterW**](https://www.bing.com/search?q=JetGetSystemParameterW)               | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetGetTableColumnInfoW**](https://www.bing.com/search?q=JetGetTableColumnInfoW)               | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetGetTableIndexInfoW**](https://www.bing.com/search?q=JetGetTableIndexInfoW)                 | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetGetTableInfoW**](https://www.bing.com/search?q=JetGetTableInfoW)                           | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetGetThreadStats**](https://www.bing.com/search?q=JetGetThreadStats)                         | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetGotoBookmark**](https://www.bing.com/search?q=JetGotoBookmark)                             | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetGotoPosition**](https://www.bing.com/search?q=JetGotoPosition)                             | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetGotoSecondaryIndexBookmark**](https://www.bing.com/search?q=JetGotoSecondaryIndexBookmark) | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetIndexRecordCount**](https://www.bing.com/search?q=JetIndexRecordCount)                     | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetInit3W**](https://www.bing.com/search?q=JetInit3W)                                         | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetIntersectIndexes**](https://www.bing.com/search?q=JetIntersectIndexes)                     | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetMakeKey**](https://www.bing.com/search?q=JetMakeKey)                                       | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetMove**](https://www.bing.com/search?q=JetMove)                                             | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetOpenDatabaseW**](https://www.bing.com/search?q=JetOpenDatabaseW)                           | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetOpenTableW**](https://www.bing.com/search?q=JetOpenTableW)                                 | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetOpenTemporaryTable2**](https://www.bing.com/search?q=JetOpenTemporaryTable2)               | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetOpenTempTable3**](https://www.bing.com/search?q=JetOpenTempTable3)                         | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetPrepareUpdate**](https://www.bing.com/search?q=JetPrepareUpdate)                           | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetPrereadIndexRanges**](https://www.bing.com/search?q=JetPrereadIndexRanges)                 | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetPrereadKeys**](https://www.bing.com/search?q=JetPrereadKeys)                               | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetRegisterCallback**](https://www.bing.com/search?q=JetRegisterCallback)                     | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetRenameColumnW**](https://www.bing.com/search?q=JetRenameColumnW)                           | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetRenameTableW**](https://www.bing.com/search?q=JetRenameTableW)                             | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetResetSessionContext**](https://www.bing.com/search?q=JetResetSessionContext)               | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetResetTableSequential**](https://www.bing.com/search?q=JetResetTableSequential)             | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetResizeDatabase**](https://www.bing.com/search?q=JetResizeDatabase)                         | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetRestoreInstanceW**](https://www.bing.com/search?q=JetRestoreInstanceW)                     | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetRetrieveColumn**](https://www.bing.com/search?q=JetRetrieveColumn)                         | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetRetrieveColumns**](https://www.bing.com/search?q=JetRetrieveColumns)                       | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetRetrieveKey**](https://www.bing.com/search?q=JetRetrieveKey)                               | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetRollback**](https://www.bing.com/search?q=JetRollback)                                     | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetSeek**](https://www.bing.com/search?q=JetSeek)                                             | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetSetColumn**](https://www.bing.com/search?q=JetSetColumn)                                   | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetSetColumns**](https://www.bing.com/search?q=JetSetColumns)                                 | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetSetCurrentIndex4W**](https://www.bing.com/search?q=JetSetCurrentIndex4W)                   | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetSetCursorFilter**](https://www.bing.com/search?q=JetSetCursorFilter)                       | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetSetIndexRange**](https://www.bing.com/search?q=JetSetIndexRange)                           | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetSetSessionContext**](https://www.bing.com/search?q=JetSetSessionContext)                   | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetSetSessionParameter**](https://www.bing.com/search?q=JetSetSessionParameter)               | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetSetSystemParameterW**](https://www.bing.com/search?q=JetSetSystemParameterW)               | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetSetTableSequential**](https://www.bing.com/search?q=JetSetTableSequential)                 | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetStopBackupInstance**](https://www.bing.com/search?q=JetStopBackupInstance)                 | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetStopServiceInstance2**](https://www.bing.com/search?q=JetStopServiceInstance2)             | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetTerm2**](https://www.bing.com/search?q=JetTerm2)                                           | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetUnregisterCallback**](https://www.bing.com/search?q=JetUnregisterCallback)                 | Introduced into esent.dll in Windows 10.0.10240.0 |
| [**JetUpdate2**](https://www.bing.com/search?q=JetUpdate2)                                       | Introduced into esent.dll in Windows 10.0.10240.0 |

 

## <span id="_HRTFAPO.DLL"></span>APIs from the dll hrtfapo.dll


| API                                        | Requirements                                        |
|--------------------------------------------|-----------------------------------------------------|
| [**CreateHrtfApo**](https://msdn.microsoft.com/en-us/library/windows/apps/mt186596.aspx) | Introduced into hrtfapo.dll in Windows 10.0.10240.0 |

 

## <span id="_MF.DLL"></span>APIs from the dll mf.dll


| API                                                                                  | Requirements                                   |
|--------------------------------------------------------------------------------------|------------------------------------------------|
| [**MFCreateAggregateSource**](https://www.bing.com/search?q=MFCreateAggregateSource) | Introduced into mf.dll in Windows 10.0.10240.0 |
| [**MFCreateProtectedEnvironmentAccess**](https://msdn.microsoft.com/en-us/library/windows/apps/hh162758.aspx)      | Introduced into mf.dll in Windows 10.0.10240.0 |
| [**MFGetLocalId**](https://msdn.microsoft.com/en-us/library/windows/apps/jj128335.aspx)                                                  | Introduced into mf.dll in Windows 10.0.10240.0 |
| [**MFGetService**](https://msdn.microsoft.com/en-us/library/windows/apps/ms694284.aspx)                                                  | Introduced into mf.dll in Windows 10.0.10240.0 |
| [**MFGetSystemId**](https://msdn.microsoft.com/en-us/library/windows/apps/hh162767.aspx)                                                | Introduced into mf.dll in Windows 10.0.10240.0 |
| [**MFLoadSignedLibrary**](https://msdn.microsoft.com/en-us/library/windows/apps/hh162769.aspx)                                    | Introduced into mf.dll in Windows 10.0.10240.0 |

 

## <span id="_MFPLAT.DLL"></span>APIs from the dll mfplat.dll


| API                                                                                 | Requirements                                       |
|-------------------------------------------------------------------------------------|----------------------------------------------------|
| [**MFAllocateSerialWorkQueue**](https://msdn.microsoft.com/en-us/library/windows/apps/hh162744.aspx)                       | Introduced into mfplat.dll in Windows 10.0.10240.0 |
| [**MFCancelWorkItem**](https://msdn.microsoft.com/en-us/library/windows/apps/ms701633.aspx)                                         | Introduced into mfplat.dll in Windows 10.0.10240.0 |
| [**MFCopyImage**](https://msdn.microsoft.com/en-us/library/windows/apps/bb970554.aspx)                                                   | Introduced into mfplat.dll in Windows 10.0.10240.0 |
| [**MFCreate2DMediaBuffer**](https://msdn.microsoft.com/en-us/library/windows/apps/hh162746.aspx)                               | Introduced into mfplat.dll in Windows 10.0.10240.0 |
| [**MFCreateAlignedMemoryBuffer**](https://msdn.microsoft.com/en-us/library/windows/apps/bb970523.aspx)                   | Introduced into mfplat.dll in Windows 10.0.10240.0 |
| [**MFCreateAsyncResult**](https://msdn.microsoft.com/en-us/library/windows/apps/ms698952.aspx)                                   | Introduced into mfplat.dll in Windows 10.0.10240.0 |
| [**MFCreateAttributes**](https://msdn.microsoft.com/en-us/library/windows/apps/ms701878.aspx)                                     | Introduced into mfplat.dll in Windows 10.0.10240.0 |
| [**MFCreateCollection**](https://msdn.microsoft.com/en-us/library/windows/apps/ms698852.aspx)                                     | Introduced into mfplat.dll in Windows 10.0.10240.0 |
| [**MFCreateContentDecryptorContext**](https://msdn.microsoft.com/en-us/library/windows/apps/mt219224.aspx)           | Introduced into mfplat.dll in Windows 10.0.10240.0 |
| [**MFCreateContentProtectionDevice**](https://msdn.microsoft.com/en-us/library/windows/apps/mt219225.aspx)           | Introduced into mfplat.dll in Windows 10.0.10240.0 |
| [**MFCreateDXGIDeviceManager**](https://msdn.microsoft.com/en-us/library/windows/apps/hh162750.aspx)                       | Introduced into mfplat.dll in Windows 10.0.10240.0 |
| [**MFCreateDXGISurfaceBuffer**](https://msdn.microsoft.com/en-us/library/windows/apps/hh162751.aspx)                       | Introduced into mfplat.dll in Windows 10.0.10240.0 |
| [**MFCreateEventQueue**](https://msdn.microsoft.com/en-us/library/windows/apps/ms695252.aspx)                                     | Introduced into mfplat.dll in Windows 10.0.10240.0 |
| [**MFCreateMediaBufferFromMediaType**](https://msdn.microsoft.com/en-us/library/windows/apps/hh162752.aspx)         | Introduced into mfplat.dll in Windows 10.0.10240.0 |
| [**MFCreateMediaBufferWrapper**](https://msdn.microsoft.com/en-us/library/windows/apps/aa370450.aspx)                     | Introduced into mfplat.dll in Windows 10.0.10240.0 |
| [**MFCreateMediaEvent**](https://msdn.microsoft.com/en-us/library/windows/apps/ms697521.aspx)                                     | Introduced into mfplat.dll in Windows 10.0.10240.0 |
| [**MFCreateMediaExtensionActivate**](https://msdn.microsoft.com/en-us/library/windows/apps/hh162753.aspx)             | Introduced into mfplat.dll in Windows 10.0.10240.0 |
| [**MFCreateMediaType**](https://msdn.microsoft.com/en-us/library/windows/apps/ms693861.aspx)                                       | Introduced into mfplat.dll in Windows 10.0.10240.0 |
| [**MFCreateMediaTypeFromProperties**](https://msdn.microsoft.com/en-us/library/windows/apps/jj247579.aspx)           | Introduced into mfplat.dll in Windows 10.0.10240.0 |
| [**MFCreateMemoryBuffer**](https://msdn.microsoft.com/en-us/library/windows/apps/ms695212.aspx)                                 | Introduced into mfplat.dll in Windows 10.0.10240.0 |
| [**MFCreateMFByteStreamOnStreamEx**](https://msdn.microsoft.com/en-us/library/windows/apps/hh162754.aspx)             | Introduced into mfplat.dll in Windows 10.0.10240.0 |
| [**MFCreatePresentationDescriptor**](https://msdn.microsoft.com/en-us/library/windows/apps/ms695404.aspx)             | Introduced into mfplat.dll in Windows 10.0.10240.0 |
| [**MFCreatePropertiesFromMediaType**](https://msdn.microsoft.com/en-us/library/windows/apps/jj247580.aspx)           | Introduced into mfplat.dll in Windows 10.0.10240.0 |
| [**MFCreateSample**](https://msdn.microsoft.com/en-us/library/windows/apps/ms702276.aspx)                                             | Introduced into mfplat.dll in Windows 10.0.10240.0 |
| [**MFCreateSourceResolver**](https://msdn.microsoft.com/en-us/library/windows/apps/ms697433.aspx)                             | Introduced into mfplat.dll in Windows 10.0.10240.0 |
| [**MFCreateStreamDescriptor**](https://msdn.microsoft.com/en-us/library/windows/apps/ms698990.aspx)                         | Introduced into mfplat.dll in Windows 10.0.10240.0 |
| [**MFCreateStreamOnMFByteStreamEx**](https://msdn.microsoft.com/en-us/library/windows/apps/hh162760.aspx)             | Introduced into mfplat.dll in Windows 10.0.10240.0 |
| [**MFCreateTrackedSample**](https://msdn.microsoft.com/en-us/library/windows/apps/hh162761.aspx)                               | Introduced into mfplat.dll in Windows 10.0.10240.0 |
| [**MFCreateVideoSampleAllocatorEx**](https://msdn.microsoft.com/en-us/library/windows/apps/hh162763.aspx)             | Introduced into mfplat.dll in Windows 10.0.10240.0 |
| [**MFCreateWaveFormatExFromMFMediaType**](https://msdn.microsoft.com/en-us/library/windows/apps/ms702177.aspx)   | Introduced into mfplat.dll in Windows 10.0.10240.0 |
| [**MFDeserializeAttributesFromStream**](https://msdn.microsoft.com/en-us/library/windows/apps/ms703162.aspx)       | Introduced into mfplat.dll in Windows 10.0.10240.0 |
| [**MFGetAttributesAsBlob**](https://msdn.microsoft.com/en-us/library/windows/apps/ms694877.aspx)                               | Introduced into mfplat.dll in Windows 10.0.10240.0 |
| [**MFGetAttributesAsBlobSize**](https://msdn.microsoft.com/en-us/library/windows/apps/ms697064.aspx)                       | Introduced into mfplat.dll in Windows 10.0.10240.0 |
| [**MFGetSystemTime**](https://msdn.microsoft.com/en-us/library/windows/apps/ms704625.aspx)                                           | Introduced into mfplat.dll in Windows 10.0.10240.0 |
| [**MFInitAttributesFromBlob**](https://msdn.microsoft.com/en-us/library/windows/apps/ms703978.aspx)                         | Introduced into mfplat.dll in Windows 10.0.10240.0 |
| [**MFInitMediaTypeFromWaveFormatEx**](https://msdn.microsoft.com/en-us/library/windows/apps/ms700801.aspx)           | Introduced into mfplat.dll in Windows 10.0.10240.0 |
| [**MFInvokeCallback**](https://msdn.microsoft.com/en-us/library/windows/apps/ms695400.aspx)                                         | Introduced into mfplat.dll in Windows 10.0.10240.0 |
| [**MFIsContentProtectionDeviceSupported**](https://msdn.microsoft.com/en-us/library/windows/apps/mt219226.aspx) | Introduced into mfplat.dll in Windows 10.0.10240.0 |
| [**MFllMulDiv**](https://msdn.microsoft.com/en-us/library/windows/apps/dd388510.aspx)                                                     | Introduced into mfplat.dll in Windows 10.0.10240.0 |
| [**MFLockDXGIDeviceManager**](https://msdn.microsoft.com/en-us/library/windows/apps/hh162770.aspx)                           | Introduced into mfplat.dll in Windows 10.0.10240.0 |
| [**MFLockPlatform**](https://msdn.microsoft.com/en-us/library/windows/apps/ms693588.aspx)                                             | Introduced into mfplat.dll in Windows 10.0.10240.0 |
| [**MFLockSharedWorkQueue**](https://msdn.microsoft.com/en-us/library/windows/apps/hh162771.aspx)                               | Introduced into mfplat.dll in Windows 10.0.10240.0 |
| [**MFLockWorkQueue**](https://msdn.microsoft.com/en-us/library/windows/apps/aa367740.aspx)                                           | Introduced into mfplat.dll in Windows 10.0.10240.0 |
| [**MFPutWaitingWorkItem**](https://msdn.microsoft.com/en-us/library/windows/apps/hh162783.aspx)                                 | Introduced into mfplat.dll in Windows 10.0.10240.0 |
| [**MFPutWorkItem2**](https://msdn.microsoft.com/en-us/library/windows/apps/hh162784.aspx)                                             | Introduced into mfplat.dll in Windows 10.0.10240.0 |
| [**MFPutWorkItemEx2**](https://msdn.microsoft.com/en-us/library/windows/apps/hh162785.aspx)                                         | Introduced into mfplat.dll in Windows 10.0.10240.0 |
| [**MFSerializeAttributesToStream**](https://msdn.microsoft.com/en-us/library/windows/apps/ms702278.aspx)               | Introduced into mfplat.dll in Windows 10.0.10240.0 |
| [**MFShutdown**](https://msdn.microsoft.com/en-us/library/windows/apps/ms694273.aspx)                                                     | Introduced into mfplat.dll in Windows 10.0.10240.0 |
| [**MFStartup**](https://msdn.microsoft.com/en-us/library/windows/apps/ms702238.aspx)                                                       | Introduced into mfplat.dll in Windows 10.0.10240.0 |
| [**MFUnlockDXGIDeviceManager**](https://msdn.microsoft.com/en-us/library/windows/apps/hh162800.aspx)                       | Introduced into mfplat.dll in Windows 10.0.10240.0 |
| [**MFUnlockPlatform**](https://msdn.microsoft.com/en-us/library/windows/apps/ms703879.aspx)                                         | Introduced into mfplat.dll in Windows 10.0.10240.0 |
| [**MFUnlockWorkQueue**](https://msdn.microsoft.com/en-us/library/windows/apps/aa372543.aspx)                                       | Introduced into mfplat.dll in Windows 10.0.10240.0 |
| [**MFUnwrapMediaType**](https://msdn.microsoft.com/en-us/library/windows/apps/ms696190.aspx)                                       | Introduced into mfplat.dll in Windows 10.0.10240.0 |
| [**MFWrapMediaType**](https://msdn.microsoft.com/en-us/library/windows/apps/ms701782.aspx)                                           | Introduced into mfplat.dll in Windows 10.0.10240.0 |

 

## <span id="_MFREADWRITE.DLL"></span>APIs from the dll mfreadwrite.dll


| API                                                                               | Requirements                                            |
|-----------------------------------------------------------------------------------|---------------------------------------------------------|
| [**MFCreateSinkWriterFromMediaSink**](https://msdn.microsoft.com/en-us/library/windows/apps/dd388103.aspx)         | Introduced into mfreadwrite.dll in Windows 10.0.10240.0 |
| [**MFCreateSinkWriterFromURL**](https://msdn.microsoft.com/en-us/library/windows/apps/dd388105.aspx)                     | Introduced into mfreadwrite.dll in Windows 10.0.10240.0 |
| [**MFCreateSourceReaderFromByteStream**](https://msdn.microsoft.com/en-us/library/windows/apps/dd388106.aspx)   | Introduced into mfreadwrite.dll in Windows 10.0.10240.0 |
| [**MFCreateSourceReaderFromMediaSource**](https://msdn.microsoft.com/en-us/library/windows/apps/dd388108.aspx) | Introduced into mfreadwrite.dll in Windows 10.0.10240.0 |
| [**MFCreateSourceReaderFromURL**](https://msdn.microsoft.com/en-us/library/windows/apps/dd388110.aspx)                 | Introduced into mfreadwrite.dll in Windows 10.0.10240.0 |

 

## <span id="_MMDEVAPI.DLL"></span>APIs from the dll mmdevapi.dll


| API                                                                      | Requirements                                         |
|--------------------------------------------------------------------------|------------------------------------------------------|
| [**ActivateAudioInterfaceAsync**](https://msdn.microsoft.com/en-us/library/windows/apps/jj128298.aspx) | Introduced into mmdevapi.dll in Windows 10.0.10240.0 |

 

## <span id="_MSAJAPI.DLL"></span>APIs from the dll MSAJApi.dll


| API                                                                                                                                                                                            | Requirements                                        |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| [**alljoyn\_aboutdata\_create**](https://www.bing.com/search?q=alljoyn_aboutdata_create)                                                                                                       | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutdata\_create\_empty**](https://www.bing.com/search?q=alljoyn_aboutdata_create_empty)                                                                                          | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutdata\_create\_full**](https://www.bing.com/search?q=alljoyn_aboutdata_create_full)                                                                                            | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutdata\_createfrommsgarg**](https://www.bing.com/search?q=alljoyn_aboutdata_createfrommsgarg)                                                                                   | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutdata\_destroy**](https://www.bing.com/search?q=alljoyn_aboutdata_destroy)                                                                                                     | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutdata\_getaboutdata**](https://www.bing.com/search?q=alljoyn_aboutdata_getaboutdata)                                                                                           | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutdata\_getajsoftwareversion**](https://www.bing.com/search?q=alljoyn_aboutdata_getajsoftwareversion)                                                                           | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutdata\_getannouncedaboutdata**](https://www.bing.com/search?q=alljoyn_aboutdata_getannouncedaboutdata)                                                                         | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutdata\_getappid**](https://www.bing.com/search?q=alljoyn_aboutdata_getappid)                                                                                                   | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutdata\_getappname**](https://www.bing.com/search?q=alljoyn_aboutdata_getappname)                                                                                               | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutdata\_getdateofmanufacture**](https://www.bing.com/search?q=alljoyn_aboutdata_getdateofmanufacture)                                                                           | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutdata\_getdefaultlanguage**](https://www.bing.com/search?q=alljoyn_aboutdata_getdefaultlanguage)                                                                               | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutdata\_getdescription**](https://www.bing.com/search?q=alljoyn_aboutdata_getdescription)                                                                                       | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutdata\_getdeviceid**](https://www.bing.com/search?q=alljoyn_aboutdata_getdeviceid)                                                                                             | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutdata\_getdevicename**](https://www.bing.com/search?q=alljoyn_aboutdata_getdevicename)                                                                                         | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutdata\_getfield**](https://www.bing.com/search?q=alljoyn_aboutdata_getfield)                                                                                                   | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutdata\_getfields**](https://www.bing.com/search?q=alljoyn_aboutdata_getfields)                                                                                                 | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutdata\_getfieldsignature**](https://www.bing.com/search?q=alljoyn_aboutdata_getfieldsignature)                                                                                 | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutdata\_gethardwareversion**](https://www.bing.com/search?q=alljoyn_aboutdata_gethardwareversion)                                                                               | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutdata\_getmanufacturer**](https://www.bing.com/search?q=alljoyn_aboutdata_getmanufacturer)                                                                                     | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutdata\_getmodelnumber**](https://www.bing.com/search?q=alljoyn_aboutdata_getmodelnumber)                                                                                       | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutdata\_getsoftwareversion**](https://www.bing.com/search?q=alljoyn_aboutdata_getsoftwareversion)                                                                               | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutdata\_getsupportedlanguages**](https://www.bing.com/search?q=alljoyn_aboutdata_getsupportedlanguages)                                                                         | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutdata\_getsupporturl**](https://www.bing.com/search?q=alljoyn_aboutdata_getsupporturl)                                                                                         | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutdata\_isfieldannounced**](https://www.bing.com/search?q=alljoyn_aboutdata_isfieldannounced)                                                                                   | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutdata\_isfieldlocalized**](https://www.bing.com/search?q=alljoyn_aboutdata_isfieldlocalized)                                                                                   | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutdata\_isfieldrequired**](https://www.bing.com/search?q=alljoyn_aboutdata_isfieldrequired)                                                                                     | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutdata\_isvalid**](https://www.bing.com/search?q=alljoyn_aboutdata_isvalid)                                                                                                     | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutdata\_setappid**](https://www.bing.com/search?q=alljoyn_aboutdata_setappid)                                                                                                   | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutdata\_setappid\_fromstring**](https://www.bing.com/search?q=alljoyn_aboutdata_setappid_fromstring)                                                                            | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutdata\_setappname**](https://www.bing.com/search?q=alljoyn_aboutdata_setappname)                                                                                               | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutdata\_setdateofmanufacture**](https://www.bing.com/search?q=alljoyn_aboutdata_setdateofmanufacture)                                                                           | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutdata\_setdefaultlanguage**](https://www.bing.com/search?q=alljoyn_aboutdata_setdefaultlanguage)                                                                               | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutdata\_setdescription**](https://www.bing.com/search?q=alljoyn_aboutdata_setdescription)                                                                                       | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutdata\_setdeviceid**](https://www.bing.com/search?q=alljoyn_aboutdata_setdeviceid)                                                                                             | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutdata\_setdevicename**](https://www.bing.com/search?q=alljoyn_aboutdata_setdevicename)                                                                                         | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutdata\_setfield**](https://www.bing.com/search?q=alljoyn_aboutdata_setfield)                                                                                                   | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutdata\_sethardwareversion**](https://www.bing.com/search?q=alljoyn_aboutdata_sethardwareversion)                                                                               | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutdata\_setmanufacturer**](https://www.bing.com/search?q=alljoyn_aboutdata_setmanufacturer)                                                                                     | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutdata\_setmodelnumber**](https://www.bing.com/search?q=alljoyn_aboutdata_setmodelnumber)                                                                                       | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutdata\_setsoftwareversion**](https://www.bing.com/search?q=alljoyn_aboutdata_setsoftwareversion)                                                                               | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutdata\_setsupportedlanguage**](https://www.bing.com/search?q=alljoyn_aboutdata_setsupportedlanguage)                                                                           | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutdata\_setsupporturl**](https://www.bing.com/search?q=alljoyn_aboutdata_setsupporturl)                                                                                         | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutdatalistener\_create**](https://www.bing.com/search?q=alljoyn_aboutdatalistener_create)                                                                                       | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutdatalistener\_destroy**](https://www.bing.com/search?q=alljoyn_aboutdatalistener_destroy)                                                                                     | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_abouticon\_clear**](https://www.bing.com/search?q=alljoyn_abouticon_clear)                                                                                                         | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_abouticon\_create**](https://www.bing.com/search?q=alljoyn_abouticon_create)                                                                                                       | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_abouticon\_destroy**](https://www.bing.com/search?q=alljoyn_abouticon_destroy)                                                                                                     | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_abouticon\_setcontent**](https://www.bing.com/search?q=alljoyn_abouticon_setcontent)                                                                                               | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_abouticon\_setcontent\_frommsgarg**](https://www.bing.com/search?q=alljoyn_abouticon_setcontent_frommsgarg)                                                                        | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_abouticon\_seturl**](https://www.bing.com/search?q=alljoyn_abouticon_seturl)                                                                                                       | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_abouticonobj\_create**](https://www.bing.com/search?q=alljoyn_abouticonobj_create)                                                                                                 | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_abouticonobj\_destroy**](https://www.bing.com/search?q=alljoyn_abouticonobj_destroy)                                                                                               | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_abouticonproxy\_create**](https://www.bing.com/search?q=alljoyn_abouticonproxy_create)                                                                                             | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_abouticonproxy\_destroy**](https://www.bing.com/search?q=alljoyn_abouticonproxy_destroy)                                                                                           | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_abouticonproxy\_geticon**](https://www.bing.com/search?q=alljoyn_abouticonproxy_geticon)                                                                                           | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_abouticonproxy\_getversion**](https://www.bing.com/search?q=alljoyn_abouticonproxy_getversion)                                                                                     | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutlistener\_create**](https://www.bing.com/search?q=alljoyn_aboutlistener_create)                                                                                               | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutlistener\_destroy**](https://www.bing.com/search?q=alljoyn_aboutlistener_destroy)                                                                                             | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutobj\_announce**](https://www.bing.com/search?q=alljoyn_aboutobj_announce)                                                                                                     | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutobj\_announce\_using\_datalistener**](https://www.bing.com/search?q=alljoyn_aboutobj_announce_using_datalistener)                                                             | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutobj\_create**](https://www.bing.com/search?q=alljoyn_aboutobj_create)                                                                                                         | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutobj\_destroy**](https://www.bing.com/search?q=alljoyn_aboutobj_destroy)                                                                                                       | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutobj\_unannounce**](https://www.bing.com/search?q=alljoyn_aboutobj_unannounce)                                                                                                 | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutobjectdescription\_clear**](https://www.bing.com/search?q=alljoyn_aboutobjectdescription_clear)                                                                               | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutobjectdescription\_create**](https://www.bing.com/search?q=alljoyn_aboutobjectdescription_create)                                                                             | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutobjectdescription\_create\_full**](https://www.bing.com/search?q=alljoyn_aboutobjectdescription_create_full)                                                                  | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutobjectdescription\_createfrommsgarg**](https://www.bing.com/search?q=alljoyn_aboutobjectdescription_createfrommsgarg)                                                         | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutobjectdescription\_destroy**](https://www.bing.com/search?q=alljoyn_aboutobjectdescription_destroy)                                                                           | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutobjectdescription\_getinterfacepaths**](https://www.bing.com/search?q=alljoyn_aboutobjectdescription_getinterfacepaths)                                                       | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutobjectdescription\_getinterfaces**](https://www.bing.com/search?q=alljoyn_aboutobjectdescription_getinterfaces)                                                               | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutobjectdescription\_getmsgarg**](https://www.bing.com/search?q=alljoyn_aboutobjectdescription_getmsgarg)                                                                       | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutobjectdescription\_getpaths**](https://www.bing.com/search?q=alljoyn_aboutobjectdescription_getpaths)                                                                         | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutobjectdescription\_hasinterface**](https://www.bing.com/search?q=alljoyn_aboutobjectdescription_hasinterface)                                                                 | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutobjectdescription\_hasinterfaceatpath**](https://www.bing.com/search?q=alljoyn_aboutobjectdescription_hasinterfaceatpath)                                                     | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutobjectdescription\_haspath**](https://www.bing.com/search?q=alljoyn_aboutobjectdescription_haspath)                                                                           | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutproxy\_create**](https://www.bing.com/search?q=alljoyn_aboutproxy_create)                                                                                                     | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutproxy\_destroy**](https://www.bing.com/search?q=alljoyn_aboutproxy_destroy)                                                                                                   | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutproxy\_getaboutdata**](https://www.bing.com/search?q=alljoyn_aboutproxy_getaboutdata)                                                                                         | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutproxy\_getobjectdescription**](https://www.bing.com/search?q=alljoyn_aboutproxy_getobjectdescription)                                                                         | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_aboutproxy\_getversion**](https://www.bing.com/search?q=alljoyn_aboutproxy_getversion)                                                                                             | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_authlistener\_create**](https://www.bing.com/search?q=alljoyn_authlistener_create)                                                                                                 | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_authlistener\_destroy**](https://www.bing.com/search?q=alljoyn_authlistener_destroy)                                                                                               | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_authlistener\_requestcredentialsresponse**](https://www.bing.com/search?q=alljoyn_authlistener_requestcredentialsresponse)                                                         | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_authlistener\_verifycredentialsresponse**](https://www.bing.com/search?q=alljoyn_authlistener_verifycredentialsresponse)                                                           | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_authlistenerasync\_create**](https://www.bing.com/search?q=alljoyn_authlistenerasync_create)                                                                                       | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_authlistenerasync\_destroy**](https://www.bing.com/search?q=alljoyn_authlistenerasync_destroy)                                                                                     | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_addlogonentry**](https://www.bing.com/search?q=alljoyn_busattachment_addlogonentry)                                                                                 | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_addmatch**](https://www.bing.com/search?q=alljoyn_busattachment_addmatch)                                                                                           | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_advertisename**](https://www.bing.com/search?q=alljoyn_busattachment_advertisename)                                                                                 | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_bindsessionport**](https://www.bing.com/search?q=alljoyn_busattachment_bindsessionport)                                                                             | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_canceladvertisename**](https://www.bing.com/search?q=alljoyn_busattachment_canceladvertisename)                                                                     | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_cancelfindadvertisedname**](https://www.bing.com/search?q=alljoyn_busattachment_cancelfindadvertisedname)                                                           | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_cancelfindadvertisednamebytransport**](https://www.bing.com/search?q=alljoyn_busattachment_cancelfindadvertisednamebytransport)                                     | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_cancelwhoimplements\_interface**](https://www.bing.com/search?q=alljoyn_busattachment_cancelwhoimplements_interface)                                                | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_cancelwhoimplements\_interfaces**](https://www.bing.com/search?q=alljoyn_busattachment_cancelwhoimplements_interfaces)                                              | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_clearkeys**](https://www.bing.com/search?q=alljoyn_busattachment_clearkeys)                                                                                         | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_clearkeystore**](https://www.bing.com/search?q=alljoyn_busattachment_clearkeystore)                                                                                 | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_connect**](https://www.bing.com/search?q=alljoyn_busattachment_connect)                                                                                             | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_create**](https://www.bing.com/search?q=alljoyn_busattachment_create)                                                                                               | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_create\_concurrency**](https://www.bing.com/search?q=alljoyn_busattachment_create_concurrency)                                                                      | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_createinterface**](https://www.bing.com/search?q=alljoyn_busattachment_createinterface)                                                                             | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_createinterface\_secure**](https://www.bing.com/search?q=alljoyn_busattachment_createinterface_secure)                                                              | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_createinterfacesfromxml**](https://www.bing.com/search?q=alljoyn_busattachment_createinterfacesfromxml)                                                             | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_deleteinterface**](https://www.bing.com/search?q=alljoyn_busattachment_deleteinterface)                                                                             | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_destroy**](https://www.bing.com/search?q=alljoyn_busattachment_destroy)                                                                                             | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_disconnect**](https://www.bing.com/search?q=alljoyn_busattachment_disconnect)                                                                                       | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_enableconcurrentcallbacks**](https://www.bing.com/search?q=alljoyn_busattachment_enableconcurrentcallbacks)                                                         | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_enablepeersecurity**](https://www.bing.com/search?q=alljoyn_busattachment_enablepeersecurity)                                                                       | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_findadvertisedname**](https://www.bing.com/search?q=alljoyn_busattachment_findadvertisedname)                                                                       | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_findadvertisednamebytransport**](https://www.bing.com/search?q=alljoyn_busattachment_findadvertisednamebytransport)                                                 | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_getalljoyndebugobj**](https://www.bing.com/search?q=alljoyn_busattachment_getalljoyndebugobj)                                                                       | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_getalljoynproxyobj**](https://www.bing.com/search?q=alljoyn_busattachment_getalljoynproxyobj)                                                                       | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_getconcurrency**](https://www.bing.com/search?q=alljoyn_busattachment_getconcurrency)                                                                               | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_getconnectspec**](https://www.bing.com/search?q=alljoyn_busattachment_getconnectspec)                                                                               | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_getdbusproxyobj**](https://www.bing.com/search?q=alljoyn_busattachment_getdbusproxyobj)                                                                             | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_getglobalguidstring**](https://www.bing.com/search?q=alljoyn_busattachment_getglobalguidstring)                                                                     | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_getinterface**](https://www.bing.com/search?q=alljoyn_busattachment_getinterface)                                                                                   | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_getinterfaces**](https://www.bing.com/search?q=alljoyn_busattachment_getinterfaces)                                                                                 | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_getkeyexpiration**](https://www.bing.com/search?q=alljoyn_busattachment_getkeyexpiration)                                                                           | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_getpeerguid**](https://www.bing.com/search?q=alljoyn_busattachment_getpeerguid)                                                                                     | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_gettimestamp**](https://www.bing.com/search?q=alljoyn_busattachment_gettimestamp)                                                                                   | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_getuniquename**](https://www.bing.com/search?q=alljoyn_busattachment_getuniquename)                                                                                 | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_isconnected**](https://www.bing.com/search?q=alljoyn_busattachment_isconnected)                                                                                     | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_ispeersecurityenabled**](https://www.bing.com/search?q=alljoyn_busattachment_ispeersecurityenabled)                                                                 | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_isstarted**](https://www.bing.com/search?q=alljoyn_busattachment_isstarted)                                                                                         | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_isstopping**](https://www.bing.com/search?q=alljoyn_busattachment_isstopping)                                                                                       | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_join**](https://www.bing.com/search?q=alljoyn_busattachment_join)                                                                                                   | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_joinsession**](https://www.bing.com/search?q=alljoyn_busattachment_joinsession)                                                                                     | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_joinsessionasync**](https://www.bing.com/search?q=alljoyn_busattachment_joinsessionasync)                                                                           | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_leavesession**](https://www.bing.com/search?q=alljoyn_busattachment_leavesession)                                                                                   | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_namehasowner**](https://www.bing.com/search?q=alljoyn_busattachment_namehasowner)                                                                                   | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_ping**](https://www.bing.com/search?q=alljoyn_busattachment_ping)                                                                                                   | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_registeraboutlistener**](https://www.bing.com/search?q=alljoyn_busattachment_registeraboutlistener)                                                                 | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_registerbuslistener**](https://www.bing.com/search?q=alljoyn_busattachment_registerbuslistener)                                                                     | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_registerbusobject**](https://www.bing.com/search?q=alljoyn_busattachment_registerbusobject)                                                                         | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_registerbusobject\_secure**](https://www.bing.com/search?q=alljoyn_busattachment_registerbusobject_secure)                                                          | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_registerkeystorelistener**](https://www.bing.com/search?q=alljoyn_busattachment_registerkeystorelistener)                                                           | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_registersignalhandler**](https://www.bing.com/search?q=alljoyn_busattachment_registersignalhandler)                                                                 | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_registersignalhandlerwithrule**](https://www.bing.com/search?q=alljoyn_busattachment_registersignalhandlerwithrule)                                                 | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_releasename**](https://www.bing.com/search?q=alljoyn_busattachment_releasename)                                                                                     | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_reloadkeystore**](https://www.bing.com/search?q=alljoyn_busattachment_reloadkeystore)                                                                               | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_removematch**](https://www.bing.com/search?q=alljoyn_busattachment_removematch)                                                                                     | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_removesessionmember**](https://www.bing.com/search?q=alljoyn_busattachment_removesessionmember)                                                                     | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_requestname**](https://www.bing.com/search?q=alljoyn_busattachment_requestname)                                                                                     | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_setdaemondebug**](https://www.bing.com/search?q=alljoyn_busattachment_setdaemondebug)                                                                               | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_setkeyexpiration**](https://www.bing.com/search?q=alljoyn_busattachment_setkeyexpiration)                                                                           | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_setlinktimeout**](https://www.bing.com/search?q=alljoyn_busattachment_setlinktimeout)                                                                               | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_setlinktimeoutasync**](https://www.bing.com/search?q=alljoyn_busattachment_setlinktimeoutasync)                                                                     | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_setsessionlistener**](https://www.bing.com/search?q=alljoyn_busattachment_setsessionlistener)                                                                       | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_start**](https://www.bing.com/search?q=alljoyn_busattachment_start)                                                                                                 | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_stop**](https://www.bing.com/search?q=alljoyn_busattachment_stop)                                                                                                   | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_unbindsessionport**](https://www.bing.com/search?q=alljoyn_busattachment_unbindsessionport)                                                                         | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_unregisteraboutlistener**](https://www.bing.com/search?q=alljoyn_busattachment_unregisteraboutlistener)                                                             | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_unregisterallaboutlisteners**](https://www.bing.com/search?q=alljoyn_busattachment_unregisterallaboutlisteners)                                                     | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_unregisterallhandlers**](https://www.bing.com/search?q=alljoyn_busattachment_unregisterallhandlers)                                                                 | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_unregisterbuslistener**](https://www.bing.com/search?q=alljoyn_busattachment_unregisterbuslistener)                                                                 | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_unregisterbusobject**](https://www.bing.com/search?q=alljoyn_busattachment_unregisterbusobject)                                                                     | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_unregistersignalhandler**](https://www.bing.com/search?q=alljoyn_busattachment_unregistersignalhandler)                                                             | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_unregistersignalhandlerwithrule**](https://www.bing.com/search?q=alljoyn_busattachment_unregistersignalhandlerwithrule)                                             | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_whoimplements\_interface**](https://www.bing.com/search?q=alljoyn_busattachment_whoimplements_interface)                                                            | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busattachment\_whoimplements\_interfaces**](https://www.bing.com/search?q=alljoyn_busattachment_whoimplements_interfaces)                                                          | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_buslistener\_create**](https://www.bing.com/search?q=alljoyn_buslistener_create)                                                                                                   | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_buslistener\_destroy**](https://www.bing.com/search?q=alljoyn_buslistener_destroy)                                                                                                 | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busobject\_addinterface**](https://www.bing.com/search?q=alljoyn_busobject_addinterface)                                                                                           | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busobject\_addinterface\_announced**](https://www.bing.com/search?q=alljoyn_busobject_addinterface_announced)                                                                      | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busobject\_addmethodhandler**](https://www.bing.com/search?q=alljoyn_busobject_addmethodhandler)                                                                                   | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busobject\_addmethodhandlers**](https://www.bing.com/search?q=alljoyn_busobject_addmethodhandlers)                                                                                 | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busobject\_cancelsessionlessmessage**](https://www.bing.com/search?q=alljoyn_busobject_cancelsessionlessmessage)                                                                   | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busobject\_cancelsessionlessmessage\_serial**](https://www.bing.com/search?q=alljoyn_busobject_cancelsessionlessmessage_serial)                                                    | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busobject\_create**](https://www.bing.com/search?q=alljoyn_busobject_create)                                                                                                       | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busobject\_destroy**](https://www.bing.com/search?q=alljoyn_busobject_destroy)                                                                                                     | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busobject\_emitpropertieschanged**](https://www.bing.com/search?q=alljoyn_busobject_emitpropertieschanged)                                                                         | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busobject\_emitpropertychanged**](https://www.bing.com/search?q=alljoyn_busobject_emitpropertychanged)                                                                             | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busobject\_getannouncedinterfacenames**](https://www.bing.com/search?q=alljoyn_busobject_getannouncedinterfacenames)                                                               | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busobject\_getbusattachment**](https://www.bing.com/search?q=alljoyn_busobject_getbusattachment)                                                                                   | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busobject\_getname**](https://www.bing.com/search?q=alljoyn_busobject_getname)                                                                                                     | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busobject\_getpath**](https://www.bing.com/search?q=alljoyn_busobject_getpath)                                                                                                     | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busobject\_issecure**](https://www.bing.com/search?q=alljoyn_busobject_issecure)                                                                                                   | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busobject\_methodreply\_args**](https://www.bing.com/search?q=alljoyn_busobject_methodreply_args)                                                                                  | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busobject\_methodreply\_err**](https://www.bing.com/search?q=alljoyn_busobject_methodreply_err)                                                                                    | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busobject\_methodreply\_status**](https://www.bing.com/search?q=alljoyn_busobject_methodreply_status)                                                                              | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busobject\_setannounceflag**](https://www.bing.com/search?q=alljoyn_busobject_setannounceflag)                                                                                     | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_busobject\_signal**](https://www.bing.com/search?q=alljoyn_busobject_signal)                                                                                                       | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_credentials\_clear**](https://www.bing.com/search?q=alljoyn_credentials_clear)                                                                                                     | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_credentials\_create**](https://www.bing.com/search?q=alljoyn_credentials_create)                                                                                                   | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_credentials\_destroy**](https://www.bing.com/search?q=alljoyn_credentials_destroy)                                                                                                 | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_credentials\_getcertchain**](https://www.bing.com/search?q=alljoyn_credentials_getcertchain)                                                                                       | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_credentials\_getexpiration**](https://www.bing.com/search?q=alljoyn_credentials_getexpiration)                                                                                     | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_credentials\_getlogonentry**](https://www.bing.com/search?q=alljoyn_credentials_getlogonentry)                                                                                     | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_credentials\_getpassword**](https://www.bing.com/search?q=alljoyn_credentials_getpassword)                                                                                         | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_credentials\_getprivateKey**](https://www.bing.com/search?q=alljoyn_credentials_getprivateKey)                                                                                     | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_credentials\_getusername**](https://www.bing.com/search?q=alljoyn_credentials_getusername)                                                                                         | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_credentials\_isset**](https://www.bing.com/search?q=alljoyn_credentials_isset)                                                                                                     | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_credentials\_setcertchain**](https://www.bing.com/search?q=alljoyn_credentials_setcertchain)                                                                                       | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_credentials\_setexpiration**](https://www.bing.com/search?q=alljoyn_credentials_setexpiration)                                                                                     | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_credentials\_setlogonentry**](https://www.bing.com/search?q=alljoyn_credentials_setlogonentry)                                                                                     | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_credentials\_setpassword**](https://www.bing.com/search?q=alljoyn_credentials_setpassword)                                                                                         | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_credentials\_setprivatekey**](https://www.bing.com/search?q=alljoyn_credentials_setprivatekey)                                                                                     | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_credentials\_setusername**](https://www.bing.com/search?q=alljoyn_credentials_setusername)                                                                                         | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_getbuildinfo**](https://www.bing.com/search?q=alljoyn_getbuildinfo)                                                                                                                | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_getnumericversion**](https://www.bing.com/search?q=alljoyn_getnumericversion)                                                                                                      | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_getversion**](https://www.bing.com/search?q=alljoyn_getversion)                                                                                                                    | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_init**](https://www.bing.com/search?q=alljoyn_init)                                                                                                                                | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_interfacedescription\_activate**](https://www.bing.com/search?q=alljoyn_interfacedescription_activate)                                                                             | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_interfacedescription\_addannotation**](https://www.bing.com/search?q=alljoyn_interfacedescription_addannotation)                                                                   | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_interfacedescription\_addmember**](https://www.bing.com/search?q=alljoyn_interfacedescription_addmember)                                                                           | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_interfacedescription\_addmemberannotation**](https://www.bing.com/search?q=alljoyn_interfacedescription_addmemberannotation)                                                       | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_interfacedescription\_addmethod**](https://www.bing.com/search?q=alljoyn_interfacedescription_addmethod)                                                                           | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_interfacedescription\_addproperty**](https://www.bing.com/search?q=alljoyn_interfacedescription_addproperty)                                                                       | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_interfacedescription\_addpropertyannotation**](https://www.bing.com/search?q=alljoyn_interfacedescription_addpropertyannotation)                                                   | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_interfacedescription\_addsignal**](https://www.bing.com/search?q=alljoyn_interfacedescription_addsignal)                                                                           | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_interfacedescription\_eql**](https://www.bing.com/search?q=alljoyn_interfacedescription_eql)                                                                                       | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_interfacedescription\_getannotation**](https://www.bing.com/search?q=alljoyn_interfacedescription_getannotation)                                                                   | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_interfacedescription\_getannotationatindex**](https://www.bing.com/search?q=alljoyn_interfacedescription_getannotationatindex)                                                     | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_interfacedescription\_getannotationscount**](https://www.bing.com/search?q=alljoyn_interfacedescription_getannotationscount)                                                       | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_interfacedescription\_getmember**](https://www.bing.com/search?q=alljoyn_interfacedescription_getmember)                                                                           | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_interfacedescription\_getmemberannotation**](https://www.bing.com/search?q=alljoyn_interfacedescription_getmemberannotation)                                                       | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_interfacedescription\_getmembers**](https://www.bing.com/search?q=alljoyn_interfacedescription_getmembers)                                                                         | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_interfacedescription\_getmethod**](https://www.bing.com/search?q=alljoyn_interfacedescription_getmethod)                                                                           | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_interfacedescription\_getname**](https://www.bing.com/search?q=alljoyn_interfacedescription_getname)                                                                               | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_interfacedescription\_getproperties**](https://www.bing.com/search?q=alljoyn_interfacedescription_getproperties)                                                                   | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_interfacedescription\_getproperty**](https://www.bing.com/search?q=alljoyn_interfacedescription_getproperty)                                                                       | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_interfacedescription\_getpropertyannotation**](https://www.bing.com/search?q=alljoyn_interfacedescription_getpropertyannotation)                                                   | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_interfacedescription\_getsecuritypolicy**](https://www.bing.com/search?q=alljoyn_interfacedescription_getsecuritypolicy)                                                           | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_interfacedescription\_getsignal**](https://www.bing.com/search?q=alljoyn_interfacedescription_getsignal)                                                                           | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_interfacedescription\_hasmember**](https://www.bing.com/search?q=alljoyn_interfacedescription_hasmember)                                                                           | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_interfacedescription\_hasproperties**](https://www.bing.com/search?q=alljoyn_interfacedescription_hasproperties)                                                                   | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_interfacedescription\_hasproperty**](https://www.bing.com/search?q=alljoyn_interfacedescription_hasproperty)                                                                       | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_interfacedescription\_introspect**](https://www.bing.com/search?q=alljoyn_interfacedescription_introspect)                                                                         | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_interfacedescription\_issecure**](https://www.bing.com/search?q=alljoyn_interfacedescription_issecure)                                                                             | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_interfacedescription\_member\_eql**](https://www.bing.com/search?q=alljoyn_interfacedescription_member_eql)                                                                        | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_interfacedescription\_member\_getannotation**](https://www.bing.com/search?q=alljoyn_interfacedescription_member_getannotation)                                                    | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_interfacedescription\_member\_getannotationatindex**](https://www.bing.com/search?q=alljoyn_interfacedescription_member_getannotationatindex)                                      | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_interfacedescription\_member\_getannotationscount**](https://www.bing.com/search?q=alljoyn_interfacedescription_member_getannotationscount)                                        | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_interfacedescription\_property\_eql**](https://www.bing.com/search?q=alljoyn_interfacedescription_property_eql)                                                                    | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_interfacedescription\_property\_getannotation**](https://www.bing.com/search?q=alljoyn_interfacedescription_property_getannotation)                                                | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_interfacedescription\_property\_getannotationatindex**](https://www.bing.com/search?q=alljoyn_interfacedescription_property_getannotationatindex)                                  | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_interfacedescription\_property\_getannotationscount**](https://www.bing.com/search?q=alljoyn_interfacedescription_property_getannotationscount)                                    | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_keystorelistener\_create**](https://www.bing.com/search?q=alljoyn_keystorelistener_create)                                                                                         | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_keystorelistener\_destroy**](https://www.bing.com/search?q=alljoyn_keystorelistener_destroy)                                                                                       | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_keystorelistener\_getkeys**](https://www.bing.com/search?q=alljoyn_keystorelistener_getkeys)                                                                                       | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_keystorelistener\_putkeys**](https://www.bing.com/search?q=alljoyn_keystorelistener_putkeys)                                                                                       | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_message\_create**](https://www.bing.com/search?q=alljoyn_message_create)                                                                                                           | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_message\_description**](https://www.bing.com/search?q=alljoyn_message_description)                                                                                                 | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_message\_destroy**](https://www.bing.com/search?q=alljoyn_message_destroy)                                                                                                         | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_message\_eql**](https://www.bing.com/search?q=alljoyn_message_eql)                                                                                                                 | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_message\_getarg**](https://www.bing.com/search?q=alljoyn_message_getarg)                                                                                                           | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_message\_getargs**](https://www.bing.com/search?q=alljoyn_message_getargs)                                                                                                         | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_message\_getauthmechanism**](https://www.bing.com/search?q=alljoyn_message_getauthmechanism)                                                                                       | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_message\_getcallserial**](https://www.bing.com/search?q=alljoyn_message_getcallserial)                                                                                             | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_message\_getcompressiontoken**](https://www.bing.com/search?q=alljoyn_message_getcompressiontoken)                                                                                 | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_message\_getdestination**](https://www.bing.com/search?q=alljoyn_message_getdestination)                                                                                           | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_message\_geterrorname**](https://www.bing.com/search?q=alljoyn_message_geterrorname)                                                                                               | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_message\_getflags**](https://www.bing.com/search?q=alljoyn_message_getflags)                                                                                                       | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_message\_getinterface**](https://www.bing.com/search?q=alljoyn_message_getinterface)                                                                                               | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_message\_getmembername**](https://www.bing.com/search?q=alljoyn_message_getmembername)                                                                                             | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_message\_getobjectpath**](https://www.bing.com/search?q=alljoyn_message_getobjectpath)                                                                                             | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_message\_getreceiveendpointname**](https://www.bing.com/search?q=alljoyn_message_getreceiveendpointname)                                                                           | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_message\_getreplyserial**](https://www.bing.com/search?q=alljoyn_message_getreplyserial)                                                                                           | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_message\_getsender**](https://www.bing.com/search?q=alljoyn_message_getsender)                                                                                                     | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_message\_getsessionid**](https://www.bing.com/search?q=alljoyn_message_getsessionid)                                                                                               | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_message\_getsignature**](https://www.bing.com/search?q=alljoyn_message_getsignature)                                                                                               | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_message\_gettimestamp**](https://www.bing.com/search?q=alljoyn_message_gettimestamp)                                                                                               | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_message\_gettype**](https://www.bing.com/search?q=alljoyn_message_gettype)                                                                                                         | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_message\_isbroadcastsignal**](https://www.bing.com/search?q=alljoyn_message_isbroadcastsignal)                                                                                     | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_message\_isencrypted**](https://www.bing.com/search?q=alljoyn_message_isencrypted)                                                                                                 | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_message\_isexpired**](https://www.bing.com/search?q=alljoyn_message_isexpired)                                                                                                     | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_message\_isglobalbroadcast**](https://www.bing.com/search?q=alljoyn_message_isglobalbroadcast)                                                                                     | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_message\_issessionless**](https://www.bing.com/search?q=alljoyn_message_issessionless)                                                                                             | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_message\_isunreliable**](https://www.bing.com/search?q=alljoyn_message_isunreliable)                                                                                               | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_message\_parseargs**](https://www.bing.com/search?q=alljoyn_message_parseargs)                                                                                                     | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_message\_setendianess**](https://www.bing.com/search?q=alljoyn_message_setendianess)                                                                                               | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_message\_tostring**](https://www.bing.com/search?q=alljoyn_message_tostring)                                                                                                       | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_array\_create**](https://www.bing.com/search?q=alljoyn_msgarg_array_create)                                                                                                | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_array\_element**](https://www.bing.com/search?q=alljoyn_msgarg_array_element)                                                                                              | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_array\_get**](https://www.bing.com/search?q=alljoyn_msgarg_array_get)                                                                                                      | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_array\_set**](https://www.bing.com/search?q=alljoyn_msgarg_array_set)                                                                                                      | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_array\_set\_offset**](https://www.bing.com/search?q=alljoyn_msgarg_array_set_offset)                                                                                       | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_array\_signature**](https://www.bing.com/search?q=alljoyn_msgarg_array_signature)                                                                                          | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_array\_tostring**](https://www.bing.com/search?q=alljoyn_msgarg_array_tostring)                                                                                            | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_clear**](https://www.bing.com/search?q=alljoyn_msgarg_clear)                                                                                                               | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_clone**](https://www.bing.com/search?q=alljoyn_msgarg_clone)                                                                                                               | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_copy**](https://www.bing.com/search?q=alljoyn_msgarg_copy)                                                                                                                 | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_create**](https://www.bing.com/search?q=alljoyn_msgarg_create)                                                                                                             | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_create\_and\_set**](https://www.bing.com/search?q=alljoyn_msgarg_create_and_set)                                                                                           | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_destroy**](https://www.bing.com/search?q=alljoyn_msgarg_destroy)                                                                                                           | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_equal**](https://www.bing.com/search?q=alljoyn_msgarg_equal)                                                                                                               | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_get**](https://www.bing.com/search?q=alljoyn_msgarg_get)                                                                                                                   | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_get\_array\_element**](https://www.bing.com/search?q=alljoyn_msgarg_get_array_element)                                                                                     | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_get\_array\_elementsignature**](https://www.bing.com/search?q=alljoyn_msgarg_get_array_elementsignature)                                                                   | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_get\_array\_numberofelements**](https://www.bing.com/search?q=alljoyn_msgarg_get_array_numberofelements)                                                                   | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_get\_bool**](https://www.bing.com/search?q=alljoyn_msgarg_get_bool)                                                                                                        | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_get\_bool\_array**](https://www.bing.com/search?q=alljoyn_msgarg_get_bool_array)                                                                                           | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_get\_double**](https://www.bing.com/search?q=alljoyn_msgarg_get_double)                                                                                                    | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_get\_double\_array**](https://www.bing.com/search?q=alljoyn_msgarg_get_double_array)                                                                                       | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_get\_int16**](https://www.bing.com/search?q=alljoyn_msgarg_get_int16)                                                                                                      | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_get\_int16\_array**](https://www.bing.com/search?q=alljoyn_msgarg_get_int16_array)                                                                                         | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_get\_int32**](https://www.bing.com/search?q=alljoyn_msgarg_get_int32)                                                                                                      | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_get\_int32\_array**](https://www.bing.com/search?q=alljoyn_msgarg_get_int32_array)                                                                                         | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_get\_int64**](https://www.bing.com/search?q=alljoyn_msgarg_get_int64)                                                                                                      | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_get\_int64\_array**](https://www.bing.com/search?q=alljoyn_msgarg_get_int64_array)                                                                                         | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_get\_objectpath**](https://www.bing.com/search?q=alljoyn_msgarg_get_objectpath)                                                                                            | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_get\_signature**](https://www.bing.com/search?q=alljoyn_msgarg_get_signature)                                                                                              | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_get\_string**](https://www.bing.com/search?q=alljoyn_msgarg_get_string)                                                                                                    | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_get\_uint16**](https://www.bing.com/search?q=alljoyn_msgarg_get_uint16)                                                                                                    | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_get\_uint16\_array**](https://www.bing.com/search?q=alljoyn_msgarg_get_uint16_array)                                                                                       | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_get\_uint32**](https://www.bing.com/search?q=alljoyn_msgarg_get_uint32)                                                                                                    | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_get\_uint32\_array**](https://www.bing.com/search?q=alljoyn_msgarg_get_uint32_array)                                                                                       | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_get\_uint64**](https://www.bing.com/search?q=alljoyn_msgarg_get_uint64)                                                                                                    | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_get\_uint64\_array**](https://www.bing.com/search?q=alljoyn_msgarg_get_uint64_array)                                                                                       | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_get\_uint8**](https://www.bing.com/search?q=alljoyn_msgarg_get_uint8)                                                                                                      | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_get\_uint8\_array**](https://www.bing.com/search?q=alljoyn_msgarg_get_uint8_array)                                                                                         | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_get\_variant**](https://www.bing.com/search?q=alljoyn_msgarg_get_variant)                                                                                                  | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_get\_variant\_array**](https://www.bing.com/search?q=alljoyn_msgarg_get_variant_array)                                                                                     | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_getdictelement**](https://www.bing.com/search?q=alljoyn_msgarg_getdictelement)                                                                                             | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_getkey**](https://www.bing.com/search?q=alljoyn_msgarg_getkey)                                                                                                             | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_getmember**](https://www.bing.com/search?q=alljoyn_msgarg_getmember)                                                                                                       | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_getnummembers**](https://www.bing.com/search?q=alljoyn_msgarg_getnummembers)                                                                                               | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_gettype**](https://www.bing.com/search?q=alljoyn_msgarg_gettype)                                                                                                           | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_getvalue**](https://www.bing.com/search?q=alljoyn_msgarg_getvalue)                                                                                                         | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_hassignature**](https://www.bing.com/search?q=alljoyn_msgarg_hassignature)                                                                                                 | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_set**](https://www.bing.com/search?q=alljoyn_msgarg_set)                                                                                                                   | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_set\_and\_stabilize**](https://www.bing.com/search?q=alljoyn_msgarg_set_and_stabilize)                                                                                     | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_set\_bool**](https://www.bing.com/search?q=alljoyn_msgarg_set_bool)                                                                                                        | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_set\_bool\_array**](https://www.bing.com/search?q=alljoyn_msgarg_set_bool_array)                                                                                           | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_set\_double**](https://www.bing.com/search?q=alljoyn_msgarg_set_double)                                                                                                    | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_set\_double\_array**](https://www.bing.com/search?q=alljoyn_msgarg_set_double_array)                                                                                       | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_set\_int16**](https://www.bing.com/search?q=alljoyn_msgarg_set_int16)                                                                                                      | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_set\_int16\_array**](https://www.bing.com/search?q=alljoyn_msgarg_set_int16_array)                                                                                         | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_set\_int32**](https://www.bing.com/search?q=alljoyn_msgarg_set_int32)                                                                                                      | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_set\_int32\_array**](https://www.bing.com/search?q=alljoyn_msgarg_set_int32_array)                                                                                         | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_set\_int64**](https://www.bing.com/search?q=alljoyn_msgarg_set_int64)                                                                                                      | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_set\_int64\_array**](https://www.bing.com/search?q=alljoyn_msgarg_set_int64_array)                                                                                         | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_set\_objectpath**](https://www.bing.com/search?q=alljoyn_msgarg_set_objectpath)                                                                                            | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_set\_objectpath\_array**](https://www.bing.com/search?q=alljoyn_msgarg_set_objectpath_array)                                                                               | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_set\_signature**](https://www.bing.com/search?q=alljoyn_msgarg_set_signature)                                                                                              | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_set\_signature\_array**](https://www.bing.com/search?q=alljoyn_msgarg_set_signature_array)                                                                                 | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_set\_string**](https://www.bing.com/search?q=alljoyn_msgarg_set_string)                                                                                                    | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_set\_string\_array**](https://www.bing.com/search?q=alljoyn_msgarg_set_string_array)                                                                                       | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_set\_uint16**](https://www.bing.com/search?q=alljoyn_msgarg_set_uint16)                                                                                                    | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_set\_uint16\_array**](https://www.bing.com/search?q=alljoyn_msgarg_set_uint16_array)                                                                                       | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_set\_uint32**](https://www.bing.com/search?q=alljoyn_msgarg_set_uint32)                                                                                                    | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_set\_uint32\_array**](https://www.bing.com/search?q=alljoyn_msgarg_set_uint32_array)                                                                                       | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_set\_uint64**](https://www.bing.com/search?q=alljoyn_msgarg_set_uint64)                                                                                                    | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_set\_uint64\_array**](https://www.bing.com/search?q=alljoyn_msgarg_set_uint64_array)                                                                                       | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_set\_uint8**](https://www.bing.com/search?q=alljoyn_msgarg_set_uint8)                                                                                                      | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_set\_uint8\_array**](https://www.bing.com/search?q=alljoyn_msgarg_set_uint8_array)                                                                                         | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_setdictentry**](https://www.bing.com/search?q=alljoyn_msgarg_setdictentry)                                                                                                 | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_setstruct**](https://www.bing.com/search?q=alljoyn_msgarg_setstruct)                                                                                                       | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_signature**](https://www.bing.com/search?q=alljoyn_msgarg_signature)                                                                                                       | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_stabilize**](https://www.bing.com/search?q=alljoyn_msgarg_stabilize)                                                                                                       | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_msgarg\_tostring**](https://www.bing.com/search?q=alljoyn_msgarg_tostring)                                                                                                         | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_observer\_create**](https://www.bing.com/search?q=alljoyn_observer_create)                                                                                                         | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_observer\_destroy**](https://www.bing.com/search?q=alljoyn_observer_destroy)                                                                                                       | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_observer\_get**](https://www.bing.com/search?q=alljoyn_observer_get)                                                                                                               | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_observer\_getfirst**](https://www.bing.com/search?q=alljoyn_observer_getfirst)                                                                                                     | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_observer\_getnext**](https://www.bing.com/search?q=alljoyn_observer_getnext)                                                                                                       | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_observer\_registerlistener**](https://www.bing.com/search?q=alljoyn_observer_registerlistener)                                                                                     | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_observer\_unregisteralllisteners**](https://www.bing.com/search?q=alljoyn_observer_unregisteralllisteners)                                                                         | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_observer\_unregisterlistener**](https://www.bing.com/search?q=alljoyn_observer_unregisterlistener)                                                                                 | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_observerlistener\_create**](https://www.bing.com/search?q=alljoyn_observerlistener_create)                                                                                         | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_observerlistener\_destroy**](https://www.bing.com/search?q=alljoyn_observerlistener_destroy)                                                                                       | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_passwordmanager\_setcredentials**](https://www.bing.com/search?q=alljoyn_passwordmanager_setcredentials)                                                                           | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_proxybusobject\_addchild**](https://www.bing.com/search?q=alljoyn_proxybusobject_addchild)                                                                                         | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_proxybusobject\_addinterface**](https://www.bing.com/search?q=alljoyn_proxybusobject_addinterface)                                                                                 | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_proxybusobject\_addinterface\_by\_name**](https://www.bing.com/search?q=alljoyn_proxybusobject_addinterface_by_name)                                                               | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_proxybusobject\_copy**](https://www.bing.com/search?q=alljoyn_proxybusobject_copy)                                                                                                 | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_proxybusobject\_create**](https://www.bing.com/search?q=alljoyn_proxybusobject_create)                                                                                             | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_proxybusobject\_create\_secure**](https://www.bing.com/search?q=alljoyn_proxybusobject_create_secure)                                                                              | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_proxybusobject\_destroy**](https://www.bing.com/search?q=alljoyn_proxybusobject_destroy)                                                                                           | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_proxybusobject\_enablepropertycaching**](https://www.bing.com/search?q=alljoyn_proxybusobject_enablepropertycaching)                                                               | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_proxybusobject\_getallproperties**](https://www.bing.com/search?q=alljoyn_proxybusobject_getallproperties)                                                                         | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_proxybusobject\_getallpropertiesasync**](https://www.bing.com/search?q=alljoyn_proxybusobject_getallpropertiesasync)                                                               | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_proxybusobject\_getchild**](https://www.bing.com/search?q=alljoyn_proxybusobject_getchild)                                                                                         | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_proxybusobject\_getchildren**](https://www.bing.com/search?q=alljoyn_proxybusobject_getchildren)                                                                                   | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_proxybusobject\_getinterface**](https://www.bing.com/search?q=alljoyn_proxybusobject_getinterface)                                                                                 | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_proxybusobject\_getinterfaces**](https://www.bing.com/search?q=alljoyn_proxybusobject_getinterfaces)                                                                               | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_proxybusobject\_getpath**](https://www.bing.com/search?q=alljoyn_proxybusobject_getpath)                                                                                           | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_proxybusobject\_getproperty**](https://www.bing.com/search?q=alljoyn_proxybusobject_getproperty)                                                                                   | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_proxybusobject\_getpropertyasync**](https://www.bing.com/search?q=alljoyn_proxybusobject_getpropertyasync)                                                                         | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_proxybusobject\_getservicename**](https://www.bing.com/search?q=alljoyn_proxybusobject_getservicename)                                                                             | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_proxybusobject\_getsessionid**](https://www.bing.com/search?q=alljoyn_proxybusobject_getsessionid)                                                                                 | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_proxybusobject\_getuniquename**](https://www.bing.com/search?q=alljoyn_proxybusobject_getuniquename)                                                                               | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_proxybusobject\_implementsinterface**](https://www.bing.com/search?q=alljoyn_proxybusobject_implementsinterface)                                                                   | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_proxybusobject\_introspectremoteobject**](https://www.bing.com/search?q=alljoyn_proxybusobject_introspectremoteobject)                                                             | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_proxybusobject\_introspectremoteobjectasync**](https://www.bing.com/search?q=alljoyn_proxybusobject_introspectremoteobjectasync)                                                   | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_proxybusobject\_issecure**](https://www.bing.com/search?q=alljoyn_proxybusobject_issecure)                                                                                         | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_proxybusobject\_isvalid**](https://www.bing.com/search?q=alljoyn_proxybusobject_isvalid)                                                                                           | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_proxybusobject\_methodcall**](https://www.bing.com/search?q=alljoyn_proxybusobject_methodcall)                                                                                     | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_proxybusobject\_methodcall\_member**](https://www.bing.com/search?q=alljoyn_proxybusobject_methodcall_member)                                                                      | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_proxybusobject\_methodcall\_member\_noreply**](https://www.bing.com/search?q=alljoyn_proxybusobject_methodcall_member_noreply)                                                     | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_proxybusobject\_methodcall\_noreply**](https://www.bing.com/search?q=alljoyn_proxybusobject_methodcall_noreply)                                                                    | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_proxybusobject\_methodcallasync**](https://www.bing.com/search?q=alljoyn_proxybusobject_methodcallasync)                                                                           | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_proxybusobject\_methodcallasync\_member**](https://www.bing.com/search?q=alljoyn_proxybusobject_methodcallasync_member)                                                            | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_proxybusobject\_parsexml**](https://www.bing.com/search?q=alljoyn_proxybusobject_parsexml)                                                                                         | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_proxybusobject\_ref\_create**](https://www.bing.com/search?q=alljoyn_proxybusobject_ref_create)                                                                                    | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_proxybusobject\_ref\_decref**](https://www.bing.com/search?q=alljoyn_proxybusobject_ref_decref)                                                                                    | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_proxybusobject\_ref\_get**](https://www.bing.com/search?q=alljoyn_proxybusobject_ref_get)                                                                                          | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_proxybusobject\_ref\_incref**](https://www.bing.com/search?q=alljoyn_proxybusobject_ref_incref)                                                                                    | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_proxybusobject\_registerpropertieschangedlistener**](https://www.bing.com/search?q=alljoyn_proxybusobject_registerpropertieschangedlistener)                                       | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_proxybusobject\_removechild**](https://www.bing.com/search?q=alljoyn_proxybusobject_removechild)                                                                                   | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_proxybusobject\_secureconnection**](https://www.bing.com/search?q=alljoyn_proxybusobject_secureconnection)                                                                         | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_proxybusobject\_secureconnectionasync**](https://www.bing.com/search?q=alljoyn_proxybusobject_secureconnectionasync)                                                               | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_proxybusobject\_setproperty**](https://www.bing.com/search?q=alljoyn_proxybusobject_setproperty)                                                                                   | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_proxybusobject\_setpropertyasync**](https://www.bing.com/search?q=alljoyn_proxybusobject_setpropertyasync)                                                                         | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_proxybusobject\_unregisterpropertieschangedlistener**](https://www.bing.com/search?q=alljoyn_proxybusobject_unregisterpropertieschangedlistener)                                   | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_sessionlistener\_create**](https://www.bing.com/search?q=alljoyn_sessionlistener_create)                                                                                           | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_sessionlistener\_destroy**](https://www.bing.com/search?q=alljoyn_sessionlistener_destroy)                                                                                         | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_sessionopts\_cmp**](https://www.bing.com/search?q=alljoyn_sessionopts_cmp)                                                                                                         | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_sessionopts\_create**](https://www.bing.com/search?q=alljoyn_sessionopts_create)                                                                                                   | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_sessionopts\_destroy**](https://www.bing.com/search?q=alljoyn_sessionopts_destroy)                                                                                                 | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_sessionopts\_get\_multipoint**](https://www.bing.com/search?q=alljoyn_sessionopts_get_multipoint)                                                                                  | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_sessionopts\_get\_proximity**](https://www.bing.com/search?q=alljoyn_sessionopts_get_proximity)                                                                                    | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_sessionopts\_get\_traffic**](https://www.bing.com/search?q=alljoyn_sessionopts_get_traffic)                                                                                        | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_sessionopts\_get\_transports**](https://www.bing.com/search?q=alljoyn_sessionopts_get_transports)                                                                                  | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_sessionopts\_iscompatible**](https://www.bing.com/search?q=alljoyn_sessionopts_iscompatible)                                                                                       | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_sessionopts\_set\_multipoint**](https://www.bing.com/search?q=alljoyn_sessionopts_set_multipoint)                                                                                  | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_sessionopts\_set\_proximity**](https://www.bing.com/search?q=alljoyn_sessionopts_set_proximity)                                                                                    | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_sessionopts\_set\_traffic**](https://www.bing.com/search?q=alljoyn_sessionopts_set_traffic)                                                                                        | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_sessionopts\_set\_transports**](https://www.bing.com/search?q=alljoyn_sessionopts_set_transports)                                                                                  | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_sessionportlistener\_create**](https://www.bing.com/search?q=alljoyn_sessionportlistener_create)                                                                                   | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_sessionportlistener\_destroy**](https://www.bing.com/search?q=alljoyn_sessionportlistener_destroy)                                                                                 | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_shutdown**](https://www.bing.com/search?q=alljoyn_shutdown)                                                                                                                        | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_unity\_deferred\_callbacks\_process**](https://www.bing.com/search?q=alljoyn_unity_deferred_callbacks_process)                                                                     | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_unity\_set\_deferred\_callback\_mainthread\_only**](https://www.bing.com/search?q=alljoyn_unity_set_deferred_callback_mainthread_only)                                             | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**AllJoynCloseBusHandle**](https://www.bing.com/search?q=AllJoynCloseBusHandle)                                                                                                               | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**AllJoynConnectToBus**](https://www.bing.com/search?q=AllJoynConnectToBus)                                                                                                                   | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**AllJoynEnumEvents**](https://www.bing.com/search?q=AllJoynEnumEvents)                                                                                                                       | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**AllJoynEventSelect**](https://www.bing.com/search?q=AllJoynEventSelect)                                                                                                                     | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**AllJoynReceiveFromBus**](https://www.bing.com/search?q=AllJoynReceiveFromBus)                                                                                                               | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**AllJoynSendToBus**](https://www.bing.com/search?q=AllJoynSendToBus)                                                                                                                         | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**QCC\_StatusText**](https://www.bing.com/search?q=QCC_StatusText)                                                                                                                            | Introduced into MSAJApi.dll in Windows 10.0.10240.0 |
| [**alljoyn\_autopinger\_adddestination**](https://www.bing.com/search?q=alljoyn_autopinger_adddestination)                                                                                     | Introduced into MSAJApi.dll in Windows 10.0.10586.0 |
| [**alljoyn\_autopinger\_addpinggroup**](https://www.bing.com/search?q=alljoyn_autopinger_addpinggroup)                                                                                         | Introduced into MSAJApi.dll in Windows 10.0.10586.0 |
| [**alljoyn\_autopinger\_create**](https://www.bing.com/search?q=alljoyn_autopinger_create)                                                                                                     | Introduced into MSAJApi.dll in Windows 10.0.10586.0 |
| [**alljoyn\_autopinger\_destroy**](https://www.bing.com/search?q=alljoyn_autopinger_destroy)                                                                                                   | Introduced into MSAJApi.dll in Windows 10.0.10586.0 |
| [**alljoyn\_autopinger\_pause**](https://www.bing.com/search?q=alljoyn_autopinger_pause)                                                                                                       | Introduced into MSAJApi.dll in Windows 10.0.10586.0 |
| [**alljoyn\_autopinger\_removedestination**](https://www.bing.com/search?q=alljoyn_autopinger_removedestination)                                                                               | Introduced into MSAJApi.dll in Windows 10.0.10586.0 |
| [**alljoyn\_autopinger\_removepinggroup**](https://www.bing.com/search?q=alljoyn_autopinger_removepinggroup)                                                                                   | Introduced into MSAJApi.dll in Windows 10.0.10586.0 |
| [**alljoyn\_autopinger\_resume**](https://www.bing.com/search?q=alljoyn_autopinger_resume)                                                                                                     | Introduced into MSAJApi.dll in Windows 10.0.10586.0 |
| [**alljoyn\_autopinger\_setpinginterval**](https://www.bing.com/search?q=alljoyn_autopinger_setpinginterval)                                                                                   | Introduced into MSAJApi.dll in Windows 10.0.10586.0 |
| [**alljoyn\_busattachment\_enablepeersecuritywithpermissionconfigurationlistener**](https://www.bing.com/search?q=alljoyn_busattachment_enablepeersecuritywithpermissionconfigurationlistener) | Introduced into MSAJApi.dll in Windows 10.0.10586.0 |
| [**alljoyn\_busattachment\_secureconnection**](https://www.bing.com/search?q=alljoyn_busattachment_secureconnection)                                                                           | Introduced into MSAJApi.dll in Windows 10.0.10586.0 |
| [**alljoyn\_busattachment\_secureconnectionasync**](https://www.bing.com/search?q=alljoyn_busattachment_secureconnectionasync)                                                                 | Introduced into MSAJApi.dll in Windows 10.0.10586.0 |
| [**alljoyn\_permissionconfigurationlistener\_create**](https://www.bing.com/search?q=alljoyn_permissionconfigurationlistener_create)                                                           | Introduced into MSAJApi.dll in Windows 10.0.10586.0 |
| [**alljoyn\_permissionconfigurationlistener\_destroy**](https://www.bing.com/search?q=alljoyn_permissionconfigurationlistener_destroy)                                                         | Introduced into MSAJApi.dll in Windows 10.0.10586.0 |
| [**alljoyn\_pinglistener\_create**](https://www.bing.com/search?q=alljoyn_pinglistener_create)                                                                                                 | Introduced into MSAJApi.dll in Windows 10.0.10586.0 |
| [**alljoyn\_pinglistener\_destroy**](https://www.bing.com/search?q=alljoyn_pinglistener_destroy)                                                                                               | Introduced into MSAJApi.dll in Windows 10.0.10586.0 |

 

## <span id="_MSCOREE.DLL"></span>APIs from the dll mscoree.dll


| API                                                    | Requirements                                        |
|--------------------------------------------------------|-----------------------------------------------------|
| [**MetaDataGetDispenser**](https://msdn.microsoft.com/en-us/library/windows/apps/br229853.aspx) | Introduced into mscoree.dll in Windows 10.0.10240.0 |

 

## <span id="_MSWSOCK.DLL"></span>APIs from the dll mswsock.dll


| API                                                        | Requirements                                        |
|------------------------------------------------------------|-----------------------------------------------------|
| [**AcceptEx**](https://msdn.microsoft.com/en-us/library/windows/apps/ms737524.aspx)                         | Introduced into mswsock.dll in Windows 10.0.10240.0 |
| [**GetAcceptExSockaddrs**](https://msdn.microsoft.com/en-us/library/windows/apps/ms738516.aspx) | Introduced into mswsock.dll in Windows 10.0.10240.0 |
| [**TransmitFile**](https://msdn.microsoft.com/en-us/library/windows/apps/ms740565.aspx)                 | Introduced into mswsock.dll in Windows 10.0.10240.0 |

 

## <span id="_NCRYPT.DLL"></span>APIs from the dll ncrypt.dll


| API                                                                            | Requirements                                                                                    |
|--------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| [**BCryptCloseAlgorithmProvider**](https://msdn.microsoft.com/en-us/library/windows/apps/aa375377.aspx) | Introduced into ncrypt.dll in Windows 10.0.10240.0. Moved to Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptCreateHash**](https://msdn.microsoft.com/en-us/library/windows/apps/aa375383.aspx)                         | Introduced into ncrypt.dll in Windows 10.0.10240.0. Moved to Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptDecrypt**](https://msdn.microsoft.com/en-us/library/windows/apps/aa375391.aspx)                               | Introduced into ncrypt.dll in Windows 10.0.10240.0. Moved to Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptDeriveKey**](https://msdn.microsoft.com/en-us/library/windows/apps/aa375393.aspx)                                | Introduced into ncrypt.dll in Windows 10.0.10240.0. Moved to Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptDeriveKeyCapi**](https://msdn.microsoft.com/en-us/library/windows/apps/dd433794.aspx)                        | Introduced into ncrypt.dll in Windows 10.0.10240.0. Moved to Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptDeriveKeyPBKDF2**](https://msdn.microsoft.com/en-us/library/windows/apps/dd433795.aspx)                    | Introduced into ncrypt.dll in Windows 10.0.10240.0. Moved to Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptDestroyHash**](https://msdn.microsoft.com/en-us/library/windows/apps/aa375399.aspx)                       | Introduced into ncrypt.dll in Windows 10.0.10240.0. Moved to Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptDestroyKey**](https://msdn.microsoft.com/en-us/library/windows/apps/aa375404.aspx)                         | Introduced into ncrypt.dll in Windows 10.0.10240.0. Moved to Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptDestroySecret**](https://msdn.microsoft.com/en-us/library/windows/apps/aa375407.aspx)                        | Introduced into ncrypt.dll in Windows 10.0.10240.0. Moved to Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptDuplicateHash**](https://msdn.microsoft.com/en-us/library/windows/apps/aa375413.aspx)                   | Introduced into ncrypt.dll in Windows 10.0.10240.0. Moved to Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptDuplicateKey**](https://msdn.microsoft.com/en-us/library/windows/apps/aa375419.aspx)                     | Introduced into ncrypt.dll in Windows 10.0.10240.0. Moved to Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptEncrypt**](https://msdn.microsoft.com/en-us/library/windows/apps/aa375421.aspx)                               | Introduced into ncrypt.dll in Windows 10.0.10240.0. Moved to Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptEnumAlgorithms**](https://msdn.microsoft.com/en-us/library/windows/apps/aa375422.aspx)                 | Introduced into ncrypt.dll in Windows 10.0.10240.0. Moved to Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptEnumProviders**](https://msdn.microsoft.com/en-us/library/windows/apps/aa375429.aspx)                   | Introduced into ncrypt.dll in Windows 10.0.10240.0. Moved to Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptExportKey**](https://msdn.microsoft.com/en-us/library/windows/apps/aa375434.aspx)                           | Introduced into ncrypt.dll in Windows 10.0.10240.0. Moved to Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptFinalizeKeyPair**](https://msdn.microsoft.com/en-us/library/windows/apps/aa375439.aspx)               | Introduced into ncrypt.dll in Windows 10.0.10240.0. Moved to Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptFinishHash**](https://msdn.microsoft.com/en-us/library/windows/apps/aa375443.aspx)                         | Introduced into ncrypt.dll in Windows 10.0.10240.0. Moved to Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptFreeBuffer**](https://msdn.microsoft.com/en-us/library/windows/apps/aa375445.aspx)                         | Introduced into ncrypt.dll in Windows 10.0.10240.0. Moved to Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptGenerateKeyPair**](https://msdn.microsoft.com/en-us/library/windows/apps/aa375451.aspx)               | Introduced into ncrypt.dll in Windows 10.0.10240.0. Moved to Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptGenerateSymmetricKey**](https://msdn.microsoft.com/en-us/library/windows/apps/aa375453.aspx)     | Introduced into ncrypt.dll in Windows 10.0.10240.0. Moved to Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptGenRandom**](https://msdn.microsoft.com/en-us/library/windows/apps/aa375458.aspx)                           | Introduced into ncrypt.dll in Windows 10.0.10240.0. Moved to Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptGetProperty**](https://msdn.microsoft.com/en-us/library/windows/apps/aa375464.aspx)                       | Introduced into ncrypt.dll in Windows 10.0.10240.0. Moved to Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptHash**](https://msdn.microsoft.com/en-us/library/windows/apps/mt633798.aspx)                                          | Introduced into ncrypt.dll in Windows 10.0.10240.0. Moved to Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptHashData**](https://msdn.microsoft.com/en-us/library/windows/apps/aa375468.aspx)                             | Introduced into ncrypt.dll in Windows 10.0.10240.0. Moved to Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptImportKey**](https://msdn.microsoft.com/en-us/library/windows/apps/aa375475.aspx)                           | Introduced into ncrypt.dll in Windows 10.0.10240.0. Moved to Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptImportKeyPair**](https://msdn.microsoft.com/en-us/library/windows/apps/aa375472.aspx)                        | Introduced into ncrypt.dll in Windows 10.0.10240.0. Moved to Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptKeyDerivation**](https://msdn.microsoft.com/en-us/library/windows/apps/hh448506.aspx)                        | Introduced into ncrypt.dll in Windows 10.0.10240.0. Moved to Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptOpenAlgorithmProvider**](https://msdn.microsoft.com/en-us/library/windows/apps/aa375479.aspx)   | Introduced into ncrypt.dll in Windows 10.0.10240.0. Moved to Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptSecretAgreement**](https://msdn.microsoft.com/en-us/library/windows/apps/aa375496.aspx)                    | Introduced into ncrypt.dll in Windows 10.0.10240.0. Moved to Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptSetProperty**](https://msdn.microsoft.com/en-us/library/windows/apps/aa375504.aspx)                       | Introduced into ncrypt.dll in Windows 10.0.10240.0. Moved to Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptSignHash**](https://msdn.microsoft.com/en-us/library/windows/apps/aa375510.aspx)                             | Introduced into ncrypt.dll in Windows 10.0.10240.0. Moved to Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptVerifySignature**](https://msdn.microsoft.com/en-us/library/windows/apps/aa375515.aspx)               | Introduced into ncrypt.dll in Windows 10.0.10240.0. Moved to Bcrypt.dll in Windows 10.0.10586.0 |
| [**NCryptCreateClaim**](https://msdn.microsoft.com/en-us/library/windows/apps/mt270085.aspx)                            | Introduced into ncrypt.dll in Windows 10.0.10240.0                                              |
| [**NCryptCreatePersistedKey**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376247.aspx)         | Introduced into ncrypt.dll in Windows 10.0.10240.0                                              |
| [**NCryptDecrypt**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376249.aspx)                               | Introduced into ncrypt.dll in Windows 10.0.10240.0                                              |
| [**NCryptDeleteKey**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376251.aspx)                           | Introduced into ncrypt.dll in Windows 10.0.10240.0                                              |
| [**NCryptDeriveKey**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376252.aspx)                                | Introduced into ncrypt.dll in Windows 10.0.10240.0                                              |
| [**NCryptEncrypt**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376255.aspx)                               | Introduced into ncrypt.dll in Windows 10.0.10240.0                                              |
| [**NCryptEnumAlgorithms**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376257.aspx)                 | Introduced into ncrypt.dll in Windows 10.0.10240.0                                              |
| [**NCryptEnumKeys**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376259.aspx)                             | Introduced into ncrypt.dll in Windows 10.0.10240.0                                              |
| [**NCryptExportKey**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376263.aspx)                           | Introduced into ncrypt.dll in Windows 10.0.10240.0                                              |
| [**NCryptFinalizeKey**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376265.aspx)                       | Introduced into ncrypt.dll in Windows 10.0.10240.0                                              |
| [**NCryptFreeBuffer**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376267.aspx)                         | Introduced into ncrypt.dll in Windows 10.0.10240.0                                              |
| [**NCryptFreeObject**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376269.aspx)                         | Introduced into ncrypt.dll in Windows 10.0.10240.0                                              |
| [**NCryptGetProperty**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376273.aspx)                       | Introduced into ncrypt.dll in Windows 10.0.10240.0                                              |
| [**NCryptImportKey**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376276.aspx)                           | Introduced into ncrypt.dll in Windows 10.0.10240.0                                              |
| [**NCryptIsAlgSupported**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376278.aspx)                 | Introduced into ncrypt.dll in Windows 10.0.10240.0                                              |
| [**NCryptKeyDerivation**](https://msdn.microsoft.com/en-us/library/windows/apps/hh448516.aspx)                        | Introduced into ncrypt.dll in Windows 10.0.10240.0                                              |
| [**NCryptOpenKey**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376284.aspx)                               | Introduced into ncrypt.dll in Windows 10.0.10240.0                                              |
| [**NCryptOpenStorageProvider**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376286.aspx)       | Introduced into ncrypt.dll in Windows 10.0.10240.0                                              |
| [**NCryptSecretAgreement**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376289.aspx)                    | Introduced into ncrypt.dll in Windows 10.0.10240.0                                              |
| [**NCryptSetProperty**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376292.aspx)                       | Introduced into ncrypt.dll in Windows 10.0.10240.0                                              |
| [**NCryptSignHash**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376295.aspx)                             | Introduced into ncrypt.dll in Windows 10.0.10240.0                                              |
| [**NCryptVerifyClaim**](https://msdn.microsoft.com/en-us/library/windows/apps/mt270086.aspx)                            | Introduced into ncrypt.dll in Windows 10.0.10240.0                                              |
| [**NCryptVerifySignature**](https://msdn.microsoft.com/en-us/library/windows/apps/aa376298.aspx)               | Introduced into ncrypt.dll in Windows 10.0.10240.0                                              |

 

## <span id="_NTDLL.DLL"></span>APIs from the dll ntdll.dll


| API                                                                 | Requirements                                      |
|---------------------------------------------------------------------|---------------------------------------------------|
| [**RtlEthernetAddressToStringA**](https://msdn.microsoft.com/en-us/library/windows/apps/dn550721.aspx) | Introduced into ntdll.dll in Windows 10.0.10240.0 |
| [**RtlEthernetAddressToStringW**](https://msdn.microsoft.com/en-us/library/windows/apps/dn550721.aspx) | Introduced into ntdll.dll in Windows 10.0.10240.0 |
| [**RtlEthernetStringToAddressA**](https://msdn.microsoft.com/en-us/library/windows/apps/dn550722.aspx) | Introduced into ntdll.dll in Windows 10.0.10240.0 |
| [**RtlEthernetStringToAddressW**](https://msdn.microsoft.com/en-us/library/windows/apps/dn550722.aspx) | Introduced into ntdll.dll in Windows 10.0.10240.0 |
| [**RtlIpv4AddressToStringA**](https://msdn.microsoft.com/en-us/library/windows/apps/aa814456.aspx)         | Introduced into ntdll.dll in Windows 10.0.10240.0 |
| [**RtlIpv4AddressToStringExA**](https://msdn.microsoft.com/en-us/library/windows/apps/aa814457.aspx)     | Introduced into ntdll.dll in Windows 10.0.10240.0 |
| [**RtlIpv4AddressToStringExW**](https://msdn.microsoft.com/en-us/library/windows/apps/aa814457.aspx)     | Introduced into ntdll.dll in Windows 10.0.10240.0 |
| [**RtlIpv4AddressToStringW**](https://msdn.microsoft.com/en-us/library/windows/apps/aa814456.aspx)         | Introduced into ntdll.dll in Windows 10.0.10240.0 |
| [**RtlIpv4StringToAddressA**](https://msdn.microsoft.com/en-us/library/windows/apps/aa814458.aspx)         | Introduced into ntdll.dll in Windows 10.0.10240.0 |
| [**RtlIpv4StringToAddressExA**](https://msdn.microsoft.com/en-us/library/windows/apps/aa814459.aspx)     | Introduced into ntdll.dll in Windows 10.0.10240.0 |
| [**RtlIpv4StringToAddressExW**](https://msdn.microsoft.com/en-us/library/windows/apps/aa814459.aspx)     | Introduced into ntdll.dll in Windows 10.0.10240.0 |
| [**RtlIpv4StringToAddressW**](https://msdn.microsoft.com/en-us/library/windows/apps/aa814458.aspx)         | Introduced into ntdll.dll in Windows 10.0.10240.0 |
| [**RtlIpv6AddressToStringA**](https://msdn.microsoft.com/en-us/library/windows/apps/aa814460.aspx)         | Introduced into ntdll.dll in Windows 10.0.10240.0 |
| [**RtlIpv6AddressToStringExA**](https://msdn.microsoft.com/en-us/library/windows/apps/aa814461.aspx)     | Introduced into ntdll.dll in Windows 10.0.10240.0 |
| [**RtlIpv6AddressToStringExW**](https://msdn.microsoft.com/en-us/library/windows/apps/aa814461.aspx)     | Introduced into ntdll.dll in Windows 10.0.10240.0 |
| [**RtlIpv6AddressToStringW**](https://msdn.microsoft.com/en-us/library/windows/apps/aa814460.aspx)         | Introduced into ntdll.dll in Windows 10.0.10240.0 |
| [**RtlIpv6StringToAddressA**](https://msdn.microsoft.com/en-us/library/windows/apps/aa814462.aspx)         | Introduced into ntdll.dll in Windows 10.0.10240.0 |
| [**RtlIpv6StringToAddressExA**](https://msdn.microsoft.com/en-us/library/windows/apps/aa814463.aspx)     | Introduced into ntdll.dll in Windows 10.0.10240.0 |
| [**RtlIpv6StringToAddressExW**](https://msdn.microsoft.com/en-us/library/windows/apps/aa814463.aspx)     | Introduced into ntdll.dll in Windows 10.0.10240.0 |
| [**RtlIpv6StringToAddressW**](https://msdn.microsoft.com/en-us/library/windows/apps/aa814462.aspx)         | Introduced into ntdll.dll in Windows 10.0.10240.0 |

 

## <span id="_OLEAUT32.DLL"></span>APIs from the dll oleaut32.dll


| API                                                                     | Requirements                                         |
|-------------------------------------------------------------------------|------------------------------------------------------|
| [**BSTR\_UserFree**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644523.aspx)                             | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**BSTR\_UserFree64**](https://msdn.microsoft.com/en-us/library/windows/apps/hh309490.aspx)                         | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**BSTR\_UserMarshal**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644509.aspx)                       | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**BSTR\_UserMarshal64**](https://msdn.microsoft.com/en-us/library/windows/apps/hh309491.aspx)                   | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**BSTR\_UserSize**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644365.aspx)                             | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**BSTR\_UserSize64**](https://msdn.microsoft.com/en-us/library/windows/apps/hh309492.aspx)                         | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**BSTR\_UserUnmarshal**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644522.aspx)                   | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**BSTR\_UserUnmarshal64**](https://msdn.microsoft.com/en-us/library/windows/apps/hh309493.aspx)               | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**DispInvoke**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221366.aspx)                                    | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**LPSAFEARRAY\_Marshal**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644537.aspx)                 | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**LPSAFEARRAY\_Size**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644517.aspx)                       | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**LPSAFEARRAY\_Unmarshal**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644390.aspx)             | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**LPSAFEARRAY\_UserFree**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644504.aspx)               | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**LPSAFEARRAY\_UserFree64**](https://msdn.microsoft.com/en-us/library/windows/apps/hh768285.aspx)           | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**LPSAFEARRAY\_UserMarshal**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644398.aspx)         | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**LPSAFEARRAY\_UserMarshal64**](https://msdn.microsoft.com/en-us/library/windows/apps/hh768286.aspx)     | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**LPSAFEARRAY\_UserSize**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644399.aspx)               | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**LPSAFEARRAY\_UserSize64**](https://msdn.microsoft.com/en-us/library/windows/apps/hh768287.aspx)           | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**LPSAFEARRAY\_UserUnmarshal**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644503.aspx)     | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**LPSAFEARRAY\_UserUnmarshal64**](https://msdn.microsoft.com/en-us/library/windows/apps/hh768288.aspx) | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**SafeArrayAccessData**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221620.aspx)                  | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**SafeArrayAllocData**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221468.aspx)                    | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**SafeArrayAllocDescriptor**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221407.aspx)        | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**SafeArrayAllocDescriptorEx**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221540.aspx)    | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**SafeArrayCopy**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221451.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**SafeArrayCopyData**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221174.aspx)                      | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**SafeArrayCreate**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221234.aspx)                          | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**SafeArrayCreateEx**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221198.aspx)                      | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**SafeArrayCreateVector**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221558.aspx)              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**SafeArrayCreateVectorEx**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221093.aspx)          | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**SafeArrayDestroy**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221702.aspx)                        | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**SafeArrayDestroyData**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221418.aspx)                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**SafeArrayDestroyDescriptor**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221681.aspx)    | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**SafeArrayGetDim**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221539.aspx)                          | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**SafeArrayGetElement**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221255.aspx)                  | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**SafeArrayGetElemsize**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221074.aspx)                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**SafeArrayGetIID**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221428.aspx)                          | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**SafeArrayGetLBound**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221622.aspx)                    | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**SafeArrayGetRecordInfo**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221022.aspx)            | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**SafeArrayGetUBound**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221584.aspx)                    | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**SafeArrayGetVartype**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221446.aspx)                  | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**SafeArrayLock**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221492.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**SafeArrayPtrOfIndex**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221452.aspx)                  | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**SafeArrayPutElement**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221283.aspx)                  | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**SafeArrayRedim**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221002.aspx)                            | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**SafeArraySetIID**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221347.aspx)                          | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**SafeArraySetRecordInfo**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221287.aspx)            | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**SafeArrayUnaccessData**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221203.aspx)              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**SafeArrayUnlock**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221246.aspx)                          | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**SysAllocString**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221458.aspx)                            | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**SysAllocStringByteLen**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221637.aspx)              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**SysAllocStringLen**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221639.aspx)                      | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**SysFreeString**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221481.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**SysReAllocString**](https://msdn.microsoft.com/en-us/library/windows/apps/ms220986.aspx)                        | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**SysReAllocStringLen**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221533.aspx)                  | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**SysStringByteLen**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221097.aspx)                        | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**SysStringLen**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221240.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**SystemTimeToVariantTime**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221646.aspx)          | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarAbs**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221343.aspx)                                            | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarAdd**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221574.aspx)                                            | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarAnd**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221576.aspx)                                            | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarBoolFromCy**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221228.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarBoolFromDate**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221076.aspx)                          | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarBoolFromDec**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221677.aspx)                            | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarBoolFromDisp**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221284.aspx)                          | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarBoolFromI1**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221660.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarBoolFromI2**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221157.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarBoolFromI4**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221056.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarBoolFromI8**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644364.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarBoolFromR4**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221579.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarBoolFromR8**](https://msdn.microsoft.com/en-us/library/windows/apps/ms220994.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarBoolFromStr**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221300.aspx)                            | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarBoolFromUI1**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221202.aspx)                            | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarBoolFromUI2**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221158.aspx)                            | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarBoolFromUI4**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221431.aspx)                            | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarBoolFromUI8**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644380.aspx)                            | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarBstrCat**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221621.aspx)                                    | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarBstrCmp**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221038.aspx)                                    | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarBstrFromBool**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221338.aspx)                          | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarBstrFromCy**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221218.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarBstrFromDate**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221699.aspx)                          | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarBstrFromDec**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221304.aspx)                            | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarBstrFromDisp**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221305.aspx)                          | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarBstrFromI1**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221419.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarBstrFromI2**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221016.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarBstrFromI4**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221516.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarBstrFromI8**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644520.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarBstrFromR4**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221092.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarBstrFromR8**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221632.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarBstrFromUI1**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221230.aspx)                            | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarBstrFromUI2**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221693.aspx)                            | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarBstrFromUI4**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221361.aspx)                            | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarBstrFromUI8**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644394.aspx)                            | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarCat**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221084.aspx)                                            | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarCmp**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221006.aspx)                                            | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarCyAbs**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221356.aspx)                                        | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarCyAdd**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221636.aspx)                                        | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarCyCmp**](https://msdn.microsoft.com/en-us/library/windows/apps/ms220995.aspx)                                        | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarCyCmpR8**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221175.aspx)                                    | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarCyFix**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221532.aspx)                                        | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarCyFromBool**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221667.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarCyFromDate**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221216.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarCyFromDec**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221384.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarCyFromDisp**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221045.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarCyFromI1**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221534.aspx)                                  | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarCyFromI2**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221484.aspx)                                  | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarCyFromI4**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221280.aspx)                                  | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarCyFromI8**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644370.aspx)                                  | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarCyFromR4**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221335.aspx)                                  | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarCyFromR8**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221572.aspx)                                  | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarCyFromStr**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221582.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarCyFromUI1**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221671.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarCyFromUI2**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221684.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarCyFromUI4**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221459.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarCyFromUI8**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644391.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarCyInt**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221054.aspx)                                        | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarCyMul**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221412.aspx)                                        | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarCyMulI4**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221104.aspx)                                    | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarCyMulI8**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644381.aspx)                                    | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarCyNeg**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221514.aspx)                                        | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarCyRound**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221546.aspx)                                    | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarCySub**](https://msdn.microsoft.com/en-us/library/windows/apps/ms220982.aspx)                                        | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarDateFromBool**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221310.aspx)                          | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarDateFromCy**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221519.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarDateFromDec**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221122.aspx)                            | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarDateFromDisp**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221271.aspx)                          | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarDateFromI1**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221408.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarDateFromI2**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221475.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarDateFromI4**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221380.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarDateFromI8**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644361.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarDateFromR4**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221261.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarDateFromR8**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221441.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarDateFromStr**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221395.aspx)                            | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarDateFromUdate**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221036.aspx)                        | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarDateFromUdateEx**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221630.aspx)                    | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarDateFromUI1**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221443.aspx)                            | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarDateFromUI2**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221166.aspx)                            | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarDateFromUI4**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221292.aspx)                            | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarDateFromUI8**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644507.aspx)                            | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarDecAbs**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221601.aspx)                                      | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarDecAdd**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221264.aspx)                                      | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarDecCmp**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221686.aspx)                                      | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarDecCmpR8**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221512.aspx)                                  | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarDecDiv**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221344.aspx)                                      | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarDecFix**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221341.aspx)                                      | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarDecFromBool**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221530.aspx)                            | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarDecFromCy**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221536.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarDecFromDate**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221650.aspx)                            | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarDecFromDisp**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221274.aspx)                            | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarDecFromI1**](https://msdn.microsoft.com/en-us/library/windows/apps/ms220988.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarDecFromI2**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221511.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarDecFromI4**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221219.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarDecFromI8**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644377.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarDecFromR4**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221517.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarDecFromR8**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221241.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarDecFromStr**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221334.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarDecFromUI1**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221654.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarDecFromUI2**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221154.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarDecFromUI4**](https://msdn.microsoft.com/en-us/library/windows/apps/ms220997.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarDecFromUI8**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644388.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarDecInt**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221189.aspx)                                      | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarDecMul**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221527.aspx)                                      | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarDecNeg**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221491.aspx)                                      | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarDecRound**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221075.aspx)                                  | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarDecSub**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221556.aspx)                                      | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarDiv**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221253.aspx)                                            | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarEqv**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221077.aspx)                                            | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarFix**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221664.aspx)                                            | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarFormat**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221128.aspx)                                      | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarFormatCurrency**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221424.aspx)                      | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarFormatDateTime**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221554.aspx)                      | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarFormatFromTokens**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221147.aspx)                  | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarFormatNumber**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221477.aspx)                          | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarFormatPercent**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221125.aspx)                        | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarI1FromBool**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221049.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarI1FromCy**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221389.aspx)                                  | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarI1FromDate**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221012.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarI1FromDec**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221094.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarI1FromDisp**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221373.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarI1FromI2**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221716.aspx)                                  | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarI1FromI4**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221129.aspx)                                  | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarI1FromI8**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644518.aspx)                                  | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarI1FromR4**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221312.aspx)                                  | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarI1FromR8**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221195.aspx)                                  | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarI1FromStr**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221201.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarI1FromUI1**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221208.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarI1FromUI2**](https://msdn.microsoft.com/en-us/library/windows/apps/ms220998.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarI1FromUI4**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221560.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarI1FromUI8**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644383.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarI2FromBool**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221178.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarI2FromCy**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221153.aspx)                                  | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarI2FromDate**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221642.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarI2FromDec**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221005.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarI2FromDisp**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221088.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarI2FromI1**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221623.aspx)                                  | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarI2FromI4**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221668.aspx)                                  | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarI2FromI8**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644393.aspx)                                  | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarI2FromR4**](https://msdn.microsoft.com/en-us/library/windows/apps/ms220989.aspx)                                  | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarI2FromR8**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221429.aspx)                                  | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarI2FromStr**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221411.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarI2FromUI1**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221659.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarI2FromUI2**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221327.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarI2FromUI4**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221383.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarI2FromUI8**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644362.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarI4FromBool**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221483.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarI4FromCy**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221707.aspx)                                  | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarI4FromDate**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221403.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarI4FromDec**](https://msdn.microsoft.com/en-us/library/windows/apps/ms220984.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarI4FromDisp**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221605.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarI4FromI1**](https://msdn.microsoft.com/en-us/library/windows/apps/ms220991.aspx)                                  | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarI4FromI2**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221137.aspx)                                  | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarI4FromI8**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644516.aspx)                                  | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarI4FromR4**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221066.aspx)                                  | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarI4FromR8**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221146.aspx)                                  | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarI4FromStr**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221194.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarI4FromUI1**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221044.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarI4FromUI2**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221182.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarI4FromUI4**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221611.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarI4FromUI8**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644378.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarI8FromBool**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644385.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarI8FromCy**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644514.aspx)                                  | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarI8FromDate**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644386.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarI8FromDec**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644389.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarI8FromDisp**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644506.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarI8FromI1**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644375.aspx)                                  | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarI8FromI2**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644528.aspx)                                  | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarI8FromR4**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644384.aspx)                                  | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarI8FromR8**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644369.aspx)                                  | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarI8FromStr**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644510.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarI8FromUI1**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644531.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarI8FromUI2**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644367.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarI8FromUI4**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644513.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarI8FromUI8**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644524.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VARIANT\_UserFree**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644359.aspx)                       | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VARIANT\_UserFree64**](https://msdn.microsoft.com/en-us/library/windows/apps/hh309497.aspx)                   | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VARIANT\_UserMarshal**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644368.aspx)                 | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VARIANT\_UserMarshal64**](https://msdn.microsoft.com/en-us/library/windows/apps/hh309498.aspx)             | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VARIANT\_UserSize**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644387.aspx)                       | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VARIANT\_UserSize64**](https://msdn.microsoft.com/en-us/library/windows/apps/hh309499.aspx)                   | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VARIANT\_UserUnmarshal**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644534.aspx)             | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VARIANT\_UserUnmarshal64**](https://msdn.microsoft.com/en-us/library/windows/apps/hh309500.aspx)         | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VariantChangeType**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221258.aspx)                      | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VariantChangeTypeEx**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221634.aspx)                  | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VariantClear**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221165.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VariantCopy**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221697.aspx)                                  | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VariantCopyInd**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221184.aspx)                            | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VariantInit**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221402.aspx)                                  | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VariantTimeToSystemTime**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221440.aspx)          | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarIdiv**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221682.aspx)                                          | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarImp**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221497.aspx)                                            | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarInt**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221460.aspx)                                            | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarMod**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221405.aspx)                                            | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarMonthName**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221299.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarMul**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221602.aspx)                                            | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarNeg**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221413.aspx)                                            | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarNot**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221606.aspx)                                            | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarNumFromParseNum**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221357.aspx)                    | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarOr**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221358.aspx)                                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarParseNumFromStr**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221573.aspx)                    | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarPow**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221303.aspx)                                            | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarR4CmpR8**](https://msdn.microsoft.com/en-us/library/windows/apps/ms220981.aspx)                                    | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarR4FromBool**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221476.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarR4FromCy**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221071.aspx)                                  | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarR4FromDate**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221266.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarR4FromDec**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221651.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarR4FromDisp**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221392.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarR4FromI1**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221454.aspx)                                  | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarR4FromI2**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221055.aspx)                                  | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarR4FromI4**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221156.aspx)                                  | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarR4FromI8**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644392.aspx)                                  | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarR4FromR8**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221273.aspx)                                  | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarR4FromStr**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221513.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarR4FromUI1**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221631.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarR4FromUI2**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221322.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarR4FromUI4**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221028.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarR4FromUI8**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644539.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarR8FromBool**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221613.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarR8FromCy**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221239.aspx)                                  | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarR8FromDate**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221034.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarR8FromDec**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221523.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarR8FromDisp**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221525.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarR8FromI1**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221462.aspx)                                  | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarR8FromI2**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221500.aspx)                                  | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarR8FromI4**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221714.aspx)                                  | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarR8FromI8**](https://msdn.microsoft.com/en-us/library/windows/apps/ms313882.aspx)                                  | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarR8FromR4**](https://msdn.microsoft.com/en-us/library/windows/apps/ms220977.aspx)                                  | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarR8FromStr**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221331.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarR8FromUI1**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221603.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarR8FromUI2**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221709.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarR8FromUI4**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221013.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarR8FromUI8**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644395.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarR8Pow**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221090.aspx)                                        | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarR8Round**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221501.aspx)                                    | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarRound**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221372.aspx)                                        | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarSub**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221079.aspx)                                            | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarTokenizeFormatString**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221340.aspx)          | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarUdateFromDate**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221217.aspx)                        | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarUI1FromBool**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221095.aspx)                            | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarUI1FromCy**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221535.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarUI1FromDate**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221011.aspx)                            | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarUI1FromDec**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221406.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarUI1FromDisp**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221151.aspx)                            | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarUI1FromI1**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221291.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarUI1FromI2**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221281.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarUI1FromI4**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221024.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarUI1FromI8**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644500.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarUI1FromR4**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221279.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarUI1FromR8**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221051.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarUI1FromStr**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221537.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarUI1FromUI2**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221163.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarUI1FromUI4**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221493.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarUI1FromUI8**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644535.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarUI2FromBool**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221070.aspx)                            | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarUI2FromCy**](https://msdn.microsoft.com/en-us/library/windows/apps/ms220979.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarUI2FromDate**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221489.aspx)                            | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarUI2FromDec**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221132.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarUI2FromDisp**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221710.aspx)                            | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarUI2FromI1**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221638.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarUI2FromI2**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221294.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarUI2FromI4**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221548.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarUI2FromI8**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644502.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarUI2FromR4**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221131.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarUI2FromR8**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221490.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarUI2FromStr**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221635.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarUI2FromUI1**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221043.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarUI2FromUI4**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221205.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarUI2FromUI8**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644526.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarUI4FromBool**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221415.aspx)                            | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarUI4FromCy**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221448.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarUI4FromDate**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221362.aspx)                            | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarUI4FromDec**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221624.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarUI4FromDisp**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221276.aspx)                            | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarUI4FromI1**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221221.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarUI4FromI2**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221562.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarUI4FromI4**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221209.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarUI4FromI8**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644533.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarUI4FromR4**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221518.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarUI4FromR8**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221073.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarUI4FromStr**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221715.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarUI4FromUI1**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221633.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarUI4FromUI2**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221521.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarUI4FromUI8**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644538.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarUI8FromBool**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644525.aspx)                            | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarUI8FromCy**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644508.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarUI8FromDate**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644396.aspx)                            | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarUI8FromDec**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644371.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarUI8FromDisp**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644515.aspx)                            | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarUI8FromI1**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644376.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarUI8FromI2**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644527.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarUI8FromI8**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644511.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarUI8FromR4**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644382.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarUI8FromR8**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644397.aspx)                                | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarUI8FromStr**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644536.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarUI8FromUI1**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644532.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarUI8FromUI2**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644366.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarUI8FromUI4**](https://msdn.microsoft.com/en-us/library/windows/apps/ms644363.aspx)                              | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarWeekdayName**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221315.aspx)                            | Introduced into oleaut32.dll in Windows 10.0.10240.0 |
| [**VarXor**](https://msdn.microsoft.com/en-us/library/windows/apps/ms221188.aspx)                                            | Introduced into oleaut32.dll in Windows 10.0.10240.0 |

 

## <span id="_PROPSYS.DLL"></span>APIs from the dll propsys.dll


| API                                                                               | Requirements                                        |
|-----------------------------------------------------------------------------------|-----------------------------------------------------|
| [**PropVariantCompareEx**](https://msdn.microsoft.com/en-us/library/windows/apps/bb776517.aspx)                       | Introduced into propsys.dll in Windows 10.0.10240.0 |
| [**PropVariantToWinRTPropertyValue**](https://msdn.microsoft.com/en-us/library/windows/apps/dn313197.aspx) | Introduced into propsys.dll in Windows 10.0.10240.0 |
| [**WinRTPropertyValueToPropVariant**](https://msdn.microsoft.com/en-us/library/windows/apps/dn313198.aspx) | Introduced into propsys.dll in Windows 10.0.10240.0 |

 

## <span id="_RPCRT4.DLL"></span>APIs from the dll rpcrt4.dll


| API                                                                                                            | Requirements                                       |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| [**CreateProxyFromTypeInfo**](https://www.bing.com/search?q=CreateProxyFromTypeInfo)                           | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**CreateStubFromTypeInfo**](https://www.bing.com/search?q=CreateStubFromTypeInfo)                             | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**CStdStubBuffer\_AddRef**](https://msdn.microsoft.com/en-us/library/windows/apps/aa373611.aspx)                                                        | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**CStdStubBuffer\_Connect**](https://msdn.microsoft.com/en-us/library/windows/apps/aa373612.aspx)                                                      | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**CStdStubBuffer\_CountRefs**](https://msdn.microsoft.com/en-us/library/windows/apps/aa373613.aspx)                                                  | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**CStdStubBuffer\_DebugServerQueryInterface**](https://msdn.microsoft.com/en-us/library/windows/apps/aa373614.aspx)                  | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**CStdStubBuffer\_DebugServerRelease**](https://msdn.microsoft.com/en-us/library/windows/apps/aa373615.aspx)                                | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**CStdStubBuffer\_Disconnect**](https://msdn.microsoft.com/en-us/library/windows/apps/aa373616.aspx)                                                | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**CStdStubBuffer\_Invoke**](https://msdn.microsoft.com/en-us/library/windows/apps/aa373617.aspx)                                                        | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**CStdStubBuffer\_IsIIDSupported**](https://www.bing.com/search?q=CStdStubBuffer_IsIIDSupported)              | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**CStdStubBuffer\_QueryInterface**](https://www.bing.com/search?q=CStdStubBuffer_QueryInterface)              | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**IUnknown\_AddRef\_Proxy**](https://msdn.microsoft.com/en-us/library/windows/apps/aa373957.aspx)                                                       | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**IUnknown\_QueryInterface\_Proxy**](https://msdn.microsoft.com/en-us/library/windows/apps/aa373958.aspx)                                       | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**IUnknown\_Release\_Proxy**](https://msdn.microsoft.com/en-us/library/windows/apps/aa373959.aspx)                                                     | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**Ndr64AsyncClientCall**](https://msdn.microsoft.com/en-us/library/windows/apps/mt728979.aspx)                                                           | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**Ndr64AsyncServerCall64**](https://www.bing.com/search?q=Ndr64AsyncServerCall64)                             | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**Ndr64AsyncServerCallAll**](https://msdn.microsoft.com/en-us/library/windows/apps/mt728980.aspx)                                                     | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrAllocate**](https://www.bing.com/search?q=NdrAllocate)                                                   | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrAsyncClientCall**](https://msdn.microsoft.com/en-us/library/windows/apps/aa374207.aspx)                                                               | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrAsyncServerCall**](https://msdn.microsoft.com/en-us/library/windows/apps/mt728981.aspx)                                                               | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrByteCountPointerBufferSize**](https://www.bing.com/search?q=NdrByteCountPointerBufferSize)               | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrByteCountPointerFree**](https://www.bing.com/search?q=NdrByteCountPointerFree)                           | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrByteCountPointerMarshall**](https://www.bing.com/search?q=NdrByteCountPointerMarshall)                   | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrByteCountPointerUnmarshall**](https://www.bing.com/search?q=NdrByteCountPointerUnmarshall)               | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NDRCContextBinding**](https://www.bing.com/search?q=NDRCContextBinding)                                     | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NDRCContextMarshall**](https://www.bing.com/search?q=NDRCContextMarshall)                                   | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NDRCContextUnmarshall**](https://www.bing.com/search?q=NDRCContextUnmarshall)                               | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrClearOutParameters**](https://www.bing.com/search?q=NdrClearOutParameters)                               | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrClientCall2**](https://msdn.microsoft.com/en-us/library/windows/apps/aa374215.aspx)                                                                       | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrClientCall3**](https://msdn.microsoft.com/en-us/library/windows/apps/mt712330.aspx)                                                                       | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrClientContextMarshall**](https://www.bing.com/search?q=NdrClientContextMarshall)                         | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrClientContextUnmarshall**](https://www.bing.com/search?q=NdrClientContextUnmarshall)                     | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrClientInitialize**](https://www.bing.com/search?q=NdrClientInitialize)                                   | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrClientInitializeNew**](https://www.bing.com/search?q=NdrClientInitializeNew)                             | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrComplexArrayBufferSize**](https://www.bing.com/search?q=NdrComplexArrayBufferSize)                       | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrComplexArrayFree**](https://www.bing.com/search?q=NdrComplexArrayFree)                                   | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrComplexArrayMarshall**](https://www.bing.com/search?q=NdrComplexArrayMarshall)                           | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrComplexArrayMemorySize**](https://www.bing.com/search?q=NdrComplexArrayMemorySize)                       | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrComplexArrayUnmarshall**](https://www.bing.com/search?q=NdrComplexArrayUnmarshall)                       | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrComplexStructBufferSize**](https://www.bing.com/search?q=NdrComplexStructBufferSize)                     | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrComplexStructFree**](https://www.bing.com/search?q=NdrComplexStructFree)                                 | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrComplexStructMarshall**](https://www.bing.com/search?q=NdrComplexStructMarshall)                         | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrComplexStructMemorySize**](https://www.bing.com/search?q=NdrComplexStructMemorySize)                     | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrComplexStructUnmarshall**](https://www.bing.com/search?q=NdrComplexStructUnmarshall)                     | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrConformantArrayBufferSize**](https://www.bing.com/search?q=NdrConformantArrayBufferSize)                 | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrConformantArrayFree**](https://www.bing.com/search?q=NdrConformantArrayFree)                             | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrConformantArrayMarshall**](https://www.bing.com/search?q=NdrConformantArrayMarshall)                     | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrConformantArrayMemorySize**](https://www.bing.com/search?q=NdrConformantArrayMemorySize)                 | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrConformantArrayUnmarshall**](https://www.bing.com/search?q=NdrConformantArrayUnmarshall)                 | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrConformantStringBufferSize**](https://msdn.microsoft.com/en-us/library/windows/apps/aa374220.aspx)                                         | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrConformantStringMarshall**](https://msdn.microsoft.com/en-us/library/windows/apps/aa374223.aspx)                                             | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrConformantStringMemorySize**](https://www.bing.com/search?q=NdrConformantStringMemorySize)               | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrConformantStringUnmarshall**](https://msdn.microsoft.com/en-us/library/windows/apps/aa374225.aspx)                                         | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrConformantStructBufferSize**](https://www.bing.com/search?q=NdrConformantStructBufferSize)               | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrConformantStructFree**](https://www.bing.com/search?q=NdrConformantStructFree)                           | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrConformantStructMarshall**](https://www.bing.com/search?q=NdrConformantStructMarshall)                   | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrConformantStructMemorySize**](https://www.bing.com/search?q=NdrConformantStructMemorySize)               | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrConformantStructUnmarshall**](https://www.bing.com/search?q=NdrConformantStructUnmarshall)               | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrConformantVaryingArrayBufferSize**](https://www.bing.com/search?q=NdrConformantVaryingArrayBufferSize)   | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrConformantVaryingArrayFree**](https://www.bing.com/search?q=NdrConformantVaryingArrayFree)               | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrConformantVaryingArrayMarshall**](https://www.bing.com/search?q=NdrConformantVaryingArrayMarshall)       | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrConformantVaryingArrayMemorySize**](https://www.bing.com/search?q=NdrConformantVaryingArrayMemorySize)   | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrConformantVaryingArrayUnmarshall**](https://www.bing.com/search?q=NdrConformantVaryingArrayUnmarshall)   | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrConformantVaryingStructBufferSize**](https://www.bing.com/search?q=NdrConformantVaryingStructBufferSize) | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrConformantVaryingStructFree**](https://www.bing.com/search?q=NdrConformantVaryingStructFree)             | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrConformantVaryingStructMarshall**](https://www.bing.com/search?q=NdrConformantVaryingStructMarshall)     | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrConformantVaryingStructMemorySize**](https://www.bing.com/search?q=NdrConformantVaryingStructMemorySize) | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrConformantVaryingStructUnmarshall**](https://www.bing.com/search?q=NdrConformantVaryingStructUnmarshall) | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrContextHandleInitialize**](https://msdn.microsoft.com/en-us/library/windows/apps/aa374229.aspx)                                               | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrContextHandleSize**](https://msdn.microsoft.com/en-us/library/windows/apps/aa374236.aspx)                                                           | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrConvert**](https://www.bing.com/search?q=NdrConvert)                                                     | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrConvert2**](https://www.bing.com/search?q=NdrConvert2)                                                   | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrCorrelationFree**](https://www.bing.com/search?q=NdrCorrelationFree)                                     | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrCorrelationInitialize**](https://www.bing.com/search?q=NdrCorrelationInitialize)                         | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrCorrelationPass**](https://www.bing.com/search?q=NdrCorrelationPass)                                     | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrCreateServerInterfaceFromStub**](https://www.bing.com/search?q=NdrCreateServerInterfaceFromStub)         | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrCStdStubBuffer\_Release**](https://msdn.microsoft.com/en-us/library/windows/apps/aa374242.aspx)                                                | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrCStdStubBuffer2\_Release**](https://msdn.microsoft.com/en-us/library/windows/apps/aa374240.aspx)                                              | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrDllCanUnloadNow**](https://msdn.microsoft.com/en-us/library/windows/apps/aa374245.aspx)                                                               | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrDllGetClassObject**](https://msdn.microsoft.com/en-us/library/windows/apps/aa374251.aspx)                                                           | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrDllRegisterProxy**](https://msdn.microsoft.com/en-us/library/windows/apps/aa374255.aspx)                                                             | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrDllUnregisterProxy**](https://msdn.microsoft.com/en-us/library/windows/apps/aa374257.aspx)                                                         | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrEncapsulatedUnionBufferSize**](https://www.bing.com/search?q=NdrEncapsulatedUnionBufferSize)             | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrEncapsulatedUnionFree**](https://www.bing.com/search?q=NdrEncapsulatedUnionFree)                         | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrEncapsulatedUnionMarshall**](https://www.bing.com/search?q=NdrEncapsulatedUnionMarshall)                 | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrEncapsulatedUnionMemorySize**](https://www.bing.com/search?q=NdrEncapsulatedUnionMemorySize)             | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrEncapsulatedUnionUnmarshall**](https://www.bing.com/search?q=NdrEncapsulatedUnionUnmarshall)             | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrFixedArrayBufferSize**](https://www.bing.com/search?q=NdrFixedArrayBufferSize)                           | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrFixedArrayFree**](https://www.bing.com/search?q=NdrFixedArrayFree)                                       | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrFixedArrayMarshall**](https://www.bing.com/search?q=NdrFixedArrayMarshall)                               | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrFixedArrayMemorySize**](https://www.bing.com/search?q=NdrFixedArrayMemorySize)                           | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrFixedArrayUnmarshall**](https://www.bing.com/search?q=NdrFixedArrayUnmarshall)                           | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrFreeBuffer**](https://www.bing.com/search?q=NdrFreeBuffer)                                               | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrFullPointerXlatFree**](https://www.bing.com/search?q=NdrFullPointerXlatFree)                             | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrFullPointerXlatInit**](https://www.bing.com/search?q=NdrFullPointerXlatInit)                             | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrGetBuffer**](https://www.bing.com/search?q=NdrGetBuffer)                                                 | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrGetDcomProtocolVersion**](https://www.bing.com/search?q=NdrGetDcomProtocolVersion)                       | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrGetUserMarshalInfo**](https://msdn.microsoft.com/en-us/library/windows/apps/aa374262.aspx)                                                         | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrInterfacePointerBufferSize**](https://msdn.microsoft.com/en-us/library/windows/apps/aa374265.aspx)                                         | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrInterfacePointerFree**](https://msdn.microsoft.com/en-us/library/windows/apps/aa374269.aspx)                                                     | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrInterfacePointerMarshall**](https://msdn.microsoft.com/en-us/library/windows/apps/aa374272.aspx)                                             | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrInterfacePointerMemorySize**](https://www.bing.com/search?q=NdrInterfacePointerMemorySize)               | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrInterfacePointerUnmarshall**](https://msdn.microsoft.com/en-us/library/windows/apps/aa374278.aspx)                                         | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrMapCommAndFaultStatus**](https://www.bing.com/search?q=NdrMapCommAndFaultStatus)                         | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrNonConformantStringBufferSize**](https://www.bing.com/search?q=NdrNonConformantStringBufferSize)         | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrNonConformantStringMarshall**](https://www.bing.com/search?q=NdrNonConformantStringMarshall)             | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrNonConformantStringMemorySize**](https://www.bing.com/search?q=NdrNonConformantStringMemorySize)         | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrNonConformantStringUnmarshall**](https://www.bing.com/search?q=NdrNonConformantStringUnmarshall)         | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrNonEncapsulatedUnionBufferSize**](https://www.bing.com/search?q=NdrNonEncapsulatedUnionBufferSize)       | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrNonEncapsulatedUnionFree**](https://www.bing.com/search?q=NdrNonEncapsulatedUnionFree)                   | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrNonEncapsulatedUnionMarshall**](https://www.bing.com/search?q=NdrNonEncapsulatedUnionMarshall)           | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrNonEncapsulatedUnionMemorySize**](https://www.bing.com/search?q=NdrNonEncapsulatedUnionMemorySize)       | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrNonEncapsulatedUnionUnmarshall**](https://www.bing.com/search?q=NdrNonEncapsulatedUnionUnmarshall)       | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrNsGetBuffer**](https://www.bing.com/search?q=NdrNsGetBuffer)                                             | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrNsSendReceive**](https://www.bing.com/search?q=NdrNsSendReceive)                                         | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrOleAllocate**](https://msdn.microsoft.com/en-us/library/windows/apps/aa374280.aspx)                                                                       | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrOleFree**](https://msdn.microsoft.com/en-us/library/windows/apps/aa374285.aspx)                                                                               | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrPartialIgnoreClientBufferSize**](https://www.bing.com/search?q=NdrPartialIgnoreClientBufferSize)         | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrPartialIgnoreClientMarshall**](https://www.bing.com/search?q=NdrPartialIgnoreClientMarshall)             | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrPartialIgnoreServerInitialize**](https://www.bing.com/search?q=NdrPartialIgnoreServerInitialize)         | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrPartialIgnoreServerUnmarshall**](https://www.bing.com/search?q=NdrPartialIgnoreServerUnmarshall)         | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrPointerBufferSize**](https://msdn.microsoft.com/en-us/library/windows/apps/aa374289.aspx)                                                           | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrPointerFree**](https://msdn.microsoft.com/en-us/library/windows/apps/aa374291.aspx)                                                                       | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrPointerMarshall**](https://msdn.microsoft.com/en-us/library/windows/apps/aa374293.aspx)                                                               | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrPointerMemorySize**](https://www.bing.com/search?q=NdrPointerMemorySize)                                 | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrPointerUnmarshall**](https://msdn.microsoft.com/en-us/library/windows/apps/aa374296.aspx)                                                           | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrProxyErrorHandler**](https://msdn.microsoft.com/en-us/library/windows/apps/aa374299.aspx)                                                           | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrRangeUnmarshall**](https://www.bing.com/search?q=NdrRangeUnmarshall)                                     | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrRpcSmClientAllocate**](https://www.bing.com/search?q=NdrRpcSmClientAllocate)                             | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrRpcSmClientFree**](https://www.bing.com/search?q=NdrRpcSmClientFree)                                     | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrRpcSmSetClientToOsf**](https://www.bing.com/search?q=NdrRpcSmSetClientToOsf)                             | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrRpcSsDefaultAllocate**](https://www.bing.com/search?q=NdrRpcSsDefaultAllocate)                           | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrRpcSsDefaultFree**](https://www.bing.com/search?q=NdrRpcSsDefaultFree)                                   | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrRpcSsDisableAllocate**](https://www.bing.com/search?q=NdrRpcSsDisableAllocate)                           | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrRpcSsEnableAllocate**](https://www.bing.com/search?q=NdrRpcSsEnableAllocate)                             | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NDRSContextMarshall**](https://www.bing.com/search?q=NDRSContextMarshall)                                   | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NDRSContextMarshall2**](https://www.bing.com/search?q=NDRSContextMarshall2)                                 | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NDRSContextMarshallEx**](https://www.bing.com/search?q=NDRSContextMarshallEx)                               | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NDRSContextUnmarshall**](https://www.bing.com/search?q=NDRSContextUnmarshall)                               | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NDRSContextUnmarshall2**](https://www.bing.com/search?q=NDRSContextUnmarshall2)                             | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NDRSContextUnmarshallEx**](https://www.bing.com/search?q=NDRSContextUnmarshallEx)                           | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrSendReceive**](https://www.bing.com/search?q=NdrSendReceive)                                             | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrServerCall2**](https://msdn.microsoft.com/en-us/library/windows/apps/mt728982.aspx)                                                                       | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrServerCallAll**](https://msdn.microsoft.com/en-us/library/windows/apps/mt728983.aspx)                                                                   | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrServerCallNdr64**](https://www.bing.com/search?q=NdrServerCallNdr64)                                     | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrServerContextMarshall**](https://www.bing.com/search?q=NdrServerContextMarshall)                         | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrServerContextNewMarshall**](https://www.bing.com/search?q=NdrServerContextNewMarshall)                   | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrServerContextNewUnmarshall**](https://www.bing.com/search?q=NdrServerContextNewUnmarshall)               | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrServerContextUnmarshall**](https://www.bing.com/search?q=NdrServerContextUnmarshall)                     | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrServerInitialize**](https://www.bing.com/search?q=NdrServerInitialize)                                   | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrServerInitializeMarshall**](https://www.bing.com/search?q=NdrServerInitializeMarshall)                   | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrServerInitializeNew**](https://www.bing.com/search?q=NdrServerInitializeNew)                             | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrServerInitializePartial**](https://www.bing.com/search?q=NdrServerInitializePartial)                     | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrServerInitializeUnmarshall**](https://www.bing.com/search?q=NdrServerInitializeUnmarshall)               | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrSimpleStructBufferSize**](https://www.bing.com/search?q=NdrSimpleStructBufferSize)                       | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrSimpleStructFree**](https://www.bing.com/search?q=NdrSimpleStructFree)                                   | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrSimpleStructMarshall**](https://www.bing.com/search?q=NdrSimpleStructMarshall)                           | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrSimpleStructMemorySize**](https://www.bing.com/search?q=NdrSimpleStructMemorySize)                       | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrSimpleStructUnmarshall**](https://www.bing.com/search?q=NdrSimpleStructUnmarshall)                       | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrSimpleTypeMarshall**](https://msdn.microsoft.com/en-us/library/windows/apps/aa374313.aspx)                                                         | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrSimpleTypeUnmarshall**](https://msdn.microsoft.com/en-us/library/windows/apps/aa374315.aspx)                                                     | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrStubCall2**](https://msdn.microsoft.com/en-us/library/windows/apps/aa374317.aspx)                                                                           | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrStubCall3**](https://msdn.microsoft.com/en-us/library/windows/apps/mt728984.aspx)                                                                           | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrStubForwardingFunction**](https://msdn.microsoft.com/en-us/library/windows/apps/aa374320.aspx)                                                 | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrUserMarshalBufferSize**](https://msdn.microsoft.com/en-us/library/windows/apps/aa374329.aspx)                                                   | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrUserMarshalFree**](https://msdn.microsoft.com/en-us/library/windows/apps/aa374332.aspx)                                                               | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrUserMarshalMarshall**](https://msdn.microsoft.com/en-us/library/windows/apps/aa374334.aspx)                                                       | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrUserMarshalMemorySize**](https://www.bing.com/search?q=NdrUserMarshalMemorySize)                         | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrUserMarshalSimpleTypeConvert**](https://www.bing.com/search?q=NdrUserMarshalSimpleTypeConvert)           | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrUserMarshalUnmarshall**](https://www.bing.com/search?q=NdrUserMarshalUnmarshall)                         | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrVaryingArrayBufferSize**](https://www.bing.com/search?q=NdrVaryingArrayBufferSize)                       | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrVaryingArrayFree**](https://www.bing.com/search?q=NdrVaryingArrayFree)                                   | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrVaryingArrayMarshall**](https://www.bing.com/search?q=NdrVaryingArrayMarshall)                           | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrVaryingArrayMemorySize**](https://www.bing.com/search?q=NdrVaryingArrayMemorySize)                       | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrVaryingArrayUnmarshall**](https://www.bing.com/search?q=NdrVaryingArrayUnmarshall)                       | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrXmitOrRepAsBufferSize**](https://www.bing.com/search?q=NdrXmitOrRepAsBufferSize)                         | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrXmitOrRepAsFree**](https://www.bing.com/search?q=NdrXmitOrRepAsFree)                                     | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrXmitOrRepAsMarshall**](https://www.bing.com/search?q=NdrXmitOrRepAsMarshall)                             | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrXmitOrRepAsMemorySize**](https://www.bing.com/search?q=NdrXmitOrRepAsMemorySize)                         | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**NdrXmitOrRepAsUnmarshall**](https://www.bing.com/search?q=NdrXmitOrRepAsUnmarshall)                         | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**RpcSmAllocate**](https://msdn.microsoft.com/en-us/library/windows/apps/aa378458.aspx)                                                                         | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**RpcSmClientFree**](https://msdn.microsoft.com/en-us/library/windows/apps/aa378459.aspx)                                                                     | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**RpcSmDestroyClientContext**](https://msdn.microsoft.com/en-us/library/windows/apps/aa378460.aspx)                                                 | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**RpcSmDisableAllocate**](https://msdn.microsoft.com/en-us/library/windows/apps/aa378461.aspx)                                                           | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**RpcSmEnableAllocate**](https://msdn.microsoft.com/en-us/library/windows/apps/aa378462.aspx)                                                             | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**RpcSmFree**](https://msdn.microsoft.com/en-us/library/windows/apps/aa378463.aspx)                                                                                 | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**RpcSmGetThreadHandle**](https://msdn.microsoft.com/en-us/library/windows/apps/aa378464.aspx)                                                           | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**RpcSmSetClientAllocFree**](https://msdn.microsoft.com/en-us/library/windows/apps/aa378465.aspx)                                                     | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**RpcSmSetThreadHandle**](https://msdn.microsoft.com/en-us/library/windows/apps/aa378466.aspx)                                                           | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**RpcSmSwapClientAllocFree**](https://msdn.microsoft.com/en-us/library/windows/apps/aa378467.aspx)                                                   | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**RpcSsAllocate**](https://msdn.microsoft.com/en-us/library/windows/apps/aa378468.aspx)                                                                         | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**RpcSsDestroyClientContext**](https://msdn.microsoft.com/en-us/library/windows/apps/aa378471.aspx)                                                 | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**RpcSsDisableAllocate**](https://msdn.microsoft.com/en-us/library/windows/apps/aa378472.aspx)                                                           | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**RpcSsEnableAllocate**](https://msdn.microsoft.com/en-us/library/windows/apps/aa378474.aspx)                                                             | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**RpcSsFree**](https://msdn.microsoft.com/en-us/library/windows/apps/aa378475.aspx)                                                                                 | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**RpcSsGetThreadHandle**](https://msdn.microsoft.com/en-us/library/windows/apps/aa378476.aspx)                                                           | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**RpcSsSetClientAllocFree**](https://msdn.microsoft.com/en-us/library/windows/apps/aa378477.aspx)                                                     | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**RpcSsSetThreadHandle**](https://msdn.microsoft.com/en-us/library/windows/apps/aa378478.aspx)                                                           | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**RpcSsSwapClientAllocFree**](https://msdn.microsoft.com/en-us/library/windows/apps/aa378479.aspx)                                                   | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |
| [**RpcUserFree**](https://msdn.microsoft.com/en-us/library/windows/apps/mt297501.aspx)                                                                             | Introduced into rpcrt4.dll in Windows 10.0.10240.0 |

 

## <span id="_UIAUTOMATIONCORE.DLL"></span>APIs from the dll uiautomationcore.dll


| API                                                                                               | Requirements                                                 |
|---------------------------------------------------------------------------------------------------|--------------------------------------------------------------|
| [**UiaClientsAreListening**](https://msdn.microsoft.com/en-us/library/windows/apps/ee671704.aspx)                       | Introduced into uiautomationcore.dll in Windows 10.0.10240.0 |
| [**UiaDisconnectAllProviders**](https://msdn.microsoft.com/en-us/library/windows/apps/hh437311.aspx)                         | Introduced into uiautomationcore.dll in Windows 10.0.10240.0 |
| [**UiaDisconnectProvider**](https://msdn.microsoft.com/en-us/library/windows/apps/hh437312.aspx)                                 | Introduced into uiautomationcore.dll in Windows 10.0.10240.0 |
| [**UiaGetReservedMixedAttributeValue**](https://msdn.microsoft.com/en-us/library/windows/apps/ee684038.aspx) | Introduced into uiautomationcore.dll in Windows 10.0.10240.0 |
| [**UiaGetReservedNotSupportedValue**](https://msdn.microsoft.com/en-us/library/windows/apps/ee684039.aspx)     | Introduced into uiautomationcore.dll in Windows 10.0.10240.0 |
| [**UiaHostProviderFromHwnd**](https://msdn.microsoft.com/en-us/library/windows/apps/ee684044.aspx)                     | Introduced into uiautomationcore.dll in Windows 10.0.10240.0 |
| [**UiaProviderForNonClient**](https://msdn.microsoft.com/en-us/library/windows/apps/hh437314.aspx)                     | Introduced into uiautomationcore.dll in Windows 10.0.10240.0 |
| [**UiaProviderFromIAccessible**](https://msdn.microsoft.com/en-us/library/windows/apps/hh437315.aspx)               | Introduced into uiautomationcore.dll in Windows 10.0.10240.0 |
| [**UiaRaiseAsyncContentLoadedEvent**](https://msdn.microsoft.com/en-us/library/windows/apps/ee684061.aspx)     | Introduced into uiautomationcore.dll in Windows 10.0.10240.0 |
| [**UiaRaiseAutomationEvent**](https://msdn.microsoft.com/en-us/library/windows/apps/ee684062.aspx)                     | Introduced into uiautomationcore.dll in Windows 10.0.10240.0 |
| [**UiaRaiseAutomationPropertyChangedEvent**](https://msdn.microsoft.com/en-us/library/windows/apps/ee671601.aspx)    | Introduced into uiautomationcore.dll in Windows 10.0.10240.0 |
| [**UiaRaiseStructureChangedEvent**](https://msdn.microsoft.com/en-us/library/windows/apps/ee684063.aspx)         | Introduced into uiautomationcore.dll in Windows 10.0.10240.0 |
| [**UiaRaiseTextEditTextChangedEvent**](https://msdn.microsoft.com/en-us/library/windows/apps/dn302213.aspx)   | Introduced into uiautomationcore.dll in Windows 10.0.10240.0 |
| [**UiaReturnRawElementProvider**](https://msdn.microsoft.com/en-us/library/windows/apps/ee684069.aspx)             | Introduced into uiautomationcore.dll in Windows 10.0.10240.0 |
| [**UiaRaiseChangesEvent**](https://msdn.microsoft.com/en-us/library/windows/apps/mt733044.aspx)                           | Introduced into uiautomationcore.dll in Windows 10.0.14393.0 |

 

## <span id="_URLMON.DLL"></span>APIs from the dll urlmon.dll


| API                                                                              | Requirements                                       |
|----------------------------------------------------------------------------------|----------------------------------------------------|
| [**CreateUri**](https://www.bing.com/search?q=CreateUri)                         | Introduced into urlmon.dll in Windows 10.0.10240.0 |
| [**CreateUriWithFragment**](https://www.bing.com/search?q=CreateUriWithFragment) | Introduced into urlmon.dll in Windows 10.0.10240.0 |

 

## <span id="_WEBSERVICES.DLL"></span>APIs from the dll webservices.dll


| API                                                                                | Requirements                                            |
|------------------------------------------------------------------------------------|---------------------------------------------------------|
| [**WsAbandonCall**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430472.aspx)                                             | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsAbandonMessage**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430473.aspx)                                       | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsAbortChannel**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430474.aspx)                                           | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsAbortServiceProxy**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430477.aspx)                                 | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsAddCustomHeader**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430479.aspx)                                     | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsAddErrorString**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430480.aspx)                                       | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsAddMappedHeader**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430481.aspx)                                     | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsAddressMessage**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430482.aspx)                                       | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsAlloc**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430483.aspx)                                                         | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsAsyncExecute**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430484.aspx)                                           | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsCall**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430485.aspx)                                                           | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsCheckMustUnderstandHeaders**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430486.aspx)               | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsCloseChannel**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430487.aspx)                                           | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsCloseServiceProxy**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430490.aspx)                                 | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsCombineUrl**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430491.aspx)                                               | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsCopyError**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430492.aspx)                                                 | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsCopyNode**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430493.aspx)                                                   | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsCreateChannel**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430495.aspx)                                         | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsCreateError**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430497.aspx)                                             | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsCreateFaultFromError**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430498.aspx)                           | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsCreateHeap**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430499.aspx)                                               | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsCreateMessage**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430501.aspx)                                         | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsCreateMessageForChannel**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430502.aspx)                     | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsCreateMetadata**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430503.aspx)                                       | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsCreateReader**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430504.aspx)                                           | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsCreateServiceProxy**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430507.aspx)                               | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsCreateServiceProxyFromTemplate**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430508.aspx)       | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsCreateWriter**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430509.aspx)                                           | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsCreateXmlBuffer**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430510.aspx)                                     | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsCreateXmlSecurityToken**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430511.aspx)                       | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsDateTimeToFileTime**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430512.aspx)                               | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsDecodeUrl**](https://www.bing.com/search?q=WsDecodeUrl)                       | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsEncodeUrl**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430516.aspx)                                                 | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsEndReaderCanonicalization**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430517.aspx)                 | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsEndWriterCanonicalization**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430518.aspx)                 | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsFileTimeToDateTime**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430519.aspx)                               | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsFillBody**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430520.aspx)                                                   | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsFillReader**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430521.aspx)                                               | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsFindAttribute**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430522.aspx)                                         | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsFlushBody**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430523.aspx)                                                 | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsFlushWriter**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430524.aspx)                                             | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsFreeChannel**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430525.aspx)                                             | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsFreeError**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430526.aspx)                                                 | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsFreeHeap**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430527.aspx)                                                   | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsFreeMessage**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430529.aspx)                                             | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsFreeMetadata**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430530.aspx)                                           | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsFreeReader**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430531.aspx)                                               | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsFreeSecurityToken**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430532.aspx)                                 | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsFreeServiceProxy**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430534.aspx)                                   | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsFreeWriter**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430535.aspx)                                               | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsGetChannelProperty**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430536.aspx)                               | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsGetCustomHeader**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430537.aspx)                                     | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsGetDictionary**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430538.aspx)                                         | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsGetErrorProperty**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430539.aspx)                                   | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsGetErrorString**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430540.aspx)                                       | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsGetFaultErrorDetail**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430541.aspx)                             | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsGetFaultErrorProperty**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430542.aspx)                         | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsGetHeader**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430543.aspx)                                                 | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsGetHeaderAttributes**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430544.aspx)                             | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsGetHeapProperty**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430545.aspx)                                     | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsGetMappedHeader**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430547.aspx)                                     | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsGetMessageProperty**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430548.aspx)                               | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsGetMetadataEndpoints**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430549.aspx)                           | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsGetMetadataProperty**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430550.aspx)                             | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsGetMissingMetadataDocumentAddress**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430551.aspx) | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsGetNamespaceFromPrefix**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430552.aspx)                       | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsGetPolicyAlternativeCount**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430554.aspx)                 | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsGetPolicyProperty**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430556.aspx)                                 | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsGetPrefixFromNamespace**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430557.aspx)                       | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsGetReaderNode**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430558.aspx)                                         | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsGetReaderPosition**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430559.aspx)                                 | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsGetReaderProperty**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430560.aspx)                                 | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsGetSecurityContextProperty**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430561.aspx)               | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsGetSecurityTokenProperty**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430562.aspx)                   | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsGetServiceProxyProperty**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430564.aspx)                     | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsGetWriterPosition**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430565.aspx)                                 | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsGetWriterProperty**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430566.aspx)                                 | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsGetXmlAttribute**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430567.aspx)                                     | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsInitializeMessage**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430568.aspx)                                 | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsMarkHeaderAsUnderstood**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430569.aspx)                       | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsMatchPolicyAlternative**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430570.aspx)                       | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsMoveReader**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430571.aspx)                                               | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsMoveWriter**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430572.aspx)                                               | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsOpenChannel**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430574.aspx)                                             | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsOpenServiceProxy**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430577.aspx)                                   | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsPullBytes**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430578.aspx)                                                 | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsPushBytes**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430580.aspx)                                                 | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsReadArray**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430581.aspx)                                                 | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsReadAttribute**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430582.aspx)                                         | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsReadBody**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430583.aspx)                                                   | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsReadBytes**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430584.aspx)                                                 | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsReadChars**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430585.aspx)                                                 | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsReadCharsUtf8**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430586.aspx)                                         | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsReadElement**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430587.aspx)                                             | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsReadEndAttribute**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430588.aspx)                                   | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsReadEndElement**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430589.aspx)                                       | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsReadEndpointAddressExtension**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430590.aspx)           | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsReadEnvelopeEnd**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430591.aspx)                                     | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsReadEnvelopeStart**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430592.aspx)                                 | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsReadMessageEnd**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430593.aspx)                                       | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsReadMessageStart**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430594.aspx)                                   | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsReadMetadata**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430595.aspx)                                           | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsReadNode**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430596.aspx)                                                   | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsReadQualifiedName**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430597.aspx)                                 | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsReadStartAttribute**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430598.aspx)                               | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsReadStartElement**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430599.aspx)                                   | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsReadToStartElement**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430600.aspx)                               | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsReadType**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430601.aspx)                                                   | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsReadValue**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430602.aspx)                                                 | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsReadXmlBuffer**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430603.aspx)                                         | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsReadXmlBufferFromBytes**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430604.aspx)                       | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsReceiveMessage**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430605.aspx)                                       | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsRemoveCustomHeader**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430607.aspx)                               | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsRemoveHeader**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430608.aspx)                                           | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsRemoveMappedHeader**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430609.aspx)                               | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsRemoveNode**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430610.aspx)                                               | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsRequestReply**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430611.aspx)                                           | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsRequestSecurityToken**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430612.aspx)                           | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsResetChannel**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430613.aspx)                                           | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsResetError**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430614.aspx)                                               | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsResetHeap**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430615.aspx)                                                 | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsResetMessage**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430617.aspx)                                           | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsResetMetadata**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430618.aspx)                                         | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsResetServiceProxy**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430620.aspx)                                 | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsRevokeSecurityContext**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430621.aspx)                         | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsSendFaultMessageForError**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430622.aspx)                   | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsSendMessage**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430623.aspx)                                             | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsSendReplyMessage**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430624.aspx)                                   | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsSetChannelProperty**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430626.aspx)                               | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsSetErrorProperty**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430627.aspx)                                   | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsSetFaultErrorDetail**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430628.aspx)                             | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsSetFaultErrorProperty**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430629.aspx)                         | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsSetHeader**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430630.aspx)                                                 | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsSetInput**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430631.aspx)                                                   | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsSetInputToBuffer**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430632.aspx)                                   | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsSetMessageProperty**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430634.aspx)                               | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsSetOutput**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430635.aspx)                                                 | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsSetOutputToBuffer**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430636.aspx)                                 | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsSetReaderPosition**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430637.aspx)                                 | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsSetWriterPosition**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430638.aspx)                                 | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsShutdownSessionChannel**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430639.aspx)                       | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsSkipNode**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430640.aspx)                                                   | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsStartReaderCanonicalization**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430641.aspx)             | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsStartWriterCanonicalization**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430642.aspx)             | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsTrimXmlWhitespace**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430643.aspx)                                 | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsVerifyXmlNCName**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430645.aspx)                                     | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsWriteArray**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430646.aspx)                                               | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsWriteAttribute**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430647.aspx)                                       | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsWriteBody**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430648.aspx)                                                 | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsWriteBytes**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430649.aspx)                                               | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsWriteChars**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430650.aspx)                                               | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsWriteCharsUtf8**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430651.aspx)                                       | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsWriteElement**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430652.aspx)                                           | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsWriteEndAttribute**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430653.aspx)                                 | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsWriteEndCData**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430654.aspx)                                         | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsWriteEndElement**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430655.aspx)                                     | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsWriteEndStartElement**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430656.aspx)                           | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsWriteEnvelopeEnd**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430657.aspx)                                   | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsWriteEnvelopeStart**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430658.aspx)                               | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsWriteMessageEnd**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430659.aspx)                                     | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsWriteMessageStart**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430660.aspx)                                 | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsWriteNode**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430661.aspx)                                                 | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsWriteQualifiedName**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430662.aspx)                               | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsWriteStartAttribute**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430663.aspx)                             | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsWriteStartCData**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430664.aspx)                                     | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsWriteStartElement**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430665.aspx)                                 | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsWriteText**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430667.aspx)                                                 | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsWriteType**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430668.aspx)                                                 | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsWriteValue**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430669.aspx)                                               | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsWriteXmlBuffer**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430670.aspx)                                       | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsWriteXmlBufferToBytes**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430671.aspx)                         | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsWriteXmlnsAttribute**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430672.aspx)                             | Introduced into webservices.dll in Windows 10.0.10240.0 |
| [**WsXmlStringEquals**](https://msdn.microsoft.com/en-us/library/windows/apps/dd430673.aspx)                                     | Introduced into webservices.dll in Windows 10.0.10240.0 |

 

## <span id="_windows.data.pdf.dll"></span><span id="_WINDOWS.DATA.PDF.DLL"></span>APIs from the dll windows.data.pdf.dll


| API                                              | Requirements                                                 |
|--------------------------------------------------|--------------------------------------------------------------|
| [**PdfCreateRenderer**](https://msdn.microsoft.com/en-us/library/windows/apps/dn302145.aspx) | Introduced into windows.data.pdf.dll in Windows 10.0.10240.0 |

 

## <span id="_windows.networking.dll"></span><span id="_WINDOWS.NETWORKING.DLL"></span>APIs from the dll windows.networking.dll


| API                                                                    | Requirements                                                   |
|------------------------------------------------------------------------|----------------------------------------------------------------|
| [**SetSocketMediaStreamingMode**](https://msdn.microsoft.com/en-us/library/windows/apps/hh994468.aspx) | Introduced into windows.networking.dll in Windows 10.0.10240.0 |

 

## <span id="_WINDOWSCODECS.DLL"></span>APIs from the dll windowscodecs.dll


| API                                                                             | Requirements                                              |
|---------------------------------------------------------------------------------|-----------------------------------------------------------|
| [**WICConvertBitmapSource**](https://msdn.microsoft.com/en-us/library/windows/apps/ee719819.aspx)             | Introduced into windowscodecs.dll in Windows 10.0.10240.0 |
| [**WICCreateBitmapFromSection**](https://msdn.microsoft.com/en-us/library/windows/apps/ee719820.aspx)     | Introduced into windowscodecs.dll in Windows 10.0.10240.0 |
| [**WICCreateBitmapFromSectionEx**](https://msdn.microsoft.com/en-us/library/windows/apps/ee719821.aspx) | Introduced into windowscodecs.dll in Windows 10.0.10240.0 |
| [**WICGetMetadataContentSize**](https://msdn.microsoft.com/en-us/library/windows/apps/ee719825.aspx)       | Introduced into windowscodecs.dll in Windows 10.0.10240.0 |
| [**WICMapGuidToShortName**](https://msdn.microsoft.com/en-us/library/windows/apps/ee719835.aspx)               | Introduced into windowscodecs.dll in Windows 10.0.10240.0 |
| [**WICMapSchemaToName**](https://msdn.microsoft.com/en-us/library/windows/apps/ee719836.aspx)                     | Introduced into windowscodecs.dll in Windows 10.0.10240.0 |
| [**WICMapShortNameToGuid**](https://msdn.microsoft.com/en-us/library/windows/apps/ee719837.aspx)               | Introduced into windowscodecs.dll in Windows 10.0.10240.0 |
| [**WICMatchMetadataContent**](https://msdn.microsoft.com/en-us/library/windows/apps/ee719838.aspx)           | Introduced into windowscodecs.dll in Windows 10.0.10240.0 |
| [**WICSerializeMetadataContent**](https://msdn.microsoft.com/en-us/library/windows/apps/ee719865.aspx)   | Introduced into windowscodecs.dll in Windows 10.0.10240.0 |

 

## <span id="_WS2_32.DLL"></span>APIs from the dll ws2\_32.dll


| API                                                                               | Requirements                                        |
|-----------------------------------------------------------------------------------|-----------------------------------------------------|
| [**\_\_WSAFDIsSet**](https://msdn.microsoft.com/en-us/library/windows/apps/ms741578.aspx)                                          | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**accept**](https://msdn.microsoft.com/en-us/library/windows/apps/ms737526.aspx)                                                    | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**bind**](https://msdn.microsoft.com/en-us/library/windows/apps/ms737550.aspx)                                                        | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**closesocket**](https://msdn.microsoft.com/en-us/library/windows/apps/ms737582.aspx)                                          | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**connect**](https://msdn.microsoft.com/en-us/library/windows/apps/ms737625.aspx)                                                  | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**freeaddrinfo**](https://msdn.microsoft.com/en-us/library/windows/apps/ms737931.aspx)                                        | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**FreeAddrInfoExW**](https://msdn.microsoft.com/en-us/library/windows/apps/ms737906.aspx)                                     | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**FreeAddrInfoW**](https://msdn.microsoft.com/en-us/library/windows/apps/ms737912.aspx)                                        | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**getaddrinfo**](https://msdn.microsoft.com/en-us/library/windows/apps/ms738520.aspx)                                          | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**GetAddrInfoExCancel**](https://msdn.microsoft.com/en-us/library/windows/apps/hh448782.aspx)                            | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**GetAddrInfoExOverlappedResult**](https://msdn.microsoft.com/en-us/library/windows/apps/hh448783.aspx)        | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**GetAddrInfoExW**](https://msdn.microsoft.com/en-us/library/windows/apps/ms738518.aspx)                                       | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**GetAddrInfoW**](https://msdn.microsoft.com/en-us/library/windows/apps/ms738519.aspx)                                          | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**gethostbyaddr**](https://msdn.microsoft.com/en-us/library/windows/apps/ms738521.aspx)                                      | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**gethostbyname**](https://msdn.microsoft.com/en-us/library/windows/apps/ms738524.aspx)                                      | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**gethostname**](https://msdn.microsoft.com/en-us/library/windows/apps/ms738527.aspx)                                          | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**GetHostNameW**](https://msdn.microsoft.com/en-us/library/windows/apps/dn793576.aspx)                                          | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**getnameinfo**](https://msdn.microsoft.com/en-us/library/windows/apps/ms738532.aspx)                                          | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**GetNameInfoW**](https://msdn.microsoft.com/en-us/library/windows/apps/ms738531.aspx)                                          | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**getpeername**](https://msdn.microsoft.com/en-us/library/windows/apps/ms738533.aspx)                                          | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**getprotobyname**](https://msdn.microsoft.com/en-us/library/windows/apps/ms738534.aspx)                                    | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**getprotobynumber**](https://msdn.microsoft.com/en-us/library/windows/apps/ms738537.aspx)                                | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**getservbyname**](https://msdn.microsoft.com/en-us/library/windows/apps/ms738538.aspx)                                      | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**getservbyport**](https://msdn.microsoft.com/en-us/library/windows/apps/ms738541.aspx)                                      | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**getsockname**](https://msdn.microsoft.com/en-us/library/windows/apps/ms738543.aspx)                                          | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**getsockopt**](https://msdn.microsoft.com/en-us/library/windows/apps/ms738544.aspx)                                            | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**htonl**](https://msdn.microsoft.com/en-us/library/windows/apps/ms738556.aspx)                                                      | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**htons**](https://msdn.microsoft.com/en-us/library/windows/apps/ms738557.aspx)                                                      | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**inet\_addr**](https://msdn.microsoft.com/en-us/library/windows/apps/ms738563.aspx)                                             | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**inet\_ntoa**](https://msdn.microsoft.com/en-us/library/windows/apps/ms738564.aspx)                                             | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**inet\_ntop**](https://www.bing.com/search?q=inet_ntop)                         | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**inet\_pton**](https://www.bing.com/search?q=inet_pton)                         | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**InetNtopW**](https://msdn.microsoft.com/en-us/library/windows/apps/cc805843.aspx)                                                | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**InetPtonW**](https://msdn.microsoft.com/en-us/library/windows/apps/cc805844.aspx)                                                | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**ioctlsocket**](https://msdn.microsoft.com/en-us/library/windows/apps/ms738573.aspx)                                          | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**listen**](https://msdn.microsoft.com/en-us/library/windows/apps/ms739168.aspx)                                                    | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**ntohl**](https://msdn.microsoft.com/en-us/library/windows/apps/ms740069.aspx)                                                      | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**ntohs**](https://msdn.microsoft.com/en-us/library/windows/apps/ms740075.aspx)                                                      | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**recv**](https://msdn.microsoft.com/en-us/library/windows/apps/ms740121.aspx)                                                        | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**recvfrom**](https://msdn.microsoft.com/en-us/library/windows/apps/ms740120.aspx)                                                | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**select**](https://msdn.microsoft.com/en-us/library/windows/apps/ms740141.aspx)                                                    | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**send**](https://msdn.microsoft.com/en-us/library/windows/apps/ms740149.aspx)                                                        | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**sendto**](https://msdn.microsoft.com/en-us/library/windows/apps/ms740148.aspx)                                                    | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**SetAddrInfoExW**](https://msdn.microsoft.com/en-us/library/windows/apps/ms740473.aspx)                                       | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**setsockopt**](https://msdn.microsoft.com/en-us/library/windows/apps/ms740476.aspx)                                            | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**shutdown**](https://msdn.microsoft.com/en-us/library/windows/apps/ms740481.aspx)                                                | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**socket**](https://msdn.microsoft.com/en-us/library/windows/apps/ms740506.aspx)                                                    | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**WSAAccept**](https://msdn.microsoft.com/en-us/library/windows/apps/ms741513.aspx)                                              | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**WSAAddressToStringA**](https://msdn.microsoft.com/en-us/library/windows/apps/ms741516.aspx)                           | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**WSAAddressToStringW**](https://msdn.microsoft.com/en-us/library/windows/apps/ms741516.aspx)                           | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**WSACleanup**](https://msdn.microsoft.com/en-us/library/windows/apps/ms741549.aspx)                                            | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**WSACloseEvent**](https://msdn.microsoft.com/en-us/library/windows/apps/ms741551.aspx)                                      | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**WSAConnect**](https://msdn.microsoft.com/en-us/library/windows/apps/ms741559.aspx)                                            | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**WSAConnectByList**](https://msdn.microsoft.com/en-us/library/windows/apps/ms741554.aspx)                                  | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**WSAConnectByNameA**](https://msdn.microsoft.com/en-us/library/windows/apps/ms741557.aspx)                               | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**WSAConnectByNameW**](https://msdn.microsoft.com/en-us/library/windows/apps/ms741557.aspx)                               | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**WSACreateEvent**](https://msdn.microsoft.com/en-us/library/windows/apps/ms741561.aspx)                                    | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**WSADuplicateSocketA**](https://msdn.microsoft.com/en-us/library/windows/apps/ms741565.aspx)                           | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**WSADuplicateSocketW**](https://msdn.microsoft.com/en-us/library/windows/apps/ms741565.aspx)                           | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**WSAEnumNameSpaceProvidersA**](https://msdn.microsoft.com/en-us/library/windows/apps/ms741570.aspx)             | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**WSAEnumNameSpaceProvidersExA**](https://msdn.microsoft.com/en-us/library/windows/apps/ms741568.aspx)           | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**WSAEnumNameSpaceProvidersExW**](https://msdn.microsoft.com/en-us/library/windows/apps/ms741568.aspx)           | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**WSAEnumNameSpaceProvidersW**](https://msdn.microsoft.com/en-us/library/windows/apps/ms741570.aspx)             | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**WSAEnumNetworkEvents**](https://msdn.microsoft.com/en-us/library/windows/apps/ms741572.aspx)                        | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**WSAEnumProtocolsA**](https://msdn.microsoft.com/en-us/library/windows/apps/ms741574.aspx)                               | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**WSAEnumProtocolsW**](https://msdn.microsoft.com/en-us/library/windows/apps/ms741574.aspx)                               | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**WSAEventSelect**](https://msdn.microsoft.com/en-us/library/windows/apps/ms741576.aspx)                                    | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**WSAGetLastError**](https://msdn.microsoft.com/en-us/library/windows/apps/ms741580.aspx)                                  | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**WSAGetOverlappedResult**](https://msdn.microsoft.com/en-us/library/windows/apps/ms741582.aspx)                    | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**WSAGetServiceClassInfoW**](https://msdn.microsoft.com/en-us/library/windows/apps/ms741592.aspx)                   | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**WSAGetServiceClassNameByClassIdW**](https://msdn.microsoft.com/en-us/library/windows/apps/ms741598.aspx) | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**WSAHtonl**](https://msdn.microsoft.com/en-us/library/windows/apps/ms741604.aspx)                                                | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**WSAHtons**](https://msdn.microsoft.com/en-us/library/windows/apps/ms741609.aspx)                                                | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**WSAIoctl**](https://msdn.microsoft.com/en-us/library/windows/apps/ms741621.aspx)                                                | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**WSAJoinLeaf**](https://msdn.microsoft.com/en-us/library/windows/apps/ms741628.aspx)                                          | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**WSALookupServiceBeginA**](https://msdn.microsoft.com/en-us/library/windows/apps/ms741633.aspx)                     | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**WSALookupServiceBeginW**](https://msdn.microsoft.com/en-us/library/windows/apps/ms741633.aspx)                     | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**WSALookupServiceEnd**](https://msdn.microsoft.com/en-us/library/windows/apps/ms741637.aspx)                          | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**WSALookupServiceNextA**](https://msdn.microsoft.com/en-us/library/windows/apps/ms741641.aspx)                       | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**WSALookupServiceNextW**](https://msdn.microsoft.com/en-us/library/windows/apps/ms741641.aspx)                       | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**WSANSPIoctl**](https://msdn.microsoft.com/en-us/library/windows/apps/ms741658.aspx)                                          | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**WSANtohl**](https://msdn.microsoft.com/en-us/library/windows/apps/ms741660.aspx)                                                | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**WSANtohs**](https://msdn.microsoft.com/en-us/library/windows/apps/ms741663.aspx)                                                | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**WSAPoll**](https://msdn.microsoft.com/en-us/library/windows/apps/ms741669.aspx)                                                    | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**WSAProviderConfigChange**](https://msdn.microsoft.com/en-us/library/windows/apps/ms741677.aspx)                  | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**WSARecv**](https://msdn.microsoft.com/en-us/library/windows/apps/ms741688.aspx)                                                  | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**WSARecvFrom**](https://msdn.microsoft.com/en-us/library/windows/apps/ms741686.aspx)                                          | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**WSAResetEvent**](https://msdn.microsoft.com/en-us/library/windows/apps/ms741690.aspx)                                      | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**WSASend**](https://msdn.microsoft.com/en-us/library/windows/apps/ms742203.aspx)                                                  | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**WSASendMsg**](https://msdn.microsoft.com/en-us/library/windows/apps/ms741692.aspx)                                              | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**WSASendTo**](https://msdn.microsoft.com/en-us/library/windows/apps/ms741693.aspx)                                              | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**WSASetEvent**](https://msdn.microsoft.com/en-us/library/windows/apps/ms742208.aspx)                                          | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**WSASetLastError**](https://msdn.microsoft.com/en-us/library/windows/apps/ms742209.aspx)                                  | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**WSASetServiceA**](https://msdn.microsoft.com/en-us/library/windows/apps/ms742211.aspx)                                     | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**WSASetServiceW**](https://msdn.microsoft.com/en-us/library/windows/apps/ms742211.aspx)                                     | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**WSASocketA**](https://msdn.microsoft.com/en-us/library/windows/apps/ms742212.aspx)                                             | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**WSASocketW**](https://msdn.microsoft.com/en-us/library/windows/apps/ms742212.aspx)                                             | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**WSAStartup**](https://msdn.microsoft.com/en-us/library/windows/apps/ms742213.aspx)                                            | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**WSAStringToAddressA**](https://msdn.microsoft.com/en-us/library/windows/apps/ms742214.aspx)                           | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**WSAStringToAddressW**](https://msdn.microsoft.com/en-us/library/windows/apps/ms742214.aspx)                           | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |
| [**WSAWaitForMultipleEvents**](https://msdn.microsoft.com/en-us/library/windows/apps/ms742219.aspx)                | Introduced into ws2\_32.dll in Windows 10.0.10240.0 |

 

## <span id="_XAUDIO2_9.DLL"></span>APIs from the dll xaudio2\_9.dll


| API                                                                                | Requirements                                           |
|------------------------------------------------------------------------------------|--------------------------------------------------------|
| [**CreateAudioReverb**](https://www.bing.com/search?q=CreateAudioReverb)           | Introduced into xaudio2\_9.dll in Windows 10.0.10240.0 |
| [**CreateAudioVolumeMeter**](https://www.bing.com/search?q=CreateAudioVolumeMeter) | Introduced into xaudio2\_9.dll in Windows 10.0.10240.0 |
| [**CreateFX**](https://msdn.microsoft.com/en-us/library/windows/apps/hh405044.aspx)                                                   | Introduced into xaudio2\_9.dll in Windows 10.0.10240.0 |
| [**X3DAudioCalculate**](https://msdn.microsoft.com/en-us/library/windows/apps/microsoft.directx_sdk.x3daudio.x3daudiocalculate.aspx)                                 | Introduced into xaudio2\_9.dll in Windows 10.0.10240.0 |
| [**X3DAudioInitialize**](https://msdn.microsoft.com/en-us/library/windows/apps/microsoft.directx_sdk.x3daudio.x3daudioinitialize.aspx)                               | Introduced into xaudio2\_9.dll in Windows 10.0.10240.0 |
| [**XAudio2Create**](https://msdn.microsoft.com/en-us/library/windows/apps/microsoft.directx_sdk.xaudio2.xaudio2create.aspx)                                         | Introduced into xaudio2\_9.dll in Windows 10.0.10240.0 |

 

## <span id="_XINPUTUAP.DLL"></span>APIs from the dll xinputuap.dll


| API                                                                   | Requirements                                          |
|-----------------------------------------------------------------------|-------------------------------------------------------|
| [**XInputEnable**](https://msdn.microsoft.com/en-us/library/windows/apps/microsoft.directx_sdk.reference.xinputenable.aspx)                               | Introduced into xinputuap.dll in Windows 10.0.10240.0 |
| [**XInputGetAudioDeviceIds**](https://msdn.microsoft.com/en-us/library/windows/apps/microsoft.directx_sdk.reference.xinputgetaudiodeviceids.aspx)         | Introduced into xinputuap.dll in Windows 10.0.10240.0 |
| [**XInputGetBatteryInformation**](https://msdn.microsoft.com/en-us/library/windows/apps/microsoft.directx_sdk.reference.xinputgetbatteryinformation.aspx) | Introduced into xinputuap.dll in Windows 10.0.10240.0 |
| [**XInputGetCapabilities**](https://msdn.microsoft.com/en-us/library/windows/apps/microsoft.directx_sdk.reference.xinputgetcapabilities.aspx)             | Introduced into xinputuap.dll in Windows 10.0.10240.0 |
| [**XInputGetKeystroke**](https://msdn.microsoft.com/en-us/library/windows/apps/microsoft.directx_sdk.reference.xinputgetkeystroke.aspx)                   | Introduced into xinputuap.dll in Windows 10.0.10240.0 |
| [**XInputGetState**](https://msdn.microsoft.com/en-us/library/windows/apps/microsoft.directx_sdk.reference.xinputgetstate.aspx)                           | Introduced into xinputuap.dll in Windows 10.0.10240.0 |
| [**XInputSetState**](https://msdn.microsoft.com/en-us/library/windows/apps/microsoft.directx_sdk.reference.xinputsetstate.aspx)                           | Introduced into xinputuap.dll in Windows 10.0.10240.0 |

 

## <span id="_XMLLITE.DLL"></span>APIs from the dll xmllite.dll


| API                                                                                                                      | Requirements                                        |
|--------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| [**CreateXmlReader**](https://www.bing.com/search?q=CreateXmlReader)                                                     | Introduced into xmllite.dll in Windows 10.0.10240.0 |
| [**CreateXmlReaderInputWithEncodingCodePage**](https://www.bing.com/search?q=CreateXmlReaderInputWithEncodingCodePage)   | Introduced into xmllite.dll in Windows 10.0.10240.0 |
| [**CreateXmlReaderInputWithEncodingName**](https://www.bing.com/search?q=CreateXmlReaderInputWithEncodingName)           | Introduced into xmllite.dll in Windows 10.0.10240.0 |
| [**CreateXmlWriter**](https://www.bing.com/search?q=CreateXmlWriter)                                                     | Introduced into xmllite.dll in Windows 10.0.10240.0 |
| [**CreateXmlWriterOutputWithEncodingCodePage**](https://www.bing.com/search?q=CreateXmlWriterOutputWithEncodingCodePage) | Introduced into xmllite.dll in Windows 10.0.10240.0 |
| [**CreateXmlWriterOutputWithEncodingName**](https://www.bing.com/search?q=CreateXmlWriterOutputWithEncodingName)         | Introduced into xmllite.dll in Windows 10.0.10240.0 |

 

## <span id="_BCRYPT.DLL"></span>APIs from the dll Bcrypt.dll


| API                                                                                            | Requirements                                       |
|------------------------------------------------------------------------------------------------|----------------------------------------------------|
| [**BCryptCloseAlgorithmProvider**](https://msdn.microsoft.com/en-us/library/windows/apps/aa375377.aspx)                 | Introduced into Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptCreateHash**](https://msdn.microsoft.com/en-us/library/windows/apps/aa375383.aspx)                                         | Introduced into Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptCreateMultiHash**](https://www.bing.com/search?q=BCryptCreateMultiHash)               | Introduced into Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptDecrypt**](https://msdn.microsoft.com/en-us/library/windows/apps/aa375391.aspx)                                               | Introduced into Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptDeriveKey**](https://msdn.microsoft.com/en-us/library/windows/apps/aa375393.aspx)                                                | Introduced into Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptDeriveKeyCapi**](https://msdn.microsoft.com/en-us/library/windows/apps/dd433794.aspx)                                        | Introduced into Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptDeriveKeyPBKDF2**](https://msdn.microsoft.com/en-us/library/windows/apps/dd433795.aspx)                                    | Introduced into Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptDestroyHash**](https://msdn.microsoft.com/en-us/library/windows/apps/aa375399.aspx)                                       | Introduced into Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptDestroyKey**](https://msdn.microsoft.com/en-us/library/windows/apps/aa375404.aspx)                                         | Introduced into Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptDestroySecret**](https://msdn.microsoft.com/en-us/library/windows/apps/aa375407.aspx)                                        | Introduced into Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptDuplicateHash**](https://msdn.microsoft.com/en-us/library/windows/apps/aa375413.aspx)                                   | Introduced into Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptDuplicateKey**](https://msdn.microsoft.com/en-us/library/windows/apps/aa375419.aspx)                                     | Introduced into Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptEncrypt**](https://msdn.microsoft.com/en-us/library/windows/apps/aa375421.aspx)                                               | Introduced into Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptEnumAlgorithms**](https://msdn.microsoft.com/en-us/library/windows/apps/aa375422.aspx)                                 | Introduced into Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptEnumProviders**](https://msdn.microsoft.com/en-us/library/windows/apps/aa375429.aspx)                                   | Introduced into Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptExportKey**](https://msdn.microsoft.com/en-us/library/windows/apps/aa375434.aspx)                                           | Introduced into Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptFinalizeKeyPair**](https://msdn.microsoft.com/en-us/library/windows/apps/aa375439.aspx)                               | Introduced into Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptFinishHash**](https://msdn.microsoft.com/en-us/library/windows/apps/aa375443.aspx)                                         | Introduced into Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptFreeBuffer**](https://msdn.microsoft.com/en-us/library/windows/apps/aa375445.aspx)                                         | Introduced into Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptGenerateKeyPair**](https://msdn.microsoft.com/en-us/library/windows/apps/aa375451.aspx)                               | Introduced into Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptGenerateSymmetricKey**](https://msdn.microsoft.com/en-us/library/windows/apps/aa375453.aspx)                     | Introduced into Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptGenRandom**](https://msdn.microsoft.com/en-us/library/windows/apps/aa375458.aspx)                                           | Introduced into Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptGetProperty**](https://msdn.microsoft.com/en-us/library/windows/apps/aa375464.aspx)                                       | Introduced into Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptHash**](https://msdn.microsoft.com/en-us/library/windows/apps/mt633798.aspx)                                                          | Introduced into Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptHashData**](https://msdn.microsoft.com/en-us/library/windows/apps/aa375468.aspx)                                             | Introduced into Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptImportKey**](https://msdn.microsoft.com/en-us/library/windows/apps/aa375475.aspx)                                           | Introduced into Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptImportKeyPair**](https://msdn.microsoft.com/en-us/library/windows/apps/aa375472.aspx)                                        | Introduced into Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptKeyDerivation**](https://msdn.microsoft.com/en-us/library/windows/apps/hh448506.aspx)                                        | Introduced into Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptOpenAlgorithmProvider**](https://msdn.microsoft.com/en-us/library/windows/apps/aa375479.aspx)                   | Introduced into Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptProcessMultiOperations**](https://www.bing.com/search?q=BCryptProcessMultiOperations) | Introduced into Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptSecretAgreement**](https://msdn.microsoft.com/en-us/library/windows/apps/aa375496.aspx)                                    | Introduced into Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptSetProperty**](https://msdn.microsoft.com/en-us/library/windows/apps/aa375504.aspx)                                       | Introduced into Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptSignHash**](https://msdn.microsoft.com/en-us/library/windows/apps/aa375510.aspx)                                             | Introduced into Bcrypt.dll in Windows 10.0.10586.0 |
| [**BCryptVerifySignature**](https://msdn.microsoft.com/en-us/library/windows/apps/aa375515.aspx)                               | Introduced into Bcrypt.dll in Windows 10.0.10586.0 |

 

## <span id="_ROMETADATA.DLL"></span>APIs from the dll rometadata.dll


| API                                                    | Requirements                                           |
|--------------------------------------------------------|--------------------------------------------------------|
| [**MetaDataGetDispenser**](https://msdn.microsoft.com/en-us/library/windows/apps/br229853.aspx) | Introduced into rometadata.dll in Windows 10.0.10586.0 |

 

## <span id="_api-ms-win-core-featurestaging-l1-1-0.dll"></span><span id="_API-MS-WIN-CORE-FEATURESTAGING-L1-1-0.DLL"></span>APIs from the API Set api-ms-win-core-featurestaging-l1-1-0.dll


| API                                                                                                                      | Requirements                                                                      |
|--------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| [**GetFeatureEnabledState**](https://www.bing.com/search?q=GetFeatureEnabledState)                                       | Introduced into api-ms-win-core-featurestaging-l1-1-0.dll in Windows 10.0.14393.0 |
| [**RecordFeatureError**](https://www.bing.com/search?q=RecordFeatureError)                                               | Introduced into api-ms-win-core-featurestaging-l1-1-0.dll in Windows 10.0.14393.0 |
| [**RecordFeatureUsage**](https://www.bing.com/search?q=RecordFeatureUsage)                                               | Introduced into api-ms-win-core-featurestaging-l1-1-0.dll in Windows 10.0.14393.0 |
| [**SubscribeFeatureStateChangeNotification**](https://www.bing.com/search?q=SubscribeFeatureStateChangeNotification)     | Introduced into api-ms-win-core-featurestaging-l1-1-0.dll in Windows 10.0.14393.0 |
| [**UnsubscribeFeatureStateChangeNotification**](https://www.bing.com/search?q=UnsubscribeFeatureStateChangeNotification) | Introduced into api-ms-win-core-featurestaging-l1-1-0.dll in Windows 10.0.14393.0 |

 

## <span id="_api-ms-win-core-heap-l2-1-0.dll"></span><span id="_API-MS-WIN-CORE-HEAP-L2-1-0.DLL"></span>APIs from the API Set api-ms-win-core-heap-l2-1-0.dll


| API                                   | Requirements                                                            |
|---------------------------------------|-------------------------------------------------------------------------|
| [**GlobalAlloc**](https://msdn.microsoft.com/en-us/library/windows/apps/aa366574.aspx)   | Introduced into api-ms-win-core-heap-l2-1-0.dll in Windows 10.0.14393.0 |
| [**GlobalFree**](https://msdn.microsoft.com/en-us/library/windows/apps/aa366579.aspx)     | Introduced into api-ms-win-core-heap-l2-1-0.dll in Windows 10.0.14393.0 |
| [**LocalAlloc**](https://msdn.microsoft.com/en-us/library/windows/apps/aa366723.aspx)     | Introduced into api-ms-win-core-heap-l2-1-0.dll in Windows 10.0.14393.0 |
| [**LocalFree**](https://msdn.microsoft.com/en-us/library/windows/apps/aa366730.aspx)       | Introduced into api-ms-win-core-heap-l2-1-0.dll in Windows 10.0.14393.0 |
| [**LocalReAlloc**](https://msdn.microsoft.com/en-us/library/windows/apps/aa366742.aspx) | Introduced into api-ms-win-core-heap-l2-1-0.dll in Windows 10.0.14393.0 |

 

## <span id="_api-ms-win-core-heap-obsolete-l1-1-0.dll"></span><span id="_API-MS-WIN-CORE-HEAP-OBSOLETE-L1-1-0.DLL"></span>APIs from the API Set api-ms-win-core-heap-obsolete-l1-1-0.dll


| API                                     | Requirements                                                                     |
|-----------------------------------------|----------------------------------------------------------------------------------|
| [**GlobalReAlloc**](https://msdn.microsoft.com/en-us/library/windows/apps/aa366590.aspx) | Introduced into api-ms-win-core-heap-obsolete-l1-1-0.dll in Windows 10.0.14393.0 |

 

## <span id="_api-ms-win-core-memory-l1-1-4.dll"></span><span id="_API-MS-WIN-CORE-MEMORY-L1-1-4.DLL"></span>APIs from the API Set api-ms-win-core-memory-l1-1-4.dll


| API                                                       | Requirements                                                              |
|-----------------------------------------------------------|---------------------------------------------------------------------------|
| [**OpenFileMappingFromApp**](https://msdn.microsoft.com/en-us/library/windows/apps/mt169844.aspx) | Introduced into api-ms-win-core-memory-l1-1-4.dll in Windows 10.0.14393.0 |
| [**VirtualAllocFromApp**](https://msdn.microsoft.com/en-us/library/windows/apps/mt169845.aspx)       | Introduced into api-ms-win-core-memory-l1-1-4.dll in Windows 10.0.14393.0 |
| [**VirtualProtectFromApp**](https://msdn.microsoft.com/en-us/library/windows/apps/mt169846.aspx)   | Introduced into api-ms-win-core-memory-l1-1-4.dll in Windows 10.0.14393.0 |

 

## <span id="_api-ms-win-core-psapi-l1-1-0.dll"></span><span id="_API-MS-WIN-CORE-PSAPI-L1-1-0.DLL"></span>APIs from the API Set api-ms-win-core-psapi-l1-1-0.dll


| API                                                                                  | Requirements                                                             |
|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| [**K32GetModuleInformation**](https://www.bing.com/search?q=K32GetModuleInformation) | Introduced into api-ms-win-core-psapi-l1-1-0.dll in Windows 10.0.14393.0 |
| [**K32GetProcessMemoryInfo**](https://www.bing.com/search?q=K32GetProcessMemoryInfo) | Introduced into api-ms-win-core-psapi-l1-1-0.dll in Windows 10.0.14393.0 |

 

## <span id="_api-ms-win-core-slapi-l1-1-0.dll"></span><span id="_API-MS-WIN-CORE-SLAPI-L1-1-0.DLL"></span>APIs from the API Set api-ms-win-core-slapi-l1-1-0.dll


| API                                                                                          | Requirements                                                             |
|----------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| [**SLQueryLicenseValueFromApp**](https://msdn.microsoft.com/en-us/library/windows/apps/mt403327.aspx)                        | Introduced into api-ms-win-core-slapi-l1-1-0.dll in Windows 10.0.14393.0 |
| [**SLQueryLicenseValueFromApp2**](https://www.bing.com/search?q=SLQueryLicenseValueFromApp2) | Introduced into api-ms-win-core-slapi-l1-1-0.dll in Windows 10.0.14393.0 |

 

## <span id="_api-ms-win-gaming-tcui-l1-1-2.dll"></span><span id="_API-MS-WIN-GAMING-TCUI-L1-1-2.DLL"></span>APIs from the API Set api-ms-win-gaming-tcui-l1-1-2.dll


| API                                                                                                              | Requirements                                                              |
|------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| [**CheckGamingPrivilegeSilently**](https://www.bing.com/search?q=CheckGamingPrivilegeSilently)                   | Introduced into api-ms-win-gaming-tcui-l1-1-2.dll in Windows 10.0.14393.0 |
| [**CheckGamingPrivilegeSilentlyForUser**](https://www.bing.com/search?q=CheckGamingPrivilegeSilentlyForUser)     | Introduced into api-ms-win-gaming-tcui-l1-1-2.dll in Windows 10.0.14393.0 |
| [**CheckGamingPrivilegeWithUI**](https://www.bing.com/search?q=CheckGamingPrivilegeWithUI)                       | Introduced into api-ms-win-gaming-tcui-l1-1-2.dll in Windows 10.0.14393.0 |
| [**CheckGamingPrivilegeWithUIForUser**](https://www.bing.com/search?q=CheckGamingPrivilegeWithUIForUser)         | Introduced into api-ms-win-gaming-tcui-l1-1-2.dll in Windows 10.0.14393.0 |
| [**ProcessPendingGameUI**](https://www.bing.com/search?q=ProcessPendingGameUI)                                   | Introduced into api-ms-win-gaming-tcui-l1-1-2.dll in Windows 10.0.14393.0 |
| [**ShowChangeFriendRelationshipUI**](https://www.bing.com/search?q=ShowChangeFriendRelationshipUI)               | Introduced into api-ms-win-gaming-tcui-l1-1-2.dll in Windows 10.0.14393.0 |
| [**ShowChangeFriendRelationshipUIForUser**](https://www.bing.com/search?q=ShowChangeFriendRelationshipUIForUser) | Introduced into api-ms-win-gaming-tcui-l1-1-2.dll in Windows 10.0.14393.0 |
| [**ShowGameInviteUI**](https://www.bing.com/search?q=ShowGameInviteUI)                                           | Introduced into api-ms-win-gaming-tcui-l1-1-2.dll in Windows 10.0.14393.0 |
| [**ShowGameInviteUIForUser**](https://www.bing.com/search?q=ShowGameInviteUIForUser)                             | Introduced into api-ms-win-gaming-tcui-l1-1-2.dll in Windows 10.0.14393.0 |
| [**ShowPlayerPickerUI**](https://www.bing.com/search?q=ShowPlayerPickerUI)                                       | Introduced into api-ms-win-gaming-tcui-l1-1-2.dll in Windows 10.0.14393.0 |
| [**ShowPlayerPickerUIForUser**](https://www.bing.com/search?q=ShowPlayerPickerUIForUser)                         | Introduced into api-ms-win-gaming-tcui-l1-1-2.dll in Windows 10.0.14393.0 |
| [**ShowProfileCardUI**](https://www.bing.com/search?q=ShowProfileCardUI)                                         | Introduced into api-ms-win-gaming-tcui-l1-1-2.dll in Windows 10.0.14393.0 |
| [**ShowProfileCardUIForUser**](https://www.bing.com/search?q=ShowProfileCardUIForUser)                           | Introduced into api-ms-win-gaming-tcui-l1-1-2.dll in Windows 10.0.14393.0 |
| [**ShowTitleAchievementsUI**](https://www.bing.com/search?q=ShowTitleAchievementsUI)                             | Introduced into api-ms-win-gaming-tcui-l1-1-2.dll in Windows 10.0.14393.0 |
| [**ShowTitleAchievementsUIForUser**](https://www.bing.com/search?q=ShowTitleAchievementsUIForUser)               | Introduced into api-ms-win-gaming-tcui-l1-1-2.dll in Windows 10.0.14393.0 |
| [**TryCancelPendingGameUI**](https://www.bing.com/search?q=TryCancelPendingGameUI)                               | Introduced into api-ms-win-gaming-tcui-l1-1-2.dll in Windows 10.0.14393.0 |

 

## <span id="_api-ms-win-security-base-l1-2-1.dll"></span><span id="_API-MS-WIN-SECURITY-BASE-L1-2-1.DLL"></span>APIs from the API Set api-ms-win-security-base-l1-2-1.dll


| API                                    | Requirements                                                                |
|----------------------------------------|-----------------------------------------------------------------------------|
| [**CveEventWrite**](https://msdn.microsoft.com/en-us/library/windows/apps/mt759300.aspx) | Introduced into api-ms-win-security-base-l1-2-1.dll in Windows 10.0.14393.0 |

 

## <span id="_INKOBJCORE.DLL"></span>APIs from the dll inkobjcore.dll


| API                                                                                  | Requirements                                           |
|--------------------------------------------------------------------------------------|--------------------------------------------------------|
| [**AddStroke**](https://www.bing.com/search?q=AddStroke)                             | Introduced into inkobjcore.dll in Windows 10.0.14393.0 |
| [**AddWordsToWordList**](https://www.bing.com/search?q=AddWordsToWordList)           | Introduced into inkobjcore.dll in Windows 10.0.14393.0 |
| [**AdviseInkChange**](https://www.bing.com/search?q=AdviseInkChange)                 | Introduced into inkobjcore.dll in Windows 10.0.14393.0 |
| [**CreateContext**](https://www.bing.com/search?q=CreateContext)                     | Introduced into inkobjcore.dll in Windows 10.0.14393.0 |
| [**CreateRecognizer**](https://www.bing.com/search?q=CreateRecognizer)               | Introduced into inkobjcore.dll in Windows 10.0.14393.0 |
| [**DestroyContext**](https://www.bing.com/search?q=DestroyContext)                   | Introduced into inkobjcore.dll in Windows 10.0.14393.0 |
| [**DestroyRecognizer**](https://www.bing.com/search?q=DestroyRecognizer)             | Introduced into inkobjcore.dll in Windows 10.0.14393.0 |
| [**DestroyWordList**](https://www.bing.com/search?q=DestroyWordList)                 | Introduced into inkobjcore.dll in Windows 10.0.14393.0 |
| [**EndInkInput**](https://www.bing.com/search?q=EndInkInput)                         | Introduced into inkobjcore.dll in Windows 10.0.14393.0 |
| [**GetAllRecognizers**](https://www.bing.com/search?q=GetAllRecognizers)             | Introduced into inkobjcore.dll in Windows 10.0.14393.0 |
| [**GetBestResultString**](https://www.bing.com/search?q=GetBestResultString)         | Introduced into inkobjcore.dll in Windows 10.0.14393.0 |
| [**GetLatticePtr**](https://www.bing.com/search?q=GetLatticePtr)                     | Introduced into inkobjcore.dll in Windows 10.0.14393.0 |
| [**GetLeftSeparator**](https://www.bing.com/search?q=GetLeftSeparator)               | Introduced into inkobjcore.dll in Windows 10.0.14393.0 |
| [**GetRecoAttributes**](https://www.bing.com/search?q=GetRecoAttributes)             | Introduced into inkobjcore.dll in Windows 10.0.14393.0 |
| [**GetResultPropertyList**](https://www.bing.com/search?q=GetResultPropertyList)     | Introduced into inkobjcore.dll in Windows 10.0.14393.0 |
| [**GetRightSeparator**](https://www.bing.com/search?q=GetRightSeparator)             | Introduced into inkobjcore.dll in Windows 10.0.14393.0 |
| [**GetUnicodeRanges**](https://www.bing.com/search?q=GetUnicodeRanges)               | Introduced into inkobjcore.dll in Windows 10.0.14393.0 |
| [**IsStringSupported**](https://www.bing.com/search?q=IsStringSupported)             | Introduced into inkobjcore.dll in Windows 10.0.14393.0 |
| [**LoadCachedAttributes**](https://www.bing.com/search?q=LoadCachedAttributes)       | Introduced into inkobjcore.dll in Windows 10.0.14393.0 |
| [**MakeWordList**](https://www.bing.com/search?q=MakeWordList)                       | Introduced into inkobjcore.dll in Windows 10.0.14393.0 |
| [**Process**](https://www.bing.com/search?q=Process)                                 | Introduced into inkobjcore.dll in Windows 10.0.14393.0 |
| [**SetEnabledUnicodeRanges**](https://www.bing.com/search?q=SetEnabledUnicodeRanges) | Introduced into inkobjcore.dll in Windows 10.0.14393.0 |
| [**SetFactoid**](https://www.bing.com/search?q=SetFactoid)                           | Introduced into inkobjcore.dll in Windows 10.0.14393.0 |
| [**SetFlags**](https://www.bing.com/search?q=SetFlags)                               | Introduced into inkobjcore.dll in Windows 10.0.14393.0 |
| [**SetGuide**](https://www.bing.com/search?q=SetGuide)                               | Introduced into inkobjcore.dll in Windows 10.0.14393.0 |
| [**SetTextContext**](https://www.bing.com/search?q=SetTextContext)                   | Introduced into inkobjcore.dll in Windows 10.0.14393.0 |
| [**SetWordList**](https://www.bing.com/search?q=SetWordList)                         | Introduced into inkobjcore.dll in Windows 10.0.14393.0 |

 

## <span id="_IPHLPAPI.DLL"></span>APIs from the dll iphlpapi.dll


| API                                                            | Requirements                                         |
|----------------------------------------------------------------|------------------------------------------------------|
| [**FreeMibTable**](https://msdn.microsoft.com/en-us/library/windows/apps/aa814408.aspx)                         | Introduced into iphlpapi.dll in Windows 10.0.14393.0 |
| [**GetAdaptersAddresses**](https://msdn.microsoft.com/en-us/library/windows/apps/aa365915.aspx)         | Introduced into iphlpapi.dll in Windows 10.0.14393.0 |
| [**GetBestRoute2**](https://msdn.microsoft.com/en-us/library/windows/apps/aa814411.aspx)                       | Introduced into iphlpapi.dll in Windows 10.0.14393.0 |
| [**GetUnicastIpAddressTable**](https://msdn.microsoft.com/en-us/library/windows/apps/aa814428.aspx) | Introduced into iphlpapi.dll in Windows 10.0.14393.0 |

 

 

 



