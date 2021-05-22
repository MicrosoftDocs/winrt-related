---
description: A helper function that retrieves the activation factory for a specified Windows Runtime class type.
title: winrt::get_activation_factory function template (C++/WinRT)
dev_langs: ["C++"]
ms.date: 04/30/2018
ms.topic: "language-reference"
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, get, activation, factory
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::get_activation_factory function template (C++/WinRT)

A helper function that retrieves the activation factory for a specified Windows Runtime class type.

## Syntax
```cppwinrt
template <typename Class, typename Interface = winrt::Windows::Foundation::IActivationFactory>
auto get_activation_factory();
```

### Template parameters
`typename Class`
A Windows Runtime class type whose activation factory to retrieve.

`typename Interface`
An interface implemented by the activation factory.

### Return value 
A reference to the specified interface of the activation factory for the specified Windows Runtime class type.

### Example
```cppwinrt
auto factory = winrt::get_activation_factory<BankAccountWRC::BankAccount>();
BankAccountWRC::BankAccount account = factory.ActivateInstance<BankAccountWRC::BankAccount>();
```

```cppwinrt
using namespace winrt::Windows::Foundation;
...
auto factory = winrt::get_activation_factory<Uri, IUriRuntimeClassFactory>();
Uri account = factory.CreateUri(L"https://www.contoso.com");
```

```cppwinrt
using namespace winrt::Windows::Globalization::NumberFormatting;
...
auto factory = winrt::get_activation_factory<CurrencyFormatter, ICurrencyFormatterFactory>();
CurrencyFormatter currency = factory.CreateCurrencyFormatterCode(L"USD");
```

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17134.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header:** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## See also 
* [winrt namespace](winrt.md)
