---
description: A sequential collection of UTF-16 Unicode characters representing a text string.
title: winrt::hstring struct (C++/WinRT)
dev_langs: ["C++"]
ms.date: 08/31/2020
ms.topic: "language-reference"
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, string
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::hstring struct (C++/WinRT)

A sequential collection of UTF-16 Unicode characters representing a text string. For more examples and info about **winrt::hstring**, see [String handling in C++/WinRT](/windows/uwp/cpp-and-winrt-apis/strings). The **winrt::hstring** type encapsulates [HSTRING](/windows/win32/winrt/hstring) behind an interface similar to that of **std::wstring**. A **HSTRING** is a handle to a Windows Runtime string.

## Syntax
```cppwinrt
struct hstring
```

## Requirements
**Minimum supported SDK:** Windows SDK version 10.0.17134.0 (Windows 10, version 1803)

**Namespace:** winrt

**Header:** %WindowsSdkDir%Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## Member type aliases
|Alias name|Type|
|------------|-----------------|
|hstring::value_type|A synonym for **wchar_t**.|
|hstring::size_type|A synonym for **uint32_t**.|
|hstring::const_reference|A synonym for **hstring::value_type const&**.|
|hstring::const_pointer|A synonym for **hstring::value_type const\***.|
|hstring::const_iterator|A synonym for **hstring::const_pointer**.|
|hstring::const_reverse_iterator|A synonym for **std::reverse_iterator\<hstring::const_iterator\>**.|

## Constructors
|Constructor|Description|
|------------|-----------------|
|[hstring::hstring constructor](#hstringhstring-constructor)|Initializes a new instance of the **hstring** struct with a copy of the input string data.|

## Member functions
|Function|Description|
|------------|-----------------|
|[hstring::back function](#hstringback-function)|Returns a reference to the last character in the **hstring** object.|
|[hstring::begin function](#hstringbegin-function)|Returns a const iterator to the first character in the **hstring** object.|
|[hstring::c_str function](#hstringc_str-function)|Returns a pointer to the underlying null-terminated C-style string of the characters in the **hstring** object; no copy is made.|
|[hstring::cbegin function](#hstringcbegin-function)|Returns a const iterator to the first character in the **hstring** object.|
|[hstring::cend function](#hstringcend-function)|Returns a const iterator to one beyond the end of (one beyond the last character in) the **hstring** object.|
|[hstring::clear function](#hstringclear-function)|Makes the **hstring** object empty.|
|[hstring::crbegin function](#hstringcrbegin-function)|Returns a const reverse iterator to one beyond the end of (one beyond the last character in) the **hstring** object.|
|[hstring::crend function](#hstringcrend-function)|Returns a const reverse iterator to the first character in the **hstring** object.|
|[hstring::data function](#hstringdata-function)|Returns a null-terminated C-style string version of the characters in the **hstring** object.|
|[hstring::empty function](#hstringempty-function)|Returns a value indicating whether the **hstring** object is empty.|
|[hstring::end function](#hstringend-function)|Returns a const iterator to one beyond the end of (one beyond the last character in) the **hstring** object.|
|[hstring::front function](#hstringfront-function)|Returns a reference to the first character in the **hstring** object.|
|[hstring::rbegin function](#hstringrbegin-function)|Returns a const reverse iterator to one beyond the end of (one beyond the last character in) the **hstring** object.|
|[hstring::rend function](#hstringrend-function)|Returns a const reverse iterator to the first character in the **hstring** object.|
|[hstring::size function](#hstringsize-function)|Returns the number of characters in the **hstring** object.|

## Member operators
|Operator|Description|
|------------|-----------------|
|[hstring::operator std::wstring_view](#hstringoperator-stdwstring_view)|Converts the **hstring** object to a **std::wstring_view**.|
|[hstring::operator[] &lpar;subscript operator)](#hstringoperator-subscript-operator))|Returns a reference to the character at the specified position within the **hstring** object.|
|[hstring::operator= (assignment operator)](#hstringoperator-assignment-operator)|Assigns a value to the **hstring** object.|

## Free functions
|Function|Description|
|------------|-----------------|
|[attach_abi function](#attach_abi-function)|Attaches a **hstring** object to a handle to a Windows Runtime string.|
|[copy_from_abi function](#copy_from_abi-function)|Copies to a **hstring** object from a handle to a Windows Runtime string. Clears the **hstring**, copies the parameter, and begins managing the handle.|
|[copy_to_abi function](#copy_to_abi-function)|Copies to a handle to a Windows Runtime string from a **hstring** object.|
|[detach_abi function](#detach_abi-function)|Detaches a **hstring** object from its handle, perhaps to return it to a caller.|
|[to_hstring function](to-hstring.md)|Converts an input value to a **winrt::hstring** containing the value's string representation.| 

## Free operators
|Operator|Description|
|------------|-----------------|
|[operator!= (inequality operator)](#operator-inequality-operator)|Returns a value indicating whether the two parameters are unequal to one another.|
|[operator+ (concatenation operator)](#operator-concatenation-operator)|Returns a new **hstring** object resulting from concatenating the two parameters together.|
|[operator< (less-than operator)](#operator-less-than-operator)|Returns a value indicating whether the first parameter is less than the second parameter.|
|[operator<= (less-than-or-equal-to operator)](#operator-less-than-or-equal-to-operator)|Returns a value indicating whether the first parameter is less than or equal to the second parameter.|
|[operator== (equality operator)](#operator-equality-operator)|Returns a value indicating whether the two parameters are equal to one another.|
|[operator> (greater-than operator)](#operator-greater-than-operator)|Returns a value indicating whether the first parameter is greater than the second parameter.|
|[operator>= (greater-than-or-equal-to operator)](#operator-greater-than-or-equal-to-operator)|Returns a value indicating whether the first parameter is greater than or equal to the second parameter.|

## Iterators
An **hstring** is a range, and that range is defined by the [hstring::begin](#hstringbegin-function) and [hstring::end](#hstringend-function) member functions, each of which returns a const iterator (as do [hstring::cbegin](#hstringcbegin-function) and [hstring::cend](#hstringcend-function)). Because of this, you can enumerate the characters in an **hstring** object with either a range-based `for` statement, or with the **std::for_each** template function.

```cppwinrt
#include <iostream>
using namespace winrt;
...
void Iterators(hstring const& theHstring)
{
    for (auto const& element : theHstring)
    {
        std::wcout << element;
    }

    std::for_each(theHstring.cbegin(), theHstring.cend(), [](T const& element) { std::wcout << element; });
}
```

## hstring::hstring constructor
Initializes a new instance of the **hstring** struct with a copy of the input string data.

### Syntax
```cppwinrt
hstring() noexcept;
hstring(winrt::hstring const& h);
explicit hstring(std::wstring_view const& v);
hstring(std::wchar_t const* c);
hstring(std::wchar_t const* c, uint32_t s);
```

### Parameters
`h`
An **hstring** value that initializes the **hstring** object.

`v`
A **std::wstring_view** value that initializes the **hstring** object.

`c`
A pointer to an array of constant **wchar_t** that initializes the **hstring** object.

`s`
A number that specifies a fixed size for the **hstring** object.

### Example
```cppwinrt
using namespace winrt;
...
void Constructors(
    hstring const& theHstring,
    std::wstring_view const& theWstringView,
    wchar_t const* wideLiteral,
    std::wstring const& wideString)
{
    // hstring() noexcept
    hstring fromDefault{};

    // hstring(hstring const& h)
    hstring fromHstring{ theHstring };

    // explicit hstring(std::wstring_view const& value)
    hstring fromWstringView{ theWstringView };

    // hstring(wchar_t const* value)
    hstring fromWideLiteral{ wideLiteral };
    hstring fromWideString{ wideString.c_str() };

    // hstring(wchar_t const* value, uint32_t size)
    hstring fromWideLiteralWithSize{ wideLiteral, 256 };
    hstring fromWideStringWithSize{ wideString.c_str(), 256 };
}
```

## hstring::back function
Returns a reference to the last character in the **hstring** object.

### Syntax
```cppwinrt
std::wchar_t const& back() const noexcept;
```

### Return value 
A reference to the last character in the **hstring** object.

## hstring::begin function
Returns a const iterator to the first character in the **hstring** object. See [Iterators](#iterators).

### Syntax
```cppwinrt
std::wchar_t const* begin() const noexcept;
```

### Return value
A const iterator to the first character in the **hstring** object.

## hstring::c_str function
Returns a pointer to the underlying null-terminated C-style string of the characters in the **hstring** object; no copy is made.

### Syntax
```cppwinrt
std::wchar_t const* c_str() const noexcept;
```

### Return value
A pointer to the underlying null-terminated C-style string of the characters in the **hstring** object; no copy is made.

### Example
```cppwinrt
#include <iostream>
using namespace winrt;
...
void PrintHstring(hstring const& theHstring)
{
    // You can get a standard wide string from an hstring.
    std::wcout << theHstring.c_str() << std::endl;
}
```

## hstring::cbegin function
Returns a const iterator to the first character in the **hstring** object. See [Iterators](#iterators).

### Syntax
```cppwinrt
std::wchar_t const* cbegin() const noexcept;
```

### Return value 
A const iterator to the first character in the **hstring** object.

## hstring::cend function
Returns a const iterator to one beyond the end of (one beyond the last character in) the **hstring** object. See [Iterators](#iterators).

### Syntax
```cppwinrt
std::wchar_t const* cend() const noexcept;
```

### Return value 
A const iterator to one beyond the end of (one beyond the last character in) the **hstring** object.

## hstring::clear function
Makes the **hstring** object empty.

### Syntax
```cppwinrt
void clear() noexcept;
```

## hstring::crbegin function
Returns a const reverse iterator to one beyond the end of (one beyond the last character in) the **hstring** object.

### Syntax
```cppwinrt
std::reverse_iterator<std::wchar_t const*> crbegin() const noexcept;
```

### Return value 
A const reverse iterator to one beyond the end of (one beyond the last character in) the **hstring** object.

## hstring::crend function
Returns a const reverse iterator to the first character in the **hstring** object.

### Syntax
```cppwinrt
std::reverse_iterator<std::wchar_t const*> crend() const noexcept;
```

### Return value 
A const reverse iterator to the first character in the **hstring** object.

## hstring::data function
Returns a null-terminated C-style string version of the characters in the **hstring** object.

### Syntax
```cppwinrt
std::wchar_t const* data() const noexcept;
```

### Return value 
A null-terminated C-style string version of the characters in the **hstring** object.

### Example
```cppwinrt
#include <iostream>
using namespace winrt;
...
void PrintHstring(hstring const& theHstring)
{
    // You can get a standard wide string from an hstring.
    std::wcout << theHstring.data() << std::endl;
}
```

## hstring::empty function
Returns a value indicating whether the **hstring** object is empty.

### Syntax
```cppwinrt
bool empty() const noexcept;
```

### Return value
`true` if the **hstring** object is empty, otherwise `false`.

## hstring::end function
Returns a const iterator to one beyond the end of (one beyond the last character in) the **hstring** object. See [Iterators](#iterators).

### Syntax
```cppwinrt
std::wchar_t const* end() const noexcept;
```

### Return value
A const iterator to one beyond the end of (one beyond the last character in) the **hstring** object.

## hstring::front function
Returns a reference to the first character in the **hstring** object.

### Syntax
```cppwinrt
std::wchar_t const& front() const noexcept;
```

### Return value
A reference to the first character in the **hstring** object.

## hstring::operator std::wstring_view
Converts the **hstring** object to a **std::wstring_view**.

### Syntax
```cppwinrt
operator std::wstring_view() const noexcept;
```

### Return value
The **hstring** object converted to a **std::wstring_view**.

### Example
```cppwinrt
using namespace winrt;
...
    Uri contosoUri{ L"https://www.contoso.com" };
    Uri awUri{ L"https://www.adventure-works.com" };

    // Uri::Domain() is of type hstring. But we can use hstring's conversion operator to std::wstring_view.
    std::wstring domainWstring{ contosoUri.Domain() }; // L"contoso.com"
    domainWstring = awUri.Domain(); // L"https://www.adventure-works.com"
```

## hstring::operator[] &lpar;subscript operator)
Returns a reference to the character at the specified position within the **hstring** object.

### Syntax
```cppwinrt
std::wchar_t const& operator[](uint32_t pos) const noexcept;
```

### Parameters
`pos`
A zero-based character position, or index.

### Return value
A reference to the character at the specified position within the **hstring** object.

## hstring::operator= (assignment operator)
Assigns a value to the **hstring** object.

### Syntax
```cppwinrt
winrt::hstring& operator=(winrt::hstring const& h);
winrt::hstring& operator=(std::wstring_view const& v);
```

### Parameters
`h`
An **hstring** value to assign to the **hstring** object.

`v`
A **std::wstring_view** value to assign to the **hstring** object.

### Return value
A reference to the **hstring** object.

## hstring::rbegin function
Returns a const reverse iterator to one beyond the end of (one beyond the last character in) the **hstring** object.

### Syntax
```cppwinrt
std::reverse_iterator<std::wchar_t const*> rbegin() const noexcept;
```

### Return value
A const reverse iterator to one beyond the end of (one beyond the last character in) the **hstring** object.

## hstring::rend function
Returns a const reverse iterator to the first character in the **hstring** object.

### Syntax
```cppwinrt
std::reverse_iterator<std::wchar_t const*> rend() const noexcept;
```

### Return value
A const reverse iterator to the first character in the **hstring** object.

## hstring::size function
Returns the number of characters in the **hstring** object.

### Syntax
```cppwinrt
uint32_t size() const noexcept;
```

### Return value
A **uint32_t** containing the number of characters in the **hstring** object.

## attach_abi function
Attaches a **hstring** object to a handle to a Windows Runtime string.

### Syntax
```cppwinrt
void attach_abi(winrt::hstring& object, HSTRING value) noexcept;
```

### Parameters
`object`
A **hstring** object to operate on.

`value`
A handle to a Windows Runtime string.

## copy_from_abi function
Copies to a **hstring** object from a handle to a Windows Runtime string. Clears the **hstring**, copies the parameter, and begins managing the handle.

### Syntax
```cppwinrt
void copy_from_abi(winrt::hstring& object, HSTRING value);
```

### Parameters
`object`
A **hstring** object to operate on.

`value`
A handle to a Windows Runtime string.

## copy_to_abi function
Copies to a handle to a Windows Runtime string from a **hstring** object.

### Syntax
```cppwinrt
void copy_to_abi(winrt::hstring const& object, HSTRING& value);
```

### Parameters
`object`
A **hstring** object to operate on.

`value`
A handle reference, via which to copy the **hstring**'s handle.

## detach_abi function
Detaches a **hstring** object from its handle, perhaps to return it to a caller.

### Syntax
```cppwinrt
HSTRING detach_abi(winrt::hstring& object) noexcept;
HSTRING detach_abi(winrt::hstring&& object) noexcept;
```

### Parameters
`object`
A **hstring** object to operate on.

### Return value
The handle to the Windows Runtime string.

## operator!= (inequality operator)
Returns a value indicating whether the two parameters are unequal to one another.

### Syntax
```cppwinrt
inline bool operator!=(winrt::hstring const& hLeft, winrt::hstring const& hRight) noexcept;
inline bool operator!=(winrt::hstring const& hLeft, std::wstring const& wRight) noexcept;
inline bool operator!=(winrt::hstring const& hLeft, std::wchar_t const* cRight) noexcept;
inline bool operator!=(std::wstring const& wLeft, winrt::hstring const& hRight) noexcept;
inline bool operator!=(std::wchar_t const* cLeft, winrt::hstring const& hRight) noexcept;
```

### Parameters
`hLeft` `hRight`
An **hstring** value to compare with the other parameter.

`wLeft` `wRight`
A `std::wstring` value to compare with the other parameter.

`cLeft` `cRight`
A pointer to an array of constant **wchar_t** to compare with the other parameter.

### Return value
`true` if the two parameters are unequal to one another, otherwise `false`.

## operator+ (concatenation operator)
Returns a new **hstring** object resulting from concatenating the two parameters together.

### Syntax
```cppwinrt
inline hstring operator+(winrt::hstring const& hLeft, winrt::hstring const& hRight);
inline hstring operator+(winrt::hstring const& hLeft, std::wstring const& wRight);
inline hstring operator+(winrt::hstring const& hLeft, std::wstring_view const& vRight);
inline hstring operator+(winrt::hstring const& hLeft, std::wchar_t const* cRight);
inline hstring operator+(winrt::hstring const& hLeft, std::wchar_t scRight);
inline hstring operator+(std::wstring const& wLeft, winrt::hstring const& hRight);
inline hstring operator+(std::wstring_view const& vLeft, winrt::hstring const& hRight);
inline hstring operator+(std::wchar_t const* cLeft, winrt::hstring const& hRight);
inline hstring operator+(std::wchar_t scLeft, winrt::hstring const& hRight);
```

### Parameters
`hLeft` `hRight`
An **hstring** value to concatenate with the other parameter.

`wLeft` `wRight`
A `std::wstring` value to concatenate with the other parameter.

`vLeft` `vRight`
A **std::wstring_view** value to concatenate with the other parameter.

`cLeft` `cRight`
A pointer to an array of constant **wchar_t** to concatenate with the other parameter.

`scLeft` `scRight`
A **wchar_t** to concatenate with the other parameter.

### Return value
A new **hstring** object resulting from concatenating the two parameters together.

## operator< (less-than operator)
Returns a value indicating whether the first parameter is less than the second parameter.

### Syntax
```cppwinrt
inline bool operator<(winrt::hstring const& hLeft, winrt::hstring const& hRight) noexcept;
inline bool operator<(winrt::hstring const& hLeft, std::wstring const& wRight) noexcept;
inline bool operator<(winrt::hstring const& hLeft, std::wchar_t const* cRight) noexcept;
inline bool operator<(std::wstring const& wLeft, winrt::hstring const& hRight) noexcept;
inline bool operator<(std::wchar_t const* cLeft, winrt::hstring const& hRight) noexcept;
```

### Parameters
`hLeft` `hRight`
An **hstring** value to compare with the other parameter.

`wLeft` `wRight`
A `std::wstring` value to compare with the other parameter.

`cLeft` `cRight`
A pointer to an array of constant **wchar_t** to compare with the other parameter.

### Return value
`true` if the first parameter is less than the second parameter, otherwise `false`.

## operator<= (less-than-or-equal-to operator)
Returns a value indicating whether the first parameter is less than or equal to the second parameter.

### Syntax
```cppwinrt
inline bool operator<=(winrt::hstring const& hLeft, winrt::hstring const& hRight) noexcept;
inline bool operator<=(winrt::hstring const& hLeft, std::wstring const& wRight) noexcept;
inline bool operator<=(winrt::hstring const& hLeft, std::wchar_t const* cRight) noexcept;
inline bool operator<=(std::wstring const& wLeft, winrt::hstring const& hRight) noexcept;
inline bool operator<=(std::wchar_t const* cLeft, winrt::hstring const& hRight) noexcept;
```

### Parameters
`hLeft` `hRight`
An **hstring** value to compare with the other parameter.

`wLeft` `wRight`
A `std::wstring` value to compare with the other parameter.

`cLeft` `cRight`
A pointer to an array of constant **wchar_t** to compare with the other parameter.

### Return value
`true` if the first parameter is less than or equal to the second parameter, otherwise `false`.

## operator== (equality operator)
Returns a value indicating whether the two parameters are equal to one another.

### Syntax
```cppwinrt
inline bool operator==(winrt::hstring const& hLeft, winrt::hstring const& hRight) noexcept;
inline bool operator==(winrt::hstring const& hLeft, std::wstring const& wRight) noexcept;
inline bool operator==(winrt::hstring const& hLeft, std::wchar_t const* cRight) noexcept;
inline bool operator==(std::wstring const& wLeft, winrt::hstring const& hRight) noexcept;
inline bool operator==(std::wchar_t const* cLeft, winrt::hstring const& hRight) noexcept;
```

### Parameters
`hLeft` `hRight`
An **hstring** value to compare with the other parameter.

`wLeft` `wRight`
A `std::wstring` value to compare with the other parameter.

`cLeft` `cRight`
A pointer to an array of constant **wchar_t** to compare with the other parameter.

### Return value
`true` if the two parameters are equal to one another, otherwise `false`.

## operator> (greater-than operator)
Returns a value indicating whether the first parameter is greater than the second parameter.

### Syntax
```cppwinrt
inline bool operator>(winrt::hstring const& hLeft, winrt::hstring const& hRight) noexcept;
inline bool operator>(winrt::hstring const& hLeft, std::wstring const& wRight) noexcept;
inline bool operator>(winrt::hstring const& hLeft, std::wchar_t const* cRight) noexcept;
inline bool operator>(std::wstring const& wLeft, winrt::hstring const& hRight) noexcept;
inline bool operator>(std::wchar_t const* cLeft, winrt::hstring const& hRight) noexcept;
```

### Parameters
`hLeft` `hRight`
An **hstring** value to compare with the other parameter.

`wLeft` `wRight`
A `std::wstring` value to compare with the other parameter.

`cLeft` `cRight`
A pointer to an array of constant **wchar_t** to compare with the other parameter.

### Return value
`true` if the first parameter is greater than the second parameter, otherwise `false`.

## operator>= (greater-than-or-equal-to operator)
Returns a value indicating whether the first parameter is greater than or equal to the second parameter.

### Syntax
```cppwinrt
inline bool operator>=(winrt::hstring const& hLeft, winrt::hstring const& hRight) noexcept;
inline bool operator>=(winrt::hstring const& hLeft, std::wstring const& wRight) noexcept;
inline bool operator>=(winrt::hstring const& hLeft, std::wchar_t const* cRight) noexcept;
inline bool operator>=(std::wstring const& wLeft, winrt::hstring const& hRight) noexcept;
inline bool operator>=(std::wchar_t const* cLeft, winrt::hstring const& hRight) noexcept;
```

### Parameters
`hLeft` `hRight`
An **hstring** value to compare with the other parameter.

`wLeft` `wRight`
A `std::wstring` value to compare with the other parameter.

`cLeft` `cRight`
A pointer to an array of constant **wchar_t** to compare with the other parameter.

### Return value
`true` if the first parameter is greater than or equal to the second parameter, otherwise `false`.

## See also 
* [winrt namespace](winrt.md)
* [String handling in C++/WinRT](/windows/uwp/cpp-and-winrt-apis/strings)
