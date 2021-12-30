---

description: A factory method that returns an instance of a projected type or interface when parameterized with the corresponding implementation type.
title: winrt::make function template (C++/WinRT)
dev_langs: ["C++"]

ms.date: 04/17/2018

ms.topic: "language-reference"


keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, construct, instantiate, projected, projection, implementation
ms.workload: ["cplusplus"]
---

# winrt::make function template (C++/WinRT)

A factory method that, when a [C++/WinRT](/windows/uwp/cpp-and-winrt-apis/intro-to-using-cpp-with-winrt) implementation type is provided as a type parameter, returns one of the following.

- If you're authoring a component to be consumed from an app, then call **make** to return the default (projected) interface of the implementation type. In this case, your project doesn't contain a projected type.
- If you're both implementing and consuming a runtime class within the same compilation unit&mdash;for example, authoring a type to be consumed from XAML UI&mdash;then call **make** to return an instance of the projected type.

For an explanation of the implementation type and projected type concepts, see [Consume APIs with C++/WinRT](/windows/uwp/cpp-and-winrt-apis/consume-apis) and [Author APIs with C++/WinRT](/windows/uwp/cpp-and-winrt-apis/author-apis). For more details, code, and a walkthrough of calling **make** in practice, see [XAML; binding a control to C++/WinRT properties and collections](/windows/uwp/cpp-and-winrt-apis/binding-property#add-a-property-of-type-bookstoreviewmodel-to-mainpage). Also see [make_self](make-self.md), which returns a [*com_ptr*](com-ptr.md) to an instance of the *implementation* type instead.

## Syntax
```cppwinrt
template <typename D, typename... Args>
auto make(Args&&... args);
```

### Template parameters
`typename D`
An implementation type.

### Parameters
`args`
Any constructor arguments for the constructor being invoked.

### Return value 
The default interface of the implementation type if no projected type exists, otherwise an instance of the projected type.

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17134.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header:** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## See also 
* [winrt namespace](winrt.md)
* [winrt::make_self function template](make-self.md)
* [Consume APIs with C++/WinRT](/windows/uwp/cpp-and-winrt-apis/consume-apis)
* [Author APIs with C++/WinRT](/windows/uwp/cpp-and-winrt-apis/author-apis)
* [XAML controls; bind to a C++/WinRT property](/windows/uwp/cpp-and-winrt-apis/binding-property)
