---
description: A type that you can use to implement (produce) the deferrable event pattern.
title: winrt::deferrable_event_args struct template (C++/WinRT)
dev_langs: ["C++"]
ms.date: 05/21/2021
ms.topic: "language-reference"
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, agile
ms.workload: ["cplusplus"]
---

# winrt::deferrable_event_args struct template (C++/WinRT)
A type that you can use to implement (produce) the deferrable event pattern. For more info, and code examples, see [Deferrable events](/windows/uwp/cpp-and-winrt-apis/author-events#deferrable-events).

## Syntax
```cppwinrt
template<typename D>
struct deferrable_event_args
```

### Template parameters
`typename D`
The type of the event args of the deferrable event.

## Requirements
**Minimum supported SDK:** Currently in [Windows SDK Insider Preview](https://www.microsoft.com/software-download/windowsinsiderpreviewSDK)

**Namespace:** winrt

**Header:** $(ProjectDir)Generated Files\winrt\Windows.Foundation.h

## Member functions
|Function|Description|
|------------|-----------------|
|[deferrable_event_args::GetDeferral function](#deferrable_event_argsgetdeferral-function)|Called by the event recipient in order to retrieve a deferral.|
|[deferrable_event_args::wait_for_deferrals function](#deferrable_event_argswait_for_deferrals-function)|Completes when all outstanding deferrals have completed (if no deferrals were taken, then it completes immediately).|

## deferrable_event_args::GetDeferral function
Called by the event recipient in order to retrieve a deferral. Doing so indicates to the event source that post-event activities should be postponed until [Complete](/uwp/api/windows.foundation.deferral.complete) has been called on the deferral. This allows an event handler to perform asynchronous actions in response to an event.

### Syntax
```cppwinrt
winrt::Windows::Foundation::Deferral GetDeferral();
```

### Return value 
A [Windows::Foundation::Deferral](/uwp/api/windows.foundation.deferral) object.

## deferrable_event_args::wait_for_deferrals function
Completes when all outstanding deferrals have completed (if no deferrals were taken, then it completes immediately).

### Syntax
```cppwinrt
winrt::Windows::Foundation::IAsyncAction wait_for_deferrals();
```

### Return value 
A [Windows::Foundation::IAsyncAction](/uwp/api/windows.foundation.iasyncaction) object.

## See also 
* [winrt namespace](winrt.md)
* [Author events in C++/WinRT](/windows/uwp/cpp-and-winrt-apis/author-events)
