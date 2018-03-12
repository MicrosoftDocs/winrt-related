---
author: stevewhims
description: A sequential collection of UTF-16 Unicode characters representing a text string.
title: winrt::hstring struct (C++/WinRT)
dev_langs: ["C++"]
ms.author: stwhi
manager: "markl"
ms.date: 03/01/2018
ms.technology: "cpp-windows"
ms.topic: "language-reference"
ms.prod: windows
ms.technology: uwp
keywords: windows 10, uwp, standard, c++, cpp, winrt, projection, api, reference, string
ms.localizationpriority: medium
ms.workload: ["cplusplus"]
---

# winrt::hstring struct (C++/WinRT)
> [!NOTE]
> **Some information relates to pre-released product which may be substantially modified before it’s commercially released. Microsoft makes no warranties, express or implied, with respect to the information provided here.**

A sequential collection of UTF-16 Unicode characters representing a text string. For more examples and info about **winrt::hstring**, see [String handling in C++/WinRT](/windows/uwp/cpp-and-winrt-apis/strings?branch=live). The **winrt::hstring** type encapsulates [HSTRING](https://msdn.microsoft.com/library/windows/desktop/br205775) behind an interface similar to that of `std::wstring`.

## Syntax
```cppwinrt
struct hstring
```

## Requirements
**Minimum supported SDK:** Windows SDK for Windows 10, version 1803

**Namespace:** winrt

**Header** %ProgramFiles(x86)%\Windows Kits\10\Include\<WindowsTargetPlatformVersion>\cppwinrt\winrt\base.h (included by default)

## Constructors
|Constructor|Description|
|------------|-----------------|
|[hstring::hstring constructor](#hstringhstring-constructor)|Initializes a new instance of the **hstring** struct with a copy of the input string data.|

## Member functions
|Function|Description|
|------------|-----------------|
|[hstring::back function](#hstringback-function)|Returns a reference to the last character in the **hstring** object.|
|[hstring::begin function](#hstringbegin-function)|Returns a const iterator to the first character in the **hstring** object.|
|[hstring::c_str function](#hstringcstr-function)|Returns a null-terminated C-style string version of the characters in the **hstring** object.|
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
|[hstring::operator std::wstring_view](#hstringoperator-stdwstringview)|Converts the **hstring** object to a `std::wstring_view`.|
|[hstring::operator[] &lpar;subscript operator)](#hstringoperator-subscript-operator))|Returns a reference to the character at the specified position within the **hstring** object.|
|[hstring::operator= (assignment operator)](#hstringoperator-assignment-operator)|Assigns a value to the **hstring** object.|

## Free functions
|Function|Description|
|------------|-----------------| 
|[to_hstring function](#tohstring-function)|Conversion function. Returns a new **hstring** object resulting from converting the parameter.| 

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
An **hstring** is a range, and that range is defined by the [hstring::begin](#hstringbegin-function) and [hstring::end](#hstringend-function) member functions, each of which returns a const iterator (as do [hstring::cbegin](#hstringcbegin-function) and [hstring::cend](#hstringcend-function)). Because of this, you can enumerate the characters in an **hstring** object with either a range-based `for` statement, or with the `std::for_each` template function.

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
hstring() noexcept
hstring(hstring const& h)
explicit hstring(std::wstring_view const& v)
hstring(wchar_t const* c)
hstring(wchar_t const* c, uint32_t s)
```

### Parameters
`h`
An **hstring** value that initializes the **hstring** object.

`v`
A `std::wstring_view` value that initializes the **hstring** object.

`c`
A pointer to an array of constant `wchar_t` that initializes the **hstring** object.

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
wchar_t const& back() const noexcept
```

### Return value 
A reference to the last character in the **hstring** object.

## hstring::begin function
Returns a const iterator to the first character in the **hstring** object. See [Iterators](#iterators).

### Syntax
```cppwinrt
wchar_t const* begin() const noexcept
```

### Return value 
A const iterator to the first character in the **hstring** object.

## hstring::c_str function
Returns a null-terminated C-style string version of the characters in the **hstring** object.

### Syntax
```cppwinrt
wchar_t const* c_str() const noexcept
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
	std::wcout << theHstring.c_str() << std::endl;
}
```

## hstring::cbegin function
Returns a const iterator to the first character in the **hstring** object. See [Iterators](#iterators).

### Syntax
```cppwinrt
wchar_t const* cbegin() const noexcept
```

### Return value 
A const iterator to the first character in the **hstring** object.

## hstring::cend function
Returns a const iterator to one beyond the end of (one beyond the last character in) the **hstring** object. See [Iterators](#iterators).

### Syntax
```cppwinrt
wchar_t const* cend() const noexcept
```

### Return value 
A const iterator to one beyond the end of (one beyond the last character in) the **hstring** object.

## hstring::clear function
Makes the **hstring** object empty.

### Syntax
```cppwinrt
void clear() noexcept
```

## hstring::crbegin function
Returns a const reverse iterator to one beyond the end of (one beyond the last character in) the **hstring** object.

### Syntax
```cppwinrt
std::reverse_iterator<wchar_t const*> crbegin() const noexcept
```

### Return value 
A const reverse iterator to one beyond the end of (one beyond the last character in) the **hstring** object.

## hstring::crend function
Returns a const reverse iterator to the first character in the **hstring** object.

### Syntax
```cppwinrt
std::reverse_iterator<wchar_t const*> crend() const noexcept
```

### Return value 
A const reverse iterator to the first character in the **hstring** object.

## hstring::data function
Returns a null-terminated C-style string version of the characters in the **hstring** object.

### Syntax
```cppwinrt
wchar_t const* data() const noexcept
```

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

### Return value 
A null-terminated C-style string version of the characters in the **hstring** object.

## hstring::empty function
Returns a value indicating whether the **hstring** object is empty.

### Syntax
```cppwinrt
bool empty() const noexcept
```

### Return value
`true` if the **hstring** object is empty, otherwise `false`.

## hstring::end function
Returns a const iterator to one beyond the end of (one beyond the last character in) the **hstring** object. See [Iterators](#iterators).

### Syntax
```cppwinrt
wchar_t const* end() const noexcept
```

### Return value
A const iterator to one beyond the end of (one beyond the last character in) the **hstring** object.

## hstring::front function
Returns a reference to the first character in the **hstring** object.

### Syntax
```cppwinrt
wchar_t const& front() const noexcept
```

### Return value
A reference to the first character in the **hstring** object.

## hstring::operator std::wstring_view
Converts the **hstring** object to a `std::wstring_view`.

### Syntax
```cppwinrt
hstring::operator std::wstring_view() const noexcept
```

### Return value
The **hstring** object converted to a `std::wstring_view`.

### Example
```cppwinrt
using namespace winrt;
...
	Uri contosoUri{ L"http://www.contoso.com" };
	Uri awUri{ L"http://www.adventure-works.com" };

	// Uri::Domain() is of type hstring. But we can use hstring's conversion operator to std::wstring_view.
	std::wstring domainWstring{ contosoUri.Domain() }; // L"contoso.com"
	domainWstring = awUri.Domain(); // L"http://www.adventure-works.com"
```

## hstring::operator[] &lpar;subscript operator)
Returns a reference to the character at the specified position within the **hstring** object.

### Syntax
```cppwinrt
wchar_t const& operator[](uint32_t pos) const noexcept
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
hstring& operator=(hstring const& h)
hstring& operator=(std::wstring_view const& v)
```

### Parameters
`h`
An **hstring** value to assign to the **hstring** object.

`v`
A `std::wstring_view` value to assign to the **hstring** object.

### Return value
A reference to the **hstring** object.

## hstring::rbegin function
Returns a const reverse iterator to one beyond the end of (one beyond the last character in) the **hstring** object.

### Syntax
```cppwinrt
std::reverse_iterator<wchar_t const*> rbegin() const noexcept
```

### Return value
A const reverse iterator to one beyond the end of (one beyond the last character in) the **hstring** object.

## hstring::rend function
Returns a const reverse iterator to the first character in the **hstring** object.

### Syntax
```cppwinrt
std::reverse_iterator<wchar_t const*> rend() const noexcept
```

### Return value
A const reverse iterator to the first character in the **hstring** object.

## hstring::size function
Returns the number of characters in the **hstring** object.

### Syntax
```cppwinrt
uint32_t size() const noexcept
```

### Return value
A `uint32_t` containing the number of characters in the **hstring** object.

## operator!= (inequality operator)
Returns a value indicating whether the two parameters are unequal to one another.

### Syntax
```cppwinrt
inline bool operator!=(hstring const& hLeft, hstring const& hRight) noexcept
inline bool operator!=(hstring const& hLeft, std::wstring const& wRight) noexcept
inline bool operator!=(hstring const& hLeft, wchar_t const* cRight) noexcept
inline bool operator!=(std::wstring const& wLeft, hstring const& hRight) noexcept
inline bool operator!=(wchar_t const* cLeft, hstring const& hRight) noexcept
```

### Parameters
`hLeft` `hRight`
An **hstring** value to compare with the other parameter.

`wLeft` `wRight`
A `std::wstring` value to compare with the other parameter.

`cLeft` `cRight`
A pointer to an array of constant `wchar_t` to compare with the other parameter.

### Return value
`true` if the two parameters are unequal to one another, otherwise `false`.

## operator+ (concatenation operator)
Returns a new **hstring** object resulting from concatenating the two parameters together.

### Syntax
```cppwinrt
inline hstring operator+(hstring const& hLeft, hstring const& hRight)
inline hstring operator+(hstring const& hLeft, std::wstring const& wRight)
inline hstring operator+(hstring const& hLeft, std::wstring_view const& vRight)
inline hstring operator+(hstring const& hLeft, wchar_t const* cRight)
inline hstring operator+(hstring const& hLeft, wchar_t scRight)
inline hstring operator+(std::wstring const& wLeft, hstring const& hRight)
inline hstring operator+(std::wstring_view const& vLeft, hstring const& hRight)
inline hstring operator+(wchar_t const* cLeft, hstring const& hRight)
inline hstring operator+(wchar_t scLeft, hstring const& hRight)
```

### Parameters
`hLeft` `hRight`
An **hstring** value to concatenate with the other parameter.

`wLeft` `wRight`
A `std::wstring` value to concatenate with the other parameter.

`vLeft` `vRight`
A `std::wstring_view` value to concatenate with the other parameter.

`cLeft` `cRight`
A pointer to an array of constant `wchar_t` to concatenate with the other parameter.

`scLeft` `scRight`
A `wchar_t` to concatenate with the other parameter.

### Return value
A new **hstring** object resulting from concatenating the two parameters together.

## operator< (less-than operator)
Returns a value indicating whether the first parameter is less than the second parameter.

### Syntax
```cppwinrt
inline bool operator<(hstring const& hLeft, hstring const& hRight) noexcept
inline bool operator<(hstring const& hLeft, std::wstring const& wRight) noexcept
inline bool operator<(hstring const& hLeft, wchar_t const* cRight) noexcept
inline bool operator<(std::wstring const& wLeft, hstring const& hRight) noexcept
inline bool operator<(wchar_t const* cLeft, hstring const& hRight) noexcept
```

### Parameters
`hLeft` `hRight`
An **hstring** value to compare with the other parameter.

`wLeft` `wRight`
A `std::wstring` value to compare with the other parameter.

`cLeft` `cRight`
A pointer to an array of constant `wchar_t` to compare with the other parameter.

### Return value
`true` if the first parameter is less than the second parameter, otherwise `false`.

## operator<= (less-than-or-equal-to operator)
Returns a value indicating whether the first parameter is less than or equal to the second parameter.

### Syntax
```cppwinrt
inline bool operator<=(hstring const& hLeft, hstring const& hRight) noexcept
inline bool operator<=(hstring const& hLeft, std::wstring const& wRight) noexcept
inline bool operator<=(hstring const& hLeft, wchar_t const* cRight) noexcept
inline bool operator<=(std::wstring const& wLeft, hstring const& hRight) noexcept
inline bool operator<=(wchar_t const* cLeft, hstring const& hRight) noexcept
```

### Parameters
`hLeft` `hRight`
An **hstring** value to compare with the other parameter.

`wLeft` `wRight`
A `std::wstring` value to compare with the other parameter.

`cLeft` `cRight`
A pointer to an array of constant `wchar_t` to compare with the other parameter.

### Return value
`true` if the first parameter is less than or equal to the second parameter, otherwise `false`.

## operator== (equality operator)
Returns a value indicating whether the two parameters are equal to one another.

### Syntax
```cppwinrt
inline bool operator==(hstring const& hLeft, hstring const& hRight) noexcept
inline bool operator==(hstring const& hLeft, std::wstring const& wRight) noexcept
inline bool operator==(hstring const& hLeft, wchar_t const* cRight) noexcept
inline bool operator==(std::wstring const& wLeft, hstring const& hRight) noexcept
inline bool operator==(wchar_t const* cLeft, hstring const& hRight) noexcept
```

### Parameters
`hLeft` `hRight`
An **hstring** value to compare with the other parameter.

`wLeft` `wRight`
A `std::wstring` value to compare with the other parameter.

`cLeft` `cRight`
A pointer to an array of constant `wchar_t` to compare with the other parameter.

### Return value
`true` if the two parameters are equal to one another, otherwise `false`.

## operator> (greater-than operator)
Returns a value indicating whether the first parameter is greater than the second parameter.

### Syntax
```cppwinrt
inline bool operator>(hstring const& hLeft, hstring const& hRight) noexcept
inline bool operator>(hstring const& hLeft, std::wstring const& wRight) noexcept
inline bool operator>(hstring const& hLeft, wchar_t const* cRight) noexcept
inline bool operator>(std::wstring const& wLeft, hstring const& hRight) noexcept
inline bool operator>(wchar_t const* cLeft, hstring const& hRight) noexcept
```

### Parameters
`hLeft` `hRight`
An **hstring** value to compare with the other parameter.

`wLeft` `wRight`
A `std::wstring` value to compare with the other parameter.

`cLeft` `cRight`
A pointer to an array of constant `wchar_t` to compare with the other parameter.

### Return value
`true` if the first parameter is greater than the second parameter, otherwise `false`.

## operator>= (greater-than-or-equal-to operator)
Returns a value indicating whether the first parameter is greater than or equal to the second parameter.

### Syntax
```cppwinrt
inline bool operator>=(hstring const& hLeft, hstring const& hRight) noexcept
inline bool operator>=(hstring const& hLeft, std::wstring const& wRight) noexcept
inline bool operator>=(hstring const& hLeft, wchar_t const* cRight) noexcept
inline bool operator>=(std::wstring const& wLeft, hstring const& hRight) noexcept
inline bool operator>=(wchar_t const* cLeft, hstring const& hRight) noexcept
```

### Parameters
`hLeft` `hRight`
An **hstring** value to compare with the other parameter.

`wLeft` `wRight`
A `std::wstring` value to compare with the other parameter.

`cLeft` `cRight`
A pointer to an array of constant `wchar_t` to compare with the other parameter.

### Return value
`true` if the first parameter is greater than or equal to the second parameter, otherwise `false`.

## to_hstring function
Conversion function. Returns a new **hstring** object resulting from converting the parameter.

### Syntax
```cppwinrt
inline hstring to_hstring(bool value)
inline hstring to_hstring(char16_t value)
inline hstring to_hstring(double value)
inline hstring to_hstring(float value)
inline hstring to_hstring(GUID const& value)
inline hstring to_hstring(hstring const& value) noexcept
inline hstring to_hstring(int16_t value)
inline hstring to_hstring(int32_t value)
inline hstring to_hstring(int64_t value)
inline hstring to_hstring(int8_t value)
template <typename T> hstring to_hstring(T const& value)
inline hstring to_hstring(uint16_t value)
inline hstring to_hstring(uint32_t value)
inline hstring to_hstring(uint64_t value)
inline hstring to_hstring(uint8_t value)
```

### Parameters
`value`
The value to convert into a new **hstring** object.

### Return value
A new **hstring** object resulting from converting the parameter.

### Remarks
For the function template, specializations are generated only for types convertible from `std::string_view`.

## See also 
* [winrt namespace (C++/WinRT)](winrt.md)
* [String handling in C++/WinRT](/windows/uwp/cpp-and-winrt-apis/strings?branch=live)