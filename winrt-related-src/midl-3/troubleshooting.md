---
author: stevewhims
description: A table of troubleshooting symptoms and remedies.
title: Troubleshooting Microsoft Interface Definition Language 3.0 issues
ms.author: stwhi
ms.date: 03/31/2018
ms.topic: "language-reference"
ms.prod: windows
ms.technology: uwp
keywords: windows 10, uwp, winrt, api, reference, idl, midl, 3.0, troubleshooting
ms.localizationpriority: medium
---

# Troubleshooting Microsoft Interface Definition Language 3.0 issues
> [!NOTE]
> **Some information relates to pre-released product which may be substantially modified before it’s commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

This topic is up front so that you're aware of it right away; even if you don't need it yet. The table of troubleshooting symptoms and remedies below may be helpful to you whether you're cutting new code or porting an existing app.

## Symptoms and remedies
| Symptom | Remedy |
|---------|--------|
| Compiling in Visual Studio results in "*error MIDL2003: [msg]redefinition [context]: IUnknown*", and many other similar errors. | Your version of the tools automatically import any types that are in system namespaces. In your IDL files, remove any import directives for Windows namespaces; you only need to import any types that you've defined in your project. |
| *error MIDL2009 : [msg]undefined symbol [context]: IInspectable*. | In your IDL file, add an import directive for `Windows.Foundation.idl`. You may need to import additional IDL for any types you're referencing. |
| *error MIDL2011 : [msg]unresolved type declaration [context]:*, followed by a type name. | In your IDL file, add an import directive for the IDL file(s) that contain the declarations of any type(s) that you reference. |
| The Windows App Certification Kit tests produce an error that one of your runtime classes "*does not derive from a Windows base class. All composable classes must ultimately derive from a type in the Windows namespace*".|The ultimate base class of each runtime class *declared in the application* must be a type originating in a Windows.* namespace. You can derive a view model from [**Windows.UI.Xaml.DependencyObject**](/uwp/api/windows.ui.xaml.dependencyobject). Alternatively, declare a bindable base class derived from **DependencyObject**, and derive your view models from that.|
