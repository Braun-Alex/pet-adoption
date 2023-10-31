//
// User.cpp
//
// This file has been generated from pet_adoption.xml. Do not edit.
//


#include "User.h"


using namespace std::string_literals;
using namespace Poco::Data::Keywords;


namespace DatabaseSystem {


User::User(ID id):
	Poco::ActiveRecord::ActiveRecord<std::string>(id)
{
}


User::User(const User& other):
	Poco::ActiveRecord::ActiveRecord<std::string>(other),
	_hashedPassword(other._hashedPassword),
	_salt(other._salt),
	_encryptedFirstName(other._encryptedFirstName),
	_encryptedLastName(other._encryptedLastName),
	_encryptedPrivateKey(other._encryptedPrivateKey),
	_encryptedPhone(other._encryptedPhone),
	_encryptedLocation(other._encryptedLocation),
	_verifiedEmail(other._verifiedEmail),
	_verifiedPhoneNumber(other._verifiedPhoneNumber),
	_twoFactorAuthentication(other._twoFactorAuthentication),
	_registration(other._registration)
{
}


User::Ptr User::find(Poco::ActiveRecord::Context::Ptr pContext, const ID& id)
{
	Poco::ActiveRecord::StatementPlaceholderProvider::Ptr pSPP(pContext->statementPlaceholderProvider());
	User::Ptr pObject(new User);

	pContext->session()
		<< "SELECT hashedEmail, hashedPassword, salt, encryptedFirstName, encryptedLastName, encryptedPrivateKey, encryptedPhone, encryptedLocation, verifiedEmail, verifiedPhoneNumber, twoFactorAuthentication, registration"
		<< "  FROM users"
		<< "  WHERE hashedEmail = " << pSPP->next(),
		into(pObject->mutableID()),
		into(*pObject),
		bind(id),
		now;

	return withContext(pObject, pContext);
}


void User::insert()
{
	Poco::ActiveRecord::StatementPlaceholderProvider::Ptr pSPP(context()->statementPlaceholderProvider());

	context()->session()
		<< "INSERT INTO users (hashedEmail, hashedPassword, salt, encryptedFirstName, encryptedLastName, encryptedPrivateKey, encryptedPhone, encryptedLocation, verifiedEmail, verifiedPhoneNumber, twoFactorAuthentication, registration)"
		<< "  VALUES (" << pSPP->next() << ", " << pSPP->next() << ", " << pSPP->next() << ", " << pSPP->next() << ", " << pSPP->next() << ", " << pSPP->next() << ", " << pSPP->next() << ", " << pSPP->next() << ", " << pSPP->next() << ", " << pSPP->next() << ", " << pSPP->next() << ", " << pSPP->next() << ")",
		bind(id()),
		use(*this),
		now;
}


void User::update()
{
	Poco::ActiveRecord::StatementPlaceholderProvider::Ptr pSPP(context()->statementPlaceholderProvider());

	context()->session()
		<< "UPDATE users"
		<< "  SET hashedPassword = " << pSPP->next() << ", salt = " << pSPP->next() << ", encryptedFirstName = " << pSPP->next() << ", encryptedLastName = " << pSPP->next() << ", encryptedPrivateKey = " << pSPP->next() << ", encryptedPhone = " << pSPP->next() << ", encryptedLocation = " << pSPP->next() << ", verifiedEmail = " << pSPP->next() << ", verifiedPhoneNumber = " << pSPP->next() << ", twoFactorAuthentication = " << pSPP->next() << ", registration = " << pSPP->next()
		<< "  WHERE hashedEmail = " << pSPP->next(),
		use(*this),
		bind(id()),
		now;
}


void User::remove()
{
	Poco::ActiveRecord::StatementPlaceholderProvider::Ptr pSPP(context()->statementPlaceholderProvider());

	context()->session()
		<< "DELETE FROM users"
		<< "  WHERE hashedEmail = " << pSPP->next(),
		bind(id()),
		now;
}


const std::vector<std::string>& User::columns()
{
	static const std::vector<std::string> cols =
	{
		"hashedEmail"s,
		"hashedPassword"s,
		"salt"s,
		"encryptedFirstName"s,
		"encryptedLastName"s,
		"encryptedPrivateKey"s,
		"encryptedPhone"s,
		"encryptedLocation"s,
		"verifiedEmail"s,
		"verifiedPhoneNumber"s,
		"twoFactorAuthentication"s,
		"registration"s,
	};

	return cols;
}


const std::string& User::table()
{
	static const std::string t = "users";
	return t;
}


} // namespace DatabaseSystem
