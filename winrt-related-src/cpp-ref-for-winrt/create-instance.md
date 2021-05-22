---
description: A function template that creates a single uninitialized object of the class associated with a specified CLSID, and returns it as a [winrt::com_ptr](./com-ptr.md) or throws if not successful.
title: winrt::create_instance function template (C++/WinRT)
dev_langs: ["C++"]
ms.date: 06/16/2020
ms.topic: "language-reference"
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, create_instance, cocreateinstance
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::create_instance function template (C++/WinRT)

A function template that creates a single uninitialized object of the class associated with a specified CLSID, and returns it as a [winrt::com_ptr](./com-ptr.md) or throws if not successful.

## Syntax

```cppwinrt
template <typename Interface>
winrt::com_ptr<Interface> create_instance(guid const& clsid,
    uint32_t context = 0x1 /*CLSCTX_INPROC_SERVER*/,
    void* outer = nullptr);
```

### Template parameters

`typename Interface`
The type of the interface pointer to query for on the newly created object.

### Parameters

`clsid`
The CLSID associated with the data and code that will be used to create the object.

`context`
Context in which the code that manages the newly created object will run. The values are taken from the enumeration [CLSCTX](/windows/win32/api/wtypesbase/ne-wtypesbase-clsctx).

`outer`
If `nullptr`, indicates that the object is not being created as part of an aggregate. If not `nullptr`, a pointer to the aggregate object's [IUnknown](/windows/win32/api/unknwn/nn-unknwn-iunknown) interface (the controlling **IUnknown**).

### Return value

A [winrt::com_ptr](./com-ptr.md) of the newly created object. Throws if not successful.

## Requirements

**Minimum supported SDK:** Windows SDK version 10.0.17134.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header:** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## See also 

* [winrt namespace](./winrt.md)
* [try_create_instance function template](./try-create-instance.md)
* [winrt::com_ptr struct template](./com-ptr.md)