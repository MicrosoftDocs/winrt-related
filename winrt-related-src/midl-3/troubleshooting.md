---
author: stevewhims
description: A table of troubleshooting symptoms and remedies.
title: Troubleshooting Microsoft Interface Definition Language 3.0 issues
ms.author: stwhi
ms.date: 03/31/2018
ms.topic: "language-reference"
keywords: windows 10, uwp, winrt, api, reference, idl, midl, 3.0, 3, midl3, troubleshooting
ms.localizationpriority: medium
---

# Troubleshooting Microsoft Interface Definition Language 3.0 issues
The table of troubleshooting symptoms and remedies below may be helpful to you whether you're cutting new code or porting an existing app.

> [!NOTE]
> The purpose of Microsoft Interface Definition Language (MIDL) 3.0 is to declare Windows Runtime types inside Interface Definition Language (IDL) files (`.idl` files). MIDL 3.0 is a particularly convenient way to declare [C++/WinRT](/windows/uwp/cpp-and-winrt-apis/index) runtime classes. For more info and background, see [Introduction to Microsoft Interface Definition Language 3.0](intro.md).
>
> IDL files have traditionally been used to declare COM types; so, MIDL 3.0 represents a new and different way of using IDL files, with an expanded syntax for them. For more info about using IDL files to declare non-Windows Runtime types (COM types), see [Microsoft Interface Definition Language](/windows/desktop/midl/midl-start-page).

## Symptoms and remedies
| Symptom | Remedy |
|---------|--------|
| Compiling in Visual Studio results in "*error MIDL2003: [msg]redefinition [context]: IUnknown*", and many other similar errors. | Your toolchain is set up to automatically reference any types that are in system namespaces. In your IDL files, remove any `import` directives for Windows namespaces; you only need to `import` any types that you've defined in your project. |
| *error MIDL2009 : [msg]undefined symbol [context]: IInspectable*. | Your toolchain is *not* set up to automatically import types in system namespaces. If you're using `midl.exe` from the command line, then see [Declaration structure, and calling midl.exe from the command line](intro.md#declaration-structure-and-calling-midlexe-from-the-command-line) for the correct command-line syntax; specifically the use of the `/reference` switch. Alternatively, compile your IDL files using Visual Studio with the C++/WinRT Visual Studio Extension (VSIX) (see [Visual Studio support for C++/WinRT, and the VSIX](/windows/uwp/cpp-and-winrt-apis/intro-to-using-cpp-with-winrt#visual-studio-support-for-cwinrt-and-the-vsix)). If you do any of these things, then it won't be necessary to add an `import` directive for `Windows.Foundation.idl` to your IDL file. But you *will* need the `import` directive to import additional IDL if you're referencing types that you've defined in your project. |
| *error MIDL2011 : [msg]unresolved type declaration [context]:*, followed by a type name. | In your IDL file, add an `import` directive for the IDL file(s) that contain the declarations of any type(s) that you reference that you've defined in your project. |
| *error MIDL2025: [msg]syntax error [context]: expecting > or, near ">>"* | Insert a space between the two `>` characters so the pair of template-closing characters is not misinterpreted as a right-shift operator. |
| *error MIDL2025: [msg]syntax error [context]: expecting > or, near "["* | This error can occur if you use an array as a parameter type argument to a parameterized interface. Doing so is not valid. But also see [**IReferenceArray\<T\>**](/uwp/api/windows.foundation.ireferencearray_t_). |
| The Windows App Certification Kit tests produce an error that one of your runtime classes "*does not derive from a Windows base class. All composable classes must ultimately derive from a type in the Windows namespace*".|Any runtime class (that you declare in your application) that derives from a base class is known as a *composable* class. The ultimate base class of a composable class must be a type originating in a Windows.* namespace; for example, [**Windows.UI.Xaml.DependencyObject**](/uwp/api/windows.ui.xaml.dependencyobject). See [XAML controls; bind to a C++/WinRT property](/windows/uwp/cpp-and-winrt-apis/binding-property) for more details.|
