//
// Animal.cpp
//
// This file has been generated from pet_adoption.xml. Do not edit.
//


#include "DatabaseSystem/Animal.h"


using namespace std::string_literals;
using namespace Poco::Data::Keywords;


namespace DatabaseSystem {


Animal::Animal(ID id):
	Poco::ActiveRecord::ActiveRecord<std::string>(id)
{
}


Animal::Animal(const Animal& other):
	Poco::ActiveRecord::ActiveRecord<std::string>(other),
	_name(other._name),
	_species(other._species),
	_birthdate(other._birthdate),
	_location(other._location),
	_gender(other._gender),
	_breed(other._breed),
	_color(other._color),
	_sterilization(other._sterilization),
	_vaccination(other._vaccination),
	_story(other._story),
	_character(other._character),
	_wishes(other._wishes),
	_salt(other._salt),
	_status(other._status),
	_shelterName(other._shelterName)
{
}


Shelter::Ptr Animal::shelterName() const
{
	return Shelter::find(context(), _shelterName);
}


Animal& Animal::shelterName(Shelter::Ptr pObject)
{
	if (pObject)
		_shelterName = pObject->id();
	else
		_shelterName = Shelter::INVALID_ID;
	return *this;
}


Animal::Ptr Animal::find(Poco::ActiveRecord::Context::Ptr pContext, const ID& id)
{
	Poco::ActiveRecord::StatementPlaceholderProvider::Ptr pSPP(pContext->statementPlaceholderProvider());
	Animal::Ptr pObject(new Animal);

	pContext->session()
		<< "SELECT id, name, species, birthdate, location, gender, breed, color, sterilization, vaccination, story, character, wishes, salt, status, shelterName"
		<< "  FROM animals"
		<< "  WHERE id = " << pSPP->next(),
		into(pObject->mutableID()),
		into(*pObject),
		bind(id),
		now;

	return withContext(pObject, pContext);
}


void Animal::insert()
{
	Poco::ActiveRecord::StatementPlaceholderProvider::Ptr pSPP(context()->statementPlaceholderProvider());

	context()->session()
		<< "INSERT INTO animals (id, name, species, birthdate, location, gender, breed, color, sterilization, vaccination, story, character, wishes, salt, status, shelterName)"
		<< "  VALUES (" << pSPP->next() << ", " << pSPP->next() << ", " << pSPP->next() << ", " << pSPP->next() << ", " << pSPP->next() << ", " << pSPP->next() << ", " << pSPP->next() << ", " << pSPP->next() << ", " << pSPP->next() << ", " << pSPP->next() << ", " << pSPP->next() << ", " << pSPP->next() << ", " << pSPP->next() << ", " << pSPP->next() << ", " << pSPP->next() << ", " << pSPP->next() << ")",
		bind(id()),
		use(*this),
		now;
}


void Animal::update()
{
	Poco::ActiveRecord::StatementPlaceholderProvider::Ptr pSPP(context()->statementPlaceholderProvider());

	context()->session()
		<< "UPDATE animals"
		<< "  SET name = " << pSPP->next() << ", species = " << pSPP->next() << ", birthdate = " << pSPP->next() << ", location = " << pSPP->next() << ", gender = " << pSPP->next() << ", breed = " << pSPP->next() << ", color = " << pSPP->next() << ", sterilization = " << pSPP->next() << ", vaccination = " << pSPP->next() << ", story = " << pSPP->next() << ", character = " << pSPP->next() << ", wishes = " << pSPP->next() << ", salt = " << pSPP->next() << ", status = " << pSPP->next() << ", shelterName = " << pSPP->next()
		<< "  WHERE id = " << pSPP->next(),
		use(*this),
		bind(id()),
		now;
}


void Animal::remove()
{
	Poco::ActiveRecord::StatementPlaceholderProvider::Ptr pSPP(context()->statementPlaceholderProvider());

	context()->session()
		<< "DELETE FROM animals"
		<< "  WHERE id = " << pSPP->next(),
		bind(id()),
		now;
}


const std::vector<std::string>& Animal::columns()
{
	static const std::vector<std::string> cols =
	{
		"id"s,
		"name"s,
		"species"s,
		"birthdate"s,
		"location"s,
		"gender"s,
		"breed"s,
		"color"s,
		"sterilization"s,
		"vaccination"s,
		"story"s,
		"character"s,
		"wishes"s,
		"salt"s,
		"status"s,
		"shelterName"s,
	};

	return cols;
}


const std::string& Animal::table()
{
	static const std::string t = "animals";
	return t;
}


} // namespace DatabaseSystem
