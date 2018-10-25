---
author: stevewhims
description: When you register a delegate, you can request an event revoker, which you can use to either automatically or manually revoke your delegate.
title: winrt::event_revoker struct template (C++/WinRT)
dev_langs: ["C++"]
ms.author: stwhi
ms.date: 05/18/2018

ms.topic: "language-reference"


keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::event_revoker struct template (C++/WinRT)

When you register a delegate, you can request an event revoker object (also known as an auto revoker). You can manually revoke your delegate by calling the **event_revoker::revoke** member function on that object, or you can just allow it to go out of scope. For more info, and a code example, see [Revoke a registered delegate](/windows/uwp/cpp-and-winrt-apis/handle-events#revoke-a-registered-delegate).

## Syntax
```cppwinrt
template <typename I>
struct event_revoker
```

### Template parameters
`typename I`
The type of the event source (the object that raises the event).

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17134.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## Member functions
|Function|Description|
|------------|-----------------|
|[event_revoker::revoke function](#eventrevokerrevoke-function)|Revokes the delegate from whose registration the **event_revoker** object was returned.|

## event_revoker::revoke function
Revokes the delegate from whose registration the **event_revoker** object was returned.

### Syntax
```cppwinrt
void revoke() noexcept;
```

## See also
* [winrt namespace](winrt.md)
* [Handle events by using delegates in C++/WinRT](/windows/uwp/cpp-and-winrt-apis/handle-events)
