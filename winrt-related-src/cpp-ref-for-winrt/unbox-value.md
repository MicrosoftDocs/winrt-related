---

title: winrt::unbox_value function template (C++/WinRT)
description: A function template that unwraps (or *unboxes*) a scalar or array value from inside a reference class object so that it can be processed in a function that expects **IInspectable**.
dev_langs: ["C++"]

ms.date: 04/10/2018
ms.topic: "language-reference"
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, box, boxing, unbox, unboxing
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::unbox_value function template (C++/WinRT)

> [!NOTE]
> You can unbox not only scalar values, but also most kinds of arrays (with the exception of arrays of enumerations) by using the **winrt::unbox_value** function.

A function template that unwraps (or *unboxes*) a scalar or array value from inside a reference class object so that it can be processed in a function that expects **IInspectable**. For more details, and code examples, see [Boxing and unboxing values to IInspectable with C++/WinRT](/windows/uwp/cpp-and-winrt-apis/boxing).

## Syntax
```cppwinrt
template <typename T>
T unbox_value(winrt::Windows::Foundation::IInspectable const& value);
```

### Template parameters
`typename T`
A scalar or array type.

### Parameters
`value`
A reference class object containing a boxed value.

### Return value 
The scalar or array value contained inside the reference class object.

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17134.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header:** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\Windows.Foundation.h

## See also 
* [winrt namespace](winrt.md)
* [winrt::box_value function template](box-value.md)
* [winrt::unbox_value_or function template](unbox-value-or.md)
* [Boxing and unboxing values to IInspectable with C++/WinRT](/windows/uwp/cpp-and-winrt-apis/boxing)
