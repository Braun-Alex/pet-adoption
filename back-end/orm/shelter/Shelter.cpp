//
// Shelter.cpp
//
// This file has been generated from pet_adoption.xml. Do not edit.
//


#include "DatabaseSystem/Shelter.h"


using namespace std::string_literals;
using namespace Poco::Data::Keywords;


namespace DatabaseSystem {


Shelter::Shelter(ID id):
	Poco::ActiveRecord::ActiveRecord<std::string>(id)
{
}


Shelter::Shelter(const Shelter& other):
	Poco::ActiveRecord::ActiveRecord<std::string>(other),
	_email(other._email),
	_hashedPassword(other._hashedPassword),
	_salt(other._salt),
	_encryptedPrivateKey(other._encryptedPrivateKey),
	_phone(other._phone),
	_location(other._location),
	_headFirstName(other._headFirstName),
	_headLastName(other._headLastName),
	_verifiedEmail(other._verifiedEmail),
	_verifiedPhoneNumber(other._verifiedPhoneNumber),
	_registration(other._registration)
{
}


Shelter::Ptr Shelter::find(Poco::ActiveRecord::Context::Ptr pContext, const ID& id)
{
	Poco::ActiveRecord::StatementPlaceholderProvider::Ptr pSPP(pContext->statementPlaceholderProvider());
	Shelter::Ptr pObject(new Shelter);

	pContext->session()
		<< "SELECT name, email, hashedPassword, salt, encryptedPrivateKey, phone, location, headFirstName, headLastName, verifiedEmail, verifiedPhoneNumber, registration"
		<< "  FROM shelters"
		<< "  WHERE name = " << pSPP->next(),
		into(pObject->mutableID()),
		into(*pObject),
		bind(id),
		now;

	return withContext(pObject, pContext);
}


void Shelter::insert()
{
	Poco::ActiveRecord::StatementPlaceholderProvider::Ptr pSPP(context()->statementPlaceholderProvider());

	context()->session()
		<< "INSERT INTO shelters (name, email, hashedPassword, salt, encryptedPrivateKey, phone, location, headFirstName, headLastName, verifiedEmail, verifiedPhoneNumber, registration)"
		<< "  VALUES (" << pSPP->next() << ", " << pSPP->next() << ", " << pSPP->next() << ", " << pSPP->next() << ", " << pSPP->next() << ", " << pSPP->next() << ", " << pSPP->next() << ", " << pSPP->next() << ", " << pSPP->next() << ", " << pSPP->next() << ", " << pSPP->next() << ", " << pSPP->next() << ")",
		bind(id()),
		use(*this),
		now;
}


void Shelter::update()
{
	Poco::ActiveRecord::StatementPlaceholderProvider::Ptr pSPP(context()->statementPlaceholderProvider());

	context()->session()
		<< "UPDATE shelters"
		<< "  SET email = " << pSPP->next() << ", hashedPassword = " << pSPP->next() << ", salt = " << pSPP->next() << ", encryptedPrivateKey = " << pSPP->next() << ", phone = " << pSPP->next() << ", location = " << pSPP->next() << ", headFirstName = " << pSPP->next() << ", headLastName = " << pSPP->next() << ", verifiedEmail = " << pSPP->next() << ", verifiedPhoneNumber = " << pSPP->next() << ", registration = " << pSPP->next()
		<< "  WHERE name = " << pSPP->next(),
		use(*this),
		bind(id()),
		now;
}


void Shelter::remove()
{
	Poco::ActiveRecord::StatementPlaceholderProvider::Ptr pSPP(context()->statementPlaceholderProvider());

	context()->session()
		<< "DELETE FROM shelters"
		<< "  WHERE name = " << pSPP->next(),
		bind(id()),
		now;
}


const std::vector<std::string>& Shelter::columns()
{
	static const std::vector<std::string> cols =
	{
		"name"s,
		"email"s,
		"hashedPassword"s,
		"salt"s,
		"encryptedPrivateKey"s,
		"phone"s,
		"location"s,
		"headFirstName"s,
		"headLastName"s,
		"verifiedEmail"s,
		"verifiedPhoneNumber"s,
		"registration"s,
	};

	return cols;
}


const std::string& Shelter::table()
{
	static const std::string t = "shelters";
	return t;
}


} // namespace DatabaseSystem
