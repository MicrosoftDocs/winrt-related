---
author: msatranjr
description: This topic lists the Win32 APIs that are part of the Universal Windows Platform (UWP) and that are implemented by all Windows 10 devices.
title: APIs present on all Windows 10 devices (grouped by module)
ms.author: misatran
ms.topic: article
ms.prod: windows
ms.technology: uwp
keywords: windows 10, uwp, win32, COM
ms.date: 07/25/2017
ms.assetid: 9763fa67-0f32-4128-b901-013b1d7ea73c
---

# APIs present on all Windows 10 devices
This topic lists the Win32 APIs that are part of the Universal Windows Platform (UWP) and that are implemented by all Windows 10 devices. For convenience, an umbrella library named WindowsApp.lib is provided in the Microsoft Windows Software Development Kit (SDK), which provides the exports for this set of Win32 APIs. Link your app with WindowsApp.lib (and no other libraries) to access these APIs.

This topic lists all the APIs in WindowsApp.lib, grouped by module (where the module is either an [API set](https://msdn.microsoft.com/en-us/library/windows/apps/mt683763.aspx#api_sets) or a dll). Linking to WindowsApp.lib will add to your app dependencies on dlls that are present on all Windows 10 devices. For delay load, use the module name. Note that an umbrella lib can contain some, but not necessarily all, APIs from a given module.


## APIs from api-ms-win-core-com-l1-1-1.dll

| API | Requirements |
| -----| --------------|
| [CLSIDFromString](https://msdn.microsoft.com/en-us/library/windows/desktop/ms680589.aspx) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. |
| [CoCreateFreeThreadedMarshaler](https://msdn.microsoft.com/en-us/library/windows/desktop/ms694500.aspx) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. |
| [CoCreateGuid](https://msdn.microsoft.com/en-us/library/windows/desktop/ms688568.aspx) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. |
| [CoCreateInstanceFromApp](https://msdn.microsoft.com/en-us/library/windows/desktop/hh404137.aspx) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. |
| [CoDisconnectObject](https://msdn.microsoft.com/en-us/library/windows/desktop/ms680756.aspx) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. |
| [CoFreeUnusedLibraries](https://msdn.microsoft.com/en-us/library/windows/desktop/ms679712.aspx) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. |
| [CoFreeUnusedLibrariesEx](https://msdn.microsoft.com/en-us/library/windows/desktop/ms678413.aspx) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. |
| [CoGetApartmentType](https://msdn.microsoft.com/en-us/library/windows/desktop/dd542641.aspx) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. |
| [CoGetContextToken](https://msdn.microsoft.com/en-us/library/windows/desktop/ms679665.aspx) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. |
| [CoGetCurrentLogicalThreadId](https://msdn.microsoft.com/en-us/library/windows/desktop/ms693805.aspx) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. |
| [CoGetInterfaceAndReleaseStream](https://msdn.microsoft.com/en-us/library/windows/desktop/ms691421.aspx) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. |
| [CoGetMarshalSizeMax](https://msdn.microsoft.com/en-us/library/windows/desktop/ms692640.aspx) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. |
| [CoGetObjectContext](https://msdn.microsoft.com/en-us/library/windows/desktop/ms690084.aspx) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. |
| [CoGetStandardMarshal](https://msdn.microsoft.com/en-us/library/windows/desktop/ms678527.aspx) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. |
| [CoInitializeEx](https://msdn.microsoft.com/en-us/library/windows/desktop/ms695279.aspx) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. |
| [CoInitializeSecurity](https://msdn.microsoft.com/en-us/library/windows/desktop/ms693736.aspx) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. |
| [CoMarshalInterface](https://msdn.microsoft.com/en-us/library/windows/desktop/ms678428.aspx) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. |
| [CoMarshalInterThreadInterfaceInStream](https://msdn.microsoft.com/en-us/library/windows/desktop/ms693316.aspx) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. |
| [CoRegisterClassObject](https://msdn.microsoft.com/en-us/library/windows/desktop/ms693407.aspx) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. |
| [CoReleaseMarshalData](https://msdn.microsoft.com/en-us/library/windows/desktop/ms690490.aspx) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. |
| [CoResumeClassObjects](https://msdn.microsoft.com/en-us/library/windows/desktop/ms692686.aspx) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. |
| [CoRevokeClassObject](https://msdn.microsoft.com/en-us/library/windows/desktop/ms688650.aspx) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. |
| [CoSuspendClassObjects](https://msdn.microsoft.com/en-us/library/windows/desktop/ms691208.aspx) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. |
| [CoSwitchCallContext](https://msdn.microsoft.com/en-us/library/windows/desktop/ms679683.aspx) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. |
| [CoTaskMemAlloc](https://msdn.microsoft.com/en-us/library/windows/desktop/ms692727.aspx) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. |
| [CoTaskMemFree](https://msdn.microsoft.com/en-us/library/windows/desktop/ms680722.aspx) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. |
| [CoTaskMemRealloc](https://msdn.microsoft.com/en-us/library/windows/desktop/ms687280.aspx) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. |
| [CoUninitialize](https://msdn.microsoft.com/en-us/library/windows/desktop/ms688715.aspx) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. |
| [CoUnmarshalInterface](https://msdn.microsoft.com/en-us/library/windows/desktop/ms693382.aspx) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. |
| [CreateStreamOnHGlobal](https://msdn.microsoft.com/en-us/library/windows/desktop/aa378980.aspx) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. |
| [FreePropVariantArray](https://msdn.microsoft.com/en-us/library/windows/desktop/bb762285.aspx) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. |
| [GetHGlobalFromStream](https://msdn.microsoft.com/en-us/library/windows/desktop/aa379145.aspx) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. |
| [IIDFromString](https://msdn.microsoft.com/en-us/library/windows/desktop/ms687262.aspx) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. |
| [PropVariantClear](https://msdn.microsoft.com/en-us/library/windows/desktop/bb776515.aspx) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. |
| [PropVariantCopy](https://msdn.microsoft.com/en-us/library/windows/desktop/bb776518.aspx) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. |
| [RoGetAgileReference](https://msdn.microsoft.com/en-us/library/windows/desktop/dn269839.aspx) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. |
| [StringFromCLSID](https://msdn.microsoft.com/en-us/library/windows/desktop/ms683917.aspx) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. |
| [StringFromGUID2](https://msdn.microsoft.com/en-us/library/windows/desktop/ms683893.aspx) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. |
| [StringFromIID](https://msdn.microsoft.com/en-us/library/windows/desktop/ms688692.aspx) | Introduced into api-ms-win-core-com-l1-1-1.dll in 10.0.10240. |


## APIs from api-ms-win-core-com-l2-1-1.dll

| API | Requirements |
| -----| --------------|
| [CreateILockBytesOnHGlobal](https://msdn.microsoft.com/en-us/library/windows/desktop/aa378977.aspx) | Introduced into api-ms-win-core-com-l2-1-1.dll in 10.0.10240. |
| [FmtIdToPropStgName](https://msdn.microsoft.com/en-us/library/windows/desktop/aa379108.aspx) | Introduced into api-ms-win-core-com-l2-1-1.dll in 10.0.10240. |
| [GetConvertStg](https://msdn.microsoft.com/en-us/library/windows/desktop/aa379138.aspx) | Introduced into api-ms-win-core-com-l2-1-1.dll in 10.0.10240. |
| [GetHGlobalFromILockBytes](https://msdn.microsoft.com/en-us/library/windows/desktop/aa379140.aspx) | Introduced into api-ms-win-core-com-l2-1-1.dll in 10.0.10240. |
| [PropStgNameToFmtId](https://msdn.microsoft.com/en-us/library/windows/desktop/aa380071.aspx) | Introduced into api-ms-win-core-com-l2-1-1.dll in 10.0.10240. |
| [ReadClassStg](https://msdn.microsoft.com/en-us/library/windows/desktop/aa380302.aspx) | Introduced into api-ms-win-core-com-l2-1-1.dll in 10.0.10240. |
| [ReadClassStm](https://msdn.microsoft.com/en-us/library/windows/desktop/aa380303.aspx) | Introduced into api-ms-win-core-com-l2-1-1.dll in 10.0.10240. |
| [StgCreateDocfile](https://msdn.microsoft.com/en-us/library/windows/desktop/aa380323.aspx) | Introduced into api-ms-win-core-com-l2-1-1.dll in 10.0.10240. |
| [StgCreateDocfileOnILockBytes](https://msdn.microsoft.com/en-us/library/windows/desktop/aa380324.aspx) | Introduced into api-ms-win-core-com-l2-1-1.dll in 10.0.10240. |
| [StgCreatePropSetStg](https://msdn.microsoft.com/en-us/library/windows/desktop/aa380325.aspx) | Introduced into api-ms-win-core-com-l2-1-1.dll in 10.0.10240. |
| [StgCreatePropStg](https://msdn.microsoft.com/en-us/library/windows/desktop/aa380327.aspx) | Introduced into api-ms-win-core-com-l2-1-1.dll in 10.0.10240. |
| [StgCreateStorageEx](https://msdn.microsoft.com/en-us/library/windows/desktop/aa380328.aspx) | Introduced into api-ms-win-core-com-l2-1-1.dll in 10.0.10240. |
| [StgIsStorageFile](https://msdn.microsoft.com/en-us/library/windows/desktop/aa380334.aspx) | Introduced into api-ms-win-core-com-l2-1-1.dll in 10.0.10240. |
| [StgIsStorageILockBytes](https://msdn.microsoft.com/en-us/library/windows/desktop/aa380335.aspx) | Introduced into api-ms-win-core-com-l2-1-1.dll in 10.0.10240. |
| [StgOpenPropStg](https://msdn.microsoft.com/en-us/library/windows/desktop/aa380340.aspx) | Introduced into api-ms-win-core-com-l2-1-1.dll in 10.0.10240. |
| [StgOpenStorage](https://msdn.microsoft.com/en-us/library/windows/desktop/aa380341.aspx) | Introduced into api-ms-win-core-com-l2-1-1.dll in 10.0.10240. |
| [StgOpenStorageEx](https://msdn.microsoft.com/en-us/library/windows/desktop/aa380342.aspx) | Introduced into api-ms-win-core-com-l2-1-1.dll in 10.0.10240. |
| [StgOpenStorageOnILockBytes](https://msdn.microsoft.com/en-us/library/windows/desktop/aa380343.aspx) | Introduced into api-ms-win-core-com-l2-1-1.dll in 10.0.10240. |
| [StgSetTimes](https://msdn.microsoft.com/en-us/library/windows/desktop/aa380347.aspx) | Introduced into api-ms-win-core-com-l2-1-1.dll in 10.0.10240. |
| [WriteClassStg](https://msdn.microsoft.com/en-us/library/windows/desktop/aa380384.aspx) | Introduced into api-ms-win-core-com-l2-1-1.dll in 10.0.10240. |
| [WriteClassStm](https://msdn.microsoft.com/en-us/library/windows/desktop/aa380385.aspx) | Introduced into api-ms-win-core-com-l2-1-1.dll in 10.0.10240. |


## APIs from api-ms-win-core-com-midlproxystub-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [CStdAsyncStubBuffer_AddRef](https://msdn.microsoft.com/en-us/library/windows/desktop/mt243874.aspx) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [CStdAsyncStubBuffer_Connect](https://msdn.microsoft.com/en-us/library/windows/desktop/mt243875.aspx) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [CStdAsyncStubBuffer_Disconnect](https://msdn.microsoft.com/en-us/library/windows/desktop/mt243876.aspx) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [CStdAsyncStubBuffer_Invoke](https://msdn.microsoft.com/en-us/library/windows/desktop/mt243877.aspx) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [CStdAsyncStubBuffer_QueryInterface](https://msdn.microsoft.com/en-us/library/windows/desktop/mt243878.aspx) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [CStdAsyncStubBuffer_Release](https://msdn.microsoft.com/en-us/library/windows/desktop/mt243879.aspx) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [CStdAsyncStubBuffer2_Connect](https://msdn.microsoft.com/en-us/library/windows/desktop/mt243871.aspx) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [CStdAsyncStubBuffer2_Disconnect](https://msdn.microsoft.com/en-us/library/windows/desktop/mt243872.aspx) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [CStdAsyncStubBuffer2_Release](https://msdn.microsoft.com/en-us/library/windows/desktop/mt243873.aspx) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [CStdStubBuffer2_Connect](https://msdn.microsoft.com/en-us/library/windows/desktop/mt243880.aspx) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [CStdStubBuffer2_CountRefs](https://msdn.microsoft.com/en-us/library/windows/desktop/mt243881.aspx) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [CStdStubBuffer2_Disconnect](https://msdn.microsoft.com/en-us/library/windows/desktop/mt243882.aspx) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |
| [CStdStubBuffer2_QueryInterface](https://msdn.microsoft.com/en-us/library/windows/desktop/mt243883.aspx) | Introduced into api-ms-win-core-com-midlproxystub-l1-1-0.dll in 10.0.10240. |


## APIs from api-ms-win-core-datetime-l1-1-1.dll

| API | Requirements |
| -----| --------------|
| [GetDateFormatEx](https://msdn.microsoft.com/en-us/library/windows/desktop/dd318088.aspx) | Introduced into api-ms-win-core-datetime-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-datetime-l1-1-2.dll in 10.0.10586. Moved into api-ms-win-core-datetime-l1-1-1.dll in 10.0.14393. |
| [GetTimeFormatEx](https://msdn.microsoft.com/en-us/library/windows/desktop/dd318131.aspx) | Introduced into api-ms-win-core-datetime-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-datetime-l1-1-2.dll in 10.0.10586. Moved into api-ms-win-core-datetime-l1-1-1.dll in 10.0.14393. |


## APIs from api-ms-win-core-datetime-l1-1-2.dll

| API | Requirements |
| -----| --------------|
| [GetDurationFormatEx](https://msdn.microsoft.com/en-us/library/windows/desktop/dd318092.aspx) | Introduced into api-ms-win-core-datetime-l1-1-2.dll in 10.0.10240. |


## APIs from api-ms-win-core-debug-l1-1-1.dll

| API | Requirements |
| -----| --------------|
| [IsDebuggerPresent](https://msdn.microsoft.com/en-us/library/windows/desktop/ms680345.aspx) | Introduced into api-ms-win-core-debug-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-debug-l1-1-2.dll in 10.0.10586. Moved into api-ms-win-core-debug-l1-1-1.dll in 10.0.14393. |
| [OutputDebugStringA](https://msdn.microsoft.com/en-us/library/windows/desktop/aa363362.aspx) | Introduced into api-ms-win-core-debug-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-debug-l1-1-2.dll in 10.0.10586. Moved into api-ms-win-core-debug-l1-1-1.dll in 10.0.14393. |
| [OutputDebugStringW](https://msdn.microsoft.com/en-us/library/windows/desktop/aa363362.aspx) | Introduced into api-ms-win-core-debug-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-debug-l1-1-2.dll in 10.0.10586. Moved into api-ms-win-core-debug-l1-1-1.dll in 10.0.14393. |


## APIs from api-ms-win-core-delayload-l1-1-1.dll

| API | Requirements |
| -----| --------------|
| [DelayLoadFailureHook](https://msdn.microsoft.com/en-us/library/windows/desktop/bb432244.aspx) | Introduced into api-ms-win-core-delayload-l1-1-1.dll in 10.0.10240. |
| [ResolveDelayLoadedAPI](https://msdn.microsoft.com/en-us/library/windows/desktop/hh829881.aspx) | Introduced into api-ms-win-core-delayload-l1-1-1.dll in 10.0.10240. |
| [ResolveDelayLoadsFromDll](https://msdn.microsoft.com/en-us/library/windows/desktop/hh829882.aspx) | Introduced into api-ms-win-core-delayload-l1-1-1.dll in 10.0.10240. |


## APIs from api-ms-win-core-errorhandling-l1-1-1.dll

| API | Requirements |
| -----| --------------|
| [GetLastError](https://msdn.microsoft.com/en-us/library/windows/desktop/ms679360.aspx) | Introduced into api-ms-win-core-errorhandling-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-errorhandling-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-errorhandling-l1-1-1.dll in 10.0.14393. |
| [RaiseException](https://msdn.microsoft.com/en-us/library/windows/desktop/ms680552.aspx) | Introduced into api-ms-win-core-errorhandling-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-errorhandling-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-errorhandling-l1-1-1.dll in 10.0.14393. |
| [SetLastError](https://msdn.microsoft.com/en-us/library/windows/desktop/ms680627.aspx) | Introduced into api-ms-win-core-errorhandling-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-errorhandling-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-errorhandling-l1-1-1.dll in 10.0.14393. |


## APIs from api-ms-win-core-errorhandling-l1-1-3.dll

| API | Requirements |
| -----| --------------|
| [RaiseFailFastException](https://msdn.microsoft.com/en-us/library/windows/desktop/dd941688.aspx) | Introduced into api-ms-win-core-errorhandling-l1-1-3.dll in 10.0.10240. |
| [SetUnhandledExceptionFilter](https://msdn.microsoft.com/en-us/library/windows/desktop/ms680634.aspx) | Introduced into api-ms-win-core-errorhandling-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-errorhandling-l1-1-1.dll in 10.0.14393. |


## APIs from api-ms-win-core-fibers-l1-1-1.dll

| API | Requirements |
| -----| --------------|
| [FlsAlloc](https://msdn.microsoft.com/en-us/library/windows/desktop/ms682664.aspx) | Introduced into api-ms-win-core-fibers-l1-1-1.dll in 10.0.10240. |
| [FlsFree](https://msdn.microsoft.com/en-us/library/windows/desktop/ms682667.aspx) | Introduced into api-ms-win-core-fibers-l1-1-1.dll in 10.0.10240. |
| [FlsGetValue](https://msdn.microsoft.com/en-us/library/windows/desktop/ms683141.aspx) | Introduced into api-ms-win-core-fibers-l1-1-1.dll in 10.0.10240. |
| [FlsSetValue](https://msdn.microsoft.com/en-us/library/windows/desktop/ms683146.aspx) | Introduced into api-ms-win-core-fibers-l1-1-1.dll in 10.0.10240. |
| [IsThreadAFiber](https://msdn.microsoft.com/en-us/library/windows/desktop/ms684131.aspx) | Introduced into api-ms-win-core-fibers-l1-1-1.dll in 10.0.10240. |


## APIs from api-ms-win-core-fibers-l2-1-1.dll

| API | Requirements |
| -----| --------------|
| CalloutOnFiberStack | Introduced into api-ms-win-core-fibers-l2-1-1.dll in 10.0.10240. Removed in 10.0.10586. |
| [ConvertFiberToThread](https://msdn.microsoft.com/en-us/library/windows/desktop/ms682112.aspx) | Introduced into api-ms-win-core-fibers-l2-1-1.dll in 10.0.10240. |
| [ConvertThreadToFiberEx](https://msdn.microsoft.com/en-us/library/windows/desktop/ms682117.aspx) | Introduced into api-ms-win-core-fibers-l2-1-1.dll in 10.0.10240. |
| [CreateFiberEx](https://msdn.microsoft.com/en-us/library/windows/desktop/ms682406.aspx) | Introduced into api-ms-win-core-fibers-l2-1-1.dll in 10.0.10240. |
| [DeleteFiber](https://msdn.microsoft.com/en-us/library/windows/desktop/ms682556.aspx) | Introduced into api-ms-win-core-fibers-l2-1-1.dll in 10.0.10240. |
| [SwitchToFiber](https://msdn.microsoft.com/en-us/library/windows/desktop/ms686350.aspx) | Introduced into api-ms-win-core-fibers-l2-1-1.dll in 10.0.10240. |


## APIs from api-ms-win-core-file-ansi-l2-1-0.dll

| API | Requirements |
| -----| --------------|
| [ReplaceFileA](https://msdn.microsoft.com/en-us/library/windows/desktop/aa365512.aspx) | Introduced into api-ms-win-core-file-ansi-l2-1-0.dll in 10.0.10240. |


## APIs from api-ms-win-core-file-l1-2-1.dll

| API | Requirements |
| -----| --------------|
| [CreateDirectoryA](https://msdn.microsoft.com/en-us/library/windows/desktop/aa363855.aspx) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. |
| [CreateDirectoryW](https://msdn.microsoft.com/en-us/library/windows/desktop/aa363855.aspx) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. |
| [CreateFile2](https://msdn.microsoft.com/en-us/library/windows/desktop/hh449422.aspx) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. |
| [DeleteFileA](https://msdn.microsoft.com/en-us/library/windows/desktop/aa363915.aspx) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. |
| [DeleteFileW](https://msdn.microsoft.com/en-us/library/windows/desktop/aa363915.aspx) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. |
| [FindClose](https://msdn.microsoft.com/en-us/library/windows/desktop/aa364413.aspx) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. |
| [FindFirstFileExA](https://msdn.microsoft.com/en-us/library/windows/desktop/aa364419.aspx) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. |
| [FindFirstFileExW](https://msdn.microsoft.com/en-us/library/windows/desktop/aa364419.aspx) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. |
| [FindNextFileA](https://msdn.microsoft.com/en-us/library/windows/desktop/aa364428.aspx) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. |
| [FindNextFileW](https://msdn.microsoft.com/en-us/library/windows/desktop/aa364428.aspx) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. |
| [FlushFileBuffers](https://msdn.microsoft.com/en-us/library/windows/desktop/aa364439.aspx) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. |
| [GetDiskFreeSpaceExA](https://msdn.microsoft.com/en-us/library/windows/desktop/aa364937.aspx) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. |
| [GetDiskFreeSpaceExW](https://msdn.microsoft.com/en-us/library/windows/desktop/aa364937.aspx) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. |
| [GetFileAttributesExA](https://msdn.microsoft.com/en-us/library/windows/desktop/aa364946.aspx) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. |
| [GetFileAttributesExW](https://msdn.microsoft.com/en-us/library/windows/desktop/aa364946.aspx) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. |
| [GetFileSizeEx](https://msdn.microsoft.com/en-us/library/windows/desktop/aa364957.aspx) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. |
| [GetFileTime](https://msdn.microsoft.com/en-us/library/windows/desktop/ms724320.aspx) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. |
| [GetFileType](https://msdn.microsoft.com/en-us/library/windows/desktop/aa364960.aspx) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. |
| [GetFullPathNameW](https://msdn.microsoft.com/en-us/library/windows/desktop/aa364963.aspx) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. |
| [GetLongPathNameW](https://msdn.microsoft.com/en-us/library/windows/desktop/aa364980.aspx) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. |
| [GetTempFileNameW](https://msdn.microsoft.com/en-us/library/windows/desktop/aa364991.aspx) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. |
| [GetTempPathW](https://msdn.microsoft.com/en-us/library/windows/desktop/aa364992.aspx) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. |
| [LockFileEx](https://msdn.microsoft.com/en-us/library/windows/desktop/aa365203.aspx) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. |
| [ReadFile](https://msdn.microsoft.com/en-us/library/windows/desktop/aa365467.aspx) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. |
| [RemoveDirectoryA](https://msdn.microsoft.com/en-us/library/windows/desktop/aa365488.aspx) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. |
| [RemoveDirectoryW](https://msdn.microsoft.com/en-us/library/windows/desktop/aa365488.aspx) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. |
| [SetEndOfFile](https://msdn.microsoft.com/en-us/library/windows/desktop/aa365531.aspx) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. |
| [SetFileAttributesA](https://msdn.microsoft.com/en-us/library/windows/desktop/aa365535.aspx) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. |
| [SetFileAttributesW](https://msdn.microsoft.com/en-us/library/windows/desktop/aa365535.aspx) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. |
| [SetFileInformationByHandle](https://msdn.microsoft.com/en-us/library/windows/desktop/aa365539.aspx) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. |
| [SetFilePointerEx](https://msdn.microsoft.com/en-us/library/windows/desktop/aa365542.aspx) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. |
| [SetFileTime](https://msdn.microsoft.com/en-us/library/windows/desktop/ms724933.aspx) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. |
| [UnlockFileEx](https://msdn.microsoft.com/en-us/library/windows/desktop/aa365716.aspx) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. |
| [WriteFile](https://msdn.microsoft.com/en-us/library/windows/desktop/aa365747.aspx) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. |
| [FileTimeToLocalFileTime](https://msdn.microsoft.com/en-us/library/windows/desktop/ms724277.aspx) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. |
| [FindFirstFileA](https://msdn.microsoft.com/en-us/library/windows/desktop/aa364418.aspx) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. |
| [FindFirstFileW](https://msdn.microsoft.com/en-us/library/windows/desktop/aa364418.aspx) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. |
| [GetDiskFreeSpaceA](https://msdn.microsoft.com/en-us/library/windows/desktop/aa364935.aspx) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. |
| [GetDiskFreeSpaceW](https://msdn.microsoft.com/en-us/library/windows/desktop/aa364935.aspx) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. |
| [GetFileAttributesA](https://msdn.microsoft.com/en-us/library/windows/desktop/aa364944.aspx) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. |
| [GetFileAttributesW](https://msdn.microsoft.com/en-us/library/windows/desktop/aa364944.aspx) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. |
| [GetFinalPathNameByHandleA](https://msdn.microsoft.com/en-us/library/windows/desktop/aa364962.aspx) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. |
| [GetFinalPathNameByHandleW](https://msdn.microsoft.com/en-us/library/windows/desktop/aa364962.aspx) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. |
| [LocalFileTimeToFileTime](https://msdn.microsoft.com/en-us/library/windows/desktop/ms724490.aspx) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. |
| [ReadFileEx](https://msdn.microsoft.com/en-us/library/windows/desktop/aa365468.aspx) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. |
| [SetFilePointer](https://msdn.microsoft.com/en-us/library/windows/desktop/aa365541.aspx) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. |
| [WriteFileEx](https://msdn.microsoft.com/en-us/library/windows/desktop/aa365748.aspx) | Introduced into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. |


## APIs from api-ms-win-core-file-l2-1-1.dll

| API | Requirements |
| -----| --------------|
| [CopyFile2](https://msdn.microsoft.com/en-us/library/windows/desktop/hh449404.aspx) | Introduced into api-ms-win-core-file-l2-1-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l2-1-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l2-1-1.dll in 10.0.14393. |
| [GetFileInformationByHandleEx](https://msdn.microsoft.com/en-us/library/windows/desktop/aa364953.aspx) | Introduced into api-ms-win-core-file-l2-1-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l2-1-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l2-1-1.dll in 10.0.14393. |
| [MoveFileExW](https://msdn.microsoft.com/en-us/library/windows/desktop/aa365240.aspx) | Introduced into api-ms-win-core-file-l2-1-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l2-1-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l2-1-1.dll in 10.0.14393. |
| [ReplaceFileW](https://msdn.microsoft.com/en-us/library/windows/desktop/aa365512.aspx) | Introduced into api-ms-win-core-file-l2-1-1.dll in 10.0.10240. Moved into api-ms-win-core-file-l2-1-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l2-1-1.dll in 10.0.14393. |


## APIs from api-ms-win-core-handle-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [CloseHandle](https://msdn.microsoft.com/en-us/library/windows/desktop/ms724211.aspx) | Introduced into api-ms-win-core-handle-l1-1-0.dll in 10.0.10240. |
| [CompareObjectHandles](https://msdn.microsoft.com/en-us/library/windows/desktop/mt438733.aspx) | Introduced into api-ms-win-core-handle-l1-1-0.dll in 10.0.10240. |
| [DuplicateHandle](https://msdn.microsoft.com/en-us/library/windows/desktop/aa375373.aspx) | Introduced into api-ms-win-core-handle-l1-1-0.dll in 10.0.10240. |


## APIs from api-ms-win-core-heap-l1-2-0.dll

| API | Requirements |
| -----| --------------|
| [GetProcessHeap](https://msdn.microsoft.com/en-us/library/windows/desktop/aa366569.aspx) | Introduced into api-ms-win-core-heap-l1-2-0.dll in 10.0.10240. |
| [HeapAlloc](https://msdn.microsoft.com/en-us/library/windows/desktop/aa366597.aspx) | Introduced into api-ms-win-core-heap-l1-2-0.dll in 10.0.10240. |
| [HeapCompact](https://msdn.microsoft.com/en-us/library/windows/desktop/aa366598.aspx) | Introduced into api-ms-win-core-heap-l1-2-0.dll in 10.0.10240. |
| [HeapCreate](https://msdn.microsoft.com/en-us/library/windows/desktop/aa366599.aspx) | Introduced into api-ms-win-core-heap-l1-2-0.dll in 10.0.10240. |
| [HeapDestroy](https://msdn.microsoft.com/en-us/library/windows/desktop/aa366700.aspx) | Introduced into api-ms-win-core-heap-l1-2-0.dll in 10.0.10240. |
| [HeapFree](https://msdn.microsoft.com/en-us/library/windows/desktop/aa366701.aspx) | Introduced into api-ms-win-core-heap-l1-2-0.dll in 10.0.10240. |
| [HeapReAlloc](https://msdn.microsoft.com/en-us/library/windows/desktop/aa366704.aspx) | Introduced into api-ms-win-core-heap-l1-2-0.dll in 10.0.10240. |
| [HeapSetInformation](https://msdn.microsoft.com/en-us/library/windows/desktop/aa366705.aspx) | Introduced into api-ms-win-core-heap-l1-2-0.dll in 10.0.10240. |
| [HeapSize](https://msdn.microsoft.com/en-us/library/windows/desktop/aa366706.aspx) | Introduced into api-ms-win-core-heap-l1-2-0.dll in 10.0.10240. |


## APIs from api-ms-win-core-interlocked-l1-2-0.dll

| API | Requirements |
| -----| --------------|
| [InitializeSListHead](https://msdn.microsoft.com/en-us/library/windows/desktop/ms683482.aspx) | Introduced into api-ms-win-core-interlocked-l1-2-0.dll in 10.0.10240. |
| [InterlockedFlushSList](https://msdn.microsoft.com/en-us/library/windows/desktop/ms683612.aspx) | Introduced into api-ms-win-core-interlocked-l1-2-0.dll in 10.0.10240. |
| [InterlockedPopEntrySList](https://msdn.microsoft.com/en-us/library/windows/desktop/ms683648.aspx) | Introduced into api-ms-win-core-interlocked-l1-2-0.dll in 10.0.10240. |
| [InterlockedPushEntrySList](https://msdn.microsoft.com/en-us/library/windows/desktop/ms684020.aspx) | Introduced into api-ms-win-core-interlocked-l1-2-0.dll in 10.0.10240. |
| [InterlockedPushListSListEx](https://msdn.microsoft.com/en-us/library/windows/desktop/hh972673.aspx) | Introduced into api-ms-win-core-interlocked-l1-2-0.dll in 10.0.10240. |
| [QueryDepthSList](https://msdn.microsoft.com/en-us/library/windows/desktop/ms684916.aspx) | Introduced into api-ms-win-core-interlocked-l1-2-0.dll in 10.0.10240. |


## APIs from api-ms-win-core-io-l1-1-1.dll

| API | Requirements |
| -----| --------------|
| [CancelIoEx](https://msdn.microsoft.com/en-us/library/windows/desktop/aa363792.aspx) | Introduced into api-ms-win-core-io-l1-1-1.dll in 10.0.10240. |
| [GetOverlappedResultEx](https://msdn.microsoft.com/en-us/library/windows/desktop/hh448542.aspx) | Introduced into api-ms-win-core-io-l1-1-1.dll in 10.0.10240. |
| [CancelIo](https://msdn.microsoft.com/en-us/library/windows/desktop/aa363791.aspx) | Introduced into api-ms-win-core-io-l1-1-1.dll in 10.0.14393. |
| [CreateIoCompletionPort](https://msdn.microsoft.com/en-us/library/windows/desktop/aa363862.aspx) | Introduced into api-ms-win-core-io-l1-1-1.dll in 10.0.14393. |
| [GetOverlappedResult](https://msdn.microsoft.com/en-us/library/windows/desktop/ms683209.aspx) | Introduced into api-ms-win-core-io-l1-1-1.dll in 10.0.14393. |
| [GetQueuedCompletionStatus](https://msdn.microsoft.com/en-us/library/windows/desktop/aa364986.aspx) | Introduced into api-ms-win-core-io-l1-1-1.dll in 10.0.14393. |
| [GetQueuedCompletionStatusEx](https://msdn.microsoft.com/en-us/library/windows/desktop/aa364988.aspx) | Introduced into api-ms-win-core-io-l1-1-1.dll in 10.0.14393. |
| [PostQueuedCompletionStatus](https://msdn.microsoft.com/en-us/library/windows/desktop/aa365458.aspx) | Introduced into api-ms-win-core-io-l1-1-1.dll in 10.0.14393. |


## APIs from api-ms-win-core-kernel32-legacy-l1-1-1.dll

| API | Requirements |
| -----| --------------|
| [MoveFileExA](https://msdn.microsoft.com/en-us/library/windows/desktop/aa365240.aspx) | Introduced into api-ms-win-core-kernel32-legacy-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-kernel32-legacy-l1-1-4.dll in 10.0.10586. Moved into api-ms-win-core-kernel32-legacy-l1-1-1.dll in 10.0.14393. |
| [GetSystemPowerStatus](https://msdn.microsoft.com/en-us/library/windows/desktop/aa372693(v=vs.85).aspx) | Introduced into api-ms-win-core-kernel32-legacy-l1-1-1.dll in 10.0.15063. |


## APIs from api-ms-win-core-largeinteger-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [MulDiv](https://msdn.microsoft.com/en-us/library/windows/desktop/aa383718.aspx) | Introduced into api-ms-win-core-largeinteger-l1-1-0.dll in 10.0.10240. |


## APIs from api-ms-win-core-libraryloader-l1-2-0.dll

| API | Requirements |
| -----| --------------|
| [DisableThreadLibraryCalls](https://msdn.microsoft.com/en-us/library/windows/desktop/ms682579.aspx) | Introduced into api-ms-win-core-libraryloader-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-libraryloader-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-libraryloader-l1-2-0.dll in 10.0.14393. |
| [FindStringOrdinal](https://msdn.microsoft.com/en-us/library/windows/desktop/dd318061.aspx) | Introduced into api-ms-win-core-libraryloader-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-libraryloader-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-libraryloader-l1-2-0.dll in 10.0.14393. |
| [FreeLibrary](https://msdn.microsoft.com/en-us/library/windows/desktop/ms683152.aspx) | Introduced into api-ms-win-core-libraryloader-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-libraryloader-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-libraryloader-l1-2-0.dll in 10.0.14393. |
| [GetModuleFileNameA](https://msdn.microsoft.com/en-us/library/windows/desktop/ms683197.aspx) | Introduced into api-ms-win-core-libraryloader-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-libraryloader-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-libraryloader-l1-2-0.dll in 10.0.14393. |
| [GetModuleFileNameW](https://msdn.microsoft.com/en-us/library/windows/desktop/ms683197.aspx) | Introduced into api-ms-win-core-libraryloader-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-libraryloader-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-libraryloader-l1-2-0.dll in 10.0.14393. |
| [GetProcAddress](https://msdn.microsoft.com/en-us/library/windows/desktop/ms683212.aspx) | Introduced into api-ms-win-core-libraryloader-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-libraryloader-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-libraryloader-l1-2-0.dll in 10.0.14393. |


## APIs from api-ms-win-core-libraryloader-l2-1-0.dll

| API | Requirements |
| -----| --------------|
| [LoadPackagedLibrary](https://msdn.microsoft.com/en-us/library/windows/desktop/hh447159.aspx) | Introduced into api-ms-win-core-libraryloader-l2-1-0.dll in 10.0.10240. |
| [QueryOptionalDelayLoadedAPI](https://msdn.microsoft.com/en-us/library/windows/desktop/mt403328.aspx) | Introduced into api-ms-win-core-libraryloader-l2-1-0.dll in 10.0.10240. |


## APIs from api-ms-win-core-localization-ansi-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [GetStringTypeExA](https://msdn.microsoft.com/en-us/library/windows/desktop/dd318118.aspx) | Introduced into api-ms-win-core-localization-ansi-l1-1-0.dll in 10.0.10240. |
| [EnumUILanguagesA](https://msdn.microsoft.com/en-us/library/Dd317834.aspx) | Introduced into api-ms-win-core-localization-ansi-l1-1-0.dll in 10.0.15063. |


## APIs from api-ms-win-core-localization-l1-2-1.dll

| API | Requirements |
| -----| --------------|
| [EnumSystemGeoID](https://msdn.microsoft.com/en-us/library/windows/desktop/dd317826.aspx) | Introduced into api-ms-win-core-localization-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-localization-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-localization-l1-2-1.dll in 10.0.14393. |
| [EnumSystemLocalesEx](https://msdn.microsoft.com/en-us/library/windows/desktop/dd317829.aspx) | Introduced into api-ms-win-core-localization-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-localization-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-localization-l1-2-1.dll in 10.0.14393. |
| [FindNLSStringEx](https://msdn.microsoft.com/en-us/library/windows/desktop/dd318059.aspx) | Introduced into api-ms-win-core-localization-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-localization-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-localization-l1-2-1.dll in 10.0.14393. |
| [FormatMessageA](https://msdn.microsoft.com/en-us/library/windows/desktop/ms679351.aspx) | Introduced into api-ms-win-core-localization-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-localization-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-localization-l1-2-1.dll in 10.0.14393. |
| [FormatMessageW](https://msdn.microsoft.com/en-us/library/windows/desktop/ms679351.aspx) | Introduced into api-ms-win-core-localization-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-localization-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-localization-l1-2-1.dll in 10.0.14393. |
| [GetCalendarInfoEx](https://msdn.microsoft.com/en-us/library/windows/desktop/dd318075.aspx) | Introduced into api-ms-win-core-localization-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-localization-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-localization-l1-2-1.dll in 10.0.14393. |
| [GetCPInfo](https://msdn.microsoft.com/en-us/library/windows/desktop/dd318078.aspx) | Introduced into api-ms-win-core-localization-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-localization-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-localization-l1-2-1.dll in 10.0.14393. |
| [GetCPInfoExW](https://msdn.microsoft.com/en-us/library/windows/desktop/dd318081.aspx) | Introduced into api-ms-win-core-localization-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-localization-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-localization-l1-2-1.dll in 10.0.14393. |
| [GetGeoInfoW](https://msdn.microsoft.com/en-us/library/windows/desktop/dd318099.aspx) | Introduced into api-ms-win-core-localization-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-localization-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-localization-l1-2-1.dll in 10.0.14393. |
| [GetLocaleInfoEx](https://msdn.microsoft.com/en-us/library/windows/desktop/dd318103.aspx) | Introduced into api-ms-win-core-localization-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-localization-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-localization-l1-2-1.dll in 10.0.14393. |
| [GetNLSVersionEx](https://msdn.microsoft.com/en-us/library/windows/desktop/dd318107.aspx) | Introduced into api-ms-win-core-localization-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-localization-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-localization-l1-2-1.dll in 10.0.14393. |
| [GetUserDefaultLocaleName](https://msdn.microsoft.com/en-us/library/windows/desktop/dd318136.aspx) | Introduced into api-ms-win-core-localization-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-localization-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-localization-l1-2-1.dll in 10.0.14393. |
| [GetUserGeoID](https://msdn.microsoft.com/en-us/library/windows/desktop/dd318138.aspx) | Introduced into api-ms-win-core-localization-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-localization-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-localization-l1-2-1.dll in 10.0.14393. |
| [IdnToAscii](https://msdn.microsoft.com/en-us/library/windows/desktop/dd318149.aspx) | Introduced into api-ms-win-core-localization-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-localization-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-localization-l1-2-1.dll in 10.0.14393. |
| [IdnToUnicode](https://msdn.microsoft.com/en-us/library/windows/desktop/dd318151.aspx) | Introduced into api-ms-win-core-localization-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-localization-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-localization-l1-2-1.dll in 10.0.14393. |
| [IsValidCodePage](https://msdn.microsoft.com/en-us/library/windows/desktop/dd318674.aspx) | Introduced into api-ms-win-core-localization-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-localization-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-localization-l1-2-1.dll in 10.0.14393. |
| [IsValidLocaleName](https://msdn.microsoft.com/en-us/library/windows/desktop/dd318681.aspx) | Introduced into api-ms-win-core-localization-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-localization-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-localization-l1-2-1.dll in 10.0.14393. |
| [IsValidNLSVersion](https://msdn.microsoft.com/en-us/library/windows/desktop/hh706739.aspx) | Introduced into api-ms-win-core-localization-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-localization-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-localization-l1-2-1.dll in 10.0.14393. |
| [LCMapStringEx](https://msdn.microsoft.com/en-us/library/windows/desktop/dd318702.aspx) | Introduced into api-ms-win-core-localization-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-localization-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-localization-l1-2-1.dll in 10.0.14393. |
| [LocaleNameToLCID](https://msdn.microsoft.com/en-us/library/windows/desktop/dd318711.aspx) | Introduced into api-ms-win-core-localization-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-localization-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-localization-l1-2-1.dll in 10.0.14393. |
| [ResolveLocaleName](https://msdn.microsoft.com/en-us/library/windows/desktop/dd319112.aspx) | Introduced into api-ms-win-core-localization-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-localization-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-localization-l1-2-1.dll in 10.0.14393. |
| [GetLocaleInfoW](https://msdn.microsoft.com/en-us/library/Dd318101.aspx) | Introduced into api-ms-win-core-localization-l1-2-1.dll in 10.0.15063. |
| [GetLocaleInfoA](https://msdn.microsoft.com/en-us/library/Dd318101.aspx) | Introduced into api-ms-win-core-localization-l1-2-1.dll in 10.0.15063. |
| [GetACP](https://msdn.microsoft.com/en-us/library/Dd318070.aspx) | Introduced into api-ms-win-core-localization-l1-2-1.dll in 10.0.15063. |
| [GetUserDefaultLangID](https://msdn.microsoft.com/en-us/library/Dd318134.aspx) | Introduced into api-ms-win-core-localization-l1-2-1.dll in 10.0.15063. |
| [IsDBCSLeadByteEx](https://msdn.microsoft.com/en-us/library/Dd318667.aspx) | Introduced into api-ms-win-core-localization-l1-2-1.dll in 10.0.15063. |
| [IsDBCSLeadByte](https://msdn.microsoft.com/en-us/library/Dd318664.aspx) | Introduced into api-ms-win-core-localization-l1-2-1.dll in 10.0.15063. |


## APIs from api-ms-win-core-localization-l1-2-2.dll

| API | Requirements |
| -----| --------------|
| [GetSystemDefaultLocaleName](https://msdn.microsoft.com/en-us/library/windows/desktop/dd318122.aspx) | Introduced into api-ms-win-core-localization-l1-2-2.dll in 10.0.10240. |
| [LCIDToLocaleName](https://msdn.microsoft.com/en-us/library/windows/desktop/dd318698.aspx) | Introduced into api-ms-win-core-localization-l1-2-2.dll in 10.0.10240. |


## APIs from api-ms-win-core-localization-l2-1-0.dll

| API | Requirements |
| -----| --------------|
| [EnumCalendarInfoExEx](https://msdn.microsoft.com/en-us/library/windows/desktop/dd317805.aspx) | Introduced into api-ms-win-core-localization-l2-1-0.dll in 10.0.10240. |
| [EnumDateFormatsExEx](https://msdn.microsoft.com/en-us/library/windows/desktop/dd317812.aspx) | Introduced into api-ms-win-core-localization-l2-1-0.dll in 10.0.10240. |
| [EnumSystemCodePagesW](https://msdn.microsoft.com/en-us/library/windows/desktop/dd317825.aspx) | Introduced into api-ms-win-core-localization-l2-1-0.dll in 10.0.10240. |
| [EnumTimeFormatsEx](https://msdn.microsoft.com/en-us/library/windows/desktop/dd317831.aspx) | Introduced into api-ms-win-core-localization-l2-1-0.dll in 10.0.10240. |
| [GetCurrencyFormatEx](https://msdn.microsoft.com/en-us/library/windows/desktop/dd318084.aspx) | Introduced into api-ms-win-core-localization-l2-1-0.dll in 10.0.10240. |
| [GetNumberFormatEx](https://msdn.microsoft.com/en-us/library/windows/desktop/dd318113.aspx) | Introduced into api-ms-win-core-localization-l2-1-0.dll in 10.0.10240. |


## APIs from api-ms-win-core-memory-l1-1-2.dll

| API | Requirements |
| -----| --------------|
| [CreateFileMappingFromApp](https://msdn.microsoft.com/en-us/library/windows/desktop/hh994453.aspx) | Introduced into api-ms-win-core-memory-l1-1-2.dll in 10.0.10240. Moved into api-ms-win-core-memory-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-memory-l1-1-2.dll in 10.0.14393. |
| [DiscardVirtualMemory](https://msdn.microsoft.com/en-us/library/windows/desktop/dn781432.aspx) | Introduced into api-ms-win-core-memory-l1-1-2.dll in 10.0.10240. Moved into api-ms-win-core-memory-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-memory-l1-1-2.dll in 10.0.14393. |
| [FlushViewOfFile](https://msdn.microsoft.com/en-us/library/windows/desktop/aa366563.aspx) | Introduced into api-ms-win-core-memory-l1-1-2.dll in 10.0.10240. Moved into api-ms-win-core-memory-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-memory-l1-1-2.dll in 10.0.14393. |
| [GetWriteWatch](https://msdn.microsoft.com/en-us/library/windows/desktop/aa366573.aspx) | Introduced into api-ms-win-core-memory-l1-1-2.dll in 10.0.10240. Moved into api-ms-win-core-memory-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-memory-l1-1-2.dll in 10.0.14393. |
| [MapViewOfFileFromApp](https://msdn.microsoft.com/en-us/library/windows/desktop/hh994454.aspx) | Introduced into api-ms-win-core-memory-l1-1-2.dll in 10.0.10240. Moved into api-ms-win-core-memory-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-memory-l1-1-2.dll in 10.0.14393. |
| [OfferVirtualMemory](https://msdn.microsoft.com/en-us/library/windows/desktop/dn781436.aspx) | Introduced into api-ms-win-core-memory-l1-1-2.dll in 10.0.10240. Moved into api-ms-win-core-memory-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-memory-l1-1-2.dll in 10.0.14393. |
| [ReclaimVirtualMemory](https://msdn.microsoft.com/en-us/library/windows/desktop/dn781437.aspx) | Introduced into api-ms-win-core-memory-l1-1-2.dll in 10.0.10240. Moved into api-ms-win-core-memory-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-memory-l1-1-2.dll in 10.0.14393. |
| [ResetWriteWatch](https://msdn.microsoft.com/en-us/library/windows/desktop/aa366874.aspx) | Introduced into api-ms-win-core-memory-l1-1-2.dll in 10.0.10240. Moved into api-ms-win-core-memory-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-memory-l1-1-2.dll in 10.0.14393. |
| [UnmapViewOfFile](https://msdn.microsoft.com/en-us/library/windows/desktop/aa366882.aspx) | Introduced into api-ms-win-core-memory-l1-1-2.dll in 10.0.10240. Moved into api-ms-win-core-memory-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-memory-l1-1-2.dll in 10.0.14393. |
| [VirtualFree](https://msdn.microsoft.com/en-us/library/windows/desktop/aa366892.aspx) | Introduced into api-ms-win-core-memory-l1-1-2.dll in 10.0.10240. Moved into api-ms-win-core-memory-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-memory-l1-1-2.dll in 10.0.14393. |
| [VirtualQuery](https://msdn.microsoft.com/en-us/library/windows/desktop/aa366902.aspx) | Introduced into api-ms-win-core-memory-l1-1-2.dll in 10.0.10240. Moved into api-ms-win-core-memory-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-memory-l1-1-2.dll in 10.0.14393. |
| [UnmapViewOfFileEx](https://msdn.microsoft.com/en-us/library/windows/desktop/mt670639.aspx) | Introduced into api-ms-win-core-memory-l1-1-2.dll in 10.0.14393. |


## APIs from api-ms-win-core-memory-l1-1-3.dll

| API | Requirements |
| -----| --------------|
| [OpenFileMappingFromApp](https://msdn.microsoft.com/en-us/library/windows/desktop/mt169844.aspx) | Introduced into api-ms-win-core-memory-l1-1-3.dll in 10.0.10240. Moved into api-ms-win-core-memory-l1-1-4.dll in 10.0.14393. Moved into api-ms-win-core-memory-l1-1-5.dll in 10.0.15063. |
| [VirtualAllocFromApp](https://msdn.microsoft.com/en-us/library/windows/desktop/mt169845.aspx) | Introduced into api-ms-win-core-memory-l1-1-3.dll in 10.0.10240. Moved into api-ms-win-core-memory-l1-1-4.dll in 10.0.14393. Moved into api-ms-win-core-memory-l1-1-5.dll in 10.0.15063. |
| [VirtualProtectFromApp](https://msdn.microsoft.com/en-us/library/windows/desktop/mt169846.aspx) | Introduced into api-ms-win-core-memory-l1-1-3.dll in 10.0.10240. Moved into api-ms-win-core-memory-l1-1-4.dll in 10.0.14393. Moved into api-ms-win-core-memory-l1-1-5.dll in 10.0.15063. |


## APIs from api-ms-win-core-normalization-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [GetStringScripts](https://msdn.microsoft.com/en-us/library/windows/desktop/dd318116.aspx) | Introduced into api-ms-win-core-normalization-l1-1-0.dll in 10.0.10240. |
| [IdnToNameprepUnicode](https://msdn.microsoft.com/en-us/library/windows/desktop/dd318150.aspx) | Introduced into api-ms-win-core-normalization-l1-1-0.dll in 10.0.10240. |
| [IsNormalizedString](https://msdn.microsoft.com/en-us/library/windows/desktop/dd318671.aspx) | Introduced into api-ms-win-core-normalization-l1-1-0.dll in 10.0.10240. |
| [NormalizeString](https://msdn.microsoft.com/en-us/library/windows/desktop/dd319093.aspx) | Introduced into api-ms-win-core-normalization-l1-1-0.dll in 10.0.10240. |
| [VerifyScripts](https://msdn.microsoft.com/en-us/library/windows/desktop/dd374129.aspx) | Introduced into api-ms-win-core-normalization-l1-1-0.dll in 10.0.10240. |


## APIs from api-ms-win-core-processenvironment-l1-2-0.dll

| API | Requirements |
| -----| --------------|
| [GetCommandLineA](https://msdn.microsoft.com/en-us/library/windows/desktop/ms683156.aspx) | Introduced into api-ms-win-core-processenvironment-l1-2-0.dll in 10.0.10240. |
| [GetCommandLineW](https://msdn.microsoft.com/en-us/library/windows/desktop/ms683156.aspx) | Introduced into api-ms-win-core-processenvironment-l1-2-0.dll in 10.0.10240. |
| [GetCurrentDirectoryW](https://msdn.microsoft.com/en-us/library/windows/desktop/aa364934.aspx) | Introduced into api-ms-win-core-processenvironment-l1-2-0.dll in 10.0.10240. |
| [SetCurrentDirectoryW](https://msdn.microsoft.com/en-us/library/windows/desktop/aa365530.aspx) | Introduced into api-ms-win-core-processenvironment-l1-2-0.dll in 10.0.10240. |


## APIs from api-ms-win-core-processthreads-l1-1-2.dll

| API | Requirements |
| -----| --------------|
| [CreateThread](https://msdn.microsoft.com/en-us/library/windows/desktop/ms682453.aspx) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.10240. Moved into api-ms-win-core-processthreads-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.14393. |
| [ExitThread](https://msdn.microsoft.com/en-us/library/windows/desktop/ms682659.aspx) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.10240. Moved into api-ms-win-core-processthreads-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.14393. |
| [FlushProcessWriteBuffers](https://msdn.microsoft.com/en-us/library/windows/desktop/ms683148.aspx) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.10240. Moved into api-ms-win-core-processthreads-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.14393. |
| [GetCurrentProcess](https://msdn.microsoft.com/en-us/library/windows/desktop/ms683179.aspx) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.10240. Moved into api-ms-win-core-processthreads-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.14393. |
| [GetCurrentProcessId](https://msdn.microsoft.com/en-us/library/windows/desktop/ms683180.aspx) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.10240. Moved into api-ms-win-core-processthreads-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.14393. |
| [GetCurrentThread](https://msdn.microsoft.com/en-us/library/windows/desktop/ms683182.aspx) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.10240. Moved into api-ms-win-core-processthreads-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.14393. |
| [GetCurrentThreadId](https://msdn.microsoft.com/en-us/library/windows/desktop/ms683183.aspx) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.10240. Moved into api-ms-win-core-processthreads-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.14393. |
| [GetExitCodeThread](https://msdn.microsoft.com/en-us/library/windows/desktop/ms683190.aspx) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.10240. Moved into api-ms-win-core-processthreads-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.14393. |
| [GetThreadContext](https://msdn.microsoft.com/en-us/library/windows/desktop/ms679362.aspx) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.10240. Moved into api-ms-win-core-processthreads-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.14393. |
| [GetThreadId](https://msdn.microsoft.com/en-us/library/windows/desktop/ms683233.aspx) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.10240. Moved into api-ms-win-core-processthreads-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.14393. |
| [GetThreadPriority](https://msdn.microsoft.com/en-us/library/windows/desktop/ms683235.aspx) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.10240. Moved into api-ms-win-core-processthreads-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.14393. |
| [IsProcessorFeaturePresent](https://msdn.microsoft.com/en-us/library/windows/desktop/ms724482.aspx) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.10240. Moved into api-ms-win-core-processthreads-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.14393. |
| [OpenProcess](https://msdn.microsoft.com/en-us/library/windows/desktop/ms684320.aspx) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.10240. Moved into api-ms-win-core-processthreads-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.14393. |
| [QueueUserAPC](https://msdn.microsoft.com/en-us/library/windows/desktop/ms684954.aspx) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.10240. Moved into api-ms-win-core-processthreads-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.14393. |
| [ResumeThread](https://msdn.microsoft.com/en-us/library/windows/desktop/ms685086.aspx) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.10240. Moved into api-ms-win-core-processthreads-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.14393. |
| [SetThreadIdealProcessorEx](https://msdn.microsoft.com/en-us/library/windows/desktop/dd405517.aspx) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.10240. Moved into api-ms-win-core-processthreads-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.14393. |
| [SetThreadPriority](https://msdn.microsoft.com/en-us/library/windows/desktop/ms686277.aspx) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.10240. Moved into api-ms-win-core-processthreads-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.14393. |
| [SuspendThread](https://msdn.microsoft.com/en-us/library/windows/desktop/ms686345.aspx) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.10240. Moved into api-ms-win-core-processthreads-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.14393. |
| [SwitchToThread](https://msdn.microsoft.com/en-us/library/windows/desktop/ms686352.aspx) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.10240. Moved into api-ms-win-core-processthreads-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.14393. |
| [TerminateProcess](https://msdn.microsoft.com/en-us/library/windows/desktop/ms686714.aspx) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.10240. Moved into api-ms-win-core-processthreads-l1-1-3.dll in 10.0.10586. Moved into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.14393. |
| [TlsAlloc](https://msdn.microsoft.com/en-us/library/windows/desktop/ms686801.aspx) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.14393. |
| [TlsFree](https://msdn.microsoft.com/en-us/library/windows/desktop/ms686804.aspx) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.14393. |
| [TlsGetValue](https://msdn.microsoft.com/en-us/library/windows/desktop/ms686812.aspx) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.14393. |
| [TlsSetValue](https://msdn.microsoft.com/en-us/library/windows/desktop/ms686818.aspx) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.14393. |
| [OpenProcessToken](https://msdn.microsoft.com/en-us/library/Aa379295.aspx) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.15063. |
| [GetProcessId](https://msdn.microsoft.com/en-us/library/ms683215.aspx) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.15063. |
| [GetProcessMitigationPolicy](https://msdn.microsoft.com/en-us/library/Hh769085.aspx) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.15063. |
| [GetExitCodeProcess](https://msdn.microsoft.com/en-us/library/ms683189.aspx) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.15063. |
| [OpenThread](https://msdn.microsoft.com/en-us/library/ms684335.aspx) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.15063. |
| [GetProcessTimes](https://msdn.microsoft.com/en-us/library/ms683223.aspx) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.15063. |
| [GetThreadTimes](https://msdn.microsoft.com/en-us/library/ms683237.aspx) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.15063. |
| [GetCurrentProcessorNumber](https://msdn.microsoft.com/en-us/library/ms683181.aspx) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.15063. |
| [GetThreadIdealProcessorEx](https://msdn.microsoft.com/en-us/library/Dd405499.aspx) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.15063. |
| [GetCurrentProcessorNumberEx](https://msdn.microsoft.com/en-us/library/Dd405487.aspx) | Introduced into api-ms-win-core-processthreads-l1-1-2.dll in 10.0.15063. |


## APIs from api-ms-win-core-processthreads-l1-1-3.dll

| API | Requirements |
| -----| --------------|
| [GetProcessDefaultCpuSets](https://msdn.microsoft.com/en-us/library/windows/desktop/mt186424.aspx) | Introduced into api-ms-win-core-processthreads-l1-1-3.dll in 10.0.10240. |
| [GetProcessInformation](https://msdn.microsoft.com/en-us/library/windows/desktop/hh448381.aspx) | Introduced into api-ms-win-core-processthreads-l1-1-3.dll in 10.0.10240. |
| [GetSystemCpuSetInformation](https://msdn.microsoft.com/en-us/library/windows/desktop/mt186425.aspx) | Introduced into api-ms-win-core-processthreads-l1-1-3.dll in 10.0.10240. |
| [GetThreadSelectedCpuSets](https://msdn.microsoft.com/en-us/library/windows/desktop/mt186426.aspx) | Introduced into api-ms-win-core-processthreads-l1-1-3.dll in 10.0.10240. |
| [SetProcessDefaultCpuSets](https://msdn.microsoft.com/en-us/library/windows/desktop/mt186427.aspx) | Introduced into api-ms-win-core-processthreads-l1-1-3.dll in 10.0.10240. |
| [SetProcessInformation](https://msdn.microsoft.com/en-us/library/windows/desktop/hh448389.aspx) | Introduced into api-ms-win-core-processthreads-l1-1-3.dll in 10.0.10240. |
| [SetThreadIdealProcessor](https://msdn.microsoft.com/en-us/library/windows/desktop/ms686253.aspx) | Introduced into api-ms-win-core-processthreads-l1-1-3.dll in 10.0.10240. |
| [SetThreadSelectedCpuSets](https://msdn.microsoft.com/en-us/library/windows/desktop/mt186428.aspx) | Introduced into api-ms-win-core-processthreads-l1-1-3.dll in 10.0.10240. |
| [GetThreadDescription](https://msdn.microsoft.com/en-us/library/Mt774972.aspx) | Introduced into api-ms-win-core-processthreads-l1-1-3.dll in 10.0.15063. |
| [SetThreadDescription](https://msdn.microsoft.com/en-us/library/Mt774976.aspx) | Introduced into api-ms-win-core-processthreads-l1-1-3.dll in 10.0.15063. |


## APIs from api-ms-win-core-profile-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [QueryPerformanceCounter](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644904.aspx) | Introduced into api-ms-win-core-profile-l1-1-0.dll in 10.0.10240. |
| [QueryPerformanceFrequency](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644905.aspx) | Introduced into api-ms-win-core-profile-l1-1-0.dll in 10.0.10240. |


## APIs from api-ms-win-core-realtime-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [QueryUnbiasedInterruptTime](https://msdn.microsoft.com/en-us/library/windows/desktop/ee662307.aspx) | Introduced into api-ms-win-core-realtime-l1-1-0.dll in 10.0.10240. Moved into api-ms-win-core-realtime-l1-1-1.dll in 10.0.10586. Moved into api-ms-win-core-realtime-l1-1-0.dll in 10.0.14393. |


## APIs from api-ms-win-core-realtime-l1-1-1.dll

| API | Requirements |
| -----| --------------|
| [QueryInterruptTime](https://msdn.microsoft.com/en-us/library/windows/desktop/dn903659.aspx) | Introduced into api-ms-win-core-realtime-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-realtime-l1-1-2.dll in 10.0.15063. |
| [QueryInterruptTimePrecise](https://msdn.microsoft.com/en-us/library/windows/desktop/dn903660.aspx) | Introduced into api-ms-win-core-realtime-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-realtime-l1-1-2.dll in 10.0.15063. |
| [QueryUnbiasedInterruptTimePrecise](https://msdn.microsoft.com/en-us/library/windows/desktop/dn891448.aspx) | Introduced into api-ms-win-core-realtime-l1-1-1.dll in 10.0.10240. Moved into api-ms-win-core-realtime-l1-1-2.dll in 10.0.15063. |


## APIs from api-ms-win-core-rtlsupport-l1-2-0.dll

| API | Requirements |
| -----| --------------|
| [RtlCaptureStackBackTrace](https://msdn.microsoft.com/en-us/library/windows/desktop/aa813366.aspx) | Introduced into api-ms-win-core-rtlsupport-l1-2-0.dll in 10.0.10240. |
| [RtlLookupFunctionEntry](https://msdn.microsoft.com/en-us/library/windows/desktop/ms680597.aspx) | Introduced into api-ms-win-core-rtlsupport-l1-2-0.dll in 10.0.10240. |
| [RtlPcToFileHeader](https://msdn.microsoft.com/en-us/library/windows/desktop/ms680603.aspx) | Introduced into api-ms-win-core-rtlsupport-l1-2-0.dll in 10.0.10240. |
| [RtlUnwind](https://msdn.microsoft.com/en-us/library/windows/desktop/ms680609.aspx) | Introduced into api-ms-win-core-rtlsupport-l1-2-0.dll in 10.0.10240. |
| [RtlUnwindEx](https://msdn.microsoft.com/en-us/library/windows/desktop/ms680615.aspx) | Introduced into api-ms-win-core-rtlsupport-l1-2-0.dll in 10.0.10240. |


## APIs from api-ms-win-core-string-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [CompareStringEx](https://msdn.microsoft.com/en-us/library/windows/desktop/dd317761.aspx) | Introduced into api-ms-win-core-string-l1-1-0.dll in 10.0.10240. |
| [CompareStringOrdinal](https://msdn.microsoft.com/en-us/library/windows/desktop/dd317762.aspx) | Introduced into api-ms-win-core-string-l1-1-0.dll in 10.0.10240. |
| [GetStringTypeExW](https://msdn.microsoft.com/en-us/library/windows/desktop/dd318118.aspx) | Introduced into api-ms-win-core-string-l1-1-0.dll in 10.0.10240. |
| [GetStringTypeW](https://msdn.microsoft.com/en-us/library/windows/desktop/dd318119.aspx) | Introduced into api-ms-win-core-string-l1-1-0.dll in 10.0.10240. |
| [MultiByteToWideChar](https://msdn.microsoft.com/en-us/library/windows/desktop/dd319072.aspx) | Introduced into api-ms-win-core-string-l1-1-0.dll in 10.0.10240. |
| [WideCharToMultiByte](https://msdn.microsoft.com/en-us/library/windows/desktop/dd374130.aspx) | Introduced into api-ms-win-core-string-l1-1-0.dll in 10.0.10240. |


## APIs from api-ms-win-core-synch-ansi-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [CreateSemaphoreA](https://msdn.microsoft.com/en-us/library/windows/desktop/ms682438.aspx) | Introduced into api-ms-win-core-synch-ansi-l1-1-0.dll in 10.0.10240. |
| [CreateSemaphoreExA](https://msdn.microsoft.com/en-us/library/windows/desktop/ms682446.aspx) | Introduced into api-ms-win-core-synch-ansi-l1-1-0.dll in 10.0.10240. |
| [OpenMutexA](https://msdn.microsoft.com/en-us/library/windows/desktop/ms684315.aspx) | Introduced into api-ms-win-core-synch-ansi-l1-1-0.dll in 10.0.10240. |
| [CreateWaitableTimerA](https://msdn.microsoft.com/en-us/library/ms682492.aspx) | Introduced into api-ms-win-core-synch-ansi-l1-1-0.dll in 10.0.15063. |
| [CreateWaitableTimerExA](https://msdn.microsoft.com/en-us/library/ms682494.aspx) | Introduced into api-ms-win-core-synch-ansi-l1-1-0.dll in 10.0.15063. |
| [OpenWaitableTimerA](https://msdn.microsoft.com/en-us/library/ms684337.aspx) | Introduced into api-ms-win-core-synch-ansi-l1-1-0.dll in 10.0.15063. |


## APIs from api-ms-win-core-synch-l1-2-0.dll

| API | Requirements |
| -----| --------------|
| [AcquireSRWLockExclusive](https://msdn.microsoft.com/en-us/library/windows/desktop/ms681930.aspx) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. |
| [AcquireSRWLockShared](https://msdn.microsoft.com/en-us/library/windows/desktop/ms681934.aspx) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. |
| [CreateEventA](https://msdn.microsoft.com/en-us/library/windows/desktop/ms682396.aspx) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. |
| [CreateEventExA](https://msdn.microsoft.com/en-us/library/windows/desktop/ms682400.aspx) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. |
| [CreateEventExW](https://msdn.microsoft.com/en-us/library/windows/desktop/ms682400.aspx) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. |
| [CreateEventW](https://msdn.microsoft.com/en-us/library/windows/desktop/ms682396.aspx) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. |
| [CreateMutexA](https://msdn.microsoft.com/en-us/library/windows/desktop/ms682411.aspx) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. |
| [CreateMutexExA](https://msdn.microsoft.com/en-us/library/windows/desktop/ms682418.aspx) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. |
| [CreateMutexExW](https://msdn.microsoft.com/en-us/library/windows/desktop/ms682418.aspx) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. |
| [CreateMutexW](https://msdn.microsoft.com/en-us/library/windows/desktop/ms682411.aspx) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. |
| [CreateSemaphoreExW](https://msdn.microsoft.com/en-us/library/windows/desktop/ms682446.aspx) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. |
| [DeleteCriticalSection](https://msdn.microsoft.com/en-us/library/windows/desktop/ms682552.aspx) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. |
| [EnterCriticalSection](https://msdn.microsoft.com/en-us/library/windows/desktop/ms682608.aspx) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. |
| [InitializeConditionVariable](https://msdn.microsoft.com/en-us/library/windows/desktop/ms683469.aspx) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. |
| [InitializeCriticalSection](https://msdn.microsoft.com/en-us/library/windows/desktop/ms683472.aspx) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. |
| [InitializeCriticalSectionAndSpinCount](https://msdn.microsoft.com/en-us/library/windows/desktop/ms683476.aspx) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. |
| [InitializeCriticalSectionEx](https://msdn.microsoft.com/en-us/library/windows/desktop/ms683477.aspx) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. |
| [InitializeSRWLock](https://msdn.microsoft.com/en-us/library/windows/desktop/ms683483.aspx) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. |
| [InitOnceBeginInitialize](https://msdn.microsoft.com/en-us/library/windows/desktop/ms683487.aspx) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. |
| [InitOnceComplete](https://msdn.microsoft.com/en-us/library/windows/desktop/ms683491.aspx) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. |
| [InitOnceExecuteOnce](https://msdn.microsoft.com/en-us/library/windows/desktop/ms683493.aspx) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. |
| [InitOnceInitialize](https://msdn.microsoft.com/en-us/library/windows/desktop/ms683495.aspx) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. |
| [LeaveCriticalSection](https://msdn.microsoft.com/en-us/library/windows/desktop/ms684169.aspx) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. |
| [OpenEventA](https://msdn.microsoft.com/en-us/library/windows/desktop/ms684305.aspx) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. |
| [OpenEventW](https://msdn.microsoft.com/en-us/library/windows/desktop/ms684305.aspx) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. |
| [OpenMutexW](https://msdn.microsoft.com/en-us/library/windows/desktop/ms684315.aspx) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. |
| [OpenSemaphoreW](https://msdn.microsoft.com/en-us/library/windows/desktop/ms684326.aspx) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. |
| [ReleaseMutex](https://msdn.microsoft.com/en-us/library/windows/desktop/ms685066.aspx) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. |
| [ReleaseSemaphore](https://msdn.microsoft.com/en-us/library/windows/desktop/ms685071.aspx) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. |
| [ReleaseSRWLockExclusive](https://msdn.microsoft.com/en-us/library/windows/desktop/ms685076.aspx) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. |
| [ReleaseSRWLockShared](https://msdn.microsoft.com/en-us/library/windows/desktop/ms685080.aspx) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. |
| [ResetEvent](https://msdn.microsoft.com/en-us/library/windows/desktop/ms685081.aspx) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. |
| [SetCriticalSectionSpinCount](https://msdn.microsoft.com/en-us/library/windows/desktop/ms686197.aspx) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. |
| [SetEvent](https://msdn.microsoft.com/en-us/library/windows/desktop/ms686211.aspx) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. |
| [Sleep](https://msdn.microsoft.com/en-us/library/windows/desktop/ms686298.aspx) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. |
| [SleepConditionVariableCS](https://msdn.microsoft.com/en-us/library/windows/desktop/ms686301.aspx) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. |
| [SleepConditionVariableSRW](https://msdn.microsoft.com/en-us/library/windows/desktop/ms686304.aspx) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. |
| [SleepEx](https://msdn.microsoft.com/en-us/library/windows/desktop/ms686307.aspx) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. |
| [TryAcquireSRWLockExclusive](https://msdn.microsoft.com/en-us/library/windows/desktop/dd405523.aspx) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. |
| [TryAcquireSRWLockShared](https://msdn.microsoft.com/en-us/library/windows/desktop/dd405524.aspx) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. |
| [TryEnterCriticalSection](https://msdn.microsoft.com/en-us/library/windows/desktop/ms686857.aspx) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. |
| [WaitForMultipleObjectsEx](https://msdn.microsoft.com/en-us/library/windows/desktop/ms687028.aspx) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. |
| [WaitForSingleObject](https://msdn.microsoft.com/en-us/library/windows/desktop/ms687032.aspx) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. |
| [WaitForSingleObjectEx](https://msdn.microsoft.com/en-us/library/windows/desktop/ms687036.aspx) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. |
| [WaitOnAddress](https://msdn.microsoft.com/en-us/library/windows/desktop/hh706898.aspx) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. |
| [WakeAllConditionVariable](https://msdn.microsoft.com/en-us/library/windows/desktop/ms687076.aspx) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. |
| [WakeByAddressAll](https://msdn.microsoft.com/en-us/library/windows/desktop/hh706899.aspx) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. |
| [WakeByAddressSingle](https://msdn.microsoft.com/en-us/library/windows/desktop/hh706900.aspx) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. |
| [WakeConditionVariable](https://msdn.microsoft.com/en-us/library/windows/desktop/ms687080.aspx) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.10240. Moved into api-ms-win-core-synch-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-synch-l1-2-0.dll in 10.0.14393. |
| [SetWaitableTimer](https://msdn.microsoft.com/en-us/library/ms686289.aspx) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.15063. |
| [CancelWaitableTimer](https://msdn.microsoft.com/en-us/library/ms681985.aspx) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.15063. |
| [CreateWaitableTimerExW](https://msdn.microsoft.com/en-us/library/ms682494.aspx) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.15063. |
| [SetWaitableTimerEx](https://msdn.microsoft.com/en-us/library/Dd405521.aspx) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.15063. |
| [SignalObjectAndWait](https://msdn.microsoft.com/en-us/library/ms686293.aspx) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.15063. |
| [OpenWaitableTimerW](https://msdn.microsoft.com/en-us/library/ms684337.aspx) | Introduced into api-ms-win-core-synch-l1-2-0.dll in 10.0.15063. |


## APIs from api-ms-win-core-synch-l1-2-1.dll

| API | Requirements |
| -----| --------------|
| [CreateSemaphoreW](https://msdn.microsoft.com/en-us/library/windows/desktop/ms682438.aspx) | Introduced into api-ms-win-core-synch-l1-2-1.dll in 10.0.10240. |
| [WaitForMultipleObjects](https://msdn.microsoft.com/en-us/library/windows/desktop/ms687025.aspx) | Introduced into api-ms-win-core-synch-l1-2-1.dll in 10.0.10240. |
| [CreateWaitableTimerW](https://msdn.microsoft.com/en-us/library/ms682492.aspx) | Introduced into api-ms-win-core-synch-l1-2-1.dll in 10.0.15063. |


## APIs from api-ms-win-core-sysinfo-l1-2-1.dll

| API | Requirements |
| -----| --------------|
| [GetLocalTime](https://msdn.microsoft.com/en-us/library/windows/desktop/ms724338.aspx) | Introduced into api-ms-win-core-sysinfo-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-sysinfo-l1-2-3.dll in 10.0.10586. Moved into api-ms-win-core-sysinfo-l1-2-1.dll in 10.0.14393. |
| [GetNativeSystemInfo](https://msdn.microsoft.com/en-us/library/windows/desktop/ms724340.aspx) | Introduced into api-ms-win-core-sysinfo-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-sysinfo-l1-2-3.dll in 10.0.10586. Moved into api-ms-win-core-sysinfo-l1-2-1.dll in 10.0.14393. |
| [GetSystemInfo](https://msdn.microsoft.com/en-us/library/windows/desktop/ms724381.aspx) | Introduced into api-ms-win-core-sysinfo-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-sysinfo-l1-2-3.dll in 10.0.10586. Moved into api-ms-win-core-sysinfo-l1-2-1.dll in 10.0.14393. |
| [GetSystemTime](https://msdn.microsoft.com/en-us/library/windows/desktop/ms724390.aspx) | Introduced into api-ms-win-core-sysinfo-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-sysinfo-l1-2-3.dll in 10.0.10586. Moved into api-ms-win-core-sysinfo-l1-2-1.dll in 10.0.14393. |
| [GetSystemTimeAsFileTime](https://msdn.microsoft.com/en-us/library/windows/desktop/ms724397.aspx) | Introduced into api-ms-win-core-sysinfo-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-sysinfo-l1-2-3.dll in 10.0.10586. Moved into api-ms-win-core-sysinfo-l1-2-1.dll in 10.0.14393. |
| [GetSystemTimePreciseAsFileTime](https://msdn.microsoft.com/en-us/library/windows/desktop/hh706895.aspx) | Introduced into api-ms-win-core-sysinfo-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-sysinfo-l1-2-3.dll in 10.0.10586. Moved into api-ms-win-core-sysinfo-l1-2-1.dll in 10.0.14393. |
| [GetTickCount64](https://msdn.microsoft.com/en-us/library/windows/desktop/ms724411.aspx) | Introduced into api-ms-win-core-sysinfo-l1-2-1.dll in 10.0.10240. Moved into api-ms-win-core-sysinfo-l1-2-3.dll in 10.0.10586. Moved into api-ms-win-core-sysinfo-l1-2-1.dll in 10.0.14393. |
| [GetLogicalProcessorInformation](https://msdn.microsoft.com/en-us/library/windows/desktop/ms683194.aspx) | Introduced into api-ms-win-core-sysinfo-l1-2-1.dll in 10.0.14393. |
| [GetLogicalProcessorInformationEx](https://msdn.microsoft.com/en-us/library/windows/desktop/dd405488.aspx) | Introduced into api-ms-win-core-sysinfo-l1-2-1.dll in 10.0.14393. |
| [GlobalMemoryStatusEx](https://msdn.microsoft.com/en-us/library/windows/desktop/aa366589.aspx) | Introduced into api-ms-win-core-sysinfo-l1-2-1.dll in 10.0.14393. |
| [GetTickCount](https://msdn.microsoft.com/en-us/library/ms724408.aspx) | Introduced into api-ms-win-core-sysinfo-l1-2-1.dll in 10.0.15063. |


## APIs from api-ms-win-core-sysinfo-l1-2-3.dll

| API | Requirements |
| -----| --------------|
| [GetIntegratedDisplaySize](https://msdn.microsoft.com/en-us/library/windows/desktop/dn904185.aspx) | Introduced into api-ms-win-core-sysinfo-l1-2-3.dll in 10.0.10240. |


## APIs from api-ms-win-core-threadpool-l1-2-0.dll

| API | Requirements |
| -----| --------------|
| [CallbackMayRunLong](https://msdn.microsoft.com/en-us/library/windows/desktop/ms681981.aspx) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [CancelThreadpoolIo](https://msdn.microsoft.com/en-us/library/windows/desktop/ms681983.aspx) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [CloseThreadpool](https://msdn.microsoft.com/en-us/library/windows/desktop/ms682030.aspx) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [CloseThreadpoolCleanupGroup](https://msdn.microsoft.com/en-us/library/windows/desktop/ms682033.aspx) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [CloseThreadpoolCleanupGroupMembers](https://msdn.microsoft.com/en-us/library/windows/desktop/ms682036.aspx) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [CloseThreadpoolIo](https://msdn.microsoft.com/en-us/library/windows/desktop/ms682038.aspx) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [CloseThreadpoolTimer](https://msdn.microsoft.com/en-us/library/windows/desktop/ms682040.aspx) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [CloseThreadpoolWait](https://msdn.microsoft.com/en-us/library/windows/desktop/ms682042.aspx) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [CloseThreadpoolWork](https://msdn.microsoft.com/en-us/library/windows/desktop/ms682043.aspx) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [CreateThreadpool](https://msdn.microsoft.com/en-us/library/windows/desktop/ms682456.aspx) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [CreateThreadpoolCleanupGroup](https://msdn.microsoft.com/en-us/library/windows/desktop/ms682462.aspx) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [CreateThreadpoolIo](https://msdn.microsoft.com/en-us/library/windows/desktop/ms682464.aspx) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [CreateThreadpoolTimer](https://msdn.microsoft.com/en-us/library/windows/desktop/ms682466.aspx) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [CreateThreadpoolWait](https://msdn.microsoft.com/en-us/library/windows/desktop/ms682474.aspx) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [CreateThreadpoolWork](https://msdn.microsoft.com/en-us/library/windows/desktop/ms682478.aspx) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [DisassociateCurrentThreadFromCallback](https://msdn.microsoft.com/en-us/library/windows/desktop/ms682581.aspx) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [FreeLibraryWhenCallbackReturns](https://msdn.microsoft.com/en-us/library/windows/desktop/ms683154.aspx) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [IsThreadpoolTimerSet](https://msdn.microsoft.com/en-us/library/windows/desktop/ms684133.aspx) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [LeaveCriticalSectionWhenCallbackReturns](https://msdn.microsoft.com/en-us/library/windows/desktop/ms684171.aspx) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [QueryThreadpoolStackInformation](https://msdn.microsoft.com/en-us/library/windows/desktop/dd405508.aspx) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [ReleaseMutexWhenCallbackReturns](https://msdn.microsoft.com/en-us/library/windows/desktop/ms685070.aspx) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [ReleaseSemaphoreWhenCallbackReturns](https://msdn.microsoft.com/en-us/library/windows/desktop/ms685073.aspx) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [SetEventWhenCallbackReturns](https://msdn.microsoft.com/en-us/library/windows/desktop/ms686214.aspx) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [SetThreadpoolStackInformation](https://msdn.microsoft.com/en-us/library/windows/desktop/dd405520.aspx) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [SetThreadpoolThreadMaximum](https://msdn.microsoft.com/en-us/library/windows/desktop/ms686266.aspx) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [SetThreadpoolThreadMinimum](https://msdn.microsoft.com/en-us/library/windows/desktop/ms686268.aspx) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [SetThreadpoolTimer](https://msdn.microsoft.com/en-us/library/windows/desktop/ms686271.aspx) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [SetThreadpoolTimerEx](https://msdn.microsoft.com/en-us/library/windows/desktop/dn894018.aspx) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [SetThreadpoolWait](https://msdn.microsoft.com/en-us/library/windows/desktop/ms686273.aspx) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [SetThreadpoolWaitEx](https://msdn.microsoft.com/en-us/library/windows/desktop/mt186618.aspx) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [StartThreadpoolIo](https://msdn.microsoft.com/en-us/library/windows/desktop/ms686326.aspx) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [SubmitThreadpoolWork](https://msdn.microsoft.com/en-us/library/windows/desktop/ms686338.aspx) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [TrySubmitThreadpoolCallback](https://msdn.microsoft.com/en-us/library/windows/desktop/ms686862.aspx) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [WaitForThreadpoolIoCallbacks](https://msdn.microsoft.com/en-us/library/windows/desktop/ms687038.aspx) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [WaitForThreadpoolTimerCallbacks](https://msdn.microsoft.com/en-us/library/windows/desktop/ms687042.aspx) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [WaitForThreadpoolWaitCallbacks](https://msdn.microsoft.com/en-us/library/windows/desktop/ms687047.aspx) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |
| [WaitForThreadpoolWorkCallbacks](https://msdn.microsoft.com/en-us/library/windows/desktop/ms687053.aspx) | Introduced into api-ms-win-core-threadpool-l1-2-0.dll in 10.0.10240. |


## APIs from api-ms-win-core-timezone-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [EnumDynamicTimeZoneInformation](https://msdn.microsoft.com/en-us/library/windows/desktop/hh706893.aspx) | Introduced into api-ms-win-core-timezone-l1-1-0.dll in 10.0.10240. |
| [FileTimeToSystemTime](https://msdn.microsoft.com/en-us/library/windows/desktop/ms724280.aspx) | Introduced into api-ms-win-core-timezone-l1-1-0.dll in 10.0.10240. |
| [GetDynamicTimeZoneInformation](https://msdn.microsoft.com/en-us/library/windows/desktop/ms724318.aspx) | Introduced into api-ms-win-core-timezone-l1-1-0.dll in 10.0.10240. |
| [GetDynamicTimeZoneInformationEffectiveYears](https://msdn.microsoft.com/en-us/library/windows/desktop/hh706894.aspx) | Introduced into api-ms-win-core-timezone-l1-1-0.dll in 10.0.10240. |
| [GetTimeZoneInformation](https://msdn.microsoft.com/en-us/library/windows/desktop/ms724421.aspx) | Introduced into api-ms-win-core-timezone-l1-1-0.dll in 10.0.10240. |
| [GetTimeZoneInformationForYear](https://msdn.microsoft.com/en-us/library/windows/desktop/bb540851.aspx) | Introduced into api-ms-win-core-timezone-l1-1-0.dll in 10.0.10240. |
| [SystemTimeToFileTime](https://msdn.microsoft.com/en-us/library/windows/desktop/ms724948.aspx) | Introduced into api-ms-win-core-timezone-l1-1-0.dll in 10.0.10240. |
| [SystemTimeToTzSpecificLocalTime](https://msdn.microsoft.com/en-us/library/windows/desktop/ms724949.aspx) | Introduced into api-ms-win-core-timezone-l1-1-0.dll in 10.0.10240. |
| [SystemTimeToTzSpecificLocalTimeEx](https://msdn.microsoft.com/en-us/library/windows/desktop/jj206642.aspx) | Introduced into api-ms-win-core-timezone-l1-1-0.dll in 10.0.10240. |
| [TzSpecificLocalTimeToSystemTime](https://msdn.microsoft.com/en-us/library/windows/desktop/ms725485.aspx) | Introduced into api-ms-win-core-timezone-l1-1-0.dll in 10.0.10240. |
| [TzSpecificLocalTimeToSystemTimeEx](https://msdn.microsoft.com/en-us/library/windows/desktop/jj206643.aspx) | Introduced into api-ms-win-core-timezone-l1-1-0.dll in 10.0.10240. |


## APIs from api-ms-win-core-util-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [DecodePointer](https://msdn.microsoft.com/en-us/library/windows/desktop/bb432242.aspx) | Introduced into api-ms-win-core-util-l1-1-0.dll in 10.0.10240. Moved into api-ms-win-core-util-l1-1-1.dll in 10.0.10586. Moved into api-ms-win-core-util-l1-1-0.dll in 10.0.14393. |
| [EncodePointer](https://msdn.microsoft.com/en-us/library/windows/desktop/bb432254.aspx) | Introduced into api-ms-win-core-util-l1-1-0.dll in 10.0.10240. Moved into api-ms-win-core-util-l1-1-1.dll in 10.0.10586. Moved into api-ms-win-core-util-l1-1-0.dll in 10.0.14393. |


## APIs from api-ms-win-core-windowsceip-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [CeipIsOptedIn](https://msdn.microsoft.com/en-us/library/windows/desktop/dn482415.aspx) | Introduced into api-ms-win-core-windowsceip-l1-1-0.dll in 10.0.10240. |


## APIs from api-ms-win-core-windowserrorreporting-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [WerRegisterFile](https://msdn.microsoft.com/en-us/library/windows/desktop/bb513619.aspx) | Introduced into api-ms-win-core-windowserrorreporting-l1-1-0.dll in 10.0.10240. |
| [WerRegisterMemoryBlock](https://msdn.microsoft.com/en-us/library/windows/desktop/bb513620.aspx) | Introduced into api-ms-win-core-windowserrorreporting-l1-1-0.dll in 10.0.10240. |
| [WerUnregisterFile](https://msdn.microsoft.com/en-us/library/windows/desktop/bb513630.aspx) | Introduced into api-ms-win-core-windowserrorreporting-l1-1-0.dll in 10.0.10240. |
| [WerUnregisterMemoryBlock](https://msdn.microsoft.com/en-us/library/windows/desktop/bb513631.aspx) | Introduced into api-ms-win-core-windowserrorreporting-l1-1-0.dll in 10.0.10240. |


## APIs from api-ms-win-core-winrt-error-l1-1-1.dll

| API | Requirements |
| -----| --------------|
| [GetRestrictedErrorInfo](https://msdn.microsoft.com/en-us/library/windows/desktop/jj219013.aspx) | Introduced into api-ms-win-core-winrt-error-l1-1-1.dll in 10.0.10240. |
| [RoCaptureErrorContext](https://msdn.microsoft.com/en-us/library/windows/desktop/jj219014.aspx) | Introduced into api-ms-win-core-winrt-error-l1-1-1.dll in 10.0.10240. |
| [RoFailFastWithErrorContext](https://msdn.microsoft.com/en-us/library/windows/desktop/jj219015.aspx) | Introduced into api-ms-win-core-winrt-error-l1-1-1.dll in 10.0.10240. |
| [RoGetErrorReportingFlags](https://msdn.microsoft.com/en-us/library/windows/desktop/br224649.aspx) | Introduced into api-ms-win-core-winrt-error-l1-1-1.dll in 10.0.10240. |
| [RoOriginateError](https://msdn.microsoft.com/en-us/library/windows/desktop/br224651.aspx) | Introduced into api-ms-win-core-winrt-error-l1-1-1.dll in 10.0.10240. |
| [RoOriginateErrorW](https://msdn.microsoft.com/en-us/library/windows/desktop/br224652.aspx) | Introduced into api-ms-win-core-winrt-error-l1-1-1.dll in 10.0.10240. |
| [RoOriginateLanguageException](https://msdn.microsoft.com/en-us/library/windows/desktop/dn302172.aspx) | Introduced into api-ms-win-core-winrt-error-l1-1-1.dll in 10.0.10240. |
| [RoReportUnhandledError](https://msdn.microsoft.com/en-us/library/windows/desktop/dn457328.aspx) | Introduced into api-ms-win-core-winrt-error-l1-1-1.dll in 10.0.10240. |
| [RoSetErrorReportingFlags](https://msdn.microsoft.com/en-us/library/windows/desktop/br224657.aspx) | Introduced into api-ms-win-core-winrt-error-l1-1-1.dll in 10.0.10240. |
| [RoTransformError](https://msdn.microsoft.com/en-us/library/windows/desktop/br224658.aspx) | Introduced into api-ms-win-core-winrt-error-l1-1-1.dll in 10.0.10240. |
| [RoTransformErrorW](https://msdn.microsoft.com/en-us/library/windows/desktop/br224659.aspx) | Introduced into api-ms-win-core-winrt-error-l1-1-1.dll in 10.0.10240. |
| [SetRestrictedErrorInfo](https://msdn.microsoft.com/en-us/library/windows/desktop/jj219016.aspx) | Introduced into api-ms-win-core-winrt-error-l1-1-1.dll in 10.0.10240. |


## APIs from api-ms-win-core-winrt-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [RoActivateInstance](https://msdn.microsoft.com/en-us/library/windows/desktop/br224646.aspx) | Introduced into api-ms-win-core-winrt-l1-1-0.dll in 10.0.10240. |
| [RoGetActivationFactory](https://msdn.microsoft.com/en-us/library/windows/desktop/br224648.aspx) | Introduced into api-ms-win-core-winrt-l1-1-0.dll in 10.0.10240. |
| [RoGetApartmentIdentifier](https://msdn.microsoft.com/en-us/library/windows/desktop/jj219266.aspx) | Introduced into api-ms-win-core-winrt-l1-1-0.dll in 10.0.10240. |
| [RoInitialize](https://msdn.microsoft.com/en-us/library/windows/desktop/br224650.aspx) | Introduced into api-ms-win-core-winrt-l1-1-0.dll in 10.0.10240. |
| [RoRegisterActivationFactories](https://msdn.microsoft.com/en-us/library/windows/desktop/br224653.aspx) | Introduced into api-ms-win-core-winrt-l1-1-0.dll in 10.0.10240. |
| [RoRegisterForApartmentShutdown](https://msdn.microsoft.com/en-us/library/windows/desktop/jj219267.aspx) | Introduced into api-ms-win-core-winrt-l1-1-0.dll in 10.0.10240. |
| [RoRevokeActivationFactories](https://msdn.microsoft.com/en-us/library/windows/desktop/br224655.aspx) | Introduced into api-ms-win-core-winrt-l1-1-0.dll in 10.0.10240. |
| [RoUninitialize](https://msdn.microsoft.com/en-us/library/windows/desktop/br224660.aspx) | Introduced into api-ms-win-core-winrt-l1-1-0.dll in 10.0.10240. |
| [RoUnregisterForApartmentShutdown](https://msdn.microsoft.com/en-us/library/windows/desktop/jj219268.aspx) | Introduced into api-ms-win-core-winrt-l1-1-0.dll in 10.0.10240. |


## APIs from api-ms-win-core-winrt-registration-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [RoGetActivatableClassRegistration](https://msdn.microsoft.com/en-us/library/windows/desktop/br229855.aspx) | Introduced into api-ms-win-core-winrt-registration-l1-1-0.dll in 10.0.10240. |
| [RoGetServerActivatableClasses](https://msdn.microsoft.com/en-us/library/windows/desktop/br229858.aspx) | Introduced into api-ms-win-core-winrt-registration-l1-1-0.dll in 10.0.10240. |


## APIs from api-ms-win-core-winrt-robuffer-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [RoGetBufferMarshaler](https://msdn.microsoft.com/en-us/library/windows/desktop/hh438433.aspx) | Introduced into api-ms-win-core-winrt-robuffer-l1-1-0.dll in 10.0.10240. |


## APIs from api-ms-win-core-winrt-roparameterizediid-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [RoFreeParameterizedTypeExtra](https://msdn.microsoft.com/en-us/library/windows/desktop/br229854.aspx) | Introduced into api-ms-win-core-winrt-roparameterizediid-l1-1-0.dll in 10.0.10240. |
| [RoGetParameterizedTypeInstanceIID](https://msdn.microsoft.com/en-us/library/windows/desktop/br229857.aspx) | Introduced into api-ms-win-core-winrt-roparameterizediid-l1-1-0.dll in 10.0.10240. |
| [RoParameterizedTypeExtraGetTypeSignature](https://msdn.microsoft.com/en-us/library/windows/desktop/br229859.aspx) | Introduced into api-ms-win-core-winrt-roparameterizediid-l1-1-0.dll in 10.0.10240. |


## APIs from api-ms-win-core-winrt-string-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [HSTRING_UserFree](https://msdn.microsoft.com/en-us/library/windows/desktop/hh846259.aspx) | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.10240. Moved into api-ms-win-core-winrt-string-l1-1-1.dll in 10.0.10586. Moved into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.14393. |
| [HSTRING_UserFree64](https://msdn.microsoft.com/en-us/library/windows/desktop/hh846260.aspx) | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.10240. Moved into api-ms-win-core-winrt-string-l1-1-1.dll in 10.0.10586. Moved into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.14393. Moved into api-ms-win-core-winrt-string-l1-1-1.dll in 10.0.15063. |
| [HSTRING_UserMarshal](https://msdn.microsoft.com/en-us/library/windows/desktop/hh846261.aspx) | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.10240. Moved into api-ms-win-core-winrt-string-l1-1-1.dll in 10.0.10586. Moved into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.14393. |
| [HSTRING_UserMarshal64](https://msdn.microsoft.com/en-us/library/windows/desktop/hh846262.aspx) | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.10240. Moved into api-ms-win-core-winrt-string-l1-1-1.dll in 10.0.10586. Moved into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.14393. Moved into api-ms-win-core-winrt-string-l1-1-1.dll in 10.0.15063. |
| [HSTRING_UserSize](https://msdn.microsoft.com/en-us/library/windows/desktop/hh846263.aspx) | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.10240. Moved into api-ms-win-core-winrt-string-l1-1-1.dll in 10.0.10586. Moved into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.14393. |
| [HSTRING_UserSize64](https://msdn.microsoft.com/en-us/library/windows/desktop/hh846264.aspx) | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.10240. Moved into api-ms-win-core-winrt-string-l1-1-1.dll in 10.0.10586. Moved into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.14393. Moved into api-ms-win-core-winrt-string-l1-1-1.dll in 10.0.15063. |
| [HSTRING_UserUnmarshal](https://msdn.microsoft.com/en-us/library/windows/desktop/hh846265.aspx) | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.10240. Moved into api-ms-win-core-winrt-string-l1-1-1.dll in 10.0.10586. Moved into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.14393. |
| [HSTRING_UserUnmarshal64](https://msdn.microsoft.com/en-us/library/windows/desktop/hh846266.aspx) | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.10240. Moved into api-ms-win-core-winrt-string-l1-1-1.dll in 10.0.10586. Moved into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.14393. Moved into api-ms-win-core-winrt-string-l1-1-1.dll in 10.0.15063. |
| [WindowsCompareStringOrdinal](https://msdn.microsoft.com/en-us/library/windows/desktop/br224628.aspx) | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.10240. Moved into api-ms-win-core-winrt-string-l1-1-1.dll in 10.0.10586. Moved into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.14393. |
| [WindowsConcatString](https://msdn.microsoft.com/en-us/library/windows/desktop/br224629.aspx) | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.10240. Moved into api-ms-win-core-winrt-string-l1-1-1.dll in 10.0.10586. Moved into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.14393. |
| [WindowsCreateString](https://msdn.microsoft.com/en-us/library/windows/desktop/br224630.aspx) | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.10240. Moved into api-ms-win-core-winrt-string-l1-1-1.dll in 10.0.10586. Moved into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.14393. |
| [WindowsCreateStringReference](https://msdn.microsoft.com/en-us/library/windows/desktop/br224631.aspx) | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.10240. Moved into api-ms-win-core-winrt-string-l1-1-1.dll in 10.0.10586. Moved into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.14393. |
| [WindowsDeleteString](https://msdn.microsoft.com/en-us/library/windows/desktop/br224632.aspx) | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.10240. Moved into api-ms-win-core-winrt-string-l1-1-1.dll in 10.0.10586. Moved into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.14393. |
| [WindowsDeleteStringBuffer](https://msdn.microsoft.com/en-us/library/windows/desktop/br224633.aspx) | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.10240. Moved into api-ms-win-core-winrt-string-l1-1-1.dll in 10.0.10586. Moved into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.14393. |
| [WindowsDuplicateString](https://msdn.microsoft.com/en-us/library/windows/desktop/br224634.aspx) | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.10240. Moved into api-ms-win-core-winrt-string-l1-1-1.dll in 10.0.10586. Moved into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.14393. |
| [WindowsGetStringLen](https://msdn.microsoft.com/en-us/library/windows/desktop/br224635.aspx) | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.10240. Moved into api-ms-win-core-winrt-string-l1-1-1.dll in 10.0.10586. Moved into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.14393. |
| [WindowsGetStringRawBuffer](https://msdn.microsoft.com/en-us/library/windows/desktop/br224636.aspx) | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.10240. Moved into api-ms-win-core-winrt-string-l1-1-1.dll in 10.0.10586. Moved into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.14393. |
| [WindowsIsStringEmpty](https://msdn.microsoft.com/en-us/library/windows/desktop/br224637.aspx) | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.10240. Moved into api-ms-win-core-winrt-string-l1-1-1.dll in 10.0.10586. Moved into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.14393. |
| [WindowsPreallocateStringBuffer](https://msdn.microsoft.com/en-us/library/windows/desktop/br224638.aspx) | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.10240. Moved into api-ms-win-core-winrt-string-l1-1-1.dll in 10.0.10586. Moved into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.14393. |
| [WindowsPromoteStringBuffer](https://msdn.microsoft.com/en-us/library/windows/desktop/br224639.aspx) | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.10240. Moved into api-ms-win-core-winrt-string-l1-1-1.dll in 10.0.10586. Moved into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.14393. |
| [WindowsReplaceString](https://msdn.microsoft.com/en-us/library/windows/desktop/br224640.aspx) | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.10240. Moved into api-ms-win-core-winrt-string-l1-1-1.dll in 10.0.10586. Moved into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.14393. |
| [WindowsStringHasEmbeddedNull](https://msdn.microsoft.com/en-us/library/windows/desktop/br224641.aspx) | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.10240. Moved into api-ms-win-core-winrt-string-l1-1-1.dll in 10.0.10586. Moved into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.14393. |
| [WindowsSubstring](https://msdn.microsoft.com/en-us/library/windows/desktop/br224642.aspx) | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.10240. Moved into api-ms-win-core-winrt-string-l1-1-1.dll in 10.0.10586. Moved into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.14393. |
| [WindowsSubstringWithSpecifiedLength](https://msdn.microsoft.com/en-us/library/windows/desktop/br224643.aspx) | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.10240. Moved into api-ms-win-core-winrt-string-l1-1-1.dll in 10.0.10586. Moved into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.14393. |
| [WindowsTrimStringEnd](https://msdn.microsoft.com/en-us/library/windows/desktop/br224644.aspx) | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.10240. Moved into api-ms-win-core-winrt-string-l1-1-1.dll in 10.0.10586. Moved into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.14393. |
| [WindowsTrimStringStart](https://msdn.microsoft.com/en-us/library/windows/desktop/br224645.aspx) | Introduced into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.10240. Moved into api-ms-win-core-winrt-string-l1-1-1.dll in 10.0.10586. Moved into api-ms-win-core-winrt-string-l1-1-0.dll in 10.0.14393. |


## APIs from api-ms-win-core-xstate-l2-1-0.dll

| API | Requirements |
| -----| --------------|
| [GetEnabledXStateFeatures](https://msdn.microsoft.com/en-us/library/windows/desktop/hh134235.aspx) | Introduced into api-ms-win-core-xstate-l2-1-0.dll in 10.0.10240. Removed in 10.0.10586. Moved into api-ms-win-core-xstate-l2-1-0.dll in 10.0.14393. |
| [GetXStateFeaturesMask](https://msdn.microsoft.com/en-us/library/windows/desktop/hh134236.aspx) | Introduced into api-ms-win-core-xstate-l2-1-0.dll in 10.0.10240. Removed in 10.0.10586. Moved into api-ms-win-core-xstate-l2-1-0.dll in 10.0.14393. |
| [InitializeContext](https://msdn.microsoft.com/en-us/library/windows/desktop/hh134237.aspx) | Introduced into api-ms-win-core-xstate-l2-1-0.dll in 10.0.10240. |
| [LocateXStateFeature](https://msdn.microsoft.com/en-us/library/windows/desktop/hh134238.aspx) | Introduced into api-ms-win-core-xstate-l2-1-0.dll in 10.0.10240. Removed in 10.0.10586. Moved into api-ms-win-core-xstate-l2-1-0.dll in 10.0.14393. |


## APIs from api-ms-win-eventing-classicprovider-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [GetTraceEnableFlags](https://msdn.microsoft.com/en-us/library/windows/desktop/aa363893.aspx) | Introduced into api-ms-win-eventing-classicprovider-l1-1-0.dll in 10.0.10240. |
| [GetTraceEnableLevel](https://msdn.microsoft.com/en-us/library/windows/desktop/aa363894.aspx) | Introduced into api-ms-win-eventing-classicprovider-l1-1-0.dll in 10.0.10240. |
| [GetTraceLoggerHandle](https://msdn.microsoft.com/en-us/library/windows/desktop/aa363897.aspx) | Introduced into api-ms-win-eventing-classicprovider-l1-1-0.dll in 10.0.10240. |
| [RegisterTraceGuidsW](https://msdn.microsoft.com/en-us/library/windows/desktop/aa364105.aspx) | Introduced into api-ms-win-eventing-classicprovider-l1-1-0.dll in 10.0.10240. |
| [TraceMessage](https://msdn.microsoft.com/en-us/library/windows/desktop/aa364139.aspx) | Introduced into api-ms-win-eventing-classicprovider-l1-1-0.dll in 10.0.10240. |
| [UnregisterTraceGuids](https://msdn.microsoft.com/en-us/library/windows/desktop/aa364154.aspx) | Introduced into api-ms-win-eventing-classicprovider-l1-1-0.dll in 10.0.10240. |


## APIs from api-ms-win-eventing-consumer-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [CloseTrace](https://msdn.microsoft.com/en-us/library/windows/desktop/aa363686.aspx) | Introduced into api-ms-win-eventing-consumer-l1-1-0.dll in 10.0.10240. |
| [OpenTraceW](https://msdn.microsoft.com/en-us/library/windows/desktop/aa364089.aspx) | Introduced into api-ms-win-eventing-consumer-l1-1-0.dll in 10.0.10240. |
| [ProcessTrace](https://msdn.microsoft.com/en-us/library/windows/desktop/aa364093.aspx) | Introduced into api-ms-win-eventing-consumer-l1-1-0.dll in 10.0.10240. |


## APIs from api-ms-win-eventing-controller-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [ControlTraceW](https://msdn.microsoft.com/en-us/library/windows/desktop/aa363696.aspx) | Introduced into api-ms-win-eventing-controller-l1-1-0.dll in 10.0.10240. |
| [EnableTraceEx2](https://msdn.microsoft.com/en-us/library/windows/desktop/dd392305.aspx) | Introduced into api-ms-win-eventing-controller-l1-1-0.dll in 10.0.10240. |
| [StartTraceW](https://msdn.microsoft.com/en-us/library/windows/desktop/aa364117.aspx) | Introduced into api-ms-win-eventing-controller-l1-1-0.dll in 10.0.10240. |
| [StopTraceW](https://msdn.microsoft.com/en-us/library/windows/desktop/aa364119.aspx) | Introduced into api-ms-win-eventing-controller-l1-1-0.dll in 10.0.10240. |


## APIs from api-ms-win-eventing-legacy-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [EnableTrace](https://msdn.microsoft.com/en-us/library/windows/desktop/aa363710.aspx) | Introduced into api-ms-win-eventing-legacy-l1-1-0.dll in 10.0.10240. |
| [EnableTraceEx](https://msdn.microsoft.com/en-us/library/windows/desktop/aa363711.aspx) | Introduced into api-ms-win-eventing-legacy-l1-1-0.dll in 10.0.10240. |
| [FlushTraceW](https://msdn.microsoft.com/en-us/library/windows/desktop/aa363891.aspx) | Introduced into api-ms-win-eventing-legacy-l1-1-0.dll in 10.0.10240. |
| [QueryTraceW](https://msdn.microsoft.com/en-us/library/windows/desktop/aa364103.aspx) | Introduced into api-ms-win-eventing-legacy-l1-1-0.dll in 10.0.10240. |


## APIs from api-ms-win-eventing-provider-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [EventActivityIdControl](https://msdn.microsoft.com/en-us/library/windows/desktop/aa363720.aspx) | Introduced into api-ms-win-eventing-provider-l1-1-0.dll in 10.0.10240. |
| [EventRegister](https://msdn.microsoft.com/en-us/library/windows/desktop/aa363744.aspx) | Introduced into api-ms-win-eventing-provider-l1-1-0.dll in 10.0.10240. |
| [EventSetInformation](https://msdn.microsoft.com/en-us/library/windows/desktop/hh447256.aspx) | Introduced into api-ms-win-eventing-provider-l1-1-0.dll in 10.0.10240. |
| [EventUnregister](https://msdn.microsoft.com/en-us/library/windows/desktop/aa363749.aspx) | Introduced into api-ms-win-eventing-provider-l1-1-0.dll in 10.0.10240. |
| [EventWrite](https://msdn.microsoft.com/en-us/library/windows/desktop/aa363752.aspx) | Introduced into api-ms-win-eventing-provider-l1-1-0.dll in 10.0.10240. |
| [EventWriteEx](https://msdn.microsoft.com/en-us/library/windows/desktop/dd392307.aspx) | Introduced into api-ms-win-eventing-provider-l1-1-0.dll in 10.0.10240. |
| [EventWriteString](https://msdn.microsoft.com/en-us/library/windows/desktop/aa363750.aspx) | Introduced into api-ms-win-eventing-provider-l1-1-0.dll in 10.0.10240. |
| [EventWriteTransfer](https://msdn.microsoft.com/en-us/library/windows/desktop/aa363751.aspx) | Introduced into api-ms-win-eventing-provider-l1-1-0.dll in 10.0.10240. |


## APIs from api-ms-win-gaming-tcui-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [ProcessPendingGameUI](https://msdn.microsoft.com/en-us/library/Mt421171.aspx) | Introduced into api-ms-win-gaming-tcui-l1-1-0.dll in 10.0.10240. Removed in 10.0.10586. Moved into api-ms-win-gaming-tcui-l1-1-2.dll in 10.0.14393. Moved into api-ms-win-gaming-tcui-l1-1-3.dll in 10.0.15063. |
| [ShowChangeFriendRelationshipUI](https://msdn.microsoft.com/en-us/library/Mt421172.aspx) | Introduced into api-ms-win-gaming-tcui-l1-1-0.dll in 10.0.10240. Removed in 10.0.10586. Moved into api-ms-win-gaming-tcui-l1-1-2.dll in 10.0.14393. Moved into api-ms-win-gaming-tcui-l1-1-3.dll in 10.0.15063. |
| [ShowGameInviteUI](https://msdn.microsoft.com/en-us/library/Mt421173.aspx) | Introduced into api-ms-win-gaming-tcui-l1-1-0.dll in 10.0.10240. Removed in 10.0.10586. Moved into api-ms-win-gaming-tcui-l1-1-2.dll in 10.0.14393. Moved into api-ms-win-gaming-tcui-l1-1-3.dll in 10.0.15063. |
| [ShowPlayerPickerUI](https://msdn.microsoft.com/en-us/library/Mt421174.aspx) | Introduced into api-ms-win-gaming-tcui-l1-1-0.dll in 10.0.10240. Removed in 10.0.10586. Moved into api-ms-win-gaming-tcui-l1-1-2.dll in 10.0.14393. Moved into api-ms-win-gaming-tcui-l1-1-3.dll in 10.0.15063. |
| [ShowProfileCardUI](https://msdn.microsoft.com/en-us/library/Mt421175.aspx) | Introduced into api-ms-win-gaming-tcui-l1-1-0.dll in 10.0.10240. Removed in 10.0.10586. Moved into api-ms-win-gaming-tcui-l1-1-2.dll in 10.0.14393. Moved into api-ms-win-gaming-tcui-l1-1-3.dll in 10.0.15063. |
| [ShowTitleAchievementsUI](https://msdn.microsoft.com/en-us/library/Mt421176.aspx) | Introduced into api-ms-win-gaming-tcui-l1-1-0.dll in 10.0.10240. Removed in 10.0.10586. Moved into api-ms-win-gaming-tcui-l1-1-2.dll in 10.0.14393. Moved into api-ms-win-gaming-tcui-l1-1-3.dll in 10.0.15063. |
| [TryCancelPendingGameUI](https://msdn.microsoft.com/en-us/library/Mt421178.aspx) | Introduced into api-ms-win-gaming-tcui-l1-1-0.dll in 10.0.10240. Removed in 10.0.10586. Moved into api-ms-win-gaming-tcui-l1-1-2.dll in 10.0.14393. Moved into api-ms-win-gaming-tcui-l1-1-3.dll in 10.0.15063. |


## APIs from api-ms-win-ro-typeresolution-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [RoGetMetaDataFile](https://msdn.microsoft.com/en-us/library/windows/desktop/br229856.aspx) | Introduced into api-ms-win-ro-typeresolution-l1-1-0.dll in 10.0.10240. |
| [RoParseTypeName](https://msdn.microsoft.com/en-us/library/windows/desktop/hh438434.aspx) | Introduced into api-ms-win-ro-typeresolution-l1-1-0.dll in 10.0.10240. |
| [RoResolveNamespace](https://msdn.microsoft.com/en-us/library/windows/desktop/br229860.aspx) | Introduced into api-ms-win-ro-typeresolution-l1-1-0.dll in 10.0.10240. |


## APIs from api-ms-win-security-cryptoapi-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [CryptReleaseContext](https://msdn.microsoft.com/en-us/library/windows/desktop/aa380268.aspx) | Introduced into api-ms-win-security-cryptoapi-l1-1-0.dll in 10.0.10240. |


## APIs from api-ms-win-shcore-stream-winrt-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [CreateRandomAccessStreamOnFile](https://msdn.microsoft.com/en-us/library/windows/desktop/hh846256.aspx) | Introduced into api-ms-win-shcore-stream-winrt-l1-1-0.dll in 10.0.10240. |
| [CreateRandomAccessStreamOverStream](https://msdn.microsoft.com/en-us/library/windows/desktop/hh846257.aspx) | Introduced into api-ms-win-shcore-stream-winrt-l1-1-0.dll in 10.0.10240. |
| [CreateStreamOverRandomAccessStream](https://msdn.microsoft.com/en-us/library/windows/desktop/hh846258.aspx) | Introduced into api-ms-win-shcore-stream-winrt-l1-1-0.dll in 10.0.10240. |


## APIs from cabinet.dll

| API | Requirements |
| -----| --------------|
| [CloseCompressor](https://msdn.microsoft.com/en-us/library/windows/desktop/hh437542.aspx) | Introduced into cabinet.dll in 10.0.10240. |
| [CloseDecompressor](https://msdn.microsoft.com/en-us/library/windows/desktop/hh437545.aspx) | Introduced into cabinet.dll in 10.0.10240. |
| [Compress](https://msdn.microsoft.com/en-us/library/windows/desktop/hh437548.aspx) | Introduced into cabinet.dll in 10.0.10240. |
| [CreateCompressor](https://msdn.microsoft.com/en-us/library/windows/desktop/hh437570.aspx) | Introduced into cabinet.dll in 10.0.10240. |
| [CreateDecompressor](https://msdn.microsoft.com/en-us/library/windows/desktop/hh437573.aspx) | Introduced into cabinet.dll in 10.0.10240. |
| [Decompress](https://msdn.microsoft.com/en-us/library/windows/desktop/hh437576.aspx) | Introduced into cabinet.dll in 10.0.10240. |
| [FDICopy](https://msdn.microsoft.com/en-us/library/windows/desktop/bb432270.aspx) | Introduced into cabinet.dll in 10.0.10240. |
| [FDICreate](https://msdn.microsoft.com/en-us/library/windows/desktop/bb432271.aspx) | Introduced into cabinet.dll in 10.0.10240. |
| [FDIDestroy](https://msdn.microsoft.com/en-us/library/windows/desktop/bb432272.aspx) | Introduced into cabinet.dll in 10.0.10240. |
| [FDIIsCabinet](https://msdn.microsoft.com/en-us/library/windows/desktop/bb432273.aspx) | Introduced into cabinet.dll in 10.0.10240. |
| [QueryCompressorInformation](https://msdn.microsoft.com/en-us/library/windows/desktop/hh437578.aspx) | Introduced into cabinet.dll in 10.0.10240. |
| [QueryDecompressorInformation](https://msdn.microsoft.com/en-us/library/windows/desktop/hh437580.aspx) | Introduced into cabinet.dll in 10.0.10240. |
| [ResetCompressor](https://msdn.microsoft.com/en-us/library/windows/desktop/hh437583.aspx) | Introduced into cabinet.dll in 10.0.10240. |
| [ResetDecompressor](https://msdn.microsoft.com/en-us/library/windows/desktop/hh437586.aspx) | Introduced into cabinet.dll in 10.0.10240. |
| [SetCompressorInformation](https://msdn.microsoft.com/en-us/library/windows/desktop/hh437588.aspx) | Introduced into cabinet.dll in 10.0.10240. |
| [SetDecompressorInformation](https://msdn.microsoft.com/en-us/library/windows/desktop/hh437592.aspx) | Introduced into cabinet.dll in 10.0.10240. |


## APIs from chakra.dll

| API | Requirements |
| -----| --------------|
| [JsAddRef](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsAddRef-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsBooleanToBool](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsBooleanToBool-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsBoolToBoolean](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsBoolToBoolean-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsCallFunction](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsCallFunction-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsCollectGarbage](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsCollectGarbage-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsConstructObject](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsConstructObject-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsConvertValueToBoolean](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsConvertValueToBoolean-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsConvertValueToNumber](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsConvertValueToNumber-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsConvertValueToObject](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsConvertValueToObject-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsConvertValueToString](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsConvertValueToString-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsCreateArray](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsCreateArray-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsCreateArrayBuffer](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsCreateArrayBuffer-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsCreateContext](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsCreateContext-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsCreateDataView](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsCreateDataView-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsCreateError](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsCreateError-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsCreateExternalObject](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsCreateExternalObject-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsCreateFunction](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsCreateFunction-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsCreateNamedFunction](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsCreateNamedFunction-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsCreateObject](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsCreateObject-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsCreateRangeError](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsCreateRangeError-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsCreateReferenceError](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsCreateReferenceError-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsCreateRuntime](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsCreateRuntime-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsCreateSymbol](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsCreateSymbol-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsCreateSyntaxError](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsCreateSyntaxError-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsCreateTypedArray](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsCreateTypedArray-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsCreateTypeError](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsCreateTypeError-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsCreateURIError](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsCreateURIError-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsDefineProperty](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsDefineProperty-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsDeleteIndexedProperty](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsDeleteIndexedProperty-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsDeleteProperty](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsDeleteProperty-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsDisableRuntimeExecution](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsDisableRuntimeExecution-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsDisposeRuntime](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsDisposeRuntime-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsDoubleToNumber](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsDoubleToNumber-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsEnableRuntimeExecution](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsEnableRuntimeExecution-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsEquals](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsEquals-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsGetAndClearException](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsGetAndClearException-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsGetArrayBufferStorage](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsGetArrayBufferStorage-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsGetCurrentContext](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsGetCurrentContext-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsGetDataViewStorage](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsGetDataViewStorage-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsGetExtensionAllowed](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsGetExtensionAllowed-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsGetExternalData](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsGetExternalData-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsGetFalseValue](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsGetFalseValue-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsGetGlobalObject](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsGetGlobalObject-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsGetIndexedPropertiesExternalData](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsGetIndexedPropertiesExternalData-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsGetIndexedProperty](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsGetIndexedProperty-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsGetNullValue](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsGetNullValue-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsGetOwnPropertyDescriptor](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsGetOwnPropertyDescriptor-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsGetOwnPropertyNames](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsGetOwnPropertyNames-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsGetOwnPropertySymbols](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsGetOwnPropertySymbols-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsGetProperty](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsGetProperty-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsGetPropertyIdFromName](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsGetPropertyIdFromName-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsGetPropertyIdFromSymbol](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsGetPropertyIdFromSymbol-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsGetPropertyIdType](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsGetPropertyIdType-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsGetPropertyNameFromId](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsGetPropertyNameFromId-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsGetPrototype](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsGetPrototype-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsGetRuntime](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsGetRuntime-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsGetRuntimeMemoryLimit](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsGetRuntimeMemoryLimit-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsGetRuntimeMemoryUsage](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsGetRuntimeMemoryUsage-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsGetStringLength](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsGetStringLength-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsGetSymbolFromPropertyId](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsGetSymbolFromPropertyId-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsGetTrueValue](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsGetTrueValue-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsGetTypedArrayStorage](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsGetTypedArrayStorage-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsGetUndefinedValue](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsGetUndefinedValue-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsGetValueType](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsGetValueType-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsHasException](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsHasException-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsHasExternalData](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsHasExternalData-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsHasIndexedPropertiesExternalData](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsHasIndexedPropertiesExternalData-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsHasIndexedProperty](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsHasIndexedProperty-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsHasProperty](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsHasProperty-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsIdle](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsIdle-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsInspectableToObject](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsInspectableToObject-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsIntToNumber](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsIntToNumber-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsIsRuntimeExecutionDisabled](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsIsRuntimeExecutionDisabled-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsNumberToDouble](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsNumberToDouble-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsNumberToInt](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsNumberToInt-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsObjectToInspectable](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsObjectToInspectable-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsParseScript](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsParseScript-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsParseSerializedScript](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsParseSerializedScript-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsPointerToString](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsPointerToString-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsPreventExtension](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsPreventExtension-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsProjectWinRTNamespace](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsProjectWinRTNamespace-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsRelease](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsRelease-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsRunScript](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsRunScript-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsRunSerializedScript](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsRunSerializedScript-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsSerializeScript](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsSerializeScript-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsSetCurrentContext](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsSetCurrentContext-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsSetException](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsSetException-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsSetExternalData](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsSetExternalData-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsSetIndexedPropertiesToExternalData](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsSetIndexedPropertiesToExternalData-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsSetIndexedProperty](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsSetIndexedProperty-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsSetObjectBeforeCollectCallback](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsSetObjectBeforeCollectCallback-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsSetProjectionEnqueueCallback](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsSetProjectionEnqueueCallback-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsSetPromiseContinuationCallback](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsSetPromiseContinuationCallback-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsSetProperty](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsSetProperty-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsSetPrototype](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsSetPrototype-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsSetRuntimeBeforeCollectCallback](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsSetRuntimeBeforeCollectCallback-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsSetRuntimeMemoryAllocationCallback](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsSetRuntimeMemoryAllocationCallback-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsSetRuntimeMemoryLimit](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsSetRuntimeMemoryLimit-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsStartDebugging](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsStartDebugging-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsStrictEquals](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsStrictEquals-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsStringToPointer](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsStringToPointer-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsValueToVariant](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsValueToVariant-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsVariantToValue](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsVariantToValue-function) | Introduced into chakra.dll in 10.0.10240. |
| [JsGetContextData](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsGetContextData-function) | Introduced into chakra.dll in 10.0.10586. |
| [JsGetContextOfObject](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsGetContextOfObject-function) | Introduced into chakra.dll in 10.0.10586. |
| [JsGetTypedArrayInfo](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsGetTypedArrayInfo-function) | Introduced into chakra.dll in 10.0.10586. |
| [JsInstanceOf](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsInstanceOf-function) | Introduced into chakra.dll in 10.0.10586. |
| [JsParseSerializedScriptWithCallback](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsParseSerializedScriptWithCallback-function) | Introduced into chakra.dll in 10.0.10586. |
| [JsRunSerializedScriptWithCallback](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsRunSerializedScriptWithCallback-function) | Introduced into chakra.dll in 10.0.10586. |
| [JsSetContextData](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsSetContextData-function) | Introduced into chakra.dll in 10.0.10586. |
| [JsCreateExternalArrayBuffer](https://docs.microsoft.com/en-us/scripting/chakra-hosting/JsCreateExternalArrayBuffer-function) | Introduced into chakra.dll in 10.0.14393. |


## APIs from crypt32.dll

| API | Requirements |
| -----| --------------|
| [CertAddCertificateContextToStore](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376009.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertAddCertificateLinkToStore](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376010.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertAddCRLContextToStore](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376011.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertAddCRLLinkToStore](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376012.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertAddCTLContextToStore](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376013.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertAddCTLLinkToStore](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376014.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertAddEncodedCertificateToStore](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376015.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertAddEncodedCRLToStore](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376016.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertAddEncodedCTLToStore](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376017.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertAddSerializedElementToStore](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376021.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertAddStoreToCollection](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376022.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertCloseStore](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376026.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertCompareCertificate](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376027.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertCompareCertificateName](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376028.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertCompareIntegerBlob](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376029.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertControlStore](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376031.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertCreateCertificateChainEngine](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376032.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertCreateCertificateContext](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376033.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertCreateContext](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376035.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertCreateCRLContext](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376036.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertCreateCTLContext](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376037.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertCreateSelfSignCertificate](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376039.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertDeleteCertificateFromStore](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376040.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertDeleteCRLFromStore](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376041.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertDeleteCTLFromStore](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376042.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertDuplicateCertificateChain](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376044.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertDuplicateCertificateContext](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376045.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertDuplicateCRLContext](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376046.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertDuplicateCTLContext](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376047.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertDuplicateStore](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376048.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertEnumCertificateContextProperties](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376049.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertEnumCertificatesInStore](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376050.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertEnumCRLContextProperties](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376051.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertEnumCRLsInStore](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376052.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertEnumCTLContextProperties](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376053.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertEnumCTLsInStore](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376054.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertEnumPhysicalStore](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376055.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertEnumSystemStore](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376058.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertEnumSystemStoreLocation](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376060.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertFindAttribute](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376062.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertFindCertificateInCRL](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376063.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertFindCertificateInStore](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376064.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertFindCRLInStore](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376066.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertFindCTLInStore](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376067.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertFindExtension](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376068.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertFindRDNAttr](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376069.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertFindSubjectInCTL](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376071.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertFreeCertificateChain](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376073.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertFreeCertificateChainEngine](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376074.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertFreeCertificateChainList](https://msdn.microsoft.com/en-us/library/windows/desktop/dd433796.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertFreeCertificateContext](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376075.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertFreeCRLContext](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376076.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertFreeCTLContext](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376077.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertGetCertificateChain](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376078.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertGetCertificateContextProperty](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376079.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertGetCRLContextProperty](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376080.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertGetCRLFromStore](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376081.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertGetCTLContextProperty](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376082.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertGetEnhancedKeyUsage](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376083.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertGetIntendedKeyUsage](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376084.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertGetIssuerCertificateFromStore](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376085.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertGetNameStringA](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376086.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertGetNameStringW](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376086.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertGetPublicKeyLength](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376087.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertGetStoreProperty](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376089.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertGetSubjectCertificateFromStore](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376090.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertGetValidUsages](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376091.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertIsValidCRLForCertificate](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376552.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertNameToStrA](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376556.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertNameToStrW](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376556.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertOpenStore](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376559.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertRDNValueToStrA](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376561.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertRDNValueToStrW](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376561.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertRemoveStoreFromCollection](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376565.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertResyncCertificateChainEngine](https://msdn.microsoft.com/en-us/library/windows/desktop/mt270087.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertSaveStore](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376567.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertSelectCertificateChains](https://msdn.microsoft.com/en-us/library/windows/desktop/dd433797.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertSerializeCertificateStoreElement](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376569.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertSerializeCRLStoreElement](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376570.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertSerializeCTLStoreElement](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376571.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertSetCertificateContextProperty](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376573.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertSetCRLContextProperty](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376574.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertSetCTLContextProperty](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376575.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertSetStoreProperty](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376577.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertStrToNameA](https://msdn.microsoft.com/en-us/library/Aa377160.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertStrToNameW](https://msdn.microsoft.com/en-us/library/Aa377160.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertVerifyCertificateChainPolicy](https://msdn.microsoft.com/en-us/library/windows/desktop/aa377163.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertVerifySubjectCertificateContext](https://msdn.microsoft.com/en-us/library/windows/desktop/aa377168.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CertVerifyTimeValidity](https://msdn.microsoft.com/en-us/library/windows/desktop/aa377169.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptAcquireCertificatePrivateKey](https://msdn.microsoft.com/en-us/library/windows/desktop/aa379885.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptDecodeObject](https://msdn.microsoft.com/en-us/library/windows/desktop/aa379911.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptDecodeObjectEx](https://msdn.microsoft.com/en-us/library/windows/desktop/aa379912.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptEncodeObject](https://msdn.microsoft.com/en-us/library/windows/desktop/aa379921.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptEncodeObjectEx](https://msdn.microsoft.com/en-us/library/windows/desktop/aa379922.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptEnumOIDFunction](https://msdn.microsoft.com/en-us/library/windows/desktop/aa379927.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptEnumOIDInfo](https://msdn.microsoft.com/en-us/library/windows/desktop/aa379928.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptFindLocalizedName](https://msdn.microsoft.com/en-us/library/windows/desktop/aa379937.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptFindOIDInfo](https://msdn.microsoft.com/en-us/library/windows/desktop/aa379938.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptFormatObject](https://msdn.microsoft.com/en-us/library/windows/desktop/aa379939.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptFreeOIDFunctionAddress](https://msdn.microsoft.com/en-us/library/windows/desktop/aa379940.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptGetDefaultOIDDllList](https://msdn.microsoft.com/en-us/library/windows/desktop/aa379943.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptGetDefaultOIDFunctionAddress](https://msdn.microsoft.com/en-us/library/windows/desktop/aa379944.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptGetOIDFunctionAddress](https://msdn.microsoft.com/en-us/library/windows/desktop/aa380088.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptGetOIDFunctionValue](https://msdn.microsoft.com/en-us/library/windows/desktop/aa380187.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptHashPublicKeyInfo](https://msdn.microsoft.com/en-us/library/windows/desktop/aa380204.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptInitOIDFunctionSet](https://msdn.microsoft.com/en-us/library/windows/desktop/aa380212.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptInstallOIDFunctionAddress](https://msdn.microsoft.com/en-us/library/windows/desktop/aa380214.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptMsgCalculateEncodedLength](https://msdn.microsoft.com/en-us/library/windows/desktop/aa380218.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptMsgClose](https://msdn.microsoft.com/en-us/library/windows/desktop/aa380219.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptMsgControl](https://msdn.microsoft.com/en-us/library/windows/desktop/aa380220.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptMsgCountersign](https://msdn.microsoft.com/en-us/library/windows/desktop/aa380221.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptMsgCountersignEncoded](https://msdn.microsoft.com/en-us/library/windows/desktop/aa380223.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptMsgDuplicate](https://msdn.microsoft.com/en-us/library/windows/desktop/aa380224.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptMsgGetAndVerifySigner](https://msdn.microsoft.com/en-us/library/windows/desktop/aa380226.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptMsgGetParam](https://msdn.microsoft.com/en-us/library/windows/desktop/aa380227.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptMsgOpenToDecode](https://msdn.microsoft.com/en-us/library/windows/desktop/aa380228.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptMsgOpenToEncode](https://msdn.microsoft.com/en-us/library/windows/desktop/aa380229.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptMsgUpdate](https://msdn.microsoft.com/en-us/library/windows/desktop/aa380231.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptMsgVerifyCountersignatureEncoded](https://msdn.microsoft.com/en-us/library/windows/desktop/aa380232.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptMsgVerifyCountersignatureEncodedEx](https://msdn.microsoft.com/en-us/library/windows/desktop/aa380233.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptProtectData](https://msdn.microsoft.com/en-us/library/windows/desktop/aa380261.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptQueryObject](https://msdn.microsoft.com/en-us/library/windows/desktop/aa380264.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptRetrieveTimeStamp](https://msdn.microsoft.com/en-us/library/windows/desktop/dd433803.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptUnprotectData](https://msdn.microsoft.com/en-us/library/windows/desktop/aa380882.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptVerifyTimeStampSignature](https://msdn.microsoft.com/en-us/library/windows/desktop/dd433804.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [PFXExportCertStore](https://msdn.microsoft.com/en-us/library/windows/desktop/aa387311.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [PFXExportCertStoreEx](https://msdn.microsoft.com/en-us/library/windows/desktop/aa387313.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [PFXImportCertStore](https://msdn.microsoft.com/en-us/library/windows/desktop/aa387314.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [PFXIsPFXBlob](https://msdn.microsoft.com/en-us/library/windows/desktop/aa387316.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [PFXVerifyPassword](https://msdn.microsoft.com/en-us/library/windows/desktop/aa387319.aspx) | Introduced into crypt32.dll in 10.0.10240. |
| [CryptImportPublicKeyInfoEx2](https://msdn.microsoft.com/en-us/library/Aa380211.aspx) | Introduced into crypt32.dll in 10.0.15063. |
| [CryptBinaryToStringW](https://msdn.microsoft.com/en-us/library/Aa379887.aspx) | Introduced into crypt32.dll in 10.0.15063. |
| [CryptProtectMemory](https://msdn.microsoft.com/en-us/library/Aa380262.aspx) | Introduced into crypt32.dll in 10.0.15063. |
| [CryptUnprotectMemory](https://msdn.microsoft.com/en-us/library/Aa380890.aspx) | Introduced into crypt32.dll in 10.0.15063. |
| [CryptHashCertificate2](https://msdn.microsoft.com/en-us/library/Aa380201.aspx) | Introduced into crypt32.dll in 10.0.15063. |
| [CryptStringToBinaryA](https://msdn.microsoft.com/en-us/library/Aa380285.aspx) | Introduced into crypt32.dll in 10.0.15063. |


## APIs from d2d1.dll

| API | Requirements |
| -----| --------------|
| [D2D1ComputeMaximumScaleFactor](https://msdn.microsoft.com/en-us/library/windows/desktop/dn280381.aspx) | Introduced into d2d1.dll in 10.0.10240. |
| [D2D1ConvertColorSpace](https://msdn.microsoft.com/en-us/library/windows/desktop/hh847939.aspx) | Introduced into d2d1.dll in 10.0.10240. |
| [D2D1CreateDevice](https://msdn.microsoft.com/en-us/library/windows/desktop/hh404272.aspx) | Introduced into d2d1.dll in 10.0.10240. |
| [D2D1CreateDeviceContext](https://msdn.microsoft.com/en-us/library/windows/desktop/hh404273.aspx) | Introduced into d2d1.dll in 10.0.10240. |
| [D2D1CreateFactory](https://msdn.microsoft.com/en-us/library/Dd368034.aspx) | Introduced into d2d1.dll in 10.0.10240. |
| [D2D1GetGradientMeshInteriorPointsFromCoonsPatch](https://msdn.microsoft.com/en-us/library/windows/desktop/mt149083.aspx) | Introduced into d2d1.dll in 10.0.10240. |
| [D2D1InvertMatrix](https://msdn.microsoft.com/en-us/library/windows/desktop/dd368044.aspx) | Introduced into d2d1.dll in 10.0.10240. |
| [D2D1IsMatrixInvertible](https://msdn.microsoft.com/en-us/library/windows/desktop/dd368045.aspx) | Introduced into d2d1.dll in 10.0.10240. |
| [D2D1MakeRotateMatrix](https://msdn.microsoft.com/en-us/library/windows/desktop/dd368049.aspx) | Introduced into d2d1.dll in 10.0.10240. |
| [D2D1MakeSkewMatrix](https://msdn.microsoft.com/en-us/library/windows/desktop/dd368052.aspx) | Introduced into d2d1.dll in 10.0.10240. |
| [D2D1SinCos](https://msdn.microsoft.com/en-us/library/windows/desktop/hh847940.aspx) | Introduced into d2d1.dll in 10.0.10240. |
| [D2D1Tan](https://msdn.microsoft.com/en-us/library/windows/desktop/hh847941.aspx) | Introduced into d2d1.dll in 10.0.10240. |
| [D2D1Vec3Length](https://msdn.microsoft.com/en-us/library/windows/desktop/hh847942.aspx) | Introduced into d2d1.dll in 10.0.10240. |


## APIs from d3d11.dll

| API | Requirements |
| -----| --------------|
| [CreateDirect3D11DeviceFromDXGIDevice](https://msdn.microsoft.com/en-us/library/Dn895087.aspx) | Introduced into d3d11.dll in 10.0.10240. |
| [CreateDirect3D11SurfaceFromDXGISurface](https://msdn.microsoft.com/en-us/library/Dn895088.aspx) | Introduced into d3d11.dll in 10.0.10240. |
| [D3D11CreateDevice](https://msdn.microsoft.com/en-us/library/windows/desktop/ff476082.aspx) | Introduced into d3d11.dll in 10.0.10240. |
| [D3D11On12CreateDevice](https://msdn.microsoft.com/en-us/library/Dn933209.aspx) | Introduced into d3d11.dll in 10.0.10240. |


## APIs from d3d12.dll

| API | Requirements |
| -----| --------------|
| [D3D12CreateDevice](https://msdn.microsoft.com/en-us/library/Dn770336.aspx) | Introduced into d3d12.dll in 10.0.10240. |
| [D3D12CreateRootSignatureDeserializer](https://msdn.microsoft.com/en-us/library/Dn859362.aspx) | Introduced into d3d12.dll in 10.0.10240. |
| [D3D12SerializeRootSignature](https://msdn.microsoft.com/en-us/library/Dn859363.aspx) | Introduced into d3d12.dll in 10.0.10240. |


## APIs from d3dcompiler_47.dll

| API | Requirements |
| -----| --------------|
| [D3DCompile](https://msdn.microsoft.com/en-us/library/windows/desktop/dd607324.aspx) | Introduced into d3dcompiler_47.dll in 10.0.10240. |
| [D3DCompile2](https://msdn.microsoft.com/en-us/library/windows/desktop/hh446869.aspx) | Introduced into d3dcompiler_47.dll in 10.0.10240. |
| [D3DCompileFromFile](https://msdn.microsoft.com/en-us/library/windows/desktop/hh446872.aspx) | Introduced into d3dcompiler_47.dll in 10.0.10240. |
| [D3DCompressShaders](https://msdn.microsoft.com/en-us/library/windows/desktop/ff728671.aspx) | Introduced into d3dcompiler_47.dll in 10.0.10240. |
| [D3DCreateBlob](https://msdn.microsoft.com/en-us/library/windows/desktop/ff728672.aspx) | Introduced into d3dcompiler_47.dll in 10.0.10240. |
| [D3DCreateFunctionLinkingGraph](https://msdn.microsoft.com/en-us/library/windows/desktop/dn280340.aspx) | Introduced into d3dcompiler_47.dll in 10.0.10240. |
| [D3DCreateLinker](https://msdn.microsoft.com/en-us/library/windows/desktop/dn280341.aspx) | Introduced into d3dcompiler_47.dll in 10.0.10240. |
| [D3DDecompressShaders](https://msdn.microsoft.com/en-us/library/windows/desktop/ff728673.aspx) | Introduced into d3dcompiler_47.dll in 10.0.10240. |
| [D3DDisassemble](https://msdn.microsoft.com/en-us/library/windows/desktop/dd607326.aspx) | Introduced into d3dcompiler_47.dll in 10.0.10240. |
| [D3DDisassemble11Trace](https://msdn.microsoft.com/en-us/library/windows/desktop/hh706343.aspx) | Introduced into d3dcompiler_47.dll in 10.0.10240. |
| [D3DDisassembleRegion](https://msdn.microsoft.com/en-us/library/windows/desktop/hh706344.aspx) | Introduced into d3dcompiler_47.dll in 10.0.10240. |
| [D3DGetBlobPart](https://msdn.microsoft.com/en-us/library/windows/desktop/ff728674.aspx) | Introduced into d3dcompiler_47.dll in 10.0.10240. |
| [D3DGetDebugInfo](https://msdn.microsoft.com/en-us/library/windows/desktop/dd607328.aspx) | Introduced into d3dcompiler_47.dll in 10.0.10240. |
| [D3DGetInputAndOutputSignatureBlob](https://msdn.microsoft.com/en-us/library/windows/desktop/dd607329.aspx) | Introduced into d3dcompiler_47.dll in 10.0.10240. |
| [D3DGetInputSignatureBlob](https://msdn.microsoft.com/en-us/library/windows/desktop/dd607330.aspx) | Introduced into d3dcompiler_47.dll in 10.0.10240. |
| [D3DGetOutputSignatureBlob](https://msdn.microsoft.com/en-us/library/windows/desktop/dd607331.aspx) | Introduced into d3dcompiler_47.dll in 10.0.10240. |
| [D3DGetTraceInstructionOffsets](https://msdn.microsoft.com/en-us/library/windows/desktop/hh446875.aspx) | Introduced into d3dcompiler_47.dll in 10.0.10240. |
| [D3DLoadModule](https://msdn.microsoft.com/en-us/library/windows/desktop/dn280342.aspx) | Introduced into d3dcompiler_47.dll in 10.0.10240. |
| [D3DPreprocess](https://msdn.microsoft.com/en-us/library/windows/desktop/dd607332.aspx) | Introduced into d3dcompiler_47.dll in 10.0.10240. |
| [D3DReadFileToBlob](https://msdn.microsoft.com/en-us/library/windows/desktop/hh446877.aspx) | Introduced into d3dcompiler_47.dll in 10.0.10240. |
| [D3DReflect](https://msdn.microsoft.com/en-us/library/windows/desktop/dd607334.aspx) | Introduced into d3dcompiler_47.dll in 10.0.10240. |
| [D3DReflectLibrary](https://msdn.microsoft.com/en-us/library/windows/desktop/dn280343.aspx) | Introduced into d3dcompiler_47.dll in 10.0.10240. |
| [D3DSetBlobPart](https://msdn.microsoft.com/en-us/library/windows/desktop/hh446880.aspx) | Introduced into d3dcompiler_47.dll in 10.0.10240. |
| [D3DStripShader](https://msdn.microsoft.com/en-us/library/windows/desktop/dd607335.aspx) | Introduced into d3dcompiler_47.dll in 10.0.10240. |
| [D3DWriteBlobToFile](https://msdn.microsoft.com/en-us/library/windows/desktop/hh446883.aspx) | Introduced into d3dcompiler_47.dll in 10.0.10240. |


## APIs from deviceaccess.dll

| API | Requirements |
| -----| --------------|
| [CreateDeviceAccessInstance](https://msdn.microsoft.com/en-us/library/windows/desktop/hh404237.aspx) | Introduced into deviceaccess.dll in 10.0.10240. |


## APIs from dhcpcsvc.dll

| API | Requirements |
| -----| --------------|
| [DhcpCApiCleanup](https://msdn.microsoft.com/en-us/library/windows/desktop/aa363272.aspx) | Introduced into dhcpcsvc.dll in 10.0.10240. |
| [DhcpCApiInitialize](https://msdn.microsoft.com/en-us/library/windows/desktop/aa363273.aspx) | Introduced into dhcpcsvc.dll in 10.0.10240. |
| [DhcpRequestParams](https://msdn.microsoft.com/en-us/library/windows/desktop/aa363298.aspx) | Introduced into dhcpcsvc.dll in 10.0.10240. |


## APIs from dhcpcsvc6.dll

| API | Requirements |
| -----| --------------|
| [Dhcpv6CApiCleanup](https://msdn.microsoft.com/en-us/library/windows/desktop/aa363305.aspx) | Introduced into dhcpcsvc6.dll in 10.0.10240. |
| [Dhcpv6CApiInitialize](https://msdn.microsoft.com/en-us/library/windows/desktop/aa363306.aspx) | Introduced into dhcpcsvc6.dll in 10.0.10240. |
| [Dhcpv6RequestParams](https://msdn.microsoft.com/en-us/library/windows/desktop/aa363327.aspx) | Introduced into dhcpcsvc6.dll in 10.0.10240. |


## APIs from dwrite.dll

| API | Requirements |
| -----| --------------|
| [DWriteCreateFactory](https://msdn.microsoft.com/en-us/library/windows/desktop/dd368040.aspx) | Introduced into dwrite.dll in 10.0.10240. |


## APIs from dxgi.dll

| API | Requirements |
| -----| --------------|
| [CreateDXGIFactory1](https://msdn.microsoft.com/en-us/library/windows/desktop/ff471318.aspx) | Introduced into dxgi.dll in 10.0.10240. |
| [CreateDXGIFactory2](https://msdn.microsoft.com/en-us/library/windows/desktop/dn268307.aspx) | Introduced into dxgi.dll in 10.0.10240. |


## APIs from esent.dll

| API | Requirements |
| -----| --------------|
| [JetAddColumnW](https://msdn.microsoft.com/en-us/library/windows/desktop/gg294122.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetAttachDatabase2W](https://msdn.microsoft.com/en-us/library/windows/desktop/gg269322.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetBackupInstanceW](https://msdn.microsoft.com/en-us/library/windows/desktop/gg269318.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetBeginSessionW](https://msdn.microsoft.com/en-us/library/windows/desktop/gg294131.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetBeginTransaction3](https://msdn.microsoft.com/en-us/library/windows/desktop/jj835043.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetCloseDatabase](https://msdn.microsoft.com/en-us/library/windows/desktop/gg294123.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetCloseTable](https://msdn.microsoft.com/en-us/library/windows/desktop/gg294087.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetCommitTransaction](https://msdn.microsoft.com/en-us/library/windows/desktop/gg269191.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetCommitTransaction2](https://msdn.microsoft.com/en-us/library/windows/desktop/jj835041.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetCreateDatabase2W](https://msdn.microsoft.com/en-us/library/windows/desktop/gg269208.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetCreateIndex4W](https://msdn.microsoft.com/en-us/library/windows/desktop/jj835044.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetCreateInstance2W](https://msdn.microsoft.com/en-us/library/windows/desktop/gg269202.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetCreateTableColumnIndex4W](https://msdn.microsoft.com/en-us/library/windows/desktop/jj835042.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetDefragment2W](https://msdn.microsoft.com/en-us/library/windows/desktop/gg294095.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetDelete](https://msdn.microsoft.com/en-us/library/windows/desktop/gg269315.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetDeleteColumn2W](https://msdn.microsoft.com/en-us/library/windows/desktop/gg269320.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetDeleteIndexW](https://msdn.microsoft.com/en-us/library/windows/desktop/gg294081.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetDeleteTableW](https://msdn.microsoft.com/en-us/library/windows/desktop/gg294128.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetDetachDatabase2W](https://msdn.microsoft.com/en-us/library/windows/desktop/gg294105.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetEndSession](https://msdn.microsoft.com/en-us/library/windows/desktop/gg294054.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetEnumerateColumns](https://msdn.microsoft.com/en-us/library/windows/desktop/gg269321.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetEscrowUpdate](https://msdn.microsoft.com/en-us/library/windows/desktop/gg294125.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetGetBookmark](https://msdn.microsoft.com/en-us/library/windows/desktop/gg269221.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetGetColumnInfoW](https://msdn.microsoft.com/en-us/library/windows/desktop/gg269215.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetGetCurrentIndexW](https://msdn.microsoft.com/en-us/library/windows/desktop/gg294041.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetGetDatabaseFileInfoW](https://msdn.microsoft.com/en-us/library/windows/desktop/gg269239.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetGetDatabaseInfoW](https://msdn.microsoft.com/en-us/library/windows/desktop/gg294076.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetGetErrorInfoW](https://msdn.microsoft.com/en-us/library/windows/desktop/hh475859.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetGetIndexInfoW](https://msdn.microsoft.com/en-us/library/windows/desktop/gg294084.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetGetObjectInfoW](https://msdn.microsoft.com/en-us/library/windows/desktop/gg269232.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetGetRecordPosition](https://msdn.microsoft.com/en-us/library/windows/desktop/gg269316.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetGetSecondaryIndexBookmark](https://msdn.microsoft.com/en-us/library/windows/desktop/gg269285.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetGetSessionParameter](https://msdn.microsoft.com/en-us/library/windows/desktop/jj835039.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetGetSystemParameterW](https://msdn.microsoft.com/en-us/library/windows/desktop/gg269291.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetGetTableColumnInfoW](https://msdn.microsoft.com/en-us/library/windows/desktop/gg294061.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetGetTableIndexInfoW](https://msdn.microsoft.com/en-us/library/windows/desktop/gg294102.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetGetTableInfoW](https://msdn.microsoft.com/en-us/library/windows/desktop/gg269177.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetGetThreadStats](https://msdn.microsoft.com/en-us/library/windows/desktop/gg269196.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetGotoBookmark](https://msdn.microsoft.com/en-us/library/windows/desktop/gg294053.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetGotoPosition](https://msdn.microsoft.com/en-us/library/windows/desktop/gg269300.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetGotoSecondaryIndexBookmark](https://msdn.microsoft.com/en-us/library/windows/desktop/gg269180.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetIndexRecordCount](https://msdn.microsoft.com/en-us/library/windows/desktop/gg269267.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetInit3W](https://msdn.microsoft.com/en-us/library/windows/desktop/gg269296.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetIntersectIndexes](https://msdn.microsoft.com/en-us/library/windows/desktop/gg269289.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetMakeKey](https://msdn.microsoft.com/en-us/library/windows/desktop/gg269329.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetMove](https://msdn.microsoft.com/en-us/library/windows/desktop/gg294117.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetOpenDatabaseW](https://msdn.microsoft.com/en-us/library/windows/desktop/gg269299.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetOpenTableW](https://msdn.microsoft.com/en-us/library/windows/desktop/gg294118.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetOpenTemporaryTable2](https://msdn.microsoft.com/en-us/library/windows/desktop/gg269302.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetOpenTempTable3](https://msdn.microsoft.com/en-us/library/windows/desktop/gg269255.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetPrepareUpdate](https://msdn.microsoft.com/en-us/library/windows/desktop/gg269339.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetPrereadIndexRanges](https://msdn.microsoft.com/en-us/library/windows/desktop/jj835045.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetPrereadKeys](https://msdn.microsoft.com/en-us/library/windows/desktop/gg294143.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetRegisterCallback](https://msdn.microsoft.com/en-us/library/windows/desktop/gg269175.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetRenameColumnW](https://msdn.microsoft.com/en-us/library/windows/desktop/gg269218.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetRenameTableW](https://msdn.microsoft.com/en-us/library/windows/desktop/gg294142.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetResetSessionContext](https://msdn.microsoft.com/en-us/library/windows/desktop/gg269250.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetResetTableSequential](https://msdn.microsoft.com/en-us/library/windows/desktop/gg269261.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetResizeDatabase](https://msdn.microsoft.com/en-us/library/windows/desktop/jj835047.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetRestoreInstanceW](https://msdn.microsoft.com/en-us/library/windows/desktop/gg269306.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetRetrieveColumn](https://msdn.microsoft.com/en-us/library/windows/desktop/gg269198.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetRetrieveColumns](https://msdn.microsoft.com/en-us/library/windows/desktop/gg294135.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetRetrieveKey](https://msdn.microsoft.com/en-us/library/windows/desktop/gg294051.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetRollback](https://msdn.microsoft.com/en-us/library/windows/desktop/gg269273.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetSeek](https://msdn.microsoft.com/en-us/library/windows/desktop/gg294103.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetSetColumn](https://msdn.microsoft.com/en-us/library/windows/desktop/gg294137.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetSetColumns](https://msdn.microsoft.com/en-us/library/windows/desktop/gg294050.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetSetCurrentIndex4W](https://msdn.microsoft.com/en-us/library/windows/desktop/gg269262.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetSetCursorFilter](https://msdn.microsoft.com/en-us/library/windows/desktop/jj835040.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetSetIndexRange](https://msdn.microsoft.com/en-us/library/windows/desktop/gg294112.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetSetSessionContext](https://msdn.microsoft.com/en-us/library/windows/desktop/gg294124.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetSetSessionParameter](https://msdn.microsoft.com/en-us/library/windows/desktop/jj835038.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetSetSystemParameterW](https://msdn.microsoft.com/en-us/library/windows/desktop/gg294044.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetSetTableSequential](https://msdn.microsoft.com/en-us/library/windows/desktop/gg269323.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetStopBackupInstance](https://msdn.microsoft.com/en-us/library/windows/desktop/gg269309.aspx) | Introduced into esent.dll in 10.0.10240. |
| JetStopServiceInstance2 | Introduced into esent.dll in 10.0.10240. |
| [JetTerm2](https://msdn.microsoft.com/en-us/library/windows/desktop/gg269223.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetUnregisterCallback](https://msdn.microsoft.com/en-us/library/windows/desktop/gg294116.aspx) | Introduced into esent.dll in 10.0.10240. |
| [JetUpdate2](https://msdn.microsoft.com/en-us/library/windows/desktop/gg269190.aspx) | Introduced into esent.dll in 10.0.10240. |


## APIs from hrtfapo.dll

| API | Requirements |
| -----| --------------|
| [CreateHrtfApo](https://msdn.microsoft.com/en-us/library/windows/desktop/mt186596.aspx) | Introduced into hrtfapo.dll in 10.0.10240. |


## APIs from mf.dll

| API | Requirements |
| -----| --------------|
| [MFCreateAggregateSource](https://msdn.microsoft.com/en-us/library/windows/desktop/dd388085.aspx) | Introduced into mf.dll in 10.0.10240. |
| [MFCreateProtectedEnvironmentAccess](https://msdn.microsoft.com/en-us/library/windows/desktop/hh162758.aspx) | Introduced into mf.dll in 10.0.10240. |
| [MFGetLocalId](https://msdn.microsoft.com/en-us/library/windows/desktop/jj128335.aspx) | Introduced into mf.dll in 10.0.10240. |
| [MFGetService](https://msdn.microsoft.com/en-us/library/windows/desktop/ms694284.aspx) | Introduced into mf.dll in 10.0.10240. |
| [MFGetSystemId](https://msdn.microsoft.com/en-us/library/windows/desktop/hh162767.aspx) | Introduced into mf.dll in 10.0.10240. |
| [MFLoadSignedLibrary](https://msdn.microsoft.com/en-us/library/windows/desktop/hh162769.aspx) | Introduced into mf.dll in 10.0.10240. |
| [MFCreatePresentationClock](https://msdn.microsoft.com/en-us/library/ms702174.aspx) | Introduced into mf.dll in 10.0.15063. |
| [MFCreateAudioRendererActivate](https://msdn.microsoft.com/en-us/library/ms702998.aspxh) | Introduced into mf.dll in 10.0.15063. |
| [MFCreatePMPMediaSession](https://msdn.microsoft.com/en-us/library/ms703144.aspx) | Introduced into mf.dll in 10.0.15063. |
| [MFCreateTopology](https://msdn.microsoft.com/en-us/library/ms701584.aspx) | Introduced into mf.dll in 10.0.15063. |
| [MFCreateTopologyNode](https://msdn.microsoft.com/en-us/library/ms697574.aspx) | Introduced into mf.dll in 10.0.15063. |


## APIs from mfplat.dll

| API | Requirements |
| -----| --------------|
| [MFAllocateSerialWorkQueue](https://msdn.microsoft.com/en-us/library/windows/desktop/hh162744.aspx) | Introduced into mfplat.dll in 10.0.10240. |
| [MFCancelWorkItem](https://msdn.microsoft.com/en-us/library/windows/desktop/ms701633.aspx) | Introduced into mfplat.dll in 10.0.10240. |
| [MFCopyImage](https://msdn.microsoft.com/en-us/library/windows/desktop/bb970554.aspx) | Introduced into mfplat.dll in 10.0.10240. |
| [MFCreate2DMediaBuffer](https://msdn.microsoft.com/en-us/library/windows/desktop/hh162746.aspx) | Introduced into mfplat.dll in 10.0.10240. |
| [MFCreateAlignedMemoryBuffer](https://msdn.microsoft.com/en-us/library/windows/desktop/bb970523.aspx) | Introduced into mfplat.dll in 10.0.10240. |
| [MFCreateAsyncResult](https://msdn.microsoft.com/en-us/library/windows/desktop/ms698952.aspx) | Introduced into mfplat.dll in 10.0.10240. |
| [MFCreateAttributes](https://msdn.microsoft.com/en-us/library/windows/desktop/ms701878.aspx) | Introduced into mfplat.dll in 10.0.10240. |
| [MFCreateCollection](https://msdn.microsoft.com/en-us/library/windows/desktop/ms698852.aspx) | Introduced into mfplat.dll in 10.0.10240. |
| [MFCreateContentDecryptorContext](https://msdn.microsoft.com/en-us/library/windows/desktop/mt219224.aspx) | Introduced into mfplat.dll in 10.0.10240. |
| [MFCreateContentProtectionDevice](https://msdn.microsoft.com/en-us/library/windows/desktop/mt219225.aspx) | Introduced into mfplat.dll in 10.0.10240. |
| [MFCreateDXGIDeviceManager](https://msdn.microsoft.com/en-us/library/windows/desktop/hh162750.aspx) | Introduced into mfplat.dll in 10.0.10240. |
| [MFCreateDXGISurfaceBuffer](https://msdn.microsoft.com/en-us/library/windows/desktop/hh162751.aspx) | Introduced into mfplat.dll in 10.0.10240. |
| [MFCreateEventQueue](https://msdn.microsoft.com/en-us/library/windows/desktop/ms695252.aspx) | Introduced into mfplat.dll in 10.0.10240. |
| [MFCreateMediaBufferFromMediaType](https://msdn.microsoft.com/en-us/library/windows/desktop/hh162752.aspx) | Introduced into mfplat.dll in 10.0.10240. |
| [MFCreateMediaBufferWrapper](https://msdn.microsoft.com/en-us/library/windows/desktop/aa370450.aspx) | Introduced into mfplat.dll in 10.0.10240. |
| [MFCreateMediaEvent](https://msdn.microsoft.com/en-us/library/windows/desktop/ms697521.aspx) | Introduced into mfplat.dll in 10.0.10240. |
| [MFCreateMediaExtensionActivate](https://msdn.microsoft.com/en-us/library/windows/desktop/hh162753.aspx) | Introduced into mfplat.dll in 10.0.10240. |
| [MFCreateMediaType](https://msdn.microsoft.com/en-us/library/windows/desktop/ms693861.aspx) | Introduced into mfplat.dll in 10.0.10240. |
| [MFCreateMediaTypeFromProperties](https://msdn.microsoft.com/en-us/library/windows/desktop/jj247579.aspx) | Introduced into mfplat.dll in 10.0.10240. |
| [MFCreateMemoryBuffer](https://msdn.microsoft.com/en-us/library/windows/desktop/ms695212.aspx) | Introduced into mfplat.dll in 10.0.10240. |
| [MFCreateMFByteStreamOnStreamEx](https://msdn.microsoft.com/en-us/library/windows/desktop/hh162754.aspx) | Introduced into mfplat.dll in 10.0.10240. |
| [MFCreatePresentationDescriptor](https://msdn.microsoft.com/en-us/library/windows/desktop/ms695404.aspx) | Introduced into mfplat.dll in 10.0.10240. |
| [MFCreatePropertiesFromMediaType](https://msdn.microsoft.com/en-us/library/windows/desktop/jj247580.aspx) | Introduced into mfplat.dll in 10.0.10240. |
| [MFCreateSample](https://msdn.microsoft.com/en-us/library/windows/desktop/ms702276.aspx) | Introduced into mfplat.dll in 10.0.10240. |
| [MFCreateSourceResolver](https://msdn.microsoft.com/en-us/library/windows/desktop/ms697433.aspx) | Introduced into mfplat.dll in 10.0.10240. |
| [MFCreateStreamDescriptor](https://msdn.microsoft.com/en-us/library/windows/desktop/ms698990.aspx) | Introduced into mfplat.dll in 10.0.10240. |
| [MFCreateStreamOnMFByteStreamEx](https://msdn.microsoft.com/en-us/library/windows/desktop/hh162760.aspx) | Introduced into mfplat.dll in 10.0.10240. |
| [MFCreateTrackedSample](https://msdn.microsoft.com/en-us/library/windows/desktop/hh162761.aspx) | Introduced into mfplat.dll in 10.0.10240. |
| [MFCreateVideoSampleAllocatorEx](https://msdn.microsoft.com/en-us/library/windows/desktop/hh162763.aspx) | Introduced into mfplat.dll in 10.0.10240. |
| [MFCreateWaveFormatExFromMFMediaType](https://msdn.microsoft.com/en-us/library/windows/desktop/ms702177.aspx) | Introduced into mfplat.dll in 10.0.10240. |
| [MFDeserializeAttributesFromStream](https://msdn.microsoft.com/en-us/library/windows/desktop/ms703162.aspx) | Introduced into mfplat.dll in 10.0.10240. |
| [MFGetAttributesAsBlob](https://msdn.microsoft.com/en-us/library/windows/desktop/ms694877.aspx) | Introduced into mfplat.dll in 10.0.10240. |
| [MFGetAttributesAsBlobSize](https://msdn.microsoft.com/en-us/library/windows/desktop/ms697064.aspx) | Introduced into mfplat.dll in 10.0.10240. |
| [MFGetSystemTime](https://msdn.microsoft.com/en-us/library/windows/desktop/ms704625.aspx) | Introduced into mfplat.dll in 10.0.10240. |
| [MFInitAttributesFromBlob](https://msdn.microsoft.com/en-us/library/windows/desktop/ms703978.aspx) | Introduced into mfplat.dll in 10.0.10240. |
| [MFInitMediaTypeFromWaveFormatEx](https://msdn.microsoft.com/en-us/library/windows/desktop/ms700801.aspx) | Introduced into mfplat.dll in 10.0.10240. |
| [MFInvokeCallback](https://msdn.microsoft.com/en-us/library/windows/desktop/ms695400.aspx) | Introduced into mfplat.dll in 10.0.10240. |
| [MFIsContentProtectionDeviceSupported](https://msdn.microsoft.com/en-us/library/windows/desktop/mt219226.aspx) | Introduced into mfplat.dll in 10.0.10240. |
| [MFllMulDiv](https://msdn.microsoft.com/en-us/library/windows/desktop/dd388510.aspx) | Introduced into mfplat.dll in 10.0.10240. |
| [MFLockDXGIDeviceManager](https://msdn.microsoft.com/en-us/library/windows/desktop/hh162770.aspx) | Introduced into mfplat.dll in 10.0.10240. |
| [MFLockPlatform](https://msdn.microsoft.com/en-us/library/windows/desktop/ms693588.aspx) | Introduced into mfplat.dll in 10.0.10240. |
| [MFLockSharedWorkQueue](https://msdn.microsoft.com/en-us/library/windows/desktop/hh162771.aspx) | Introduced into mfplat.dll in 10.0.10240. |
| [MFLockWorkQueue](https://msdn.microsoft.com/en-us/library/windows/desktop/aa367740.aspx) | Introduced into mfplat.dll in 10.0.10240. |
| [MFPutWaitingWorkItem](https://msdn.microsoft.com/en-us/library/windows/desktop/hh162783.aspx) | Introduced into mfplat.dll in 10.0.10240. |
| [MFPutWorkItem2](https://msdn.microsoft.com/en-us/library/windows/desktop/hh162784.aspx) | Introduced into mfplat.dll in 10.0.10240. |
| [MFPutWorkItemEx2](https://msdn.microsoft.com/en-us/library/windows/desktop/hh162785.aspx) | Introduced into mfplat.dll in 10.0.10240. |
| [MFSerializeAttributesToStream](https://msdn.microsoft.com/en-us/library/windows/desktop/ms702278.aspx) | Introduced into mfplat.dll in 10.0.10240. |
| [MFShutdown](https://msdn.microsoft.com/en-us/library/windows/desktop/ms694273.aspx) | Introduced into mfplat.dll in 10.0.10240. |
| [MFStartup](https://msdn.microsoft.com/en-us/library/windows/desktop/ms702238.aspx) | Introduced into mfplat.dll in 10.0.10240. |
| [MFUnlockDXGIDeviceManager](https://msdn.microsoft.com/en-us/library/windows/desktop/hh162800.aspx) | Introduced into mfplat.dll in 10.0.10240. |
| [MFUnlockPlatform](https://msdn.microsoft.com/en-us/library/windows/desktop/ms703879.aspx) | Introduced into mfplat.dll in 10.0.10240. |
| [MFUnlockWorkQueue](https://msdn.microsoft.com/en-us/library/windows/desktop/aa372543.aspx) | Introduced into mfplat.dll in 10.0.10240. |
| [MFUnwrapMediaType](https://msdn.microsoft.com/en-us/library/windows/desktop/ms696190.aspx) | Introduced into mfplat.dll in 10.0.10240. |
| [MFWrapMediaType](https://msdn.microsoft.com/en-us/library/windows/desktop/ms701782.aspx) | Introduced into mfplat.dll in 10.0.10240. |
| [MFTEnumEx](https://msdn.microsoft.com/en-us/library/Dd388652.aspx) | Introduced into mfplat.dll in 10.0.15063. |
| [MFCreateSystemTimeSource](https://msdn.microsoft.com/en-us/library/ms705610.aspx) | Introduced into mfplat.dll in 10.0.15063. |
| [MFScheduleWorkItemEx](https://msdn.microsoft.com/en-us/library/ms702259.aspx) | Introduced into mfplat.dll in 10.0.15063. |


## APIs from mfreadwrite.dll

| API | Requirements |
| -----| --------------|
| [MFCreateSinkWriterFromMediaSink](https://msdn.microsoft.com/en-us/library/windows/desktop/dd388103.aspx) | Introduced into mfreadwrite.dll in 10.0.10240. |
| [MFCreateSinkWriterFromURL](https://msdn.microsoft.com/en-us/library/windows/desktop/dd388105.aspx) | Introduced into mfreadwrite.dll in 10.0.10240. |
| [MFCreateSourceReaderFromByteStream](https://msdn.microsoft.com/en-us/library/windows/desktop/dd388106.aspx) | Introduced into mfreadwrite.dll in 10.0.10240. |
| [MFCreateSourceReaderFromMediaSource](https://msdn.microsoft.com/en-us/library/windows/desktop/dd388108.aspx) | Introduced into mfreadwrite.dll in 10.0.10240. |
| [MFCreateSourceReaderFromURL](https://msdn.microsoft.com/en-us/library/windows/desktop/dd388110.aspx) | Introduced into mfreadwrite.dll in 10.0.10240. |


## APIs from mmdevapi.dll

| API | Requirements |
| -----| --------------|
| [ActivateAudioInterfaceAsync](https://msdn.microsoft.com/en-us/library/windows/desktop/jj128298.aspx) | Introduced into mmdevapi.dll in 10.0.10240. |


## APIs from MSAJApi.dll

| API | Requirements |
| -----| --------------|
| [alljoyn_aboutdata_create](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutdata_create_empty](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutdata_create_full](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutdata_createfrommsgarg](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutdata_destroy](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutdata_getaboutdata](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutdata_getajsoftwareversion](https://docs.microsoft.com/en-us/scripting/chakra-hosting/jsoftwareversion-function) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutdata_getannouncedaboutdata](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutdata_getappid](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutdata_getappname](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutdata_getdateofmanufacture](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutdata_getdefaultlanguage](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutdata_getdescription](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutdata_getdeviceid](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutdata_getdevicename](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutdata_getfield](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutdata_getfields](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutdata_getfieldsignature](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutdata_gethardwareversion](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutdata_getmanufacturer](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutdata_getmodelnumber](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutdata_getsoftwareversion](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutdata_getsupportedlanguages](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutdata_getsupporturl](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutdata_isfieldannounced](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutdata_isfieldlocalized](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutdata_isfieldrequired](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutdata_isvalid](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutdata_setappid](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutdata_setappid_fromstring](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutdata_setappname](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutdata_setdateofmanufacture](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutdata_setdefaultlanguage](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutdata_setdescription](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutdata_setdeviceid](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutdata_setdevicename](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutdata_setfield](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutdata_sethardwareversion](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutdata_setmanufacturer](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutdata_setmodelnumber](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutdata_setsoftwareversion](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutdata_setsupportedlanguage](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutdata_setsupporturl](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutdatalistener_create](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutdatalistener_destroy](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_abouticon_clear](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_abouticon_create](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_abouticon_destroy](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_abouticon_setcontent](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_abouticon_setcontent_frommsgarg](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_abouticon_seturl](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_abouticonobj_create](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_abouticonobj_destroy](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_abouticonproxy_create](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_abouticonproxy_destroy](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_abouticonproxy_geticon](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_abouticonproxy_getversion](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutlistener_create](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutlistener_destroy](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutobj_announce](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutobj_announce_using_datalistener](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutobj_create](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutobj_destroy](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutobj_unannounce](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutobjectdescription_clear](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutobjectdescription_create](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutobjectdescription_create_full](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutobjectdescription_createfrommsgarg](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutobjectdescription_destroy](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutobjectdescription_getinterfacepaths](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutobjectdescription_getinterfaces](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutobjectdescription_getmsgarg](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutobjectdescription_getpaths](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutobjectdescription_hasinterface](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutobjectdescription_hasinterfaceatpath](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutobjectdescription_haspath](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutproxy_create](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutproxy_destroy](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutproxy_getaboutdata](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutproxy_getobjectdescription](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_aboutproxy_getversion](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_authlistener_create](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_authlistener_destroy](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_authlistener_requestcredentialsresponse](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_authlistener_verifycredentialsresponse](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_authlistenerasync_create](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_authlistenerasync_destroy](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_addlogonentry](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_addmatch](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_advertisename](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_bindsessionport](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_canceladvertisename](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_cancelfindadvertisedname](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_cancelfindadvertisednamebytransport](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_cancelwhoimplements_interface](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_cancelwhoimplements_interfaces](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_clearkeys](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_clearkeystore](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_connect](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_create](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_create_concurrency](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_createinterface](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_createinterface_secure](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_createinterfacesfromxml](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_deleteinterface](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_destroy](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_disconnect](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_enableconcurrentcallbacks](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_enablepeersecurity](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_findadvertisedname](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_findadvertisednamebytransport](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_getalljoyndebugobj](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_getalljoynproxyobj](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_getconcurrency](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_getconnectspec](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_getdbusproxyobj](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_getglobalguidstring](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_getinterface](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_getinterfaces](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_getkeyexpiration](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_getpeerguid](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_gettimestamp](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_getuniquename](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_isconnected](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_ispeersecurityenabled](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_isstarted](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_isstopping](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_join](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_joinsession](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_joinsessionasync](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_leavesession](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_namehasowner](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_ping](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_registeraboutlistener](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_registerbuslistener](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_registerbusobject](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_registerbusobject_secure](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_registerkeystorelistener](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_registersignalhandler](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_registersignalhandlerwithrule](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_releasename](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_reloadkeystore](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_removematch](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_removesessionmember](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_requestname](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_setdaemondebug](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_setkeyexpiration](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_setlinktimeout](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_setlinktimeoutasync](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_setsessionlistener](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_start](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_stop](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_unbindsessionport](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_unregisteraboutlistener](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_unregisterallaboutlisteners](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_unregisterallhandlers](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_unregisterbuslistener](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_unregisterbusobject](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_unregistersignalhandler](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_unregistersignalhandlerwithrule](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_whoimplements_interface](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_whoimplements_interfaces](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_buslistener_create](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_buslistener_destroy](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busobject_addinterface](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busobject_addinterface_announced](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busobject_addmethodhandler](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busobject_addmethodhandlers](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busobject_cancelsessionlessmessage](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busobject_cancelsessionlessmessage_serial](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busobject_create](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busobject_destroy](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busobject_emitpropertieschanged](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busobject_emitpropertychanged](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busobject_getannouncedinterfacenames](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busobject_getbusattachment](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busobject_getname](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busobject_getpath](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busobject_issecure](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busobject_methodreply_args](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busobject_methodreply_err](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busobject_methodreply_status](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busobject_setannounceflag](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busobject_signal](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_credentials_clear](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_credentials_create](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_credentials_destroy](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_credentials_getcertchain](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_credentials_getexpiration](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_credentials_getlogonentry](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_credentials_getpassword](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_credentials_getprivateKey](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_credentials_getusername](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_credentials_isset](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_credentials_setcertchain](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_credentials_setexpiration](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_credentials_setlogonentry](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_credentials_setpassword](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_credentials_setprivatekey](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_credentials_setusername](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_getbuildinfo](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_getnumericversion](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_getversion](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_init](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_interfacedescription_activate](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_interfacedescription_addannotation](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_interfacedescription_addmember](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_interfacedescription_addmemberannotation](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_interfacedescription_addmethod](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_interfacedescription_addproperty](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_interfacedescription_addpropertyannotation](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_interfacedescription_addsignal](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_interfacedescription_eql](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_interfacedescription_getannotation](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_interfacedescription_getannotationatindex](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_interfacedescription_getannotationscount](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_interfacedescription_getmember](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_interfacedescription_getmemberannotation](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_interfacedescription_getmembers](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_interfacedescription_getmethod](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_interfacedescription_getname](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_interfacedescription_getproperties](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_interfacedescription_getproperty](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_interfacedescription_getpropertyannotation](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_interfacedescription_getsecuritypolicy](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_interfacedescription_getsignal](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_interfacedescription_hasmember](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_interfacedescription_hasproperties](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_interfacedescription_hasproperty](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_interfacedescription_introspect](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_interfacedescription_issecure](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_interfacedescription_member_eql](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_interfacedescription_member_getannotation](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_interfacedescription_member_getannotationatindex](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_interfacedescription_member_getannotationscount](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_interfacedescription_property_eql](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_interfacedescription_property_getannotation](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_interfacedescription_property_getannotationatindex](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_interfacedescription_property_getannotationscount](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_keystorelistener_create](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_keystorelistener_destroy](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_keystorelistener_getkeys](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_keystorelistener_putkeys](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_message_create](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_message_description](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_message_destroy](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_message_eql](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_message_getarg](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_message_getargs](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_message_getauthmechanism](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_message_getcallserial](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_message_getcompressiontoken](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_message_getdestination](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_message_geterrorname](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_message_getflags](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_message_getinterface](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_message_getmembername](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_message_getobjectpath](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_message_getreceiveendpointname](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_message_getreplyserial](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_message_getsender](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_message_getsessionid](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_message_getsignature](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_message_gettimestamp](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_message_gettype](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_message_isbroadcastsignal](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_message_isencrypted](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_message_isexpired](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_message_isglobalbroadcast](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_message_issessionless](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_message_isunreliable](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_message_parseargs](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_message_setendianess](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_message_tostring](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_array_create](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_array_element](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_array_get](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_array_set](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_array_set_offset](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_array_signature](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_array_tostring](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_clear](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_clone](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_copy](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_create](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_create_and_set](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_destroy](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_equal](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_get](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_get_array_element](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_get_array_elementsignature](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_get_array_numberofelements](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_get_bool](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_get_bool_array](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_get_double](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_get_double_array](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_get_int16](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_get_int16_array](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_get_int32](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_get_int32_array](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_get_int64](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_get_int64_array](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_get_objectpath](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_get_signature](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_get_string](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_get_uint16](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_get_uint16_array](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_get_uint32](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_get_uint32_array](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_get_uint64](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_get_uint64_array](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_get_uint8](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_get_uint8_array](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_get_variant](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_get_variant_array](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_getdictelement](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_getkey](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_getmember](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_getnummembers](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_gettype](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_getvalue](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_hassignature](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_set](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_set_and_stabilize](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_set_bool](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_set_bool_array](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_set_double](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_set_double_array](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_set_int16](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_set_int16_array](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_set_int32](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_set_int32_array](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_set_int64](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_set_int64_array](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_set_objectpath](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_set_objectpath_array](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_set_signature](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_set_signature_array](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_set_string](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_set_string_array](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_set_uint16](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_set_uint16_array](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_set_uint32](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_set_uint32_array](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_set_uint64](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_set_uint64_array](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_set_uint8](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_set_uint8_array](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_setdictentry](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_setstruct](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_signature](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_stabilize](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_msgarg_tostring](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_observer_create](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_observer_destroy](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_observer_get](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_observer_getfirst](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_observer_getnext](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_observer_registerlistener](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_observer_unregisteralllisteners](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_observer_unregisterlistener](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_observerlistener_create](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_observerlistener_destroy](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_passwordmanager_setcredentials](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_proxybusobject_addchild](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_proxybusobject_addinterface](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_proxybusobject_addinterface_by_name](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_proxybusobject_copy](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_proxybusobject_create](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_proxybusobject_create_secure](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_proxybusobject_destroy](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_proxybusobject_enablepropertycaching](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_proxybusobject_getallproperties](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_proxybusobject_getallpropertiesasync](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_proxybusobject_getchild](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_proxybusobject_getchildren](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_proxybusobject_getinterface](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_proxybusobject_getinterfaces](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_proxybusobject_getpath](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_proxybusobject_getproperty](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_proxybusobject_getpropertyasync](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_proxybusobject_getservicename](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_proxybusobject_getsessionid](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_proxybusobject_getuniquename](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_proxybusobject_implementsinterface](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_proxybusobject_introspectremoteobject](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_proxybusobject_introspectremoteobjectasync](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_proxybusobject_issecure](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_proxybusobject_isvalid](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_proxybusobject_methodcall](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_proxybusobject_methodcall_member](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_proxybusobject_methodcall_member_noreply](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_proxybusobject_methodcall_noreply](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_proxybusobject_methodcallasync](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_proxybusobject_methodcallasync_member](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_proxybusobject_parsexml](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_proxybusobject_ref_create](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_proxybusobject_ref_decref](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_proxybusobject_ref_get](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_proxybusobject_ref_incref](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_proxybusobject_registerpropertieschangedlistener](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_proxybusobject_removechild](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_proxybusobject_secureconnection](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_proxybusobject_secureconnectionasync](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_proxybusobject_setproperty](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_proxybusobject_setpropertyasync](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_proxybusobject_unregisterpropertieschangedlistener](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_sessionlistener_create](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_sessionlistener_destroy](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_sessionopts_cmp](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_sessionopts_create](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_sessionopts_destroy](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_sessionopts_get_multipoint](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_sessionopts_get_proximity](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_sessionopts_get_traffic](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_sessionopts_get_transports](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_sessionopts_iscompatible](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_sessionopts_set_multipoint](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_sessionopts_set_proximity](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_sessionopts_set_traffic](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_sessionopts_set_transports](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_sessionportlistener_create](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_sessionportlistener_destroy](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_shutdown](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_unity_deferred_callbacks_process](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_unity_set_deferred_callback_mainthread_only](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [AllJoynCloseBusHandle](https://msdn.microsoft.com/en-us/library/Mt270088.aspx) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [AllJoynConnectToBus](https://msdn.microsoft.com/en-us/library/Mt270089.aspx) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [AllJoynEnumEvents](https://msdn.microsoft.com/en-us/library/Mt270090.aspx) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [AllJoynEventSelect](https://msdn.microsoft.com/en-us/library/Mt270091.aspx) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [AllJoynReceiveFromBus](https://msdn.microsoft.com/en-us/library/Mt270092.aspx) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [AllJoynSendToBus](https://msdn.microsoft.com/en-us/library/Mt270093.aspx) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [QCC_StatusText](https://msdn.microsoft.com/en-us/library/Mt186561.aspx) | Introduced into MSAJApi.dll in 10.0.10240. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_autopinger_adddestination](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10586. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_autopinger_addpinggroup](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10586. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_autopinger_create](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10586. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_autopinger_destroy](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10586. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_autopinger_pause](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10586. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_autopinger_removedestination](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10586. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_autopinger_removepinggroup](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10586. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_autopinger_resume](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10586. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_autopinger_setpinginterval](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10586. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_enablepeersecuritywithpermissionconfigurationlistener](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10586. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_secureconnection](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10586. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_secureconnectionasync](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10586. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_permissionconfigurationlistener_create](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10586. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_permissionconfigurationlistener_destroy](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10586. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_pinglistener_create](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10586. Moved into msajapi.dll in 10.0.14393. |
| [alljoyn_pinglistener_destroy](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into MSAJApi.dll in 10.0.10586. Moved into msajapi.dll in 10.0.14393. |


## APIs from mscoree.dll

| API | Requirements |
| -----| --------------|
| _CorDllMain | Introduced into mscoree.dll in 10.0.10240. Removed in 10.0.15063. |
| _CorExeMain | Introduced into mscoree.dll in 10.0.10240. Removed in 10.0.15063. |
| [MetaDataGetDispenser](https://msdn.microsoft.com/en-us/library/windows/desktop/br229853.aspx) | Introduced into mscoree.dll in 10.0.10240. Moved into rometadata.dll in 10.0.10586. |


## APIs from mswsock.dll

| API | Requirements |
| -----| --------------|
| [AcceptEx](https://msdn.microsoft.com/en-us/library/windows/desktop/ms737524.aspx) | Introduced into mswsock.dll in 10.0.10240. |
| [GetAcceptExSockaddrs](https://msdn.microsoft.com/en-us/library/windows/desktop/ms738516.aspx) | Introduced into mswsock.dll in 10.0.10240. |
| [TransmitFile](https://msdn.microsoft.com/en-us/library/windows/desktop/ms740565.aspx) | Introduced into mswsock.dll in 10.0.10240. |


## APIs from ncrypt.dll

| API | Requirements |
| -----| --------------|
| [BCryptCloseAlgorithmProvider](https://msdn.microsoft.com/en-us/library/windows/desktop/aa375377.aspx) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptCreateHash](https://msdn.microsoft.com/en-us/library/windows/desktop/aa375383.aspx) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptDecrypt](https://msdn.microsoft.com/en-us/library/windows/desktop/aa375391.aspx) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptDeriveKey](https://msdn.microsoft.com/en-us/library/windows/desktop/aa375393.aspx) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptDeriveKeyCapi](https://msdn.microsoft.com/en-us/library/windows/desktop/dd433794.aspx) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptDeriveKeyPBKDF2](https://msdn.microsoft.com/en-us/library/windows/desktop/dd433795.aspx) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptDestroyHash](https://msdn.microsoft.com/en-us/library/windows/desktop/aa375399.aspx) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptDestroyKey](https://msdn.microsoft.com/en-us/library/windows/desktop/aa375404.aspx) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptDestroySecret](https://msdn.microsoft.com/en-us/library/windows/desktop/aa375407.aspx) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptDuplicateHash](https://msdn.microsoft.com/en-us/library/windows/desktop/aa375413.aspx) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptDuplicateKey](https://msdn.microsoft.com/en-us/library/windows/desktop/aa375419.aspx) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptEncrypt](https://msdn.microsoft.com/en-us/library/windows/desktop/aa375421.aspx) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptEnumAlgorithms](https://msdn.microsoft.com/en-us/library/windows/desktop/aa375422.aspx) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptEnumProviders](https://msdn.microsoft.com/en-us/library/windows/desktop/aa375429.aspx) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptExportKey](https://msdn.microsoft.com/en-us/library/windows/desktop/aa375434.aspx) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptFinalizeKeyPair](https://msdn.microsoft.com/en-us/library/windows/desktop/aa375439.aspx) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptFinishHash](https://msdn.microsoft.com/en-us/library/windows/desktop/aa375443.aspx) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptFreeBuffer](https://msdn.microsoft.com/en-us/library/windows/desktop/aa375445.aspx) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptGenerateKeyPair](https://msdn.microsoft.com/en-us/library/windows/desktop/aa375451.aspx) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptGenerateSymmetricKey](https://msdn.microsoft.com/en-us/library/windows/desktop/aa375453.aspx) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptGenRandom](https://msdn.microsoft.com/en-us/library/windows/desktop/aa375458.aspx) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptGetProperty](https://msdn.microsoft.com/en-us/library/windows/desktop/aa375464.aspx) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptHash](https://msdn.microsoft.com/en-us/library/windows/desktop/mt633798.aspx) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptHashData](https://msdn.microsoft.com/en-us/library/windows/desktop/aa375468.aspx) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptImportKey](https://msdn.microsoft.com/en-us/library/windows/desktop/aa375475.aspx) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptImportKeyPair](https://msdn.microsoft.com/en-us/library/windows/desktop/aa375472.aspx) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptKeyDerivation](https://msdn.microsoft.com/en-us/library/windows/desktop/hh448506.aspx) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptOpenAlgorithmProvider](https://msdn.microsoft.com/en-us/library/windows/desktop/aa375479.aspx) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptSecretAgreement](https://msdn.microsoft.com/en-us/library/windows/desktop/aa375496.aspx) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptSetProperty](https://msdn.microsoft.com/en-us/library/windows/desktop/aa375504.aspx) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptSignHash](https://msdn.microsoft.com/en-us/library/windows/desktop/aa375510.aspx) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [BCryptVerifySignature](https://msdn.microsoft.com/en-us/library/windows/desktop/aa375515.aspx) | Introduced into ncrypt.dll in 10.0.10240. Moved into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| [NCryptCreateClaim](https://msdn.microsoft.com/en-us/library/windows/desktop/mt270085.aspx) | Introduced into ncrypt.dll in 10.0.10240. |
| [NCryptCreatePersistedKey](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376247.aspx) | Introduced into ncrypt.dll in 10.0.10240. |
| [NCryptDecrypt](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376249.aspx) | Introduced into ncrypt.dll in 10.0.10240. |
| [NCryptDeleteKey](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376251.aspx) | Introduced into ncrypt.dll in 10.0.10240. |
| [NCryptDeriveKey](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376252.aspx) | Introduced into ncrypt.dll in 10.0.10240. |
| [NCryptEncrypt](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376255.aspx) | Introduced into ncrypt.dll in 10.0.10240. |
| [NCryptEnumAlgorithms](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376257.aspx) | Introduced into ncrypt.dll in 10.0.10240. |
| [NCryptEnumKeys](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376259.aspx) | Introduced into ncrypt.dll in 10.0.10240. |
| [NCryptExportKey](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376263.aspx) | Introduced into ncrypt.dll in 10.0.10240. |
| [NCryptFinalizeKey](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376265.aspx) | Introduced into ncrypt.dll in 10.0.10240. |
| [NCryptFreeBuffer](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376267.aspx) | Introduced into ncrypt.dll in 10.0.10240. |
| [NCryptFreeObject](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376269.aspx) | Introduced into ncrypt.dll in 10.0.10240. |
| [NCryptGetProperty](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376273.aspx) | Introduced into ncrypt.dll in 10.0.10240. |
| [NCryptImportKey](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376276.aspx) | Introduced into ncrypt.dll in 10.0.10240. |
| [NCryptIsAlgSupported](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376278.aspx) | Introduced into ncrypt.dll in 10.0.10240. |
| [NCryptKeyDerivation](https://msdn.microsoft.com/en-us/library/windows/desktop/hh448516.aspx) | Introduced into ncrypt.dll in 10.0.10240. |
| [NCryptOpenKey](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376284.aspx) | Introduced into ncrypt.dll in 10.0.10240. |
| [NCryptOpenStorageProvider](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376286.aspx) | Introduced into ncrypt.dll in 10.0.10240. |
| [NCryptSecretAgreement](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376289.aspx) | Introduced into ncrypt.dll in 10.0.10240. |
| [NCryptSetProperty](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376292.aspx) | Introduced into ncrypt.dll in 10.0.10240. |
| [NCryptSignHash](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376295.aspx) | Introduced into ncrypt.dll in 10.0.10240. |
| [NCryptVerifyClaim](https://msdn.microsoft.com/en-us/library/windows/desktop/mt270086.aspx) | Introduced into ncrypt.dll in 10.0.10240. |
| [NCryptVerifySignature](https://msdn.microsoft.com/en-us/library/windows/desktop/aa376298.aspx) | Introduced into ncrypt.dll in 10.0.10240. |


## APIs from ntdll.dll

| API | Requirements |
| -----| --------------|
| [RtlEthernetAddressToStringA](https://msdn.microsoft.com/en-us/library/windows/desktop/dn550721.aspx) | Introduced into ntdll.dll in 10.0.10240. |
| [RtlEthernetAddressToStringW](https://msdn.microsoft.com/en-us/library/windows/desktop/dn550721.aspx) | Introduced into ntdll.dll in 10.0.10240. |
| [RtlEthernetStringToAddressA](https://msdn.microsoft.com/en-us/library/windows/desktop/dn550722.aspx) | Introduced into ntdll.dll in 10.0.10240. |
| [RtlEthernetStringToAddressW](https://msdn.microsoft.com/en-us/library/windows/desktop/dn550722.aspx) | Introduced into ntdll.dll in 10.0.10240. |
| [RtlIpv4AddressToStringA](https://msdn.microsoft.com/en-us/library/windows/desktop/aa814456.aspx) | Introduced into ntdll.dll in 10.0.10240. |
| [RtlIpv4AddressToStringExA](https://msdn.microsoft.com/en-us/library/windows/desktop/aa814457.aspx) | Introduced into ntdll.dll in 10.0.10240. |
| [RtlIpv4AddressToStringExW](https://msdn.microsoft.com/en-us/library/windows/desktop/aa814457.aspx) | Introduced into ntdll.dll in 10.0.10240. |
| [RtlIpv4AddressToStringW](https://msdn.microsoft.com/en-us/library/windows/desktop/aa814456.aspx) | Introduced into ntdll.dll in 10.0.10240. |
| [RtlIpv4StringToAddressA](https://msdn.microsoft.com/en-us/library/windows/desktop/aa814458.aspx) | Introduced into ntdll.dll in 10.0.10240. |
| [RtlIpv4StringToAddressExA](https://msdn.microsoft.com/en-us/library/windows/desktop/aa814459.aspx) | Introduced into ntdll.dll in 10.0.10240. |
| [RtlIpv4StringToAddressExW](https://msdn.microsoft.com/en-us/library/windows/desktop/aa814459.aspx) | Introduced into ntdll.dll in 10.0.10240. |
| [RtlIpv4StringToAddressW](https://msdn.microsoft.com/en-us/library/windows/desktop/aa814458.aspx) | Introduced into ntdll.dll in 10.0.10240. |
| [RtlIpv6AddressToStringA](https://msdn.microsoft.com/en-us/library/windows/desktop/aa814460.aspx) | Introduced into ntdll.dll in 10.0.10240. |
| [RtlIpv6AddressToStringExA](https://msdn.microsoft.com/en-us/library/windows/desktop/aa814461.aspx) | Introduced into ntdll.dll in 10.0.10240. |
| [RtlIpv6AddressToStringExW](https://msdn.microsoft.com/en-us/library/windows/desktop/aa814461.aspx) | Introduced into ntdll.dll in 10.0.10240. |
| [RtlIpv6AddressToStringW](https://msdn.microsoft.com/en-us/library/windows/desktop/aa814460.aspx) | Introduced into ntdll.dll in 10.0.10240. |
| [RtlIpv6StringToAddressA](https://msdn.microsoft.com/en-us/library/windows/desktop/aa814462.aspx) | Introduced into ntdll.dll in 10.0.10240. |
| [RtlIpv6StringToAddressExA](https://msdn.microsoft.com/en-us/library/windows/desktop/aa814463.aspx) | Introduced into ntdll.dll in 10.0.10240. |
| [RtlIpv6StringToAddressExW](https://msdn.microsoft.com/en-us/library/windows/desktop/aa814463.aspx) | Introduced into ntdll.dll in 10.0.10240. |
| [RtlIpv6StringToAddressW](https://msdn.microsoft.com/en-us/library/windows/desktop/aa814462.aspx) | Introduced into ntdll.dll in 10.0.10240. |


## APIs from oleaut32.dll

| API | Requirements |
| -----| --------------|
| [BSTR_UserFree](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644523.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [BSTR_UserFree64](https://msdn.microsoft.com/en-us/library/windows/desktop/hh309490.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [BSTR_UserMarshal](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644509.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [BSTR_UserMarshal64](https://msdn.microsoft.com/en-us/library/windows/desktop/hh309491.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [BSTR_UserSize](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644365.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [BSTR_UserSize64](https://msdn.microsoft.com/en-us/library/windows/desktop/hh309492.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [BSTR_UserUnmarshal](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644522.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [BSTR_UserUnmarshal64](https://msdn.microsoft.com/en-us/library/windows/desktop/hh309493.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [DispInvoke](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221366.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [LPSAFEARRAY_Marshal](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644537.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [LPSAFEARRAY_Size](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644517.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [LPSAFEARRAY_Unmarshal](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644390.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [LPSAFEARRAY_UserFree](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644504.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [LPSAFEARRAY_UserFree64](https://msdn.microsoft.com/en-us/library/windows/desktop/hh768285.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [LPSAFEARRAY_UserMarshal](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644398.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [LPSAFEARRAY_UserMarshal64](https://msdn.microsoft.com/en-us/library/windows/desktop/hh768286.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [LPSAFEARRAY_UserSize](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644399.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [LPSAFEARRAY_UserSize64](https://msdn.microsoft.com/en-us/library/windows/desktop/hh768287.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [LPSAFEARRAY_UserUnmarshal](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644503.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [LPSAFEARRAY_UserUnmarshal64](https://msdn.microsoft.com/en-us/library/windows/desktop/hh768288.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [SafeArrayAccessData](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221620.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [SafeArrayAllocData](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221468.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [SafeArrayAllocDescriptor](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221407.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [SafeArrayAllocDescriptorEx](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221540.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [SafeArrayCopy](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221451.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [SafeArrayCopyData](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221174.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [SafeArrayCreate](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221234.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [SafeArrayCreateEx](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221198.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [SafeArrayCreateVector](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221558.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [SafeArrayCreateVectorEx](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221093.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [SafeArrayDestroy](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221702.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [SafeArrayDestroyData](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221418.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [SafeArrayDestroyDescriptor](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221681.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [SafeArrayGetDim](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221539.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [SafeArrayGetElement](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221255.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [SafeArrayGetElemsize](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221074.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [SafeArrayGetIID](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221428.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [SafeArrayGetLBound](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221622.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [SafeArrayGetRecordInfo](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221022.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [SafeArrayGetUBound](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221584.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [SafeArrayGetVartype](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221446.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [SafeArrayLock](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221492.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [SafeArrayPtrOfIndex](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221452.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [SafeArrayPutElement](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221283.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [SafeArrayRedim](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221002.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [SafeArraySetIID](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221347.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [SafeArraySetRecordInfo](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221287.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [SafeArrayUnaccessData](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221203.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [SafeArrayUnlock](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221246.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [SysAllocString](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221458.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [SysAllocStringByteLen](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221637.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [SysAllocStringLen](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221639.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [SysFreeString](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221481.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [SysReAllocString](https://msdn.microsoft.com/en-us/library/windows/desktop/ms220986.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [SysReAllocStringLen](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221533.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [SysStringByteLen](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221097.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [SysStringLen](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221240.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [SystemTimeToVariantTime](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221646.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarAbs](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221343.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarAdd](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221574.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarAnd](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221576.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBoolFromCy](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221228.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBoolFromDate](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221076.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBoolFromDec](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221677.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBoolFromDisp](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221284.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBoolFromI1](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221660.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBoolFromI2](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221157.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBoolFromI4](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221056.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBoolFromI8](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644364.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBoolFromR4](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221579.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBoolFromR8](https://msdn.microsoft.com/en-us/library/windows/desktop/ms220994.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBoolFromStr](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221300.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBoolFromUI1](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221202.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBoolFromUI2](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221158.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBoolFromUI4](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221431.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBoolFromUI8](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644380.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBstrCat](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221621.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBstrCmp](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221038.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBstrFromBool](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221338.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBstrFromCy](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221218.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBstrFromDate](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221699.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBstrFromDec](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221304.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBstrFromDisp](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221305.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBstrFromI1](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221419.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBstrFromI2](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221016.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBstrFromI4](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221516.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBstrFromI8](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644520.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBstrFromR4](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221092.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBstrFromR8](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221632.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBstrFromUI1](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221230.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBstrFromUI2](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221693.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBstrFromUI4](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221361.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarBstrFromUI8](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644394.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarCat](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221084.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarCmp](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221006.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarCyAbs](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221356.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarCyAdd](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221636.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarCyCmp](https://msdn.microsoft.com/en-us/library/windows/desktop/ms220995.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarCyCmpR8](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221175.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarCyFix](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221532.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarCyFromBool](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221667.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarCyFromDate](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221216.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarCyFromDec](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221384.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarCyFromDisp](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221045.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarCyFromI1](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221534.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarCyFromI2](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221484.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarCyFromI4](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221280.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarCyFromI8](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644370.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarCyFromR4](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221335.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarCyFromR8](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221572.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarCyFromStr](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221582.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarCyFromUI1](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221671.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarCyFromUI2](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221684.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarCyFromUI4](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221459.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarCyFromUI8](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644391.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarCyInt](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221054.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarCyMul](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221412.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarCyMulI4](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221104.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarCyMulI8](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644381.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarCyNeg](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221514.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarCyRound](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221546.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarCySub](https://msdn.microsoft.com/en-us/library/windows/desktop/ms220982.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDateFromBool](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221310.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDateFromCy](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221519.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDateFromDec](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221122.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDateFromDisp](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221271.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDateFromI1](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221408.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDateFromI2](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221475.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDateFromI4](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221380.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDateFromI8](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644361.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDateFromR4](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221261.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDateFromR8](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221441.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDateFromStr](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221395.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDateFromUdate](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221036.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDateFromUdateEx](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221630.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDateFromUI1](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221443.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDateFromUI2](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221166.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDateFromUI4](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221292.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDateFromUI8](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644507.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDecAbs](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221601.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDecAdd](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221264.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDecCmp](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221686.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDecCmpR8](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221512.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDecDiv](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221344.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDecFix](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221341.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDecFromBool](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221530.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDecFromCy](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221536.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDecFromDate](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221650.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDecFromDisp](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221274.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDecFromI1](https://msdn.microsoft.com/en-us/library/windows/desktop/ms220988.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDecFromI2](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221511.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDecFromI4](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221219.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDecFromI8](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644377.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDecFromR4](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221517.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDecFromR8](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221241.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDecFromStr](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221334.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDecFromUI1](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221654.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDecFromUI2](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221154.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDecFromUI4](https://msdn.microsoft.com/en-us/library/windows/desktop/ms220997.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDecFromUI8](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644388.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDecInt](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221189.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDecMul](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221527.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDecNeg](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221491.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDecRound](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221075.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDecSub](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221556.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarDiv](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221253.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarEqv](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221077.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarFix](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221664.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarFormat](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221128.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarFormatCurrency](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221424.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarFormatDateTime](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221554.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarFormatFromTokens](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221147.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarFormatNumber](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221477.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarFormatPercent](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221125.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI1FromBool](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221049.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI1FromCy](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221389.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI1FromDate](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221012.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI1FromDec](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221094.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI1FromDisp](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221373.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI1FromI2](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221716.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI1FromI4](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221129.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI1FromI8](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644518.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI1FromR4](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221312.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI1FromR8](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221195.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI1FromStr](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221201.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI1FromUI1](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221208.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI1FromUI2](https://msdn.microsoft.com/en-us/library/windows/desktop/ms220998.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI1FromUI4](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221560.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI1FromUI8](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644383.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI2FromBool](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221178.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI2FromCy](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221153.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI2FromDate](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221642.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI2FromDec](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221005.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI2FromDisp](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221088.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI2FromI1](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221623.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI2FromI4](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221668.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI2FromI8](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644393.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI2FromR4](https://msdn.microsoft.com/en-us/library/windows/desktop/ms220989.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI2FromR8](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221429.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI2FromStr](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221411.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI2FromUI1](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221659.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI2FromUI2](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221327.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI2FromUI4](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221383.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI2FromUI8](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644362.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI4FromBool](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221483.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI4FromCy](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221707.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI4FromDate](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221403.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI4FromDec](https://msdn.microsoft.com/en-us/library/windows/desktop/ms220984.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI4FromDisp](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221605.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI4FromI1](https://msdn.microsoft.com/en-us/library/windows/desktop/ms220991.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI4FromI2](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221137.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI4FromI8](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644516.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI4FromR4](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221066.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI4FromR8](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221146.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI4FromStr](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221194.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI4FromUI1](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221044.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI4FromUI2](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221182.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI4FromUI4](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221611.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI4FromUI8](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644378.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI8FromBool](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644385.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI8FromCy](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644514.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI8FromDate](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644386.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI8FromDec](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644389.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI8FromDisp](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644506.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI8FromI1](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644375.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI8FromI2](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644528.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI8FromR4](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644384.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI8FromR8](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644369.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI8FromStr](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644510.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI8FromUI1](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644531.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI8FromUI2](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644367.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI8FromUI4](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644513.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarI8FromUI8](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644524.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VARIANT_UserFree](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644359.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VARIANT_UserFree64](https://msdn.microsoft.com/en-us/library/windows/desktop/hh309497.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VARIANT_UserMarshal](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644368.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VARIANT_UserMarshal64](https://msdn.microsoft.com/en-us/library/windows/desktop/hh309498.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VARIANT_UserSize](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644387.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VARIANT_UserSize64](https://msdn.microsoft.com/en-us/library/windows/desktop/hh309499.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VARIANT_UserUnmarshal](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644534.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VARIANT_UserUnmarshal64](https://msdn.microsoft.com/en-us/library/windows/desktop/hh309500.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VariantChangeType](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221258.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VariantChangeTypeEx](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221634.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VariantClear](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221165.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VariantCopy](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221697.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VariantCopyInd](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221184.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VariantInit](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221402.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VariantTimeToSystemTime](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221440.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarIdiv](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221682.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarImp](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221497.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarInt](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221460.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarMod](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221405.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarMonthName](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221299.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarMul](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221602.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarNeg](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221413.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarNot](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221606.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarNumFromParseNum](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221357.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarOr](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221358.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarParseNumFromStr](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221573.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarPow](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221303.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR4CmpR8](https://msdn.microsoft.com/en-us/library/windows/desktop/ms220981.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR4FromBool](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221476.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR4FromCy](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221071.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR4FromDate](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221266.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR4FromDec](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221651.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR4FromDisp](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221392.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR4FromI1](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221454.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR4FromI2](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221055.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR4FromI4](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221156.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR4FromI8](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644392.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR4FromR8](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221273.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR4FromStr](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221513.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR4FromUI1](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221631.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR4FromUI2](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221322.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR4FromUI4](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221028.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR4FromUI8](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644539.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR8FromBool](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221613.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR8FromCy](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221239.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR8FromDate](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221034.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR8FromDec](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221523.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR8FromDisp](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221525.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR8FromI1](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221462.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR8FromI2](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221500.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR8FromI4](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221714.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR8FromI8](https://msdn.microsoft.com/en-us/library/windows/desktop/ms313882.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR8FromR4](https://msdn.microsoft.com/en-us/library/windows/desktop/ms220977.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR8FromStr](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221331.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR8FromUI1](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221603.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR8FromUI2](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221709.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR8FromUI4](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221013.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR8FromUI8](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644395.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR8Pow](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221090.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarR8Round](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221501.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarRound](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221372.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarSub](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221079.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarTokenizeFormatString](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221340.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUdateFromDate](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221217.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI1FromBool](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221095.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI1FromCy](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221535.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI1FromDate](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221011.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI1FromDec](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221406.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI1FromDisp](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221151.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI1FromI1](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221291.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI1FromI2](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221281.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI1FromI4](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221024.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI1FromI8](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644500.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI1FromR4](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221279.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI1FromR8](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221051.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI1FromStr](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221537.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI1FromUI2](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221163.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI1FromUI4](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221493.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI1FromUI8](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644535.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI2FromBool](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221070.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI2FromCy](https://msdn.microsoft.com/en-us/library/windows/desktop/ms220979.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI2FromDate](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221489.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI2FromDec](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221132.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI2FromDisp](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221710.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI2FromI1](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221638.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI2FromI2](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221294.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI2FromI4](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221548.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI2FromI8](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644502.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI2FromR4](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221131.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI2FromR8](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221490.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI2FromStr](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221635.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI2FromUI1](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221043.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI2FromUI4](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221205.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI2FromUI8](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644526.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI4FromBool](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221415.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI4FromCy](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221448.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI4FromDate](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221362.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI4FromDec](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221624.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI4FromDisp](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221276.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI4FromI1](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221221.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI4FromI2](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221562.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI4FromI4](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221209.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI4FromI8](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644533.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI4FromR4](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221518.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI4FromR8](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221073.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI4FromStr](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221715.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI4FromUI1](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221633.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI4FromUI2](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221521.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI4FromUI8](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644538.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI8FromBool](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644525.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI8FromCy](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644508.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI8FromDate](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644396.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI8FromDec](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644371.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI8FromDisp](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644515.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI8FromI1](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644376.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI8FromI2](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644527.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI8FromI8](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644511.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI8FromR4](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644382.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI8FromR8](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644397.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI8FromStr](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644536.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI8FromUI1](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644532.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI8FromUI2](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644366.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarUI8FromUI4](https://msdn.microsoft.com/en-us/library/windows/desktop/ms644363.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarWeekdayName](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221315.aspx) | Introduced into oleaut32.dll in 10.0.10240. |
| [VarXor](https://msdn.microsoft.com/en-us/library/windows/desktop/ms221188.aspx) | Introduced into oleaut32.dll in 10.0.10240. |


## APIs from propsys.dll

| API | Requirements |
| -----| --------------|
| [PropVariantCompareEx](https://msdn.microsoft.com/en-us/library/windows/desktop/bb776517.aspx) | Introduced into propsys.dll in 10.0.10240. |
| [PropVariantToWinRTPropertyValue](https://msdn.microsoft.com/en-us/library/windows/desktop/dn313197.aspx) | Introduced into propsys.dll in 10.0.10240. |
| [WinRTPropertyValueToPropVariant](https://msdn.microsoft.com/en-us/library/windows/desktop/dn313198.aspx) | Introduced into propsys.dll in 10.0.10240. |
| [PSCreateMemoryPropertyStore](https://msdn.microsoft.com/en-us/library/ms647446.aspx) | Introduced into propsys.dll in 10.0.15063. |
| [PropVariantChangeType](https://msdn.microsoft.com/en-us/library/ms648136.aspx) | Introduced into propsys.dll in 10.0.15063. |
| [PropVariantToStringAlloc](https://msdn.microsoft.com/en-us/library/Aa969050.aspx) | Introduced into propsys.dll in 10.0.15063. |
| [PropVariantToStringWithDefault](https://msdn.microsoft.com/en-us/library/Aa969152.aspx) | Introduced into propsys.dll in 10.0.15063. |
| [PropVariantToBoolean](https://msdn.microsoft.com/en-us/library/ms648171.aspx) | Introduced into propsys.dll in 10.0.15063. |
| [PropVariantToGUID](https://msdn.microsoft.com/en-us/library/ms648203.aspx) | Introduced into propsys.dll in 10.0.15063. |
| [PropVariantToVariant](https://msdn.microsoft.com/en-us/library/Bb529975.aspx) | Introduced into propsys.dll in 10.0.15063. |
| [VariantToPropVariant](https://msdn.microsoft.com/en-us/library/Bb529976.aspx) | Introduced into propsys.dll in 10.0.15063. |
| [InitVariantFromBuffer](https://msdn.microsoft.com/en-us/library/ms648093.aspx) | Introduced into propsys.dll in 10.0.15063. |
| [PropVariantToBSTR](https://msdn.microsoft.com/en-us/library/ms648179.aspx) | Introduced into propsys.dll in 10.0.15063. |
| [PSCreateAdapterFromPropertyStore](https://msdn.microsoft.com/en-us/library/ms647443.aspx) | Introduced into propsys.dll in 10.0.15063. |
| [PSCreatePropertyStoreFromObject](https://msdn.microsoft.com/en-us/library/ms647449.aspx) | Introduced into propsys.dll in 10.0.15063. |
| [InitPropVariantFromCLSID](https://msdn.microsoft.com/en-us/library/ms647963.aspx) | Introduced into propsys.dll in 10.0.15063. |
| [InitPropVariantFromFileTime](https://msdn.microsoft.com/en-us/library/ms647966.aspx) | Introduced into propsys.dll in 10.0.15063. |
| [VariantToGUID](https://msdn.microsoft.com/en-us/library/ms648318.aspx) | Introduced into propsys.dll in 10.0.15063. |


## APIs from rpcrt4.dll

| API | Requirements |
| -----| --------------|
| CreateProxyFromTypeInfo | Introduced into rpcrt4.dll in 10.0.10240. |
| CreateStubFromTypeInfo | Introduced into rpcrt4.dll in 10.0.10240. |
| [CStdStubBuffer_AddRef](https://msdn.microsoft.com/en-us/library/windows/desktop/aa373611.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| [CStdStubBuffer_Connect](https://msdn.microsoft.com/en-us/library/windows/desktop/aa373612.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| [CStdStubBuffer_CountRefs](https://msdn.microsoft.com/en-us/library/windows/desktop/aa373613.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| [CStdStubBuffer_DebugServerQueryInterface](https://msdn.microsoft.com/en-us/library/windows/desktop/aa373614.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| [CStdStubBuffer_DebugServerRelease](https://msdn.microsoft.com/en-us/library/windows/desktop/aa373615.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| [CStdStubBuffer_Disconnect](https://msdn.microsoft.com/en-us/library/windows/desktop/aa373616.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| [CStdStubBuffer_Invoke](https://msdn.microsoft.com/en-us/library/windows/desktop/aa373617.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| [CStdStubBuffer_IsIIDSupported](https://msdn.microsoft.com/en-us/library/windows/desktop/aa373618.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| [CStdStubBuffer_QueryInterface](https://msdn.microsoft.com/en-us/library/windows/desktop/aa373619.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| [IUnknown_AddRef_Proxy](https://msdn.microsoft.com/en-us/library/windows/desktop/aa373957.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| [IUnknown_QueryInterface_Proxy](https://msdn.microsoft.com/en-us/library/windows/desktop/aa373958.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| [IUnknown_Release_Proxy](https://msdn.microsoft.com/en-us/library/windows/desktop/aa373959.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| [Ndr64AsyncClientCall](https://msdn.microsoft.com/en-us/library/windows/desktop/mt728979.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| Ndr64AsyncServerCall64 | Introduced into rpcrt4.dll in 10.0.10240. |
| [Ndr64AsyncServerCallAll](https://msdn.microsoft.com/en-us/library/windows/desktop/mt728980.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrAllocate | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrAsyncClientCall](https://msdn.microsoft.com/en-us/library/windows/desktop/aa374207.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrAsyncServerCall](https://msdn.microsoft.com/en-us/library/windows/desktop/mt728981.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrByteCountPointerBufferSize | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrByteCountPointerFree | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrByteCountPointerMarshall | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrByteCountPointerUnmarshall | Introduced into rpcrt4.dll in 10.0.10240. |
| NDRCContextBinding | Introduced into rpcrt4.dll in 10.0.10240. |
| NDRCContextMarshall | Introduced into rpcrt4.dll in 10.0.10240. |
| NDRCContextUnmarshall | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrClearOutParameters](https://msdn.microsoft.com/en-us/library/Aa374209.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrClientCall2](https://msdn.microsoft.com/en-us/library/windows/desktop/aa374215.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrClientCall3](https://msdn.microsoft.com/en-us/library/windows/desktop/mt712330.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrClientContextMarshall | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrClientContextUnmarshall | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrClientInitialize | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrClientInitializeNew | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrComplexArrayBufferSize](https://msdn.microsoft.com/en-us/library/Bb432364.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrComplexArrayFree | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrComplexArrayMarshall](https://msdn.microsoft.com/en-us/library/Bb432365.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrComplexArrayMemorySize | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrComplexArrayUnmarshall](https://msdn.microsoft.com/en-us/library/Bb432366.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrComplexStructBufferSize](https://msdn.microsoft.com/en-us/library/Bb432367.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrComplexStructFree | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrComplexStructMarshall](https://msdn.microsoft.com/en-us/library/Bb432368.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrComplexStructMemorySize | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrComplexStructUnmarshall](https://msdn.microsoft.com/en-us/library/Bb432369.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrConformantArrayBufferSize | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrConformantArrayFree | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrConformantArrayMarshall | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrConformantArrayMemorySize | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrConformantArrayUnmarshall](https://msdn.microsoft.com/en-us/library/Aa374216.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrConformantStringBufferSize](https://msdn.microsoft.com/en-us/library/windows/desktop/aa374220.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrConformantStringMarshall](https://msdn.microsoft.com/en-us/library/windows/desktop/aa374223.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrConformantStringMemorySize | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrConformantStringUnmarshall](https://msdn.microsoft.com/en-us/library/windows/desktop/aa374225.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
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
| [NdrContextHandleInitialize](https://msdn.microsoft.com/en-us/library/windows/desktop/aa374229.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrContextHandleSize](https://msdn.microsoft.com/en-us/library/windows/desktop/aa374236.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrConvert](https://msdn.microsoft.com/en-us/library/Aa374239.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrConvert2 | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrCorrelationFree | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrCorrelationInitialize | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrCorrelationPass | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrCreateServerInterfaceFromStub | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrCStdStubBuffer_Release](https://msdn.microsoft.com/en-us/library/windows/desktop/aa374242.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrCStdStubBuffer2_Release](https://msdn.microsoft.com/en-us/library/windows/desktop/aa374240.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrDllCanUnloadNow](https://msdn.microsoft.com/en-us/library/windows/desktop/aa374245.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrDllGetClassObject](https://msdn.microsoft.com/en-us/library/windows/desktop/aa374251.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrDllRegisterProxy](https://msdn.microsoft.com/en-us/library/windows/desktop/aa374255.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrDllUnregisterProxy](https://msdn.microsoft.com/en-us/library/windows/desktop/aa374257.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
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
| [NdrGetUserMarshalInfo](https://msdn.microsoft.com/en-us/library/windows/desktop/aa374262.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrInterfacePointerBufferSize](https://msdn.microsoft.com/en-us/library/windows/desktop/aa374265.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrInterfacePointerFree](https://msdn.microsoft.com/en-us/library/windows/desktop/aa374269.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrInterfacePointerMarshall](https://msdn.microsoft.com/en-us/library/windows/desktop/aa374272.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrInterfacePointerMemorySize | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrInterfacePointerUnmarshall](https://msdn.microsoft.com/en-us/library/windows/desktop/aa374278.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
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
| [NdrOleAllocate](https://msdn.microsoft.com/en-us/library/windows/desktop/aa374280.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrOleFree](https://msdn.microsoft.com/en-us/library/windows/desktop/aa374285.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrPartialIgnoreClientBufferSize | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrPartialIgnoreClientMarshall | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrPartialIgnoreServerInitialize | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrPartialIgnoreServerUnmarshall | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrPointerBufferSize](https://msdn.microsoft.com/en-us/library/windows/desktop/aa374289.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrPointerFree](https://msdn.microsoft.com/en-us/library/windows/desktop/aa374291.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrPointerMarshall](https://msdn.microsoft.com/en-us/library/windows/desktop/aa374293.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrPointerMemorySize | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrPointerUnmarshall](https://msdn.microsoft.com/en-us/library/windows/desktop/aa374296.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrProxyErrorHandler](https://msdn.microsoft.com/en-us/library/windows/desktop/aa374299.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
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
| [NdrServerCall2](https://msdn.microsoft.com/en-us/library/windows/desktop/mt728982.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrServerCallAll](https://msdn.microsoft.com/en-us/library/windows/desktop/mt728983.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrServerCallNdr64 | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrServerContextMarshall | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrServerContextNewMarshall | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrServerContextNewUnmarshall | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrServerContextUnmarshall | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrServerInitialize | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrServerInitializeMarshall | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrServerInitializeNew | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrServerInitializePartial | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrServerInitializeUnmarshall | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrSimpleStructBufferSize](https://msdn.microsoft.com/en-us/library/Bb432370.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrSimpleStructFree | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrSimpleStructMarshall](https://msdn.microsoft.com/en-us/library/Bb432371.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrSimpleStructMemorySize | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrSimpleStructUnmarshall](https://msdn.microsoft.com/en-us/library/Bb432372.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrSimpleTypeMarshall](https://msdn.microsoft.com/en-us/library/windows/desktop/aa374313.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrSimpleTypeUnmarshall](https://msdn.microsoft.com/en-us/library/windows/desktop/aa374315.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrStubCall2](https://msdn.microsoft.com/en-us/library/windows/desktop/aa374317.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrStubCall3](https://msdn.microsoft.com/en-us/library/windows/desktop/mt728984.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrStubForwardingFunction](https://msdn.microsoft.com/en-us/library/windows/desktop/aa374320.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrUserMarshalBufferSize](https://msdn.microsoft.com/en-us/library/windows/desktop/aa374329.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrUserMarshalFree](https://msdn.microsoft.com/en-us/library/windows/desktop/aa374332.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrUserMarshalMarshall](https://msdn.microsoft.com/en-us/library/windows/desktop/aa374334.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrUserMarshalMemorySize | Introduced into rpcrt4.dll in 10.0.10240. |
| NdrUserMarshalSimpleTypeConvert | Introduced into rpcrt4.dll in 10.0.10240. |
| [NdrUserMarshalUnmarshall](https://msdn.microsoft.com/en-us/library/Bb432373.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
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
| [RpcSmAllocate](https://msdn.microsoft.com/en-us/library/windows/desktop/aa378458.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| [RpcSmClientFree](https://msdn.microsoft.com/en-us/library/windows/desktop/aa378459.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| [RpcSmDestroyClientContext](https://msdn.microsoft.com/en-us/library/windows/desktop/aa378460.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| [RpcSmDisableAllocate](https://msdn.microsoft.com/en-us/library/windows/desktop/aa378461.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| [RpcSmEnableAllocate](https://msdn.microsoft.com/en-us/library/windows/desktop/aa378462.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| [RpcSmFree](https://msdn.microsoft.com/en-us/library/windows/desktop/aa378463.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| [RpcSmGetThreadHandle](https://msdn.microsoft.com/en-us/library/windows/desktop/aa378464.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| [RpcSmSetClientAllocFree](https://msdn.microsoft.com/en-us/library/windows/desktop/aa378465.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| [RpcSmSetThreadHandle](https://msdn.microsoft.com/en-us/library/windows/desktop/aa378466.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| [RpcSmSwapClientAllocFree](https://msdn.microsoft.com/en-us/library/windows/desktop/aa378467.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| [RpcSsAllocate](https://msdn.microsoft.com/en-us/library/windows/desktop/aa378468.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| [RpcSsDestroyClientContext](https://msdn.microsoft.com/en-us/library/windows/desktop/aa378471.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| [RpcSsDisableAllocate](https://msdn.microsoft.com/en-us/library/windows/desktop/aa378472.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| [RpcSsEnableAllocate](https://msdn.microsoft.com/en-us/library/windows/desktop/aa378474.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| [RpcSsFree](https://msdn.microsoft.com/en-us/library/windows/desktop/aa378475.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| [RpcSsGetThreadHandle](https://msdn.microsoft.com/en-us/library/windows/desktop/aa378476.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| [RpcSsSetClientAllocFree](https://msdn.microsoft.com/en-us/library/windows/desktop/aa378477.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| [RpcSsSetThreadHandle](https://msdn.microsoft.com/en-us/library/windows/desktop/aa378478.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| [RpcSsSwapClientAllocFree](https://msdn.microsoft.com/en-us/library/windows/desktop/aa378479.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| [RpcUserFree](https://msdn.microsoft.com/en-us/library/windows/desktop/mt297501.aspx) | Introduced into rpcrt4.dll in 10.0.10240. |
| [UuidCreate](https://msdn.microsoft.com/en-us/library/Aa379205.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [RpcAsyncAbortCall](https://msdn.microsoft.com/en-us/library/Aa375565.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [RpcAsyncCompleteCall](https://msdn.microsoft.com/en-us/library/Aa375572.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [RpcAsyncInitializeHandle](https://msdn.microsoft.com/en-us/library/Aa375578.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [RpcBindingFree](https://msdn.microsoft.com/en-us/library/Aa375588.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [RpcBindingSetOption](https://msdn.microsoft.com/en-us/library/Aa375611.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [RpcBindingToStringBindingW](https://msdn.microsoft.com/en-us/library/Aa375612.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [RpcRaiseException](https://msdn.microsoft.com/en-us/library/Aa378429.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [RpcStringBindingParseW](https://msdn.microsoft.com/en-us/library/Aa378482.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [RpcStringFreeW](https://msdn.microsoft.com/en-us/library/Aa378483.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [RpcBindingFromStringBindingW](https://msdn.microsoft.com/en-us/library/Aa375590.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [RpcBindingSetAuthInfoExW](https://msdn.microsoft.com/en-us/library/Aa375608.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [RpcEpResolveBinding](https://msdn.microsoft.com/en-us/library/Aa375645.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [RpcMgmtInqStats](https://msdn.microsoft.com/en-us/library/Aa375759.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [RpcStringBindingComposeW](https://msdn.microsoft.com/en-us/library/Aa378481.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [RpcExceptionFilter](https://msdn.microsoft.com/en-us/library/JJ203733.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [RpcAsyncCancelCall](https://msdn.microsoft.com/en-us/library/Aa375570.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [UuidFromStringW](https://msdn.microsoft.com/en-us/library/Aa379336.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [UuidToStringW](https://msdn.microsoft.com/en-us/library/Aa379352.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [RpcBindingBind](https://msdn.microsoft.com/en-us/library/Aa375583.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [RpcBindingCreateW](https://msdn.microsoft.com/en-us/library/Aa375587.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [RpcBindingSetAuthInfoA](https://msdn.microsoft.com/en-us/library/Aa375606.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [RpcBindingSetAuthInfoW](https://msdn.microsoft.com/en-us/library/Aa375606.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [RpcStringFreeA](https://msdn.microsoft.com/en-us/library/Aa378483.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [UuidToStringA](https://msdn.microsoft.com/en-us/library/Aa379352.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [UuidCompare](https://msdn.microsoft.com/en-us/library/Aa379201.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [RpcMgmtIsServerListening](https://msdn.microsoft.com/en-us/library/Aa375763.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [RpcMgmtSetCancelTimeout](https://msdn.microsoft.com/en-us/library/Aa375771.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [RpcBindingUnbind](https://msdn.microsoft.com/en-us/library/Aa375613.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [UuidEqual](https://msdn.microsoft.com/en-us/library/Aa379329.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [RpcBindingInqObject](https://msdn.microsoft.com/en-us/library/Aa375598.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [UuidIsNil](https://msdn.microsoft.com/en-us/library/Aa379347.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [RpcBindingReset](https://msdn.microsoft.com/en-us/library/Aa375603.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [RpcMgmtSetComTimeout](https://msdn.microsoft.com/en-us/library/Aa375779.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [UuidFromStringA](https://msdn.microsoft.com/en-us/library/Aa379336.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [RpcMgmtInqServerPrincNameW](https://msdn.microsoft.com/en-us/library/Aa375756.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [RpcNetworkIsProtseqValidW](https://msdn.microsoft.com/en-us/library/Aa375804.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [RpcNetworkIsProtseqValidA](https://msdn.microsoft.com/en-us/library/Aa375804.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [RpcAsyncGetCallStatus](https://msdn.microsoft.com/en-us/library/Aa375576.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [RpcBindingCopy](https://msdn.microsoft.com/en-us/library/Aa375585.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [RpcBindingInqAuthInfoExW](https://msdn.microsoft.com/en-us/library/Aa375595.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [RpcErrorAddRecord](https://msdn.microsoft.com/en-us/library/Aa375658.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [RpcErrorEndEnumeration](https://msdn.microsoft.com/en-us/library/Aa375664.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [RpcErrorGetNextRecord](https://msdn.microsoft.com/en-us/library/Aa375668.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [RpcErrorStartEnumeration](https://msdn.microsoft.com/en-us/library/Aa375686.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [UuidCreateSequential](https://msdn.microsoft.com/en-us/library/Aa379322.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [UuidHash](https://msdn.microsoft.com/en-us/library/Aa379343.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [RpcBindingFromStringBindingA](https://msdn.microsoft.com/en-us/library/Aa375590.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [RpcStringBindingComposeA](https://msdn.microsoft.com/en-us/library/Aa378481.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [RpcBindingSetAuthInfoExA](https://msdn.microsoft.com/en-us/library/Aa375608.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [UuidCreateNil](https://msdn.microsoft.com/en-us/library/Aa379262.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [RpcBindingToStringBindingA](https://msdn.microsoft.com/en-us/library/Aa375612.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [RpcTestCancel](https://msdn.microsoft.com/en-us/library/Aa378484.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [RpcBindingInqAuthInfoW](https://msdn.microsoft.com/en-us/library/Aa375593.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [RpcBindingSetObject](https://msdn.microsoft.com/en-us/library/Aa375609.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [RpcErrorGetNumberOfRecords](https://msdn.microsoft.com/en-us/library/Aa375671.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [RpcStringBindingParseA](https://msdn.microsoft.com/en-us/library/Aa378482.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [RpcBindingInqAuthInfoA](https://msdn.microsoft.com/en-us/library/Aa375593.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [RpcErrorClearInformation](https://msdn.microsoft.com/en-us/library/Aa375661.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [RpcErrorLoadErrorInfo](https://msdn.microsoft.com/en-us/library/Aa375677.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [RpcErrorResetEnumeration](https://msdn.microsoft.com/en-us/library/Aa375679.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [RpcErrorSaveErrorInfo](https://msdn.microsoft.com/en-us/library/Aa375684.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [DceErrorInqTextA](https://msdn.microsoft.com/en-us/library/Aa373623.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [DceErrorInqTextW](https://msdn.microsoft.com/en-us/library/Aa373623.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [RpcBindingCreateA](https://msdn.microsoft.com/en-us/library/Aa375587.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [RpcBindingInqAuthInfoExA](https://msdn.microsoft.com/en-us/library/Aa375595.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [RpcBindingInqOption](https://msdn.microsoft.com/en-us/library/Aa375600.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |
| [RpcMgmtInqServerPrincNameA](https://msdn.microsoft.com/en-us/library/Aa375756.aspx) | Introduced into rpcrt4.dll in 10.0.15063. |


## APIs from uiautomationcore.dll

| API | Requirements |
| -----| --------------|
| [UiaClientsAreListening](https://msdn.microsoft.com/en-us/library/windows/desktop/ee671704.aspx) | Introduced into uiautomationcore.dll in 10.0.10240. Moved into ext-ms-win-uiacore-l1-1-3.dll in 10.0.15063. |
| [UiaDisconnectAllProviders](https://msdn.microsoft.com/en-us/library/windows/desktop/hh437311.aspx) | Introduced into uiautomationcore.dll in 10.0.10240. Moved into ext-ms-win-uiacore-l1-1-3.dll in 10.0.15063. |
| [UiaDisconnectProvider](https://msdn.microsoft.com/en-us/library/windows/desktop/hh437312.aspx) | Introduced into uiautomationcore.dll in 10.0.10240. Moved into ext-ms-win-uiacore-l1-1-3.dll in 10.0.15063. |
| [UiaGetReservedMixedAttributeValue](https://msdn.microsoft.com/en-us/library/windows/desktop/ee684038.aspx) | Introduced into uiautomationcore.dll in 10.0.10240. Moved into ext-ms-win-uiacore-l1-1-3.dll in 10.0.15063. |
| [UiaGetReservedNotSupportedValue](https://msdn.microsoft.com/en-us/library/windows/desktop/ee684039.aspx) | Introduced into uiautomationcore.dll in 10.0.10240. Moved into ext-ms-win-uiacore-l1-1-3.dll in 10.0.15063. |
| [UiaHostProviderFromHwnd](https://msdn.microsoft.com/en-us/library/windows/desktop/ee684044.aspx) | Introduced into uiautomationcore.dll in 10.0.10240. Moved into ext-ms-win-uiacore-l1-1-0.dll in 10.0.15063. |
| [UiaProviderForNonClient](https://msdn.microsoft.com/en-us/library/windows/desktop/hh437314.aspx) | Introduced into uiautomationcore.dll in 10.0.10240. |
| [UiaProviderFromIAccessible](https://msdn.microsoft.com/en-us/library/windows/desktop/hh437315.aspx) | Introduced into uiautomationcore.dll in 10.0.10240. |
| [UiaRaiseAsyncContentLoadedEvent](https://msdn.microsoft.com/en-us/library/windows/desktop/ee684061.aspx) | Introduced into uiautomationcore.dll in 10.0.10240. |
| [UiaRaiseAutomationEvent](https://msdn.microsoft.com/en-us/library/windows/desktop/ee684062.aspx) | Introduced into uiautomationcore.dll in 10.0.10240. Moved into ext-ms-win-uiacore-l1-1-3.dll in 10.0.15063. |
| [UiaRaiseAutomationPropertyChangedEvent](https://msdn.microsoft.com/en-us/library/windows/desktop/ee671601.aspx) | Introduced into uiautomationcore.dll in 10.0.10240. Moved into ext-ms-win-uiacore-l1-1-3.dll in 10.0.15063. |
| [UiaRaiseStructureChangedEvent](https://msdn.microsoft.com/en-us/library/windows/desktop/ee684063.aspx) | Introduced into uiautomationcore.dll in 10.0.10240. Moved into ext-ms-win-uiacore-l1-1-3.dll in 10.0.15063. |
| [UiaRaiseTextEditTextChangedEvent](https://msdn.microsoft.com/en-us/library/windows/desktop/dn302213.aspx) | Introduced into uiautomationcore.dll in 10.0.10240. Moved into ext-ms-win-uiacore-l1-1-3.dll in 10.0.15063. |
| [UiaReturnRawElementProvider](https://msdn.microsoft.com/en-us/library/windows/desktop/ee684069.aspx) | Introduced into uiautomationcore.dll in 10.0.10240. Moved into ext-ms-win-uiacore-l1-1-0.dll in 10.0.15063. |
| [UiaRaiseChangesEvent](https://msdn.microsoft.com/en-us/library/windows/desktop/mt733044.aspx) | Introduced into uiautomationcore.dll in 10.0.14393. Moved into ext-ms-win-uiacore-l1-1-3.dll in 10.0.15063. |


## APIs from urlmon.dll

| API | Requirements |
| -----| --------------|
| [CreateUri](https://msdn.microsoft.com/en-us/library/windows/desktop/ms775098.aspx) | Introduced into urlmon.dll in 10.0.10240. Moved into ext-ms-win-core-iuri-l1-1-0.dll in 10.0.15063. |
| [CreateUriWithFragment](https://msdn.microsoft.com/en-us/library/windows/desktop/ms775100.aspx) | Introduced into urlmon.dll in 10.0.10240. Moved into ext-ms-win-core-iuri-l1-1-0.dll in 10.0.15063. |
| UrlMkGetSessionOption | Introduced into urlmon.dll in 10.0.15063. |
| UrlMkSetSessionOption | Introduced into urlmon.dll in 10.0.15063. |


## APIs from webservices.dll

| API | Requirements |
| -----| --------------|
| [WsAbandonCall](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430472.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsAbandonMessage](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430473.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsAbortChannel](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430474.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsAbortServiceProxy](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430477.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsAddCustomHeader](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430479.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsAddErrorString](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430480.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsAddMappedHeader](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430481.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsAddressMessage](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430482.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsAlloc](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430483.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsAsyncExecute](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430484.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsCall](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430485.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsCheckMustUnderstandHeaders](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430486.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsCloseChannel](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430487.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsCloseServiceProxy](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430490.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsCombineUrl](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430491.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsCopyError](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430492.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsCopyNode](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430493.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsCreateChannel](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430495.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsCreateError](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430497.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsCreateFaultFromError](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430498.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsCreateHeap](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430499.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsCreateMessage](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430501.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsCreateMessageForChannel](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430502.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsCreateMetadata](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430503.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsCreateReader](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430504.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsCreateServiceProxy](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430507.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsCreateServiceProxyFromTemplate](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430508.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsCreateWriter](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430509.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsCreateXmlBuffer](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430510.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsCreateXmlSecurityToken](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430511.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsDateTimeToFileTime](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430512.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsDecodeUrl](https://msdn.microsoft.com/en-us/library/Dd430513.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsEncodeUrl](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430516.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsEndReaderCanonicalization](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430517.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsEndWriterCanonicalization](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430518.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsFileTimeToDateTime](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430519.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsFillBody](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430520.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsFillReader](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430521.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsFindAttribute](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430522.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsFlushBody](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430523.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsFlushWriter](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430524.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsFreeChannel](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430525.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsFreeError](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430526.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsFreeHeap](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430527.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsFreeMessage](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430529.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsFreeMetadata](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430530.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsFreeReader](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430531.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsFreeSecurityToken](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430532.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsFreeServiceProxy](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430534.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsFreeWriter](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430535.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsGetChannelProperty](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430536.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsGetCustomHeader](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430537.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsGetDictionary](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430538.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsGetErrorProperty](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430539.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsGetErrorString](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430540.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsGetFaultErrorDetail](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430541.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsGetFaultErrorProperty](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430542.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsGetHeader](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430543.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsGetHeaderAttributes](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430544.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsGetHeapProperty](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430545.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsGetMappedHeader](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430547.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsGetMessageProperty](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430548.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsGetMetadataEndpoints](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430549.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsGetMetadataProperty](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430550.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsGetMissingMetadataDocumentAddress](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430551.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsGetNamespaceFromPrefix](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430552.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsGetPolicyAlternativeCount](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430554.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsGetPolicyProperty](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430556.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsGetPrefixFromNamespace](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430557.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsGetReaderNode](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430558.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsGetReaderPosition](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430559.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsGetReaderProperty](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430560.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsGetSecurityContextProperty](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430561.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsGetSecurityTokenProperty](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430562.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsGetServiceProxyProperty](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430564.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsGetWriterPosition](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430565.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsGetWriterProperty](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430566.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsGetXmlAttribute](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430567.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsInitializeMessage](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430568.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsMarkHeaderAsUnderstood](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430569.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsMatchPolicyAlternative](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430570.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsMoveReader](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430571.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsMoveWriter](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430572.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsOpenChannel](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430574.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsOpenServiceProxy](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430577.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsPullBytes](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430578.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsPushBytes](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430580.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsReadArray](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430581.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsReadAttribute](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430582.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsReadBody](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430583.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsReadBytes](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430584.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsReadChars](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430585.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsReadCharsUtf8](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430586.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsReadElement](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430587.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsReadEndAttribute](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430588.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsReadEndElement](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430589.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsReadEndpointAddressExtension](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430590.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsReadEnvelopeEnd](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430591.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsReadEnvelopeStart](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430592.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsReadMessageEnd](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430593.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsReadMessageStart](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430594.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsReadMetadata](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430595.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsReadNode](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430596.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsReadQualifiedName](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430597.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsReadStartAttribute](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430598.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsReadStartElement](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430599.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsReadToStartElement](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430600.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsReadType](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430601.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsReadValue](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430602.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsReadXmlBuffer](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430603.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsReadXmlBufferFromBytes](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430604.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsReceiveMessage](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430605.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsRemoveCustomHeader](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430607.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsRemoveHeader](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430608.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsRemoveMappedHeader](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430609.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsRemoveNode](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430610.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsRequestReply](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430611.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsRequestSecurityToken](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430612.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsResetChannel](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430613.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsResetError](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430614.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsResetHeap](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430615.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsResetMessage](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430617.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsResetMetadata](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430618.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsResetServiceProxy](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430620.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsRevokeSecurityContext](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430621.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsSendFaultMessageForError](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430622.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsSendMessage](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430623.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsSendReplyMessage](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430624.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsSetChannelProperty](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430626.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsSetErrorProperty](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430627.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsSetFaultErrorDetail](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430628.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsSetFaultErrorProperty](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430629.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsSetHeader](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430630.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsSetInput](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430631.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsSetInputToBuffer](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430632.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsSetMessageProperty](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430634.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsSetOutput](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430635.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsSetOutputToBuffer](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430636.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsSetReaderPosition](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430637.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsSetWriterPosition](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430638.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsShutdownSessionChannel](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430639.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsSkipNode](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430640.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsStartReaderCanonicalization](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430641.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsStartWriterCanonicalization](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430642.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsTrimXmlWhitespace](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430643.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsVerifyXmlNCName](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430645.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsWriteArray](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430646.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsWriteAttribute](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430647.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsWriteBody](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430648.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsWriteBytes](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430649.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsWriteChars](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430650.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsWriteCharsUtf8](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430651.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsWriteElement](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430652.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsWriteEndAttribute](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430653.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsWriteEndCData](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430654.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsWriteEndElement](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430655.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsWriteEndStartElement](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430656.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsWriteEnvelopeEnd](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430657.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsWriteEnvelopeStart](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430658.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsWriteMessageEnd](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430659.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsWriteMessageStart](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430660.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsWriteNode](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430661.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsWriteQualifiedName](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430662.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsWriteStartAttribute](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430663.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsWriteStartCData](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430664.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsWriteStartElement](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430665.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsWriteText](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430667.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsWriteType](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430668.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsWriteValue](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430669.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsWriteXmlBuffer](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430670.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsWriteXmlBufferToBytes](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430671.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsWriteXmlnsAttribute](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430672.aspx) | Introduced into webservices.dll in 10.0.10240. |
| [WsXmlStringEquals](https://msdn.microsoft.com/en-us/library/windows/desktop/dd430673.aspx) | Introduced into webservices.dll in 10.0.10240. |


## APIs from windows.data.pdf.dll

| API | Requirements |
| -----| --------------|
| [PdfCreateRenderer](https://msdn.microsoft.com/en-us/library/windows/desktop/dn302145.aspx) | Introduced into windows.data.pdf.dll in 10.0.10240. |


## APIs from windows.networking.dll

| API | Requirements |
| -----| --------------|
| [SetSocketMediaStreamingMode](https://msdn.microsoft.com/en-us/library/windows/desktop/hh994468.aspx) | Introduced into windows.networking.dll in 10.0.10240. |


## APIs from windowscodecs.dll

| API | Requirements |
| -----| --------------|
| [WICConvertBitmapSource](https://msdn.microsoft.com/en-us/library/windows/desktop/ee719819.aspx) | Introduced into windowscodecs.dll in 10.0.10240. |
| [WICCreateBitmapFromSection](https://msdn.microsoft.com/en-us/library/windows/desktop/ee719820.aspx) | Introduced into windowscodecs.dll in 10.0.10240. |
| [WICCreateBitmapFromSectionEx](https://msdn.microsoft.com/en-us/library/windows/desktop/ee719821.aspx) | Introduced into windowscodecs.dll in 10.0.10240. |
| [WICGetMetadataContentSize](https://msdn.microsoft.com/en-us/library/windows/desktop/ee719825.aspx) | Introduced into windowscodecs.dll in 10.0.10240. |
| [WICMapGuidToShortName](https://msdn.microsoft.com/en-us/library/windows/desktop/ee719835.aspx) | Introduced into windowscodecs.dll in 10.0.10240. |
| [WICMapSchemaToName](https://msdn.microsoft.com/en-us/library/windows/desktop/ee719836.aspx) | Introduced into windowscodecs.dll in 10.0.10240. |
| [WICMapShortNameToGuid](https://msdn.microsoft.com/en-us/library/windows/desktop/ee719837.aspx) | Introduced into windowscodecs.dll in 10.0.10240. |
| [WICMatchMetadataContent](https://msdn.microsoft.com/en-us/library/windows/desktop/ee719838.aspx) | Introduced into windowscodecs.dll in 10.0.10240. |
| [WICSerializeMetadataContent](https://msdn.microsoft.com/en-us/library/windows/desktop/ee719865.aspx) | Introduced into windowscodecs.dll in 10.0.10240. |


## APIs from ws2_32.dll

| API | Requirements |
| -----| --------------|
| [__WSAFDIsSet](https://msdn.microsoft.com/en-us/library/windows/desktop/ms741578.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [accept](https://msdn.microsoft.com/en-us/library/windows/desktop/ms737526.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [bind](https://msdn.microsoft.com/en-us/library/windows/desktop/ms737550.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [closesocket](https://msdn.microsoft.com/en-us/library/windows/desktop/ms737582.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [connect](https://msdn.microsoft.com/en-us/library/windows/desktop/ms737625.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [freeaddrinfo](https://msdn.microsoft.com/en-us/library/windows/desktop/ms737931.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [FreeAddrInfoExW](https://msdn.microsoft.com/en-us/library/windows/desktop/ms737906.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [FreeAddrInfoW](https://msdn.microsoft.com/en-us/library/windows/desktop/ms737912.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [getaddrinfo](https://msdn.microsoft.com/en-us/library/windows/desktop/ms738520.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [GetAddrInfoExCancel](https://msdn.microsoft.com/en-us/library/windows/desktop/hh448782.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [GetAddrInfoExOverlappedResult](https://msdn.microsoft.com/en-us/library/windows/desktop/hh448783.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [GetAddrInfoExW](https://msdn.microsoft.com/en-us/library/windows/desktop/ms738518.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [GetAddrInfoW](https://msdn.microsoft.com/en-us/library/windows/desktop/ms738519.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [gethostbyaddr](https://msdn.microsoft.com/en-us/library/windows/desktop/ms738521.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [gethostbyname](https://msdn.microsoft.com/en-us/library/windows/desktop/ms738524.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [gethostname](https://msdn.microsoft.com/en-us/library/windows/desktop/ms738527.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [GetHostNameW](https://msdn.microsoft.com/en-us/library/windows/desktop/dn793576.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [getnameinfo](https://msdn.microsoft.com/en-us/library/windows/desktop/ms738532.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [GetNameInfoW](https://msdn.microsoft.com/en-us/library/windows/desktop/ms738531.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [getpeername](https://msdn.microsoft.com/en-us/library/windows/desktop/ms738533.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [getprotobyname](https://msdn.microsoft.com/en-us/library/windows/desktop/ms738534.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [getprotobynumber](https://msdn.microsoft.com/en-us/library/windows/desktop/ms738537.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [getservbyname](https://msdn.microsoft.com/en-us/library/windows/desktop/ms738538.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [getservbyport](https://msdn.microsoft.com/en-us/library/windows/desktop/ms738541.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [getsockname](https://msdn.microsoft.com/en-us/library/windows/desktop/ms738543.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [getsockopt](https://msdn.microsoft.com/en-us/library/windows/desktop/ms738544.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [htonl](https://msdn.microsoft.com/en-us/library/windows/desktop/ms738556.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [htons](https://msdn.microsoft.com/en-us/library/windows/desktop/ms738557.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [inet_addr](https://msdn.microsoft.com/en-us/library/windows/desktop/ms738563.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [inet_ntoa](https://msdn.microsoft.com/en-us/library/windows/desktop/ms738564.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [inet_ntop](https://msdn.microsoft.com/en-us/library/Cc805843.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [inet_pton](https://msdn.microsoft.com/en-us/library/Cc805844.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [InetNtopW](https://msdn.microsoft.com/en-us/library/windows/desktop/cc805843.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [InetPtonW](https://msdn.microsoft.com/en-us/library/windows/desktop/cc805844.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [ioctlsocket](https://msdn.microsoft.com/en-us/library/windows/desktop/ms738573.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [listen](https://msdn.microsoft.com/en-us/library/windows/desktop/ms739168.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [ntohl](https://msdn.microsoft.com/en-us/library/windows/desktop/ms740069.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [ntohs](https://msdn.microsoft.com/en-us/library/windows/desktop/ms740075.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [recv](https://msdn.microsoft.com/en-us/library/windows/desktop/ms740121.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [recvfrom](https://msdn.microsoft.com/en-us/library/windows/desktop/ms740120.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [select](https://msdn.microsoft.com/en-us/library/windows/desktop/ms740141.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [send](https://msdn.microsoft.com/en-us/library/windows/desktop/ms740149.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [sendto](https://msdn.microsoft.com/en-us/library/windows/desktop/ms740148.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [SetAddrInfoExW](https://msdn.microsoft.com/en-us/library/windows/desktop/ms740473.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [setsockopt](https://msdn.microsoft.com/en-us/library/windows/desktop/ms740476.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [shutdown](https://msdn.microsoft.com/en-us/library/windows/desktop/ms740481.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [socket](https://msdn.microsoft.com/en-us/library/windows/desktop/ms740506.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSAAccept](https://msdn.microsoft.com/en-us/library/windows/desktop/ms741513.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSAAddressToStringA](https://msdn.microsoft.com/en-us/library/windows/desktop/ms741516.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSAAddressToStringW](https://msdn.microsoft.com/en-us/library/windows/desktop/ms741516.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSACleanup](https://msdn.microsoft.com/en-us/library/windows/desktop/ms741549.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSACloseEvent](https://msdn.microsoft.com/en-us/library/windows/desktop/ms741551.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSAConnect](https://msdn.microsoft.com/en-us/library/windows/desktop/ms741559.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSAConnectByList](https://msdn.microsoft.com/en-us/library/windows/desktop/ms741554.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSAConnectByNameA](https://msdn.microsoft.com/en-us/library/windows/desktop/ms741557.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSAConnectByNameW](https://msdn.microsoft.com/en-us/library/windows/desktop/ms741557.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSACreateEvent](https://msdn.microsoft.com/en-us/library/windows/desktop/ms741561.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSADuplicateSocketA](https://msdn.microsoft.com/en-us/library/windows/desktop/ms741565.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSADuplicateSocketW](https://msdn.microsoft.com/en-us/library/windows/desktop/ms741565.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSAEnumNameSpaceProvidersA](https://msdn.microsoft.com/en-us/library/windows/desktop/ms741570.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSAEnumNameSpaceProvidersExA](https://msdn.microsoft.com/en-us/library/windows/desktop/ms741568.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSAEnumNameSpaceProvidersExW](https://msdn.microsoft.com/en-us/library/windows/desktop/ms741568.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSAEnumNameSpaceProvidersW](https://msdn.microsoft.com/en-us/library/windows/desktop/ms741570.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSAEnumNetworkEvents](https://msdn.microsoft.com/en-us/library/windows/desktop/ms741572.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSAEnumProtocolsA](https://msdn.microsoft.com/en-us/library/windows/desktop/ms741574.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSAEnumProtocolsW](https://msdn.microsoft.com/en-us/library/windows/desktop/ms741574.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSAEventSelect](https://msdn.microsoft.com/en-us/library/windows/desktop/ms741576.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSAGetLastError](https://msdn.microsoft.com/en-us/library/windows/desktop/ms741580.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSAGetOverlappedResult](https://msdn.microsoft.com/en-us/library/windows/desktop/ms741582.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSAGetServiceClassInfoW](https://msdn.microsoft.com/en-us/library/windows/desktop/ms741592.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSAGetServiceClassNameByClassIdW](https://msdn.microsoft.com/en-us/library/windows/desktop/ms741598.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSAHtonl](https://msdn.microsoft.com/en-us/library/windows/desktop/ms741604.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSAHtons](https://msdn.microsoft.com/en-us/library/windows/desktop/ms741609.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSAIoctl](https://msdn.microsoft.com/en-us/library/windows/desktop/ms741621.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSAJoinLeaf](https://msdn.microsoft.com/en-us/library/windows/desktop/ms741628.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSALookupServiceBeginA](https://msdn.microsoft.com/en-us/library/windows/desktop/ms741633.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSALookupServiceBeginW](https://msdn.microsoft.com/en-us/library/windows/desktop/ms741633.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSALookupServiceEnd](https://msdn.microsoft.com/en-us/library/windows/desktop/ms741637.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSALookupServiceNextA](https://msdn.microsoft.com/en-us/library/windows/desktop/ms741641.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSALookupServiceNextW](https://msdn.microsoft.com/en-us/library/windows/desktop/ms741641.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSANSPIoctl](https://msdn.microsoft.com/en-us/library/windows/desktop/ms741658.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSANtohl](https://msdn.microsoft.com/en-us/library/windows/desktop/ms741660.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSANtohs](https://msdn.microsoft.com/en-us/library/windows/desktop/ms741663.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSAPoll](https://msdn.microsoft.com/en-us/library/windows/desktop/ms741669.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSAProviderConfigChange](https://msdn.microsoft.com/en-us/library/windows/desktop/ms741677.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSARecv](https://msdn.microsoft.com/en-us/library/windows/desktop/ms741688.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSARecvFrom](https://msdn.microsoft.com/en-us/library/windows/desktop/ms741686.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSAResetEvent](https://msdn.microsoft.com/en-us/library/windows/desktop/ms741690.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSASend](https://msdn.microsoft.com/en-us/library/windows/desktop/ms742203.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSASendMsg](https://msdn.microsoft.com/en-us/library/windows/desktop/ms741692.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSASendTo](https://msdn.microsoft.com/en-us/library/windows/desktop/ms741693.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSASetEvent](https://msdn.microsoft.com/en-us/library/windows/desktop/ms742208.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSASetLastError](https://msdn.microsoft.com/en-us/library/windows/desktop/ms742209.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSASetServiceA](https://msdn.microsoft.com/en-us/library/windows/desktop/ms742211.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSASetServiceW](https://msdn.microsoft.com/en-us/library/windows/desktop/ms742211.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSASocketA](https://msdn.microsoft.com/en-us/library/windows/desktop/ms742212.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSASocketW](https://msdn.microsoft.com/en-us/library/windows/desktop/ms742212.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSAStartup](https://msdn.microsoft.com/en-us/library/windows/desktop/ms742213.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSAStringToAddressA](https://msdn.microsoft.com/en-us/library/windows/desktop/ms742214.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSAStringToAddressW](https://msdn.microsoft.com/en-us/library/windows/desktop/ms742214.aspx) | Introduced into ws2_32.dll in 10.0.10240. |
| [WSAWaitForMultipleEvents](https://msdn.microsoft.com/en-us/library/windows/desktop/ms742219.aspx) | Introduced into ws2_32.dll in 10.0.10240. |


## APIs from xaudio2_9.dll

| API | Requirements |
| -----| --------------|
| CreateAudioReverb | Introduced into xaudio2_9.dll in 10.0.10240. |
| CreateAudioVolumeMeter | Introduced into xaudio2_9.dll in 10.0.10240. |
| [CreateFX](https://msdn.microsoft.com/en-us/library/windows/desktop/hh405044.aspx) | Introduced into xaudio2_9.dll in 10.0.10240. |
| [X3DAudioCalculate](https://msdn.microsoft.com/en-us/library/windows/desktop/microsoft.directx_sdk.x3daudio.x3daudiocalculate.aspx) | Introduced into xaudio2_9.dll in 10.0.10240. |
| [X3DAudioInitialize](https://msdn.microsoft.com/en-us/library/windows/desktop/microsoft.directx_sdk.x3daudio.x3daudioinitialize.aspx) | Introduced into xaudio2_9.dll in 10.0.10240. |
| [XAudio2Create](https://msdn.microsoft.com/en-us/library/windows/desktop/microsoft.directx_sdk.xaudio2.xaudio2create.aspx) | Introduced into xaudio2_9.dll in 10.0.10240. |


## APIs from xinputuap.dll

| API | Requirements |
| -----| --------------|
| [XInputEnable](https://msdn.microsoft.com/en-us/library/windows/desktop/microsoft.directx_sdk.reference.xinputenable.aspx) | Introduced into xinputuap.dll in 10.0.10240. Moved into ext-ms-win-gaming-xinput-l1-1-0.dll in 10.0.15063. |
| [XInputGetAudioDeviceIds](https://msdn.microsoft.com/en-us/library/windows/desktop/microsoft.directx_sdk.reference.xinputgetaudiodeviceids.aspx) | Introduced into xinputuap.dll in 10.0.10240. Moved into ext-ms-win-gaming-xinput-l1-1-0.dll in 10.0.15063. |
| [XInputGetBatteryInformation](https://msdn.microsoft.com/en-us/library/windows/desktop/microsoft.directx_sdk.reference.xinputgetbatteryinformation.aspx) | Introduced into xinputuap.dll in 10.0.10240. Moved into ext-ms-win-gaming-xinput-l1-1-0.dll in 10.0.15063. |
| [XInputGetCapabilities](https://msdn.microsoft.com/en-us/library/windows/desktop/microsoft.directx_sdk.reference.xinputgetcapabilities.aspx) | Introduced into xinputuap.dll in 10.0.10240. Moved into ext-ms-win-gaming-xinput-l1-1-0.dll in 10.0.15063. |
| [XInputGetKeystroke](https://msdn.microsoft.com/en-us/library/windows/desktop/microsoft.directx_sdk.reference.xinputgetkeystroke.aspx) | Introduced into xinputuap.dll in 10.0.10240. Moved into ext-ms-win-gaming-xinput-l1-1-0.dll in 10.0.15063. |
| [XInputGetState](https://msdn.microsoft.com/en-us/library/windows/desktop/microsoft.directx_sdk.reference.xinputgetstate.aspx) | Introduced into xinputuap.dll in 10.0.10240. Moved into ext-ms-win-gaming-xinput-l1-1-0.dll in 10.0.15063. |
| [XInputSetState](https://msdn.microsoft.com/en-us/library/windows/desktop/microsoft.directx_sdk.reference.xinputsetstate.aspx) | Introduced into xinputuap.dll in 10.0.10240. Moved into ext-ms-win-gaming-xinput-l1-1-0.dll in 10.0.15063. |


## APIs from xmllite.dll

| API | Requirements |
| -----| --------------|
| [CreateXmlReader](https://msdn.microsoft.com/en-us/library/windows/desktop/ms752822.aspx) | Introduced into xmllite.dll in 10.0.10240. |
| [CreateXmlReaderInputWithEncodingCodePage](https://msdn.microsoft.com/en-us/library/windows/desktop/ms752859.aspx) | Introduced into xmllite.dll in 10.0.10240. |
| [CreateXmlReaderInputWithEncodingName](https://msdn.microsoft.com/en-us/library/windows/desktop/ms752899.aspx) | Introduced into xmllite.dll in 10.0.10240. |
| [CreateXmlWriter](https://msdn.microsoft.com/en-us/library/windows/desktop/ms752911.aspx) | Introduced into xmllite.dll in 10.0.10240. |
| [CreateXmlWriterOutputWithEncodingCodePage](https://msdn.microsoft.com/en-us/library/windows/desktop/ms753133.aspx) | Introduced into xmllite.dll in 10.0.10240. |
| [CreateXmlWriterOutputWithEncodingName](https://msdn.microsoft.com/en-us/library/windows/desktop/ms752894.aspx) | Introduced into xmllite.dll in 10.0.10240. |


## APIs from api-ms-win-core-file-l1-2-2.dll

| API | Requirements |
| -----| --------------|
| [CompareFileTime](https://msdn.microsoft.com/en-us/library/windows/desktop/ms724214.aspx) | Introduced into api-ms-win-core-file-l1-2-2.dll in 10.0.10586. Moved into api-ms-win-core-file-l1-2-1.dll in 10.0.14393. |


## APIs from api-ms-win-core-libraryloader-l1-2-1.dll

| API | Requirements |
| -----| --------------|
| [FreeLibraryAndExitThread](https://msdn.microsoft.com/en-us/library/windows/desktop/ms683153.aspx) | Introduced into api-ms-win-core-libraryloader-l1-2-1.dll in 10.0.10586. Moved into api-ms-win-core-libraryloader-l1-2-0.dll in 10.0.14393. |


## APIs from Bcrypt.dll

| API | Requirements |
| -----| --------------|
| BCryptCreateMultiHash | Introduced into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |
| BCryptProcessMultiOperations | Introduced into Bcrypt.dll in 10.0.10586. Moved into bcrypt.dll in 10.0.14393. |


## APIs from api-ms-win-core-featurestaging-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| GetFeatureEnabledState | Introduced into api-ms-win-core-featurestaging-l1-1-0.dll in 10.0.14393. Moved into api-ms-win-core-featurestaging-l1-1-1.dll in 10.0.15063. |
| RecordFeatureError | Introduced into api-ms-win-core-featurestaging-l1-1-0.dll in 10.0.14393. Moved into api-ms-win-core-featurestaging-l1-1-1.dll in 10.0.15063. |
| RecordFeatureUsage | Introduced into api-ms-win-core-featurestaging-l1-1-0.dll in 10.0.14393. Moved into api-ms-win-core-featurestaging-l1-1-1.dll in 10.0.15063. |
| SubscribeFeatureStateChangeNotification | Introduced into api-ms-win-core-featurestaging-l1-1-0.dll in 10.0.14393. Moved into api-ms-win-core-featurestaging-l1-1-1.dll in 10.0.15063. |
| UnsubscribeFeatureStateChangeNotification | Introduced into api-ms-win-core-featurestaging-l1-1-0.dll in 10.0.14393. Moved into api-ms-win-core-featurestaging-l1-1-1.dll in 10.0.15063. |


## APIs from api-ms-win-core-heap-l2-1-0.dll

| API | Requirements |
| -----| --------------|
| [GlobalAlloc](https://msdn.microsoft.com/en-us/library/windows/desktop/aa366574.aspx) | Introduced into api-ms-win-core-heap-l2-1-0.dll in 10.0.14393. |
| [GlobalFree](https://msdn.microsoft.com/en-us/library/windows/desktop/aa366579.aspx) | Introduced into api-ms-win-core-heap-l2-1-0.dll in 10.0.14393. |
| [LocalAlloc](https://msdn.microsoft.com/en-us/library/windows/desktop/aa366723.aspx) | Introduced into api-ms-win-core-heap-l2-1-0.dll in 10.0.14393. |
| [LocalFree](https://msdn.microsoft.com/en-us/library/windows/desktop/aa366730.aspx) | Introduced into api-ms-win-core-heap-l2-1-0.dll in 10.0.14393. |
| [LocalReAlloc](https://msdn.microsoft.com/en-us/library/windows/desktop/aa366742.aspx) | Introduced into api-ms-win-core-heap-l2-1-0.dll in 10.0.14393. |


## APIs from api-ms-win-core-heap-obsolete-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [GlobalReAlloc](https://msdn.microsoft.com/en-us/library/windows/desktop/aa366590.aspx) | Introduced into api-ms-win-core-heap-obsolete-l1-1-0.dll in 10.0.14393. |
| [GlobalLock](https://msdn.microsoft.com/en-us/library/Aa366584.aspx) | Introduced into api-ms-win-core-heap-obsolete-l1-1-0.dll in 10.0.15063. |
| [GlobalUnlock](https://msdn.microsoft.com/en-us/library/Aa366595.aspx) | Introduced into api-ms-win-core-heap-obsolete-l1-1-0.dll in 10.0.15063. |
| [GlobalSize](https://msdn.microsoft.com/en-us/library/Aa366593.aspx) | Introduced into api-ms-win-core-heap-obsolete-l1-1-0.dll in 10.0.15063. |


## APIs from api-ms-win-core-psapi-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| K32GetModuleInformation | Introduced into api-ms-win-core-psapi-l1-1-0.dll in 10.0.14393. |
| K32GetProcessMemoryInfo | Introduced into api-ms-win-core-psapi-l1-1-0.dll in 10.0.14393. |
| K32GetModuleFileNameExW | Introduced into api-ms-win-core-psapi-l1-1-0.dll in 10.0.15063. |
| K32GetModuleBaseNameW | Introduced into api-ms-win-core-psapi-l1-1-0.dll in 10.0.15063. |


## APIs from api-ms-win-core-slapi-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [SLQueryLicenseValueFromApp](https://msdn.microsoft.com/en-us/library/windows/desktop/mt403327.aspx) | Introduced into api-ms-win-core-slapi-l1-1-0.dll in 10.0.14393. |
| SLQueryLicenseValueFromApp2 | Introduced into api-ms-win-core-slapi-l1-1-0.dll in 10.0.14393. |


## APIs from api-ms-win-gaming-tcui-l1-1-2.dll

| API | Requirements |
| -----| --------------|
| [CheckGamingPrivilegeSilently](https://msdn.microsoft.com/en-us/library/Mt736759.aspx) | Introduced into api-ms-win-gaming-tcui-l1-1-2.dll in 10.0.14393. Moved into api-ms-win-gaming-tcui-l1-1-3.dll in 10.0.15063. |
| CheckGamingPrivilegeSilentlyForUser | Introduced into api-ms-win-gaming-tcui-l1-1-2.dll in 10.0.14393. Moved into api-ms-win-gaming-tcui-l1-1-3.dll in 10.0.15063. |
| [CheckGamingPrivilegeWithUI](https://msdn.microsoft.com/en-us/library/Mt736760.aspx) | Introduced into api-ms-win-gaming-tcui-l1-1-2.dll in 10.0.14393. Moved into api-ms-win-gaming-tcui-l1-1-3.dll in 10.0.15063. |
| CheckGamingPrivilegeWithUIForUser | Introduced into api-ms-win-gaming-tcui-l1-1-2.dll in 10.0.14393. Moved into api-ms-win-gaming-tcui-l1-1-3.dll in 10.0.15063. |
| ShowChangeFriendRelationshipUIForUser | Introduced into api-ms-win-gaming-tcui-l1-1-2.dll in 10.0.14393. Moved into api-ms-win-gaming-tcui-l1-1-3.dll in 10.0.15063. |
| ShowGameInviteUIForUser | Introduced into api-ms-win-gaming-tcui-l1-1-2.dll in 10.0.14393. Moved into api-ms-win-gaming-tcui-l1-1-3.dll in 10.0.15063. |
| ShowPlayerPickerUIForUser | Introduced into api-ms-win-gaming-tcui-l1-1-2.dll in 10.0.14393. Moved into api-ms-win-gaming-tcui-l1-1-3.dll in 10.0.15063. |
| ShowProfileCardUIForUser | Introduced into api-ms-win-gaming-tcui-l1-1-2.dll in 10.0.14393. Moved into api-ms-win-gaming-tcui-l1-1-3.dll in 10.0.15063. |
| ShowTitleAchievementsUIForUser | Introduced into api-ms-win-gaming-tcui-l1-1-2.dll in 10.0.14393. Moved into api-ms-win-gaming-tcui-l1-1-3.dll in 10.0.15063. |


## APIs from api-ms-win-security-base-l1-2-1.dll

| API | Requirements |
| -----| --------------|
| [CveEventWrite](https://msdn.microsoft.com/en-us/library/windows/desktop/mt759300.aspx) | Introduced into api-ms-win-security-base-l1-2-1.dll in 10.0.14393. Moved into api-ms-win-security-base-l1-2-2.dll in 10.0.15063. |


## APIs from inkobjcore.dll

| API | Requirements |
| -----| --------------|
| [AddStroke](https://msdn.microsoft.com/en-us/library/ms695546.aspx) | Introduced into inkobjcore.dll in 10.0.14393. |
| [AddWordsToWordList](https://msdn.microsoft.com/en-us/library/ms700667.aspx) | Introduced into inkobjcore.dll in 10.0.14393. |
| [AdviseInkChange](https://msdn.microsoft.com/en-us/library/ms696411.aspx) | Introduced into inkobjcore.dll in 10.0.14393. |
| [CreateContext](https://msdn.microsoft.com/en-us/library/ms698176.aspx) | Introduced into inkobjcore.dll in 10.0.14393. |
| [CreateRecognizer](https://msdn.microsoft.com/en-us/library/ms702413.aspx) | Introduced into inkobjcore.dll in 10.0.14393. |
| [DestroyContext](https://msdn.microsoft.com/en-us/library/ms702394.aspx) | Introduced into inkobjcore.dll in 10.0.14393. |
| [DestroyRecognizer](https://msdn.microsoft.com/en-us/library/ms705335.aspx) | Introduced into inkobjcore.dll in 10.0.14393. |
| [DestroyWordList](https://msdn.microsoft.com/en-us/library/ms697342.aspx) | Introduced into inkobjcore.dll in 10.0.14393. |
| [EndInkInput](https://msdn.microsoft.com/en-us/library/ms704432.aspx) | Introduced into inkobjcore.dll in 10.0.14393. |
| [GetAllRecognizers](https://msdn.microsoft.com/en-us/library/Mt752491.aspx) | Introduced into inkobjcore.dll in 10.0.14393. |
| [GetBestResultString](https://msdn.microsoft.com/en-us/library/ms701193.aspx) | Introduced into inkobjcore.dll in 10.0.14393. |
| [GetLatticePtr](https://msdn.microsoft.com/en-us/library/ms698571.aspx) | Introduced into inkobjcore.dll in 10.0.14393. |
| [GetLeftSeparator](https://msdn.microsoft.com/en-us/library/Mt218779.aspx) | Introduced into inkobjcore.dll in 10.0.14393. |
| [GetRecoAttributes](https://msdn.microsoft.com/en-us/library/ms698123.aspx) | Introduced into inkobjcore.dll in 10.0.14393. |
| [GetResultPropertyList](https://msdn.microsoft.com/en-us/library/ms704360.aspx) | Introduced into inkobjcore.dll in 10.0.14393. |
| [GetRightSeparator](https://msdn.microsoft.com/en-us/library/Mt218780.aspx) | Introduced into inkobjcore.dll in 10.0.14393. |
| [GetUnicodeRanges](https://msdn.microsoft.com/en-us/library/ms698151.aspx) | Introduced into inkobjcore.dll in 10.0.14393. |
| [IsStringSupported](https://msdn.microsoft.com/en-us/library/ms702420.aspx) | Introduced into inkobjcore.dll in 10.0.14393. |
| [LoadCachedAttributes](https://msdn.microsoft.com/en-us/library/Mt752492.aspx) | Introduced into inkobjcore.dll in 10.0.14393. |
| [MakeWordList](https://msdn.microsoft.com/en-us/library/ms702408.aspx) | Introduced into inkobjcore.dll in 10.0.14393. |
| [Process](https://msdn.microsoft.com/en-us/library/ms698535(v=vs.85).aspx) | Introduced into inkobjcore.dll in 10.0.14393. |
| [SetEnabledUnicodeRanges](https://msdn.microsoft.com/en-us/library/ms699520.aspx) | Introduced into inkobjcore.dll in 10.0.14393. |
| [SetFactoid](https://msdn.microsoft.com/en-us/library/ms704885.aspx) | Introduced into inkobjcore.dll in 10.0.14393. |
| [SetFlags](https://msdn.microsoft.com/en-us/library/ms698610(v=vs.85).aspx) | Introduced into inkobjcore.dll in 10.0.14393. |
| [SetGuide](https://msdn.microsoft.com/en-us/library/ms697487.aspx) | Introduced into inkobjcore.dll in 10.0.14393. |
| [SetTextContext](https://msdn.microsoft.com/en-us/library/ms704873.aspx) | Introduced into inkobjcore.dll in 10.0.14393. |
| [SetWordList](https://msdn.microsoft.com/en-us/library/ms701660.aspx) | Introduced into inkobjcore.dll in 10.0.14393. |


## APIs from iphlpapi.dll

| API | Requirements |
| -----| --------------|
| [FreeMibTable](https://msdn.microsoft.com/en-us/library/windows/desktop/aa814408.aspx) | Introduced into iphlpapi.dll in 10.0.14393. |
| [GetAdaptersAddresses](https://msdn.microsoft.com/en-us/library/windows/desktop/aa365915.aspx) | Introduced into iphlpapi.dll in 10.0.14393. |
| [GetBestRoute2](https://msdn.microsoft.com/en-us/library/windows/desktop/aa814411.aspx) | Introduced into iphlpapi.dll in 10.0.14393. |
| [GetUnicastIpAddressTable](https://msdn.microsoft.com/en-us/library/windows/desktop/aa814428.aspx) | Introduced into iphlpapi.dll in 10.0.14393. |
| [GetIfEntry2](https://msdn.microsoft.com/en-us/library/windows/desktop/aa365941(v=vs.85).aspx) | Introduced into iphlpapi.dll in 10.0.15063. |
| [GetPerAdapterInfo](https://msdn.microsoft.com/en-us/library/Aa366012.aspx) | Introduced into iphlpapi.dll in 10.0.15063. |
| [GetIcmpStatisticsEx](https://msdn.microsoft.com/en-us/library/Aa365936.aspx) | Introduced into iphlpapi.dll in 10.0.15063. |
| [GetIpStatisticsEx](https://msdn.microsoft.com/en-us/library/Aa365963.aspx) | Introduced into iphlpapi.dll in 10.0.15063. |
| [GetTcpStatisticsEx](https://msdn.microsoft.com/en-us/library/Aa366023.aspx) | Introduced into iphlpapi.dll in 10.0.15063. |
| [GetUdpStatisticsEx](https://msdn.microsoft.com/en-us/library/Aa366031.aspx) | Introduced into iphlpapi.dll in 10.0.15063. |
| [CancelMibChangeNotify2](https://msdn.microsoft.com/en-us/library/windows/desktop/aa814397(v=vs.85).aspx) | Introduced into iphlpapi.dll in 10.0.15063. |
| [Icmp6CreateFile](https://msdn.microsoft.com/en-us/library/Aa366037.aspx) | Introduced into iphlpapi.dll in 10.0.15063. |
| [Icmp6SendEcho2](https://msdn.microsoft.com/en-us/library/Aa366041.aspx) | Introduced into iphlpapi.dll in 10.0.15063. |
| [IcmpCloseHandle](https://msdn.microsoft.com/en-us/library/Aa366043.aspx) | Introduced into iphlpapi.dll in 10.0.15063. |
| [IcmpCreateFile](https://msdn.microsoft.com/en-us/library/Aa366045.aspx) | Introduced into iphlpapi.dll in 10.0.15063. |
| [NotifyUnicastIpAddressChange](https://msdn.microsoft.com/en-us/library/windows/desktop/aa814454(v=vs.85).aspx) | Introduced into iphlpapi.dll in 10.0.15063. |
| [IcmpSendEcho2](https://msdn.microsoft.com/en-us/library/Aa366051.aspx) | Introduced into iphlpapi.dll in 10.0.15063. |
| [GetNetworkParams](https://msdn.microsoft.com/en-us/library/Aa365968.aspx) | Introduced into iphlpapi.dll in 10.0.15063. |
| [GetBestInterfaceEx](https://msdn.microsoft.com/en-us/library/Aa365922.aspx) | Introduced into iphlpapi.dll in 10.0.15063. |
| [NotifyStableUnicastIpAddressTable](https://msdn.microsoft.com/en-us/library/Aa814452.aspx) | Introduced into iphlpapi.dll in 10.0.15063. |
| [GetIcmpStatistics](https://msdn.microsoft.com/en-us/library/Aa365934.aspx) | Introduced into iphlpapi.dll in 10.0.15063. |
| [GetTcpTable](https://msdn.microsoft.com/en-us/library/Aa366026.aspx) | Introduced into iphlpapi.dll in 10.0.15063. |
| [GetUdpTable](https://msdn.microsoft.com/en-us/library/Aa366033.aspx) | Introduced into iphlpapi.dll in 10.0.15063. |
| [GetExtendedTcpTable](https://msdn.microsoft.com/en-us/library/Aa365928.aspx) | Introduced into iphlpapi.dll in 10.0.15063. |
| [GetExtendedUdpTable](https://msdn.microsoft.com/en-us/library/Aa365930.aspx) | Introduced into iphlpapi.dll in 10.0.15063. |


## APIs from msajapi.dll

| API | Requirements |
| -----| --------------|
| [alljoyn_aboutdata_createfromxml](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.14393. |
| [alljoyn_abouticon_getcontent](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.14393. |
| [alljoyn_abouticon_geturl](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.14393. |
| [alljoyn_applicationstatelistener_create](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.14393. |
| [alljoyn_applicationstatelistener_destroy](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_getpermissionconfigurator](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_registerapplicationstatelistener](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.14393. |
| [alljoyn_busattachment_unregisterapplicationstatelistener](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.14393. |
| [alljoyn_interfacedescription_addargannotation](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.14393. |
| [alljoyn_interfacedescription_getdescriptionlanguages](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.14393. |
| [alljoyn_interfacedescription_getdescriptiontranslationcallback](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.14393. |
| [alljoyn_interfacedescription_getmemberargannotation](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.14393. |
| [alljoyn_interfacedescription_hasdescription](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.14393. |
| [alljoyn_interfacedescription_member_getargannotation](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.14393. |
| [alljoyn_interfacedescription_member_getargannotationatindex](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.14393. |
| [alljoyn_interfacedescription_member_getargannotationscount](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.14393. |
| [alljoyn_interfacedescription_setargdescription](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.14393. |
| [alljoyn_interfacedescription_setdescription](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.14393. |
| [alljoyn_interfacedescription_setdescriptionlanguage](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.14393. |
| [alljoyn_interfacedescription_setdescriptiontranslationcallback](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.14393. |
| [alljoyn_interfacedescription_setmemberdescription](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.14393. |
| [alljoyn_interfacedescription_setpropertydescription](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.14393. |
| [alljoyn_permissionconfigurator_getapplicationstate](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.14393. |
| [alljoyn_permissionconfigurator_getclaimcapabilities](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.14393. |
| [alljoyn_permissionconfigurator_getclaimcapabilitiesadditionalinfo](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.14393. |
| [alljoyn_permissionconfigurator_reset](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.14393. |
| [alljoyn_permissionconfigurator_setapplicationstate](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.14393. |
| [alljoyn_permissionconfigurator_setclaimcapabilities](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.14393. |
| [alljoyn_permissionconfigurator_setclaimcapabilitiesadditionalinfo](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.14393. |
| [alljoyn_permissionconfigurator_setmanifestfromxml](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.14393. |
| [alljoyn_securityapplicationproxy_claim](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.14393. |
| [alljoyn_securityapplicationproxy_create](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.14393. |
| [alljoyn_securityapplicationproxy_destroy](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.14393. |
| [alljoyn_securityapplicationproxy_eccpublickey_destroy](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.14393. |
| [alljoyn_securityapplicationproxy_endmanagement](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.14393. |
| [alljoyn_securityapplicationproxy_getapplicationstate](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.14393. |
| [alljoyn_securityapplicationproxy_getclaimcapabilities](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.14393. |
| [alljoyn_securityapplicationproxy_getclaimcapabilitiesadditionalinfo](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.14393. |
| [alljoyn_securityapplicationproxy_geteccpublickey](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.14393. |
| [alljoyn_securityapplicationproxy_getmanifesttemplate](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.14393. |
| [alljoyn_securityapplicationproxy_installmembership](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.14393. |
| [alljoyn_securityapplicationproxy_manifest_destroy](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.14393. |
| [alljoyn_securityapplicationproxy_manifesttemplate_destroy](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.14393. |
| [alljoyn_securityapplicationproxy_reset](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.14393. |
| [alljoyn_securityapplicationproxy_resetpolicy](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.14393. |
| [alljoyn_securityapplicationproxy_signmanifest](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.14393. |
| [alljoyn_securityapplicationproxy_startmanagement](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.14393. |
| [alljoyn_securityapplicationproxy_updateidentity](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.14393. |
| [alljoyn_securityapplicationproxy_updatepolicy](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.14393. |
| [alljoyn_authlistener_setsharedsecret](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.15063. |
| [alljoyn_busattachment_deletedefaultkeystore](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.15063. |
| [alljoyn_interfacedescription_getargdescriptionforlanguage](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.15063. |
| [alljoyn_interfacedescription_getdescriptionforlanguage](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.15063. |
| [alljoyn_interfacedescription_getdescriptionlanguages2](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.15063. |
| [alljoyn_interfacedescription_getmemberdescriptionforlanguage](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.15063. |
| [alljoyn_interfacedescription_getpropertydescriptionforlanguage](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.15063. |
| [alljoyn_interfacedescription_setargdescriptionforlanguage](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.15063. |
| [alljoyn_interfacedescription_setdescriptionforlanguage](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.15063. |
| [alljoyn_interfacedescription_setmemberdescriptionforlanguage](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.15063. |
| [alljoyn_interfacedescription_setpropertydescriptionforlanguage](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.15063. |
| [alljoyn_keystorelistener_with_synchronization_create](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.15063. |
| [alljoyn_routerinit](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.15063. |
| [alljoyn_routerinitwithconfig](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.15063. |
| [alljoyn_routershutdown](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.15063. |
| [alljoyn_permissionconfigurator_certificatechain_destroy](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.15063. |
| [alljoyn_permissionconfigurator_certificateid_cleanup](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.15063. |
| [alljoyn_permissionconfigurator_certificateidarray_cleanup](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.15063. |
| [alljoyn_permissionconfigurator_claim](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.15063. |
| [alljoyn_permissionconfigurator_endmanagement](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.15063. |
| [alljoyn_permissionconfigurator_getdefaultclaimcapabilities](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.15063. |
| [alljoyn_permissionconfigurator_getdefaultpolicy](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.15063. |
| [alljoyn_permissionconfigurator_getidentity](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.15063. |
| [alljoyn_permissionconfigurator_getidentitycertificateid](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.15063. |
| [alljoyn_permissionconfigurator_getmanifests](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.15063. |
| [alljoyn_permissionconfigurator_getmanifesttemplate](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.15063. |
| [alljoyn_permissionconfigurator_getmembershipsummaries](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.15063. |
| [alljoyn_permissionconfigurator_getpolicy](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.15063. |
| [alljoyn_permissionconfigurator_getpublickey](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.15063. |
| [alljoyn_permissionconfigurator_installmanifests](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.15063. |
| [alljoyn_permissionconfigurator_installmembership](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.15063. |
| [alljoyn_permissionconfigurator_manifestarray_cleanup](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.15063. |
| [alljoyn_permissionconfigurator_manifesttemplate_destroy](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.15063. |
| [alljoyn_permissionconfigurator_policy_destroy](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.15063. |
| [alljoyn_permissionconfigurator_publickey_destroy](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.15063. |
| [alljoyn_permissionconfigurator_removemembership](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.15063. |
| [alljoyn_permissionconfigurator_resetpolicy](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.15063. |
| [alljoyn_permissionconfigurator_setmanifesttemplatefromxml](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.15063. |
| [alljoyn_permissionconfigurator_startmanagement](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.15063. |
| [alljoyn_permissionconfigurator_updateidentity](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.15063. |
| [alljoyn_permissionconfigurator_updatepolicy](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.15063. |
| [alljoyn_securityapplicationproxy_computemanifestdigest](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.15063. |
| [alljoyn_securityapplicationproxy_digest_destroy](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.15063. |
| [alljoyn_securityapplicationproxy_getdefaultpolicy](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.15063. |
| [alljoyn_securityapplicationproxy_getpermissionmanagementsessionport](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.15063. |
| [alljoyn_securityapplicationproxy_getpolicy](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.15063. |
| [alljoyn_securityapplicationproxy_policy_destroy](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.15063. |
| [alljoyn_securityapplicationproxy_setmanifestsignature](https://github.com/allseenalliance/core-alljoyn/tree/master/alljoyn_c) | Introduced into msajapi.dll in 10.0.15063. |


## APIs from api-ms-win-security-base-l1-2-0.dll

| API | Requirements |
| -----| --------------|
| [CopySid](https://msdn.microsoft.com/en-us/library/Aa376404.aspx) | Introduced into api-ms-win-security-base-l1-2-0.dll in 10.0.15063. |
| [GetLengthSid](https://msdn.microsoft.com/en-us/library/Aa446642.aspx) | Introduced into api-ms-win-security-base-l1-2-0.dll in 10.0.15063. |
| [GetTokenInformation](https://msdn.microsoft.com/en-us/library/Aa446671.aspx) | Introduced into api-ms-win-security-base-l1-2-0.dll in 10.0.15063. |
| [FreeSid](https://msdn.microsoft.com/en-us/library/Aa446631.aspx) | Introduced into api-ms-win-security-base-l1-2-0.dll in 10.0.15063. |
| [AllocateAndInitializeSid](https://msdn.microsoft.com/en-us/library/Aa375213.aspx) | Introduced into api-ms-win-security-base-l1-2-0.dll in 10.0.15063. |
| [CreateWellKnownSid](https://msdn.microsoft.com/en-us/library/Aa446585.aspx) | Introduced into api-ms-win-security-base-l1-2-0.dll in 10.0.15063. |
| [IsValidSid](https://msdn.microsoft.com/en-us/library/Aa379151.aspx) | Introduced into api-ms-win-security-base-l1-2-0.dll in 10.0.15063. |
| [CheckTokenMembership](https://msdn.microsoft.com/en-us/library/Aa376389.aspx) | Introduced into api-ms-win-security-base-l1-2-0.dll in 10.0.15063. |
| [AdjustTokenPrivileges](https://msdn.microsoft.com/en-us/library/Aa375202.aspx) | Introduced into api-ms-win-security-base-l1-2-0.dll in 10.0.15063. |
| [GetAce](https://msdn.microsoft.com/en-us/library/Aa446634.aspx) | Introduced into api-ms-win-security-base-l1-2-0.dll in 10.0.15063. |
| [GetAclInformation](https://msdn.microsoft.com/en-us/library/Aa446635.aspx) | Introduced into api-ms-win-security-base-l1-2-0.dll in 10.0.15063. |
| [GetSecurityDescriptorDacl](https://msdn.microsoft.com/en-us/library/Aa446648.aspx) | Introduced into api-ms-win-security-base-l1-2-0.dll in 10.0.15063. |
| [CheckTokenMembershipEx](https://msdn.microsoft.com/en-us/library/Hh448479.aspx) | Introduced into api-ms-win-security-base-l1-2-0.dll in 10.0.15063. |
| [DuplicateTokenEx](https://msdn.microsoft.com/en-us/library/Aa446617.aspx) | Introduced into api-ms-win-security-base-l1-2-0.dll in 10.0.15063. |
| [AddAce](https://msdn.microsoft.com/en-us/library/Aa374970.aspx) | Introduced into api-ms-win-security-base-l1-2-0.dll in 10.0.15063. |
| [GetSecurityDescriptorControl](https://msdn.microsoft.com/en-us/library/Aa446647.aspx) | Introduced into api-ms-win-security-base-l1-2-0.dll in 10.0.15063. |
| [GetSecurityDescriptorGroup](https://msdn.microsoft.com/en-us/library/Aa446649.aspx) | Introduced into api-ms-win-security-base-l1-2-0.dll in 10.0.15063. |
| [GetSecurityDescriptorLength](https://msdn.microsoft.com/en-us/library/Aa446650.aspx) | Introduced into api-ms-win-security-base-l1-2-0.dll in 10.0.15063. |
| [GetSecurityDescriptorOwner](https://msdn.microsoft.com/en-us/library/Aa446651.aspx) | Introduced into api-ms-win-security-base-l1-2-0.dll in 10.0.15063. |
| [GetSecurityDescriptorSacl](https://msdn.microsoft.com/en-us/library/Aa446653.aspx) | Introduced into api-ms-win-security-base-l1-2-0.dll in 10.0.15063. |
| [GetSidIdentifierAuthority](https://msdn.microsoft.com/en-us/library/Aa446655.aspx) | Introduced into api-ms-win-security-base-l1-2-0.dll in 10.0.15063. |
| [InitializeAcl](https://msdn.microsoft.com/en-us/library/Aa378853.aspx) | Introduced into api-ms-win-security-base-l1-2-0.dll in 10.0.15063. |
| [InitializeSecurityDescriptor](https://msdn.microsoft.com/en-us/library/Aa378863.aspx) | Introduced into api-ms-win-security-base-l1-2-0.dll in 10.0.15063. |
| [MakeSelfRelativeSD](https://msdn.microsoft.com/en-us/library/Aa379265.aspx) | Introduced into api-ms-win-security-base-l1-2-0.dll in 10.0.15063. |
| [SetSecurityDescriptorDacl](https://msdn.microsoft.com/en-us/library/Aa379583.aspx) | Introduced into api-ms-win-security-base-l1-2-0.dll in 10.0.15063. |
| [SetSecurityDescriptorGroup](https://msdn.microsoft.com/en-us/library/Aa379584.aspx) | Introduced into api-ms-win-security-base-l1-2-0.dll in 10.0.15063. |
| [SetSecurityDescriptorOwner](https://msdn.microsoft.com/en-us/library/Aa379585.aspx) | Introduced into api-ms-win-security-base-l1-2-0.dll in 10.0.15063. |
| [SetSecurityDescriptorSacl](https://msdn.microsoft.com/en-us/library/Aa379587.aspx) | Introduced into api-ms-win-security-base-l1-2-0.dll in 10.0.15063. |
| [AddAccessAllowedAce](https://msdn.microsoft.com/en-us/library/Aa374947.aspx) | Introduced into api-ms-win-security-base-l1-2-0.dll in 10.0.15063. |
| [GetSidLengthRequired](https://msdn.microsoft.com/en-us/library/Aa446656.aspx) | Introduced into api-ms-win-security-base-l1-2-0.dll in 10.0.15063. |
| [GetSidSubAuthority](https://msdn.microsoft.com/en-us/library/Aa446657.aspx) | Introduced into api-ms-win-security-base-l1-2-0.dll in 10.0.15063. |
| [GetSidSubAuthorityCount](https://msdn.microsoft.com/en-us/library/Aa446658.aspx) | Introduced into api-ms-win-security-base-l1-2-0.dll in 10.0.15063. |
| [AddAccessAllowedAceEx](https://msdn.microsoft.com/en-us/library/Aa374951.aspx) | Introduced into api-ms-win-security-base-l1-2-0.dll in 10.0.15063. |
| [AdjustTokenGroups](https://msdn.microsoft.com/en-us/library/Aa375199.aspx) | Introduced into api-ms-win-security-base-l1-2-0.dll in 10.0.15063. |
| [AllocateLocallyUniqueId](https://msdn.microsoft.com/en-us/library/Aa375260.aspx) | Introduced into api-ms-win-security-base-l1-2-0.dll in 10.0.15063. |
| [DeleteAce](https://msdn.microsoft.com/en-us/library/Aa446612.aspx) | Introduced into api-ms-win-security-base-l1-2-0.dll in 10.0.15063. |
| [DuplicateToken](https://msdn.microsoft.com/en-us/library/Aa446616.aspx) | Introduced into api-ms-win-security-base-l1-2-0.dll in 10.0.15063. |
| [EqualDomainSid](https://msdn.microsoft.com/en-us/library/Aa446620.aspx) | Introduced into api-ms-win-security-base-l1-2-0.dll in 10.0.15063. |
| [GetKernelObjectSecurity](https://msdn.microsoft.com/en-us/library/Aa446641.aspx) | Introduced into api-ms-win-security-base-l1-2-0.dll in 10.0.15063. |
| [GetSecurityDescriptorRMControl](https://msdn.microsoft.com/en-us/library/Aa446652.aspx) | Introduced into api-ms-win-security-base-l1-2-0.dll in 10.0.15063. |
| [GetWindowsAccountDomainSid](https://msdn.microsoft.com/en-us/library/Aa446676.aspx) | Introduced into api-ms-win-security-base-l1-2-0.dll in 10.0.15063. |
| [InitializeSid](https://msdn.microsoft.com/en-us/library/Aa378875.aspx) | Introduced into api-ms-win-security-base-l1-2-0.dll in 10.0.15063. |
| [IsValidAcl](https://msdn.microsoft.com/en-us/library/Aa379142.aspx) | Introduced into api-ms-win-security-base-l1-2-0.dll in 10.0.15063. |
| [IsValidSecurityDescriptor](https://msdn.microsoft.com/en-us/library/Aa379147.aspx) | Introduced into api-ms-win-security-base-l1-2-0.dll in 10.0.15063. |
| [IsWellKnownSid](https://msdn.microsoft.com/en-us/library/Aa379154.aspx) | Introduced into api-ms-win-security-base-l1-2-0.dll in 10.0.15063. |
| [MakeAbsoluteSD](https://msdn.microsoft.com/en-us/library/Aa379264.aspx) | Introduced into api-ms-win-security-base-l1-2-0.dll in 10.0.15063. |
| [SetKernelObjectSecurity](https://msdn.microsoft.com/en-us/library/Aa379578.aspx) | Introduced into api-ms-win-security-base-l1-2-0.dll in 10.0.15063. |
| [SetSecurityDescriptorControl](https://msdn.microsoft.com/en-us/library/Aa379582.aspx) | Introduced into api-ms-win-security-base-l1-2-0.dll in 10.0.15063. |
| [SetSecurityDescriptorRMControl](https://msdn.microsoft.com/en-us/library/Aa379586.aspx) | Introduced into api-ms-win-security-base-l1-2-0.dll in 10.0.15063. |
| [SetTokenInformation](https://msdn.microsoft.com/en-us/library/Aa379591.aspx) | Introduced into api-ms-win-security-base-l1-2-0.dll in 10.0.15063. |
| [AddMandatoryAce](https://msdn.microsoft.com/en-us/library/Aa965464.aspx) | Introduced into api-ms-win-security-base-l1-2-0.dll in 10.0.15063. |


## APIs from api-ms-win-security-sddl-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [ConvertSidToStringSidW](https://msdn.microsoft.com/en-us/library/Aa376399.aspx) | Introduced into api-ms-win-security-sddl-l1-1-0.dll in 10.0.15063. |
| [ConvertStringSecurityDescriptorToSecurityDescriptorW](https://msdn.microsoft.com/en-us/library/Aa376401.aspx) | Introduced into api-ms-win-security-sddl-l1-1-0.dll in 10.0.15063. |
| [ConvertStringSidToSidW](https://msdn.microsoft.com/en-us/library/Aa376402.aspx) | Introduced into api-ms-win-security-sddl-l1-1-0.dll in 10.0.15063. |
| [ConvertSecurityDescriptorToStringSecurityDescriptorW](https://msdn.microsoft.com/en-us/library/Aa376397.aspx) | Introduced into api-ms-win-security-sddl-l1-1-0.dll in 10.0.15063. |


## APIs from api-ms-win-security-lsalookup-l2-1-1.dll

| API | Requirements |
| -----| --------------|
| [LookupAccountSidW](https://msdn.microsoft.com/en-us/library/Aa379166.aspx) | Introduced into api-ms-win-security-lsalookup-l2-1-1.dll in 10.0.15063. |
| [LookupAccountNameW](https://msdn.microsoft.com/en-us/library/Aa379159.aspx) | Introduced into api-ms-win-security-lsalookup-l2-1-1.dll in 10.0.15063. |
| [LookupPrivilegeValueW](https://msdn.microsoft.com/en-us/library/Aa379180.aspx) | Introduced into api-ms-win-security-lsalookup-l2-1-1.dll in 10.0.15063. |
| [LookupPrivilegeDisplayNameW](https://msdn.microsoft.com/en-us/library/Aa379168.aspx) | Introduced into api-ms-win-security-lsalookup-l2-1-1.dll in 10.0.15063. |
| [LookupPrivilegeNameW](https://msdn.microsoft.com/en-us/library/Aa379176.aspx) | Introduced into api-ms-win-security-lsalookup-l2-1-1.dll in 10.0.15063. |


## APIs from api-ms-win-security-provider-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [SetEntriesInAclW](https://msdn.microsoft.com/en-us/library/Aa379576.aspx) | Introduced into api-ms-win-security-provider-l1-1-0.dll in 10.0.15063. |
| [SetNamedSecurityInfoW](https://msdn.microsoft.com/en-us/library/Aa379579.aspx) | Introduced into api-ms-win-security-provider-l1-1-0.dll in 10.0.15063. |
| [GetExplicitEntriesFromAclW](https://msdn.microsoft.com/en-us/library/Aa446638.aspx) | Introduced into api-ms-win-security-provider-l1-1-0.dll in 10.0.15063. |
| [GetNamedSecurityInfoW](https://msdn.microsoft.com/en-us/library/Aa446645.aspx) | Introduced into api-ms-win-security-provider-l1-1-0.dll in 10.0.15063. |
| [GetSecurityInfo](https://msdn.microsoft.com/en-us/library/Aa446654.aspx) | Introduced into api-ms-win-security-provider-l1-1-0.dll in 10.0.15063. |
| [SetSecurityInfo](https://msdn.microsoft.com/en-us/library/Aa379588.aspx) | Introduced into api-ms-win-security-provider-l1-1-0.dll in 10.0.15063. |


## APIs from api-ms-win-appmodel-runtime-l1-1-1.dll

| API | Requirements |
| -----| --------------|
| [PackageFamilyNameFromFullName](https://msdn.microsoft.com/en-us/library/Hh446769.aspx) | Introduced into api-ms-win-appmodel-runtime-l1-1-1.dll in 10.0.15063. |
| [ParseApplicationUserModelId](https://msdn.microsoft.com/en-us/library/Dn313168.aspx) | Introduced into api-ms-win-appmodel-runtime-l1-1-1.dll in 10.0.15063. |
| [PackageFamilyNameFromId](https://msdn.microsoft.com/en-us/library/Hh446770.aspx) | Introduced into api-ms-win-appmodel-runtime-l1-1-1.dll in 10.0.15063. |
| [PackageNameAndPublisherIdFromFamilyName](https://msdn.microsoft.com/en-us/library/Hh446773.aspx) | Introduced into api-ms-win-appmodel-runtime-l1-1-1.dll in 10.0.15063. |
| [FormatApplicationUserModelId](https://msdn.microsoft.com/en-us/library/Dn270602.aspx) | Introduced into api-ms-win-appmodel-runtime-l1-1-1.dll in 10.0.15063. |
| [PackageIdFromFullName](https://msdn.microsoft.com/en-us/library/Hh446772.aspx) | Introduced into api-ms-win-appmodel-runtime-l1-1-1.dll in 10.0.15063. |
| [PackageFullNameFromId](https://msdn.microsoft.com/en-us/library/Hh446771.aspx) | Introduced into api-ms-win-appmodel-runtime-l1-1-1.dll in 10.0.15063. |


## APIs from bcrypt.dll

| API | Requirements |
| -----| --------------|
| [BCryptGetFipsAlgorithmMode](https://msdn.microsoft.com/en-us/library/Aa375460.aspx) | Introduced into bcrypt.dll in 10.0.15063. |


## APIs from api-ms-win-core-path-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [PathCchCombine](https://msdn.microsoft.com/en-us/library/Hh707085.aspx) | Introduced into api-ms-win-core-path-l1-1-0.dll in 10.0.15063. |
| [PathCchRemoveFileSpec](https://msdn.microsoft.com/en-us/library/Hh707092.aspx) | Introduced into api-ms-win-core-path-l1-1-0.dll in 10.0.15063. |
| [PathCchAddBackslash](https://msdn.microsoft.com/en-us/library/Hh707078.aspx) | Introduced into api-ms-win-core-path-l1-1-0.dll in 10.0.15063. |
| [PathCchAppend](https://msdn.microsoft.com/en-us/library/Hh707081.aspx) | Introduced into api-ms-win-core-path-l1-1-0.dll in 10.0.15063. |
| [PathCchFindExtension](https://msdn.microsoft.com/en-us/library/Hh707087.aspx) | Introduced into api-ms-win-core-path-l1-1-0.dll in 10.0.15063. |
| [PathCchRemoveBackslash](https://msdn.microsoft.com/en-us/library/Hh707089.aspx) | Introduced into api-ms-win-core-path-l1-1-0.dll in 10.0.15063. |
| [PathAllocCombine](https://msdn.microsoft.com/en-us/library/Hh707077.aspx) | Introduced into api-ms-win-core-path-l1-1-0.dll in 10.0.15063. |
| [PathCchSkipRoot](https://msdn.microsoft.com/en-us/library/Hh707094.aspx) | Introduced into api-ms-win-core-path-l1-1-0.dll in 10.0.15063. |
| [PathAllocCanonicalize](https://msdn.microsoft.com/en-us/library/Hh707076.aspx) | Introduced into api-ms-win-core-path-l1-1-0.dll in 10.0.15063. |
| [PathCchAddExtension](https://msdn.microsoft.com/en-us/library/Hh707080.aspx) | Introduced into api-ms-win-core-path-l1-1-0.dll in 10.0.15063. |
| [PathCchRemoveExtension](https://msdn.microsoft.com/en-us/library/Hh707091.aspx) | Introduced into api-ms-win-core-path-l1-1-0.dll in 10.0.15063. |
| [PathCchCanonicalize](https://msdn.microsoft.com/en-us/library/Hh707083.aspx) | Introduced into api-ms-win-core-path-l1-1-0.dll in 10.0.15063. |
| [PathCchCanonicalizeEx](https://msdn.microsoft.com/en-us/library/Hh707084.aspx) | Introduced into api-ms-win-core-path-l1-1-0.dll in 10.0.15063. |
| [PathCchCombineEx](https://msdn.microsoft.com/en-us/library/Hh707086.aspx) | Introduced into api-ms-win-core-path-l1-1-0.dll in 10.0.15063. |
| [PathCchRenameExtension](https://msdn.microsoft.com/en-us/library/Hh707093.aspx) | Introduced into api-ms-win-core-path-l1-1-0.dll in 10.0.15063. |
| [PathCchIsRoot](https://msdn.microsoft.com/en-us/library/Hh707088.aspx) | Introduced into api-ms-win-core-path-l1-1-0.dll in 10.0.15063. |
| [PathCchStripToRoot](https://msdn.microsoft.com/en-us/library/Hh707096.aspx) | Introduced into api-ms-win-core-path-l1-1-0.dll in 10.0.15063. |
| [PathIsUNCEx](https://msdn.microsoft.com/en-us/library/Hh707097.aspx) | Introduced into api-ms-win-core-path-l1-1-0.dll in 10.0.15063. |
| [PathCchStripPrefix](https://msdn.microsoft.com/en-us/library/Hh707095.aspx) | Introduced into api-ms-win-core-path-l1-1-0.dll in 10.0.15063. |
| [PathCchAppendEx](https://msdn.microsoft.com/en-us/library/Hh707082.aspx) | Introduced into api-ms-win-core-path-l1-1-0.dll in 10.0.15063. |
| [PathCchAddBackslashEx](https://msdn.microsoft.com/en-us/library/Hh707079.aspx) | Introduced into api-ms-win-core-path-l1-1-0.dll in 10.0.15063. |
| [PathCchRemoveBackslashEx](https://msdn.microsoft.com/en-us/library/Hh707090.aspx) | Introduced into api-ms-win-core-path-l1-1-0.dll in 10.0.15063. |


## APIs from api-ms-win-core-localization-obsolete-l1-3-0.dll

| API | Requirements |
| -----| --------------|
| [GetUserDefaultUILanguage](https://msdn.microsoft.com/en-us/library/Dd318137.aspx) | Introduced into api-ms-win-core-localization-obsolete-l1-3-0.dll in 10.0.15063. |
| [EnumUILanguagesW](https://msdn.microsoft.com/en-us/library/Dd317834.aspx) | Introduced into api-ms-win-core-localization-obsolete-l1-3-0.dll in 10.0.15063. |


## APIs from api-ms-win-core-namespace-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [AddSIDToBoundaryDescriptor](https://msdn.microsoft.com/en-us/library/ms681937.aspx) | Introduced into api-ms-win-core-namespace-l1-1-0.dll in 10.0.15063. |
| [ClosePrivateNamespace](https://msdn.microsoft.com/en-us/library/ms682026.aspx) | Introduced into api-ms-win-core-namespace-l1-1-0.dll in 10.0.15063. |
| [CreateBoundaryDescriptorW](https://msdn.microsoft.com/en-us/library/ms682121.aspx) | Introduced into api-ms-win-core-namespace-l1-1-0.dll in 10.0.15063. |
| [CreatePrivateNamespaceW](https://msdn.microsoft.com/en-us/library/ms682419.aspx) | Introduced into api-ms-win-core-namespace-l1-1-0.dll in 10.0.15063. |
| [DeleteBoundaryDescriptor](https://msdn.microsoft.com/en-us/library/ms682549.aspx) | Introduced into api-ms-win-core-namespace-l1-1-0.dll in 10.0.15063. |
| [OpenPrivateNamespaceW](https://msdn.microsoft.com/en-us/library/ms684318.aspx) | Introduced into api-ms-win-core-namespace-l1-1-0.dll in 10.0.15063. |


## APIs from api-ms-win-appmodel-runtime-l1-1-2.dll

| API | Requirements |
| -----| --------------|
| VerifyPackageFullName | Introduced into api-ms-win-appmodel-runtime-l1-1-2.dll in 10.0.15063. |
| VerifyApplicationUserModelId | Introduced into api-ms-win-appmodel-runtime-l1-1-2.dll in 10.0.15063. |
| VerifyPackageFamilyName | Introduced into api-ms-win-appmodel-runtime-l1-1-2.dll in 10.0.15063. |
| VerifyPackageId | Introduced into api-ms-win-appmodel-runtime-l1-1-2.dll in 10.0.15063. |
| VerifyPackageRelativeApplicationId | Introduced into api-ms-win-appmodel-runtime-l1-1-2.dll in 10.0.15063. |


## APIs from api-ms-win-core-url-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [GetAcceptLanguagesW](https://msdn.microsoft.com/en-us/library/ms538578.aspx) | Introduced into api-ms-win-core-url-l1-1-0.dll in 10.0.15063. |
| [GetAcceptLanguagesA](https://msdn.microsoft.com/en-us/library/ms538578.aspx) | Introduced into api-ms-win-core-url-l1-1-0.dll in 10.0.15063. |


## APIs from api-ms-win-security-isolatedcontainer-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| IsProcessInIsolatedContainer | Introduced into api-ms-win-security-isolatedcontainer-l1-1-0.dll in 10.0.15063. |


## APIs from api-ms-win-core-featurestaging-l1-1-1.dll

| API | Requirements |
| -----| --------------|
| GetFeatureVariant | Introduced into api-ms-win-core-featurestaging-l1-1-1.dll in 10.0.15063. |


## APIs from api-ms-win-core-memory-l1-1-5.dll

| API | Requirements |
| -----| --------------|
| [SetProcessValidCallTargets](https://msdn.microsoft.com/en-us/library/Dn934202.aspx) | Introduced into api-ms-win-core-memory-l1-1-5.dll in 10.0.15063. |


## APIs from api-ms-win-security-lsalookup-ansi-l2-1-0.dll

| API | Requirements |
| -----| --------------|
| [LookupPrivilegeValueA](https://msdn.microsoft.com/en-us/library/Aa379180.aspx) | Introduced into api-ms-win-security-lsalookup-ansi-l2-1-0.dll in 10.0.15063. |
| [LookupAccountNameA](https://msdn.microsoft.com/en-us/library/Aa379159.aspx) | Introduced into api-ms-win-security-lsalookup-ansi-l2-1-0.dll in 10.0.15063. |
| [LookupAccountSidA](https://msdn.microsoft.com/en-us/library/Aa379166.aspx) | Introduced into api-ms-win-security-lsalookup-ansi-l2-1-0.dll in 10.0.15063. |
| [LookupPrivilegeDisplayNameA](https://msdn.microsoft.com/en-us/library/Aa379168.aspx) | Introduced into api-ms-win-security-lsalookup-ansi-l2-1-0.dll in 10.0.15063. |
| [LookupPrivilegeNameA](https://msdn.microsoft.com/en-us/library/Aa379176.aspx) | Introduced into api-ms-win-security-lsalookup-ansi-l2-1-0.dll in 10.0.15063. |


## APIs from api-ms-win-core-psapi-ansi-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| K32GetModuleBaseNameA | Introduced into api-ms-win-core-psapi-ansi-l1-1-0.dll in 10.0.15063. |
| K32GetModuleFileNameExA | Introduced into api-ms-win-core-psapi-ansi-l1-1-0.dll in 10.0.15063. |


## APIs from api-ms-win-core-windowserrorreporting-l1-1-1.dll

| API | Requirements |
| -----| --------------|
| [WerRegisterAdditionalProcess](https://msdn.microsoft.com/en-us/library/Mt492585.aspx) | Introduced into api-ms-win-core-windowserrorreporting-l1-1-1.dll in 10.0.15063. |
| [WerRegisterCustomMetadata](https://msdn.microsoft.com/en-us/library/Mt492586.aspx) | Introduced into api-ms-win-core-windowserrorreporting-l1-1-1.dll in 10.0.15063. |
| [WerRegisterExcludedMemoryBlock](https://msdn.microsoft.com/en-us/library/Mt492587.aspx) | Introduced into api-ms-win-core-windowserrorreporting-l1-1-1.dll in 10.0.15063. |
| [WerUnregisterAdditionalProcess](https://msdn.microsoft.com/en-us/library/Mt492592.aspx) | Introduced into api-ms-win-core-windowserrorreporting-l1-1-1.dll in 10.0.15063. |
| [WerUnregisterCustomMetadata](https://msdn.microsoft.com/en-us/library/Mt492593.aspx) | Introduced into api-ms-win-core-windowserrorreporting-l1-1-1.dll in 10.0.15063. |
| [WerUnregisterExcludedMemoryBlock](https://msdn.microsoft.com/en-us/library/Mt492594.aspx) | Introduced into api-ms-win-core-windowserrorreporting-l1-1-1.dll in 10.0.15063. |


## APIs from api-ms-win-security-provider-ansi-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [SetEntriesInAclA](https://msdn.microsoft.com/en-us/library/Aa379576.aspx) | Introduced into api-ms-win-security-provider-ansi-l1-1-0.dll in 10.0.15063. |
| [GetExplicitEntriesFromAclA](https://msdn.microsoft.com/en-us/library/Aa446638.aspx) | Introduced into api-ms-win-security-provider-ansi-l1-1-0.dll in 10.0.15063. |
| [GetNamedSecurityInfoA](https://msdn.microsoft.com/en-us/library/Aa446645.aspx) | Introduced into api-ms-win-security-provider-ansi-l1-1-0.dll in 10.0.15063. |
| [SetNamedSecurityInfoA](https://msdn.microsoft.com/en-us/library/Aa379579.aspx) | Introduced into api-ms-win-security-provider-ansi-l1-1-0.dll in 10.0.15063. |


## APIs from api-ms-win-security-sddl-ansi-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [ConvertSidToStringSidA](https://msdn.microsoft.com/en-us/library/Aa376399.aspx) | Introduced into api-ms-win-security-sddl-ansi-l1-1-0.dll in 10.0.15063. |
| [ConvertStringSidToSidA](https://msdn.microsoft.com/en-us/library/Aa376402.aspx) | Introduced into api-ms-win-security-sddl-ansi-l1-1-0.dll in 10.0.15063. |


## APIs from api-ms-win-core-namespace-ansi-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [CreateBoundaryDescriptorA](https://msdn.microsoft.com/en-us/library/ms682121.aspx) | Introduced into api-ms-win-core-namespace-ansi-l1-1-0.dll in 10.0.15063. |
| [CreatePrivateNamespaceA](https://msdn.microsoft.com/en-us/library/ms682419.aspx) | Introduced into api-ms-win-core-namespace-ansi-l1-1-0.dll in 10.0.15063. |
| [OpenPrivateNamespaceA](https://msdn.microsoft.com/en-us/library/ms684318.aspx) | Introduced into api-ms-win-core-namespace-ansi-l1-1-0.dll in 10.0.15063. |


## APIs from api-ms-win-gaming-expandedresources-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [GetExpandedResourceExclusiveCpuCount](https://msdn.microsoft.com/en-us/library/Mt808809.aspx) | Introduced into api-ms-win-gaming-expandedresources-l1-1-0.dll in 10.0.15063. |
| [HasExpandedResources](https://msdn.microsoft.com/en-us/library/Mt808810.aspx) | Introduced into api-ms-win-gaming-expandedresources-l1-1-0.dll in 10.0.15063. |
| [ReleaseExclusiveCpuSets](https://msdn.microsoft.com/en-us/library/Mt808811.aspx) | Introduced into api-ms-win-gaming-expandedresources-l1-1-0.dll in 10.0.15063. |


## APIs from api-ms-win-core-realtime-l1-1-2.dll

| API | Requirements |
| -----| --------------|
| [ConvertAuxiliaryCounterToPerformanceCounter](https://msdn.microsoft.com/en-us/library/Mt781214.aspx) | Introduced into api-ms-win-core-realtime-l1-1-2.dll in 10.0.15063. |
| [ConvertPerformanceCounterToAuxiliaryCounter](https://msdn.microsoft.com/en-us/library/Mt781215.aspx) | Introduced into api-ms-win-core-realtime-l1-1-2.dll in 10.0.15063. |
| [QueryAuxiliaryCounterFrequency](https://msdn.microsoft.com/en-us/library/Mt781218.aspx) | Introduced into api-ms-win-core-realtime-l1-1-2.dll in 10.0.15063. |


## APIs from api-ms-win-gaming-gamemonitor-l1-1-0.dll

| API | Requirements |
| -----| --------------|
| [EnableActiveGameMonitoring](https://msdn.microsoft.com/en-us/library/Mt808782.aspx) | Introduced into api-ms-win-gaming-gamemonitor-l1-1-0.dll in 10.0.15063. |
| [ReportGameActivity](https://msdn.microsoft.com/en-us/library/Mt808783.aspx) | Introduced into api-ms-win-gaming-gamemonitor-l1-1-0.dll in 10.0.15063. |
| [SetGameActivityCorrelationId](https://msdn.microsoft.com/en-us/library/Mt808784.aspx) | Introduced into api-ms-win-gaming-gamemonitor-l1-1-0.dll in 10.0.15063. |


## APIs from api-ms-win-gaming-tcui-l1-1-3.dll

| API | Requirements |
| -----| --------------|
| ShowGameInviteUIWithContext | Introduced into api-ms-win-gaming-tcui-l1-1-3.dll in 10.0.15063. |
| ShowGameInviteUIWithContextForUser | Introduced into api-ms-win-gaming-tcui-l1-1-3.dll in 10.0.15063. |


