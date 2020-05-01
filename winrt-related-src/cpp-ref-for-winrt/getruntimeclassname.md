---

description: A member function (of a generated implementation type) that returns a string containing the fully-qualified type name of the Windows Runtime class being implemented.
title: GetRuntimeClassName function (C++/WinRT)
dev_langs: ["C++"]

ms.date: 04/30/2018

ms.topic: "language-reference"


keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, runtime, class, name, string
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# GetRuntimeClassName function (C++/WinRT)

A member function (of a generated implementation type) that returns a string containing the fully-qualified type name of the Windows Runtime class being implemented.

For an explanation of the implementation type and projected type concepts, see [Consume APIs with C++/WinRT](/windows/uwp/cpp-and-winrt-apis/consume-apis) and [Author APIs with C++/WinRT](/windows/uwp/cpp-and-winrt-apis/author-apis).

Also see [IInspectable::GetRuntimeClassName](/windows/win32/api/inspectable/nf-inspectable-iinspectable-getruntimeclassname).

## Syntax
```cppwinrt
winrt::hstring GetRuntimeClassName() const;
```

### Return value
A [winrt::hstring](hstring.md) containing the fully-qualified type name of the Windows Runtime class implemented by the implementation type.

### Example
```cppwinrt
// MainPage.cpp
void winrt::MyProject::implementation::MainPage::f()
{
    winrt::hstring name = GetRuntimeClassName();
    assert(name == L"MyProject.MainPage");
}
```

You can implement [ICustomPropertyProvider::Type](/uwp/api/windows.ui.xaml.data.icustompropertyprovider.type) like this.

```cppwinrt
Windows::UI::Xaml::Interop::TypeName Type()
{
    return Windows::UI::Xaml::Interop::TypeName{ GetRuntimeClassName() };
};
```

Or you can use the [winrt::xaml_typename](xaml-typename.md) function template.

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17134.0 (Windows 10, version 1803)

**Tool:** cppwinrt.exe

## See also 
* [winrt::xaml_typename function template](xaml-typename.md)
* [Consume APIs with C++/WinRT](/windows/uwp/cpp-and-winrt-apis/consume-apis)
* [Author APIs with C++/WinRT](/windows/uwp/cpp-and-winrt-apis/author-apis)
