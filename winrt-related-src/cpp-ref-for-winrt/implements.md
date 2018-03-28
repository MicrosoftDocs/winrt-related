---
author: stevewhims
description: A base struct template that implements one or more Windows Runtime interfaces on behalf of a derived type.
title: winrt::implements struct template (C++/WinRT)
dev_langs: ["C++"]
ms.author: stwhi
manager: "markl"
ms.date: 03/26/2018
ms.technology: "cpp-windows"
ms.topic: "language-reference"
ms.prod: windows
ms.technology: uwp
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, implement, interface
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::implements struct template (C++/WinRT)
> [!NOTE]
> **Some information relates to pre-released product which may be substantially modified before it’s commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

A base struct template that implements one or more Windows Runtime interfaces on behalf of a derived type. For more info about deriving from this type, and examples, see [Interfaces; how to implement them in C++/WinRT](/windows/uwp/cpp-and-winrt-apis/implement-an-interface).

## Syntax
```cppwinrt
template <typename D, typename... I>
struct implements : impl::producer<D, impl::uncloak_t<I>>..., impl::base_implements<D, I...>::type
```

### Template parameters
`typename D`
Your derived type name.

`typename... I`
Any number of interfaces to implement.

### Example
```cppwinrt
// App.cpp
...
struct App : implements<App, IFrameworkViewSource>
{
	IFrameworkView CreateView()
	{
		return ...
	}
}
...
```

## Requirements
**Minimum supported SDK:** Windows SDK for Windows 10, version 1803

**Namespace:** winrt

**Header** %ProgramFiles(x86)%\Windows Kits\10\Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## Member functions
|Function|Description|
|------------|-----------------|
|[implements::AddRef function](#implementsaddref-function)|Increments the reference count for the default interface of the **implements** object.|
|[implements::find_interface function](#implementsfindinterface-function)|The pointer to the interface implemented by the **implements** object, identified by the specified identifier; doesn't call **AddRef**.|
|[implements::get_local_iids function](#implementsgetlocaliids-function)|Retrieves a two-element tuple containing the identifiers of the interfaces that are implemented by the **implements** object.|
|[implements::QueryInterface function](#implementsqueryinterface-function)|Retrieves the pointer to the interface implemented by the **implements** object, identified by the specified identifier; calls **AddRef**.|
|[implements::Release function](#implementsrelease-function)|Decrements the reference count for the default interface of the **implements** object.|

## Member operators
|Operator|Description| 
|------------|-----------------|
|[implements::operator Windows::Foundation::IInspectable](#implementsoperator-windowsfoundationiinspectable)|Converts the **implements** object to a **Windows::Foundation::IInspectable**.|

## implements::AddRef function
Increments the reference count for the default interface of the **implements** object.

### Syntax
```cppwinrt
unsigned long __stdcall AddRef() noexcept
```

### Return value 
The new reference count. This value is intended to be used only for test purposes.

## implements::find_interface function
Retrieves the pointer to the interface implemented by the **implements** object, identified by the specified identifier. Does not call **AddRef** on the pointer that it returns.

### Syntax
```cppwinrt
void* find_interface(GUID const& id) const noexcept override
```

### Return value 
The pointer to the interface implemented by the **implements** object, identified by the specified identifier.

## implements::get_local_iids function
Retrieves a two-element tuple containing the identifiers of the interfaces that are implemented by the **implements** object.

### Syntax
```cppwinrt
std::pair<uint32_t, const GUID*> get_local_iids() const noexcept override
```

### Return value 
A two-element tuple containing the identifiers of the interfaces that are implemented by the **implements** object

## implements::QueryInterface function
Retrieves the pointer to the interface implemented by the **implements** object, identified by the specified identifier. Calls **AddRef** on the pointer that it returns.

### Syntax
```cppwinrt
HRESULT __stdcall QueryInterface(GUID const& id, void** object) noexcept
```

### Return value 
The new reference count. This value is intended to be used only for test purposes.

## implements::Release function
Decrements the reference count for the default interface of the **implements** object.

### Syntax
```cppwinrt
unsigned long __stdcall Release() noexcept
```

### Return value 
The new reference count. This value is intended to be used only for test purposes.

## implements::operator Windows::Foundation::IInspectable
Converts the **implements** object to a **Windows::Foundation::IInspectable**. This operators allows you to pass the **implements** object to a function that expects an **IInspectable**.

### Syntax
```cppwinrt
operator Windows::Foundation::IInspectable() const noexcept
```

### Return value
The **implements** object converted to a **Windows::Foundation::IInspectable**.

## See also 
[winrt namespace (C++/WinRT)](winrt.md)
