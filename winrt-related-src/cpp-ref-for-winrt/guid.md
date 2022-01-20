---
title: winrt::guid struct (C++/WinRT)
description: Represents a globally-unique identifier ([GUID](/windows/win32/api/guiddef/ns-guiddef-guid)).
dev_langs: ["C++"]
ms.date: 12/08/2021
ms.topic: "language-reference"
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, Windows, guid
ms.workload: ["cplusplus"]
---

# winrt::guid struct (C++/WinRT)

Represents a globally-unique identifier ([GUID](/windows/win32/api/guiddef/ns-guiddef-guid)).

For more details, and code examples, see [Interoperating with the ABI's GUID struct](/windows/uwp/cpp-and-winrt-apis/interop-winrt-abi#interoperating-with-the-abis-guid-struct).

## Syntax
```cppwinrt
struct guid
{
    public:
        uint32_t Data1;
        uint16_t Data2;
        uint16_t Data3;
        uint8_t  Data4[8];

        guid() noexcept = default;

        constexpr guid(uint32_t const Data1, uint16_t const Data2, uint16_t const Data3, std::array<uint8_t, 8> const& Data4) noexcept;

#ifdef WINRT_IMPL_IUNKNOWN_DEFINED
        constexpr guid(GUID const& value) noexcept;
        operator GUID const&() const noexcept;
#endif

        constexpr explicit guid(std::string_view const value);
        constexpr explicit guid(std::wstring_view const value);
};

inline bool operator==(guid const& left, guid const& right) noexcept;
inline bool operator!=(guid const& left, guid const& right) noexcept;
inline bool operator<(guid const& left, guid const& right) noexcept;
```

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17763.0 (Windows 10, version 1809)

**Namespace:** winrt

**Header:** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## See also 
* [winrt namespace](winrt.md)
* [Interop between C++/WinRT and the ABI](/windows/uwp/cpp-and-winrt-apis/interop-winrt-abi)
