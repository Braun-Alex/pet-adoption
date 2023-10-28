//
// Animal.h
//
// This file has been generated from pet_adoption.xml. Do not edit.
//


#ifndef DatabaseSystem_Animal_INCLUDED
#define DatabaseSystem_Animal_INCLUDED


#include "Poco/ActiveRecord/ActiveRecord.h"
#include "DatabaseSystem/Shelter.h"


namespace DatabaseSystem {


class Animal: public Poco::ActiveRecord::ActiveRecord<std::string>
{
public:
	using Ptr = Poco::AutoPtr<Animal>;

	explicit Animal(ID id);
	Animal() = default;
	Animal(const Animal& other);
	~Animal() = default;

	const std::string& name() const;
	Animal& name(const std::string& value);

	const std::string& species() const;
	Animal& species(const std::string& value);

	const Poco::Timestamp& birthdate() const;
	Animal& birthdate(const Poco::Timestamp& value);

	const std::string& location() const;
	Animal& location(const std::string& value);

	char gender() const;
	Animal& gender(char value);

	const std::string& breed() const;
	Animal& breed(const std::string& value);

	const std::string& color() const;
	Animal& color(const std::string& value);

	bool sterilization() const;
	Animal& sterilization(bool value);

	bool vaccination() const;
	Animal& vaccination(bool value);

	const std::string& story() const;
	Animal& story(const std::string& value);

	const std::string& character() const;
	Animal& character(const std::string& value);

	const std::string& wishes() const;
	Animal& wishes(const std::string& value);

	const std::string& salt() const;
	Animal& salt(const std::string& value);

	const std::string& status() const;
	Animal& status(const std::string& value);

	Shelter::Ptr shelterName() const;
	const std::string& shelterNameID() const;
	Animal& shelterName(Shelter::Ptr pObject);
	Animal& shelterNameID(const std::string& id);

	static Ptr find(Poco::ActiveRecord::Context::Ptr pContext, const ID& id);

	void insert();
	void update();
	void remove();

	static const std::vector<std::string>& columns();
	static const std::string& table();

private:
	std::string _name;
	std::string _species;
	Poco::Timestamp _birthdate;
	std::string _location;
	char _gender = 0;
	std::string _breed;
	std::string _color;
	bool _sterilization = false;
	bool _vaccination = false;
	std::string _story;
	std::string _character;
	std::string _wishes;
	std::string _salt;
	std::string _status;
	std::string _shelterName;

	friend class Poco::Data::TypeHandler<Animal>;
};


inline const std::string& Animal::name() const
{
	return _name;
}


inline Animal& Animal::name(const std::string& value)
{
	_name = value;
	return *this;
}


inline const std::string& Animal::species() const
{
	return _species;
}


inline Animal& Animal::species(const std::string& value)
{
	_species = value;
	return *this;
}


inline const Poco::Timestamp& Animal::birthdate() const
{
	return _birthdate;
}


inline Animal& Animal::birthdate(const Poco::Timestamp& value)
{
	_birthdate = value;
	return *this;
}


inline const std::string& Animal::location() const
{
	return _location;
}


inline Animal& Animal::location(const std::string& value)
{
	_location = value;
	return *this;
}


inline char Animal::gender() const
{
	return _gender;
}


inline Animal& Animal::gender(char value)
{
	_gender = value;
	return *this;
}


inline const std::string& Animal::breed() const
{
	return _breed;
}


inline Animal& Animal::breed(const std::string& value)
{
	_breed = value;
	return *this;
}


inline const std::string& Animal::color() const
{
	return _color;
}


inline Animal& Animal::color(const std::string& value)
{
	_color = value;
	return *this;
}


inline bool Animal::sterilization() const
{
	return _sterilization;
}


inline Animal& Animal::sterilization(bool value)
{
	_sterilization = value;
	return *this;
}


inline bool Animal::vaccination() const
{
	return _vaccination;
}


inline Animal& Animal::vaccination(bool value)
{
	_vaccination = value;
	return *this;
}


inline const std::string& Animal::story() const
{
	return _story;
}


inline Animal& Animal::story(const std::string& value)
{
	_story = value;
	return *this;
}


inline const std::string& Animal::character() const
{
	return _character;
}


inline Animal& Animal::character(const std::string& value)
{
	_character = value;
	return *this;
}


inline const std::string& Animal::wishes() const
{
	return _wishes;
}


inline Animal& Animal::wishes(const std::string& value)
{
	_wishes = value;
	return *this;
}


inline const std::string& Animal::salt() const
{
	return _salt;
}


inline Animal& Animal::salt(const std::string& value)
{
	_salt = value;
	return *this;
}


inline const std::string& Animal::status() const
{
	return _status;
}


inline Animal& Animal::status(const std::string& value)
{
	_status = value;
	return *this;
}


inline const std::string& Animal::shelterNameID() const
{
	return _shelterName;
}


inline Animal& Animal::shelterNameID(const std::string& value)
{
	_shelterName = value;
	return *this;
}


} // namespace DatabaseSystem


namespace Poco {
namespace Data {


template <>
class TypeHandler<DatabaseSystem::Animal>
{
public:
	static std::size_t size()
	{
		return 15;
	}

	static void bind(std::size_t pos, const DatabaseSystem::Animal& ar, AbstractBinder::Ptr pBinder, AbstractBinder::Direction dir)
	{
		TypeHandler<std::string>::bind(pos++, ar._name, pBinder, dir);
		TypeHandler<std::string>::bind(pos++, ar._species, pBinder, dir);
		TypeHandler<Poco::Timestamp>::bind(pos++, ar._birthdate, pBinder, dir);
		TypeHandler<std::string>::bind(pos++, ar._location, pBinder, dir);
		TypeHandler<char>::bind(pos++, ar._gender, pBinder, dir);
		TypeHandler<std::string>::bind(pos++, ar._breed, pBinder, dir);
		TypeHandler<std::string>::bind(pos++, ar._color, pBinder, dir);
		TypeHandler<bool>::bind(pos++, ar._sterilization, pBinder, dir);
		TypeHandler<bool>::bind(pos++, ar._vaccination, pBinder, dir);
		TypeHandler<std::string>::bind(pos++, ar._story, pBinder, dir);
		TypeHandler<std::string>::bind(pos++, ar._character, pBinder, dir);
		TypeHandler<std::string>::bind(pos++, ar._wishes, pBinder, dir);
		TypeHandler<std::string>::bind(pos++, ar._salt, pBinder, dir);
		TypeHandler<std::string>::bind(pos++, ar._status, pBinder, dir);
		TypeHandler<std::string>::bind(pos++, ar._shelterName, pBinder, dir);
}

	static void extract(std::size_t pos, DatabaseSystem::Animal& ar, const DatabaseSystem::Animal& deflt, AbstractExtractor::Ptr pExtr)
	{
		TypeHandler<std::string>::extract(pos++, ar._name, deflt._name, pExtr);
		TypeHandler<std::string>::extract(pos++, ar._species, deflt._species, pExtr);
		TypeHandler<Poco::Timestamp>::extract(pos++, ar._birthdate, deflt._birthdate, pExtr);
		TypeHandler<std::string>::extract(pos++, ar._location, deflt._location, pExtr);
		TypeHandler<char>::extract(pos++, ar._gender, deflt._gender, pExtr);
		TypeHandler<std::string>::extract(pos++, ar._breed, deflt._breed, pExtr);
		TypeHandler<std::string>::extract(pos++, ar._color, deflt._color, pExtr);
		TypeHandler<bool>::extract(pos++, ar._sterilization, deflt._sterilization, pExtr);
		TypeHandler<bool>::extract(pos++, ar._vaccination, deflt._vaccination, pExtr);
		TypeHandler<std::string>::extract(pos++, ar._story, deflt._story, pExtr);
		TypeHandler<std::string>::extract(pos++, ar._character, deflt._character, pExtr);
		TypeHandler<std::string>::extract(pos++, ar._wishes, deflt._wishes, pExtr);
		TypeHandler<std::string>::extract(pos++, ar._salt, deflt._salt, pExtr);
		TypeHandler<std::string>::extract(pos++, ar._status, deflt._status, pExtr);
		TypeHandler<std::string>::extract(pos++, ar._shelterName, deflt._shelterName, pExtr);
}

	static void prepare(std::size_t pos, const DatabaseSystem::Animal& ar, AbstractPreparator::Ptr pPrep)
	{
		TypeHandler<std::string>::prepare(pos++, ar._name, pPrep);
		TypeHandler<std::string>::prepare(pos++, ar._species, pPrep);
		TypeHandler<Poco::Timestamp>::prepare(pos++, ar._birthdate, pPrep);
		TypeHandler<std::string>::prepare(pos++, ar._location, pPrep);
		TypeHandler<char>::prepare(pos++, ar._gender, pPrep);
		TypeHandler<std::string>::prepare(pos++, ar._breed, pPrep);
		TypeHandler<std::string>::prepare(pos++, ar._color, pPrep);
		TypeHandler<bool>::prepare(pos++, ar._sterilization, pPrep);
		TypeHandler<bool>::prepare(pos++, ar._vaccination, pPrep);
		TypeHandler<std::string>::prepare(pos++, ar._story, pPrep);
		TypeHandler<std::string>::prepare(pos++, ar._character, pPrep);
		TypeHandler<std::string>::prepare(pos++, ar._wishes, pPrep);
		TypeHandler<std::string>::prepare(pos++, ar._salt, pPrep);
		TypeHandler<std::string>::prepare(pos++, ar._status, pPrep);
		TypeHandler<std::string>::prepare(pos++, ar._shelterName, pPrep);
	}
};


} } // namespace Poco::Data


#endif // DatabaseSystem_Animal_INCLUDED
