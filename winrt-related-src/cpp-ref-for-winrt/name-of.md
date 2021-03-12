---
description: A helper function that retrieves a string view containing the fully-qualified type name of a particular Windows Runtime class.
title: winrt::name_of function template (C++/WinRT)
dev_langs: ["C++"]
ms.date: 03/10/2021
ms.topic: "language-reference"
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, projected, implementation, type
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::name_of function template (C++/WinRT)

A helper function that retrieves a string view containing the fully-qualified type name of a particular Windows Runtime class.

**name_of** works best with a projected type. If you specify an implementation type, then **name_of** returns the stringified GUID of the default interface.

## Syntax
```cppwinrt
template <typename T>
constexpr auto name_of() noexcept;
```

### Template parameters
`typename T`
A projected interface or runtime class type.

### Return value 
A string view with a null-terminator beyond the end.

### Example

```cppwinrt
if (ApiInformation.IsMethodPresent(
      winrt::name_of<Windows::Devices::PointOfService::ReceiptPrintJob>(),
      L"FeedPaperByLine")) {
  ...
}
```

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17134.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## See also 
* [winrt namespace](winrt.md)
