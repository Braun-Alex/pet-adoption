//
// Shelter.h
//
// This file has been generated from pet_adoption.xml. Do not edit.
//


#ifndef DatabaseSystem_Shelter_INCLUDED
#define DatabaseSystem_Shelter_INCLUDED


#include "Poco/ActiveRecord/ActiveRecord.h"


namespace DatabaseSystem {


class Shelter: public Poco::ActiveRecord::ActiveRecord<std::string>
{
public:
	using Ptr = Poco::AutoPtr<Shelter>;

	explicit Shelter(ID id);
	Shelter() = default;
	Shelter(const Shelter& other);
	~Shelter() = default;

	const std::string& email() const;
	Shelter& email(const std::string& value);

	const std::string& hashedPassword() const;
	Shelter& hashedPassword(const std::string& value);

	const std::string& salt() const;
	Shelter& salt(const std::string& value);

	const std::string& encryptedPrivateKey() const;
	Shelter& encryptedPrivateKey(const std::string& value);

	const std::string& phone() const;
	Shelter& phone(const std::string& value);

	const std::string& location() const;
	Shelter& location(const std::string& value);

	const std::string& headFirstName() const;
	Shelter& headFirstName(const std::string& value);

	const std::string& headLastName() const;
	Shelter& headLastName(const std::string& value);

	bool verifiedEmail() const;
	Shelter& verifiedEmail(bool value);

	bool verifiedPhoneNumber() const;
	Shelter& verifiedPhoneNumber(bool value);

	const Poco::DateTime& registration() const;
	Shelter& registration(const Poco::DateTime& value);

	static Ptr find(Poco::ActiveRecord::Context::Ptr pContext, const ID& id);

	void insert();
	void update();
	void remove();

	static const std::vector<std::string>& columns();
	static const std::string& table();

private:
	std::string _email;
	std::string _hashedPassword;
	std::string _salt;
	std::string _encryptedPrivateKey;
	std::string _phone;
	std::string _location;
	std::string _headFirstName;
	std::string _headLastName;
	bool _verifiedEmail = false;
	bool _verifiedPhoneNumber = false;
	Poco::DateTime _registration;

	friend class Poco::Data::TypeHandler<Shelter>;
};


inline const std::string& Shelter::email() const
{
	return _email;
}


inline Shelter& Shelter::email(const std::string& value)
{
	_email = value;
	return *this;
}


inline const std::string& Shelter::hashedPassword() const
{
	return _hashedPassword;
}


inline Shelter& Shelter::hashedPassword(const std::string& value)
{
	_hashedPassword = value;
	return *this;
}


inline const std::string& Shelter::salt() const
{
	return _salt;
}


inline Shelter& Shelter::salt(const std::string& value)
{
	_salt = value;
	return *this;
}


inline const std::string& Shelter::encryptedPrivateKey() const
{
	return _encryptedPrivateKey;
}


inline Shelter& Shelter::encryptedPrivateKey(const std::string& value)
{
	_encryptedPrivateKey = value;
	return *this;
}


inline const std::string& Shelter::phone() const
{
	return _phone;
}


inline Shelter& Shelter::phone(const std::string& value)
{
	_phone = value;
	return *this;
}


inline const std::string& Shelter::location() const
{
	return _location;
}


inline Shelter& Shelter::location(const std::string& value)
{
	_location = value;
	return *this;
}


inline const std::string& Shelter::headFirstName() const
{
	return _headFirstName;
}


inline Shelter& Shelter::headFirstName(const std::string& value)
{
	_headFirstName = value;
	return *this;
}


inline const std::string& Shelter::headLastName() const
{
	return _headLastName;
}


inline Shelter& Shelter::headLastName(const std::string& value)
{
	_headLastName = value;
	return *this;
}


inline bool Shelter::verifiedEmail() const
{
	return _verifiedEmail;
}


inline Shelter& Shelter::verifiedEmail(bool value)
{
	_verifiedEmail = value;
	return *this;
}


inline bool Shelter::verifiedPhoneNumber() const
{
	return _verifiedPhoneNumber;
}


inline Shelter& Shelter::verifiedPhoneNumber(bool value)
{
	_verifiedPhoneNumber = value;
	return *this;
}


inline const Poco::DateTime& Shelter::registration() const
{
	return _registration;
}


inline Shelter& Shelter::registration(const Poco::DateTime& value)
{
	_registration = value;
	return *this;
}


} // namespace DatabaseSystem


namespace Poco {
namespace Data {


template <>
class TypeHandler<DatabaseSystem::Shelter>
{
public:
	static std::size_t size()
	{
		return 11;
	}

	static void bind(std::size_t pos, const DatabaseSystem::Shelter& ar, AbstractBinder::Ptr pBinder, AbstractBinder::Direction dir)
	{
		TypeHandler<std::string>::bind(pos++, ar._email, pBinder, dir);
		TypeHandler<std::string>::bind(pos++, ar._hashedPassword, pBinder, dir);
		TypeHandler<std::string>::bind(pos++, ar._salt, pBinder, dir);
		TypeHandler<std::string>::bind(pos++, ar._encryptedPrivateKey, pBinder, dir);
		TypeHandler<std::string>::bind(pos++, ar._phone, pBinder, dir);
		TypeHandler<std::string>::bind(pos++, ar._location, pBinder, dir);
		TypeHandler<std::string>::bind(pos++, ar._headFirstName, pBinder, dir);
		TypeHandler<std::string>::bind(pos++, ar._headLastName, pBinder, dir);
		TypeHandler<bool>::bind(pos++, ar._verifiedEmail, pBinder, dir);
		TypeHandler<bool>::bind(pos++, ar._verifiedPhoneNumber, pBinder, dir);
		TypeHandler<Poco::DateTime>::bind(pos++, ar._registration, pBinder, dir);
}

	static void extract(std::size_t pos, DatabaseSystem::Shelter& ar, const DatabaseSystem::Shelter& deflt, AbstractExtractor::Ptr pExtr)
	{
		TypeHandler<std::string>::extract(pos++, ar._email, deflt._email, pExtr);
		TypeHandler<std::string>::extract(pos++, ar._hashedPassword, deflt._hashedPassword, pExtr);
		TypeHandler<std::string>::extract(pos++, ar._salt, deflt._salt, pExtr);
		TypeHandler<std::string>::extract(pos++, ar._encryptedPrivateKey, deflt._encryptedPrivateKey, pExtr);
		TypeHandler<std::string>::extract(pos++, ar._phone, deflt._phone, pExtr);
		TypeHandler<std::string>::extract(pos++, ar._location, deflt._location, pExtr);
		TypeHandler<std::string>::extract(pos++, ar._headFirstName, deflt._headFirstName, pExtr);
		TypeHandler<std::string>::extract(pos++, ar._headLastName, deflt._headLastName, pExtr);
		TypeHandler<bool>::extract(pos++, ar._verifiedEmail, deflt._verifiedEmail, pExtr);
		TypeHandler<bool>::extract(pos++, ar._verifiedPhoneNumber, deflt._verifiedPhoneNumber, pExtr);
		TypeHandler<Poco::DateTime>::extract(pos++, ar._registration, deflt._registration, pExtr);
}

	static void prepare(std::size_t pos, const DatabaseSystem::Shelter& ar, AbstractPreparator::Ptr pPrep)
	{
		TypeHandler<std::string>::prepare(pos++, ar._email, pPrep);
		TypeHandler<std::string>::prepare(pos++, ar._hashedPassword, pPrep);
		TypeHandler<std::string>::prepare(pos++, ar._salt, pPrep);
		TypeHandler<std::string>::prepare(pos++, ar._encryptedPrivateKey, pPrep);
		TypeHandler<std::string>::prepare(pos++, ar._phone, pPrep);
		TypeHandler<std::string>::prepare(pos++, ar._location, pPrep);
		TypeHandler<std::string>::prepare(pos++, ar._headFirstName, pPrep);
		TypeHandler<std::string>::prepare(pos++, ar._headLastName, pPrep);
		TypeHandler<bool>::prepare(pos++, ar._verifiedEmail, pPrep);
		TypeHandler<bool>::prepare(pos++, ar._verifiedPhoneNumber, pPrep);
		TypeHandler<Poco::DateTime>::prepare(pos++, ar._registration, pPrep);
	}
};


} } // namespace Poco::Data


#endif // DatabaseSystem_Shelter_INCLUDED
