//
// User.h
//
// This file has been generated from pet_adoption.xml. Do not edit.
//


#ifndef DatabaseSystem_User_INCLUDED
#define DatabaseSystem_User_INCLUDED


#include "Poco/ActiveRecord/ActiveRecord.h"


namespace DatabaseSystem {


class User: public Poco::ActiveRecord::ActiveRecord<std::string>
{
public:
	using Ptr = Poco::AutoPtr<User>;

	explicit User(ID id);
	User() = default;
	User(const User& other);
	~User() = default;

	const std::string& hashedPassword() const;
	User& hashedPassword(const std::string& value);

	const std::string& salt() const;
	User& salt(const std::string& value);

	const std::string& encryptedFirstName() const;
	User& encryptedFirstName(const std::string& value);

	const std::string& encryptedLastName() const;
	User& encryptedLastName(const std::string& value);

	const std::string& encryptedPrivateKey() const;
	User& encryptedPrivateKey(const std::string& value);

	const std::string& encryptedPhone() const;
	User& encryptedPhone(const std::string& value);

	const std::string& encryptedLocation() const;
	User& encryptedLocation(const std::string& value);

	bool verifiedEmail() const;
	User& verifiedEmail(bool value);

	bool verifiedPhoneNumber() const;
	User& verifiedPhoneNumber(bool value);

	bool twoFactorAuthentication() const;
	User& twoFactorAuthentication(bool value);

	const Poco::Timestamp& registration() const;
	User& registration(const Poco::Timestamp& value);

	static Ptr find(Poco::ActiveRecord::Context::Ptr pContext, const ID& id);

	void insert();
	void update();
	void remove();

	static const std::vector<std::string>& columns();
	static const std::string& table();

private:
	std::string _hashedPassword;
	std::string _salt;
	std::string _encryptedFirstName;
	std::string _encryptedLastName;
	std::string _encryptedPrivateKey;
	std::string _encryptedPhone;
	std::string _encryptedLocation;
	bool _verifiedEmail = false;
	bool _verifiedPhoneNumber = false;
	bool _twoFactorAuthentication = false;
	Poco::Timestamp _registration;

	friend class Poco::Data::TypeHandler<User>;
};


inline const std::string& User::hashedPassword() const
{
	return _hashedPassword;
}


inline User& User::hashedPassword(const std::string& value)
{
	_hashedPassword = value;
	return *this;
}


inline const std::string& User::salt() const
{
	return _salt;
}


inline User& User::salt(const std::string& value)
{
	_salt = value;
	return *this;
}


inline const std::string& User::encryptedFirstName() const
{
	return _encryptedFirstName;
}


inline User& User::encryptedFirstName(const std::string& value)
{
	_encryptedFirstName = value;
	return *this;
}


inline const std::string& User::encryptedLastName() const
{
	return _encryptedLastName;
}


inline User& User::encryptedLastName(const std::string& value)
{
	_encryptedLastName = value;
	return *this;
}


inline const std::string& User::encryptedPrivateKey() const
{
	return _encryptedPrivateKey;
}


inline User& User::encryptedPrivateKey(const std::string& value)
{
	_encryptedPrivateKey = value;
	return *this;
}


inline const std::string& User::encryptedPhone() const
{
	return _encryptedPhone;
}


inline User& User::encryptedPhone(const std::string& value)
{
	_encryptedPhone = value;
	return *this;
}


inline const std::string& User::encryptedLocation() const
{
	return _encryptedLocation;
}


inline User& User::encryptedLocation(const std::string& value)
{
	_encryptedLocation = value;
	return *this;
}


inline bool User::verifiedEmail() const
{
	return _verifiedEmail;
}


inline User& User::verifiedEmail(bool value)
{
	_verifiedEmail = value;
	return *this;
}


inline bool User::verifiedPhoneNumber() const
{
	return _verifiedPhoneNumber;
}


inline User& User::verifiedPhoneNumber(bool value)
{
	_verifiedPhoneNumber = value;
	return *this;
}


inline bool User::twoFactorAuthentication() const
{
	return _twoFactorAuthentication;
}


inline User& User::twoFactorAuthentication(bool value)
{
	_twoFactorAuthentication = value;
	return *this;
}


inline const Poco::Timestamp& User::registration() const
{
	return _registration;
}


inline User& User::registration(const Poco::Timestamp& value)
{
	_registration = value;
	return *this;
}


} // namespace DatabaseSystem


namespace Poco {
namespace Data {


template <>
class TypeHandler<DatabaseSystem::User>
{
public:
	static std::size_t size()
	{
		return 11;
	}

	static void bind(std::size_t pos, const DatabaseSystem::User& ar, AbstractBinder::Ptr pBinder, AbstractBinder::Direction dir)
	{
		TypeHandler<std::string>::bind(pos++, ar._hashedPassword, pBinder, dir);
		TypeHandler<std::string>::bind(pos++, ar._salt, pBinder, dir);
		TypeHandler<std::string>::bind(pos++, ar._encryptedFirstName, pBinder, dir);
		TypeHandler<std::string>::bind(pos++, ar._encryptedLastName, pBinder, dir);
		TypeHandler<std::string>::bind(pos++, ar._encryptedPrivateKey, pBinder, dir);
		TypeHandler<std::string>::bind(pos++, ar._encryptedPhone, pBinder, dir);
		TypeHandler<std::string>::bind(pos++, ar._encryptedLocation, pBinder, dir);
		TypeHandler<bool>::bind(pos++, ar._verifiedEmail, pBinder, dir);
		TypeHandler<bool>::bind(pos++, ar._verifiedPhoneNumber, pBinder, dir);
		TypeHandler<bool>::bind(pos++, ar._twoFactorAuthentication, pBinder, dir);
		TypeHandler<Poco::Timestamp>::bind(pos++, ar._registration, pBinder, dir);
}

	static void extract(std::size_t pos, DatabaseSystem::User& ar, const DatabaseSystem::User& deflt, AbstractExtractor::Ptr pExtr)
	{
		TypeHandler<std::string>::extract(pos++, ar._hashedPassword, deflt._hashedPassword, pExtr);
		TypeHandler<std::string>::extract(pos++, ar._salt, deflt._salt, pExtr);
		TypeHandler<std::string>::extract(pos++, ar._encryptedFirstName, deflt._encryptedFirstName, pExtr);
		TypeHandler<std::string>::extract(pos++, ar._encryptedLastName, deflt._encryptedLastName, pExtr);
		TypeHandler<std::string>::extract(pos++, ar._encryptedPrivateKey, deflt._encryptedPrivateKey, pExtr);
		TypeHandler<std::string>::extract(pos++, ar._encryptedPhone, deflt._encryptedPhone, pExtr);
		TypeHandler<std::string>::extract(pos++, ar._encryptedLocation, deflt._encryptedLocation, pExtr);
		TypeHandler<bool>::extract(pos++, ar._verifiedEmail, deflt._verifiedEmail, pExtr);
		TypeHandler<bool>::extract(pos++, ar._verifiedPhoneNumber, deflt._verifiedPhoneNumber, pExtr);
		TypeHandler<bool>::extract(pos++, ar._twoFactorAuthentication, deflt._twoFactorAuthentication, pExtr);
		TypeHandler<Poco::Timestamp>::extract(pos++, ar._registration, deflt._registration, pExtr);
}

	static void prepare(std::size_t pos, const DatabaseSystem::User& ar, AbstractPreparator::Ptr pPrep)
	{
		TypeHandler<std::string>::prepare(pos++, ar._hashedPassword, pPrep);
		TypeHandler<std::string>::prepare(pos++, ar._salt, pPrep);
		TypeHandler<std::string>::prepare(pos++, ar._encryptedFirstName, pPrep);
		TypeHandler<std::string>::prepare(pos++, ar._encryptedLastName, pPrep);
		TypeHandler<std::string>::prepare(pos++, ar._encryptedPrivateKey, pPrep);
		TypeHandler<std::string>::prepare(pos++, ar._encryptedPhone, pPrep);
		TypeHandler<std::string>::prepare(pos++, ar._encryptedLocation, pPrep);
		TypeHandler<bool>::prepare(pos++, ar._verifiedEmail, pPrep);
		TypeHandler<bool>::prepare(pos++, ar._verifiedPhoneNumber, pPrep);
		TypeHandler<bool>::prepare(pos++, ar._twoFactorAuthentication, pPrep);
		TypeHandler<Poco::Timestamp>::prepare(pos++, ar._registration, pPrep);
	}
};


} } // namespace Poco::Data


#endif // DatabaseSystem_User_INCLUDED
