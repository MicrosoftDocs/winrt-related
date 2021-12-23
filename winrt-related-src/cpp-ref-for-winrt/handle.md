---
description: Represents a Windows handle object.
title: winrt::handle struct (C++/WinRT)
dev_langs: ["C++"]
ms.date: 05/14/2018
ms.topic: "language-reference"
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, Windows, handle
ms.workload: ["cplusplus"]
---

# winrt::handle struct (C++/WinRT)

Represents a Windows handle object. **winrt::handle** is a type alias for **winrt::handle_type&lt;winrt::handle_traits&gt;**, so see the [**winrt::handle_type**](handle-type.md) struct template topic to learn about the functions and operators that are available to **winrt::handle**.

## Syntax
```cppwinrt
struct handle_traits {};

using handle = handle_type<handle_traits>;
```

### Example
```cppwinrt
winrt::handle h{ ::CreateEvent(nullptr, false, false, nullptr) };
winrt::check_bool(bool{ h });
winrt::check_bool(::SetEvent(h.get()));
```

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17134.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header:** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## See also 
* [winrt namespace](winrt.md)
* [winrt::handle_type struct template](handle-type.md)
* [winrt::file_handle struct](file-handle.md)
