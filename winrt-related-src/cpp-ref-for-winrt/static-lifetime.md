---
description: A marker type used to opt an activation factory in to static lifetime.
title: winrt::static_lifetime marker struct (C++/WinRT)
dev_langs: ["C++"]
ms.date: 03/19/2019
ms.topic: "language-reference"
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, marker, type
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::static_lifetime marker struct (C++/WinRT)

A marker type, which is passed to the [**implements**](implements.md) base struct of an activation factory in order to opt it in to static lifetime (to *pin* it). For a usage example of marker types, see [Marker types](implements.md#marker-types).

## Syntax
```cppwinrt
struct winrt::static_lifetime
```

### Examples

Here's a specific example of **winrt::static_lifetime**. If you want the activation factory for **MyRuntimeClass** to be a singleton, then pin it like this.

```cppwinrt
// MyRuntimeclass.h
#pragma once

#include "MyRuntimeClass.g.h"

namespace winrt::MYNAMESPACE::implementation
{
    struct MyRuntimeClass : MyRuntimeClassT<MyRuntimeClass> { ... };
}

namespace winrt::MYNAMESPACE::factory_implementation
{
    struct MyRuntimeClass : MyRuntimeClassT<MyRuntimeClass, implementation::MyRuntimeClass, static_lifetime>
    {
    };
}
```

You should implement static events on your activation factory object using the **winrt::static_lifetime** marker. You pin the factory to ensure that its lifetime is stable as event handlers are added and removed. You can do all that in a header such as in this next example.

> [!NOTE]
> A new C++/WinRT project (from a project template) will use [component optimizations](/windows/uwp/cpp-and-winrt-apis/news#component-optimizations) by default. If you're *not* using component optimizations, then you can omit the part of the listing indicated.

```cppwinrt
// MyRuntimeClass.h
#pragma once

#include "MyRuntimeClass.g.h"

// Forward-declare the instance class.
namespace winrt::Component::implementation
{
    struct MyRuntimeClass;
}

// Then define the activation factory class before the instance class.
namespace winrt::Component::factory_implementation
{
    struct MyRuntimeClass : MyRuntimeClassT<MyRuntimeClass, implementation::MyRuntimeClass, static_lifetime>
    {
        winrt::event_token MyRuntimeClassEvent(Windows::Foundation::EventHandler<int32_t> const& handler)
        {
            return m_static.add(handler);
        }

        void MyRuntimeClassEvent(winrt::event_token const& cookie)
        {
            m_static.remove(cookie);
        }

        void RaiseMyRuntimeClassStaticEvent(int32_t value)
        {
            m_static(nullptr, value);
        }

        event<Windows::Foundation::EventHandler<int32_t>> m_static;
    };
}

namespace winrt::Component::implementation
{
    struct MyRuntimeClass
    {
        MyRuntimeClass() = delete;

        // If you're not using component optimizations, then you can omit these next three methods.

        // Component optimizations means that you have to implement any statics on the instance class,
        // and have those forward to the activation factory. You will see build errors if you don't do this.

        static winrt::event_token MyRuntimeClassStaticEvent(Windows::Foundation::EventHandler<int32_t> const& handler)
        {
            return make_self<factory_implementation::MyRuntimeClass>()->MyRuntimeClassStaticEvent(handler);
        }

        static void MyRuntimeClassStaticEvent(winrt::event_token const& cookie)
        {
            return make_self<factory_implementation::MyRuntimeClass>()->MyRuntimeClassStaticEvent(cookie);
        }

        static void RaiseMyRuntimeClassStaticEvent(int32_t value)
        {
            return make_self<factory_implementation::MyRuntimeClass>()->RaiseMyRuntimeClassStaticEvent(value);
        }
    };
}
```

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17763.0 (Windows 10, version 1809)

**Namespace:** winrt

**Header:** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## See also 
* [winrt namespace](winrt.md)
