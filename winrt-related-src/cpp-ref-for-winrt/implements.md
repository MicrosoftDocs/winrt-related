---
author: stevewhims
description: A base struct template that implements one or more Windows Runtime interfaces on behalf of a derived type.
title: winrt::implements struct template (C++/WinRT)
dev_langs: ["C++"]
ms.author: stwhi
ms.date: 04/17/2018

ms.topic: "language-reference"


keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, implement, interface
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::implements struct template (C++/WinRT)

This is the base from which your own [C++/WinRT](/windows/uwp/cpp-and-winrt-apis/intro-to-using-cpp-with-winrt) implementations directly or indirectly derive. It implements one or more Windows Runtime interfaces (which you specify to it as type parameters), and it also provides efficient implementations of [IUnknown](https://msdn.microsoft.com/library/windows/desktop/ms680509), [IInspectable](/windows/desktop/api/inspectable/nn-inspectable-iinspectable), [IAgileObject](https://msdn.microsoft.com/library/windows/desktop/hh802476), [IWeakReferenceSource](/windows/desktop/api/weakreference/nn-weakreference-iweakreferencesource), and others.

For more info about deriving from this type, and examples, see [Author APIs with C++/WinRT](/windows/uwp/cpp-and-winrt-apis/author-apis).

## Marker types
The **implements** struct template supports the [non_agile](non-agile.md) and [no_weak_ref](no-weak-ref.md) marker types, which override default behavior. They should be rarely used, because the defaults are sufficient for almost all cases. A marker type can appear anywhere in the interface list, which is the variadic parameter pack.

This first example applies when you derive directly from **implements**.

```cppwinrt
struct MyImplementation: implements<MyImplementation, IFrameworkViewSource, no_weak_ref>
{
    ...
}
```

This next example is for when you're authoring a runtime class.

```cppwinrt
struct BookSku : BookSkuT<BookSku, no_weak_ref>
{
    ...
}
```

## Syntax
```cppwinrt
template <typename D, typename... I>
struct implements
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
**Minimum supported SDK:** Windows SDK version 10.0.17134.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## Member functions
|Function|Description|
|------------|-----------------|
|[implements::AddRef function](#implementsaddref-function)|Increments the reference count for the default interface of the **implements** object.|
|[implements::find_interface function](#implementsfindinterface-function)|The pointer to the interface implemented by the **implements** object, identified by the specified identifier; doesn't call **AddRef**.|
|[implements::get_local_iids function](#implementsgetlocaliids-function)|Retrieves a two-element tuple containing the identifiers of the interfaces that are implemented by the **implements** object.|
|[implements::QueryInterface function](#implementsqueryinterface-function)|Retrieves the pointer to the interface implemented by the **implements** object, identified by the specified identifier; calls **AddRef**.|
|[implements::Release function](#implementsrelease-function)|Decrements the reference count for the default interface of the **implements** object.|

## Protected member functions
|Function|Description|
|------------|-----------------|
|[implements::get_strong function](#implementsgetstrong-function)|Retrieves a strong reference to the **implements** object's *this* pointer.|
|[implements::get_weak function](#implementsgetweak-function)|Retrieves a weak reference to the **implements** object's *this* pointer.|
|[implements::static_lifetime function](#implementsstaticlifetime-function)|Configures the **implements** object to have static lifetime.|

## Member operators
|Operator|Description| 
|------------|-----------------|
|[implements::operator Windows::Foundation::IInspectable](#implementsoperator-windowsfoundationiinspectable)|Converts the **implements** object to a **Windows::Foundation::IInspectable**.|

## implements::AddRef function
Increments the reference count for the default interface of the **implements** object.

### Syntax
```cppwinrt
unsigned long __stdcall AddRef() noexcept;
```

### Return value 
The new reference count. This value is intended to be used only for test purposes.

## implements::find_interface function
Retrieves the pointer to the interface implemented by the **implements** object, identified by the specified identifier. Does not call **AddRef** on the pointer that it returns.

### Syntax
```cppwinrt
void* find_interface(GUID const& id) const noexcept override;
```

### Return value 
The pointer to the interface implemented by the **implements** object, identified by the specified identifier.

## implements::get_local_iids function
Retrieves a two-element tuple containing the identifiers of the interfaces that are implemented by the **implements** object.

### Syntax
```cppwinrt
std::pair<uint32_t, const GUID*> get_local_iids() const noexcept override;
```

### Return value 
A two-element tuple containing the identifiers of the interfaces that are implemented by the **implements** object.

## implements::get_strong function
Retrieves a strong reference to the **implements** object's *this* pointer.

### Syntax
```cppwinrt
protected:
    winrt::com_ptr<D> get_strong() noexcept;
```

### Return value 
A strong reference to the **implements** object's *this* pointer.

## implements::get_weak function
Retrieves a weak reference to the **implements** object's *this* pointer. See [Strong and weak references in C++/WinRT](/windows/uwp/cpp-and-winrt-apis/weak-references).

### Syntax
```cppwinrt
protected:
    winrt::weak_ref<D> get_weak() noexcept;
```

### Return value 
A [**weak_ref**](weak-ref.md) object representing a weak reference to the **implements** object's *this* pointer.

## implements::QueryInterface function
Retrieves the pointer to the interface implemented by the **implements** object, identified by the specified identifier. Calls **AddRef** on the pointer that it returns.

### Syntax
```cppwinrt
HRESULT __stdcall QueryInterface(GUID const& id, void** object) noexcept;
```

### Return value 
The new reference count. This value is intended to be used only for test purposes.

## implements::Release function
Decrements the reference count for the default interface of the **implements** object.

### Syntax
```cppwinrt
unsigned long __stdcall Release() noexcept;
```

### Return value 
The new reference count. This value is intended to be used only for test purposes.

## implements::static_lifetime function
Configures the **implements** object to have static lifetime.

### Syntax
```cppwinrt
protected:
    void static_lifetime();
```

## implements::operator Windows::Foundation::IInspectable
Converts the **implements** object to a **Windows::Foundation::IInspectable**. This operators allows you to pass the **implements** object to a function that expects an **IInspectable**.

### Syntax
```cppwinrt
operator winrt::Windows::Foundation::IInspectable() const noexcept;
```

### Return value
The **implements** object converted to a **Windows::Foundation::IInspectable**.

## See also 
* [winrt namespace](winrt.md)
* [winrt::weak_ref struct template](weak-ref.md)
* [Author APIs with C++/WinRT](/windows/uwp/cpp-and-winrt-apis/author-apis)
* [Strong and weak references in C++/WinRT](/windows/uwp/cpp-and-winrt-apis/weak-references)
