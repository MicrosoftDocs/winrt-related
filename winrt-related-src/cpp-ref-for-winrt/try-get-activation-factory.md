---

description: A helper function that retrieves the activation factory for a specified Windows Runtime class type or an empty **com_ptr** if not successful.
title: winrt::try_get_activation_factory function template (C++/WinRT)
dev_langs: ["C++"]
ms.date: 03/31/2021
ms.topic: "language-reference"
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, get, activation, factory
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::try_get_activation_factory function template (C++/WinRT)

A helper function that retrieves the activation factory for a specified Windows Runtime class type or an empty **com_ptr** if not successful.

Also see the [winrt::get_activation_factory function template](./get-activation-factory.md).

## Syntax
```cppwinrt
template <typename Class, typename Interface = Windows::Foundation::IActivationFactory>
auto try_get_activation_factory() noexcept;

template <typename Class, typename Interface = Windows::Foundation::IActivationFactory>
auto try_get_activation_factory(hresult_error& exception) noexcept;
```

### Template parameters
`typename Class`
A Windows Runtime class type whose activation factory to retrieve.

`typename Interface`
An interface implemented by the activation factory.

### Return value 
A reference to the specified interface of the activation factory for the specified Windows Runtime class type or an empty **com_ptr** if not successful.

### Example

This example verifies that a class is present on the system before using it. For example, the class might be in a different device family from that of the machine running the app (see [Programming with extension SDKs](../extension-sdks/device-families-overview.md)). The technique shown below works with public and non-public types.

```cppwinrt
if (auto factory { winrt::try_get_activation_factory<Class>() })
{
    // use Class.
}
```

Also see the examples for [winrt::get_activation_factory function template](./get-activation-factory.md).

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17763.0 (Windows 10, version 1809)

**Namespace:** winrt

**Header** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## See also 
* [winrt namespace](winrt.md)