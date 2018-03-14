---
author: stevewhims
description: A function template that unwraps (or *unboxes*) a scalar value from inside a reference class object so that it can be processed in a function that expects **IInspectable**.
dev_langs: ["C++"]
ms.author: stwhi
manager: "markl"
ms.date: 03/13/2018
ms.technology: "cpp-windows"
ms.topic: "language-reference"
ms.prod: windows
ms.technology: uwp
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, box, boxing, unbox, unboxing
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::unbox_value function template (C++/WinRT)
> [!NOTE]
> **Some information relates to pre-released product which may be substantially modified before it’s commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

A function template that unwraps (or *unboxes*) a scalar value from inside a reference class object so that it can be processed in a function that expects **IInspectable**. For more details, and code examples, see [Boxing and unboxing scalar values to IInspectable with C++/WinRT](/windows/uwp/cpp-and-winrt-apis/boxing?branch=live).

## Syntax
```cppwinrt
template <typename T>
T unbox_value(Windows::Foundation::IInspectable const& value)
```

### Template parameters
`typename T`
A scalar type.

### Parameters
`value`
A reference class object containing a boxed value.

### Return value 
The scalar value contained inside the reference class object.

## Requirements
**Minimum supported SDK:** Windows SDK for Windows 10, version 1803

**Namespace:** winrt

**Header** %ProgramFiles(x86)%\Windows Kits\10\Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## See also 
* [winrt namespace (C++/WinRT)](winrt.md)
* [Boxing and unboxing scalar values to IInspectable with C++/WinRT](/windows/uwp/cpp-and-winrt-apis/boxing?branch=live)